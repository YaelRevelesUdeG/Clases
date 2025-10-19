#ELIF

#Condicion donde se evalue cada argumento

edad = int(input("Ingrese su edad: "))

#Bebe < 3
#Infante 3>11
#Adolescente 11>18
#Adulto 18<34
#Chavorruco 34 < 65
#Reliquia 65 < 85
#Pal museo 85 < ...

if edad <= 3:
   print("Eres un bebe")
elif edad > 3 & edad <= 11:
    print("Eres un infante")
elif edad > 11 & edad <=18:
    print("Eres un adolescente")
elif edad > 18 & edad <= 34:
    print("Eres un adulto")
elif edad > 34 & edad <= 65:
    print("Eres un chavorruco")
elif edad > 65 & edad <= 85:
    print("Eres una reliquia")
elif edad > 85:
    print("Estas pal museo")

