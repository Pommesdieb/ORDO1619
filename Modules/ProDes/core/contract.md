# ProDes public core contract

**Status:** PUBLIC_STAGING / CANDIDATE_CONTRACT  
**Scope:** target-neutral prompt generation and review

## Contract objects

| Object | Purpose |
| --- | --- |
| IntentRecord | Requested outcome, artifact family, target, phase, and constraints. |
| ResolutionPlan | Facts and mutable questions that the target resolver must answer. |
| ResolvedContext | Resolver results with source, time, confidence, and explicit gaps. |
| GenerationPlan | Ordered content and validation obligations derived from the resolved context. |
| PromptArtifact | The standalone copyable prompt and its artifact family. |
| ValidationReport | Rule results, repairs, unresolved findings, and emission eligibility. |
| ReviewReport | Separate goal-achievement and generator-compliance evaluations using observed effects where available. |

## Core invariants

1. Resolve mutable target state at execution time.
2. Treat historical input as provenance, never as current authority.
3. Do not generate a stable identifier unless creation is explicitly requested, authorized, collision-checked, and recorded with positive provenance.
4. Keep workspace name, entity name, stable identifier, functional identity, interaction identity, and carrier binding as separate dimensions.
5. A resolve-first request and a fixed result for the same field are contradictory.
6. Capability preflight is phase-scoped; a later capability cannot block an earlier independent phase.
7. Target adapters may change target syntax and ordering, not factual or authority semantics.
8. Emit exactly one standalone artifact boundary. Analysis, provenance, validation, and runtime metadata remain outside it.

## Generation lifecycle

~~~text
INTENT_CAPTURED
→ RESOLUTION_PLANNED
→ CONTEXT_RESOLVED
→ PLAN_MATERIALIZED
→ ARTIFACT_GENERATED
→ VALIDATED
→ REPAIRED_IF_NEEDED
→ EMITTABLE
~~~

A package with an unresolved material contradiction is not emittable. A bounded noncritical gap may be emitted only when the gap is explicit and the artifact cannot misrepresent it as resolved.

## Review lifecycle

~~~text
ARTIFACT_EXECUTED
→ EFFECT_EVIDENCE_COLLECTED
→ GOAL_EVALUATED
→ GENERATOR_COMPLIANCE_EVALUATED
→ FINDINGS_CLASSIFIED
→ REGRESSION_OR_IMPROVEMENT_ROUTED
~~~

Repository persistence proves only that a candidate exists. It does not prove target execution, runtime adoption, or observed effectiveness.
