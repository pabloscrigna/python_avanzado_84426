from db import get_connection


def actualizar_email(nombre, nuevo_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE alumnos SET email = %s WHERE nombre = %s",
        (nuevo_email, nombre)
    )

    conn.commit()
    conn.close()
    print("Email actualizado ✅")


if __name__ == "__main__":
    actualizar_email("Ana", "ana_nuevo@mail.com")