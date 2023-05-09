'''
Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso
'''

#OP 1
palabra = input("INGRESE UNA PALABRA: ")

#LIST() CREA LISTA DEL PARAMETRO
pl = list(palabra)

pl.reverse()

for x in pl:
	print(x)


#OP 2
palabra = input("Escriba cualquier palabra: ")

for i in range(len(palabra), 0, -1):
	print(palabra[i-1])
