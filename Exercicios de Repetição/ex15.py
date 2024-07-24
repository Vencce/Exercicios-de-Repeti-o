#Fazer um algoritimo que calcule e escreva a soma dos 20 primeiros termos da serie: 100/0! + 99/1! + 98/2! + ...

soma = 0
cont = 0
while cont < 20:
    cont = cont + 1
    fat = 1
    for i in range(1, cont):
        fat = fat * i
    soma = soma + (cont / fat)
print(soma)
