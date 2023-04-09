# backend/models.py
from django.db import models

class BondData(models.Model):
    issue_date = models.DateField()
    maturity_date = models.DateField()
    coupon_rate = models.DecimalField(max_digits=5, decimal_places=2)
    yield_to_maturity = models.DecimalField(max_digits=5, decimal_places=2)
    credit_rating = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    issuer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.issuer} ({self.issue_date} - {self.maturity_date})'
