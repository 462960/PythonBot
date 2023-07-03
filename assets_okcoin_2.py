import requests
import base64
import hmac
import hashlib
import time
# Import 'okcoin_api_key', 'okcoin_api_secret', and 'okcoin_api_passphrase' from recently
# created credits.py file with your own API credentials
from credits import okcoin_api_key
from credits import okcoin_api_secret
from credits import okcoin_api_passphrase


def retrieve_user_assets():
    url = 'https://www.okcoin.com/api/v5/account/balance'
    method = 'GET'
    timestamp = str(int(time.time() * 1000))

    sign = hmac.new(okcoin_api_secret.encode(), (timestamp + method + '/api/v5/account/balance').encode(),
                    hashlib.sha256).digest()
    sign = base64.b64encode(sign).decode()

    headers = {
        'OK-ACCESS-KEY': okcoin_api_key,
        'OK-ACCESS-SIGN': sign,
        'OK-ACCESS-TIMESTAMP': timestamp,
        'OK-ACCESS-PASSPHRASE': okcoin_api_passphrase,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        print('Request failed with status:', response.status_code)
        return None

retrieve_user_assets()