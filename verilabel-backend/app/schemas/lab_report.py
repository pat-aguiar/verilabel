from pydantic import BaseModel
from typing import Dict, Optional

class LabReportCreate(BaseModel):
    brand_name: str

class LabReportResponse(BaseModel):
    report_id: int
    status: str
    data: Dict

    class Config:
        from_attributes = True