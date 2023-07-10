from fastapi import FastAPI, Depends, UploadFile, File
from sqlalchemy.orm import Session
import app.services as _services
import app.models as models
import app.crud as crud
from app.db import engine
import tempfile
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def index():
    return {"Message": "Success"}

@app.post("/upload_sheet")
def create_data(file: UploadFile, db: Session = Depends(_services.get_session)):
    # contents = file.file.read()
    # with open(file.filename, "wb") as f:
    #     f.write(contents)
    # crud.upload_sheet(db, file.filename)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        contents = file.file.read()
        temp_file.write(contents)
        temp_file.flush()
        temp_file.seek(0)
        
        crud.upload_sheet(db, temp_file.name)
        temp_file.close()
        os.remove(temp_file.name)
    return {"message": "file uploaded successfully"}

@app.get("/top_gainers/{country}")
def get_gainers(country: str, db: Session = Depends(_services.get_session)):
    winners = crud.get_gainers(db, country)
    return {"gainers":winners}

@app.get("/top_losers/{country}")
def get_losers(country: str, db: Session = Depends(_services.get_session)):
    losers = crud.get_losers(db, country)
    return {"losers": losers}

@app.get("/top_traders/{country}")
def get_traders(country: str, db: Session = Depends(_services.get_session)):
    traders = crud.get_traders(db, country)
    return {"traders": traders}

@app.get("/indices/{country}")
def get_indices(country: str, db: Session = Depends(_services.get_session)):
    indices = crud.get_indices(db, country)
    return {"indices": indices}



