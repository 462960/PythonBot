from binance.client import Client
# Import 'binance_api_key' and 'binance_api_secret' from recently
# created credits.py file with your own API credentials
from credits import binance_api_key
from credits import binance_api_secret

# Create a Binance client
client = Client(binance_api_key, binance_api_secret)


def get_asset_balance(asset):
    # Retrieve the account balance for a specific asset
    account_info = client.get_account()
    balances = account_info['balances']
    for balance in balances:
        if balance['asset'] == asset:
            my_assets = {f'{asset}_free': float(balance['free']), f'{asset}_locked': float(balance['locked'])}
            return my_assets
    return 'Nothing found'

