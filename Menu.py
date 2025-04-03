# SISTEMA DE SUSTENTABILIDADE PESSOAL - PROJETO INTEGRADOR 1
# PROF: MARCELO TRAINA CHACON

# Diogo Gomes dos Santos Ferreira - 23011569
# Gustavo Antunes - 25013281
# Lucas Henrique Ferreira - 25005444
# Pedro Henrique de Oliveira - 25006386
# Yuri Kauan Moreira de Almeida - 25004132

print("SISTEMA DE SUSTENTABILIDADE PESSOAL")

from datetime import datetime

while True:
    # Solicitar a data ao usuário no formato 'dd/mm/aaaa'
    data_str = input("Digite a data atual (dd/mm/aaaa): ")

    # Converter a string em um objeto datetime
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")

        #Ano
        if data.year < 2025:
            print("Erro: a data informada é inválida (ano invàlido).")
        #Mês
        elif data.month > 12 or data.month < 1:
            print("Erro: a data informada é inválida (mês inválido).")
        #Dia
        else:
            if data.month in [1, 3, 5, 7, 8, 10, 12]:
                MaxDias = 31
            elif data.month in [4, 6, 9, 11]:
                MaxDias = 30
            else: #Fevereiro
                if ((data.year%4==0 and data.year%100!=0) or data.year%400==0):
                    MaxDias = 29
                else:
                    MaxDias = 28
        
        if data.day < 1 or data.day > MaxDias:
            print("Erro: a data informada é inválida (dia inválido).")
        else:
            print(f"Data informada: {data.strftime('%d/%m/%Y')}")
            break

    except ValueError:
        print("Erro: formato de data inválido. Por favor, digite a data no formato correto: dd/mm/aaaa")

while True:
    try:
        qtd_agua = float(input("Quantos litros de água você consumiu hoje? (Aprox. em litros):"))

        if qtd_agua < 0:
            print("Erro: valor inválido. Por favor, insira um valor positivo.")
        else:
            break
    
    except ValueError:
        print("Erro: entrada inválida. Por favor, insira um valor númerico.")

if qtd_agua < 150:
    sustentabilidade = "Alta"
elif 150 <= qtd_agua <= 200:
    sustentabilidade = "Moderada"
elif qtd_agua > 200:
    sustentabilidade = "Baixa"

resultado = f"Consumo de água: {sustentabilidade} Sustentabilidade"
print(resultado)

while True:
    try:
        qtd_energia = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))

        if qtd_agua < 0:
            print("Erro: valor inválido. Por favor, insira um valor positivo.")
        else:
            break

    except ValueError:
        print("Erro: entrada inválida. Por favor, insira um valor númerico.")

if qtd_energia < 5:
    sustentabilidade = "Alta"
elif 5 <= qtd_energia <= 10:
    sustentabilidade = "Moderada"
elif qtd_energia > 10:
    sustentabilidade = "Baixa"

resultado = f"Consumo de energia: {sustentabilidade} Sustentabilidade"
print(resultado)

while True:
    try:
        qtd_residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))

        if qtd_residuos < 0:
            print("Erro: valor inválido. Por favor, insira um valor positivo.")
        else:
            break

    except ValueError:
        print("Erro: entrada inválida. Por favor, insira um valor númerico.")

while True:
    try:
        qtd_residuos_reciclaveis = float(input("Qual a porcentagem de resíduos reciclados no total (em %)?: "))

        if qtd_residuos_reciclaveis < 0:
            print("Erro: valor inválido. Por favor, insira um valor positivo.")
        else:
            break

    except ValueError:
        print("Erro: entrada inválida. Por favor, insira um valor númerico.")

if qtd_residuos_reciclaveis > 50:
    sustentabilidade = "Alta"
elif 20 <= qtd_residuos_reciclaveis <= 50:
    sustentabilidade = "Moderada"
elif qtd_residuos < 20:
    sustentabilidade = "Baixa"

resultado = f"Geração de Resíduos Não Recicláveis: {sustentabilidade} Sustentabilidade"
print(resultado)

print('Qual o meio de transporte você usou hoje?')        

# Validações de entrada
while True:
    transporte_publico = input('Transporte público (ônibus, metrô, trem) (s/n): ').lower()
    if transporte_publico in ['s', 'n']:
        break
    else:
        print('Entrada inválida, responda com "s" ou "n"')

while True:
    bicicleta = input('Bicicleta (s/n): ').lower()
    if bicicleta in ['s', 'n']:
        break
    else:
        print('Entrada inválida, responda com "s" ou "n"')

while True:
    caminhada = input('Caminhada (s/n): ').lower()
    if caminhada in ['s', 'n']:
        break
    else:
        print('Entrada inválida, responda com "s" ou "n"')

while True:
    carro = input('Carro (combustível fósseis): ').lower()
    if carro in ['s', 'n']:
        break
    else:
        print('Entrada inválida, responda com "s" ou "n"')

while True:
    eletrico = input('Carro elétrico: ').lower()
    if eletrico in ['s', 'n']:
        break
    else:
        print('Entrada inválida, responda com "s" ou "n"')

while True:
    carona = input('Carona compartilhada (Fósseis): ').lower()
    if carona in ['s', 'n']:
        break
    else:
        print('Entrada inválida, responda com "s" ou "n"')

grupo1 = 0
grupo2 = 0

# Verifica se algum transporte do grupo 1 foi escolhido (transporte público, bicicleta, caminhada ou carro elétrico)
if 's' in [transporte_publico, bicicleta, caminhada, eletrico]:
    grupo1 = 1

# Verifica se algum transporte do grupo 2 foi escolhido (carro ou carona compartilhada).
if 's' in [carro, carona]:
    grupo2 = 1

# Dependendo da combinação de escolhas, atribui a sustentabilidade como 'Alta', 'Baixa' ou 'Moderada'
if grupo1 == 1 and grupo2 == 1:
    saida = 'Moderada'
elif grupo1 == 1:
    saida = 'Alta'
elif grupo2 == 1:
    saida = 'Baixa'

print(saida, 'sustentabilidade')