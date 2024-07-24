#Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva: • o número de inscrição e a altura do atleta mais alto; • o número de inscrição e a altura do atleta mais baixo; • a altura média do grupo de atletas

n = 0
soma = 0
somaAltura = 0
cont = 0
contAltura = 0
contAlturaBaixa = 0
while n != 0:
    n = int(input("digite o numero de inscricao: "))
    if n != 0:
        altura = float(input("digite a altura: "))
        cont = cont + 1
        soma = soma + altura
        if altura > contAltura:
            contAltura = altura
            numAltura = n
        if altura < contAlturaBaixa:
            contAlturaBaixa = altura
            numAlturaBaixa = n
        somaAltura = somaAltura + altura

print(numAltura, contAltura, numAlturaBaixa, contAlturaBaixa, soma / cont)