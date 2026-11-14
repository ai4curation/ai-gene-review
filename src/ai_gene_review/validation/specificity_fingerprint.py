"""Check a protein for a curated substrate-specificity fingerprint (Kinateder et al. 2024).

Family HMMs and trusted cutoffs (``enzyme_family_cutoff``) say whether a protein belongs
to a family. Within a superfamily whose families catalyse different reactions, closely
related paralogs can pass the same models, and what decides the reaction is a handful
of substrate-pocket residues. Kinateder et al. (PMID:38284491) found such residues by an
alanine scan of one characterized histidinol-phosphate phosphatase, then used them to
sort its homologues, many annotated as phosphoserine phosphatases, and confirmed the
calls in vitro.

This module applies a curated fingerprint to any protein: align the query to the
fingerprint's reference protein, read the residues at the reference positions, and
compare them with the residues that indicate the function and with those typical of the
paralogous ("contrast") function. Fingerprints live in ``conf/specificity_fingerprints.yaml``
and must come from mutagenesis plus testing of homologues; this module never infers one.

Verdicts
--------
``PRESENT``
    Every required position carries an indicating residue.
``CONTRAST``
    Every required position carries a residue typical of the contrast function.
``PARTIAL``
    Some, but not all, required positions carry an indicating residue.
``ABSENT``
    No required position carries an indicating residue.
``LOW_IDENTITY``
    Identity to the reference is below the fingerprint's ``min_identity``, so the
    alignment is not trusted. Residues are still reported.

In the protocol of Schnoes et al. (PMID:20011109) this follows family membership and the
catalytic-residue check: a protein can belong to the family and keep its catalytic
machinery while carrying the residues of a different substrate specificity.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml
from Bio import Align
from Bio.Align import substitution_matrices

from ai_gene_review.validation.family_residue_validator import SequenceCache

DEFAULT_FINGERPRINTS = Path("conf/specificity_fingerprints.yaml")


@dataclass
class Position:
    """One fingerprint position, numbered on the reference protein."""

    position: int
    residues: list[str]
    role: str  # "required" or "supporting"
    contrast_residues: list[str] = field(default_factory=list)


@dataclass
class Fingerprint:
    """A curated specificity fingerprint."""

    id: str
    function: dict
    contrast_function: dict | None
    reference: dict
    min_identity: float
    source: dict
    positions: list[Position]

    @classmethod
    def from_dict(cls, d: dict) -> Fingerprint:
        return cls(
            id=d["id"],
            function=d["function"],
            contrast_function=d.get("contrast_function"),
            reference=d["reference"],
            min_identity=d["min_identity"],
            source=d["source"],
            positions=[Position(**p) for p in d["positions"]],
        )


@dataclass
class ResidueCall:
    """The query residue aligned to one fingerprint position."""

    position: int
    role: str
    expected: list[str]
    query_position: int | None
    query_residue: str | None  # None when the position aligns to a gap
    matches: bool
    matches_contrast: bool


@dataclass
class FingerprintReport:
    accession: str
    fingerprint: str
    function: str
    reference: str
    identity: float
    verdict: str
    calls: list[ResidueCall]


def load_fingerprints(path: Path = DEFAULT_FINGERPRINTS) -> dict[str, Fingerprint]:
    """Read the curated fingerprints, keyed by id."""
    data = yaml.safe_load(path.read_text())
    return {d["id"]: Fingerprint.from_dict(d) for d in data["fingerprints"]}


def align_positions(reference: str, query: str) -> tuple[dict[int, int], float]:
    """Map 1-based reference positions to query positions by global alignment.

    Returns the mapping and the identity: identical aligned positions divided by the
    reference length, so a short fragment cannot reach a high identity.

    >>> mapping, identity = align_positions("MKDLDYW", "MKDLEYW")
    >>> mapping[5], round(identity, 2)
    (5, 0.86)
    >>> mapping, _ = align_positions("MKDLDYWAA", "MKDYWAA")
    >>> mapping[1], mapping[6], 4 in mapping
    (1, 4, False)
    """
    aligner = Align.PairwiseAligner(
        mode="global",
        substitution_matrix=substitution_matrices.load("BLOSUM62"),
        open_gap_score=-10,
        extend_gap_score=-0.5,
        # free end gaps, so a query with extra termini is not forced into internal gaps
        end_gap_score=0,
    )
    alignment = aligner.align(reference, query)[0]
    mapping: dict[int, int] = {}
    for (r_start, r_end), (q_start, _q_end) in zip(*alignment.aligned):
        for offset in range(int(r_end - r_start)):
            mapping[int(r_start) + offset + 1] = int(q_start) + offset + 1
    identical = sum(reference[r - 1] == query[q - 1] for r, q in mapping.items())
    return mapping, identical / len(reference)


def call_residues(
    fp: Fingerprint, reference: str, query: str
) -> tuple[list[ResidueCall], float]:
    """Read the query residue at each fingerprint position."""
    mapping, identity = align_positions(reference, query)
    calls = []
    for p in fp.positions:
        q_pos = mapping.get(p.position)
        residue = query[q_pos - 1] if q_pos else None
        calls.append(
            ResidueCall(
                position=p.position,
                role=p.role,
                expected=p.residues,
                query_position=q_pos,
                query_residue=residue,
                matches=residue in p.residues,
                matches_contrast=residue in p.contrast_residues,
            )
        )
    return calls, identity


def verdict_for(calls: list[ResidueCall], identity: float, min_identity: float) -> str:
    """Reduce residue calls to a verdict; see the module docstring.

    >>> c = lambda m, x=False: ResidueCall(1, "required", ["D"], 1, "D", m, x)
    >>> verdict_for([c(True), c(True)], 0.6, 0.45)
    'PRESENT'
    >>> verdict_for([c(False, True), c(False, True)], 0.6, 0.45)
    'CONTRAST'
    >>> verdict_for([c(True), c(False)], 0.6, 0.45)
    'PARTIAL'
    >>> verdict_for([c(True), c(True)], 0.3, 0.45)
    'LOW_IDENTITY'
    """
    if identity < min_identity:
        return "LOW_IDENTITY"
    required = [c for c in calls if c.role == "required"]
    if all(c.matches for c in required):
        return "PRESENT"
    if all(c.matches_contrast for c in required):
        return "CONTRAST"
    if any(c.matches for c in required):
        return "PARTIAL"
    return "ABSENT"


def check(accession: str, fp: Fingerprint, cache: SequenceCache) -> FingerprintReport:
    """Apply one fingerprint to one UniProt protein."""
    reference = cache.get(fp.reference["accession"])
    calls, identity = call_residues(fp, reference, cache.get(accession))
    return FingerprintReport(
        accession=accession,
        fingerprint=fp.id,
        function=f"{fp.function['go']} {fp.function['label']}",
        reference=fp.reference["accession"],
        identity=round(identity, 3),
        verdict=verdict_for(calls, identity, fp.min_identity),
        calls=calls,
    )


def reference_mismatches(fp: Fingerprint, cache: SequenceCache) -> list[str]:
    """Positions where the reference protein does not carry the curated residue.

    A non-empty result means the fingerprint's numbering or reference is wrong.
    """
    reference = cache.get(fp.reference["accession"])
    return [
        f"{fp.id}: {fp.reference['accession']} position {p.position} is "
        f"{reference[p.position - 1] if p.position <= len(reference) else 'beyond the end'}, "
        f"expected {'/'.join(p.residues)}"
        for p in fp.positions
        if p.position > len(reference) or reference[p.position - 1] not in p.residues
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("accession", help="UniProt accession of the query protein")
    parser.add_argument("--fingerprint", help="fingerprint id; default: all")
    parser.add_argument("--fingerprints-file", type=Path, default=DEFAULT_FINGERPRINTS)
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/uniprot_seq"))
    parser.add_argument("-o", "--output", type=Path, help="Write the YAML report here")
    args = parser.parse_args(argv)

    fingerprints = load_fingerprints(args.fingerprints_file)
    if args.fingerprint and args.fingerprint not in fingerprints:
        parser.error(
            f"unknown fingerprint {args.fingerprint}; known: {', '.join(fingerprints)}"
        )
    selected = (
        [fingerprints[args.fingerprint]]
        if args.fingerprint
        else list(fingerprints.values())
    )
    cache = SequenceCache(args.cache_dir)
    reports = [check(args.accession, fp, cache) for fp in selected]

    text = yaml.safe_dump(
        [asdict(r) for r in reports], sort_keys=False, default_flow_style=None
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        sys.stdout.write(text)
    for r in reports:
        residues = " ".join(
            f"{c.position}{c.query_residue or '-'}{'*' if c.role == 'required' else ''}"
            for c in r.calls
        )
        print(
            f"{r.accession} {r.fingerprint}: {r.verdict} (identity {r.identity:.0%}; {residues})",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
