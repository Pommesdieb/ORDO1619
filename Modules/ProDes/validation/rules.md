# Validation rules

**Status:** PUBLIC_STAGING / EXECUTABLE_CANDIDATE

| Rule | Failure condition |
| --- | --- |
| PD-001 IDENTIFIER_PROVENANCE | A stable identifier is generated or asserted without verified provenance and explicit creation authority. |
| PD-002 INIT_ORDER | A persistent ORDO-WORK INIT artifact does not order workspace name, Identity creation, and `ordo_init` correctly. |
| PD-003 COMMAND_DEDUPLICATION | A bootstrap or refresh command is repeated without an explicit target requirement. |
| PD-004 MUTABLE_STATE_RESOLUTION | Mutable runtime, version, registry, authority, or capability state is copied as fixed current truth instead of resolved at execution. |
| PD-005 IDENTITY_DIMENSION_SEPARATION | Distinct identity dimensions are collapsed into an ambiguous field. |
| PD-006 RESOLVE_RESULT_CONTRADICTION | The package asks to resolve a field and also fixes its result. |
| PD-007 PHASE_SCOPED_PREFLIGHT | A future-phase capability blocks the current independent phase. |
| PD-008 ARTIFACT_BOUNDARY | The copyable artifact is missing or mixed with analysis, provenance, or runtime metadata. |

The executable validator is intentionally narrow. It demonstrates these invariants against public fixtures; it is not a target authority resolver and cannot prove live usability.
