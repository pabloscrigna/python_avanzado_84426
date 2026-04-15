from db import get_connection


def obtener_alumnos_nombre(cursor, nombre):
    print("Alumnos")
    filas = cursor.execute(
        "SELECT * FROM alumnos WHERE nombre = ?",
        (nombre,)
    )

    for fila in filas:
        print(dict(fila))


def obtener_alumnos_mayores(cursor, edad):
    print("Alunos mayores")
    filas = cursor.execute(
        "SELECT * FROM alumnos WHERE edad > ?",
        (edad,)
    )

    for fila in filas:
        print(dict(fila))


def filtro_completo(cursor, nombre, edad_minima, edad_maxima):
    print("filtro completo")
    filas = cursor.execute("""
            SELECT * FROM alumnos
            WHERE edad BETWEEN ? AND ?
            AND nombre LIKE ?
            ORDER BY edad DESC
            LIMIT 3
        """, (edad_minima, edad_maxima, f"%{nombre}%"))

    for fila in filas:
        print(dict(fila))


if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()

    obtener_alumnos_nombre(cursor, "Ana")
    obtener_alumo_mayores(cursor, 25)
    filtro_completo(cursor, "a", 18, 35)

    conn.close()
