from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.models.compliance import LabReport
from app.services.extraction import ExtractionService
from app.services.compliance import ComplianceEngine
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_lab_report(
    brand_name: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_session)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # 1. Read file
    content = await file.read()
    
    # 2. Extract Text & Parse with AI
    try:
        raw_text = ExtractionService.extract_text_from_pdf(content)
        extracted_json = ExtractionService.parse_with_ai(raw_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Extraction failed: {str(e)}")

    # 3. Save initial report to DB
    new_report = LabReport(
        filename=file.filename,
        brand_name=brand_name,
        extracted_data=extracted_json
    )
    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    # 4. Run Compliance Engine
    processed_report = ComplianceEngine.check_compliance(new_report, db)

    return {
        "report_id": processed_report.id,
        "status": processed_report.status,
        "data": processed_report.extracted_data
    }