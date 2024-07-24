#faça um algoritimo que leia 20 numeros inteiros e escreva, para cada um, se ele é par ou impar

numero = 0
while numero != 20:
    numero = int(input("digite um numero: "))
    if (numero % 2) == 0:
        print("par")
    else:
        print("impar")