from typing import Optional, Dict
from sqlmodel import SQLModel, Field, JSON, Column
from datetime import datetime

class Regulation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # e.g., "California Prop 65"
    chemical_name: str             # e.g., "lead"
    threshold_ppm: float           # Parts Per Million limit
    category: str                  # e.g., "Heavy Metal"

class LabReport(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    brand_name: str = Field(index=True)
    upload_date: datetime = Field(default_factory=datetime.utcnow)
    
    # Store the AI's raw extraction as JSON for flexibility
    # e.g., {"lead_ppm": 0.02, "mercury_ppm": 0.001}
    extracted_data: Dict = Field(default={}, sa_column=Column(JSON))
    
    status: str = Field(default="pending") # pending, compliant, non-compliant