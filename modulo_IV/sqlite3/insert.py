from db import get_connection


def insert_alumno(nombre, edad):
    conn = get_connection()
    cursor = conn.cursor()    # me permite enviar comandos a la DB

    cursor.execute(
        "INSERT INTO alumnos (nombre, edad) VALUES (?, ?)",
        (nombre, edad)
    )
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    insert_alumno("Juan", 20)
    insert_alumno("Maria", 30)