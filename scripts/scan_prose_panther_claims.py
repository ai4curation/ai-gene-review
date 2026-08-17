"""Check PANTHER family ids written into module prose against PANTHER's own data.

Module validation reads ``term.id``/``term.label`` pairs, so a PANTHER id that
appears in a ``notes``, ``description`` or ``statement`` field is invisible to
it. That gap is not theoretical: nine such claims were contradicted by
``interpro/panther/panther-members.tsv`` -- the same file committed to validate
the structured slots -- including three naming a family none of the proteins
belonged to. Removing a wrong id from ``term`` while leaving it asserted in prose
is worse than leaving both, because prose is what a curator reads when deciding
how to re-ground a descriptor.

Two constraints, both learned by getting them wrong first:

* **Match ids exactly.** A fixed-width lookahead window truncates ids
  mid-number (``PTHR11157`` -> ``PTHR111``), which manufactures false positives.
  Find complete ids, then test proximity.
* **Report what could not be checked.** ``panther-members.tsv`` indexes
  accessions cited in ``representative_members``; prose-only accessions may be
  absent. Skipping those silently reports a clean sweep over a set that was
  partly unexamined. They are counted and listed, and ``--online`` resolves them
  through UniProt.

Only accession/id pairs are checked. Claims phrased with gene symbols
("CYP17A1/CYP21A2 share PTHR24289") are not detected -- the symbol-to-accession
step is ambiguous, and a wrong guess there would be a false accusation.

Measured against the nine errors it was built from (run it over the tree at
afbc432eb5): it catches seven. The two it misses are precisely the documented
limitations -- one symbol-phrased, one the first-named member of a shared claim.
That is the honest detection rate, not a clean sweep.

Usage::

    uv run python scripts/scan_prose_panther_claims.py            # offline
    uv run python scripts/scan_prose_panther_claims.py --online   # + UniProt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, Iterator, List, NamedTuple

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ai_gene_review.etl.panther_families import (  # noqa: E402
    fetch_panther_from_uniprot,
)
from ai_gene_review.validation.module_validator import (  # noqa: E402
    load_member_index,
)

# UniProtKB accession syntax (both the classic and the extended forms).
ACCESSION_RE = re.compile(
    r"\b([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})\b"
)
# Complete PANTHER ids only -- never a prefix of one.
PANTHER_RE = re.compile(r"\bPTHR\d+(?::SF\d+)?\b")

# Prose slots. A PANTHER id in any of these is unreachable by term validation.
PROSE_KEYS = frozenset(
    {"notes", "description", "statement", "role_description", "preferred_term"}
)

# How close an id must sit after an accession to be read as a claim about it.
# Deliberately tight: at 60 characters the scan pairs accessions with the *next*
# protein's id across a clause boundary and reports false contradictions.
PROXIMITY_CHARS = 30


class Claim(NamedTuple):
    """A prose assertion that some accession belongs to some PANTHER family."""

    module: str
    accession: str
    claimed_family: str


def iter_prose(node: object) -> Iterator[str]:
    """Yield every prose string in a module document, whitespace-normalised."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in PROSE_KEYS and isinstance(value, str):
                yield " ".join(value.split())
            yield from iter_prose(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_prose(item)


def extract_claims(module: str, text: str) -> Iterator[Claim]:
    """Yield accession/family claims from one prose string.

    An id is attributed to the accession it *immediately* follows. Proximity
    alone is not enough: at any useful distance it also pairs an accession with
    the NEXT protein's id across a clause boundary, inventing a contradiction.

    >>> list(extract_claims("m", "HSD17B4 (P51659 PTHR45024, hydratase)"))
    [Claim(module='m', accession='P51659', claimed_family='PTHR45024')]

    The id here belongs to GDA, not to the PNP mentioned just before it:

    >>> list(extract_claims("m", "PNP P00491, GO:0004731); GDA Q9Y2T3 PTHR11271"))
    [Claim(module='m', accession='Q9Y2T3', claimed_family='PTHR11271')]

    Known limitation: a shared-family claim naming several members
    ("A (x) + B (y) share PTHR1") is only checked for the last-named accession.
    Attributing it to all of them would re-introduce the cross-clause error, and
    a false accusation is worse than a missed check.
    """
    accessions = list(ACCESSION_RE.finditer(text))
    for family in PANTHER_RE.finditer(text):
        preceding = [a for a in accessions if a.end() <= family.start()]
        if not preceding:
            continue
        anchor = preceding[-1]
        if family.start() - anchor.end() <= PROXIMITY_CHARS:
            yield Claim(module, anchor.group(1), family.group(0).split(":")[0])


def collect_claims(modules_dir: Path) -> List[Claim]:
    """Collect every prose claim across a modules directory."""
    claims: List[Claim] = []
    for path in sorted(Path(modules_dir).rglob("*.yaml")):
        document = yaml.safe_load(path.read_text())
        for text in iter_prose(document):
            claims.extend(extract_claims(path.name, text))
    return claims


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modules-dir", type=Path, default=REPO_ROOT / "modules")
    parser.add_argument(
        "--online",
        action="store_true",
        help="Resolve accessions missing from panther-members.tsv via UniProt.",
    )
    args = parser.parse_args(argv)

    index: Dict[str, str] = dict(
        load_member_index(REPO_ROOT / "interpro" / "panther" / "panther-members.tsv")
    )
    claims = collect_claims(args.modules_dir)

    missing = {c.accession for c in claims if c.accession not in index}
    if missing and args.online:
        index.update(fetch_panther_from_uniprot(missing))

    contradicted = [
        c
        for c in claims
        if c.accession in index
        and index[c.accession].split(":")[0] != c.claimed_family
    ]
    unresolvable = sorted({c.accession for c in claims if c.accession not in index})

    print(f"prose accession/PANTHER claims : {len(claims)}")
    print(f"checked                        : {len(claims) - sum(1 for c in claims if c.accession not in index)}")
    print(f"contradicted                   : {len(contradicted)}")
    print(f"unresolvable                   : {len(unresolvable)}")

    for claim in contradicted:
        print(
            f"❌ {claim.module}: {claim.accession} is claimed as "
            f"{claim.claimed_family} but PANTHER has it in "
            f"{index[claim.accession]}"
        )
    if unresolvable:
        print(
            "⚠️  not in panther-members.tsv, so NOT checked "
            f"(re-run with --online): {', '.join(unresolvable)}"
        )
    return 1 if contradicted else 0


if __name__ == "__main__":
    sys.exit(main())
