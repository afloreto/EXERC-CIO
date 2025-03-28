#9. Crie um programa que solicite dois números e uma operação (+, -, *, /). Utilize condicionais para realizar a operação e exibir o resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
else:
    print("Operação inválida!")