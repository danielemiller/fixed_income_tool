from datetime import datetime
from .external_data import get_bond_price, get_risk_free_yield, get_benchmark_yield


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

    risk_free_yield = data.get('risk_free_yield', None)
    benchmark_yield = data.get('benchmark_yield', None)
    option_value = data.get('option_value', None)
    years_to_call = data.get('years_to_call', None)
    call_price = data.get('call_price', None)

    return {
        'face_value': 1000,
        'coupon_rate': coupon_rate,
        'yield_to_maturity': yield_to_maturity,
        'years_to_maturity': years_to_maturity,
        'credit_rating': credit_rating,
        'currency': currency,
        'issuer': issuer,
        'payment_schedule': payment_schedule,
        'risk_free_yield': risk_free_yield,
        'benchmark_yield': benchmark_yield,
        'option_value': option_value,
        'years_to_call': years_to_call,
        'call_price': call_price,
    }

def parse_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').date()

def format_output_data(output_data):
    formatted_output = {
        key: '{:,.2f}'.format(value) if isinstance(value, float) else value
        for key, value in output_data.items()
    }
    formatted_output['yield_to_maturity'] = '{:.2f}%'.format(output_data['yield_to_maturity'] * 100)
    
    if output_data['yield_to_call'] is not None:
        formatted_output['yield_to_call'] = '{:.2f}%'.format(output_data['yield_to_call'] * 100)

    return formatted_output

