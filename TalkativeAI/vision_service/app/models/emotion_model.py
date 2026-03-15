from deepface import DeepFace

print("Loading emotion model...")

def analyze_emotion(frame):

    result = DeepFace.analyze(
        img_path=frame,
        actions=["emotion"],
        enforce_detection=False
    )

    emotions = result[0]["emotion"]

    dominant = result[0]["dominant_emotion"]

    confidence = emotions[dominant]

    return dominant, confidence
