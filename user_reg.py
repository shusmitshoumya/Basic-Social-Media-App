import sqlite3
import hashlib

conn  = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users(    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password NOT NULL
    )'''
)

conn.commit()


def hash_pass(password) :
    return hashlib.sha256(password.encode()).hexdigest()


def userRegister(username, password) :
    try:
        hashed_pass = hash_pass(password)
        cursor.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, hashed_pass))
        conn.commit()

        return True, "User registered succesfully!"
    
    except sqlite3.IntegrityError :
        return False, "Username already exists!"


def userLogin(username, password) :
        
        hashed = hash_pass(password)
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

        return cursor.fetchone() is not None