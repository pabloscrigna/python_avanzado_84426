import requests

BASE_URL = "http://localhost:7001/student"


def crear_alumno():
    data = {
        "name": input("Nombre: "),
        "courses": input("Cursos (separados por coma): ").split(",")
    }

    response = requests.post(BASE_URL, json=data)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())


def listar_alumnos():
    response = requests.get(BASE_URL)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())


def obtener_alumno():
    alumno_id = input("ID del alumno: ")
    response = requests.get(f"{BASE_URL}/{alumno_id}")
    print("Status:", response.status_code)
    print("Respuesta:", response.json())


def modificar_alumno():
    alumno_id = input("ID del alumno: ")

    data = {}
    nombre = input("Nuevo nombre (enter para omitir): ")
    cursos = input("Nuevos cursos (coma, enter para omitir): ")

    if nombre:
        data["name"] = nombre
    if cursos:
        data["courses"] = cursos.split(",")

    response = requests.put(f"{BASE_URL}/{alumno_id}", json=data)

    print("Status:", response.status_code)
    if response.content:
        print("Respuesta:", response.json())


def borrar_alumno():
    alumno_id = input("ID del alumno: ")
    response = requests.delete(f"{BASE_URL}/{alumno_id}")

    print("Status:", response.status_code)
    if response.content:
        print("Respuesta:", response.json())


def menu():
    while True:
        print("""--- CRUD ALUMNOS ---"
        1. Crear alumno
        2. Listar alumnos
        3. Ver alumno
        4. Modificar alumno
        5. Borrar alumno
        0. Salir""")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            crear_alumno()
        elif opcion == "2":
            listar_alumnos()
        elif opcion == "3":
            obtener_alumno()
        elif opcion == "4":
            modificar_alumno()
        elif opcion == "5":
            borrar_alumno()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()