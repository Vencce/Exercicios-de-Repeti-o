#Faça um algoritmo que leia valores, sendo que cada valor representa a idade de uma pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser computados no cálculo valores maiores do que zero. O algoritmo deve apresentar ao usuário a seguinte mensagem: deseja digitar mais um valor: s (SIM) / n (NAO)?, antes de prosseguir com a entrada de dados.

soma = 0
cont = 0
while True:
    idade = int(input("digite a idade: "))
    if idade > 0:
        soma = soma + idade
        cont = cont + 1
    else:
        break
print(soma / cont)