# Desafio 1: Valor da variável SOMA
def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print(f"Desafio 1: O valor final de SOMA é {SOMA}")

# Desafio 2: Verificação na Sequência de Fibonacci
def fibonacci_check(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or n == 0:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Desafio 3: Análise de Faturamento Diário
import json

def analisar_faturamento(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    faturamento = [dia['valor'] for dia in data if dia['valor'] > 0]

    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

    print(f"Desafio 3: Menor valor: {menor_valor}")
    print(f"Maior valor: {maior_valor}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Desafio 4: Percentual de Faturamento por Estado
def calcular_percentual_faturamento(faturamento):
    total = sum(faturamento.values())
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

# Desafio 5: Inversão de String
def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

# Executando os desafios
if __name__ == "__main__":
    # Desafio 1
    calcular_soma()

    # Desafio 2
    numero = int(input("Desafio 2: Informe um número para verificar na sequência de Fibonacci: "))
    print(fibonacci_check(numero))

    # Desafio 3
    arquivo_json = "faturamento.json"  #Caminho do arquivo JSON
    analisar_faturamento(arquivo_json)

    # Desafio 4
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    print("Desafio 4: Percentual de faturamento por estado:")
    calcular_percentual_faturamento(faturamento_estados)

    # Desafio 5
    string_para_inverter = input("Desafio 5: Informe uma string para inverter: ")
    print(f"String invertida: {inverter_string(string_para_inverter)}")
