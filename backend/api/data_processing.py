from datetime import datetime

def parse_input_data(data):
    issue_date = parse_date(data['issue_date'])
    maturity_date = parse_date(data['maturity_date'])
    coupon_rate = float(data['coupon_rate']) / 100
    yield_to_maturity = float(data['yield_to_maturity']) / 100
    credit_rating = data['credit_rating']
    currency = data['currency']
    issuer = data['issuer']

    years_to_maturity = (maturity_date - issue_date).days // 365

    payment_schedule = data['payment_schedule']

    # Add 'risk_free_yield', 'benchmark_yield', and 'option_value' to the parsed_data dictionary
    risk_free_yield = data.get('risk_free_yield', None)
    benchmark_yield = data.get('benchmark_yield', None)
    option_value = data.get('option_value', None)

    return {
        'face_value': 1000,  # Assuming a face value of 1000
        'coupon_rate': coupon_rate,
        'yield_to_maturity': yield_to_maturity,
        'years_to_maturity': years_to_maturity,
        'credit_rating': credit_rating,
        'currency': currency,
        'issuer': issuer,
        'payment_schedule': payment_schedule,
        'risk_free_yield': risk_free_yield,  # Include 'risk_free_yield' in the output dictionary
        'benchmark_yield': benchmark_yield,  # Include 'benchmark_yield' in the output dictionary
        'option_value': option_value,  # Include 'option_value' in the output dictionary
    }

def parse_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').date()

def format_output_data(output_data):
    bond_price = '{:,.2f}'.format(output_data['bond_price'])
    yield_to_maturity = '{:.2f}%'.format(output_data['yield_to_maturity'] * 100)

    return {
        'bond_price': bond_price,
        'yield_to_maturity': yield_to_maturity,
    }
