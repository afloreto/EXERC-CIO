#10. Peça para o usuário informar sua idade e exiba a categoria correspondente: Menor de 12 anos: Criança; Entre 12 e 17 anos: Adolescente; Entre 18 e 59 anos: Adulto; 60 anos ou mais: Idoso.

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")
elif idade >= 12 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")