# Incident: CI is red on main

**Filed by:** Sam Ortiz, QA
**Status:** Open — main auto-deploys on every push, so whatever's on `main`
right now is already live in production.

## What we know

- `pytest tests/test_pricing.py` has been failing since Marcus pushed a fix
  for the missing `$` sign on receipts this week. The tests were green
  before that.
- Support is getting reports that discount totals look wrong — a customer
  says a *discount* somehow made their total go *up*.
- The receipts do correctly show `$` now, so whatever Marcus shipped isn't
  entirely bad.
- Nobody has manually reviewed what else was in that push besides the
  receipt formatting.

## What to do

Figure out exactly what changed, decide how to safely undo the damage given
that `main` is deployed continuously and other engineers pull from it every
day, and get `pytest tests/test_pricing.py` back to green.

Check `README.md`'s "Engineering Git Playbook" if you're unsure which tool
is safe to use on a branch in this state.
