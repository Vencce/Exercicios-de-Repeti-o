#faça um algoritimo que leia 20 numeros inteiros, escreva os numeros que são negativos e escreva a média dos positivos

numero = 0
soma = 0
cont = 0
while numero != 20:
    numero = int(input("digite um numero: "))
    if numero < 0:
        print(numero)
    if numero > 0:
        soma = soma + numero
        cont = cont + 1
print(soma / cont)