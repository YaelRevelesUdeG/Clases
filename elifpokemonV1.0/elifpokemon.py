# ELIF pokemon

print("Sistema de eleccion Pokemon v1.0 \n")
print("Elige tu tipo de Pokemon inicial: ")
print("1. Fuego")
print("2. Agua")
print("3. Hierba")
print("4. Electrico")
print("5. Hielo")
print("6. Psiquico\n")

pokemon_Elegido = str(input("Elige tu tipo: ")).lower()


if pokemon_Elegido == "fuego":
    print("Has elegido el pokemon Charmander. !Preparate para la batalla!")
elif pokemon_Elegido == "agua":
    print("Has elegido el pokemon Squirtle. !Preparate para la batalla!")
elif pokemon_Elegido == "hierba":
    print("Has elegido el pokemon Bulbasaur. !Preparate para la batalla!")
elif pokemon_Elegido == "electrico":
    print("Has elegido el pokemon Pikachu. !Preparate para la batalla!")
elif pokemon_Elegido == "hielo":
    print("Has elegido el pokemon Absol. !Preparate para la batalla!")
elif pokemon_Elegido == "psiquico":
    print("Has elegido el pokemon Abra. !Preparate para la batalla!")
else:
    print("Has desbloqueado un ... metappod, buena eleccion")
