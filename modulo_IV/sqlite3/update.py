from db import get_connection


def actualizar_edad(nombre, nueva_edad):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE alumnos SET edad = ? WHERE nombre = ?",
        (nueva_edad, nombre)
    )

    conn.commit()
    conn.close()
    print("Alumno actualizado ✅")


if __name__ == "__main__":
    actualizar_edad("Maria", 26)
