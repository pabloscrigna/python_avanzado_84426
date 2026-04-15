import sqlite3

DB_NAME = "eduit-sqlite.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row     # lea la DB me devuelva un diccionario
    return conn
