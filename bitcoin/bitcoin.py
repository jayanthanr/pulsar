import requests
import sys
import json

def main():

    try:
        if len(sys.argv) < 2:
            sys.exit("Missing Command-line argument")
        elif len(sys.argv) == 2:
            flnum = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        obj = response.json()
        bitcoin_price = obj["bpi"]["USD"]["rate_float"]
        amount = bitcoin_price * flnum
        #print(amount)
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("Error")

main()




