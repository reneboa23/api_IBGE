import requests
import json

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'

response = requests.get(url)

data = json.loads(response.text)

def execute():

    municipios = []

    #data = data[:2]
    for info in data:
        municipio = {}
        municipio['municipio'] = info['nome']
        municipio['uf'] = info['municipio']['microrregiao']['mesorregiao']['UF']['nome']
        municipio['sigla_uf'] = info['municipio']['microrregiao']['mesorregiao']['UF']['sigla']
        municipio['regiao'] = info['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['nome']
        municipios.append(municipio)

    return municipios

