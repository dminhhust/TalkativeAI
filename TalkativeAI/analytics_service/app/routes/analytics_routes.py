from fastapi import APIRouter
from app.schemas.analytics_schema import *
from app.services.analytics_service import *

router = APIRouter()


@router.post("/update")
def update_metrics(data: AnalyticsRequest):

    result = analyze_session(data)

    return result
