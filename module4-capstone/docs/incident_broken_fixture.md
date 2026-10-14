# Incident Note: Broken Gold Fixture Diagnosis

## Symptom
A gold fixture expected `routine` for the phrase `mild headache`, but an early rule set had no headache pattern and returned `self_care`.

## Diagnosis
The test displayed the fixture ID. Comparing the input with `RULES` showed the missing pattern.

## Fix
Added the `headache` routine pattern and retained the gold test as regression coverage. No fixture expectation was silently changed to make the test pass.
