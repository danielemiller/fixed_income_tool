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

class ValuationMetrics(models.Model):
    bond = models.ForeignKey(BondData, on_delete=models.CASCADE)
    bond_price = models.DecimalField(max_digits=10, decimal_places=2)
    yield_to_maturity = models.DecimalField(max_digits=5, decimal_places=2)
    modified_duration = models.DecimalField(max_digits=10, decimal_places=2)
    macaulay_duration = models.DecimalField(max_digits=10, decimal_places=2)
    convexity = models.DecimalField(max_digits=10, decimal_places=2)
    credit_spread = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Valuation Metrics for {self.bond.name}"

class RiskAnalysisMetrics(models.Model):
    bond = models.ForeignKey(BondData, on_delete=models.CASCADE)
    yield_to_call = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    average_life = models.DecimalField(max_digits=10, decimal_places=2)
    option_adjusted_spread = models.DecimalField(max_digits=5, decimal_places=2)
    risk_free_yield = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Risk Analysis Metrics for {self.bond.name}"

class HistoricalData(models.Model):
    bond = models.ForeignKey(BondData, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    yield_to_maturity = models.DecimalField(max_digits=5, decimal_places=2)
    credit_spread = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Historical Data for {self.bond.name} on {self.date}"
