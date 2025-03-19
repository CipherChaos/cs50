import requests
from requests import RequestException

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    data = response.json()
    price = data["priceUsd"]
    for x in price:
        price = x.values()
        print(price
              )
except RequestException:
    print("Cannot open the following url")

