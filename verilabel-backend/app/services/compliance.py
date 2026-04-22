from sqlmodel import Session, select
from app.models.compliance import Regulation, LabReport
from app.core.database import engine

class ComplianceEngine:
    @staticmethod
    def check_compliance(report: LabReport, db: Session):
        """
        Compares extracted_data against Regulation thresholds.
        Updates report.status to 'compliant' or 'non-compliant'.
        """
        extracted = report.extracted_data
        is_compliant = True
        
        # Fetch all regulations to compare
        regulations = db.exec(select(Regulation)).all()
        
        for reg in regulations:
            # Check if the extracted data contains this chemical
            if reg.chemical_name in extracted:
                actual_value = extracted[reg.chemical_name]
                if actual_value > reg.threshold_ppm:
                    is_compliant = False
                    break
        
        report.status = "compliant" if is_compliant else "non-compliant"
        db.add(report)
        db.commit()
        db.refresh(report)
        return report