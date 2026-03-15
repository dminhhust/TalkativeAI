from app.database import get_connection


def create_session(user_id, scenario):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO sessions(user_id,scenario)
        VALUES(%s,%s)
        RETURNING id
        """,
        (user_id, scenario),
    )

    session_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return session_id
