#Uma companhia de teatro planeja dar uma série de espetáculos. A direção calcula que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos. Com a diminuição de R$ 0,50 no preço dos ingressos, espera-se que haja um aumento de 26 ingressos vendidos. As despesas estão estipuladas em R$ 200,00 independente do número de ingressos vendidos. Faça um algoritmo que escreva uma tabela contendo o preço do ingresso, o número de ingressos e o lucro esperado em função do preço do ingresso, fazendo-se variar este preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50. Escreva também o lucromáximo esperado, o preço e o número de ingressos correspondentes.

n = 0
soma = 0
somaLucro = 0
cont = 0
while n != 0:
    n = int(input("digite o numero de ingressos: "))
    if n != 0:
        ingresso = float(input("digite o valor do ingresso: "))
        if ingresso == 5.00:
            soma = soma + 120
            cont = cont + 1
            somaLucro = somaLucro + 120
        if ingresso == 4.00:
            soma = soma + 100
            cont = cont + 1
            somaLucro = somaLucro + 100
        if ingresso == 3.00:
            soma = soma + 80
            cont = cont + 1
            somaLucro = somaLucro + 80
        if ingresso == 2.00:
            soma = soma + 60
            cont = cont + 1
            somaLucro = somaLucro + 60
        if ingresso == 1.00:
            soma = soma + 40
            cont = cont + 1
            somaLucro = somaLucro + 40
print(soma, cont, somaLucro)