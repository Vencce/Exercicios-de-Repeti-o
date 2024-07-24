#Uma turma tem 50 alunos. Faça um algoritmo que: • leia para cada aluno o seu nome e idade; • escreva os nomes dos alunos que tem 18 anos; • escreva a quantidade de alunos que tem idade acima de 20 anos.

n = 0
soma = 0
cont = 0
while n != 0:
    n = int(input("digite o numero de alunos: "))
    if n != 0:
        nome = input("digite o nome do aluno: ")
        idade = int(input("digite a idade do aluno: "))
        if idade > 20:
            print(nome)
            cont = cont + 1
print(cont)