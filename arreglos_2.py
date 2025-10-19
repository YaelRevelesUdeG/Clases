edadesCiber11a13 = [36, 28, 18, 18, 18, 19, 18, 19, 21, 21, 19, 21, 20, 20, 22, 20, 18]

acumulador = 0


def medidaEdades():
    suma = 0
    for edad in edadesCiber11a13:
        suma += edad
    return suma / len(edadesCiber11a13)


#        acumulador =+ edad
#    return acumulador / edadesCiber11a13.count()

print(medidaEdades())
