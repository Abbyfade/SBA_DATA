from db import Base, engine, SessionLocal

def get_session():
    session = SessionLocal()
    try: 
        yield session
    finally:
        session.close()