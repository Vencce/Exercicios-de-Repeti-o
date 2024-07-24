#Faça um algoritmo que leia n números inteiros e escreva, para cada número lido, os divisores e quantidade de divisores. EXEMPLO: número lido = 12 divisores = 1, 2, 3, 4, 6, 12 quantidade divisores = 6

n = 0
soma = 0
somaDivisores = 0
cont = 0
while n != 0:
    n = int(input("digite um numero: "))
    if n != 0:
        cont = cont + 1
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)
                somaDivisores = somaDivisores + 1
print(somaDivisores, cont)