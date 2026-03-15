from app.services.speech_metrics import *
from app.services.emotion_metrics import *
from app.services.text_metrics import *
from app.utils.scoring_utils import *
from app.models.performance_model import *


def analyze_session(data):

    transcript = data.transcript
    emotions = data.emotions
    duration = data.duration_seconds

    clarity = clarity_score(transcript)

    confidence = compute_confidence_score(emotions)

    structure = structure_score(transcript)

    overall = overall_score(clarity, confidence, structure)

    save_performance(
        data.user_id,
        data.session_id,
        clarity,
        confidence,
        structure,
        overall
    )

    return {
        "clarity_score": clarity,
        "confidence_score": confidence,
        "structure_score": structure,
        "overall_score": overall
    }
