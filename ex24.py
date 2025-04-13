#24. Escreva um programa que simula a chamada de senhas em um sistema de atendimento. O usuário pode escolher "chamar próximo" ou "encerrar atendimento".

def sistema_senhas():
    contador = 1  # inicia o contador de senhas

    print("--------------------------------------------------")
    print("Sistema de Atendimento")
    print("--------------------------------------------------")
    
    while True:
        acao = input("Digite 'chamar' para chamar o próximo ou 'encerrar' para encerrar o atendimento: ")

        if acao == "chamar":
            print(f"Senha {contador} chamada!")
            contador += 1
        elif acao == "encerrar":
            print("Atendimento encerrado.")
            break
        else:
            print("Ação inválida! Tente novamente.")
            
sistema_senhas()    #chama a função para iniciar o sistema de senhas
