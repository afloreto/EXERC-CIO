# 25. Crie um programa que permita ao usuário cadastrar nomes de alunos em uma lista. Depois, exiba todos os alunos cadastrados. Pergunte ao usuário se deseja remover um aluno específico. Exiba a lista atualizada após a remoção.

lista_alunos = [] # lista para armazenar os nomes dos alunos

print("-------- Cadastro de Alunos -------- ")

while True:
    aluno = input("Digite o nome do aluno ou 'sair' para finalizar: ") # solicita ao usuário para cadastrar um aluno
    
    if aluno.lower() == 'sair':  # verifica se o usuário deseja sair do loop
        break
    
    lista_alunos.append(aluno) # adiciona o nome do aluno a lista
    
print("Alunos cadastrados: ") # exibe todos os alunos cadastrados
for aluno in lista_alunos:
    print(aluno)
    
remover = input("Deseja remover um aluno específico? (sim/não): ") # pergunta ao usuário se deseja remover um aluno

if remover.lower() == 'sim':
    aluno_remover = input("Digite o nome do aluno que você deseja remover: ") # solicita o nome do aluno a ser removido
    
    if aluno_remover in lista_alunos: # verifica se o aluno está na lista
        lista_alunos.remove(aluno_remover) # remove o aluno da lista
        print(f"{aluno_remover} foi removido da lista.") # exibe mensagem de confirmação
        
    else:
        print(f"{aluno_remover} não está na lista.") # exibe mensagem de erro se o aluno não estiver na lista