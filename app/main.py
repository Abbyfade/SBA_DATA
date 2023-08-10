from fastapi import FastAPI, Depends, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import app.services as _services
import app.schemas as schemas
import app.models as models
import app.crud as crud
from app.db import engine
import tempfile
from typing import List
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"Message": "Success"}

@app.post("/upload_sheet")
def create_data(file: UploadFile, background_tasks: BackgroundTasks, db: Session = Depends(_services.get_session)):
    # contents = file.file.read()
    # with open(file.filename, "wb") as f:
    #     f.write(contents)
    # crud.upload_sheet(db, file.filename)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        contents = file.file.read()
        temp_file.write(contents)
        temp_file.flush()
        temp_file.seek(0)
        background_tasks.add_task(crud.upload_sheet, db, temp_file.name, temp_file)
        # crud.upload_sheet(db, temp_file.name)
        # temp_file.close()
        # os.remove(temp_file.name)
    return {"message": "file uploading in the background, check back in 3 minutes"}

@app.get("/top_gainers/{country}", response_model=List[schemas.Gainer])
def get_gainers(country: str, db: Session = Depends(_services.get_session)):
    gainers = crud.get_gainers(db, country)
    return gainers

@app.get("/top_losers/{country}", response_model=List[schemas.Loser])
def get_losers(country: str, db: Session = Depends(_services.get_session)):
    losers = crud.get_losers(db, country)
    return losers

@app.get("/top_traders/{country}", response_model=List[schemas.Trader])
def get_traders(country: str, db: Session = Depends(_services.get_session)):
    traders = crud.get_traders(db, country)
    return traders

@app.get("/indices/{country}", response_model=List[schemas.Index])
def get_indices(country: str, db: Session = Depends(_services.get_session)):
    indices = crud.get_indices(db, country)
    return indices



