import hashlib
from app.database import get_connection


def register_user(user):

    password_hash = hashlib.sha256(
        user.password.encode()
    ).hexdigest()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users(username,password_hash)
        VALUES(%s,%s)
        RETURNING id
        """,
        (user.username, password_hash),
    )

    user_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {"user_id": user_id}


def login_user(user):

    password_hash = hashlib.sha256(
        user.password.encode()
    ).hexdigest()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id FROM users
        WHERE username=%s AND password_hash=%s
        """,
        (user.username, password_hash),
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        return {"error": "invalid credentials"}

    return {"user_id": row[0]}
