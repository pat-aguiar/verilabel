from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# Engine handles the connection pool to PostgreSQL
engine = create_engine(settings.DATABASE_URL, echo=True) 

def init_db():
    # Creates the tables based on the models defined in app.models
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session