# 30. Crie um programa que simule um sorteio: • Adicione os nomes dos participantes em uma lista. • Utilize a função random.choice() para escolher um ganhador aleatório. • Exiba o nome do vencedor.

lista_de_participantes = []                             # lista para armazenar os nomes dos participantes
import random                                           # importa o módulo random para gerar números aleatórios

print('-------------------------------------------------')
print('Sistema de Sorteio')
print('-------------------------------------------------')

print("Digite 'adicionar' para adicionar um participante, 'sortear' para sortear um ganhador ou 'sair' para finalizar o programa.") 

while True:
    acao = input('Escolha uma ação: ').strip().lower()                  # solicita ao usuário a ação desejada
    if acao == 'adicionar':
        nome_participante = input('Digite o nome do participante: ').strip()
        lista_de_participantes.append(nome_participante)            # adiciona o nome do participante à lista
        print(f"Participante '{nome_participante}' adicionado ao sorteio.")
    elif acao == 'sortear':
        if lista_de_participantes:                  # verifica se há participantes na lista
            ganhador = random.choice(lista_de_participantes)                # escolhe um ganhador aleatório
            print(f"O ganhador do sorteio é: {ganhador}.")
        else:
            print('Nenhum participante cadastrado para o sorteio.')
    elif acao == 'sair':
        print('Programa encerrado!')
        break
    else:
        print('Ação inválida! Tente novamente.')