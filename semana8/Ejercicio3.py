class Triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def imprimir_lado_mayor(self):
		mayor = max(self.lado1, self.lado2, self.lado3)
		print(f'El lado mayor es --> {mayor}')

	def tipo_triangulo(self):
		if self.lado1 == self.lado2 == self.lado3:
			print('El tríangulo es EQUILATERO')
		elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
			print('El tríangulo es ISÓSCELES')
		else:
			print('El tríangulo es ESCALENO')



lado1 = float(input('Ingrese el primer lado del tríangulo: '))
lado2 = float(input('Ingrese el segundo lado del tríangulo: '))
lado3 = float(input('Ingrese el tercer lado del tríangulo: '))

triangulo = Triangulo(lado1, lado2, lado3)
triangulo.tipo_triangulo()
triangulo.imprimir_lado_mayor()