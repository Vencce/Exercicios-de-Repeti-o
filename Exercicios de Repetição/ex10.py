#Construir um algoritmo que calcule o fatorial de um número N.

n = int(input("digite um numero: "))
fatorial = 1
while n > 1:
    fatorial = fatorial * n
    n = n - 1
print(fatorial)