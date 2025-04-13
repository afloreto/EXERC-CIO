# 19. Uma pessoa deseja otimizar a sua lista de compras para isso criar um algoritmo que permita a inclusão dos itens faltantes em uma lista.

def lista_de_compras():         # função para otimizar a lista de compras
    lista = []                  # lista para armazenar os itens da lista de compras

    print("--------------------------------------------------")
    print("Informe os itens que estão faltando na sua lista. Digite 'fim' para encerrar.")
    print("--------------------------------------------------")
    

    while True:
        item = input("Adicionar item: ")           # solicita ao usuário para inserir o item   

        if item == 'fim':              
            break
        elif item == "":
            print("Item vazio! Tente novamente.")
        elif item in lista:
            print(f"'{item}' já está na lista.")
        else:
            lista.append(item)
            print(f"'{item}' adicionado à lista.")

    print("Lista de compras final: ")
    for i, item in enumerate(lista, start=1):               
        print(f"{i}. {item}")          # mostra a lista de compras final com os itens adicionados

lista_de_compras()       # chama a função para executar o programa
