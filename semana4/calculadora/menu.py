
def menu():

	while True:
		print("1: sumar")
		print("2: restar")
		print("3: dividir")
		print("4: multiplicar")
		print("5: salir")
		respuesta = int(input())
		
		if respuesta not in [1,2,3,4,5]:
			print("INGRESE UNA OPCION VALIDA")
		else:
			break

	return respuesta