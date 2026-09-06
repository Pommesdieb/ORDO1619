# Generator pipeline

**Status:** PUBLIC_STAGING / CANDIDATE_PIPELINE

## Resolve

Collect the requested outcome, artifact family, target profile, current phase, supplied facts, mutable questions, and authority boundaries. Mark provenance separately from authority.

## Apply

Materialize a GenerationPlan from resolved inputs. Select the target profile and order required sections. This step changes the package plan only; it does not execute the target artifact.

## Generate

Produce one PromptArtifact. Use placeholders or resolver instructions for mutable state. Do not generate stable identifiers as convenience values.

## Validate

Apply the [validation rules](../validation/rules.md). Record all findings with rule identifiers. A failing package is not emittable.

## Repair

Perform only deterministic repairs that preserve intent and authority boundaries, such as removing a duplicate command or moving provenance outside the artifact. A repair that needs a new factual or authority decision becomes an unresolved finding.

## Emit

Return the prompt artifact as one standalone copyable block, followed or preceded by clearly separate optional analysis and validation metadata. Emission does not imply target execution.

## Minimum output package

~~~json
{
  "artifact_type": "CONFIG",
  "target_profile": "generic",
  "phase": "CONFIGURATION",
  "artifact": {"content": "..."},
  "analysis": {},
  "provenance": [],
  "runtime_metadata": {},
  "validation": {"result": "PASS", "rules": []}
}
~~~
