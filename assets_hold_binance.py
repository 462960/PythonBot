import time
import hmac
import hashlib
from urllib.parse import urlencode

from credits import binance_api_key_one
from credits import binance_api_secret_one

import requests

def get_on_hold_deposits():
    base_url = "https://api.binance.com"
    endpoint = "/sapi/v1/capital/deposit/hisrec"
    params = {
        "timestamp": int(time.time() * 1000),
        "status": 0,  # 0 represents "on hold" status
        "recvWindow": 5000,  # optional, adjust as needed
    }
    headers = {
        "X-MBX-APIKEY": binance_api_key_one,
    }

    # Generate the query string and sign it
    query_string = urlencode(params)
    signature = hmac.new(binance_api_secret_one.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
    url = f"{base_url}{endpoint}?{query_string}&signature={signature}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        res = response.json()
        amount = float(extract_amount(res))
        return amount
    except requests.exceptions.RequestException as e:
        print("Error occurred:", str(e))

def extract_amount(arr):
    if arr:
        if isinstance(arr[0], dict) and 'amount' in arr[0]:
            return arr[0]['amount']
    return 0

# Call the function to get the on-hold deposits
on_hold_deposits = get_on_hold_deposits()
print(on_hold_deposits)
