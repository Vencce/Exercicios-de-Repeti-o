#Faça um algoritimo que leia n valor inteiros e escreva quantos valores são negativos 

soma = 0
cont = 0
while cont < 10:
    cont = cont + 1
    valor = int(input("digite um valor: "))
    if valor < 0:
        soma = soma + 1
print(soma)