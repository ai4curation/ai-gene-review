"""Validation of residue numbers that reference findings report.

A paper often numbers residues on an isoform other than the one UniProt displays, so
one residue appears under two numbers: RASAL2 "S351" (PMID:33563064) is Ser351 of
isoform 2 (Q9UJF2-2) and Ser203 of the displayed sequence (Q9UJF2), where position
351 is Asp. Read against the wrong sequence, such a number silently names the wrong
residue or a residue in the wrong domain.

``references[].findings[].residue_mappings`` records each named residue in the
sequence whose numbering the source used (``as_reported``) and, optionally, the same
residue in the displayed sequence of the review's entry (``canonical``). Checks:

``AS_REPORTED``
    The reported sequence has that residue at that position.
``CANONICAL_IDENTITY``
    ``canonical`` names this review's own entry, without an isoform suffix.
``CANONICAL``
    The displayed sequence has that residue at that position.
``SAME_RESIDUE``
    Both sides claim the same amino acid; a mapping between two different residues
    cannot be the same position in two numberings.

Only UniProtKB sequences can be fetched. A side whose accession carries another
prefix (an isoform known only from RefSeq, say) is reported ``UNRESOLVED`` rather than
failing the run; a prefix-less accession is treated as UniProtKB, as in
``gene_residue_claims``.

Positions are resolved with the same sequence cache and position check as
``gene_residue_claims``. The slot is optional, so reviews that state residues only
in prose are unaffected.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from yaml import CSafeLoader as _Loader

from ai_gene_review.validation.family_residue_validator import SequenceCache
from ai_gene_review.validation.gene_residue_claims import (
    ClaimCheck,
    ClaimOutcome,
    _check_position,
)


def _bare(accession: str) -> str:
    """Strip a CURIE prefix.

    >>> _bare("UniProtKB:Q9UJF2-2")
    'Q9UJF2-2'
    """
    return accession.split(":")[-1]


def _check_side(
    cache: SequenceCache, spec: dict, label: str, gene: str, ref_id: str, kind: str
) -> ClaimCheck:
    """Check one side of a mapping; report it unresolved if it names a non-UniProtKB prefix.

    >>> _check_side(None, {"accession": "RefSeq:NP_1.1", "position": 1, "residue": "M"},
    ...             "as reported", "G", "PMID:1", "AS_REPORTED").outcome.value
    'UNRESOLVED'
    """
    acc = spec["accession"]
    if ":" in acc and not acc.startswith("UniProtKB:"):
        return ClaimCheck(
            kind, gene, ref_id,
            f"{label} {spec['accession']} cannot be checked: only UniProtKB sequences "
            "are fetched",
            ClaimOutcome.UNRESOLVED,
        )
    check, _ = _check_position(cache, spec, label, gene, ref_id, kind)
    return check


def check_mapping(
    mapping: dict,
    review_accession: str,
    gene: str,
    ref_id: str,
    cache: SequenceCache,
) -> list[ClaimCheck]:
    """Run every check for one residue mapping on one finding."""
    reported = mapping["as_reported"]
    results = [_check_side(cache, reported, "as reported", gene, ref_id, "AS_REPORTED")]
    canonical = mapping.get("canonical")
    if not canonical:
        return results

    if _bare(canonical["accession"]) == _bare(review_accession):
        results.append(ClaimCheck(
            "CANONICAL_IDENTITY", gene, ref_id,
            f"canonical {canonical['accession']} is this review's entry",
            ClaimOutcome.PASS,
        ))
    else:
        results.append(ClaimCheck(
            "CANONICAL_IDENTITY", gene, ref_id,
            f"canonical {canonical['accession']} is not this review's displayed "
            f"sequence; use UniProtKB:{_bare(review_accession)} without an isoform suffix",
            ClaimOutcome.FAIL,
        ))
    results.append(_check_side(cache, canonical, "canonical", gene, ref_id, "CANONICAL"))

    same = reported["residue"] == canonical["residue"]
    results.append(ClaimCheck(
        "SAME_RESIDUE", gene, ref_id,
        f"as reported {reported['residue']}{reported['position']} and canonical "
        f"{canonical['residue']}{canonical['position']} "
        + ("are the same amino acid" if same else "are different amino acids"),
        ClaimOutcome.PASS if same else ClaimOutcome.FAIL,
    ))
    return results


def validate_finding_residue_mappings(path: Path, cache: SequenceCache) -> list[ClaimCheck]:
    """Validate every residue mapping on the reference findings of one gene review."""
    doc = yaml.load(path.read_text(), Loader=_Loader) or {}
    gene = doc.get("gene_symbol") or path.stem
    accession = doc.get("id", "")
    results: list[ClaimCheck] = []
    for ref in doc.get("references") or []:
        for finding in ref.get("findings") or []:
            for mapping in finding.get("residue_mappings") or []:
                results.extend(check_mapping(mapping, accession, gene, ref["id"], cache))
    return results


def main(argv: list[str] | None = None) -> int:
    """Validate finding residue mappings across the gene corpus."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Validate finding residue mappings.")
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--genes-dir", type=Path, default=Path("genes"))
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/uniprot_seq"))
    args = parser.parse_args(argv)

    paths = args.paths or sorted(args.genes_dir.glob("*/*/*-ai-review.yaml"))
    cache = SequenceCache(args.cache_dir)
    counts = {o.value: 0 for o in ClaimOutcome}
    reviews = 0
    for path in paths:
        if "residue_mappings" not in path.read_text():   # cheap skip; most have none
            continue
        results = validate_finding_residue_mappings(path, cache)
        reviews += bool(results)
        for r in results:
            counts[r.outcome.value] += 1
            if r.outcome is not ClaimOutcome.PASS:
                print(r, file=sys.stderr)
    print(
        f"finding residue-mapping validation over {reviews} gene review(s): "
        f"{counts['PASS']} pass, {counts['FAIL']} fail, {counts['UNRESOLVED']} unresolved"
    )
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
