"""Deterministic validation of gene-level residue claims.

``review.propagation_review.residue_claims`` records, in checkable form, the argument that
a protein has lost (or kept) a functionally important residue. This module resolves those
claims against real sequences and against the curated family-level site they cite.

The claim is deliberately over-specified: it states the anchor's position *and* residue and
the target's position *and* residue. That redundancy is what lets most of it be checked
without an alignment -- each side is resolved directly against its own sequence -- and it
means a wrong claim is contradicted by data rather than merely unsupported.

Four checks:

``check_anchor``
    The anchor protein really has that residue at that position.
``check_target``
    This gene's protein really has that residue at that position. Also confirms the
    claimed accession matches the gene review's own ``id``, so a claim cannot quietly be
    about a different protein.
``check_internal_consistency``
    ``LOST`` requires the target residue to differ from the anchor's, ``RETAINED`` requires
    it to match. This is the check that would have caught the four intact-site claims found
    in this repo (CASP12, LPA, AZIN1, HSPA13): each asserted loss while the residue was
    still there.
``check_site_ref``
    When the claim cites a family-level site, the site must exist in that family review and
    the anchor position must be one the site actually declares. This is what stops a gene
    review and a family review drifting apart silently.

Enforcement is forward-only by construction: ``residue_claims`` is optional, so the 900-odd
existing reviews that make residue arguments in prose remain valid and are never
retroactively invalidated.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import yaml
from yaml import CSafeLoader as _Loader

from ai_gene_review.validation.family_residue_validator import SequenceCache


class ClaimOutcome(str, Enum):
    """Result of one residue-claim check."""

    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"


@dataclass
class ClaimCheck:
    """One check applied to one residue claim."""

    kind: str
    gene: str
    term: str
    detail: str
    outcome: ClaimOutcome

    def __str__(self) -> str:
        return f"[{self.outcome.value}] {self.kind} {self.gene} {self.term}: {self.detail}"


def _residue_at(seq: str, position: int) -> str | None:
    return seq[position - 1] if 1 <= position <= len(seq) else None


def _version_note(cache: SequenceCache, spec: dict, acc: str) -> str:
    """Describe sequence-version drift, if the claim pinned one and it has moved.

    Kept separate from the residue comparison so the two signals do not get confused.
    A drifted version with a still-correct residue is fine; a drifted version with a
    wrong residue usually *explains* the wrong residue, and saying so turns a bare
    contradiction into an actionable one.
    """
    claimed_v = spec.get("sequence_version")
    if claimed_v is None:
        return ""
    current_v = cache.sequence_version(acc)
    if current_v is None or current_v == claimed_v:
        return ""
    return f" [sequence version has moved {claimed_v} -> {current_v} since this claim]"


def _check_position(
    cache: SequenceCache, spec: dict, label: str, gene: str, term: str, kind: str
) -> tuple[ClaimCheck, str | None]:
    """Resolve one ResiduePosition; return the check and the observed residue."""
    acc = spec["accession"]
    pos = spec["position"]
    claimed = spec["residue"]
    seq = cache.get(acc)
    drift = _version_note(cache, spec, acc)
    observed = _residue_at(seq, pos)
    if observed is None:
        return (
            ClaimCheck(
                kind, gene, term,
                f"{label} {acc}:{pos} is beyond the end of a "
                f"{len(seq)}-residue sequence{drift}",
                ClaimOutcome.FAIL,
            ),
            None,
        )
    if observed != claimed:
        return (
            ClaimCheck(
                kind, gene, term,
                f"{label} {acc}:{pos} claimed {claimed} but the sequence "
                f"has {observed}{drift}",
                ClaimOutcome.FAIL,
            ),
            observed,
        )
    return (
        ClaimCheck(kind, gene, term,
                   f"{label} {acc}:{pos} is {observed} as claimed{drift}",
                   ClaimOutcome.PASS),
        observed,
    )


def check_claim(
    claim: dict,
    gene_accession: str,
    gene: str,
    term: str,
    cache: SequenceCache,
    family_sites: dict[str, set[int]] | None = None,
) -> list[ClaimCheck]:
    """Run every check for a single residue claim."""
    results: list[ClaimCheck] = []
    anchor = claim.get("anchor") or {}
    target = claim.get("target")
    claim_type = claim.get("claim_type", "?")

    anchor_check, anchor_res = _check_position(
        cache, anchor, "anchor", gene, term, "ANCHOR"
    )
    results.append(anchor_check)

    target_res = None
    if target:
        # the claim must be about this gene's own protein
        claimed_acc = target["accession"].split(":")[-1]
        if claimed_acc != gene_accession.split(":")[-1]:
            results.append(
                ClaimCheck(
                    "TARGET_IDENTITY", gene, term,
                    f"target accession {target['accession']} is not this gene "
                    f"({gene_accession})",
                    ClaimOutcome.FAIL,
                )
            )
        target_check, target_res = _check_position(
            cache, target, "target", gene, term, "TARGET"
        )
        results.append(target_check)
    else:
        results.append(
            ClaimCheck(
                "TARGET", gene, term,
                "no target position given; the claim cannot be fully resolved",
                ClaimOutcome.UNRESOLVED,
            )
        )

    # internal consistency between the claim type and the observed residues
    if anchor_res and target_res:
        same = anchor_res == target_res
        if claim_type == "LOST" and same:
            results.append(
                ClaimCheck(
                    "CLAIM_CONSISTENCY", gene, term,
                    f"claim is LOST but the target carries the same residue "
                    f"({target_res}) as the anchor -- the site is intact",
                    ClaimOutcome.FAIL,
                )
            )
        elif claim_type == "RETAINED" and not same:
            results.append(
                ClaimCheck(
                    "CLAIM_CONSISTENCY", gene, term,
                    f"claim is RETAINED but the target has {target_res} where the "
                    f"anchor has {anchor_res}",
                    ClaimOutcome.FAIL,
                )
            )
        else:
            results.append(
                ClaimCheck(
                    "CLAIM_CONSISTENCY", gene, term,
                    f"{claim_type} is consistent with anchor {anchor_res} / "
                    f"target {target_res}",
                    ClaimOutcome.PASS,
                )
            )

    site_ref = claim.get("site_ref")
    if site_ref:
        if family_sites is None:
            results.append(
                ClaimCheck("SITE_REF", gene, term,
                           f"{site_ref} not checked (no family reviews loaded)",
                           ClaimOutcome.UNRESOLVED))
        elif site_ref not in family_sites:
            results.append(
                ClaimCheck("SITE_REF", gene, term,
                           f"{site_ref} does not resolve to a curated family residue site",
                           ClaimOutcome.FAIL))
        elif anchor.get("position") not in family_sites[site_ref]:
            results.append(
                ClaimCheck(
                    "SITE_REF", gene, term,
                    f"anchor position {anchor.get('position')} is not one of the "
                    f"positions {sorted(family_sites[site_ref])} declared by {site_ref}",
                    ClaimOutcome.FAIL,
                )
            )
        else:
            results.append(
                ClaimCheck("SITE_REF", gene, term,
                           f"anchor position matches site {site_ref}", ClaimOutcome.PASS))
    return results


def load_family_sites(panther_dir: Path) -> dict[str, set[int]]:
    """Map ``<family_id>#<site_id>`` -> the anchor positions that site covers.

    A site defined by a ``motif`` rather than by individual residues covers the whole
    declared block, so its span is expanded here. Without that a motif-only site would
    yield an empty position set and every gene claim citing it would fail -- a site
    that exists but can never be cited.
    """
    sites: dict[str, set[int]] = {}
    for path in sorted(panther_dir.glob("PTHR*/PTHR*-review.yaml")):
        review = yaml.load(path.read_text(), Loader=_Loader)
        family = (review or {}).get("family_id")
        if not family:
            continue
        for site in review.get("residue_sites") or []:
            key = f"{family}#{site.get('site_id')}"
            positions = {
                r["position"] for r in (site.get("residues") or []) if "position" in r
            }
            motif = site.get("motif")
            if motif and "start" in motif and "end" in motif:
                positions |= set(range(motif["start"], motif["end"] + 1))
            sites[key] = positions
    return sites


def validate_gene_residue_claims(
    path: Path, cache: SequenceCache, family_sites: dict[str, set[int]] | None = None
) -> list[ClaimCheck]:
    """Validate every residue claim in one gene review."""
    doc = yaml.load(path.read_text(), Loader=_Loader)
    gene = (doc or {}).get("gene_symbol") or path.stem
    accession = (doc or {}).get("id", "")
    results: list[ClaimCheck] = []
    for ann in (doc or {}).get("existing_annotations") or []:
        pr = (ann.get("review") or {}).get("propagation_review") or {}
        term = (ann.get("term") or {}).get("id", "?")
        for claim in pr.get("residue_claims") or []:
            results.extend(
                check_claim(claim, accession, gene, term, cache, family_sites)
            )
    return results


def main(argv: list[str] | None = None) -> int:
    """Validate residue claims across the gene corpus."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Validate gene residue claims.")
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--genes-dir", type=Path, default=Path("genes"))
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache/uniprot_seq"))
    args = parser.parse_args(argv)

    paths = args.paths or sorted(args.genes_dir.glob("*/*/*-ai-review.yaml"))
    cache = SequenceCache(args.cache_dir)
    family_sites = load_family_sites(Path("interpro/panther"))

    counts = {o.value: 0 for o in ClaimOutcome}
    genes_with_claims = 0
    for path in paths:
        text = path.read_text()
        if "residue_claims" not in text:      # cheap skip; most reviews have none
            continue
        results = validate_gene_residue_claims(path, cache, family_sites)
        if results:
            genes_with_claims += 1
        for r in results:
            counts[r.outcome.value] += 1
            if r.outcome is not ClaimOutcome.PASS:
                print(r, file=sys.stderr)

    print(
        f"residue-claim validation over {genes_with_claims} gene review(s) with claims: "
        f"{counts['PASS']} pass, {counts['FAIL']} fail, {counts['UNRESOLVED']} unresolved"
    )
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
