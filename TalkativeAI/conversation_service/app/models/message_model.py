from app.database import get_connection


def save_message(session_id, role, content):

    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO messages(session_id, role, content)
    VALUES (%s, %s, %s)
    """

    cur.execute(query, (session_id, role, content))

    conn.commit()

    cur.close()
    conn.close()
