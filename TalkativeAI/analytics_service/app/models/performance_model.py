from app.database import get_connection


def save_performance(
    user_id,
    session_id,
    clarity,
    confidence,
    structure,
    overall
):

    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO performance_history(
        user_id,
        session_id,
        clarity_score,
        confidence_score,
        structure_score,
        overall_score
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cur.execute(
        query,
        (user_id, session_id, clarity, confidence, structure, overall)
    )

    conn.commit()

    cur.close()
    conn.close()
