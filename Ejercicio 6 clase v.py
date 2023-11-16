Datos =[]

with open ("agencia.cvs", "r") as f:
    for linea in f:
        lista=linea.split("|")
        lista[2]=lista[2].replace("\n", "")
        Datos.append(lista)

print(">> Contenido de la nueva lista.\n")
print(Datos)