def subtotal_descontado(base: float, descuento: float):
    subtotal = base * (1 - descuento / 100)
    return subtotal


def total_con_impuesto(subtotal: float, impuesto: float):
    total = subtotal * (1 + impuesto / 100)
    return total


base = float(input("Ingrese el valor base: "))
porcentaje_descuento = float(input("Ingrese porcentaje descuento: "))
porcentaje_impuesto = float(input("Ingrese procentaje impuesto: "))

subtotal = subtotal_descontado(base, porcentaje_descuento)
total = total_con_impuesto(subtotal, porcentaje_impuesto)

print("Subtotal: ", subtotal)
print("Total: ", total)
