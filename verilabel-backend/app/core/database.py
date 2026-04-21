from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# engine handles the connection pool to PostgreSQL
engine = create_engine(settings.DATABASE_URL, echo=True) 

def init_db():
    # This creates the tables based on our models (Step 2)
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session