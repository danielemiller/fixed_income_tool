import math
from scipy.optimize import brentq, root_scalar

def bond_price(face_value, coupon_rate, yield_to_maturity, years_to_maturity):
    coupon_payment = face_value * coupon_rate

    present_value_coupon_payments = sum([coupon_payment * math.exp(-yield_to_maturity * t) for t in range(1, years_to_maturity + 1)])
    present_value_face_value = face_value * math.exp(-yield_to_maturity * years_to_maturity)

    return present_value_coupon_payments + present_value_face_value


def yield_to_maturity(bond_price_value, face_value, coupon_rate, years_to_maturity):
    def f(y):
        return bond_price_value - bond_price(face_value, coupon_rate, y, years_to_maturity)

    return brentq(f, 0.0, 1.0) # Provide a reasonable range of yield values


def yield_to_call(bond_price_value, face_value, coupon_rate, years_to_call, call_price):
    def f(ytc):
        c = face_value * coupon_rate
        t = years_to_call
        p = bond_price_value
        cp = call_price

        right_side = (c / 2) * ((1 - (1 + ytc / 2) ** (-2 * t)) / (ytc / 2)) + (cp / (1 + ytc / 2) ** (2 * t))
        return p - right_side

    # Change the lower bound of the bracket from 0 to a small positive number (e.g., 1e-8)
    result = root_scalar(f, bracket=[1e-8, 1], method='brentq')
    return result.root


def average_life(payment_schedule):
    weighted_payments = [t * pmt for t, pmt in enumerate(payment_schedule, 1)]
    return sum(weighted_payments) / sum(payment_schedule)


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
    yield_to_call_result = yield_to_call(bond_price_result, face_value, coupon_rate, parsed_data['years_to_call'], parsed_data['call_price'])
    average_life_result = average_life(parsed_data['payment_schedule'])
    duration_result = duration(face_value, coupon_rate, ytm, years_to_maturity)
    convexity_result = convexity(face_value, coupon_rate, ytm, years_to_maturity)
    credit_spread_result = credit_spread(yield_to_maturity_result, parsed_data['risk_free_yield'])
    option_adjusted_spread_result = option_adjusted_spread(yield_to_maturity_result, parsed_data['benchmark_yield'], parsed_data['option_value'])

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
