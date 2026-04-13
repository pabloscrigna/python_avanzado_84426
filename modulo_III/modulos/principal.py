# Forma 1
# import operaciones
# 
# 
num1 = 100
num2 = 500
# 
# 
# resultado = operaciones.suma(num1, num2)
# 
# print("principal -- resultado suma: ", resultado)


# forma 2
#from operaciones import *
#
#resultado = suma(num1, num2)
#resultado_resta = resta(num1, num2)
#
#print("principal -- resultado suma: ", resultado)
#print("principal -- resultado resta: ", resultado_resta)


# forma3
# from operaciones import suma
# from operaciones import suma, resta
# 
# resultado = suma(num1, num2)
# resultado_resta = resta(num1, num2)
# 
# print("principal -- resultado suma: ", resultado)


# forma4
from operaciones import suma as s


def main():
    print("name principal: ", __name__)
    resultado = s(num1, num2)
    print("principal -- resultado suma: ", resultado)


if __name__ == "__main__":
    main()

