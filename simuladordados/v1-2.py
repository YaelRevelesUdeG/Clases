# simulador de tirada de dado

import random

bandera = True

while bandera:
    print("este es el juego mas maravilloso del mundo mundial ese madafakiu!!v1.1\n")
    selector = input("presione cualquier tecla para tirar el dado o 2 para salir: ")

    if selector == 2:
        bandera = False
    else:
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        print("El valor del dado 1 es: \n", dado_1)
        print("El valor del dado 2 es: \n", dado_2)
        print("Suman: ", dado_1 + dado_2)
# Hacer dos dados y sumarlos
