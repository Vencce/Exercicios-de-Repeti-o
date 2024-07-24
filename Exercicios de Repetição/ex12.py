#Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos: 1/1 + 1/2 + 1/3 + ... + 1/100

soma = 0
cont = 0
while cont < 100:
    cont = cont + 1
    soma = soma + (1 / cont)
print(soma)
