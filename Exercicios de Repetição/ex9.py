#Faça um algoritmo que calcule e imprima os valores de y, onde: y = 3 + 2x + 6x^2/ 1+ 9x + 16x^2, para x variando de 1.0 até 5.0, em intervalos de 0.1 unidades.

# Função para calcular o valor de y
def calcular_y(x):
    numerador = 3 + 2 * x + 6 * x ** 2
    denominador = 1 + 9 * x + 16 * x ** 2
    y = numerador / denominador
    return y

# Calcular e imprimir os valores de y para x de 1.0 a 5.0 em intervalos de 0.1
x = 1.0
while x <= 5.0:
    y = calcular_y(x)
    print(f"Para x = {x:.1f}, y = {y:.6f}")
    x += 0.1