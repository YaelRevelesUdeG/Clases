# Yael Emmanuel Reveles Calleja
# Josue Sebastian Ramirez Rodriguez


# Diccionarios
from names import names
from last_name import last_name
import random
import time

diccionario = {
    "codigo": "",
    "nombre": "",
    "apellido_P": "",
    "apellido_M": "",
}


# INSTRUCCION 1
# Crear funcion que genere un codigo aleatorio
# Siguiendo la logica de U de G => 9 digitos


def codigo():
    print("Generando codigo, espere")
    time.sleep(1)
    return str(random.randint(100000000, 9999999998))


# INSTRUCCION 2
# genere una funcion que genere un diccionarios siguiendo
# la estructura "diccionario"
# La funcion debe de exportar el codigo en String


def Generador():
    return {
        "codigo": codigo(),
        "nombre": names[random.randint(0, 999)],
        "apellido_P": last_name[random.randint(0, 999)],
        "apellido_M": last_name[random.randint(0, 999)],
    }


print(Generador())

# INSTRUCCION 3

arregloInstruccion3 = []

for i in range(100):
    arregloInstruccion3.append(Generador())

print(arregloInstruccion3)
