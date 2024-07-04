import sys
import requests


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    usd_price = data["bpi"]["USD"]["rate_float"]

    if len(sys.argv) == 2:
        value = float(sys.argv[1])
        amount = value * usd_price
        print(f"${amount:,.4f}")

    else:
        sys.exit("Missing command-line argument")
except (IndexError, ValueError, requests.RequestException):
    sys.exit("Missing command-line argument")
