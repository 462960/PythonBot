from assets_kucoin import get_kucoin_asset

# In order to have flexibility to extract any currency type from response
# we use the editable schema
schema = [
    {'currency': 'BTC', 'type': 'main'},
    {'currency': 'BTC', 'type': 'trade'},
    {'currency': 'STX', 'type': 'main'},
    {'currency': 'STX', 'type': 'trade'},
]

api_response = get_kucoin_asset()


def extract_kucoin_data():
    extracted_data = []
    for item in schema:
        currency = item['currency']
        currency_type = item['type']
        found = False

        for data_item in api_response['data']:
            if data_item['currency'] == currency and data_item['type'] == currency_type:
                type = data_item['type']
                free = data_item['available']
                locked = data_item['holds']
                extracted_data.append({f'{currency}': f'{type}', f'kucoin_{currency}_free': float(free),
                                       f'kucoin_{currency}_locked': float(locked)})
                found = True
                break

        if not found:
            continue

    return extracted_data
