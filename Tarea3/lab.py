import random


def generador_codigo(codigo=[2, 2]):
    if len(codigo) > 8:
        return codigo
    else:
        str(codigo.append(random.randint(1, 9)))
        generador_codigo()
    return "".join(codigo)


print(generador_codigo())
