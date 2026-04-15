import pymysql
from db import get_connection


def insertar_alumno(nombre, edad, email, sexo):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO alumnos (nombre, edad, email, sexo) VALUES (%s, %s, %s, %s)",
            (nombre, edad, email, sexo)
        )
        conn.commit()
        print("Alumno insertado ✅")

    except pymysql.err.IntegrityError as e:
        print("Error (email duplicado o dato inválido):", e)

    finally:
        conn.close()


def insertar_muchos():
    conn = get_connection()
    cursor = conn.cursor()

    alumnos = [
        ("Ana", 22, "ana@mail.com", "F"),
        ("Luis", 28, "luis@mail.com", "M"),
        ("Carla", 31, "carla@mail.com", "F"),
        ("Pedro", 19, "pedro@mail.com", "M"),
        ("Alex", 25, "alex@mail.com", "NC"),
    ]

    try:
        cursor.executemany(
            "INSERT INTO alumnos (nombre, edad, email, sexo) VALUES (%s, %s, %s, %s)",
            alumnos
        )
        conn.commit()
        print("Insert masivo ✅")

    except Exception as e:
        print("Error en insert masivo:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    # insertar_alumno("Santiago", 23, "santi@mail.com", "M")
    insertar_muchos()