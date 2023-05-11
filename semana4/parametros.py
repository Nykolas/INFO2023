#TODOS LOS PARAMETROS SON POSICIONALES

def suma(a,b):
	r = a + b
	return r

print(f"OPCION 1 {suma(4,4)}")
#a y b son obligatorios

def suma2(a,b=5):
	r = a + b
	return r

print(f"OPCION 2 {suma2(3)}")
#a es obligatorio, b es ocpional (si no se pasa b, vale por defecto 5)

def suma3(a=0,b=5):
	r = a + b
	return r

print(f"OPCION 3 {suma3()}")
#a y b son ocpionales