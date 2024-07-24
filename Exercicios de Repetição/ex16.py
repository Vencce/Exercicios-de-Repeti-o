#Fazer um algoritmo que calcule e imprima o valor de ex através da série: e^x = x^0 + x^1/1! + x^2/2! + x^3/3! + ...

soma = 0
cont = 0
x = float(input("digite o valor de x: "))
while cont < 10:
    cont = cont + 1
    fat = 1
    for i in range(1, cont):
        fat = fat * i
    soma = soma + (x ** cont) / fat
print(soma)