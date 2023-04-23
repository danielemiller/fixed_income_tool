import math
from scipy.optimize import brentq, root_scalar

def bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity):
    coupon_payment = face_value * coupon_rate

    present_value_coupon_payments = sum([coupon_payment * math.exp(-yield_to_maturity * t) for t in range(1, years_to_maturity + 1)])
    present_value_face_value = face_value * math.exp(-yield_to_maturity * years_to_maturity)

    return present_value_coupon_payments + present_value_face_value


def yield_to_maturity(bond_price_value, face_value, coupon_rate, years_to_maturity):
    def f(y):
        # Ensure bond_price_value is a float
        bond_price_value_float = float(bond_price_value)
        return bond_price_value_float - bond_price(face_value, coupon_rate, y, years_to_maturity)

    return brentq(f, 0.0, 1.0)  # Provide a reasonable range of yield values


def yield_to_call(bond_price, face_value, coupon_rate, years_to_call, call_price):
    def f(y):
        present_value_sum = sum([(face_value * coupon_rate) / ((1 + y) ** i) for i in range(1, int(years_to_call * 2) + 1)])
        present_value_call = call_price / ((1 + y) ** (years_to_call * 2))
        return present_value_sum + present_value_call - bond_price

    methods = ['brentq', 'bisect', 'ridder', 'newton']
    brackets = [[1e-8, 2], [1e-8, 3], [1e-8, 4], [1e-8, 5], [0.001, 0.999]]

    for method in methods:
        for bracket in brackets:
            try:
                result = root_scalar(f, bracket=bracket, method=method)
                if result.converged:
                    return result.root
            except (ValueError, RuntimeError):
                continue

    raise ValueError("Failed to find root with provided methods and brackets. Please check if the input data is correct.")


def average_life(payment_schedule):
    weighted_payments = [t * pmt['payment'] for t, pmt in enumerate(payment_schedule, 1)]
    return sum(weighted_payments) / sum(pmt['payment'] for pmt in payment_schedule)


def yield_curve(spot_rates, time_to_maturities):
    return [(t, r) for t, r in zip(time_to_maturities, spot_rates)]


def duration(face_value, coupon_rate, yield_to_maturity, years_to_maturity):
    coupon_payment = face_value * coupon_rate
    discount_rate = 1 + yield_to_maturity

    weighted_payments = [t * coupon_payment / (discount_rate ** t) for t in range(1, years_to_maturity + 1)]
    weighted_final_payment = years_to_maturity * face_value / (discount_rate ** years_to_maturity)

    return (sum(weighted_payments) + weighted_final_payment) / bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity)


def convexity(face_value, coupon_rate, yield_to_maturity, years_to_maturity):
    coupon_payment = face_value * coupon_rate
    discount_rate = 1 + yield_to_maturity

    weighted_squared_payments = [(t * (t + 1) * coupon_payment) / (discount_rate ** t) for t in range(1, years_to_maturity + 1)]
    weighted_squared_final_payment = years_to_maturity * (years_to_maturity + 1) * face_value / (discount_rate ** years_to_maturity)

    return (sum(weighted_squared_payments) + weighted_squared_final_payment) / (bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity) * (1 + yield_to_maturity) ** 2)


def credit_spread(bond_yield, risk_free_yield):
    return bond_yield - risk_free_yield


def option_adjusted_spread(bond_yield, benchmark_yield, option_value):
    return (bond_yield - benchmark_yield) - option_value

def calculate_bond_metrics(parsed_data):
    face_value = parsed_data['face_value']
    coupon_rate = parsed_data['coupon_rate']
    ytm = parsed_data['yield_to_maturity']
    years_to_maturity = parsed_data['years_to_maturity']
    
    bond_price_result = bond_price(face_value, coupon_rate, ytm, years_to_maturity)
    yield_to_maturity_result = yield_to_maturity(bond_price_result, face_value, coupon_rate, years_to_maturity)
    
    if 'years_to_call' in parsed_data and 'call_price' in parsed_data:
        yield_to_call_result = yield_to_call(bond_price_result, face_value, coupon_rate, parsed_data['years_to_call'], parsed_data['call_price'])
    else:
        yield_to_call_result = None
    
    average_life_result = average_life(parsed_data['payment_schedule'])
    duration_result = duration(face_value, coupon_rate, ytm, years_to_maturity)
    convexity_result = convexity(face_value, coupon_rate, ytm, years_to_maturity)

    # Calculate credit spread only if risk_free_yield is provided
    if parsed_data['risk_free_yield']:
        credit_spread_result = credit_spread(yield_to_maturity_result, parsed_data['risk_free_yield'])
    else:
        credit_spread_result = None

    # Calculate option adjusted spread only if benchmark_yield and option_value are provided
    if parsed_data['benchmark_yield'] and parsed_data['option_value']:
        option_adjusted_spread_result = option_adjusted_spread(yield_to_maturity_result, parsed_data['benchmark_yield'], parsed_data['option_value'])
    else:
        option_adjusted_spread_result = None

    return {
        'bond_price': bond_price_result,
        'yield_to_maturity': yield_to_maturity_result,
        'yield_to_call': yield_to_call_result,
        'average_life': average_life_result,
        'duration': duration_result,
        'convexity': convexity_result,
        'credit_spread': credit_spread_result,
        'option_adjusted_spread': option_adjusted_spread_result
    }
