'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que
es una persona) y cantidad (puede tener decimales). El titular será obligatorio y
la cantidad es opcional.
Implementa los siguientes métodos:
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
					introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
					números rojos
'''

class Persona:
	def __init__(self,nombre, apellido,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def __str__(self):
		return f"{self.apellido}, {self.nombre}"


class Cuenta:
	def __init__(self, titular, cantidad=0):
		self.titular = titular
		self.cantidad = cantidad

	def mostrar(self):
		print("Titular:", self.titular)
		print("Cantidad:", self.cantidad)

	def ingresar(self, cantidad):
		if cantidad > 0:
			self.cantidad += cantidad

	def retirar(self, cantidad):
		self.cantidad -= cantidad

p1 = Persona('Elizabeth','Barrios', 18)

Cuenta1 = Cuenta(p1, 120000)
Cuenta1.mostrar()

retirar = float(input(f"ingrese por favor ingrese el monto a retirar: "))
Cuenta1.retirar(retirar)
Cuenta1.mostrar()

ing = float(input(f"ingrese por favor ingrese el monto a ingresar: "))
Cuenta1.ingresar(ing)
Cuenta1.mostrar()