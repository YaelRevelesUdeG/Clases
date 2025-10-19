jericallos = [
    "Raymundo",
    "Eimy",
    "Gama",
    "Omar",
    "Fernando",
    "Giovani",
    "Elsa",
    "Cesar",
]
tejuineros = ["Fausto", "Daniel", "Daniel", "Enrique", "Sebastian", "Yael"]

print(jericallos)
print("")
print(tejuineros)

# Metodo Append
jericallos.append("Moises")
jericallos.append("Moises")
print("")
print(jericallos)

# Metodo clear()
print("")
# tejuineros.clear()
# print(tejuineros)

# Metodo copy()
TortaAhogado = jericallos.copy()
print("This is a tortilla milshake team: ", TortaAhogado)

# Metodo count()
print(tejuineros.count("Daniel\n \n \n \n"))

# Metodo extend()
tejuineros.extend(jericallos)
print(jericallos)

# Metodo index()
print(tejuineros.index("Yael"))

# Metodo insert()
tejuineros.insert(6, "Nava")
print(tejuineros)

# Metodo pop()
tejuineros.pop(6)
print(tejuineros)

# Metodo remove()
tejuineros.remove("Omar")
print(tejuineros)

# Metodo reverse()
tejuineros.reverse()
print(tejuineros)
