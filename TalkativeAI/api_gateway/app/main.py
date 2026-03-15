from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router
from app.routes.conversation_routes import router as conv_router
from app.routes.session_routes import router as session_router

app = FastAPI(
    title="API Gateway",
    version="1.0"
)

app.include_router(auth_router, prefix="/auth")
app.include_router(conv_router, prefix="/conversation")
app.include_router(session_router, prefix="/session")
