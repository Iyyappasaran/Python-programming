# Implement a program that gets the input of  the count of bitcoin and convert it into dollars at real time
import requests
import sys
import json

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")
        else:
            coin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=851ee9e5871f17ed6f7d494e581abda715fb2800d77798a33f7722f47e37614d")
    n = response.json()
    price = float(n["data"]["priceUsd"])
    print(f"${(price*coin):,.2f}")

main()