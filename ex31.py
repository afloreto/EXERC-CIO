# 31. Solicite ao usuário que insira 10 números em uma lista. • Exiba os números em ordem crescente. • Exiba os números em ordem decrescente. • Exiba apenas os valores pares.

def lista_numeros():                # função para solicitar e exibir números
    numeros = []

    print('Informe 10 números!')

    for i in range(10):         # loop para solicitar 10 números ao usuário
        while True:
            try:
                num = int(input(f'Informe o {i+1}º número: '))
                numeros.append(num)           # adiciona o número a lista se for válido
                break
            except ValueError:              # verifica se o valor informado é um número inteiro
                print('Número inválido! Informe um número inteiro.')

    print('Números em ordem crescente: ')
    print(sorted(numeros))           # exibe os números em ordem crescente

    print('Números em ordem decrescente: ')
    print(sorted(numeros, reverse=True))          # exibe os números em ordem decrescente

    print("Números pares: ")
    pares = [num for num in numeros if num % 2 == 0]              # filtra os números pares
    print(pares if pares else 'Nenhum número par encontrado.')        # exibe os números pares ou mensagem se não houver

lista_numeros()                           # chamada da função para executar o código
