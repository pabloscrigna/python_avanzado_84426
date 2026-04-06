def sumar(a: int, b: int) -> int:
    return a + b


def saludar(nombre: str) -> str:
    return f"Hola {nombre}"


def promedio(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)


def obtener_claves(dic: dict[str, int]) -> list[str]:
    return list(dic.keys())


print(sumar(15.7, 15))
