"""Refund calculations for Acme Retail."""

from pricing import calculate_final_price


def calculate_refund(unit_price, quantity, discount_pct, days_since_purchase):
    """Return the refund owed for an order. No cap applied yet."""
    return calculate_final_price(unit_price, quantity, discount_pct)
