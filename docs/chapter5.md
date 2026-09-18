# Incident: wrong total on a customer's order

**Filed by:** Sam Ortiz, QA
**Status:** Open

## What we know

- A customer says their total was wrong on a 3-pack of WIDGET-3PACK at
  $19.99 each with a 10% discount.
- Sam wrote a regression script, `scripts/check_total.py`, that reproduces
  it right now against `main` — run it and see for yourself.
- Nobody knows which change actually caused this or how long it's been
  broken. It's not tied to anything from this week's other incidents.
- `scripts/check_total.py` has existed for a while and always ran clean
  against older versions of this codebase, as far as anyone remembers.

## What to do

Find the exact change responsible, using `scripts/check_total.py` as your
signal for "is it broken here or not." Once you've found it, look closely
at what else that commit did before deciding how to undo the damage —
check the Playbook if the answer isn't just "undo the whole thing." When
you're done, the full suite (`pytest`) should be green.
