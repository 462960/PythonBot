from assets_binance import get_binance_asset

def print_binance_assets(binance_api_key, binance_api_secret, binance_STXBTC_ratio):
    # Get binance BTC balance
    binance_btc_balance = get_binance_asset(binance_api_key, binance_api_secret, 'BTC')
    binance_BTC_free = binance_btc_balance['BTC_free']
    binance_BTC_locked = binance_btc_balance['BTC_locked']
    binance_BTC_total = binance_BTC_free + binance_BTC_locked

    # Get binance STX balance
    binance_stx_balance = get_binance_asset(binance_api_key, binance_api_secret, 'STX')
    binance_STX_free = binance_stx_balance['STX_free']
    binance_STX_locked = binance_stx_balance['STX_locked']
    binance_STX_total = binance_STX_free + binance_STX_locked

    # Calculate binance STX balance in BTC
    binance_converted_STX_free = binance_STX_free * float(binance_STXBTC_ratio)
    binance_converted_STX_locked = binance_STX_locked * float(binance_STXBTC_ratio)

    # Calculate binance free assets
    binance_free_assets = binance_BTC_free + binance_converted_STX_free
    # Calculate binance locked assets
    binance_locked_assets = binance_BTC_locked + binance_converted_STX_locked
    # Calculate binance total assets in BTC
    binance_account_total_assets = binance_free_assets + binance_locked_assets


    print(f"Free assets in BTC: {binance_BTC_free}")
    print(f"Locked assets in BTC: {binance_BTC_locked}")
    print(f"All assets in BTC: {binance_BTC_total}")

    print(f"Free assets in STX: {binance_STX_free}")
    print(f"Locked assets in STX: {binance_STX_locked}")
    print(f"All assets in STX: {binance_STX_total}")
    return binance_account_total_assets

