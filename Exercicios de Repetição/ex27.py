#Um motorista acaba de voltar de um feriado prolongado. Antes de sair de viagem eimediatamente após retornar, o motorista encheu o tanque do veículo e registrou asmedidas do odômetro. Em cada parada feita durante a viagem, foi registrado o valordo odômetro e a quantidade de combustível comprado para reabastecer o veículo(suponha que o tanque ficou vazio e foi enchido a cada parada). Faça um algoritmoque leia o número total de reabastecimentos feitos (incluindo o primeiro) e os dadosregistrados relativos à compra de combustível. Calcule e escreva:a) a quilometragem obtida por litro de combustível entre cada par de paradasb) a quilometragem média obtida por litro de combustível em toda a viagem.

n = 0
soma = 0
somaQuilometragem = 0
cont = 0
while n != 0:
    n = int(input("digite o numero de reabastecimentos: "))
    if n != 0:
        km = float(input("digite a quilometragem: "))
        litros = float(input("digite a quantidade de litros: "))
        cont = cont + 1
        soma = soma + km
        somaQuilometragem = somaQuilometragem + km / litros
print(somaQuilometragem / cont)
