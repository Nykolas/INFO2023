from funciones import suma,resta,multiplicacion,division
from menu import menu

print("-------CALCULADORA-------")

opcion = menu()

while opcion != 5:
	
	x = int(input("INGRESE NUMERO 1: "))
	y = int(input("INGRESE NUMERO 2: "))

	if opcion == 1:
		r = suma(x,y)
	elif opcion == 2:
		r = resta(x,y)
	elif opcion == 3:
		r = division(x,y)
	elif opcion == 4:
		r = multiplicacion(x,y)

	print(f"el resultado de la operacion es: {r}")
	print("")
	opcion = menu()

print("GRACIAS POR USAR !CALCULADORA!")