# ProDes

**Status:** STAGING_IMPLEMENTED / PUBLIC_STAGING_CANDIDATE / NOT_RELEASE_READY  
**Product family:** ORDO-WORK feature  
**Public Component identity:** NOT_ASSIGNED  
**License:** NO_LICENSE_GRANTED

## Purpose

ProDes supports controlled generation and post-execution review of reproducible prompt artifacts. It keeps target-specific rules outside the generic core and makes unresolved state, authority boundaries, and validation results visible.

Initial artifact families are INIT, CONFIG, HANDOVER, and RECOVERY. Additional families require an explicit contract and regression evidence.

## Operating loop

~~~text
Resolve → Apply → Generate → Validate → Repair → Emit
~~~

In this module, Apply materializes resolved requirements into a generation plan. It does not execute the generated prompt and does not grant authority in the target context.

## Module surfaces

- [Core contract](core/contract.md) — portable data model, invariants, and lifecycle.
- [ORDO-WORK target profile](profiles/ordo-work.md) — target-specific initialization and resolution constraints.
- [Generator pipeline](pipelines/generator.md) — deterministic production path.
- [Review pipeline](pipelines/review.md) — goal evaluation and generator-compliance review.
- [Validation rules](validation/rules.md) — public rule catalog.
- [Executable assurance](validation/prodes_lint.py) — dependency-free regression and disclosure checks.
- [Regression fixtures](fixtures/regressions.json) — eight known failure classes.
- [Examples](examples/) — public-safe prompt packages and a review report.

## Boundaries

ProDes must not:

- execute authority belonging to a target context;
- turn a generated artifact into an implicit change, approval, identity, or release;
- invent unresolved runtime, identity, authority, capability, freshness, or verification state;
- require private registries, carrier locators, conversation references, or confidential operational data;
- embed mutable target rules in the generic core;
- present a repository path, module name, or version as a Public Component identity;
- present public staging as runtime adoption or Public Release.

The target context resolves its current authority and executes any generated artifact. The terminal output must keep the copyable prompt artifact separate from analysis, provenance, and runtime-response metadata.

## State separation

| Dimension | State |
| --- | --- |
| Public module implementation | STAGING_IMPLEMENTED |
| ORDO-WORK product classification | DECIDED |
| ORDO-WORK runtime adoption | PENDING_TARGET_ADOPTION |
| Public Component identity | NOT_ASSIGNED |
| Release Candidate | NOT_DECLARED |
| Public Release | NOT_RELEASED |

The name `ProDes` is a product label at this stage. The directory is a locator. Neither allocates a public identifier.
