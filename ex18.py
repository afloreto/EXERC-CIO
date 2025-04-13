#18. Ordenar uma lista em ordem crescente: Crie uma função que receba uma lista de números como entrada e retorne a mesma lista ordenada em ordem crescente (conhecimentos da resenha feita em casa).

def ordenar_lista(lista):                           # função para ordenar a lista
    return sorted(lista)                                # retorna a lista ordenada em ordem crescente

lista_de_numeros = []                                   # lista para armazenar os números inseridos pelo usuário

print("Digite 10 números para adicionar à lista:")                              # solicita ao usuário para inserir os números
for i in range(10):                                     # loop para inserir 10 números
    numero = int(input(f"Número {i + 1}: "))                    # solicita o número ao usuário
    lista_de_numeros.append(numero)                     # adiciona o número à lista
    
print('Lista em ordem crescente:', ordenar_lista(lista_de_numeros))              # imprime a lista ordenada em ordem crescente


