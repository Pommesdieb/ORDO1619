# Design Principles

These principles guide the ORDO Public Design Language during `DESIGN_CONCEPTION`.

They describe preferred design behavior. They do not replace normative ORDO contracts.

## Semantic clarity before decoration

Every visible distinction should correspond to a meaningful distinction. Decorative structure without semantic value should be avoided.

Prefer short, stable, speaking names and visually distinguish concepts only when the underlying ORDO semantics are genuinely different.

## Meaning before visual convention

Typography, color, spacing, labels, borders, diagrams, and syntax are representational tools. They must follow meaning rather than define it.

A visual treatment must not silently merge or redefine Entity, Workspace, WID, Interaction Identity, Authority, Owner, Repository, or Release State.

## Progressive disclosure

The first layer should be understandable by humans without requiring full framework knowledge. Technical precision remains available underneath and appears where it is needed.

Simple entry does not justify simplified parallel semantics.

## Human-first, technical underneath

Public ORDO should be easy to enter, inspect, and explain. Reference detail, contracts, provenance, and governance remain precise, but they should not dominate the first orientation layer.

## Public by design

Public material is constructed from public-safe semantics rather than created by redacting private Development content at the end.

Private Control Plane information, registry records, personal data, sensitivity configuration, and internal operational provenance are excluded by default.

## Carrier independence

Design terminology and semantic distinctions should remain meaningful if GitHub, ChatGPT, Drive, Markdown, or another implementation carrier changes.

Carrier-specific guidance belongs at the surface layer and must not redefine underlying semantics.

## One semantic model, multiple views

Human-facing and technical representations should derive from the same semantic model.

Different views may vary in depth, order, examples, and visual density, but they must not evolve into independently maintained meanings.

## Structure only when needed

Use as little repository and document structure as possible and as much as necessary.

Do not create empty directories, speculative hierarchy, or taxonomy merely for possible future use.

## Reversible, low-maintenance implementation

Prefer static artifacts, Markdown, simple diagrams, and understandable file structures over generators, services, build dependencies, or complex tooling unless demonstrated value justifies them.

## Restrained visual hierarchy

Favor whitespace, text-first presentation, clear grouping, functional diagrams, and deliberate emphasis.

Avoid dashboard styling, decorative density, and visual hierarchy that competes with semantic hierarchy.

## Examples before abstract completeness

A small number of strong examples should make ORDO understandable before the public surface attempts to expose the full internal taxonomy.

Examples are both explanatory devices and tests of whether the design language works in practice.

## No Development-repository mirroring

The public staging and release-candidate environment is not a visual or structural mirror of `Pommesdieb/ORDO`.

Its information architecture should be derived from external comprehension and release needs.

## No premature brand or enterprise aesthetics

Do not introduce a Brand system, logo ecosystem, asset library, website architecture, template library, comprehensive component system, or token system before design evidence requires it.

The desired character is technically credible, calm, precise, and distinct rather than generically corporate.

## ORDO-WORK remains separate

The public presentation of ORDO must not semantically merge the personal and experimental ORDO core with a later commercial or professional ORDO-WORK derivation.
