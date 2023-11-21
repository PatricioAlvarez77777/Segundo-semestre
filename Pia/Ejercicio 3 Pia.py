def leer_precio_por_litro():
    precio_por_litro = float(input("Ingrese el precio de la gasolina por litro: "))
    return precio_por_litro

def leer_galones_surtenidos():
    galones_surtenidos = float(input("Ingrese la cantidad de galones surtenidos: "))
    return galones_surtenidos

def convertir_galones_a_litros(galones):
    litros = galones * 3.780
    return litros

def calcular_costo(litros, precio_por_litro):
    costo = litros * precio_por_litro
    return costo

# Proceso
precio_por_litro = leer_precio_por_litro()
galones_surtenidos = leer_galones_surtenidos()
litros_surtenidos = convertir_galones_a_litros(galones_surtenidos)
costo = calcular_costo(litros_surtenidos, precio_por_litro)

# Salida
print("El cliente debe pagar :",costo)