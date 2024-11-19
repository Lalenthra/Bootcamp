import interest
import unittest
import datetime


class TestInterest(unittest.TestCase):
    def test_annual_fund(self):
        self.assertEqual(interest.simulate(
            opening_balance=1000,
            rate="10% annually",
            time=datetime.timedelta(days=360),
            # 360 days is 12 30-day months, sometimes used in financial calculations
        ), 1100)
    
    def test_annual_fund_monthly(self):
        balance = 1000
        
        for month in range(12):
            balance = interest.simulate(
                opening_balance=balance,
                rate="10% annually",
                time=datetime.timedelta(days=30),
            )
        
        self.assertEqual(int(balance), 1100)
    
    def test_monthly_fund(self):
        self.assertEqual(interest.simulate(
            opening_balance=1000,
            rate="1% monthly",
            time=datetime.timedelta(days=30),
        ), 1010)
    
    def test_monthly_fund_annually(self):
        self.assertEqual(interest.simulate(
            opening_balance=5500,
            rate="1% monthly",
            time=datetime.timedelta(days=360),
        ), 5500 * (1.01) ** 12)
    
    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            interest.simulate(
                opening_balance=1000,
                rate="1% blorgly",
                time=datetime.timedelta(days=360),
            )
    
    def test_invalid_rate2(self):
        with self.assertRaises(ValueError):
            interest.simulate(
                opening_balance=1000,
                rate="57 annually",
                time=datetime.timedelta(days=360),
            )
    
    def test_has_docstring(self):
        self.assertIsNotNone(interest.simulate.__doc__)