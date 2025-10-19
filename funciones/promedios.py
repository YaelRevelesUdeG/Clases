#Capturador de datos para calculo de media aritmetica

promedio_Ciber_Compas = 0
suma_Promedios = 0
tamano_De_La_Muestra: 0

tamano_De_La_Muestra = int(input("Ingrese el tamano de la muestra"))

for i in range(tamano_De_La_Muestra):
    promedio_Ciber_Compas = int(input("Ingrese su promedio: "))
    suma_Promedios +=  promedio_Ciber_Compas

print("El promedio de los cibercompas es: ", suma_Promedios/tamano_De_La_Muestra)

