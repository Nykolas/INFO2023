class Estudiante:
	#DEFINICIO ATRIBUTOS
	def __init__(self,leg,nom):
		self.__legajo = leg
		self.__nombre = nom

	#DEFINICIO METODOS
	def __mostrar_nombre(self):
		return f"Mi nombre es: {self.__nombre}"

	def set_legajo(self,leg):
		if leg > 10:
			self.__legajo = leg

	def __str__(self):
		return f"legajo {self.__legajo}, nombre {self.__nombre}"

####################################################

e1 = Estudiante(10,'Nicolas')

print(e1)
#SIN ENCAPSULAMIENTO
e1.legajo = 5
print(e1)
#CON ENCAPSULAMIENTO
e1.set_legajo(20)
print(e1)

print(e1.__mostrar_nombre())