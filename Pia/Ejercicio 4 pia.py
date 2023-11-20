class ArchivosTexto:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    def crear_archivo(self):
        with open(self.nombre_archivo, "w") as archivo:
            archivo.write("")
    def escribir_archivo(self, texto):
        with open(self.nombre_archivo, "a") as archivo:
            archivo.write(texto)
    def leer_archivo(self):
        with open(self.nombre_archivo, "r") as archivo:
            texto = archivo.read()
        return texto
    def ejecutar_metodos(self):
        self.crear_archivo()
        self.escribir_archivo("Hola mundo")
        texto = self.leer_archivo()
        return texto
# Demostración del funcionamiento de la clase
archivos_texto = ArchivosTexto("Ejercicio 4 Pia")
texto = archivos_texto.ejecutar_metodos()
print(texto)