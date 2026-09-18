# Incident: finish last week's stock-mismatch investigation

**Filed by:** you (last week)
**Status:** Open

## What we know

- You started digging into a stock-count mismatch last week and left three
  commits on `investigation/stock-mismatch` — nobody else has ever seen this
  branch.
- Looking back at it, at least one of those commits was a dead end, and
  there's leftover debug logging and a scratch notes file that were never
  meant to be permanent.
- The actual fix is in there somewhere.

## What to do

Turn those three commits into whatever `main` should actually receive: the
real fix, cleanly committed, with the noise gone. Nobody else has this
branch, so how you get there is entirely up to you.
`pytest tests/test_inventory.py` should pass when you're done.
