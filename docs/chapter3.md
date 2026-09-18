# Incident: Dana's refund-cap work needs to land

**Filed by:** Sam Ortiz, QA
**Status:** Open — Dana's back Monday and would like this merged before then.

## What we know

- Dana's been working on a refund cap (`feature/refund-cap`) for a couple of
  weeks. She only ever worked on it on her own laptop — she never pushed it
  anywhere else, and nobody else has this branch.
- It hasn't been touched since before Priya's and Marcus's discount work
  landed, so it's probably out of date with current `main`.
- Dana's commit history on this branch is rough — she was thinking out loud
  as she went (there's at least one debug print and what looks like an
  editor slip into an unrelated file).

## What to do

Get Dana's refund cap onto `main` in a clean state — no debug output, no
unrelated file changes riding along, and no merge commit muddying up what
was actually her work versus a routine update to current `main`. Check the
Playbook for guidance on picking an approach when a branch is genuinely
private like this one. `pytest tests/test_refunds.py` should pass when
you're done.
