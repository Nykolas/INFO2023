'''
Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante.
'''

#OPCION 1
letra = input("ingrese letra: ")

if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
	print("Es una vocal")
else:
	print("Es una consonante")

#OPCION 2
letra = input('Ingresá una letra: ')

if letra.lower() in 'aeiou':
	print('Ingresaste una vocal')
else:
	print('Ingresaste una consonante')

#OPCION 3
letra = input("Ingrese una letra: ")
if letra in "aeiouAEIOU":
	print(f"la letra que usted ingreso es una Vocal")
else:
	print(f"La letra que usted ingreso es una consonante")

#OPCION 4
letra= input("ingrese un letra: ")
#LISTA
vocales=['a','e','i','o','u','A','E','I','O','U']

if letra in vocales:
	print("es vocal")
else:
	print("es consonante")