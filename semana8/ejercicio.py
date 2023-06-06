class Estudiante:

	def __init__(self,leg,nom):
		self.legajo = leg
		self.nombre = nom
		self.notas = []
	
	def mostrar_nombre(self):
		return f"Mi nombre es: {self.nombre}"

	def cargar_notas(self,n):
		self.notas.append(n)

	def calcular_promedio(self):
		promedio = 0
		for n in self.notas:
			promedio = promedio + n 

		return promedio/len(self.notas)

#### MAIN

cantidad = int(input("cuantos estudiantes quiere cargar?"))
lista_estudiantes = []

for i in range(1,cantidad+1):
	leg = int(input(f"ingrese el legajo del estudiante {i}: "))
	nombre = input(f"ingrese el nombre del estudiante {i}: ")

	e = Estudiante(leg,nombre)
	lista_estudiantes.append(e)

print("VAMOS A CARGAR LAS NOTAS")

#SUPONEMOS QUE SON 3 NOTAS
for i in lista_estudiantes:
	print(f"Cargemos las notas de {i.mostrar_nombre()}")
	n1 = int(input("NOTA 1: "))
	n2 = int(input("NOTA 2: "))
	n3 = int(input("NOTA 3: "))
	i.cargar_notas(n1)
	i.cargar_notas(n2)
	i.cargar_notas(n3)

print("NOTAS YA FUERON CARGADAS ")

################################################################

for estu in lista_estudiantes:
	print(f"EL promedio de {estu.mostrar_nombre()} es {estu.calcular_promedio()}")