# 7.faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.05
preco_final = preco - desconto
print(f"O preço do produto com 5% de desconto é: {preco_final}")