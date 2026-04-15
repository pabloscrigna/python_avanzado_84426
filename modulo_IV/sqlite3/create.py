from db import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()    # me permite enviar comandos a la DB

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
    """)
    conn.commit()
    conn.close()
    print("se creo la tabla")


if __name__ == "__main__":
    create_table()
