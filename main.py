from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.context import router as context_router

app = FastAPI(
    title="Banking Context API",
    description="QR Context Aware Module",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(context_router)

@app.get("/")
def home():
    return {"message": "Banking Context API is running!"}