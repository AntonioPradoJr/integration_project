import requests

#Define EndPoint
url = "https://api.coingecko.com/api/v3/simple/price"
#Define Params
params = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "brl"
}

# GET response
response = requests.get(url, params=params)
print(response.json())