
class Persona:
	def __init__(self,nombre,edad):
		self.__nombre = nombre
		self.__edad = edad

	def getNombre(self):
		return self.__nombre
	def setNombre(self, nuevo):
		self.__nombre = nuevo
	def getEdad(self):
		return self.__edad
	def setEdad(self, nuevo):
		self.__edad = nuevo

	def __str__(self):
		return f"Nombre : {self.__nombre}"
#SUPER LLAMA AL PADRE
class Estudiante(Persona):
	def __init__(self, nombre, edad, legajo):
		super().__init__(nombre,edad)
		self.__legajo = legajo

	def getLegajo(self):
		return self.__legajo

	def setLegajo(self,nuevo):
		self.__legajo = nuevo
	def __str__(self):
		return f"{super().__str__()}, Legajo: {self.__legajo}"

e1 = Estudiante('Nicolas',30,10)
print(e1)
e1.setNombre('Pedro')
print(e1)