"""QA regression oracle.

Exits 0 if a known order's total is correct, 1 otherwise. Meant to be run
with `git bisect run` to find the commit that broke it.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from orders import calculate_order_total, create_order

EXPECTED_TOTAL = 58.29

order = create_order("WIDGET-3PACK", 19.99, 3, discount_pct=10)
actual = round(calculate_order_total(order), 2)

if actual == EXPECTED_TOTAL:
    sys.exit(0)

print(f"expected {EXPECTED_TOTAL}, got {actual}")
sys.exit(1)
