#O valor aproximado do número pi pode ser calculado usando-se a série: S = 1 - 1/3^3 + 1/5^3 - 1/7^3 + ...

soma = 0
cont = 0
while cont < 100:
    cont = cont + 1
    if cont % 3 == 0:
        soma = soma - (1 / (cont ** 3))
    else:
        soma = soma + (1 / (cont ** 3))
print(soma)