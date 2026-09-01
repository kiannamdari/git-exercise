from refunds import calculate_refund


def test_full_refund_matches_order_total():
    assert calculate_refund(25.00, 2, 0, days_since_purchase=3) == 54.00
