from fastapi import FastAPI
from app.routes.speech_routes import router

app = FastAPI(
    title="Speech Service"
)

app.include_router(router, prefix="/speech")
