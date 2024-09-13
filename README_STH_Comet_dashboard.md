
# Luminosity Data Viewer

Este projeto é um aplicativo web simples desenvolvido em [Dash](https://dash.plotly.com/) que exibe os dados de luminosidade de uma API externa. Os dados são atualizados em intervalos regulares e exibidos em um gráfico interativo, com uma linha média que acompanha a luminosidade ao longo do tempo.

## Funcionalidades

- Exibição dos dados de luminosidade de uma API externa.
- Atualização automática dos dados a cada 10 segundos.
- Conversão de timestamps de UTC para o fuso horário de Lisboa.
- Cálculo e exibição de uma linha média da luminosidade para fácil visualização.
- Gráfico interativo com zoom, pan e visualização de detalhes por meio de hover.

## Pré-requisitos

- Python 3.x
- Bibliotecas necessárias (listadas em `requirements.txt`):
  - `dash`
  - `plotly`
  - `requests`
  - `pytz`

## Instalação

1. Clone o repositório:

```bash
git clone <URL_do_repositorio>
cd <nome_do_repositorio>
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

No código, você encontrará as seguintes variáveis que podem ser configuradas de acordo com suas necessidades:

- `IP_ADDRESS`: Endereço IP do servidor onde os dados estão hospedados.
- `PORT_STH`: Porta de conexão para a API de dados.
- `DASH_HOST`: O endereço do servidor Dash. Padrão para `"0.0.0.0"` para permitir acesso externo.
- `lastN`: Define quantos dados recentes devem ser buscados da API em cada intervalo de tempo.

## Execução

Para iniciar o aplicativo, execute o seguinte comando:

```bash
python app.py
```

O servidor estará acessível em `http://localhost:8050` (ou no endereço configurado, se você usar outro host).

## Estrutura do Código

- O aplicativo utiliza [Dash](https://dash.plotly.com/) para criar uma interface web interativa que exibe um gráfico Plotly dos dados de luminosidade.
- Os dados são coletados da API fornecida em intervalos de 10 segundos e armazenados localmente usando `dcc.Store`.
- Os timestamps são convertidos de UTC para o fuso horário de Lisboa, garantindo que as datas exibidas no gráfico sejam precisas.
- Um gráfico de linhas exibe os dados de luminosidade ao longo do tempo, com uma linha pontilhada representando a luminosidade média.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests para melhorias ou correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
