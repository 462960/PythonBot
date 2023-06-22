import requests

api_url = 'https://api.binance.com/api/v3/ticker/price'
symbol = 'STXBTC'


def get_exchange_rate():
    response = requests.get(api_url, params={'symbol': symbol})

    if response.status_code == 200:
        data = response.json()
        latest_ratio = data['price']
        return latest_ratio
    else:
        print("Failed to retrieve data from Binance API")

