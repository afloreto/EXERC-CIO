#23. Escreva um programa que pergunte o valor total da conta e permita ao usuário escolher a porcentagem de gorjeta que deseja adicionar (10%, 15%, ou 20%).

valor_total = float(input("Informe o valor total da conta: R$ "))           # solicita o valor total da conta
porcentagem = input("Escolha a porcentagem de gorjeta (10%, 15% ou 20%): ")             # solicita a porcentagem de gorjeta

while True:
    if porcentagem == "10%":
        gorjeta = valor_total * 0.10         # calcula a gorjeta de 10%
        print(f"Gorjeta de 10%: R$ {gorjeta}")       # exibe o valor da gorjeta
        break
    elif porcentagem == "15%":
        gorjeta = valor_total * 0.15             # calcula a gorjeta de 15%
        print(f"Gorjeta de 15%: R$ {gorjeta}")
        break
    elif porcentagem == "20%":
        gorjeta = valor_total * 0.20            # calcula a gorjeta de 20%
        print(f"Gorjeta de 20%: R$ {gorjeta}")
        break
    else:
        porcentagem = input("Porcentagem inválida! Escolha entre 10%, 15% ou 20%: ")            # solicita novamente a porcentagem

