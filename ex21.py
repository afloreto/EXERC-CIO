#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input('Informe um número inteiro: '))

if numero < 2:                   # verifica se o número é menor que 2
    print(f'O número {numero} não é primo.')                                # exibe mensagem de que o número n é primo
else:
    primo = True
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:                                 # verifica se o número é divisível por i
            primo = False
            break                       # se for divisível, n é primo
        
        if primo:
            print(f'O número {numero} é primo.')
        else:
            print(f'O número {numero} não é primo.')