from semillas import ArrayNombres as n
from semillas import ArrayApellidos as a
from semillas import CarrerasCUGdl as c
from semillas import MateriasSemestre1 as m1
from semillas import MateriasSemestre2 as m2
from semillas import TuplaSemestres as s
import random

# Cree un programa que genere de forma aleatoria y utilizando
# la informacion semilla del archivo "semilla.py" la estructura de codigo
# mencionada en el archivo estructura.py

# Utilice la informacion de clases anteriores.
# La funcion que estructure la informacion,
# debe de regresar un arreglo llamado AspirantesLista

# Generador de codigo de estudiante


def generador_codigo(codigo=[2, 2]):
    if len(codigo) > 8:
        return codigo
    else:
        codigo.append(random.randint(1, 9))
        generador_codigo()
    return codigo

# Randomizador de las claves de los diccionario.


def randomizador(diccionario):
    listaDeClaves = list(diccionario)
    key = random.choice(listaDeClaves)
    return key


def calificaciones_de_materias(materias={}):
    if s == 1:
        for m in m1:
            materias[m] = random.randint(0, 100)
    elif s == 2:
        for m in m2:
            materias[m] = random.randint(0, 100)
    else:
        print("No existen materias para este semestre")
    return materias


print(calificaciones_de_materias())

# Funcion principal


def aspirantes_generador(numeroAspirantes, AspirantesLista=[]):
    for i in range(numeroAspirantes):
        estudiante = {
            'codigo': generador_codigo(),
            'nombre': n[random.randint(0, 4)],
            'apellidoP': a[random.randint(0, 4)],
            'apellidoM': a[random.randint(0, 4)],
            'promedioEP': random.randint(60, 100),
            'carrera': randomizador(c),
            'semestre': s[random.randint(0, 2)],
            'activo': True,
            'calificaciones': calificaciones_de_materias()
        }
        AspirantesLista.append(estudiante)
    return AspirantesLista
