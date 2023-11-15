marcas = ["Audi \n", "Alfa Romeo\n", "BMW\n", "Mercedes Benz\n"]
with open ("marcas.txt", "w+") as f:
    f.writelines(marcas)
    f.seek(0,0)
    for linea in f:
        print (linea)