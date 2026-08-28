from orders import calculate_order_total, create_order, format_receipt


def test_calculate_order_total_no_discount():
    order = create_order("WIDGET-1", 25.00, 2)
    assert calculate_order_total(order) == 54.00


def test_format_receipt_includes_sku():
    order = create_order("WIDGET-1", 25.00, 2)
    assert "WIDGET-1" in format_receipt(order, 54.00)
