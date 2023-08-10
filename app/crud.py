from sqlalchemy.orm import Session
import app.models as models
import pandas as pd
import os

def get_gainers(db: Session, country:str):
    return db.query(models.TopGainers).filter(models.TopGainers.country==country).all()

def get_losers(db: Session, country:str):
    return db.query(models.TopLosers).filter(models.TopLosers.country==country).all()

def get_traders(db: Session, country:str):
    return db.query(models.TopTraders).filter(models.TopTraders.country==country).all()

def get_indices(db: Session, country:str):
    return db.query(models.Indices).filter(models.Indices.country==country).all()

def create_gainer(db: Session, date:str, country:str, number: int, code: str, opening_price: float, closing_price: float, percent_change: float):
    db_winner = models.TopGainers(date=date, country=country, number=number, code=code,
                                  opening_price=opening_price, closing_price=closing_price, percent_change=percent_change)
    db.add(db_winner)
    db.commit()
    db.refresh

def create_loser(db: Session, date:str, country:str, number: int, code: str, opening_price: float, closing_price: float, percent_change: float):
    db_loser = models.TopLosers(date=date, country=country, number=number, code=code,
                                  opening_price=opening_price, closing_price=closing_price, percent_change=percent_change)
    db.add(db_loser)
    db.commit()
    db.refresh

def create_trader(db: Session, date:str, country:str, number: int, exchange_code: str, opening_price: float, closing_price: float, volume: float):
    db_trader= models.TopTraders(date=date, country=country, number=number, exchange_code=exchange_code,
                                  opening_price=opening_price, closing_price=closing_price, volume=volume)
    db.add(db_trader)
    db.commit()
    db.refresh

def create_indices(db: Session, date:str, exchange_code: str, country: str, previous_value: float, index_value: float, percent_change: float):
    db_indices = models.Indices(date=date, exchange_code=exchange_code, country=country, 
                                  previous_value=previous_value, index_value=index_value, percent_change=percent_change)
    db.add(db_indices)
    db.commit()
    db.refresh

def update_top_gainers(db, dataframe):
    dataframe = dataframe[dataframe.notna().all(axis=1)]
    db.query(models.TopGainers).delete()
    db.commit()
    for row, col in dataframe.iterrows():
        create_gainer(db, col['Date'], col["Country"], col["No"], col["Code"], col["Opening Price"], col["Closing Price"], col["Change %"])

def update_top_losers(db, dataframe):
    dataframe = dataframe[dataframe.notna().all(axis=1)]
    db.query(models.TopLosers).delete()
    db.commit()
    for row, col in dataframe.iterrows():
        create_loser(db, col['Date'], col["Country"], col["No"], col["Code"], col["Opening Price"], col["Closing Price"], col["Change %"])
        
def update_top_traders(db, dataframe):
    dataframe = dataframe[dataframe.notna().all(axis=1)]
    db.query(models.TopTraders).delete()
    db.commit()
    for row, col in dataframe.iterrows():
        create_trader(db, col['Date'], col["Country"], col["No"], col["Code"], col["Opening Price"], col["Closing Price"], col["Volume"])
        
def update_indices(db, dataframe):
    dataframe = dataframe[dataframe.notna().all(axis=1)]
    db.query(models.Indices).delete()
    db.commit()
    for row, col in dataframe.iterrows():
        create_indices(db, col['Date'], col["Exchange Code"], col["Country"], col["Previous Value"], col["Index Value"], col["Change %"])
        
        

def upload_sheet(db:Session, excel_sheet: str, temp_file):
    file_path = excel_sheet
    data = pd.read_excel(file_path, sheet_name=None)
    top_gainers = data.get("Top Gainers")
    top_losers = data.get("Top Losers")
    top_traders = data.get("Top Traders")
    indices = data.get("Indices")

    top_gainers["Date"] = pd.to_datetime(top_gainers['Date']).dt.strftime('%d/%b/%Y').str.upper()
    top_losers["Date"] = pd.to_datetime(top_losers["Date"]).dt.strftime('%d/%b/%Y').str.upper()
    top_traders["Date"] = pd.to_datetime(top_traders["Date"]).dt.strftime('%d/%b/%Y').str.upper()
    indices["Date"] = pd.to_datetime(indices["Date"]).dt.strftime('%d/%b/%Y').str.upper()

    for column in top_gainers.columns:
        if pd.api.types.is_numeric_dtype(top_gainers[column]) and (column != "No"):
            top_gainers[column] = [format(i,".2f") for i in top_gainers[column]]

    for column in top_losers.columns:
        if pd.api.types.is_numeric_dtype(top_losers[column]) and (column != "No") :
            top_losers[column] = [format(i,".2f") for i in top_losers[column]]

    for column in top_traders.columns:
        if pd.api.types.is_numeric_dtype(top_traders[column]) and (column != "No"):
            top_traders[column] = [format(i,".2f") for i in top_traders[column]]

    for column in indices.columns:
        if pd.api.types.is_numeric_dtype(indices[column]) and (column != "No"):
            indices[column] = [format(i,".2f") for i in indices[column]]


    # top_gainers['Change %'] = top_gainers['Change %'].round(2)
    # top_losers['Change %'] = top_losers['Change %'].round(2)
    # indices['Change %'] = indices['Change %'].round(2)


    update_top_gainers(db, top_gainers)
    update_top_losers(db, top_losers)
    update_top_traders(db, top_traders)
    update_indices(db, indices)

    temp_file.close()
    os.remove(temp_file.name)


    




