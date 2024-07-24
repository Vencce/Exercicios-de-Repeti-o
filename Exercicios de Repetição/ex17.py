#Foi feita uma pesquisa de audiência de canal de TV em n casas de um determinado bairro de Joinville, em um certo dia do mês. Na pesquisa foi utilizado um coletor de dados portátil. Para cada casa visitada, foi fornecido o número do canal (4, 5, 9, 12) e o número de pessoas que estavam assistindo a TV naquele horário, considerando que em cada casa só existia uma televisão. Em casas onde a televisão estava desligada, foi registrado zero para o número do canal e para o número de pessoas. Faça um algoritmo que calcule e escreva, para cada emissora, o percentual de audiência.

n = 0
soma = 0
somaCanal = 0
somaPessoas = 0
cont = 0
while n != 0:
    n = int(input("digite o canal: "))
    if n != 0:
        pessoas = int(input("digite o numero de pessoas: "))
        somaPessoas = somaPessoas + pessoas
        cont = cont + 1
        if n == 4:
            somaCanal = somaCanal + pessoas
        if n == 5:
            somaCanal = somaCanal + pessoas
        if n == 9:
            somaCanal = somaCanal + pessoas
        if n == 12:
            somaCanal = somaCanal + pessoas
print(somaCanal, somaPessoas, cont)