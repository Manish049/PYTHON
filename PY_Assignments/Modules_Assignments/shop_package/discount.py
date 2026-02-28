# discount.py - Discount calculation functions

def apply_discount(price, percent):
    """Returns discounted price"""
    return price - (price * percent / 100)

def flat_discount(price):
    """Always subtracts 50 from price"""
    return price - 50
