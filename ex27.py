# 27. Peça ao usuário para inserir as notas de um aluno em uma lista. Após cadastrar todas as notas, calcule e exiba: • A maior nota. • A menor nota. • A média das notas.

lista_notas = []        # lista para armazenar as notas
print("------------------- Sistema de Cadastro de Notas -------------------")

notas = int(input("Quantas notas você deseja cadastrar? "))             # solicita ao usuário o número de notas a serem cadastradas
for i in range(notas):               # loop para cadastrar as notas
    nota = float(input(f"Digite {i + 1}ª nota: "))              # solicita a nota ao usuário
    lista_notas.append(nota)                # adiciona a nota à lista

calculo_maior_nota = max(lista_notas)                   # calcula a maior nota
print(f"A maior nota é: {calculo_maior_nota}")              # exibe a maior nota
calculo_menor_nota = min(lista_notas)                            # calcula a menor nota
print(f"A menor nota é: {calculo_menor_nota}")                      # exibe a menor nota
calculo_media_nota = sum(lista_notas) / len(lista_notas)                 # calcula a média das notas
print(f"A média das notas é: {calculo_media_nota}")                          # exibe a média das notas com duas casas decimais

