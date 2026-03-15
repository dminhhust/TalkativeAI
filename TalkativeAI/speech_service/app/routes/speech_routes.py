from fastapi import APIRouter, UploadFile
from app.services.speech_service import *

router = APIRouter()


@router.post("/transcribe")
async def transcribe(file: UploadFile):

    audio_bytes = await file.read()

    text = process_audio(audio_bytes)

    return {
        "transcript": text
    }
