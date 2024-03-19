class Empleados():
    def __init__(self,nombre='',salario=0,antiguedad=''):
        self.nombre = nombre
        self.salario = salario
        self.antiguedad = antiguedad

    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_salario(self,salario):
        self.salario = salario
    
    def set_antiguedad(self,antiguedad):
        self.antiguedad = antiguedad

    def get_nombre(self):
        return self.nombre
    
    def get_salario(self):
        return self.salario
    
    def get_antiguedad(self):
        return self.antiguedad

    def mostrar(self):
        print("su nombre es : ",self.nombre)
        print("su salario es : ",self.salario)
        print("su antiguedad es: ",self.antiguedad)
    

class Gerente(Empleados):
    def __init__(self, nombre='', salario=0, antiguedad='',rol=''):
        super().__init__(nombre, salario, antiguedad,)
        self.rol = rol

    def set_rol(self,rol):
        self.rol = rol
     
    def get_rol(self):
        return self.rol
    
    def mostrar(self):
        super().mostrar()
        print("su rol es:",self.rol)



empleado1= Empleados()
print("Informacion de empleados: ")
empleado1.set_nombre (input("ingresa tu nombre por favor: "))
empleado1.set_salario(int(input("ingresa tu salario por favor\n sin puntos: ")))
empleado1.set_antiguedad (input("ingresa tu antiguedad por favor: "))

print("\n")

empleado1.mostrar()

print("\n")

gerente1 = Gerente()
print("informacion del gerente: ")
gerente1.set_nombre(input("ingresa tu nombre por favor"))
gerente1.set_salario(int(input("ingresa tu salario por favor \n sin puntos :")))
gerente1.set_antiguedad (input("ingresa tu antiguedad por favor"))
gerente1.set_rol(input("ingrese su rol porfavor: "))
gerente1.mostrar()


