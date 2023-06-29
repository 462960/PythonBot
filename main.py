from assets_binance import get_binance_asset
from exchange_STXBTC_binance_48 import exchange_STXBTC_binance_48
from assets_extract_kucoin import extract_kucoin_data
from print_binance_assets import print_binance_assets
import sys
# Import 'binance_api_key_one' and 'binance_api_secret_one' from recently
# created credits.py file with your own API credentials
from credits import binance_api_key_one
from credits import binance_api_secret_one
# Import 'binance_api_key_two' and 'binance_api_secret_two' from recently
# created credits.py file with your own API credentials
from credits import binance_api_key_two
from credits import binance_api_secret_two
# Import editable Binance accounts names from recently
# created credits.py file
from credits import binance_account_name_one
from credits import binance_account_name_two

# The next line turns off Traceback of error message
# Commenting the line enables Traceback.
# Other than comment/uncomment options have not been explored
sys.tracebacklimit = 0

# ------------ Binance section --------------
# Get binance exchange ratio
binance_STXBTC_ratio = exchange_STXBTC_binance_48()
print('Binance:')
print(f"Binance STX to BTC exchange ratio: {binance_STXBTC_ratio}")
# Print binance assets and get binance_account_total_assets_one
print('')
print(f'{binance_account_name_one}')
binance_account_total_assets_one = print_binance_assets(binance_api_key_one, binance_api_secret_one, binance_STXBTC_ratio)
# Print binance assets and get binance_account_total_assets_two
print('')
print(f'{binance_account_name_two}')
binance_account_total_assets_two = print_binance_assets(binance_api_key_two, binance_api_secret_two, binance_STXBTC_ratio)
binance_total_assets = binance_account_total_assets_one + binance_account_total_assets_two
print('')
formatted_number = f"{binance_total_assets:.3f}"
print(f"Total Binance assets in BTC: {formatted_number}")

# ------------ Kucoin section --------------
# Get kucoin exchange ratio
print('')
print('Kucoin:')
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
kucoin_converted_STX_free = kucoin_STX_free * float(binance_STXBTC_ratio)
kucoin_converted_STX_locked = kucoin_STX_locked * float(binance_STXBTC_ratio)
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
# all_assets = binance_total_assets + kucoin_total_assets
# print('')
# print(f"All assets in BTC: {all_assets}")


