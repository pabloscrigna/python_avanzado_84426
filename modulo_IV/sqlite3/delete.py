from db import get_connection


def borrar_usuario(nombre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM alumnos WHERE nombre = ?",
        (nombre,)
    )

    conn.commit()
    conn.close()
    print("Usuario eliminado ✅")


if __name__ == "__main__":
    borrar_usuario("Pablo")
