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

import http.client
import json
import ssl
import time
import urllib.error
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


def _retryable_uniprot_error(exc: Exception) -> bool:
    """Limit retries to transient HTTP and network/read failures."""
    if isinstance(exc, urllib.error.HTTPError):
        return exc.code in {408, 429, 500, 502, 503, 504}
    if isinstance(exc, urllib.error.URLError):
        # Certificate/configuration errors will not improve after a short wait.
        return not isinstance(exc.reason, (ssl.SSLError, PermissionError))
    return isinstance(exc, (TimeoutError, ConnectionError, http.client.IncompleteRead))


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


class InactiveEntryError(LookupError):
    """Raised when UniProtKB returns an inactive (deleted/merged/demerged) entry.

    Such a record carries no sequence. This is a property of the cited accession, not a
    retrieval failure, so callers report it as a FAIL on the claim that cites it rather
    than letting one stale accession stop validation of every other family.
    """

    def __init__(self, accession: str, data: dict) -> None:
        self.accession = accession
        reason = data.get("inactiveReason") or {}
        self.reason_type = reason.get("inactiveReasonType") or data.get("entryType") or "INACTIVE"
        self.detail = reason.get("deletedReason") or ""
        self.merged_into = list(reason.get("mergeDemergeTo") or [])
        super().__init__(self.describe())

    def describe(self) -> str:
        """Human-readable explanation, for use in a check message.

        >>> InactiveEntryError("C0H4F3", {"entryType": "Inactive", "inactiveReason": {
        ...     "inactiveReasonType": "DELETED",
        ...     "deletedReason": "Deleted from sequence source (ENSEMBL)"}}).describe()
        'accession C0H4F3 is inactive in UniProtKB (DELETED: Deleted from sequence source (ENSEMBL))'
        >>> InactiveEntryError("P1", {"entryType": "Inactive", "inactiveReason": {
        ...     "inactiveReasonType": "MERGED", "mergeDemergeTo": ["P2"]}}).describe()
        'accession P1 is inactive in UniProtKB (MERGED; now P2)'
        """
        msg = f"accession {self.accession} is inactive in UniProtKB ({self.reason_type}"
        if self.detail:
            msg += f": {self.detail}"
        if self.merged_into:
            msg += f"; now {', '.join(self.merged_into)}"
        return msg + ")"


@dataclass
class SequenceCache:
    """Fetches and caches UniProt sequences.

    Sequences are cached on disk so repeated runs do not refetch. ``.cache`` is
    gitignored, so in CI the cache is restored by an ``actions/cache`` step rather than
    coming from the checkout -- on a cold key the first run still resolves every
    sequence over the network.

    Retrieval failures retain accession/URL context and propagate with their cause;
    they are never converted into UNRESOLVED curation results.
    """

    cache_dir: Path
    _mem: dict[str, str] = field(default_factory=dict)
    _versions: dict[str, int] = field(default_factory=dict)
    _inactive: dict[str, InactiveEntryError] = field(default_factory=dict)

    def _fetch_json(self, acc: str) -> dict:
        req = urllib.request.Request(
            UNIPROT_JSON.format(acc=acc), headers={"User-Agent": "ai-gene-review"}
        )
        # Three total attempts, with only 2s and 4s waits. A successful record
        # still passes through the same validation and persistent cache paths.
        attempts = 3
        for attempt in range(1, attempts + 1):
            try:
                with urllib.request.urlopen(req, timeout=60) as fh:
                    return json.load(fh)
            except (OSError, json.JSONDecodeError, http.client.HTTPException) as exc:
                if attempt == attempts or not _retryable_uniprot_error(exc):
                    # Keep the final HTTPError body available through __cause__;
                    # only responses discarded before another attempt are closed.
                    raise RuntimeError(
                        f"Could not retrieve UniProt record {acc} from {req.full_url}"
                    ) from exc
                if isinstance(exc, urllib.error.HTTPError):
                    # urlopen raised before entering the response context manager.
                    exc.close()
                time.sleep(2 ** attempt)
        raise AssertionError("unreachable")

    def _record_sequence(self, acc: str, data: object) -> str:
        """Validate a response before caching or classifying a cited accession.

        Only explicit inactive metadata denotes an inactive accession. Other
        sequence-less or malformed responses remain contextual hard errors.
        """
        entry_type = data.get("entryType") if isinstance(data, dict) else None
        try:
            if not isinstance(data, dict):
                raise TypeError("expected a JSON object")
            reason = data.get("inactiveReason")
            if reason is not None and not isinstance(reason, dict):
                raise TypeError("inactiveReason must be an object")
            reason_type = (reason or {}).get("inactiveReasonType")
            if entry_type == "Inactive" or (
                isinstance(reason_type, str) and bool(reason_type.strip())
            ):
                # Memory only: a later run must be able to observe reactivation.
                err = InactiveEntryError(acc, data)
                self._inactive[acc] = err
                raise err
            seq = data["sequence"]["value"]
            if not isinstance(seq, str) or not (
                seq and seq.isascii() and seq.isalpha() and seq.isupper()
            ):
                raise ValueError("sequence.value must be nonempty uppercase letters")
        except (KeyError, TypeError, ValueError) as exc:
            raise RuntimeError(
                f"UniProt record {acc} from {UNIPROT_JSON.format(acc=acc)} "
                f"has an invalid sequence payload (entryType={entry_type!r})"
            ) from exc
        return seq

    def get(self, accession: str) -> str:
        """Return the amino-acid sequence for a UniProt accession.

        A cached sequence is used even when no version file sits beside it: an older
        cache entry is still a valid sequence, and requiring both would force a refetch
        of everything the first time versions were introduced.
        """
        acc = accession.split(":")[-1]
        if acc in self._inactive:
            raise self._inactive[acc]
        if acc in self._mem:
            return self._mem[acc]
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        seq_path = self.cache_dir / f"{acc}.seq"
        if seq_path.exists():
            seq = seq_path.read_text().strip()
        else:
            data = self._fetch_json(acc)
            seq = self._record_sequence(acc, data)
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
        if acc in self._inactive:
            raise self._inactive[acc]
        if acc in self._versions:
            return self._versions[acc]
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        ver_path = self.cache_dir / f"{acc}.sv"
        if ver_path.exists():
            version = int(ver_path.read_text().strip())
        else:
            data = self._fetch_json(acc)
            self._record_sequence(acc, data)
            version = data.get("entryAudit", {}).get("sequenceVersion")
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

        try:
            seq = cache.get(anchor)
            pinned = site.get("anchor_sequence_version")
            current = cache.sequence_version(anchor) if pinned is not None else None
        except InactiveEntryError as exc:
            results.append(
                ResidueCheck(
                    family, site_id, anchor, 0, [], None, Outcome.FAIL,
                    f"{exc.describe()}; choose a live anchor protein",
                    kind="ANCHOR_RESIDUE",
                )
            )
            continue
        drift = ""
        if pinned is not None:
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
) -> "tuple[dict[str, str], dict[str, str], MemberIndexGaps, dict[str, str]]":
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
        load_member_index_alternates,
        load_member_index_gaps,
        load_obo_names,
        member_index_path,
    )

    # panther_dir is <repo>/interpro/panther; the member index is a build
    # artifact in <repo>/.cache/panther.
    members = member_index_path(Path(panther_dir).parents[1])
    return (
        load_obo_names(panther_dir / "panther.obo"),
        load_member_index(members),
        load_member_index_gaps(members),
        load_member_index_alternates(members),
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
    alternates: "dict[str, str] | None" = None,
) -> list[ResidueCheck]:
    """Check every PANTHER family/subfamily id resolves, and that labels are verbatim.

    CLAUDE.md's rule applies with full force here: a plausible-sounding label is exactly
    how a wrong family id stays hidden, because the id is real and nothing else catches
    it. So the label must equal PANTHER's official name character for character.

    PTN node ids are skipped -- they are not in panther.obo and are checked separately
    against PAINT.

    Membership is checked where the PANTHER member index covers the protein. Coverage is
    partial (it indexes cited proteins), so an absent accession is UNRESOLVED rather than
    a failure, matching the convention documented in CLAUDE.md. Where PANTHER's
    classification files and UniProt disagree (``alternates``), a member matching
    either is accepted, and the disagreement is reported as UNRESOLVED.
    """
    alternates = alternates or {}
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
            elif members[acc] != bare and alternates.get(acc) == bare:
                results.append(
                    ResidueCheck(
                        family, declared, acc, 0, [], None, Outcome.UNRESOLVED,
                        f"sources disagree: PANTHER's classification files put it in "
                        f"{members[acc]}, UniProt's cross-reference in the declared "
                        f"{bare}; both are accepted",
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


GAIN_VERDICTS = frozenset({"SOUND", "TOO_DEEP", "WRONG_NODE", "NEEDS_PRUNING"})
LOSS_VERDICTS = frozenset({"LOSS_SUPPORTED", "LOSS_CONTRADICTED", "LOSS_TOO_BROAD", "LOSS_STALE"})


def node_polarity_problem(assessment: dict, term_rows: list) -> str | None:
    """Return why a node assessment's evidence/negation/verdict disagree with PAINT, or None.

    ``term_rows`` are the family's PAINT rows for this node and term. A PAINT loss (IRD,
    IKR or a rare NOT|IBD) must be declared ``negated: true`` with its evidence code and
    judged with a LOSS_* verdict; a gain must not be. Without this an IRD can be assessed
    as though it were an IBD, and a "WRONG_NODE" on a loss reads, to the family/gene
    cross-check, as the opposite of what the reviewer meant.

    >>> class Row:
    ...     def __init__(self, evidence, negated):
    ...         self.evidence, self.negated = evidence, negated
    >>> ird = [Row("IRD", True)]
    >>> node_polarity_problem({"assessment": "LOSS_SUPPORTED", "negated": True,
    ...                        "evidence": "IRD"}, ird) is None
    True
    >>> node_polarity_problem({"assessment": "WRONG_NODE"}, ird)
    'PAINT records this as a loss (IRD); declare negated: true and evidence: IRD'
    >>> node_polarity_problem({"assessment": "SOUND", "negated": True, "evidence": "IRD"}, ird)
    "verdict SOUND is for gain rows; a loss row needs one of ['LOSS_CONTRADICTED', 'LOSS_STALE', 'LOSS_SUPPORTED', 'LOSS_TOO_BROAD'] or UNRESOLVED"
    >>> node_polarity_problem({"assessment": "SOUND"}, [Row("IBD", False)]) is None
    True
    >>> node_polarity_problem({"assessment": "SOUND", "evidence": "IKR"}, [Row("IBD", False)])
    "declared evidence IKR, but PAINT records ['IBD'] for this node and term"
    """
    paint_negated = {bool(getattr(r, "negated", False)) for r in term_rows}
    paint_evidence = sorted({getattr(r, "evidence", "") for r in term_rows} - {""})
    declared_negated = bool(assessment.get("negated", False))
    declared_evidence = assessment.get("evidence")
    verdict = assessment.get("assessment", "")

    if declared_evidence and paint_evidence and declared_evidence not in paint_evidence:
        return (
            f"declared evidence {declared_evidence}, but PAINT records {paint_evidence} "
            "for this node and term"
        )
    if True in paint_negated and False not in paint_negated:
        if not declared_negated or not declared_evidence:
            ev = "/".join(paint_evidence) or "IRD/IKR"
            return f"PAINT records this as a loss ({ev}); declare negated: true and evidence: {ev}"
    elif declared_negated and paint_negated == {False}:
        return "declared negated: true, but PAINT records a gain (not a NOT) here"
    if declared_negated and verdict in GAIN_VERDICTS:
        return (
            f"verdict {verdict} is for gain rows; a loss row needs one of "
            f"{sorted(LOSS_VERDICTS)} or UNRESOLVED"
        )
    if not declared_negated and verdict in LOSS_VERDICTS:
        return f"verdict {verdict} is for loss rows; declare negated: true and evidence"
    return None


#: PAINT actions a node verdict may request, and whether each needs a target node.
#: Verdicts absent from this map (SOUND, LOSS_SUPPORTED, UNRESOLVED) take no action.
ALLOWED_PAINT_ACTIONS: dict[str, frozenset[str]] = {
    "TOO_DEEP": frozenset({"MOVE_IBD", "REMOVE_IBD"}),
    "WRONG_NODE": frozenset({"MOVE_IBD", "REMOVE_IBD"}),
    "NEEDS_PRUNING": frozenset({"ADD_IRD", "ADD_IKR"}),
    "LOSS_CONTRADICTED": frozenset({"REMOVE_LOSS"}),
    "LOSS_STALE": frozenset({"REMOVE_LOSS"}),
    "LOSS_TOO_BROAD": frozenset({"MOVE_LOSS"}),
}
TARGETED_PAINT_ACTIONS = frozenset({"MOVE_IBD", "MOVE_LOSS", "ADD_IRD", "ADD_IKR"})
#: Verdicts whose target must lie strictly below the assessed node. WRONG_NODE is absent:
#: a wrongly placed IBD may belong anywhere in the family.
DESCENDANT_TARGET_VERDICTS = frozenset({"TOO_DEEP", "NEEDS_PRUNING", "LOSS_TOO_BROAD"})


def _proposed_action_fit_problem(assessment: dict) -> str | None:
    """Check the verdict/action pairing and target presence, without the tree.

    >>> _proposed_action_fit_problem({"assessment": "SOUND",
    ...     "proposed_action": {"paint_action": "REMOVE_IBD"}})
    'verdict SOUND takes no proposed action'
    >>> _proposed_action_fit_problem({"assessment": "TOO_DEEP",
    ...     "proposed_action": {"paint_action": "REMOVE_IBD"}}) is None
    True
    """
    verdict = assessment.get("assessment", "")
    proposal = assessment.get("proposed_action") or {}
    action = proposal.get("paint_action", "")
    target = proposal.get("target_node_id")
    allowed = ALLOWED_PAINT_ACTIONS.get(verdict)
    if allowed is None:
        return f"verdict {verdict} takes no proposed action"
    if action not in allowed:
        return f"{action} is not allowed for verdict {verdict}; use one of {sorted(allowed)}"
    if action in TARGETED_PAINT_ACTIONS and not target:
        return f"{action} needs a target_node_id"
    if action not in TARGETED_PAINT_ACTIONS and target:
        return f"{action} acts on the assessed node and takes no target_node_id"
    return None


def proposed_action_problem(assessment: dict, under: dict[str, list[str]]) -> str | None:
    """Return why a node assessment's ``proposed_action`` is invalid, or None.

    ``under`` maps each internal PANTHER node of the family to the leaves below it (the
    ``under`` table of ``ai_gene_review.etl.panther_trees``). The action must fit the
    verdict (see ``ALLOWED_PAINT_ACTIONS``); a targeted action's node must be an internal
    node of the family other than the assessed one, and for TOO_DEEP, NEEDS_PRUNING and
    LOSS_TOO_BROAD it must lie strictly below the assessed node.

    >>> tree = {"PTN1": ["a", "b", "c"], "PTN2": ["a", "b"]}
    >>> proposed_action_problem({"node_id": "PANTHER:PTN1", "assessment": "TOO_DEEP",
    ...     "proposed_action": {"paint_action": "MOVE_IBD",
    ...                         "target_node_id": "PANTHER:PTN2"}}, tree) is None
    True
    >>> proposed_action_problem({"node_id": "PANTHER:PTN2", "assessment": "NEEDS_PRUNING",
    ...     "proposed_action": {"paint_action": "ADD_IKR",
    ...                         "target_node_id": "PANTHER:PTN1"}}, tree)
    'target PTN1 is not below the assessed node PTN2'
    """
    fit = _proposed_action_fit_problem(assessment)
    if fit:
        return fit
    proposal = assessment["proposed_action"]
    target = (proposal.get("target_node_id") or "").split(":")[-1]
    if not target:
        return None
    node = (assessment.get("node_id") or "").split(":")[-1]
    if target == node:
        return f"target {target} is the assessed node itself"
    if target not in under:
        return f"target {target} is not an internal node of this family's PANTHER tree"
    if assessment.get("assessment") in DESCENDANT_TARGET_VERDICTS:
        node_leaves = set(under.get(node, []))
        if not node_leaves:
            return f"assessed node {node} is not an internal node of this family's tree"
        if not set(under[target]) < node_leaves:
            return f"target {target} is not below the assessed node {node}"
    return None


def check_proposed_actions(review: dict, tree_loader) -> list[ResidueCheck]:
    """Check every node assessment's ``proposed_action`` against its verdict and the tree.

    ``tree_loader(family)`` returns the compact PANTHER tree (``{"under": ...}``) for a bare
    family id such as ``PTHR24416``, or None when it cannot be fetched. It is called at
    most once, and only when the review proposes an action. Without a tree the
    verdict/action pairing is still enforced, and the tree relation is UNRESOLVED.
    """
    family_id = review.get("family_id", "?")
    proposals = [a for a in review.get("node_assessments") or [] if a.get("proposed_action")]
    if not proposals:
        return []
    tree = tree_loader(family_id.split(":")[-1])
    under = (tree or {}).get("under")
    results: list[ResidueCheck] = []
    for assessment in proposals:
        node = assessment.get("node_id", "?")
        term = (assessment.get("asserted_term") or {}).get("id", "?")
        action = assessment["proposed_action"].get("paint_action", "?")
        if under is None:
            problem = _proposed_action_fit_problem(assessment)
            outcome = Outcome.FAIL if problem else Outcome.UNRESOLVED
            message = problem or (
                f"{action} fits the verdict; target not checked: PANTHER tree unavailable"
            )
        else:
            problem = proposed_action_problem(assessment, under)
            outcome = Outcome.FAIL if problem else Outcome.PASS
            message = problem or f"{action} fits the verdict and the PANTHER tree"
        results.append(
            ResidueCheck(family_id, node, term, 0, [], None, outcome, message,
                         kind="NODE_PROPOSED_ACTION")
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
            term_rows = [r for r in family_rows if getattr(r, "go_id", "") == term]
            problem = node_polarity_problem(assessment, term_rows)
            results.append(
                ResidueCheck(
                    family_id, node, term, 0, [], None,
                    Outcome.FAIL if problem else Outcome.PASS,
                    problem or "evidence, negation and verdict agree with PAINT",
                    kind="NODE_POLARITY",
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
    try:
        seq = cache.get(acc)
    except InactiveEntryError as exc:
        return ResidueCheck(
            family, site_id, acc, pos, sorted(expected), None, Outcome.FAIL,
            f"{kind} control {exc.describe()}; replace or drop this control",
            kind="CONTROL_RESIDUE",
        )
    observed = _residue_at(seq, pos)
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
    from ai_gene_review.etl.panther_trees import load_family
    from ai_gene_review.validation.module_validator import load_paint_index

    review = yaml.safe_load(path.read_text())
    cache = SequenceCache(cache_dir)
    paint_index = load_paint_index(panther_dir)
    labels, members, gaps, alternates = _panther_index(panther_dir)
    return (
        check_anchor_residues(review, cache)
        + check_controls(review, cache)
        + check_node_assessments(review, paint_index)
        + check_proposed_actions(review, load_family)
        + check_term_assessment_site_refs(review)
        + check_panther_ids(review, labels, members, gaps, alternates)
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
