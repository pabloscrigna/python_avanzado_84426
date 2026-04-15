from db import get_connection


def insert_alumnos(alumnos):
    conn = get_connection()
    cursor = conn.cursor()    # me permite enviar comandos a la DB

    cursor.executemany(
        "INSERT INTO alumnos (nombre, edad) VALUES (?, ?)",
        alumnos
    )
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    alumnos = [
        ("Ana", 21),
        ("Agustin", 19),
        ("Victoria", 27),
    ]

    insert_alumnos(alumnos)