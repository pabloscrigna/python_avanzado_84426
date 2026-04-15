from db import get_connection


def crear_tabla():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        edad INT,
        email VARCHAR(100) UNIQUE,
        sexo ENUM('M', 'F', 'NC')
    )
    """)

    conn.commit()
    conn.close()
    print("Tabla alumnos creada ✅")


if __name__ == "__main__":
    crear_tabla()
