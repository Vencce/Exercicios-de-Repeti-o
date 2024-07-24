#Dado um conjunto de valores inteiros, mostre quantos valores pares existem no conjunto e qual é o menor e o maior. Um numero com valor 0 (zero) encerra o programa.

soma = 0
cont = 0
menor = 0
maior = 0
numero = 1

while numero != 0:
    numero = int(input("digite um numero: "))
    if numero > 0:
        if cont == 0:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        soma = soma + numero
        cont = cont + 1
print(soma, cont, maior, menor)