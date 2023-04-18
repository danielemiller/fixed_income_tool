from datetime import datetime
from .external_data import get_bond_price, get_risk_free_yield, get_benchmark_yield
from .calculation_engine import yield_to_maturity
from .option_value import calculate_option_value

def parse_input_data(data):
    bond_data = data.get('bondData', {})
    optional_data = data.get('optionalData', {})

    issue_date = parse_date(bond_data.get('issue_date', ''))
    maturity_date = parse_date(bond_data.get('maturity_date', ''))
    coupon_rate = float(bond_data.get('coupon_rate', 0)) / 100
    credit_rating = bond_data.get('credit_rating', '')
    currency = bond_data.get('currency', '')
    issuer = bond_data.get('issuer', '')
    bond_cusip = bond_data.get('bond_cusip', '')
    years_to_maturity = (maturity_date - issue_date).days // 365
    payment_schedule = bond_data.get('payment_schedule', '')

    use_api_data = bond_data.get('use_api_data', False)

    if use_api_data:
        bond_price = get_bond_price(bond_cusip) if not optional_data.get('bondPrice') else float(optional_data['bondPrice'])
        risk_free_yield = get_risk_free_yield() if not optional_data.get('riskFreeYield') else float(optional_data['riskFreeYield']) / 100
        benchmark_yield = get_benchmark_yield() if not optional_data.get('benchmarkYield') else float(optional_data['benchmarkYield']) / 100
        option_value = calculate_option_value(issuer, currency) if not optional_data.get('optionValue') else float(optional_data['optionValue'])

        # Calculate yield_to_maturity using the calculation_engine
        ytm = yield_to_maturity(bond_price, 1000, coupon_rate, years_to_maturity)
    else:
        bond_price = float(optional_data.get('bondPrice', 0))
        ytm = float(optional_data.get('yieldToMaturity', 0)) / 100
        risk_free_yield = float(optional_data.get('riskFreeYield', 0)) / 100
        benchmark_yield = float(optional_data.get('benchmarkYield', 0)) / 100
        option_value = float(optional_data.get('optionValue', 0))

    years_to_call = bond_data.get('years_to_call', None)
    call_price = bond_data.get('call_price', None)

    return {
        'face_value': 1000,
        'coupon_rate': coupon_rate,
        'yield_to_maturity': ytm,
        'years_to_maturity': years_to_maturity,
        'credit_rating': credit_rating,
        'currency': currency,
        'issuer': issuer,
        'payment_schedule': payment_schedule,
        'bond_price': bond_price,
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
