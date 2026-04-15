from db import get_connection


def obtener_alumnos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alumnos")
    registros = cursor.fetchall()

    print("\n--- LISTA DE ALUMNOS ---")
    for registro in registros:
        print(registro)

    conn.close()


if __name__ == "__main__":
    obtener_alumnos()