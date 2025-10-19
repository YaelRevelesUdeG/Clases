# Yael Emmanuel Reveles Calleja
# Josue Sebastian Ramirez Rodriguez

import random


# ACTIVIDAD DE REPASO - 21032025


# Funcion que devuelva la suma de dos numeros
def suma(a, b):
    resultado = a + b
    return resultado


# Funcion que devuelva la resta de dos numeros
def resta(a, b):
    resultado = a - b
    return resultado


# Funcion que devuelva el producto de dos numeros
def producto(a, b):
    resultado = a * b
    return resultado


# Funcion que devuelva el cociente de dos numeros
def cociente(a, b):
    resultado = a / b
    return resultado


# Funcion que devuelva la raiz cuadrada de un numero
def raiz(a):
    resultado = a ** (1 / 2)
    return resultado


print(raiz(9))


# Funcion que devuelva el area de un triangulo donde b, h serán dados por el usario
def areaTriangulo(b, h):
    resultado = (b * h) / 2
    return resultado


# Funcion que devuelva el area de un circulo donde r será dado por el usario
def areaCirculo(r):
    pi = 3.1416
    resultado = pi * r**2
    return resultado


# Funcion que devuelva el area de un cuadrado donde l será dado por el usuario
def areaCuadrado(l):
    resultado = l * l
    return resultado


# Funcion que devuelva el area de un rectangulo donde l1 y l2 serán dados por el usuario
def areaRectangulo(l1, l2):
    base = l1
    altura = l2
    resultado = base * altura
    return resultado


# Función que devuelva el perimetro de un rectángulo donde l1 y l2 será dado por el usuario
def perimetroRectangulo(l1, l2):
    resultado = l1 + l2
    return resultado


# Funcion que devuelva True/False si un número es par/impar
def parImpar(numero):
    if numero % 2 == 0:
        return "Numero par"
    else:
        return "Numero impar"


# Funcion que devuelva la suma de todos los elementos de un arreglo
def sumaArreglo(arreglo):
    acumulador = 0
    for elemento in arreglo:
        acumulador = acumulador + elemento
    return acumulador


# Funcion que devuelva el promedio de un arreglo de numeros
def promedio(arreglo):
    acumulador = 0
    contador = 0
    for i in arreglo:
        contador = contador + 1
        acumulador = acumulador + i
    return acumulador / contador


# Función que devuelva un arreglo variable de numeros aleatorios de un rango especifico
def arregloVariable(deDonde, aDonde, longitud):
    arregloCompleto = [random.randint(deDonde, aDonde)]
    for length in range(longitud):
        arregloCompleto.insert(
            length,
            random.randint(deDonde, aDonde),
        )
    return arregloCompleto


# Funcion que devuelva un arreglo de N strings dados por el usuario
def impresionStringNVeces(N, stringAImprimir):
    for i in range(N):
        print(stringAImprimir)
    return "resultado"
