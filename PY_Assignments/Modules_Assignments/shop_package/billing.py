# billing.py - Billing calculation functions

def calculate_total(prices):
    """Returns total bill (sum of all prices)"""
    return sum(prices)

def apply_tax(amount):
    """Adds 5% tax"""
    return amount + (amount * 0.05)
