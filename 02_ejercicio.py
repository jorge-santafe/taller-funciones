def calcular_precio(precio_total:int, cantidad:int):
    if precio_total >=0 and cantidad > 0:
        precio_por_gramo = precio_total // cantidad
        return precio_por_gramo
    else:
        precio_por_gramo = 0
        return 0

def comparar_paquete (precio1:int, precio2:int):
    if precio1 < precio2: 
        mensaje = "El paquete 1 es más ecónomico"
        return mensaje
    elif precio1 > precio2:
        mensaje = "El paquete 2 es más ecónomico"
        return mensaje
    else:
        mensaje = "Ambos paquetes cuentan los mismo"
        return mensaje


precio_1= 0
precio_2= 0

for i in range(1,3):
    print("Paquete: ", i)
    precio = int(input("Ingrese el precio total: "))
    gramos = int(input("Ingrese la cantidad en gramos: "))

    precio_unitario = calcular_precio(precio,gramos)
    if i == 1:
        precio_1 = precio_unitario
    else:
        precio_2 = precio_unitario

    print("Precio por gramo del paquete " ,i, ":",precio_unitario, "\n")

resultado = comparar_paquete(precio_1, precio_2)
print(resultado)