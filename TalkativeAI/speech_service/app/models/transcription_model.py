import whisper
from app.config import *

print("Loading Whisper model...")

model = whisper.load_model(MODEL_SIZE)

print("Whisper model loaded")


def transcribe_audio(file_path):

    result = model.transcribe(file_path)

    return result["text"]
