# 34. Implemente um programa para gerenciar uma agenda de compromissos: • O usuário deve poder adicionar compromissos e suas datas. • Exiba os compromissos cadastrados. • Ofereça a opção de buscar compromissos por data. • Exiba todos os compromissos ordenados pela data.

def agenda_compromissos():
    compromissos = {}                           # dicionário para armazenar os compromissos e suas datas
    
    print('-----------------------------------------------------------------')
    print('Sistema de Gerenciamento de Compromissos')
    print('-----------------------------------------------------------------')
    
    while True:
        acao = input("Digite 'adicionar' para adicionar um compromisso, 'buscar' para buscar um compromisso por data, 'listar' para listar todos os compromissos ou 'sair' para finalizar o programa: ")
        
        if acao == 'adicionar':
            compromisso = input('Digite o compromisso: ')
            data = input('Informe a data do compromisso (dd/mm/aaaa): ')            # solicita a data do compromisso
            compromissos[data] = compromisso                                     # adiciona o compromisso ao dicionário com a data como chave
            print(f"Compromisso '{compromisso}' adicionado na data {data}.")     # exibe mensagem de confirmação      
            
        elif acao == 'buscar':
            data = input('Informe a data que deseja buscar (dd/mm/aaaa): ')
            if data in compromissos:
                print(f"Compromisso na data {data}: {compromissos[data]}")
            else:
                print(f'Nenhum compromisso encontrado na data {data}.')
                
        elif acao == 'listar':
            print('Lista de compromissos: ')
            for data, compromisso in sorted(compromissos.items()):          # ordena os compromissos pela data
                print(f'{data}: {compromisso}')                     # exibe todos os compromissos ordenados pela data
                
        elif acao == 'sair':
            print('Programa encerrado!')
            break
        
        else:
            print('Ação inválida! Tente novamente.')                 # mensagem de erro para ação inválida
            
agenda_compromissos()                # chamada da função para iniciar o sistema de gerenciamento de compromissos