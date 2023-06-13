class Vehiculo:
	def __init__(self, ruedas, color):
		self.__ruedas = ruedas
		self.__color = color

	def getRuedas(self):
		return self.__ruedas
	def setRuedas(self,nuevas):
		self.__ruedas = nuevas
	def getColor(self):
		return self.__color
	def setColor(self,nuevas):
		self.__color = nuevas

class Coche(Vehiculo):
	def __init__(self,ruedas, color, velocidad, cilindrada):
		super().__init__(ruedas,color)
		self.__velocidad = velocidad
		self.__cilindrada = cilindrada
	def getVelocidad(self):
		return self.__velocidad
	def setVelocidad(self,nuevas):
		self.__velocidad = nuevas
	def getCilindrada(self):
		return self.__cilindrada
	def setCilindrada(self,nuevas):
		self.__cilindrada = nuevas