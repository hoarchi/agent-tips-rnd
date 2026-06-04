# Protocol 05 - Analysis and Decision

## Goal

Turn measurements into bounded decisions.

## Steps

1. Compare every method to the declared baselines.
2. Break results down by task family.
3. Inspect false positives, false negatives, and abstention errors.
4. Check whether improvements are real or driven by label leakage, prompt
   leakage, cherry-picked cases, or metric mismatch.
5. Assign decision state:
   - accept_for_now
   - reject
   - inconclusive
   - revise
   - productize
6. Update the claim ledger.

## Output

An analysis report should say what changed in our beliefs, not just what the
numbers were.

