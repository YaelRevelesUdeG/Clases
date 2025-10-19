from collections import deque
import time

# Creamos una cola para la impresora

puntosextra = True
cola = deque()
CapacidadMaxima = 15


print("-----Bienvenidos al administrador de colas de autos-----\n")

while puntosextra:
    print("Menu\n \n")
    selector = int(
        input(
            " ■ 1. Introducir auto \n ■ 2. Retirar auto \n ■ 3. Mostrar autos en el estacionamiento \n ■ 4. Salir \n "
        )
    )
    placa = str
    if selector == 1:
        placa = input(" ■ Ingrese su placa: ")
        flag = True
        while flag:
            if len(cola) < CapacidadMaxima:
                cola.append(placa)
                time.sleep(1)
                print(" ■ Auto estacionado")
            else:
                print(" ■ Capacidad maxima superada, por favor espere")
                time.sleep(1)
    elif selector == 2:
        salida = cola.popleft()
        print(f" ■ El auto {salida} ha salido")
        time.sleep(1)
    elif selector == 3:
        print(cola)
        time.sleep(1)
    elif selector == 4:
        print(" ■ Gracias por visitarnos")
        puntosextra = False
    else:
        " ■ No esta en las opciones elija un numero del 1 al 4 por favor"
