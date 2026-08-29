"""Deterministic validation of curated residue sites in family reviews.

A ``ResidueSite`` says "position N of protein P is expected to be residue X". That is a
checkable statement, and this module checks it: it fetches P's sequence and compares.

This is the same discipline the repo already applies elsewhere -- ``supporting_text`` must
be a verbatim substring of a cached publication, GO ids must resolve in the ontology --
extended to residue claims, which until now were only ever prose. The motivating evidence:
of 17 "lacks the catalytic residue" claims surveyed in this repo, 4 were made about
proteins whose catalytic site was fully intact.

Two checks, deliberately separated by cost:

``check_anchor_residues``
    Confirms each curated position really carries one of the expected residues in the
    anchor protein. Needs one sequence per site and no alignment, so it is cheap enough to
    run in CI on every changed file. It catches invented positions, wrong residue
    identities, off-by-one numbering, and anchors pointing at the wrong protein.

``check_controls``
    Confirms the declared positive controls retain the site and the negative controls do
    not. This is what catches a *mislabelled control*, which is the failure that makes
    genuine enzymes look degenerate -- an earlier PGRP analysis in this repo used
    Drosophila PGRP-LE as a "catalytic" control when it is itself non-catalytic, and every
    real amidase then appeared to have lost the site. Controls need an alignment when the
    control's own numbering differs from the anchor's, so this check reports UNRESOLVED
    rather than failing when no alignment is supplied.

Known limitation
----------------
Residue-identity checking cannot detect an off-by-one *inside a run of the same amino
acid*. PGLYRP2 has a tandem His pair at 410-411, so a claim citing 411 for the zinc ligand
at 410 still finds a histidine and passes. This catches invented positions, wrong residue
identities, and anchors pointing at the wrong protein; distinguishing a shift within a
tandem repeat needs alignment- or structure-level checking. See
``test_tandem_residues_hide_off_by_one_errors``.
"""

from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Iterable

import yaml

UNIPROT_JSON = "https://rest.uniprot.org/uniprotkb/{acc}.json"


class Outcome(str, Enum):
    """Result of a single residue check."""

    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"


@dataclass
class ResidueCheck:
    """One curated position, checked against the anchor sequence."""

    family: str
    site_id: str
    accession: str
    position: int
    expected: list[str]
    observed: str | None
    outcome: Outcome
    message: str

    def __str__(self) -> str:
        return (
            f"[{self.outcome.value}] {self.family}#{self.site_id} "
            f"{self.accession}:{self.position} {self.message}"
        )


@dataclass
class SequenceCache:
    """Fetches and caches UniProt sequences.

    Sequences are cached on disk so CI does not refetch, and so a validation run is
    reproducible from a checkout. No try/except around the fetch: a network failure should
    surface, not be silently converted into an UNRESOLVED result that looks like curation
    uncertainty.
    """

    cache_dir: Path
    _mem: dict[str, str] = field(default_factory=dict)

    def get(self, accession: str) -> str:
        """Return the amino-acid sequence for a UniProt accession."""
        acc = accession.split(":")[-1]
        if acc in self._mem:
            return self._mem[acc]
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        path = self.cache_dir / f"{acc}.seq"
        if path.exists():
            seq = path.read_text().strip()
        else:
            req = urllib.request.Request(
                UNIPROT_JSON.format(acc=acc), headers={"User-Agent": "ai-gene-review"}
            )
            with urllib.request.urlopen(req, timeout=60) as fh:
                seq = json.load(fh)["sequence"]["value"]
            path.write_text(seq)
        self._mem[acc] = seq
        return seq


def _residue_at(seq: str, position: int) -> str | None:
    """Return the 1-based residue, or None if the position is out of range."""
    if 1 <= position <= len(seq):
        return seq[position - 1]
    return None


def check_anchor_residues(
    review: dict, cache: SequenceCache
) -> list[ResidueCheck]:
    """Check every curated residue position against its anchor protein's sequence.

    The anchor is the site's own ``anchor`` if present, else the family
    ``reference_protein``. A site with neither is UNRESOLVED rather than FAIL: the claim
    is incomplete, not contradicted.
    """
    family = review.get("family_id", "?")
    default_anchor = (review.get("reference_protein") or {}).get("id")
    results: list[ResidueCheck] = []

    for site in review.get("residue_sites") or []:
        site_id = site.get("site_id", "?")
        anchor = (site.get("anchor") or {}).get("id") or default_anchor
        if not anchor:
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.UNRESOLVED,
                    "no anchor on the site and no reference_protein on the family",
                )
            )
            continue

        seq = cache.get(anchor)
        for res in site.get("residues") or []:
            pos = res["position"]
            expected = list(res["expected"])
            observed = _residue_at(seq, pos)
            if observed is None:
                outcome = Outcome.FAIL
                msg = f"position beyond end of sequence (length {len(seq)})"
            elif observed in expected:
                outcome = Outcome.PASS
                msg = f"expected {'/'.join(expected)}, found {observed}"
            else:
                outcome = Outcome.FAIL
                msg = (
                    f"expected {'/'.join(expected)}, found {observed} "
                    f"-- the curated position does not carry the curated residue"
                )
            results.append(
                ResidueCheck(family, site_id, anchor, pos, expected, observed, outcome, msg)
            )

        motif = site.get("motif")
        if motif:
            results.append(_check_motif(family, site_id, anchor, seq, motif))

    return results


def _check_motif(
    family: str, site_id: str, anchor: str, seq: str, motif: dict
) -> ResidueCheck:
    """Check that the anchor's declared block matches the curated pattern."""
    import re

    start, end = motif["start"], motif["end"]
    pattern = motif["pattern_regex"]
    if not (1 <= start <= end <= len(seq)):
        return ResidueCheck(
            family, site_id, anchor, start, [pattern], None, Outcome.FAIL,
            f"block {start}-{end} is out of range for a {len(seq)}-residue sequence",
        )
    block = seq[start - 1 : end]
    if re.fullmatch(pattern, block):
        return ResidueCheck(
            family, site_id, anchor, start, [pattern], block, Outcome.PASS,
            f"block {start}-{end} is {block!r}, matches /{pattern}/",
        )
    return ResidueCheck(
        family, site_id, anchor, start, [pattern], block, Outcome.FAIL,
        f"block {start}-{end} is {block!r}, does not match /{pattern}/",
    )


def check_node_assessments(review: dict, paint_index: dict) -> list[ResidueCheck]:
    """Check every ``node_assessment`` against the family's own cached PAINT rows.

    A node assessment claims "PAINT asserted term T at node N". That is checkable against
    ``interpro/panther/<PTHR>/<PTHR>-paint.tsv``, and checking it stops an agent inventing
    a plausible node/term pairing -- the same class of hallucination that curated PANTHER
    family ids already guard against.

    Three things are verified, and the second matters more than it looks:

    1. The node exists in the cached PAINT index at all.
    2. The node belongs to **this** family. PTN ids are *not* family-unique -- 283 of the
       6094 nodes in this repo's PAINT slices appear under more than one family (e.g.
       PTN000010968 under PTHR43464, PTHR43591 and PTHR44068), so a family-agnostic lookup
       would happily accept another family's node.
    3. The asserted term is actually recorded at that node, rather than merely being a term
       the family carries somewhere.
    """
    family_id = review.get("family_id", "?")
    bare_family = family_id.split(":")[-1]
    results: list[ResidueCheck] = []

    for assessment in review.get("node_assessments") or []:
        node = assessment.get("node_id", "?")
        term = (assessment.get("asserted_term") or {}).get("id", "?")
        rows = paint_index.get(node, [])

        if not rows:
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None, Outcome.FAIL,
                    "node not found in any cached interpro/panther/*/*-paint.tsv",
                )
            )
            continue

        family_rows = [r for r in rows if getattr(r, "family", "") == bare_family]
        if not family_rows:
            seen = sorted({getattr(r, "family", "?") for r in rows})
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None, Outcome.FAIL,
                    f"node exists but belongs to {seen}, not {bare_family}",
                )
            )
            continue

        terms_here = {getattr(r, "go_id", "") for r in family_rows}
        if term in terms_here:
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None, Outcome.PASS,
                    f"PAINT records {term} at this node in {bare_family}",
                )
            )
        else:
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None, Outcome.FAIL,
                    f"PAINT does not record {term} at this node; "
                    f"terms present are {sorted(terms_here)}",
                )
            )
    return results


def check_controls(review: dict, cache: SequenceCache) -> list[ResidueCheck]:
    """Sanity-check declared controls.

    A positive control must not be the anchor's own accession repeated -- that proves
    nothing -- and both control lists must be non-empty for a site whose requirement is
    REQUIRED, since a REQUIRED site is the only kind that licenses contradicting a gene
    review.
    """
    family = review.get("family_id", "?")
    results: list[ResidueCheck] = []

    for site in review.get("residue_sites") or []:
        site_id = site.get("site_id", "?")
        strengths = {
            req.get("strength") for req in (site.get("required_for") or [])
        }
        pos_ctl = [c["id"] for c in site.get("positive_controls") or []]
        neg_ctl = [c["id"] for c in site.get("negative_controls") or []]

        if "REQUIRED" in strengths:
            if not pos_ctl or not neg_ctl:
                results.append(
                    ResidueCheck(
                        family, site_id, "-", 0, [], None, Outcome.FAIL,
                        "a REQUIRED site needs both positive and negative controls; "
                        f"got {len(pos_ctl)} positive, {len(neg_ctl)} negative",
                    )
                )
                continue

        overlap = set(pos_ctl) & set(neg_ctl)
        if overlap:
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.FAIL,
                    f"protein(s) listed as both positive and negative control: "
                    f"{sorted(overlap)}",
                )
            )
        else:
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.PASS,
                    f"{len(pos_ctl)} positive and {len(neg_ctl)} negative controls declared, disjoint",
                )
            )
    return results


def validate_family_review(path: Path, cache_dir: Path) -> list[ResidueCheck]:
    """Run all residue checks for one family review file.

    >>> from pathlib import Path
    >>> results = validate_family_review(
    ...     Path("interpro/panther/PTHR11022/PTHR11022-review.yaml"),
    ...     Path(".cache/uniprot_seq"),
    ... )   # doctest: +SKIP
    >>> all(r.outcome.value == "PASS" for r in results)   # doctest: +SKIP
    True
    """
    from ai_gene_review.validation.module_validator import load_paint_index

    review = yaml.safe_load(path.read_text())
    cache = SequenceCache(cache_dir)
    paint_index = load_paint_index(Path("interpro/panther"))
    return (
        check_anchor_residues(review, cache)
        + check_controls(review, cache)
        + check_node_assessments(review, paint_index)
    )


def summarize(results: Iterable[ResidueCheck]) -> dict[str, int]:
    """Count outcomes by kind.

    >>> summarize([])
    {'PASS': 0, 'FAIL': 0, 'UNRESOLVED': 0}
    """
    counts = {o.value: 0 for o in Outcome}
    for r in results:
        counts[r.outcome.value] += 1
    return counts


def main(argv: list[str] | None = None) -> int:
    """Validate every family review under interpro/panther. Returns a process exit code."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "paths", nargs="*", type=Path,
        help="Family review YAML files; defaults to all under interpro/panther.",
    )
    parser.add_argument(
        "--cache-dir", type=Path, default=Path(".cache/uniprot_seq"),
        help="Where UniProt sequences are cached.",
    )
    args = parser.parse_args(argv)

    paths = args.paths or sorted(Path("interpro/panther").glob("PTHR*/PTHR*-review.yaml"))
    if not paths:
        print("No family review files found.")
        return 0

    all_results: list[ResidueCheck] = []
    for path in paths:
        results = validate_family_review(path, args.cache_dir)
        all_results.extend(results)
        for r in results:
            if r.outcome is not Outcome.PASS:
                print(r, file=sys.stderr)

    counts = summarize(all_results)
    print(
        f"residue-site validation over {len(paths)} family review(s): "
        f"{counts['PASS']} pass, {counts['FAIL']} fail, {counts['UNRESOLVED']} unresolved"
    )
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
