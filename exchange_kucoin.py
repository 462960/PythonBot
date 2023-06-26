from webbrowser import get
import requests

api_url = 'https://api.kucoin.com'
symbol = 'STX-BTC'


def get_kucoin_exchange_rate():
    response = requests.get(api_url + f'/api/v1/market/orderbook/level1?symbol={symbol}', data={'data': 'price'}).json()
    exchange_price = response['data']['price']
    return exchange_price
