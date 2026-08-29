# Identity

Identity is the first semantic stress test for the ORDO Public Design Language.

The purpose of this document is not to redefine ORDO identity semantics. It establishes the design problem that public representations must solve while preserving the authoritative distinctions defined elsewhere in ORDO.

## Design question

How can different ORDO identity dimensions remain immediately distinguishable without creating separate visual systems or parallel terminology?

## Semantic test set

| Dimension | Example | Meaning |
| --- | --- | --- |
| Entity Identifier | `OR-030` | Canonical identifier of an Entity within an Entity namespace |
| Workspace ID / WID | `ORDO.PD` | Stable logical identifier of a Workspace, independent of carrier |
| Interaction Identity | `ProDes` | Visible identity used for interaction in its governed context |
| Deferred Idea | `DI-003` | Identifier from a non-Entity identifier class |

These examples are deliberately close enough in use to expose ambiguity if the design language is weak.

## Invariants to preserve

Public representation must not collapse these distinctions:

```text
Entity ≠ Workspace
Workspace ≠ Interaction Identity
Entity Identifier ≠ Workspace ID
Entity Namespace ≠ non-Entity Identifier Class
Authority ≠ Owner
Repository ≠ Workspace
Visibility ≠ Release State
Carrier ≠ Identity
```

The visual language may clarify these relationships, but it must not invent new semantic categories to do so.

## Representation dimensions to test

The first experiments should test combinations of:

- syntax
- typography
- label placement
- weight
- spacing
- alignment
- annotation
- boundary
- relation
- information order

Color is secondary. A robust identity grammar should remain understandable in monochrome.

## Initial hypothesis

**Structure carries meaning before decoration does.**

A viable ORDO design language should make identity dimensions recognizable through stable form, context, and hierarchy before relying on color, iconography, or branded decoration.

## Evaluation criteria

An experiment is promising when a reader can:

1. distinguish the identity dimensions without prior exposure to the full framework;
2. understand that the dimensions belong to one coherent system;
3. avoid inferring false equivalence between syntax or labels;
4. trace the representation back to authoritative ORDO semantics;
5. reuse the same grammar across Markdown, repository documentation, diagrams, and later interfaces.

Concrete visual treatments belong in `Design/Playground/` until they are sufficiently tested for promotion.
