import uuid

# In-memory session storage (simple for now)
sessions = {}

def create_session(branch_id: str, location: str, services: list, languages: list):
    session_id = str(uuid.uuid4())
    
    sessions[session_id] = {
        "session_id": session_id,
        "branch_id": branch_id,
        "location": location,
        "available_services": services,
        "language_supported": languages,
        "language": None,
        "state": "LANGUAGE_SELECTION",
        "mode": "2-way"
    }
    
    return sessions[session_id]

def get_session(session_id: str):
    if session_id not in sessions:
        return None
    return sessions[session_id]

def update_session(session_id: str, updates: dict):
    if session_id not in sessions:
        return None
    sessions[session_id].update(updates)
    return sessions[session_id]

def delete_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
        return True
    return False
