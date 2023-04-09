# backend/api/tests/factories.py
import factory
from factory.django import DjangoModelFactory
from api.models import BondData

class BondDataFactory(DjangoModelFactory):
    class Meta:
        model = BondData

    issue_date = factory.Faker('date_between', start_date='-10y', end_date='today')
    maturity_date = factory.Faker('date_between', start_date='today', end_date='+10y')
    coupon_rate = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    yield_to_maturity = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    credit_rating = factory.Faker('random_element', elements=['AAA', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-'])
    currency = factory.Faker('random_element', elements=['USD', 'EUR', 'JPY', 'GBP', 'CAD', 'CHF'])
    issuer = factory.Faker('company')
