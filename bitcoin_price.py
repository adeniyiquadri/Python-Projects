import json
import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing Command Line Argument")
    else:
        try:
            n = float(sys.argv[1])
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=00b77256257d8e8e95352739a21134f80ef643d1fe1ac3250604afb57e4b1216")
            #Getting the price of 1 Bitcoin
            price = float(response.json()["data"]["priceUsd"])
            total_price = price * n
            print(f"${total_price:,.4f}")
        except ValueError:
            sys.exit("Command line Argument is not a number")
except requests.RequestException:
    sys.exit("Network Request failed")