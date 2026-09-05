# Modules

**Status:** PUBLIC_STAGING / NON-RELEASE

This directory is the smallest current staging surface for independently understandable ORDO capability modules.

A module belongs here only when its public purpose, boundaries, inputs, outputs, and evaluation path can be explained without reproducing private control-plane data or internal operational provenance.

## Boundary

Material in this directory:

- is constructed from public-safe semantics;
- does not become normative merely because it is public;
- does not inherit authority from a development workspace or repository path;
- does not establish ORDO-WORK product ownership;
- does not imply Release Candidate or Public Release status;
- remains subject to disclosure, security, licensing, assurance, and human release gates.

Directory names and links are locators, not Public Component identities.

## Inclusion check

Before a candidate can progress beyond evaluation, it needs:

1. a clear external purpose and audience;
2. explicit scope and exclusions;
3. independently understandable public-safe examples;
4. defined authority and execution boundaries;
5. validation evidence against realistic use;
6. a resolved licensing and release path.

## Current candidates

| Candidate | State | Current purpose |
| --- | --- | --- |
| [ProDes](ProDes/) | EVALUATION / NOT_RELEASE_READY | Test whether prompt-package design can become a reusable public ORDO module. |
| [ORS](ORS/) | EVALUATION / NOT_RELEASE_READY | Construct a public-safe module from the internally active ORDO Response Standard. |
| [Commands](Commands/) | EARLY_DESIGN / NOT_RELEASE_READY | Explore a canonical, governed command language and its complete response behavior. |

Additional structure should be added only when demonstrated need justifies it.
