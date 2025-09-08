import requests
import matplotlib.pyplot as plt

# Função para obter os dados de luminosidade a partir da API
def obter_dados_luminosidade(lastN):
    url = f"http://<ip>:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:001/attributes/luminosity?lastN={lastN}"

    headers = {
        'fiware-service': 'smart',
        'fiware-servicepath': '/'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        luminosity_data = data['contextResponses'][0]['contextElement']['attributes'][0]['values']
        return luminosity_data
    else:
        print(f"Erro ao obter dados: {response.status_code}")
        return []

# Função para criar e exibir o gráfico
def plotar_grafico(luminosity_data):
    if not luminosity_data:
        print("Nenhum dado disponível para plotar.")
        return

    luminosidade = [entry['attrValue'] for entry in luminosity_data]
    tempos = [entry['recvTime'] for entry in luminosity_data]

    # Calcular a média dos valores de luminosidade
    media_ = sum(luminosidade) / len(luminosidade)

    plt.figure(figsize=(12, 6))
    plt.plot(tempos, luminosidade, marker='o', linestyle='-', color='r')

    # Adicionar uma linha horizontal para a média
    plt.axhline(media_, color='b', linestyle='--', label=f'Média de Luminosidade: {media_:.2f}')

    plt.title('Gráfico de Luminosidade em Função do Tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Luminosidade')
    plt.xticks(rotation=45)
    plt.grid(True)

    # Adicionar uma legenda
    plt.legend()

    plt.tight_layout()
    plt.show()

# Solicitar ao usuário um valor "lastN" entre 1 e 100
while True:
    try:
        lastN = int(input("Digite um valor para lastN (entre 1 e 100): "))
        if 1 <= lastN <= 100:
            break
        else:
            print("O valor deve estar entre 1 e 100. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Obter os dados de luminosidade e plotar o gráfico
luminosity_data = obter_dados_luminosidade(lastN)
plotar_grafico(luminosity_data)
