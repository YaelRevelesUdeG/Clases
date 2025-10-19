# PIEDRA, PAPEL O TIJERA
#
# CONVIERTA EL JUEGO A CODIGO
#
# Criterios
#
# Piedra le gana a tijera y pierde con papel
# Tijera le gana a papel y su nemesis es piedra
# Papel le gana a piedra y pierde con tijera
import random

pc = 0
jugador = 0
juego_iniciado = True
selector = 0

# Esta es la presentacion al usuario
print("Este es el juego del piedra papel o tijera\n")
selector = int(input("Quiere jugar? \n 1.Si 2.No "))
if selector == 1:
    juego_iniciado = True
elif selector == 2:
    juego_iniciado = False
else:
    print("No es una opcion")

# Logica de equivalencia entre los objetos

elementos = ["Piedra", "Papel", "Tijera"]
eleccion_de_elementos = [2, 3, 4]
elemento_seleccionado = ""

if eleccion_de_elementos == 2:
    elemento_seleccionado = [elementos[0]]
elif eleccion_de_elementos == 3:
    elemento_seleccionado = [elementos[1]]
elif eleccion_de_elementos == 4:
    elemento_seleccionado = [elementos[2]]
else:
    print("Como?")


# Logica del inicio del juego

pc = random.randint(2, 4)

while juego_iniciado:
    print("Ahora vas a jugar contra la PC")
    jugador = int(input("Que eliges?:\n 1. Piedra\n 2. Papel\n3. Tijera\n"))

    # Logica del juego
    #
    if jugador == 1:
        print("Elegiste: ", elementos[0])
        print("Tu oponenente eligio: ", eleccion_de_elementos[pc])
