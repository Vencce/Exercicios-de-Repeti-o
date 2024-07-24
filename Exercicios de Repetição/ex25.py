#Um hotel cobra R$ 50,00 de diária por hóspede e mais uma taxa de serviços. A taxa de serviços é de: • R$ 7,50 por diária, caso o número de diárias seja menor que 15; • R$ 6,50 por diária, caso o número de diárias seja igual a 15; • R$ 5,00 por diária, caso o número de diárias seja maior que 15. Faça um algoritmo que apresente as seguintes opções ao recepcionista:1. encerrar a conta de um hóspede 2. verificar número de contas encerradas 3. finalizar a execução Caso a opção escolhida seja a primeira, leia o nome e o número de diárias do hóspede e escreva o nome e total a ser pago. Caso a opção escolhida seja a segunda, informe o número de hóspedes que deixaram o hotel (número de contas encerradas).

n = 0
soma = 0
somaDiarias = 0
somaTotal = 0
somaTotalFinal = 0
cont = 0
contTotal = 0
contDiarias = 0

while n != 0:
    n = int(input("digite o numero de diarias: "))
    if n != 0:
        nome = input("digite o nome: ")
        if n < 15:
            somaDiarias = somaDiarias + 1
            somaTotal = somaTotal + 7.5
        if n == 15:
            somaDiarias = somaDiarias + 1
            somaTotal = somaTotal + 6.5
        if n > 15:
            somaDiarias = somaDiarias + 1
            somaTotal = somaTotal + 5
        cont = cont + 1
        somaTotalFinal = somaTotalFinal + somaTotal
        print("total a ser pago:", somaTotal)
print("total de contas encerradas:", cont)
print("total de diarias:", somaDiarias)
print("total a ser pago:", somaTotalFinal)
