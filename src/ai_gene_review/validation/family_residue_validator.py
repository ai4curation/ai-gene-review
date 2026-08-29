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
    real amidase then appeared to have lost the site. Each control states the position in
    its own numbering, so no alignment is needed; a control that states none is reported
    UNRESOLVED rather than silently accepted.

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
from functools import lru_cache
from typing import TYPE_CHECKING, NamedTuple
from enum import Enum
from pathlib import Path
from typing import Iterable

import yaml

if TYPE_CHECKING:  # annotation only; the runtime import lives in _panther_index
    from ai_gene_review.etl.panther_families import MemberIndexGaps

UNIPROT_JSON = "https://rest.uniprot.org/uniprotkb/{acc}.json"


class Outcome(str, Enum):
    """Result of a single residue check."""

    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"


@dataclass
class ResidueCheck:
    """One curated position, checked against the anchor sequence.

    ``kind`` names the check that produced this result, so results can be grouped by
    check rather than by the data they happened to touch. Without it there is no way
    to ask "has this check ever failed?", which is the question that catches an
    assertion that cannot fail.
    """

    family: str
    site_id: str
    accession: str
    position: int
    expected: list[str]
    observed: str | None
    outcome: Outcome
    message: str
    kind: str = "RESIDUE"

    def __str__(self) -> str:
        return (
            f"[{self.outcome.value}] {self.kind} {self.family}#{self.site_id} "
            f"{self.accession}:{self.position} {self.message}"
        )


@dataclass
class SequenceCache:
    """Fetches and caches UniProt sequences.

    Sequences are cached on disk so repeated runs do not refetch. ``.cache`` is
    gitignored, so in CI the cache is restored by an ``actions/cache`` step rather than
    coming from the checkout -- on a cold key the first run still resolves every
    sequence over the network.

    No try/except around the fetch: a network failure should surface, not be silently
    converted into an UNRESOLVED result that looks like curation uncertainty.
    """

    cache_dir: Path
    _mem: dict[str, str] = field(default_factory=dict)
    _versions: dict[str, int] = field(default_factory=dict)

    def _fetch_json(self, acc: str) -> dict:
        req = urllib.request.Request(
            UNIPROT_JSON.format(acc=acc), headers={"User-Agent": "ai-gene-review"}
        )
        with urllib.request.urlopen(req, timeout=60) as fh:
            return json.load(fh)

    def get(self, accession: str) -> str:
        """Return the amino-acid sequence for a UniProt accession.

        A cached sequence is used even when no version file sits beside it: an older
        cache entry is still a valid sequence, and requiring both would force a refetch
        of everything the first time versions were introduced.
        """
        acc = accession.split(":")[-1]
        if acc in self._mem:
            return self._mem[acc]
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        seq_path = self.cache_dir / f"{acc}.seq"
        if seq_path.exists():
            seq = seq_path.read_text().strip()
        else:
            data = self._fetch_json(acc)
            seq = data["sequence"]["value"]
            seq_path.write_text(seq)
            version = data.get("entryAudit", {}).get("sequenceVersion")
            if version is not None:
                (self.cache_dir / f"{acc}.sv").write_text(str(version))
                self._versions[acc] = version
        self._mem[acc] = seq
        return seq

    def sequence_version(self, accession: str) -> int | None:
        """Return the UniProt sequence version, fetching it only if not already known.

        Looked up lazily: only a claim that actually pinned a version asks for this, so
        an unversioned corpus costs no extra requests.
        """
        acc = accession.split(":")[-1]
        if acc in self._versions:
            return self._versions[acc]
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        ver_path = self.cache_dir / f"{acc}.sv"
        if ver_path.exists():
            version = int(ver_path.read_text().strip())
        else:
            version = self._fetch_json(acc).get("entryAudit", {}).get("sequenceVersion")
            if version is None:
                return None
            ver_path.write_text(str(version))
        self._versions[acc] = version
        return version


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
                    kind="ANCHOR_MISSING",
                )
            )
            continue

        seq = cache.get(anchor)
        pinned = site.get("anchor_sequence_version")
        drift = ""
        if pinned is not None:
            current = cache.sequence_version(anchor)
            if current is not None and current != pinned:
                drift = (
                    f" [anchor sequence version has moved {pinned} -> {current} "
                    "since this site was curated]"
                )
        for res in site.get("residues") or []:
            pos = res["position"]
            expected = list(res["expected"])
            observed = _residue_at(seq, pos)
            if observed is None:
                outcome = Outcome.FAIL
                msg = f"position beyond end of sequence (length {len(seq)}){drift}"
            elif observed in expected:
                outcome = Outcome.PASS
                msg = f"expected {'/'.join(expected)}, found {observed}{drift}"
            else:
                outcome = Outcome.FAIL
                msg = (
                    f"expected {'/'.join(expected)}, found {observed} "
                    f"-- the curated position does not carry the curated residue{drift}"
                )
            results.append(
                ResidueCheck(family, site_id, anchor, pos, expected, observed, outcome, msg, kind="ANCHOR_RESIDUE")
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
            kind="MOTIF",
        )
    block = seq[start - 1 : end]
    if re.fullmatch(pattern, block):
        return ResidueCheck(
            family, site_id, anchor, start, [pattern], block, Outcome.PASS,
            f"block {start}-{end} is {block!r}, matches /{pattern}/",
            kind="MOTIF",
        )
    return ResidueCheck(
        family, site_id, anchor, start, [pattern], block, Outcome.FAIL,
        f"block {start}-{end} is {block!r}, does not match /{pattern}/",
        kind="MOTIF",
    )


def check_term_assessment_site_refs(review: dict) -> list[ResidueCheck]:
    """A ``RESIDUE_DETERMINED`` term assessment must point at a real site in this review.

    Without this the pointer is decorative: a term could claim its applicability is
    decided by a site that does not exist, and nothing would notice.
    """
    family = review.get("family_id", "?")
    known = {
        s.get("site_id") for s in (review.get("residue_sites") or []) if s.get("site_id")
    }
    results: list[ResidueCheck] = []
    for assessment in review.get("term_assessments") or []:
        site = assessment.get("determined_by_site")
        if not site:
            continue
        term = (assessment.get("assessed_term") or {}).get("id", "?")
        if site in known:
            results.append(
                ResidueCheck(family, site, term, 0, [], None, Outcome.PASS,
                             f"determined_by_site resolves to site '{site}'", kind="TERM_SITE_REF")
            )
        else:
            results.append(
                ResidueCheck(family, site, term, 0, [], None, Outcome.FAIL,
                             f"determined_by_site '{site}' is not a residue site in this "
                             f"review; known sites are {sorted(known) or '(none)'}", kind="TERM_SITE_REF")
            )
    return results


@lru_cache(maxsize=None)
def _panther_index(
    panther_dir: Path,
) -> "tuple[dict[str, str], dict[str, str], MemberIndexGaps]":
    """Load the PANTHER artifacts once per directory.

    Reuses ``etl.panther_families`` rather than reimplementing: those loaders are
    tested, they skip the artifact's comment block deliberately rather than by luck,
    and ``load_member_index`` degrades to an empty mapping on a fresh checkout instead
    of raising. Cached because ``panther.obo`` is 13.8 MB and this runs once per family
    review file.

    The third element distinguishes an accession PANTHER genuinely has no family for
    from one whose lookup was never done -- reporting both as "run
    refresh-panther-members" would give advice that cannot work for the former.
    """
    from ai_gene_review.etl.panther_families import (
        load_member_index,
        load_member_index_gaps,
        load_obo_names,
    )

    return (
        load_obo_names(panther_dir / "panther.obo"),
        load_member_index(panther_dir / "panther-members.tsv"),
        load_member_index_gaps(panther_dir / "panther-members.tsv"),
    )


class PantherTerm(NamedTuple):
    """One PANTHER identifier found in a review, with the rule that governs it.

    ``must_be_own_subfamily`` travels with the term rather than being matched against a
    set of path strings elsewhere. A path-string set is a rename away from silently
    dropping a slot: SUBFAMILY_SLOTS previously had to spell
    ``"affected_subfamilies[]"`` exactly, and that slot's failure mode is invisible --
    ``check_pruning_conflicts`` skips genes not in the affected set, so a bad id there
    does not misfire, it quietly stops the pruning check from examining the node, and
    absent conflicts read as no conflicts.
    """

    path: str
    curie: str | None
    label: str | None
    must_be_own_subfamily: bool = False


def _iter_panther_terms(review: dict):
    """Yield a :class:`PantherTerm` for every PANTHER identifier in the review."""
    yield PantherTerm("family_id", review.get("family_id"), review.get("family_name"))
    for sub in review.get("subfamilies") or []:
        yield PantherTerm(
            "subfamilies[].subfamily_id", sub.get("subfamily_id"), sub.get("label"),
            must_be_own_subfamily=True,
        )
        if sub.get("clade_node_id"):
            yield PantherTerm(
                "subfamilies[].clade_node_id", sub["clade_node_id"], None
            )
    for node in review.get("node_assessments") or []:
        yield PantherTerm("node_assessments[].node_id", node.get("node_id"), None)
        for sf in node.get("affected_subfamilies") or []:
            yield PantherTerm(
                "node_assessments[].affected_subfamilies[]", sf.get("id"),
                sf.get("label"), must_be_own_subfamily=True,
            )
    for ta in review.get("term_assessments") or []:
        for sf in ta.get("applicable_subfamilies") or []:
            yield PantherTerm(
                "term_assessments[].applicable_subfamilies[]", sf.get("id"),
                sf.get("label"), must_be_own_subfamily=True,
            )


def check_panther_ids(
    review: dict,
    labels: dict[str, str],
    members: dict[str, str],
    gaps: "MemberIndexGaps | None" = None,
) -> list[ResidueCheck]:
    """Check every PANTHER family/subfamily id resolves, and that labels are verbatim.

    CLAUDE.md's rule applies with full force here: a plausible-sounding label is exactly
    how a wrong family id stays hidden, because the id is real and nothing else catches
    it. So the label must equal PANTHER's official name character for character.

    PTN node ids are skipped -- they are not in panther.obo and are checked separately
    against PAINT.

    Membership is checked where ``panther-members.tsv`` covers the protein. Coverage is
    partial (it indexes cited proteins), so an absent accession is UNRESOLVED rather than
    a failure, matching the convention documented in CLAUDE.md.
    """
    family = review.get("family_id", "?")
    results: list[ResidueCheck] = []

    from ai_gene_review.validation.module_validator import (
        _is_panther_subfamily,
        _panther_family_base,
    )

    own_family = _panther_family_base(family)
    if family and own_family is None:
        results.append(
            ResidueCheck(
                family, "family_id", family, 0, [], None, Outcome.UNRESOLVED,
                "family_id is not a usable PANTHER family CURIE, so subfamilies "
                "cannot be checked against it",
                kind="PANTHER_FAMILY_SCOPE",
            )
        )

    for term in _iter_panther_terms(review):
        path, curie, label = term.path, term.curie, term.label
        if not curie or curie.startswith("PANTHER:PTN"):
            continue
        # Resolution first: a non-PANTHER CURIE is not "a family, not a subfamily",
        # it is simply unresolvable, and that is the clearer message.
        if curie not in labels:
            results.append(
                ResidueCheck(
                    family, path, curie, 0, [], None, Outcome.FAIL,
                    f"{curie} does not resolve in panther.obo",
                    kind="PANTHER_ID",
                )
            )
            continue
        if term.must_be_own_subfamily:
            if not _is_panther_subfamily(curie):
                results.append(
                    ResidueCheck(
                        family, path, curie, 0, [], None, Outcome.FAIL,
                        f"{curie} is a family, not a subfamily; a family id here "
                        "matches no member's subfamily and would flag every one of "
                        "them as a scope violation",
                        kind="PANTHER_FAMILY_SCOPE",
                    )
                )
                continue
            if own_family and _panther_family_base(curie) != own_family:
                results.append(
                    ResidueCheck(
                        family, path, curie, 0, [], None, Outcome.FAIL,
                        f"{curie} belongs to a different family; this review is "
                        f"about {family}",
                        kind="PANTHER_FAMILY_SCOPE",
                    )
                )
                continue
        official = labels[curie]
        if label is not None and label != official:
            results.append(
                ResidueCheck(
                    family, path, curie, 0, [], None, Outcome.FAIL,
                    f"label {label!r} is not PANTHER's official name {official!r}; "
                    "fix the id rather than the label if they name different things",
                    kind="PANTHER_LABEL",
                )
            )
        else:
            results.append(
                ResidueCheck(
                    family, path, curie, 0, [], None, Outcome.PASS,
                    f"{curie} resolves" + (" with the official label" if label else ""),
                    kind="PANTHER_LABEL" if label else "PANTHER_ID",
                )
            )

    # every protein named under a subfamily should belong to it
    for sub in review.get("subfamilies") or []:
        declared = sub.get("subfamily_id")
        if not declared:
            continue
        bare = declared.split(":", 1)[1]
        for member in sub.get("representative_members") or []:
            acc = (member.get("id") or "").split(":")[-1]
            if acc not in members:
                if gaps is not None and acc in gaps.absent:
                    detail = (
                        "PANTHER and UniProt hold no family for it, so membership "
                        "cannot be checked and re-indexing will not help"
                    )
                elif gaps is not None and acc in gaps.unchecked:
                    detail = (
                        "UniProt was not consulted for it; rerun "
                        "`just refresh-panther-members` to resolve its status"
                    )
                else:
                    detail = "not indexed yet; run `just refresh-panther-members`"
                results.append(
                    ResidueCheck(
                        family, declared, acc, 0, [], None, Outcome.UNRESOLVED,
                        f"membership not checked: {detail}",
                        kind="PANTHER_MEMBERSHIP",
                    )
                )
            elif members[acc] != bare:
                results.append(
                    ResidueCheck(
                        family, declared, acc, 0, [], None, Outcome.FAIL,
                        f"is classified {members[acc]}, not the declared {bare}",
                        kind="PANTHER_MEMBERSHIP",
                    )
                )
            else:
                results.append(
                    ResidueCheck(
                        family, declared, acc, 0, [], None, Outcome.PASS,
                        f"is classified {members[acc]} as declared",
                        kind="PANTHER_MEMBERSHIP",
                    )
                )
    return results


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
                    kind="NODE_EXISTS",
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
                    kind="NODE_FAMILY",
                )
            )
            continue

        # seeds, when declared, must actually appear in PAINT's with-list for this
        # (node, term). A curated seed list is allowed to be a readable subset, but a
        # seed PAINT never recorded is a fabrication.
        declared = {
            s.get("id", "").split(":")[-1]
            for s in (assessment.get("seeds") or [])
            if isinstance(s, dict)
        }
        if declared:
            paint_seeds: set[str] = set()
            for r in family_rows:
                if getattr(r, "go_id", "") == term:
                    paint_seeds |= {
                        piece.split(":")[-1]
                        for piece in (getattr(r, "seeds", "") or "").split("|")
                        if piece
                    }
            unknown = declared - paint_seeds
            if unknown:
                results.append(
                    ResidueCheck(
                        family_id, node, term, 0, [], None, Outcome.FAIL,
                        f"declared seed(s) {sorted(unknown)} do not appear in PAINT's "
                        f"with-list for this node and term",
                        kind="NODE_SEEDS",
                    )
                )
            else:
                results.append(
                    ResidueCheck(
                        family_id, node, term, 0, [], None, Outcome.PASS,
                        f"all {len(declared)} declared seed(s) appear in PAINT's "
                        f"with-list of {len(paint_seeds)}",
                        kind="NODE_SEEDS",
                    )
                )

        terms_here = {getattr(r, "go_id", "") for r in family_rows}
        if term in terms_here:
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None, Outcome.PASS,
                    f"PAINT records {term} at this node in {bare_family}",
                    kind="NODE_ASSERTION",
                )
            )
        else:
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None, Outcome.FAIL,
                    f"PAINT does not record {term} at this node; "
                    f"terms present are {sorted(terms_here)}",
                    kind="NODE_ASSERTION",
                )
            )
    return results


def check_controls(review: dict, cache: SequenceCache) -> list[ResidueCheck]:
    """Validate the declared positive and negative controls.

    Controls are what make a residue site trustworthy, so this resolves them rather
    than merely counting them. An earlier PGRP analysis in this repo used Drosophila
    PGRP-LE as a "catalytic" control when it is itself non-catalytic, and every real
    amidase then appeared to have lost the site; that is the error this catches.

    Structural checks, always run:

    * a ``REQUIRED`` site needs both positive and negative controls, since only
      ``REQUIRED`` licenses contradicting a gene review;
    * no protein may be listed as both;
    * at least one positive control must be a protein other than the anchor. The
      anchor defines the positions, so asserting that the anchor has them is
      tautological and cannot corroborate anything.

    Residue checks, run per control that supplies ``control_position`` and
    ``control_residue``: the stated residue must really be there, a positive control
    must carry one of the site's expected residues, and a negative control must not.
    A control without a declared position is reported UNRESOLVED -- its assertion is
    simply unchecked, which is worth surfacing rather than silently accepting.
    """
    family = review.get("family_id", "?")
    default_anchor = (review.get("reference_protein") or {}).get("id")
    results: list[ResidueCheck] = []

    for site in review.get("residue_sites") or []:
        site_id = site.get("site_id", "?")
        anchor = (site.get("anchor") or {}).get("id") or default_anchor
        strengths = {req.get("strength") for req in (site.get("required_for") or [])}
        pos_ctl = site.get("positive_controls") or []
        neg_ctl = site.get("negative_controls") or []
        expected = {
            r for res in (site.get("residues") or []) for r in (res.get("expected") or [])
        }

        if "REQUIRED" in strengths and (not pos_ctl or not neg_ctl):
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.FAIL,
                    "a REQUIRED site needs both positive and negative controls; "
                    f"got {len(pos_ctl)} positive, {len(neg_ctl)} negative",
                    kind="CONTROL_PRESENCE",
                )
            )
            continue

        overlap = {c["id"] for c in pos_ctl} & {c["id"] for c in neg_ctl}
        if overlap:
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.FAIL,
                    f"protein(s) listed as both positive and negative control: "
                    f"{sorted(overlap)}",
                    kind="CONTROL_DISJOINT",
                )
            )

        independent = [c for c in pos_ctl if c["id"] != anchor]
        if pos_ctl and not independent:
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.FAIL,
                    "the only positive control is the anchor itself, which is "
                    "tautological; name a different protein that has the site",
                    kind="CONTROL_INDEPENDENT",
                )
            )
        elif pos_ctl:
            results.append(
                ResidueCheck(
                    family, site_id, "-", 0, [], None, Outcome.PASS,
                    f"{len(pos_ctl)} positive ({len(independent)} independent of the "
                    f"anchor) and {len(neg_ctl)} negative controls, disjoint",
                    kind="CONTROL_INDEPENDENT",
                )
            )

        for control, is_positive in [(c, True) for c in pos_ctl] + [
            (c, False) for c in neg_ctl
        ]:
            results.append(
                _check_control_residue(
                    family, site_id, control, is_positive, expected, cache
                )
            )
    return results


def _check_control_residue(  # noqa: PLR0911 - one branch per distinguishable outcome
    family: str,
    site_id: str,
    control: dict,
    is_positive: bool,
    expected: set[str],
    cache: SequenceCache,
) -> ResidueCheck:
    """Resolve one control's declared residue and check it behaves as claimed."""
    kind = "positive" if is_positive else "negative"
    acc = control["id"]
    pos = control.get("control_position")
    claimed = control.get("control_residue")
    if pos is None or claimed is None:
        return ResidueCheck(
            family, site_id, acc, 0, sorted(expected), None, Outcome.UNRESOLVED,
            f"{kind} control declares no position/residue, so its assertion is unchecked",
            kind="CONTROL_RESIDUE",
        )
    observed = _residue_at(cache.get(acc), pos)
    if observed is None:
        return ResidueCheck(
            family, site_id, acc, pos, sorted(expected), None, Outcome.FAIL,
            f"{kind} control position {pos} is beyond the end of the sequence",
            kind="CONTROL_RESIDUE",
        )
    if observed != claimed:
        return ResidueCheck(
            family, site_id, acc, pos, sorted(expected), observed, Outcome.FAIL,
            f"{kind} control claims {claimed} at {pos} but the sequence has {observed}",
            kind="CONTROL_RESIDUE",
        )
    if not expected:
        # A motif-only site declares no per-residue expectations, so *membership*
        # cannot be decided. The residue identity above is self-contained and has
        # already been checked, so only this half is undecidable -- guarding earlier
        # would let a control declare a residue the sequence does not have.
        return ResidueCheck(
            family, site_id, acc, pos, [], observed, Outcome.UNRESOLVED,
            f"{kind} control states {observed} at {pos} as claimed, but the site "
            "declares a motif rather than individual expected residues, so whether "
            "that counts as having the site cannot be decided",
            kind="CONTROL_RESIDUE",
        )
    carries = observed in expected
    if is_positive and not carries:
        return ResidueCheck(
            family, site_id, acc, pos, sorted(expected), observed, Outcome.FAIL,
            f"positive control has {observed} at {pos}, which is not one of the "
            f"site's expected residues {sorted(expected)} -- it does not have the site",
            kind="CONTROL_RESIDUE",
        )
    if not is_positive and carries:
        return ResidueCheck(
            family, site_id, acc, pos, sorted(expected), observed, Outcome.FAIL,
            f"negative control has {observed} at {pos}, which IS an expected residue "
            f"-- it has the site and cannot serve as a negative control",
            kind="CONTROL_RESIDUE",
        )
    return ResidueCheck(
        family, site_id, acc, pos, sorted(expected), observed, Outcome.PASS,
        f"{kind} control has {observed} at {pos}, as expected for a {kind} control",
        kind="CONTROL_RESIDUE",
    )


def validate_family_review(
    path: Path, cache_dir: Path, panther_dir: Path = Path("interpro/panther")
) -> list[ResidueCheck]:
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
    paint_index = load_paint_index(panther_dir)
    labels, members, gaps = _panther_index(panther_dir)
    return (
        check_anchor_residues(review, cache)
        + check_controls(review, cache)
        + check_node_assessments(review, paint_index)
        + check_term_assessment_site_refs(review)
        + check_panther_ids(review, labels, members, gaps)
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
