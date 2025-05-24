def get_price(crypto_name:str, currency:str) -> dict:
    import requests

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": crypto_name,
        "vs_currencies": currency,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("Erro ao acessar a API:", error)
        return{}
    

preco = get_price("bitcoin,solana", "brl,usd")

print(preco)