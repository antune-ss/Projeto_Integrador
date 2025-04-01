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