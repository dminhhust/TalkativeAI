from app.database import get_connection


def store_message(session_id, role, message):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO messages(session_id,role,message)
        VALUES(%s,%s,%s)
        """,
        (session_id, role, message),
    )

    conn.commit()

    cur.close()
    conn.close()
