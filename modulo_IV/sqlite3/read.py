from db import get_connection


def leer_alumnos():
    conn = get_connection()
    cursor = conn.cursor()    # me permite enviar comandos a la DB

    cursor.execute(
        "SELECT * FROM alumnos"
    )
    registros = cursor.fetchall()

    for registro in registros:
        print(dict(registro)) 

    conn.close()


if __name__ == "__main__":
    leer_alumnos()