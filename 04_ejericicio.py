def pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
        return pago
    else:
        pago = 40 * tarifa + (horas - 40) * tarifa * 1.5
        return pago


total = 0
for i in range(1, 3):
    horas = float(input("Ingrese las horas trabajadas: "))
    tarifa = float(input("Ingrese la tarifa por hora: "))

    pago = pago_semanal(horas, tarifa)
    print("Pago persona ", i, ": ", pago, "\n")
    total += pago

print("\nTotal: ", total)
