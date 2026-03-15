from fastapi import FastAPI
from app.routes.conversation_routes import router

app = FastAPI(
    title="Conversation Service"
)

app.include_router(router, prefix="/conversation")
