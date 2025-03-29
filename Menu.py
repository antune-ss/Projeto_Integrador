# SISTEMA DE SUSTENTABILIDADE PESSOAL - PROJETO INTEGRADOR 1
# PROF: MARCELO TRAINA CHACON

# Diogo Gomes dos Santos Ferreira - 23011569
# Gustavo Antunes - 25013281
# Lucas Henrique Ferreira - 25005444
# Pedro Henrique de Oliveira - 25006386
# Yuri Kauan Moreira de Almeida - 25004132

print("SISTEMA DE SUSTENTABILIDADE PESSOAL")

from datetime import datetime

# Solicitar a data ao usuário no formato 'dd/mm/aaaa'
data_str = input("Digite a data atual (dd/mm/aaaa): ")

# Converter a string em um objeto datetime
try:
    data = datetime.strptime(data_str, "%d/%m/%Y")
    print(f"Data informada: {data.strftime('%d/%m/%Y')}")
except ValueError:
    print("Formato de data inválido. Por favor, digite a data no formato correto: dd/mm/aaaa")