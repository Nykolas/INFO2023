'''
Crea un programa que pida al usuario el radio de un círculo y muestre su
diámetro, su circunferencia y su área.
Supón que pi es aproximadamente 3.14159
'''

PI = 3.14159

radio = float(input("ingrese el radio de un circulo: "))

diametro = radio * 2
circunferencia = 2 * PI * radio
area = PI * radio ** 2

print(f"El diametro del círculo es: {diametro}")
print(f"La circunferencia del círculo es: {circunferencia}")
print(f"El área del círculo es: {area}")