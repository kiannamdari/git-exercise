"""Order creation and totals for Acme Retail."""

from pricing import calculate_final_price


def create_order(sku, unit_price, quantity, discount_pct=0):
    """Build an order dict for the given line item."""
    return {
        "sku": sku,
        "unit_price": unit_price,
        "quantity": quantity,
        "discount_pct": discount_pct,
    }


def calculate_order_total(order):
    """Return the final total (discount + tax applied) for an order."""
    return calculate_final_price(
        order["unit_price"], order["quantity"], order["discount_pct"]
    )


def format_receipt(order, total):
    """Return a one-line receipt string for an order."""
    return f"{order['sku']}: {total}"
