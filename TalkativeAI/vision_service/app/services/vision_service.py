from app.utils.image_utils import *
from app.models.emotion_model import *


def process_frame(frame_bytes):

    image = bytes_to_image(frame_bytes)

    emotion, confidence = analyze_emotion(image)

    return {
        "emotion": emotion,
        "confidence": confidence
    }
