#Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a sua massa inicial em Kg, faça um algoritmo que determine o tempo necessário para que essa massa se torne menor que 0,5 gramas. Escreva a massa inicial, a massa final e o tempo.

m = float(input("digite a massa inicial em gramas: "))
while m > 0.5:
    m = m / 2
    print(m)
print("massa final:", m)
print("tempo:", 50 * (m / 0.5))