import numpy as np


def compute_confidence_score(emotions):

    negative = ["fear","sad","angry","disgust"]

    negative_count = 0

    for e in emotions:

        if e["emotion"] in negative:
            negative_count += 1

    ratio = negative_count / len(emotions)

    score = 1 - ratio

    return score
