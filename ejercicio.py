# Para que el ejercicio vuelva a pedir la marca del vehículo si se ingresa "Toyota", puedes hacer lo siguiente:

class Vehiculos():
    def __init__(self, marca='', color='', modelo=''):
        self.marca = marca
        self.color = color
        self.modelo = modelo

    def set_marca(self, marca):
        self.marca = marca

    def set_color(self, color):
        self.color = color

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_marca(self):
        return self.marca
    
    def get_color(self):
        return self.color
    
    def get_modelo(self):
        return self.modelo

    def mostrar(self):
        print("La marca de tu vehiculo es:", self.marca)
        print("Color de tu vehiculo es:", self.color)
        print("El modelo de tu vehiculo es:", self.modelo)

    
    def validacion(self):
        while self.marca.lower() == "toyota":  # Corregir el método lower() para que convierta la marca a minúsculas
            print("No puedes ingresar esta marca. Intenta nuevamente.")
            self.set_marca(input("Ingrese la marca de su vehiculo por favor: "))  # Solicitar nuevamente la marca

vehiculos1 = Vehiculos()
vehiculos1.set_marca(input("Ingrese la marca de su vehiculo por favor: "))
vehiculos1.validacion()  # Llamar al método validación para verificar la marca ingresada
vehiculos1.set_color(input("Ingrese el color de su vehiculo por favor: "))
vehiculos1.set_modelo(input("Ingrese el modelo de su vehiculo por favor: "))
vehiculos1.mostrar()
