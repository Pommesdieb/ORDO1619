# ORDO Public Design Language

The ORDO Public Design Language projects ORDO's semantic architecture into a coherent visual and communicative system.

Design is not decoration applied to ORDO documentation. It is a visual projection of ORDO's semantic model.

## Development status

**DESIGN_CONCEPTION**

This directory is an experimental development environment. Its structure may change as design evidence emerges.

## Semantic authority

`Design/` does not redefine ORDO semantics.

Normative concepts remain governed by their authoritative ORDO contracts. This directory develops public-facing representations of those concepts and tests whether they remain clear across repositories, documentation, diagrams, and later interfaces.

`Design/Semantics/` therefore has **projection authority, not semantic authority**.

## Direction

```text
ORDO semantic architecture
        ↓
Design semantics
        ↓
visual and communicative representation rules
        ↓
elements + patterns + visualization
        ↓
public surfaces
```

Repository structure, documentation, diagrams, and later interfaces are downstream consumers of the design language rather than its source.

## Current MVP

The initial physical footprint is intentionally small:

- [`Foundations/Principles.md`](Foundations/Principles.md)
- [`Semantics/Identity.md`](Semantics/Identity.md)
- [`Playground/README.md`](Playground/README.md)

Additional structure should emerge only from demonstrated need.

## Public boundary

Public ORDO is constructed from public-safe semantics. Private Control Plane data, registry records, personal data, sensitivity configuration, and internal operational provenance must not enter the design system merely because they exist in Development.
