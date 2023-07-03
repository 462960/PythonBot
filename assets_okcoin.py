import requests
import time
import hmac
import hashlib
import base64
# Import 'okcoin_api_key', 'okcoin_api_secret', and 'okcoin_api_passphrase' from recently
# created credits.py file with your own API credentials
from credits import okcoin_api_key
from credits import okcoin_api_secret
from credits import okcoin_api_passphrase


def get_assets_okcoin():
    base_url = 'https://www.okcoin.com'
    endpoint = '/api/v5/account/balance'
    params = {'ccy': 'BTC,STX'}

    # Generate signature
    timestamp = str(int(time.time() * 1000))

    sign = timestamp + 'GET' + endpoint
    secret_key = base64.b64decode(okcoin_api_secret)
    signature = hmac.new(secret_key, sign.encode(), hashlib.sha256).hexdigest()
    print(f'OKcoin timestamp: {timestamp}')
    headers = {
        'OK-ACCESS-KEY': okcoin_api_key,
        'OK-ACCESS-SIGN': signature,
        'OK-ACCESS-TIMESTAMP': timestamp,
        'OK-ACCESS-PASSPHRASE': okcoin_api_passphrase,  # Replace with your passphrase
        'Content-Type': 'application/json'
    }

    # Make the API request
    response = requests.get(base_url + endpoint, params=params, headers=headers)
    data = response.json()
    return data
    # # Extract BTC and STX balances
    # btc_balance = 0.0
    # stx_balance = 0.0
    #
    # for balance in data:
    #     if balance['ccy'] == 'BTC':
    #         btc_balance = float(balance['bal'])
    #     elif balance['ccy'] == 'STX':
    #         stx_balance = float(balance['bal'])
    #
    # return btc_balance, stx_balance


bob = get_assets_okcoin()
print(bob)
