#Uma loja de departamentos oferece para seus clientes um determinado desconto de acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra seja maior que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar. Um nome de cliente igual a ULTIMO indica o fim da entrada de dados.

soma = 0
cont = 0
nome = input("digite o nome do cliente: ")
while nome != "ULTIMO":
    valor = float(input("digite o valor da casa: "))
    if valor > 500:
        desconto = valor * 0.20
    else:
        desconto = valor * 0.15
    soma = soma + (valor - desconto)
    print("desconto de: ", desconto)
    nome = input("digite o nome do cliente: ")
print(soma)