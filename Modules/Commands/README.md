# Commands

**Public status:** EARLY_DESIGN / PUBLIC_STAGING_CANDIDATE / NOT_RELEASE_READY  
**Development evidence:** ACTIVE DEVELOPMENT SUBJECT / CANONICAL MODULE CONTRACT ABSENT  
**Inclusion assessment:** FIT_AS_EARLY_MODULE_CANDIDATE

## Candidate purpose

Commands is the early design surface for a coherent, governed ORDO command language.

The intended subject is broader than a list of keywords. A command definition may need to describe the complete interaction contract around an invocation, including:

- recognized intent and invocation form;
- required context and preconditions;
- authority and capability boundaries;
- permitted effects and human gates;
- expected response behavior;
- failure, degradation, and recovery behavior;
- routing and handover semantics.

No specific command vocabulary or grammar is established by this staging page.

## Required boundaries

Commands must not:

- create authority merely because an invocation is recognized;
- turn a request into an implicit mutation, activation, approval, or release;
- treat interaction formats, roles, aliases, or ordinary natural-language intent as executable commands by default;
- invent missing target state, permissions, capabilities, or routing;
- duplicate ORS response-envelope authority;
- expose private registries, carrier bindings, internal audit data, or confidential operational context;
- present early design material as normative ORDO behavior.

Commands and ORS are related but distinct: Commands governs invocation and execution semantics; ORS governs the applicable response envelope. Their integration remains a design and validation task.

## Open design questions

Before a stable module can be specified, development must resolve at least:

1. the exact boundary between command, interaction format, ordinary intent, and implementation shortcut;
2. the canonical command definition schema;
3. naming, aliases, case sensitivity, parameters, and composition;
4. authority, permission, capability, and human-gate evaluation;
5. mutation and effect-state semantics;
6. complete-response requirements for each command;
7. errors, partial execution, recovery, and idempotency;
8. versioning, supersession, discoverability, and compatibility;
9. integration with ORS and target-specific profiles;
10. the public-safe command catalog and example set.

## Evidence needed for progression

Progression beyond early design requires at least:

- a consolidated candidate vocabulary;
- a canonical command-definition model;
- representative public-safe examples;
- ambiguity and collision tests;
- authority and effect-state regression fixtures;
- ORS integration tests;
- usability and accessibility evaluation;
- security and disclosure review;
- a licensing decision;
- explicit Release Candidate and Public Release gates.

Until these conditions are met, Commands remains an intentionally incomplete public staging candidate.
