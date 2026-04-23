from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# Encode password with special characters
password = quote_plus("Naveen@nitte")

# Database connection
DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/banking_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_branch(branch_id: str):
    with SessionLocal() as session:
        result = session.execute(
            text("SELECT * FROM branches WHERE branch_id = :branch_id"),
            {"branch_id": branch_id}
        ).fetchone()
        
        if result is None:
            return None
            
        return {
            "branch_id": result[0],
            "location": result[1],
            "available_services": result[2],
            "language_supported": result[3]
        }

def get_all_branches():
    with SessionLocal() as session:
        results = session.execute(
            text("SELECT * FROM branches")
        ).fetchall()
        return results