def compute_speaking_speed(transcript, duration):

    words = len(transcript.split())

    wpm = words / (duration / 60)

    return wpm
