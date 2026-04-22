from sqlmodel import Session, select
from app.core.database import engine
from app.models.compliance import Regulation

def seed_data():
    # Common Prop 65 & FDA thresholds (Simplified for MVP)
    regulations = [
        Regulation(name="Prop 65", chemical_name="lead", threshold_ppm=0.5, category="Heavy Metal"),
        Regulation(name="Prop 65", chemical_name="mercury", threshold_ppm=0.1, category="Heavy Metal"),
        Regulation(name="Prop 65", chemical_name="arsenic", threshold_ppm=10.0, category="Heavy Metal"),
        Regulation(name="FDA Limit", chemical_name="cadmium", threshold_ppm=0.3, category="Heavy Metal"),
    ]

    with Session(engine) as session:
        for reg in regulations:
            # Check if it already exists to avoid duplicates
            statement = select(Regulation).where(Regulation.chemical_name == reg.chemical_name)
            existing = session.exec(statement).first()
            if not existing:
                session.add(reg)
        
        session.commit()
        print("✅ Database seeded with regulatory thresholds.")

if __name__ == "__main__":
    seed_data()