# ORDO-WORK target profile

**Status:** PUBLIC_STAGING_PROFILE / ADOPTION_PENDING  
**Profile key:** `ordo-work`

This profile specializes the ProDes core for ORDO-WORK prompt artifacts. It defines generation constraints only; it does not activate a runtime, create an identity, or execute target authority.

## Persistent INIT ordering

When the target contract requires a persistent initialization package, the copyable artifact uses this resolved order:

~~~text
current workspace.name = "<resolved or user-supplied workspace name>"

Identity creation

ordo_init
~~~

The placeholder is input evidence, not permission to invent a stable identifier. Any current runtime, registry, version, authority, or capability detail is resolved by the target at execution time.

## Profile rules

- Include each bootstrap or refresh command at most once unless the current target contract explicitly requires repetition.
- Keep INIT, CONFIG, HANDOVER, and RECOVERY as distinct artifact families.
- Name identity dimensions explicitly; never collapse them into a generic `canonical_name` field.
- A resolver instruction must not be accompanied by a fixed answer for the same mutable field.
- Run only the capability preflight needed for the current phase.
- Keep the prompt artifact in a standalone copyable boundary.
- Treat execution output as evidence for review, not as a source of new target authority.

## Compatibility

If a target contract is unavailable or incomplete, emit an explicit bounded gap or stop at a genuine gate. Do not substitute remembered rules, guessed identifiers, or a private carrier reference.

## Adoption boundary

This public profile records a staging design. ORDO-WORK runtime adoption, manifest integration, capability catalog changes, and operational validation remain separate target-governed work.
