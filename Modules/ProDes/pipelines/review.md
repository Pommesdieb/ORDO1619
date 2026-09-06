# Review pipeline

**Status:** PUBLIC_STAGING / CANDIDATE_PIPELINE

ProDes reviews both generated prompts and the responses or effects they produced. It keeps two questions separate:

1. Did the execution achieve the user's intended outcome?
2. Did the generator comply with its construction contract?

## Evidence order

Prefer observed target effects, target-native read-back, and executed output over predicted behavior. Static prompt inspection remains valid evidence for generator compliance but cannot prove live target effect.

## Review steps

~~~text
collect artifact + execution evidence
→ classify evidence quality
→ evaluate goal achievement
→ evaluate generator compliance
→ identify causal findings
→ route each finding
~~~

## Finding routes

| Finding | Route |
| --- | --- |
| Deterministic generator defect | Add or update a regression fixture, then repair the generator rule. |
| Target-profile mismatch | Update the target profile without changing the generic core. |
| Missing mutable target state | Add a resolver requirement or explicit gap; do not hard-code a result. |
| Target execution defect | Route to the target owner; do not claim a generator fix solved it. |
| Material semantic decision | Stop at the appropriate human or authority gate. |

A review report must include `goal_evaluation`, `generator_compliance`, `observed_effects`, `findings`, and `next_routes`. A sample is provided in [the examples directory](../examples/review-report.json).
