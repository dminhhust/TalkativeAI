from app.models.transcription_model import *
from app.utils.audio_utils import *


def process_audio(file_bytes):

    path = save_temp_audio(file_bytes)

    text = transcribe_audio(path)

    delete_temp_audio(path)

    return text
