from fastapi import APIRouter, HTTPException
from database import get_branch
from services.session import create_session
import uuid

router = APIRouter()

@router.get("/context/{branch_id}")
def get_context(branch_id: str):
    # Get branch from database
    branch = get_branch(branch_id)
    
    # Check if branch exists
    if branch is None:
        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )
    
    # Create session
    session = create_session(
        branch_id=branch["branch_id"],
        location=branch["location"],
        services=branch["available_services"],
        languages=branch["language_supported"]
    )
    
    return {
        "session_id": session["session_id"],
        "branch_id": branch["branch_id"],
        "location": branch["location"],
        "available_services": branch["available_services"],
        "language_supported": branch["language_supported"],
        "state": "LANGUAGE_SELECTION"
    }