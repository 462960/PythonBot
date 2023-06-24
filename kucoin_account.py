import time
import base64
import hmac
import requests
import hashlib
# Import 'kucoin_api_key', 'kucoin_api_secret', and 'kucoin_api_passphrase' from recently
# created credits.py file with your own API credentials
from credits import kucoin_api_key
from credits import kucoin_api_secret
from credits import kucoin_api_passphrase

url = 'https://api.kucoin.com/api/v1/accounts'
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
response = requests.request('get', url, headers=headers)
print(response.status_code)
print(response.json())
