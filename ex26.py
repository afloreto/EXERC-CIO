# 26. Implemente um programa onde o usuário pode: Adicionar itens a uma lista de compras. Exibir todos os itens na lista. Remover um item específico, caso o usuário deseje. Finalizar o programa exibindo a lista final.

listas_de_compras = []          # lista para armazenar os itens de compras
print("-------- Sistema de Lista de Compras -------- ")         # exibe o título do sistema

print("Digite 'adicionar' para adicionar um item, 'exibir' para ver a lista, 'remover' para remover um item ou 'sair' para finalizar o programa.")              # instruções iniciais

while True:
    acao = input("Escolha uma ação: ").strip().lower()          # solicita ao usuário a ação desejada
    if acao == "adicionar":
        item = input("Digite o item que deseja adicionar: ").strip()         # solicita o item a ser adicionado
        listas_de_compras.append(item)              # adiciona o item a lista
        print(f"Item '{item}' adicionado à lista de compras.")              # exibe confirmação
    elif acao == "exibir":
        if listas_de_compras:
            print("Lista de Compras:")
            for i, item in enumerate(listas_de_compras, start=1):           # exibe os itens da lista com numeração
                print(f"{i}. {item}")
        else:
            print("A lista de compras está vazia.")
    elif acao == "remover":
        if listas_de_compras:
            item = input("Digite o item que deseja remover: ").strip()          # solicita o item a ser removido
            if item in listas_de_compras:
                listas_de_compras.remove(item)          # remove o item da lista
                print(f"Item '{item}' removido da lista de compras.")       # exibe confirmação
            else:
                print(f"Item '{item}' não encontrado na lista.")
        else:
            print("A lista de compras está vazia.")
    elif acao == "sair":
        print("Programa encerrado! Lista final de compras:")            # exibe mensagem de encerramento
        for i, item in enumerate(listas_de_compras, start=1):           # exibe os itens da lista final com numeração
            print(f"{i}. {item}")
        break           # encerra o loop e o programa
    else:
        print("Ação inválida! Tente novamente.")            # mensagem de erro para ações inválidas
        