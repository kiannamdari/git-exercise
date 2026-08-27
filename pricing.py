"""Pricing calculations for Acme Retail orders."""

TAX_RATE = 0.08


def calculate_tax(amount):
    """Return the sales tax owed on `amount`, rounded to the nearest cent."""
    return round(amount * TAX_RATE, 2)


def calculate_final_price(price, quantity, discount_pct=0):
    """Return the final price for `quantity` units of `price`, including
    an optional percentage discount and sales tax.
    """
    subtotal = price * quantity
    discount_amount = subtotal * (discount_pct / 100)
    discounted = subtotal - discount_amount
    tax = calculate_tax(discounted)
    return discounted + tax
