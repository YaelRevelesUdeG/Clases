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


def generadorCodigo(codigo=[2, 2]):
    if len(codigo) > 8:
        return codigo
    else:
        codigo.append(random.randint(1, 9))
        generadorCodigo()
    return codigo


def aspirantesGenerador(numeroAspirantes):
    AspirantesLista = []
    for i in range(numeroAspirantes):
        estudiante = {
            'codigo': generadorCodigo,
            'nombre': n[random.randint(0, 4)],
            'apellidoP': a[random.randint(0, 4)],
            'apellidoM': a[random.randint(0, 4)],
            'promedioEP': random.randint(60, 100),
            'carrera': 
        }
    return AspirantesLista
