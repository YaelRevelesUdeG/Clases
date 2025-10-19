# Realice la funcion que calcule el area de un triangulo


def area_Triangulo():
    Base = int(input("Cual es la base?: "))
    Altura = int(input("Cual es la altura?: "))
    return (Base * Altura) / 2


print(area_Triangulo())


# Tipos de triangulo: equilatero, escaleno, isoceles
def perimetro_triangulo(l1, l2, l3):
    return l1 + l2 + l3


T_equilatero = perimetro_triangulo(2, 2, 2)
T_escaleno = perimetro_triangulo(1, 2, 3)
T_isoceles = perimetro_triangulo(2, 2, 4)
