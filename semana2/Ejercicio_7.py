'''
Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial.
'''

caracter = input("Ingrese un carácter: ")

if caracter.isalpha():

	if caracter.isupper():
		print(f"El carácter que usted ingreso {caracter} es una letra mayuscula")
	else:
		print(f"El carácter que usted ingreso {caracter} es una letra minuscula")

elif caracter.isdigit():

	print(f"El carácter que usted ingreso {caracter} es un numero")

else:
	
	print(f"El carácter que usted ingreso {caracter} es especial")