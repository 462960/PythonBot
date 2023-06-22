from assets import get_asset_balance
from exchange import get_exchange_rate
import sys

# The next line turns off Traceback of error message
# Commenting the line enables Traceback.
# Other than comment/uncomment options have not been explored
sys.tracebacklimit = 0

# Get exchange ratio
STXBTC_ratio = get_exchange_rate()
print(f"STX to BTC exchange ratio is: {STXBTC_ratio}")

# Get BTC balance
btc_balance = get_asset_balance('BTC')
BTC_free = btc_balance['BTC_free']
BTC_locked = btc_balance['BTC_locked']
# Get STX balance
stx_balance = get_asset_balance('STX')
STX_free = stx_balance['STX_free']
STX_locked = stx_balance['STX_locked']

# Calculate STX balance in BTC
converted_STX_free = STX_free * float(STXBTC_ratio)
converted_STX_locked = STX_locked * float(STXBTC_ratio)

# Calculate free assets
free_assets = BTC_free + converted_STX_free
# Calculate locked assets
locked_assets = BTC_locked + converted_STX_locked
# Calculate total assets in BTC
total_assets = free_assets  + locked_assets


print(f"Free assets in BTC: {free_assets}")
print(f"Locked assets in BTC: {locked_assets}")
print(f"Total assets in BTC: {total_assets}")

