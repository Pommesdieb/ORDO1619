#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

RULES = {f"PD-{number:03d}" for number in range(1, 9)}
CONTROL_COMMANDS = {"identity creation", "ordo_init", "ordo_refresh"}
IDENTITY_KEYS = {
    "workspace_name",
    "entity_canonical_name",
    "stable_identifiers",
    "functional_identity",
    "interaction_identity",
    "conversation_binding",
}
FORBIDDEN_DISCLOSURE = {
    "private_repository_locator": re.compile(r"Pommesdieb/(?:ORDO|ISAAC|ORDO-WORK)"),
    "private_workspace_identifier": re.compile(r"\b(?:ORDO|ISAAC)\.[A-Z0-9.-]+\b"),
    "internal_record_identifier": re.compile(r"\b(?:OR|OW|IE|DI)-[0-9]{3,}\b"),
    "carrier_reference_value": re.compile(r"(?:conversation[_ -]?(?:id|ref)|carrier[_ -]?locator)\s*[:=]\s*\S+", re.I),
}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def deep_merge(base: dict, patch: dict) -> dict:
    result = copy.deepcopy(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def validate_package(package: dict) -> list[str]:
    errors: set[str] = set()
    identity = package.get("identity_fields", {})

    for identifier in identity.get("stable_identifiers", []):
        if not identifier.get("provenance_verified") or not identifier.get("creation_authorized"):
            errors.add("PD-001")

    content = package.get("artifact", {}).get("content", "")
    lowered = content.lower()
    if (
        package.get("artifact_type") == "INIT"
        and package.get("target_profile") == "ordo-work"
        and package.get("persistent") is True
    ):
        markers = ["current workspace.name", "identity creation", "ordo_init"]
        positions = [lowered.find(marker) for marker in markers]
        if any(position < 0 for position in positions) or positions != sorted(positions):
            errors.add("PD-002")

    command_lines = [line.strip().lower() for line in content.splitlines()]
    if any(command_lines.count(command) > 1 for command in CONTROL_COMMANDS):
        errors.add("PD-003")

    for claim in package.get("mutable_claims", []):
        resolved_now = claim.get("source") == "runtime_resolver" and claim.get("verified") is True
        if claim.get("mode") != "resolve_at_execution" and not resolved_now:
            errors.add("PD-004")

    if "canonical_name" in identity or any(key not in IDENTITY_KEYS for key in identity):
        errors.add("PD-005")

    resolve_first = set(package.get("resolve_first", []))
    fixed_results = set(package.get("fixed_results", {}))
    if resolve_first & fixed_results:
        errors.add("PD-006")

    phase = package.get("phase")
    for item in package.get("capability_preflight", []):
        if item.get("blocking") and item.get("required_phase") != phase:
            errors.add("PD-007")

    forbidden_sections = ("## analysis", "## provenance", "## runtime metadata")
    if not content.strip() or any(section in lowered for section in forbidden_sections):
        errors.add("PD-008")

    return sorted(errors)


def check_regressions(module_root: Path) -> tuple[int, list[dict]]:
    data = json.loads((module_root / "fixtures" / "regressions.json").read_text(encoding="utf-8"))
    base = data["base_package"]
    findings = []
    for case in data["cases"]:
        actual = validate_package(deep_merge(base, case["patch"]))
        expected = sorted(case["expected_errors"])
        if actual != expected:
            findings.append({"case": case["id"], "expected": expected, "actual": actual})
    covered = {rule for case in data["cases"] for rule in case["expected_errors"]}
    if covered != RULES:
        findings.append({"coverage": sorted(covered), "required": sorted(RULES)})
    return len(data["cases"]), findings


def check_examples(module_root: Path) -> list[dict]:
    findings = []
    for path in sorted((module_root / "examples").glob("*-package.json")):
        errors = validate_package(json.loads(path.read_text(encoding="utf-8")))
        if errors:
            findings.append({"example": path.name, "errors": errors})
    review = json.loads((module_root / "examples" / "review-report.json").read_text(encoding="utf-8"))
    required = {"goal_evaluation", "generator_compliance", "observed_effects", "findings", "next_routes"}
    missing = sorted(required - set(review))
    if missing:
        findings.append({"example": "review-report.json", "missing": missing})
    return findings


def check_links(repo_root: Path, module_root: Path) -> list[dict]:
    findings = []
    sources = [repo_root / "README.md", repo_root / "Modules" / "README.md"]
    sources.extend(sorted(module_root.rglob("*.md")))
    for source in sources:
        text = source.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            candidate = (source.parent / target).resolve()
            if not candidate.exists():
                findings.append({"source": str(source.relative_to(repo_root)), "target": raw})
    return findings


def check_disclosure(module_root: Path) -> list[dict]:
    findings = []
    for path in sorted(module_root.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".json", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        for name, pattern in FORBIDDEN_DISCLOSURE.items():
            if pattern.search(text):
                findings.append({"file": str(path.relative_to(module_root)), "kind": name})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Assure the public ProDes staging module.")
    parser.add_argument("--self-test", action="store_true", help="Run regression, example, link, and disclosure checks.")
    parser.add_argument("package", nargs="?", help="Optional prompt package JSON to validate.")
    args = parser.parse_args()

    if args.package:
        path = Path(args.package)
        errors = validate_package(json.loads(path.read_text(encoding="utf-8")))
        print(json.dumps({"package": str(path), "errors": errors, "result": "PASS" if not errors else "FAIL"}, indent=2))
        return 0 if not errors else 1

    if not args.self_test:
        parser.error("provide --self-test or a package path")

    module_root = Path(__file__).resolve().parents[1]
    repo_root = module_root.parents[1]
    case_count, regression_findings = check_regressions(module_root)
    findings = {
        "regressions": regression_findings,
        "examples": check_examples(module_root),
        "links": check_links(repo_root, module_root),
        "disclosure": check_disclosure(module_root),
    }
    prodes_dirs = [path for path in (repo_root / "Modules").iterdir() if path.is_dir() and path.name.lower() == "prodes"]
    if len(prodes_dirs) != 1:
        findings["module_count"] = [{"expected": 1, "actual": len(prodes_dirs)}]
    failed = any(findings.values())
    summary = {
        "result": "FAIL" if failed else "PASS",
        "regression_cases": case_count,
        "rules_covered": len(RULES),
        "findings": findings,
    }
    print(json.dumps(summary, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
