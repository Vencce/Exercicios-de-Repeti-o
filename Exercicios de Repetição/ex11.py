#Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos: 1+2+3+4+...+100

soma = 0
cont = 0
while cont < 100:
    cont = cont + 1
    soma = soma + cont
print(soma)