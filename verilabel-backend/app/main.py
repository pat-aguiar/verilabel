from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.api.endpoints import reports

from app.core.config import settings

app = FastAPI(title="VeriLabel API", version="0.1.0")

# Enable CORS for React frontend (securely reading from env)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "active", "service": "VeriLabel"}

app.include_router(reports.router, prefix="/api/v1", tags=["Reports"])