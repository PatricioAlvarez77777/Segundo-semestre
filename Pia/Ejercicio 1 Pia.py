class Tres_programas:
    def __init__(self, programa1, programa2, programa3):
        self.programa1 = programa1
        self.programa2 = programa2
        self.programa3 = programa3

    def descuento_clientes(self, monto_compra):
        if monto_compra < 500:
            descuento = 0
        elif 500 <= monto_compra <= 1000:
            descuento = monto_compra * 0.05
        elif 1000 <= monto_compra <= 7000:
            descuento = monto_compra * 0.11
        elif 7000 <= monto_compra <= 15000:
            descuento = monto_compra * 0.18
        else:
            descuento = monto_compra * 0.25

        descuento_total = self.programa1 + self.programa2 + self.programa3 + descuento
        return descuento_total

# Datos del problema
compras = [3500.00, 6850.00, 375.00, 690.50, 12350.00, 23314.18, 3750.00, 14200.50, 895.80, 1318.50]
num_corrida = 1


for compra in compras:
    programas = Tres_programas(10, 5, 8)
    descuento_total = programas.descuento_clientes(compra)
    pagar = compra - descuento_total
    print(f"Corrida {num_corrida}: Compra: {compra:.2f}, Pagar: {pagar:.2f}")
    num_corrida += 1