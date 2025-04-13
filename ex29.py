# 29. Simule um controle de presença para uma aula: Cadastre os nomes dos alunos presentes em uma lista. Exiba o número total de alunos presentes. Pergunte ao usuário se deseja buscar o nome de um aluno específico para verificar se ele estava presente.

lista_de_alunos = []  # lista para armazenar os nomes dos alunos presentes
print("-------- Controle de Presença -------- ") 

print("Digite 'adicionar' para adicionar um aluno, 'buscar' para buscar um aluno ou 'sair' para finalizar o programa.")     # instruções iniciais

while True:
    acao = input("Escolha uma ação: ").strip().lower()          # solicita ao usuário a ação desejada
    if acao == "adicionar":
        nome_aluno = input("Digite o nome do aluno: ").strip()
        lista_de_alunos.append(nome_aluno)              # adiciona o nome do aluno a lista
        print(f"Aluno '{nome_aluno}' adicionado à lista de presença.")          # exibe confirmação
    elif acao == "buscar":
        nome_aluno = input("Digite o nome do aluno que deseja buscar: ").strip()        # solicita o nome do aluno a ser buscado
        if nome_aluno in lista_de_alunos:                   # verifica se o aluno está na lista
            print(f"Aluno '{nome_aluno}' estava presente.")
        else:
            print(f"Aluno '{nome_aluno}' não estava presente.")
    elif acao == "sair":
        print("Programa encerrado! Total de alunos presentes:")
        print(len(lista_de_alunos))                         # exibe o número total de alunos presentes
        break                    # encerra o loop e o programa
    else:
        print("Ação inválida! Tente novamente.")