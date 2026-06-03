import sqlite3

conn = sqlite3.connect("chatbot.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password BLOB
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS chats(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    chat_name TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    chat_name TEXT,
    role TEXT,
    message TEXT
)
""")

conn.commit()