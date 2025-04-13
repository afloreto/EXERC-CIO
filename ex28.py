# 28. Crie um programa que gerencie um estoque de produtos: • O usuário deve poder adicionar produtos (nome e quantidade). • Permita a busca por um produto específico e exiba sua quantidade. • Ofereça a opção de atualizar a quantidade de um produto. • Exiba o estoque completo ao final.

lista_de_produtos = {}                               # dicionário para armazenar os produtos e suas quantidades
print("-------- Sistema de Gerenciamento de Estoque -------- ")

print("Digite 'adicionar' para adicionar um produto, 'buscar' para buscar um produto, 'atualizar' para atualizar a quantidade de um produto ou 'sair' para finalizar o programa.") 

while True:
    acao = input("Escolha uma ação: ")                      # solicita ao usuário a ação desejada
    if acao == "adicionar":
        nome_produto = input("Digite o nome do produto: ")
        quantidade_produto = int(input("Digite a quantidade do produto: "))                     # solicita a quantidade do produto
        lista_de_produtos[nome_produto] = quantidade_produto                            # adiciona o produto e sua quantidade ao dicionário
        print(f"Produto '{nome_produto}' adicionado ao estoque com quantidade {quantidade_produto}.")
    elif acao == "buscar":
        nome_produto = input("Digite o nome do produto que deseja buscar: ")
        if nome_produto in lista_de_produtos:
            print(f"Produto '{nome_produto}' encontrado com quantidade {lista_de_produtos[nome_produto]}.")
        else:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")
    elif acao == "atualizar":
        nome_produto = input("Digite o nome do produto que deseja atualizar: ")
        if nome_produto in lista_de_produtos:
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            lista_de_produtos[nome_produto] = nova_quantidade
            print(f"Quantidade do produto '{nome_produto}' atualizada para {nova_quantidade}.")
        else:
            print(f"Produto '{nome_produto}' não encontrado no estoque.")
    elif acao == "sair":
        print("Programa encerrado! Estoque final:")
        for produto, quantidade in lista_de_produtos.items():
            print(f"{produto}: {quantidade}")
        break