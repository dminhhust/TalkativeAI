from fastapi import FastAPI
from app.routes.auth_routes import router

app = FastAPI(
    title="Auth Service",
    version="1.0"
)

app.include_router(router, prefix="/auth")
