import requests
from datetime import datetime, timedelta

def exchange_STXBTC_binance_48():
    # Calculate the start and end timestamps for the last 48 hours
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=48)

    # Convert timestamps to milliseconds
    start_timestamp = int(start_time.timestamp() * 1000)
    end_timestamp = int(end_time.timestamp() * 1000)

    # Make the API call to retrieve the klines data
    url = f"https://api.binance.com/api/v3/klines?symbol=STXBTC&interval=1m&startTime={start_timestamp}&endTime={end_timestamp}"
    response = requests.get(url)

    if response.status_code == 200:
        klines = response.json()

        # Calculate the average exchange rate
        total_rate = sum(float(kline[4]) for kline in klines)  # Use the closing price at index 4
        average_rate = total_rate / len(klines)
        return format(average_rate, '.8f')

    else:
        print("Failed to retrieve data from the Binance API.")
        return None
