from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db

app = FastAPI(title="VeriLabel API", version="0.1.0")

# Enable CORS for our React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Tighten this for production
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