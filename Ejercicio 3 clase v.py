import os
archivo="colores.txt"
f = open(archivo,"a+")
# Verificación de que ya se creo.
if os.path.exists(archivo):
    print("\nEl archivo ya existe")
else:
    print("\nEl archivo no existe")
# Se cierra el archivo.
f.close()