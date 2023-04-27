'''
5-Crea un programa que pida al usuario dos números enteros y muestre en
pantalla su cociente y su resto
'''
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
cociente = num1 // num2
resto = num1 % num2
print(f'En la DIVISION DE {num1}/{num2} el cociente es: {cociente} y su resto es: {resto}')
