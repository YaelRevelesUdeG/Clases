# Arreglos

# Que es un Arreglos?
# Un arreglo es una direccion de memoria que contiene colecciones ya sea unicas o multiples

# nombre1 = "Horacio"
# nombre2 = "Sebastian"
# nombre3 = "Omar"
# nombre4 = "Leonardo"
# nombre5 = "Elsa"

# cibercompas = [nombre1,nombre2,nombre3,nombre4,nombre5]

# print("Antes del cambio")
# print(f"Los nombres de los cibercompas son: {nombre1}, {nombre2}, {nombre3}, {nombre4},{nombre5}")

# nombre3 = "Salamalenco"

# print("Despues del cambio")
# print(f"Los nuevos nombres son: {nombre1}, {nombre2}, {nombre3},{nombre4},{nombre5}")

tejuineros = [
    "Jonathan",
    "Job",
    "Jonathan",
    "Elsa",
    "Cesar",
    "Carlos",
    "Omar",
    "Raymundo",
    "Giovani",
    "Fernando",
]
tortahogados = [
    "Francia",
    "Daniel",
    "Horacio",
    "Yael",
    "Moises",
    "Enrique",
    "Pirulin",
    "Omahar",
    "Sebastian",
    "Christian",
    "Leonardo",
    "Daniel",
]

# Iterar sobre los arreglos
print("Los tejuineros son : ", tejuineros, "\n")
print("Los tortahogados son: ", tortahogados)

# Acceder a un elemento del arreglo
# Comando len otorga el conteo de los arreglos
print(len(tejuineros))
print(tejuineros[7])

# Unificar los arreglos
Jericayos = tejuineros + tortahogados
CiberTapatios = tortahogados + tejuineros

print("La nueva faccion de Jericayos consta de: ", Jericayos)
print("La nueva faccion de CiberTapatios consta de: ", CiberTapatios)

# Actividad.- Busquense en el nuevo arreglo

print(len(Jericayos), "\n")

print(Jericayos[13])
