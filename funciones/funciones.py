# FUNCIONES
#
# Son como maquinas que reciben datos, los procesan y devuelven un resultadp
#
# Se definen con las palabra reservada def, seguida del nombre de la funcion y parentesis


# Declaracion de funciones

# Sin parametros
def saludar():
    return "Que onda ese madafakiu"


# Con parametros
def sumar(a, b):
    return a + b


# print(saludar())
# print(sumar(2, 2))

# Realice una funcion que calcule el area de una circunferencia


def area_circular(radio):
    return radio**2 * 3.1416


# ** es elevar a


print(area_circular(1))
