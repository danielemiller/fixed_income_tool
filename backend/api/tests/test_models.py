from django.test import TestCase
from api.models import BondData
from datetime import date

class BondDataTestCase(TestCase):
    def test_create_and_retrieve_bond_data(self):
        # Create a new instance of the BondData model and save it to the database
        bond_data = BondData(issue_date=date(2023, 4, 14), maturity_date=date(2028, 4, 14),
                             coupon_rate=2.5, yield_to_maturity=3.0, credit_rating='AAA',
                             currency='USD', issuer='ABC Corp')
        bond_data.save()

        # Retrieve the saved instance from the database
        saved_bond_data = BondData.objects.get(issuer='ABC Corp')

        # Check if the retrieved instance is equal to the created one
        self.assertEqual(saved_bond_data.issue_date, date(2023, 4, 14))
        self.assertEqual(saved_bond_data.maturity_date, date(2028, 4, 14))
        self.assertEqual(saved_bond_data.coupon_rate, 2.5)
        self.assertEqual(saved_bond_data.yield_to_maturity, 3.0)
        self.assertEqual(saved_bond_data.credit_rating, 'AAA')
        self.assertEqual(saved_bond_data.currency, 'USD')
        self.assertEqual(saved_bond_data.issuer, 'ABC Corp')
