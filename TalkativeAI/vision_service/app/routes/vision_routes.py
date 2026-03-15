from fastapi import APIRouter, UploadFile
from app.services.vision_service import *

router = APIRouter()


@router.post("/emotion")
async def detect_emotion(frame: UploadFile):

    frame_bytes = await frame.read()

    result = process_frame(frame_bytes)

    return result
