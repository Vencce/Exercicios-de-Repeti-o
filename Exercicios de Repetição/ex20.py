#Uma máquina de biscoito está com problemas. Quando ligada, após 1 hora ela quebra 1 biscoito, na segunda hora ela quebra 3 biscoitos, na hora seguinte ela quebra 3 vezes a quantidade de biscoitos quebrados na hora anterior, e assim por diante. Faça um algoritmo que calcule quantos biscoitos são quebrados no final de cada dia (a máquina opera 16 horas por dia).

n = 0
soma = 0
cont = 0
while n != 0:
    n = int(input("digite o numero de biscoitos: "))
    if n != 0:
        soma = soma + n
        cont = cont + 1
print(soma, cont)
