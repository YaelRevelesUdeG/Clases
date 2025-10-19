import random

bandera = True

decision = int(input("Cuantos dados quieres usar? \n 1.- Uno 2.- Dos\n"))

if decision == 1:
    while bandera:
        print(
            "este es el juego mas maravilloso del mundo mundial ese madafakiu!!v1.1\n"
        )
        selector = input("presione cualquier tecla para tirar el dado o 2 para salir: ")
        if selector == "2":
            bandera = False
        else:
            dado = random.randint(1, 6)
            print("el valor del dado es: \n", dado)
elif decision == 2:
    while bandera:
        print(
            "este es el juego mas maravilloso del mundo mundial ese madafakiu!!v1.1\n"
        )
        selector = input("presione cualquier tecla para tirar el dado o 2 para salir: ")

        if selector == "2":
            bandera = False
        else:
            dado_1 = random.randint(1, 6)
            dado_2 = random.randint(1, 6)
            print("El valor del dado 1 es: \n", dado_1)
            print("El valor del dado 2 es: \n", dado_2)
            print("Suman: ", dado_1 + dado_2)
else:
    print("Ese valor no figura dentro de las opciones")
