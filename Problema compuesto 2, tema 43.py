class Triangulo:

    def inicializar (self):
        self.ladol=int (input ("Ingrese primer lado:"))
        self.lado2=int (input ("Ingrese segundo lado:"))
        self.lado3=int (input ("Ingrese tercer lado:"))

    def imprimir (self):
        print ("Ladol:",self.ladol)
        print ("Lado2:",self.lado2)
        print ("Lado3:",self.lado3)

    def lado_mayor (self):
        print ("Lado mayor:")
        if self.ladol>self.lado2 and self.ladol>self.lado3:
            print (self.ladol)
        else:
            if self.lado2>self.lado3:
                print (self.lado2)
            else:
                print (self.lado3)

    def es_equilatero(self):
        if self.ladol==self.lado2 and self.ladol==self.lado3:
            print ("El triangulo es equilatero")
        else:
            print ("El triangulo no es equilatero")

# bloque principal

triangulol=Triangulo()
triangulol.inicializar()
triangulol. imprimir ()
triangulol.lado_mayor()
triangulol.es_equilatero()
