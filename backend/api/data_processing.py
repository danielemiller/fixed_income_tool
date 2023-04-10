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

    return {
        'face_value': 1000,  # Assuming a face value of 1000
        'coupon_rate': coupon_rate,
        'yield_to_maturity': yield_to_maturity,
        'years_to_maturity': years_to_maturity,
        'credit_rating': credit_rating,
        'currency': currency,
        'issuer': issuer
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
