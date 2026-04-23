from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.context import router as context_router

app = FastAPI(
    title="Banking Context API",
    description="QR Context Aware Module",
    version="1.0.0"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(context_router)

@app.get("/")
def home():
    return {"message": "Banking Context API is running!"}