#Fazer um algoritmo para calcular o valor de S, dado por: S= 1/N + 2/N-1 + 3/N-2 + ... + N -1/2 + N/1

soma = 0
cont = 0
while cont < 10:
    cont = cont + 1
    if cont == 1:
        soma = soma + 1
    else:
        soma = soma + (cont / (cont - 1))
print(soma) 