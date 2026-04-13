def suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


def resta(numero1, numero2):
    return numero2 - numero1


if __name__ == "__main__":
    print("name operaciones: ", __name__)
    numero1 = 100
    numero2 = 200
    print(f"operaciones - numero1: {numero1} - numero2: {numero2}")
    print("suma resultado: ", suma(numero1, numero2))
