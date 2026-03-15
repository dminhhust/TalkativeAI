from fastapi import FastAPI
from app.routes.vision_routes import router

app = FastAPI(
    title="Vision Service"
)

app.include_router(router, prefix="/vision")
