def overall_score(clarity, confidence, structure):

    score = (
        0.4 * clarity +
        0.3 * confidence +
        0.3 * structure
    )

    return score
