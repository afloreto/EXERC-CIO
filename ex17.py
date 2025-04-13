# 17. Contar a quantidade de vogais em uma palavra: Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra (conhecimentos da resenha feita em casa).

def contar_vogais(palavra):  # função para contar vogais
    vogais = "aeiouAEIOU"    # define as vogais
    contador = sum(1 for letra in palavra if letra in vogais)   # conta as vogais
    return contador  # retorna o contador

palavra = input('Informe uma palavra: ')    # solicita ao usuário para informar uma palavra
print(f"A quantidade de vogais na palavra '{palavra}' é: {contar_vogais(palavra)}")  # exibe a quantidade de vogais na palavra
