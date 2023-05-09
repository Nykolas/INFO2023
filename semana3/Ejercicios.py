#un ejercicio de cuantos caracteres tiene una cadena de texto contando los blancos
'''
texto = input("INGRESE UN TEXTO: ")

cant = 0

for x in texto:
	cant = cant + 1

print(f"La cantidad de caracteres es de: {cant}")
'''

#un ejercicio de cuanto palabras tiene una cadena de texto contando los blancos

texto = input("INGRESE UN TEXTO: ")

#HOLA MUNDO NUESTRO
#OP 1
'''
cant = 0
for x in texto:
	if x == ' ':
		cant = cant + 1

cant = cant + 1
print(f"La cantidad de palabras es de: {cant}")
'''
#OP 2
'''
palabras = texto.split()
cantidad = len(palabras)
print(f"La cantidad de palabras es de: {cantidad}")
'''
#OP 3

palabras = texto.split()

cant = 0
for x in palabras:
	cant = cant + 1
	
print(f"La cantidad de palabras es de: {cant}")
