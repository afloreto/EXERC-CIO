# 33. Peça ao usuário para inserir 10 palavras em uma lista. • Crie uma nova lista contendo apenas palavras que começam com uma vogal. • Exiba a lista original e a filtrada.

def filtrar_palavras_vogais():                  # função para filtrar palavras que começam com vogais
    palavras = []

    print('Informe 10 palavras!')

    for i in range(10):                         # loop para solicitar 10 palavras ao usuário
        while True:
            palavra = input(f'Informe a {i+1}ª palavra: ')
            if palavra.isalpha():                   # verifica se a palavra contém apenas letras
                palavras.append(palavra)            # adiciona a palavra à lista se for válida
                break
            else:
                print('Palavra inválida! Informe apenas letras.')

    palavras_vogais = [palavra for palavra in palavras if palavra[0].lower() in 'aeiou']   # filtra palavras que começam com vogais

    print('Lista original:')
    print(palavras)

    print('Lista filtrada (palavras que começam com vogal):')
    print(palavras_vogais if palavras_vogais else 'Nenhuma palavra encontrada que comece com vogal.')

filtrar_palavras_vogais()           # chamada da função para executar o código