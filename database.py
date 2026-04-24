from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://banking_db_pl3j_user:dRwzXCqlW3qu1K4ad1IfaE9wYZjUoM4Q@dpg-d7l51ngg4nts73fkg35g-a.oregon-postgres.render.com/banking_db_pl3j"

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
            "available_services": list(result[2]),
            "language_supported": list(result[3])
        }

def get_all_branches():
    with SessionLocal() as session:
        results = session.execute(
            text("SELECT * FROM branches")
        ).fetchall()
        return [
            {
                "branch_id": row[0],
                "location": row[1],
                "available_services": list(row[2]),
                "language_supported": list(row[3])
            }
            for row in results
        ]