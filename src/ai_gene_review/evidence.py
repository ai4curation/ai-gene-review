"""Preserve source evidence identifiers and share coarse evidence categories."""

from collections.abc import Iterable


# This is a reporting/policy category, NOT a GAF mapping or an assertion that
# combinatorial evidence is identical to EXP. Keep the source identifier in
# annotations, strict matching and exports. See docs/goa-evidence.md.
COMBINATORIAL_MANUAL_EVIDENCE = "ECO:0007744"
EXPERIMENTAL_EVIDENCE_CODES = frozenset({
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP",
    COMBINATORIAL_MANUAL_EVIDENCE,
})
LITERATURE_EVIDENCE_CODES = (
    EXPERIMENTAL_EVIDENCE_CODES - {"HTP", "HDA", "HMP", "HGI", "HEP"}
) | {"TAS", "NAS"}


def source_evidence_code(go_code: str | None, eco_id: str | None = None) -> str:
    """Use a supplied GO shorthand, otherwise preserve the supplied ECO id."""
    return (go_code or "").strip() or (eco_id or "").strip()


def evidence_matches(code: str | None, accepted: Iterable[str]) -> bool:
    """Apply broad EXP policy to evidence with an experimental component.

    Exact configured ECO matches also work. This does not license an IDA/IMP
    inference or change an annotation's evidence identifier.
    """
    value = source_evidence_code(code)
    accepted = frozenset(accepted)
    return value in accepted or (
        value == COMBINATORIAL_MANUAL_EVIDENCE and "EXP" in accepted
    )
