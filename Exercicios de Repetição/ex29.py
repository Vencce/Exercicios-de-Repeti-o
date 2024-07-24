#Os regulamentos de uma competição de pesca impõem um limite no peso total de pesca de um dia. Faça um algoritmo que leia o limite diário (em quilogramas) e então leia o peso (em gramas) de cada peixe e escreva o peso total da pesca obtido até aquele ponto. Quando o limite diário for excedido escreva uma mensagem e encerre a execução do algoritmo. O algoritmo deve ainda apresentar ao usuário a seguinte mensagem: informar o peso de mais um peixe: s (SIM) / n (NÃO)? antes de prosseguir com a entrada de dados.

soma = 0
cont = 0
while True:
    peso = float(input("digite o peso: "))
    if peso > 0:
        soma = soma + peso
        cont = cont + 1
    else:
        break
print(soma / cont)