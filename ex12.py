#12. Crie um sistema simples que verifica se o nome de usuário e a senha inseridos estão corretos (defina valores fixos para esses dados).

usuario = "admin"
senha = "1234"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido!")
else:
    print("Acesso negado!")