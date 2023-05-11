
def contar_vocales(cadena):
	vocales = "aeiouAEIOU"
	count = 0
	for letra in cadena:
		if letra in vocales:
			count += 1
	return count

texto = input("Ingrese una cadena de texto: ")
num_vocales = contar_vocales(texto)
print("El número de vocales en la cadena es:", num_vocales)