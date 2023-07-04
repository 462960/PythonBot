import time
import base64
import hmac
import requests
import hashlib

api_url = 'https://api.kucoin.com/api/v1/accounts/holds'


def get_stx_deposits_on_hold(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + 'GET' + '/api/v1/accounts/holds'
    signature = base64.b64encode(
        hmac.new(kucoin_api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    passphrase = base64.b64encode(
        hmac.new(kucoin_api_secret.encode('utf-8'), kucoin_api_passphrase.encode('utf-8'), hashlib.sha256).digest())
    headers = {
        "KC-API-SIGN": signature,
        "KC-API-TIMESTAMP": str(now),
        "KC-API-KEY": kucoin_api_key,
        "KC-API-PASSPHRASE": passphrase,
        "KC-API-KEY-VERSION": "2"
    }
    response = requests.request('get', api_url, headers=headers)
    return response

# Replace with your own API key, secret, and passphrase
from credits import kucoin_api_key_one
from credits import kucoin_api_secret_one
from credits import kucoin_api_passphrase_one

# Call the function to retrieve STX deposits on hold
stx_deposits_on_hold = get_stx_deposits_on_hold(kucoin_api_key_one, kucoin_api_secret_one, kucoin_api_passphrase_one)

# Print the result
print(stx_deposits_on_hold)