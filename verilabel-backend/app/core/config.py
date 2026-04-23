import os

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Render sets 'postgres://' but SQLAlchemy requires 'postgresql://'
    _db_url = os.getenv("DATABASE_URL", "sqlite:///./verilabel.db")
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
        
    DATABASE_URL: str = _db_url
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:5173")

settings = Settings()
