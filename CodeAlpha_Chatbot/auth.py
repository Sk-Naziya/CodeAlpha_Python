import bcrypt
from database import conn,c

def register(username,password):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        c.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username,hashed)
        )
        conn.commit()
        return True
    except:
        return False

def login(username,password):

    c.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    user=c.fetchone()

    if user:
        return bcrypt.checkpw(
            password.encode(),
            user[0]
        )

    return False