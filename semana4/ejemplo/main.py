'''
Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario
'''
#SINTAXiS PARAiMPORTAR MiS FuNCIONES
#FROM NOMBRE_DEL_ARCHIVO IMPORT NOMBRE DE LA FUNCION
from funciones import es_divisible

a = int(input("INGRESE EL PRIMER NUMERO: "))
b = int(input("INGRESE EL SEGUNDO NUMERO: "))

resultado = es_divisible(a,b)

print(resultado)