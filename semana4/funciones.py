
#FUNCIONES:
#def NOMBRE (PARAMETROS):

def suma(x,y):
	r = x + y
	return r

def suma2(x,y):
	r = x + y
	print(f"la suma es {r}")

#LA FUNCION SOLO SE EJECUTA CUANDO ALGUIEN LA LLAMA
##############################

a = int(input("INGRESE EL PRIMER NUMERO: "))
b = int(input("INGRESE EL SEGUNDO NUMERO: "))

#SI LA FUNCION RETORNA ALGO
resultado = suma(a,b)
print(f"la suma es {resultado}")
#---------------------------------------------------------------------------#

#SUMA2 NO RETORNA NADA
suma2(a,b)

#INTERNAMENTE ES COMO SI PYTHON LE ASIGNARA A x = a, y = b.


