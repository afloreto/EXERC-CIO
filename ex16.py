# 16. Calcular o fatorial de um número: Crie uma função que calcule o fatorial de um número dado como entrada.

numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i
    print('O fatorial do número', numero, 'é: ', fatorial)