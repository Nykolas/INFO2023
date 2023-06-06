#POO

#DEFINO EL MOLDE (LA ESTRUCTURA o EL TIPO DE DATO)
class Estudiante:
	#DEFINICIO ATRIBUTOS
	def __init__(self,leg,nom):
		self.legajo = leg
		self.nombre = nom

	#DEFINICIO METODOS
	def mostrar_nombre(self):
		return f"Mi nombre es: {self.nombre}"


#LA VARIABLE e1 ES DEL TIPO DE DATO ESTUDIANTE, ES DECIR
#QUE CONTIENE SUS ATRIBUTOS Y METODOS

#LA SETENCIA SIGUIENTE QUE SIRVE PARA CREAR UN OBJETO DEL TIPO ESTUDIANTE
#LLAMA AUTOMATICAMENTE AL METODO __init__

e1 = Estudiante(24,'Nicolas')
e2 = Estudiante(30,'Marina')
e3 = Estudiante(45,'Vanesa')


'''
SIN CLASES DEBERIA GUARDAR ALGO ASI:
estudiantes_dic = [
	{'legajo':24, 'nombre':'Nicolas'},
	{'legajo':30, 'nombre:''Marina'},
	{'legajo':45, 'nombre':'Vanesa'}
]
'''

print(e1.mostrar_nombre())


