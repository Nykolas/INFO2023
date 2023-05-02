# CONDICIONALES ANIDADOS (CONDICIONALES DENTRO DE CONDICIONALES)
# INDICAR SI UNA PERSONA PUEDE JUBILAR, TENER CUENTA QUE LOS HOMBRES SE JUBILAN A LOS 65
# Y LAS MUJERES A LOS 60

edad = int(input("ingrese su edad: "))
sexo = input("ingrese su sexo de forma M o H: ")

if sexo == 'H':

	if edad >= 65:
		print("SE PUEDE JUBILAR")
	else:
		print("NO SE PUEDE JUBILAR")

else:
	
	if edad >= 60:
		print("SE PUEDE JUBILAR")
	else:
		print("NO SE PUEDE JUBILAR")