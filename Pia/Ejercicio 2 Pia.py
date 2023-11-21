class Dinosaurio:
    def __init__(self, nombre, peso_toneladas, longitud_pies):
        self.nombre = nombre
        self.peso_toneladas = peso_toneladas
        self.longitud_pies = longitud_pies

    def dinosaurio(self):
        # Convertir peso de toneladas a kilogramos
        peso_kg = self.peso_toneladas * 1000

        # Convertir longitud de pies a metros
        longitud_metros = self.longitud_pies * 0.3048

        return f"El dinosaurio {self.nombre} tiene un peso de {peso_kg} kilogramos y una longitud de {longitud_metros} metros."

# Datos proporcionados
nombres = ["PLATAEOSAURUS", "DIPLOJOCUS", "BRACHIOSAURUS", "BRONTOSAURUS", "TYRANNOSAURUS"]
pesos = [5, 15, 50, 25, 8]
longitudes = [30, 90, 80, 70, 30]

# Crear objetos de la clase Dinosaurio para cada conjunto de datos
resultados = []
for i in range(len(nombres)):
    dino = Dinosaurio(nombres[i], pesos[i], longitudes[i])
    resultados.append(dino.dinosaurio())

# Mostrar resultados
for resultado in resultados:
    print(resultado)