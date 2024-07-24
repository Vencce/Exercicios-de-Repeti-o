#Em uma disputa de pingue-pongue os pontos são anotados como D, ponto para ojogador do lado direito, e E, ponto para o jogador do lado esquerdo da mesa. Faça umalgoritmo que leia o código do ponto de cada jogada e determine o vencedor. Apartida encerra quando:a) um dos jogadores chegar a 21 pontos e a diferença de pontos entre os jogadores formaior ou igual a dois;b) o jogador com mais de 21 pontos conseguir uma diferença de dois pontos sobre oadversário, caso a primeira condição não seja atendida.

D = float(input("digite o ponto para ojogador do lado direito: "))
E = float(input("digite o ponto para o jogador do lado esquerdo da mesa: "))

if D == 21 or E == 21:
    print("a partida encerrou")
elif D == E + 2:
    print("o vencedor foi o do lado direito")
elif E == D + 2:
    print("o vencedor foi o do lado esquerdo")
else:
    print("a partida encerrou")
    



