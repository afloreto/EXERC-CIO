#22. Crie um programa que simule o acesso a um sistema onde o usuário tem três tentativas para informar a senha correta.

senha_correta = "123456"                # define a senha correta
tentativas = 3                       # define o número de tentativas

print('--------------  Bem-vindo ao sistema! Você tem 3 tentativas para informar a senha correta. -------------- ') 

while tentativas > 0:
    senha = input('Informe a senha: ')                  # solicita ao usuário para informar a senha
    if senha == senha_correta:                      # verifica se a senha está correta
        print('Acesso com sucesso!') 
        break                # sai do loop se a senha estiver correta
    else:
        tentativas -= 1                 # decrementa o numero de tentativas
        print(f'Senha incorreta! Você ainda tem {tentativas} tentativas.')         # exibe mensagem de erro e o número de tentativas restantes
else:
    print('Número de tentativas excedido! Acesso negado.')