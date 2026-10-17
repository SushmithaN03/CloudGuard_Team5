from fastapi import FastAPI

from src.api.routes.auth import router as auth_router

from src.core.database import Base
from src.core.database import engine

from src.models.user import User
from src.models.subscription import Subscription

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CloudGuard",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "CloudGuard API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }