from fastapi import FastAPI
from app.routes.analytics_routes import router

app = FastAPI(
    title="Analytics Service"
)

app.include_router(router, prefix="/analytics")
