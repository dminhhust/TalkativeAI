from app.database import get_connection


def create_user(username, password_hash):

    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO users (username, password_hash)
    VALUES (%s, %s)
    RETURNING id
    """

    cur.execute(query, (username, password_hash))
    user_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return user_id


def get_user_by_username(username):

    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT id, username, password_hash
    FROM users
    WHERE username = %s
    """

    cur.execute(query, (username,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    return result
