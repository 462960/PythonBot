from assets_binance import get_binance_asset
from exchange_binance import get_binance_exchange_rate
from exchange_kucoin import get_kucoin_exchange_rate
from assets_extract_kucoin import extract_kucoin_data
import sys

# The next line turns off Traceback of error message
# Commenting the line enables Traceback.
# Other than comment/uncomment options have not been explored
sys.tracebacklimit = 0

# ------------ Binance section --------------
# Get binance exchange ratio
binance_STXBTC_ratio = get_binance_exchange_rate()

# Get binance BTC balance
binance_btc_balance = get_binance_asset('BTC')
binance_BTC_free = binance_btc_balance['BTC_free']
binance_BTC_locked = binance_btc_balance['BTC_locked']
binance_BTC_total = binance_BTC_free + binance_BTC_locked

# Get binance STX balance
binance_stx_balance = get_binance_asset('STX')
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
binance_total_assets = binance_free_assets + binance_locked_assets

print('Binance:')
print(f"Binance STX to BTC exchange ratio: {binance_STXBTC_ratio}")
print(f"Free assets in BTC: {binance_BTC_free}")
print(f"Locked assets in BTC: {binance_BTC_locked}")
print(f"All assets in BTC: {binance_BTC_total}")

print(f"Free assets in STX: {binance_STX_free}")
print(f"Locked assets in STX: {binance_STX_locked}")
print(f"All assets in STX: {binance_STX_total}")
print('')
print(f"Total Binance assets in BTC: {binance_total_assets}")

# ------------ Kucoin section --------------
# Get kucoin exchange ratio
kucoin_STXBTC_ratio = get_kucoin_exchange_rate()
print('')
print('Kucoin:')
print(f"Kucoin STX to BTC exchange ratio: {kucoin_STXBTC_ratio}")
# Get kucoin assets
kucoin_assets = extract_kucoin_data()
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
kucoin_converted_STX_free = kucoin_STX_free * float(kucoin_STXBTC_ratio)
kucoin_converted_STX_locked = kucoin_STX_locked * float(kucoin_STXBTC_ratio)
# Calculate kucoin free assets
kucoin_free_assets = kucoin_BTC_free + kucoin_converted_STX_free
# Calculate kucoin locked assets
kucoin_locked_assets = kucoin_BTC_locked + kucoin_converted_STX_locked
# Calculate kucoin total assets in BTC
kucoin_total_assets = kucoin_free_assets + kucoin_locked_assets

print(f"Free assets in BTC: {kucoin_BTC_free}")
print(f"Locked assets in BTC: {kucoin_BTC_locked}")
print(f"All assets in BTC: {kucoin_BTC_total}")

print(f"Free assets in STX: {kucoin_STX_free}")
print(f"Locked assets in STX: {kucoin_STX_locked}")
print(f"All assets in STX: {kucoin_STX_total}")
print('')
print(f"Total Kucoin assets in BTC: {kucoin_total_assets}")

# ------- Summarise all assets from all resources --------------
all_assets = binance_total_assets + kucoin_total_assets
print('')
print(f"All assets in BTC: {all_assets}")


