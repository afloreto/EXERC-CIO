# 15. Calcular a média de alguns números: Crie um programa que receba uma quantidade de números definido pelo usuário e retorne a média dos valores presentes na lista.

quantidade = int(input('Digite a quantidade de números que você deseja calcular a média: '))
numeros = []

for i in range(quantidade):
    numero = float(input(f'Digite o {i + 1}º número: '))
    numeros.append(numero)

media = sum(numeros) / quantidade
print(f'A média dos números é: {media}')


