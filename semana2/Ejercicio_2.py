'''
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero.
'''

n = int(input("INGRESE UN NUMERO ENTERO: "))

#OPCION 1
if (n > 0):
	print("EL NUMERO INGRESADO ES POSITIVO")
elif (n < 0):
	print("EL NUMERO INGRESADO ES NEGATIVO")
else:
	print("EL NUMERO ES IGUAL A CERO")

#OPCION 2
if (n > 0):
	print("EL NUMERO INGRESADO ES POSITIVO")
else:
	if (n < 0):
		print("EL NUMERO INGRESADO ES NEGATIVO")
	else:
		print("EL NUMERO ES IGUAL A CERO")