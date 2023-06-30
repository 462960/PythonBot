import time
import base64
import hmac
import requests
import hashlib

api_url = 'https://api.kucoin.com/api/v1/accounts'


def get_kucoin_asset(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase):
    now = int(time.time() * 1000)
    str_to_sign = str(now) + 'GET' + '/api/v1/accounts'
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
    return response.json()['data']

