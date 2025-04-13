# 20. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0                   # inicializa o contador de pares
impares = 0                 # inicializa o contador de ímpares

print('Informe 10 números inteiros:')

for i in range(10):             # loop para solicitar 10 números
    numero = int(input(f'Informe o {i+1}º número: '))                   # solicita o número inteiro
    if numero % 2 == 0:                             # verifica se o número é par
        pares += 1                              # incrementa o contador de pares
    else:
        impares += 1                            # incrementa o contador de ímpares

print(f'A quantidade de números pares é: {pares}')
print(f'A quantidade de números ímpares é: {impares}')
