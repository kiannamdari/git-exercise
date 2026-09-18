# Incident: two approved features, one conflict

**Filed by:** Sam Ortiz, QA
**Status:** Open

## What we know

- Priya's bulk-discount work (`feature/bulk-discount`) and Marcus's
  loyalty-discount work (`feature/loyalty-discount`) both got sign-off from
  review. Priya's was approved first.
- Sam also noticed a typo in `README.md` ("Its maintained by..." should be
  "It's") — worth a quick one-line fix on your own before tackling the
  bigger branches.
- Both discount features touch the same pricing function, so don't be
  surprised if getting both of them onto `main` isn't completely smooth.
- Product's requirement, in case the two features interact: **bulk discount
  applies first, then any manual discount code, then the loyalty discount,
  then tax is calculated last.**

## What to do

Fix the README typo, then get both discount branches onto `main`, in the
order they were approved. Think about whether each of these three changes
deserves its own visible bump in `git log` or not — they're not all the same
kind of change. Resolve whatever comes up according to product's ordering
rule above, and get `pytest tests/test_pricing.py` green.
