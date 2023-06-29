from binance.client import Client


def get_binance_asset(binance_api_key, binance_api_secret, asset):
    # Create a Binance client
    client = Client(binance_api_key, binance_api_secret)
    # Retrieve the account balance for a specific asset
    account_info = client.get_account()
    balances = account_info['balances']
    for balance in balances:
        if balance['asset'] == asset:
            my_assets = {f'{asset}_free': float(balance['free']), f'{asset}_locked': float(balance['locked'])}
            return my_assets
    return 'Nothing found'

