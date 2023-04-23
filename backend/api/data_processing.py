from datetime import datetime, timedelta
from collections import defaultdict
from .external_data import get_bond_price, get_risk_free_yield, get_benchmark_yield
from .calculation_engine import yield_to_maturity
from .option_value import calculate_option_value

def parse_input_data(data, call_premium_percentage=0.03):
    print('Parsing data input...')
    bond_data = data.get('bondData', {})
    optional_data = data.get('optionalData', {})
    option_value_calculation_data = bond_data.get('optionalData', {}).get('optionValueCalculation', {})


    issue_date = parse_date(bond_data.get('issue_date', ''))
    maturity_date = parse_date(bond_data.get('maturity_date', ''))
    coupon_rate = float(bond_data.get('coupon_rate', 0)) / 100
    face_value = bond_data.get("face_value", 1000)
    face_value = float(bond_data.get("face_value", 1000))
    credit_rating = bond_data.get('credit_rating', '')
    currency = bond_data.get('currency', '')
    issuer = bond_data.get('issuer', '')
    bond_cusip = bond_data.get('bond_cusip', '')
    years_to_maturity = (maturity_date - issue_date).days // 365
    payment_schedule = bond_data.get('payment_schedule', '')

    strike_price = option_value_calculation_data.get('strike_price', 0)
    underlying_price = option_value_calculation_data.get('underlying_price', 0)
    risk_free_rate = float(option_value_calculation_data.get('risk_free_rate', 0)) / 100
    volatility = option_value_calculation_data.get('volatility', 0)
    expiration_date = parse_date(option_value_calculation_data.get('expiration_date', ''))

    if not payment_schedule:
        payment_schedule = calculate_payment_schedule(issue_date, maturity_date, coupon_rate, face_value)

    use_api_data = data.get('useApiData', False)
    is_call_option_selected = data.get('isCallOptionSelected', False)

    if use_api_data:
        bond_price = get_bond_price(bond_cusip) if not optional_data.get('bondPrice') else float(optional_data['bondPrice'])
        risk_free_yield = float(get_risk_free_yield()) if not optional_data.get('riskFreeYield') else float(optional_data['riskFreeYield']) / 100
        benchmark_yield = get_benchmark_yield() if not optional_data.get('benchmarkYield') else float(optional_data['benchmarkYield']) / 100

        # Calculate yield_to_maturity using the calculation_engine
        ytm = yield_to_maturity(bond_price, 1000, coupon_rate, years_to_maturity)
    else:
        bond_price = float(optional_data.get('bondPrice', 0))
        ytm = float(optional_data.get('yieldToMaturity', 0)) / 100
        risk_free_yield = float(optional_data.get('riskFreeYield', 0)) / 100
        benchmark_yield = float(optional_data.get('benchmarkYield', 0)) / 100

    years_to_call = None

    if 'date_first_par_call' in bond_data:
        date_first_par_call = bond_data.get('date_first_par_call')
        if date_first_par_call:
            date_first_par_call = date_first_par_call.replace('-', '')
            years_to_call = calculate_years_to_call(date_first_par_call, issue_date.strftime('%Y%m%d'))
    
    call_price = float(bond_data.get('call_price', 0))

    if call_price == 0:
        face_value = 1000
        call_price = estimate_call_price(face_value, call_premium_percentage)

    if is_call_option_selected:
        option_value = calculate_option_value(option_value_calculation_data) if (not optional_data.get('optionValue') and is_call_option_selected) else float(optional_data.get('optionValue', 0))
    else:
        option_value = 0

    return {
        'face_value': face_value,
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
        'strike_price': strike_price,
        'underlying_price': underlying_price,
        'risk_free_rate': risk_free_rate,
        'volatility': volatility,
        'expiration_date': expiration_date
    }

def parse_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').date()

def format_output_data(output_data):
    print('formatting data...')
    formatted_output = {
        key: '{:,.2f}'.format(value) if isinstance(value, float) else value
        for key, value in output_data.items()
    }

    # Format percentages
    percentage_metrics = ['yield_to_maturity', 'yield_to_call', 'option_adjusted_spread', 'price_earnings_ratio']
    for metric in percentage_metrics:
        if metric in output_data:
            formatted_output[metric] = '{:.2f}%'.format(output_data[metric] * 100)

    # Format other metrics if needed
    if 'average_life' in output_data:
        formatted_output['average_life'] = '{:.2f} years'.format(output_data['average_life'])

    print('Data:')
    print(format_output_data)
    print('formatted output:')
    print(formatted_output)
    return formatted_output

def calculate_years_to_call(date_first_par_call, analysis_date):
    print('calculating years to call...')
    call_date = datetime.strptime(date_first_par_call, "%Y%m%d")
    current_date = datetime.strptime(analysis_date, "%Y%m%d")
    delta = call_date - current_date
    years_to_call = delta.days / 365
    return years_to_call

def estimate_call_price(face_value, premium_percentage):
    print('calculating estimated call price...')
    call_price = face_value * (1 + premium_percentage)
    return call_price

def calculate_payment_schedule(issue_date, maturity_date, coupon_rate, face_value):
    print('calculating payment schedule...')
    payment_schedule = []
    payment_amount = face_value * (coupon_rate / 100) / 2  # Assuming semi-annual payments

    payment_date = issue_date
    while payment_date <= maturity_date:
        payment_schedule.append({
            "payment_date": payment_date.strftime("%Y-%m-%d"),
            "payment": payment_amount,
        })

        payment_date += timedelta(days=6*30)  # Assuming semi-annual payments

    print('payment schedule: ')
    print(payment_schedule)
    return payment_schedule

