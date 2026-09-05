# ORDO1619

Public staging, demonstration, and release-candidate environment for ORDO.

## Status

This repository is **public by design**, but its contents are not automatically an ORDO Public Release.

Current role:

- public demonstration surface
- public staging environment
- release-candidate preparation
- distribution source for a future release to `ORDO1619/ORDO`

The current development state is **DESIGN_CONCEPTION**.

## Repository boundaries

| Role | Repository |
| --- | --- |
| Development SSoT | `Pommesdieb/ORDO` |
| Public staging, demonstration, and release-candidate environment | `Pommesdieb/ORDO1619` |
| Public release target | `ORDO1619/ORDO` |

Repository visibility does not imply release status.

`Pommesdieb/ORDO1619` is intentionally a separate public-facing staging surface. It is not a mirror of the private Development SSoT, and public-ready material is constructed from public-safe semantics rather than produced by sanitizing internal Development content.

## Current work

The immediate development focus is the **ORDO Public Design Language**: a visual and communicative system that projects ORDO's semantic architecture into a coherent external form.

See [`Design/`](Design/).

A minimal public module staging area is available under [`Modules/`](Modules/). Its current candidates, [`ProDes`](Modules/ProDes/) and [`ORS`](Modules/ORS/), are evaluation surfaces and not ORDO Public Releases.

## Release model

```text
Development
    ↓
Public-safe staging
    ↓
Release Candidate
    ↓
Assurance
    ↓
Public Boundary / Risk Review
    ↓
Human Gate
    ↓
Public Release
```

A state in this repository may be demonstrable, experimental, or release-candidate material without being an ORDO Public Release. Promotion to `ORDO1619/ORDO` is a separate governed transaction.

## License

No license has been granted yet.
