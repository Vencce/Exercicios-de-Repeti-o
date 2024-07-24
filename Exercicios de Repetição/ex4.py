#faça um algoritimo que calcule e escreva a soma dos números pares e a soma dos números ímpares entre 1 e 100

soma = 0
somaImpar = 0
cont = 0
while cont < 100:
    cont = cont + 1
    if cont % 2 == 0:
        soma = soma + cont
    else:
        somaImpar = somaImpar + cont
print(soma, somaImpar)  