#Faça um algoritimo que leia a altura de 20 pessoas e calcule a media aritmética das alturas

soma = 0
cont = 0
while cont < 20:
    cont = cont + 1
    altura = float(input("digite a altura: "))
    soma = soma + altura
print(soma / cont)