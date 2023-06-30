from assets_extract_kucoin import extract_kucoin_data

def print_kucoin_assets(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase, binance_STXBTC_ratio):
    # Get kucoin assets
    kucoin_assets = extract_kucoin_data(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase)
    # Extract and summarize 'kucoin_BTC_free'
    kucoin_BTC_free_values = [item.get('kucoin_BTC_free', 0) for item in kucoin_assets]
    kucoin_BTC_free = sum(kucoin_BTC_free_values)

    # Extract and summarize 'kucoin_BTC_locked'
    kucoin_BTC_locked_values = [item.get('kucoin_BTC_locked', 0) for item in kucoin_assets]
    kucoin_BTC_locked = sum(kucoin_BTC_locked_values)
    # Total BTC value
    kucoin_BTC_total = kucoin_BTC_free + kucoin_BTC_locked

    # Extract and summarize 'kucoin_STX_free'
    kucoin_STX_free_values = [item.get('kucoin_STX_free', 0) for item in kucoin_assets]
    kucoin_STX_free = sum(kucoin_STX_free_values)

    # Extract and summarize 'kucoin_STX_locked'
    kucoin_STX_locked_values = [item.get('kucoin_STX_locked', 0) for item in kucoin_assets]
    kucoin_STX_locked = sum(kucoin_STX_locked_values)
    # Total STX value
    kucoin_STX_total = kucoin_STX_free + kucoin_STX_locked
    # Calculate kucoin STX balance in BTC
    kucoin_converted_STX_free = kucoin_STX_free * float(binance_STXBTC_ratio)
    kucoin_converted_STX_locked = kucoin_STX_locked * float(binance_STXBTC_ratio)
    # Calculate kucoin free assets
    kucoin_free_assets = kucoin_BTC_free + kucoin_converted_STX_free
    # Calculate kucoin locked assets
    kucoin_locked_assets = kucoin_BTC_locked + kucoin_converted_STX_locked
    # Calculate kucoin total assets in BTC
    kucoin_account_total_assets = kucoin_free_assets + kucoin_locked_assets

    print(f"Free assets in BTC: {kucoin_BTC_free:.3f}")
    print(f"Locked assets in BTC: {kucoin_BTC_locked:.3f}")
    print(f"All assets in BTC: {kucoin_BTC_total:.3f}")

    print(f"Free assets in STX: {kucoin_STX_free:.3f}")
    print(f"Locked assets in STX: {kucoin_STX_locked:.3f}")
    print(f"All assets in STX: {kucoin_STX_total:.3f}")
    return kucoin_account_total_assets