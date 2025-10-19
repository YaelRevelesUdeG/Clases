# simulador de tirada de dado

import random

bandera = True

while bandera:
    print("este es el juego mas maravilloso del mundo mundial ese madafakiu!!v1.1\n")
    selector = int(
        input("presione cualquier tecla para tirar el dado o 2 para salir: ")
    )
    if selector == 2:
        bandera = False
    else:
        dado = random.randint(1, 6)
        print("el valor del dado es: \n", dado)
