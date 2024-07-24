#Foi feita uma pesquisa do consumo mensal de energia elétrica em uma determinada cidade. Para cada consumidor, são fornecidos os seguintes dados: número de identificação do consumidor, quantidade de kWh consumidos durante o mês, código do tipo de consumidor (R - residencial, C - comercial, I - industrial). Faça um algoritmo que: a) leia o preço do kWh por tipo de consumidor; b) leia os dados de n consumidores; c) escreva o número de identificação e o total a pagar, para cada consumidor; d) escreva a quantidade total de KWh consumida para cada um dos três tipos de consumidores; e) escreva a quantidade média geral de consumo.

n = 0
soma = 0
somaResidencial = 0
somaComercial = 0
somaIndustrial = 0
cont = 0
while n != 0:
    n = int(input("digite o numero de identificação do consumidor: "))
    if n != 0:
        kWh = float(input("digite a quantidade de kWh consumidos: "))
        tipo = input("digite o tipo de consumidor (R - residencial, C - comercial, I - industrial): ")
        if tipo == "R":
            somaResidencial = somaResidencial + kWh
        if tipo == "C":
            somaComercial = somaComercial + kWh
        if tipo == "I":
            somaIndustrial = somaIndustrial + kWh
        soma = soma + kWh
        cont = cont + 1
print(somaResidencial, somaComercial, somaIndustrial, soma / cont)