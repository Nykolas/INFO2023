
'''
3 PARTES:
1 - ENTRAR DATOS
2 - PROCESARLOS
3 - MOSTRAR/SALIDA DATOS
'''
'''
LOS DATOS LOS GUARDO EN VARIABLES (ESPACIOS DE MEMORIA CON NOMBRE)
TIPOS DE DATOS:
DATOS SIMPLES:
	numericos (enteros, reales --- int , float, decimal)
	alfanumericos (palabras --- str)
	logicos (Verdedore o Falso --- bool)
DATOS COMPLEJOS (DATOS ESTRUCTURADOS):
	listas
	tuplas
	diccionarios

PARA SABER QUE TIPO DE DATOS ES UNA VARIABLE PUEDO USAR LA FUNCION type

type(x) ---- me dice el tipo de datos de la variable x



persona_1 = "NICOLAS"

#MUESTRA EL TIPO DE DATO DE LA VARIABLE PERSONA
print(type(persona_1))
#MUESTRA EL CONTENIDO DE LA VARIABLE PERSONA
print(persona_1)

'''

# PARA INGRESAR DATOS

# input es una funcion que toma lo que el usuario escribe por consola y a eso lo guarda en la variable
# a la cual es asignado (en este caso a V1)
# siempre, siempre y siempre el valor tomado por el input es un STR
# si yo quiero que sea un numero lo debo convertir.

nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")


# PARA MOSTRAR DATOS SE USA LA FUNCION PRINT
# f es de format, une el texto literal con el contenido de las variables
# lo que esta entre llaves lo toma como variable, es decir busca contenido

print(f"EL NOMBRE QUE USTED INGRESO ES: {nombre} Y SU APELLIDO ES {apellido}")

# PASAR DE UN TIPO A OTRO

# int(x) ---> pasar el contenido de x a entero (si es posible)
# float(x) ---> pasa el contenido de x a flotante (si es posible)
# str(x) ---> pasa el contenido de x a un str