from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
import app.models

from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GlitrAI Content Engine",
    description="Mini Content Engine for AI Product Images",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://glitter-ai-assignment-1.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register all routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to GlitrAI Content Engine 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/about")
def about():
    return {
        "project": "GlitrAI Assignment",
        "developer": "Your Name"
    }