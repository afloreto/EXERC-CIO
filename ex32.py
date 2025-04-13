# 32. Peça ao usuário que insira as temperaturas registradas durante uma semana. • Exiba a maior e a menor temperatura. • Informe a média semanal. • Exiba os dias em que a temperatura foi maior que a média.

def temperaturas_semanais():                    # função para registrar e analisar temperaturas semanais
    temperaturas = []                           # lista para armazenar as temperaturas

    print('Informe as temperaturas registradas durante uma semana (7 dias).')

    for i in range(7):              # loop para solicitar as temperaturas dos 7 dias
        while True:
            try:
                temp = float(input(f'{i+1}º dia: '))                    # solicita a temperatura do dia
                temperaturas.append(temp)                               # adiciona a temperatura a lista
                break
            except ValueError:                                          # verifica se o valor informado é um número
                print('Temperatura inválida! Informe um número.')

    maior_temp = max(temperaturas)                          # encontra a maior temperatura
    menor_temp = min(temperaturas)                          # encontra a menor temperatura
    media_temp = sum(temperaturas) / len(temperaturas)      # calcula a média semanal

    print(f'Maior temperatura: {maior_temp}°C')             # exibe a maior temperatura
    print(f'Menor temperatura: {menor_temp}°C')             # exibe a menor temperatura
    print(f'Média semanal: {media_temp}°C')                 # exibe a média semanal

    dias_acima_media = [i + 1 for i, temp in enumerate(temperaturas) if temp > media_temp]              # encontra os dias com temperatura acima da média
    if dias_acima_media:                            ## verifica se há dias com temperatura acima da média
        print(f'Dias com temperatura acima da média: {", ".join(map(str, dias_acima_media))}')
    else:
        print('Nenhum dia teve temperatura acima da média.')
        
temperaturas_semanais()                     # chamada da função para executar o código