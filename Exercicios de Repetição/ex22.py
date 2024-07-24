#Faça um algoritmo que: • leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e sexo = 'F' ou sexo = 'f' para feminino); • escreva a média da altura das mulheres; • escreva a média da altura da turma.

n = 0
soma = 0
somaMulher = 0
cont = 0
contMulher = 0
while n != 0:
    n = int(input("digite o numero de pessoas: "))
    if n != 0:
        sexo = input("digite o sexo (m/f): ")
        altura = float(input("digite a altura: "))
        if sexo == 'm' or sexo == 'M':
            somaMulher = somaMulher + altura
            contMulher = contMulher + 1
        soma = soma + altura
        cont = cont + 1
print(somaMulher / contMulher, soma / cont)