from pydantic import BaseModel
from typing import Dict, Optional

class LabReportCreate(BaseModel):
    brand_name: str

class LabReportResponse(BaseModel):
    id: int
    filename: str
    status: str
    extracted_data: Dict
    compliance_summary: Optional[str] = None

    class Config:
        from_attributes = True