from exchange_STXBTC_binance_48 import exchange_STXBTC_binance_48
from print_binance_assets import print_binance_assets
from print_kucoin_assets import print_kucoin_assets
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
# Import 'kucoin_api_key_one', 'kucoin_api_secret_one', and 'kucoin_api_passphrase_one' from recently
# created credits.py file with your own API credentials
from credits import kucoin_api_key_one
from credits import kucoin_api_secret_one
from credits import kucoin_api_passphrase_one
# Import 'kucoin_api_key_two', 'kucoin_api_secret_two', and 'kucoin_api_passphrase_two' from recently
# created credits.py file with your own API credentials
from credits import kucoin_api_key_two
from credits import kucoin_api_secret_two
from credits import kucoin_api_passphrase_two
# Import editable Kucoin accounts names from recently
# created credits.py file
from credits import kucoin_account_name_one
from credits import kucoin_account_name_two

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
binance_formatted_number = f"{binance_total_assets:.3f}"
print(f"Total Binance assets in BTC: {binance_formatted_number}")

# ------------ Kucoin section --------------
# Get kucoin exchange ratio
print('')
print('Kucoin:')
# Print kucoin assets and get kucoin_account_total_assets_one
print(f'{kucoin_account_name_one}')
kucoin_account_total_assets_one = print_kucoin_assets(kucoin_api_key_one, kucoin_api_secret_one, kucoin_api_passphrase_one, binance_STXBTC_ratio)
print('')
print(f'{kucoin_account_name_two}')
kucoin_account_total_assets_two = print_kucoin_assets(kucoin_api_key_two, kucoin_api_secret_two, kucoin_api_passphrase_two, binance_STXBTC_ratio)
kucoin_total_assets = kucoin_account_total_assets_one + kucoin_account_total_assets_two
print('')
kucoin_formatted_number = f"{kucoin_total_assets:.3f}"
print(f"Total Kucoin assets in BTC: {kucoin_formatted_number}")

# ------- Summarise all assets from all resources --------------
all_assets = binance_total_assets + kucoin_total_assets
print('')
all_assets_formatted_number = f"{all_assets:.3f}"
print(f"All assets in BTC: {all_assets_formatted_number}")


