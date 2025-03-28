#13. Faça um programa que leia a nota de um aluno e indique se ele foi aprovado, reprovado ou está em recuperação. Exemplo: Nota maior ou igual a 7: Aprovado; Nota entre 5 e 6.9: Recuperação; Nota abaixo de 5: Reprovado.

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado!")
elif 5 <= nota < 7:
    print("Recuperação!")
else:
    print("Reprovado!")