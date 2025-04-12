import requests
from requests import RequestException
import sys

def get_price_value():
    #send a "get" request to API
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    return price


def main():
    try:
        price = get_price_value()

        if len(sys.argv) == 2:
            #calculate the number of bitcoin in cash
            bitcoin_count = float(sys.argv[1])
            if type(bitcoin_count) is float:
                price *= bitcoin_count
                print(f"${price:,.4f}", end="")
            else:
                print("Command-line argument is not a number")
                sys.exit(1)
        else:
            print("Missing command-line argument: ")
            sys.exit(1)

    except RequestException:
        print("Cannot open the following url")
        sys.exit(1)

if __name__ == "__main__":
    main()


