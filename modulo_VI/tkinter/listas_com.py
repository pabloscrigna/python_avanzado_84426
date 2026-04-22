
lista = [1, 2, 3, 4, 5]

lista_nueva = []


for item in lista:
    lista_nueva.append(item**2)


print("lista", lista)
print("lista 2", lista_nueva)

lista_nueva = [ x**2 for x in lista ]

lista_impares = [ x**2 for x in lista if x%2 ]

print("lista impares: ", lista_impares)