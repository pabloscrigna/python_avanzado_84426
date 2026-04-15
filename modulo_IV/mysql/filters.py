from db import get_connection


def buscar_alumnos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM alumnos
        WHERE edad BETWEEN %s AND %s
        AND sexo = %s
        AND nombre LIKE %s
        ORDER BY edad DESC
        LIMIT 5
    """, (20, 35, "F", "%a%"))

    resultados = cursor.fetchall()

    print("\n--- FILTRO AVANZADO ---")
    for fila in resultados:
        print(fila)

    conn.close()


if __name__ == "__main__":
    buscar_alumnos()