import sys
import requests

def main():
    # 1. Verificar argumento
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    # 2. Tentar obter preço do Bitcoin da API
    try:
        url = "https://api.coincap.io/v2/assets/bitcoin?apikey=20230ac08fe9016c06d42d8e45a686c9ac8220dd674f0b0599af9cac32233c9a"
        response = requests.get(url, timeout=5)  # timeout de 5 segundos
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        source = "API CoinCap"
    except (requests.RequestException, KeyError, ValueError):
        # Se não conseguir, usar valor fixo
        price = 34000.0
        source = "valor fixo (offline)"
    
    # 3. Calcular e imprimir custo
    cost = n * price
    print(f"${cost:,.4f}  (preço obtido através de {source})")

if __name__ == "__main__":
    main()
