import uuid
from sqlalchemy import text
from database import SessionLocal

def create_session(branch_id: str, location: str, services: list, languages: list):
    session_id = str(uuid.uuid4())
    
    with SessionLocal() as db:
        db.execute(
            text("""
                INSERT INTO sessions (session_id, branch_id, language, state, mode)
                VALUES (:session_id, :branch_id, :language, :state, :mode)
            """),
            {
                "session_id": session_id,
                "branch_id": branch_id,
                "language": None,
                "state": "LANGUAGE_SELECTION",
                "mode": "2-way"
            }
        )
        db.commit()
    
    return {
        "session_id": session_id,
        "branch_id": branch_id,
        "location": location,
        "available_services": services,
        "language_supported": languages,
        "language": None,
        "state": "LANGUAGE_SELECTION",
        "mode": "2-way"
    }

def get_session(session_id: str):
    with SessionLocal() as db:
        result = db.execute(
            text("SELECT * FROM sessions WHERE session_id = :session_id"),
            {"session_id": session_id}
        ).fetchone()
        
        if result is None:
            return None
            
        return {
            "session_id": result[0],
            "branch_id": result[1],
            "language": result[2],
            "state": result[3],
            "mode": result[4]
        }

def update_session_language(session_id: str, language: str):
    with SessionLocal() as db:
        db.execute(
            text("""
                UPDATE sessions 
                SET language = :language, state = :state
                WHERE session_id = :session_id
            """),
            {
                "session_id": session_id,
                "language": language,
                "state": "SERVICE_SELECTION"
            }
        )
        db.commit()
    return get_session(session_id)