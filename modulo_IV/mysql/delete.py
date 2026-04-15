from db import get_connection


def borrar_alumno(nombre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM alumnos WHERE nombre = %s",
        (nombre,)
    )

    conn.commit()
    conn.close()
    print("Alumno eliminado ✅")


if __name__ == "__main__":
    borrar_alumno("Pedro")
