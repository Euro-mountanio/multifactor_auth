import sqlite3
import hashlib

class authentication:
    def __init__(self):
        pass



    def register_user(self, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users ( email, password) VALUES (?, ?, ?)', ( email, hashed_password))
        conn.commit()
        conn.close()
        return True

    def login_user(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and user[3] == hashed_password:
            return True
        else:
            return False


