import QuantLib as ql
from datetime import datetime

def calculate_option_value(option_data):
    # Perform option value calculations using QuantLib
    # You will need to provide specific option features and market data

    # Example code (assuming European option with basic parameters):
    option_type = ql.Option.Call if option_data.get('option_type', 'call') == 'call' else ql.Option.Put
    strike_price = option_data['strike_price']
    underlying_price = option_data['underlying_price']
    risk_free_rate = option_data['risk_free_rate']
    volatility = option_data['volatility']
    expiration_date_str = option_data.get('expiration_date', '')
    expiration_date_dt = datetime.strptime(expiration_date_str, "%Y-%m-%d")
    expiration_date = ql.Date(expiration_date_dt.day, expiration_date_dt.month, expiration_date_dt.year)

    print("Option data:", option_data)
    print("Option type:", option_type)
    print("Strike price:", strike_price)
    print("Underlying price:", underlying_price)
    print("Risk-free rate:", risk_free_rate)
    print("Volatility:", volatility)
    print("Expiration date:", expiration_date)

    # Set up the option pricing environment
    calendar = ql.TARGET()
    calculation_date = ql.Date.todaysDate()
    ql.Settings.instance().evaluationDate = calculation_date

    # Ensure variables are of the correct type
    if not isinstance(strike_price, (float, int)):
        strike_price = float(strike_price)

    if not isinstance(underlying_price, (float, int)):
        underlying_price = float(underlying_price)

    if not isinstance(risk_free_rate, (float, int)):
        risk_free_rate = float(risk_free_rate)

    if not isinstance(volatility, (float, int)):
        volatility = float(volatility)

    day_count = ql.Actual365Fixed()
    interest_rate = ql.FlatForward(calculation_date, ql.QuoteHandle(ql.SimpleQuote(risk_free_rate)), day_count)
    dividend_yield = ql.FlatForward(calculation_date, 0, day_count)
    flat_vol = ql.BlackConstantVol(calculation_date, calendar, volatility, day_count)

    exercise = ql.EuropeanExercise(expiration_date)
    option = ql.VanillaOption(ql.PlainVanillaPayoff(option_type, strike_price), exercise)

    # Set up the Black-Scholes-Merton process
    process = ql.BlackScholesMertonProcess(ql.QuoteHandle(ql.SimpleQuote(underlying_price)),
                                           ql.YieldTermStructureHandle(dividend_yield),
                                           ql.YieldTermStructureHandle(interest_rate),
                                           ql.BlackVolTermStructureHandle(flat_vol))
    
    # Set the pricing engine
    engine = ql.AnalyticEuropeanEngine(process)
    option.setPricingEngine(engine)

    # Calculate the option value
    option_value = option.NPV()

    return option_value
