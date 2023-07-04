from assets_binance import get_binance_asset
from assets_hold_binance import get_on_hold_deposits

def print_binance_assets(binance_api_key, binance_api_secret, binance_STXBTC_ratio):
    # Get STX deposit on_hold
    deposit_STX_on_hold = get_on_hold_deposits(binance_api_key, binance_api_secret)
    # Get binance BTC balance
    binance_btc_balance = get_binance_asset(binance_api_key, binance_api_secret, 'BTC')
    binance_BTC_free = binance_btc_balance['BTC_free']
    binance_BTC_locked = binance_btc_balance['BTC_locked']
    binance_BTC_total = binance_BTC_free + binance_BTC_locked

    # Get binance STX balance
    binance_stx_balance = get_binance_asset(binance_api_key, binance_api_secret, 'STX')
    binance_STX_free = binance_stx_balance['STX_free']
    binance_STX_locked = binance_stx_balance['STX_locked'] + deposit_STX_on_hold
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


    print(f"Free assets in BTC: {binance_BTC_free:.3f}")
    print(f"Locked assets in BTC: {binance_BTC_locked:.3f}")
    print(f"All assets in BTC: {binance_BTC_total:.3f}")

    print(f"Free assets in STX: {binance_STX_free:.3f}")
    print(f"Locked assets in STX: {binance_STX_locked:.3f}")
    print(f"All assets in STX: {binance_STX_total:.3f}")
    return binance_account_total_assets

