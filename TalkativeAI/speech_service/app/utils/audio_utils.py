import os
import uuid

UPLOAD_DIR = "temp_audio"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_temp_audio(file):

    filename = f"{uuid.uuid4()}.wav"

    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        buffer.write(file)

    return filepath


def delete_temp_audio(filepath):

    if os.path.exists(filepath):
        os.remove(filepath)
