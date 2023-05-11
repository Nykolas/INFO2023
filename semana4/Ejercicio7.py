'''
def imprimirPares(numero):
	for x in range (2, numero + 1, 2):
		print (x)

numero = int(input("Introduzca un valor: "))
imprimirPares(numero)
'''

def imprimir_pares(n):
	for i in range(1,n+1):
		if i % 2 == 0:
			print(f'los numeros pares son{i}')


a = int(input('ingrese un numero: '))
imprimir_pares(a)
	