import requests

def buscar_cotacao():
    cotacao = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json")
    if cotacao.status_code == 200:
        lista_cotacao = cotacao.json()
        return lista_cotacao[0]
    else:
        raise ValueError(f"Erro na API: {cotacao.status_code}")

def converter(reais, cotacao):
    if reais <=0:
        raise ValueError("O valor deve ser maior que 0")
    dolar = cotacao['valor']
    dolar = float(dolar)
    valor_convertido = reais / dolar
    return valor_convertido

if __name__ == '__main__':
    cotacao_atual = buscar_cotacao()
    valor = converter(100, cotacao_atual)
    print(round(valor, 2))
    print(cotacao_atual['data'], cotacao_atual['valor'])
    print(cotacao_atual)
    try:
        converter(0, cotacao_atual)
    except ValueError as e:
        print(e)



