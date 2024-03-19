class Vehiculos():
    def __init__(self,marca='',color='',modelo=''):
        self.marca = marca
        self.color = color
        self.modelo = modelo

    def set_marca(self,marca):
        self.marca = marca

    def set_color(self,color):
        self.color = color

    def set_modelo(self,modelo):
        self.modelo = modelo

    def get_marca(self):
        return self.marca
    
    def get_color(self):
        return self.color
    
    def get_modelo(self):
        return self.modelo


    def mostrar(self):
        print("la marca de tu vehiculo es: ",self.marca)
        print("color de tu vehiculo es : ",self.color)
        print("el modelo de tu vehiculo es : ",self.modelo)

    def validacion(self):
        while self.marca.lower() == "toyota":
            print("No esta permitida la marca intente de nuevo: ")
            self.set_marca(input("ingrese la marca de su vehiculo por favor: "))


class Motos(Vehiculos):
    def __init__(self, marca='', color='', modelo=''):
        super().__init__(marca, color, modelo)
    
    def validacion2(self):
         while self.marca.lower() == "akt":
            print("No esta permitida la marca intente de nuevo: ")
            self.set_marca(input("ingrese la marca de su vehiculo por favor: "))

    
vehiculos1 = Vehiculos(Motos)
vehiculos1.set_marca (input("ingrese la marca de su vehiculo por favor: "))
vehiculos1.validacion()
vehiculos1.set_color (input("ingrese el color de su vehiculo por favor: "))
vehiculos1.set_modelo (input("ingrese el modelo de su vehiculo por favor: "))
vehiculos1.mostrar()



