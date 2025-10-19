# Esta parte sirve para importar los modulos que vamos a usar

import DiezMilNombres
import CienPeliculas

# Vamos a crear un array que contenfa los diex mil nombres

nombres = DiezMilNombres.nombresCompletos

# Agregar mi nombre al array
nombres.append("Yael Emmanuel Reveles Calleja")
# print(nombres)

# Agregar un array llamado frankenstainarray

FrankestainArray = []

# Copiando el arreglo nombresCompletos en nc1 y CienPeliculas en pmv1

nc1 = nombres.copy()
pmv1 = CienPeliculas.peliculasMasVistas.copy()
# print(pmv1)
# print(nc1)

# Vertiendo el contenido de nc1 y pmv1 en FrankestainArray

pmv1.extend(nc1)
FrankestainArray = pmv1

# Colocando el string "P. Sherman, calle Wallaby, 42, Sydney" en distintas posiciones

position = [
    47862,
    3207,
    19880,
    23845,
    89659,
    99515,
    67427,
    85030,
    16232,
    76148,
    91368,
    48370,
    92469,
    25542,
    25752,
    44716,
    65896,
    45433,
    9639,
    23366,
    56630,
    61188,
    17988,
    94996,
    69153,
    78184,
    15322,
    14179,
    28304,
    39938,
    17997,
    79152,
    46246,
    14031,
    20242,
    44850,
    14581,
    23015,
    45545,
    42079,
    42670,
    91044,
    35203,
    68530,
    26615,
    91330,
    5273,
    21817,
    76052,
    53913,
    43999,
    29239,
    67667,
    61232,
    88338,
    95500,
    1102,
    56637,
    36731,
    4189,
    85711,
    28507,
    48210,
    16889,
    33442,
    77577,
    75372,
    99706,
    57401,
    23393,
    61692,
    63367,
    27742,
    63876,
    54736,
    86757,
    70450,
    16108,
    61613,
    66316,
    99743,
    13753,
    22505,
    60737,
    45529,
    78338,
    43624,
    8162,
    49336,
    58490,
    70903,
    82869,
    23808,
    69378,
    98290,
    95458,
    1911,
    60790,
    52294,
    57228,
    54746,
    95707,
    36615,
    87976,
    27486,
    23600,
    54518,
    70533,
    68351,
    86674,
    74711,
    53153,
    63630,
    29389,
    28197,
]


def insertando_Valores_Perrones():
    for contador in range(1):
        for comodin in position:
            FrankestainArray.insert(comodin, "P. Sherman, calle Wallaby, 42, Sydney")

    return print(FrankestainArray.count("P. Sherman, calle Wallaby, 42, Sydney"))


insertando_Valores_Perrones()

# print(FrankestainArray.count("P. Sherman, calle Wallaby, 42, Sydney"))

# Encuentra los  elementos llamados: “Are you talking to me?”, "Allene Tomasino Baily",  "Cristal Capnerhurst Silverson" y "Spider-Man: Lejos de casa"
# try:
#    print(FrankestainArray.index("Are you talking to me?"))
# except ValueError:
#    print("Are you talking to me no existe en la lista")
# try:
#    print(FrankestainArray.index("Allene Tomasino Baily"))
# except ValueError:
#    print("Allene Tomasino Baily no existe en la lista")
# try:
#    print(FrankestainArray.index("Allene Tomasino Baily"))
# except ValueError:
#    print("Allene Tomasino Baily no existe en la lista")
# try:
#    print(FrankestainArray.index("Cristal Capnerhurst Silverson"))
# except ValueError:
# print("Cristal Capnerhurst Silverson no esta en la lista")
# try:
#   print(FrankestainArray.index("Spider-Man: Lejos de casa"))
# except ValueError:
#    print("Spider-Man: Lejos de casa no esxiste en la lista")

# Inserte el siguiente String “Mi estrategia en cambio es más profunda y  más simple,
# mi estrategia es que un día cualquiera no sé cómo ni  sé con
# qué pretexto por fin me necesites…” en distintas posiciones

FrankestainArray.insert(
    501,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    547,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    635,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    855,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    898,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    900,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    935,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    957,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)
FrankestainArray.insert(
    977,
    "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…",
)

# print(
#    FrankestainArray.count(
#        "Mi estrategia en cambio es más profunda y  más simple, mi estrategia es que un día cualquiera no sé cómo ni sé con qué pretexto por fin me necesites…"
#    )
# )

# ¿Cuántos elementos se llaman "Eustaquio De Jesus Rodriguez"?

# print(FrankestainArray.count("Eustaquio De Jesus Rodriguez"))

# Creando un arreglo llamdo rostro de vos partiendo un string

StringAPartir = "Tengo una soledad tan concurrida Tan llena de  nostalgias y de rostros de vos De adioses hace tiempo y besos bienvenidos De primeras  de cambio y de último vagón Tengo una soledad tan concurrida Que puedo organizarla  como una procesión Por colores, tamaños y promesas Por época, por tacto y por sabor  Sin un temblor de más Me abrazo a tus ausencias Que asisten y me asisten Con mi  rostro de vos Estoy lleno de sombras De noches y deseos De risas y de alguna maldición  Mis huéspedes concurren Concurren como sueños Con sus rencores nuevos Su falta  de candor Yo les pongo una escoba tras la puerta Porque quiero estar solo Con mi rostro  de vos. Pero el rostro de vos Mira a otra parte Con sus ojos de amor que ya no aman  Como víveres que buscan su hambre Miran y miran y apagan mi jornada Las paredes se  van Queda la noche Las nostalgias se van No queda nada Ya mi rostro de vos Cierra los  ojos Y es una soledad Tan desolada"

RostrosDeVos = StringAPartir.split()

# print(RostrosDeVos)


# Invierta los elementos en el arreglo RostrosDeVos y  extiéndalo al arreglo  FrankensteinArray.

CopiaDeRostrosDeVos = RostrosDeVos.copy()

CopiaDeRostrosDeVos.reverse()

FrankestainArray.extend(CopiaDeRostrosDeVos)

# print(FrankestainArray)

# Elimine todos los elementos del arreglo FrankesteinArray con nombre  “rostro”, “rostros”, “soledad”, “apagan”, “Tengo”, “Jose”, “Cierra”,  "Ethelind Godfery Boick", "Petronille Alfonzo Kingh", "Meryl McCroary  McCroary", "Deborah Beevers Burdytt",  "Judi Bleythin Teligin", "Linnell Hillborne Demaid", "Annabella Dyneley  Stallon", "Jo ann Geerdts Lauritsen", "Moe Shalliker Hannent", "Ree  Renzullo Element"

ElementoAEliminar = input(
    "Que elementos desea eliminar? (Separe sus valores por espacios): \n"
)
spliteando = ElementoAEliminar.split()


def eliminador_de_elementos_3000_super_chingon():
    try:
        for i in spliteando:
            while i in FrankestainArray:
                FrankestainArray.remove(i)
                print(f"Elementos eliminados: {i}")
    except ValueError:
        print("Elemento eliminado")
    return print(ElementoAEliminar, " fue eliminado")


eliminador_de_elementos_3000_super_chingon()
