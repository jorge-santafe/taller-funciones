def calcular_area (base:float, altura:float):
    if base >0 and altura >0:
        area= (base * altura)/2
        return area
    else:
        area = 0
        return area

suma=0
for i in range (1,3):
    print('\nTriangulo', i)
    base= float(input("Ingrese base del triángulo: "))
    altura= float(input("Ingrese altura del triángulo: "))

    area= calcular_area(base,altura)
    print ("\nArea del triángulo ", i, ": ", area,"\n")

    suma+=area

print("Suma de las áreas: ", suma)