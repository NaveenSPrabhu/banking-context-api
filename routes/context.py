from fastapi import APIRouter, HTTPException
from database import get_branch, get_all_branches
from services.session import create_session, get_session, update_session_language
import uuid

router = APIRouter()

@router.get("/context/{branch_id}")
def get_context(branch_id: str):
    branch = get_branch(branch_id)
    
    if branch is None:
        raise HTTPException(
            status_code=404,
            detail="Branch not found"
        )
    
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

@router.get("/branches")
def get_branches():
    branches = get_all_branches()
    return {"branches": branches}

@router.put("/session/{session_id}/language")
def update_language(session_id: str, language: str):
    session = update_session_language(session_id, language)
    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    return session

@router.get("/session/{session_id}")
def get_session_details(session_id: str):
    session = get_session(session_id)
    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    return session