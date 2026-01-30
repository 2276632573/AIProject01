from sqlmodel import create_engine, Session
import os   

DB = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

engine = None
def get_engine():
    global engine
    if engine is None:
        db_url = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}"
        engine = create_engine(db_url, echo=True)
    return engine

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e