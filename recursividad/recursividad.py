""""def funcion_recursiva(DoYouWantToContinue):
selector = input("Do you want to continue? (yes/no): ").strip().lower()
    if DoYouWantToContinue == "yes":
        return funcion_recursiva(selector)
    else:
        print("Exiting the function")


funcion_recursiva("yes")"""
"""
def cuenta_regresiva(n):
    if n <= 0:
        print("Despegue !")
    else:
        print(n)
        cuenta_regresiva(n-1)
"""


# Factorital
"""
def factotrial(n):
    if n == 0:
        return 1
    else:
        return n * factotrial(n-1)

print(factotrial(5))
"""

# Suma de una lista
"""
lista_1 = [1, 2, 3, 4, 5, 6, 7]


def sumalista(lista):
    suma = 0
    if not lista:
        return suma
    else:
        elementoFuera = lista.pop()
        listaNueva = sumalista(lista)
        return elementoFuera + listaNueva


print(sumalista(lista_1))
"""

# Secuencia de Fibonacci
