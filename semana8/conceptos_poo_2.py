class Estudiante:
	#DEFINICIO ATRIBUTOS
	def __init__(self,leg,nom):
		self.legajo = leg
		self.nombre = nom

	#DEFINICIO METODOS
	def mostrar_nombre(self):
		return f"Mi nombre es: {self.nombre}"

	def __str__(self):
		return f"legajo {self.legajo}, nombre {self.nombre}"

e1 = Estudiante(10,'Nicolas')
print(e1)
print(e1.mostrar_nombre())