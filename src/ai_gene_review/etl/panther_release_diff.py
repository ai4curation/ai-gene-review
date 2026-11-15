"""Dry-run report of what a PANTHER release bump would change in this repository.

Subfamily ids are renumbered and renamed between PANTHER releases, so a bump cannot be
done by relabelling ids (see ``docs/panther_node_anchoring_plan.md``, Phase 2). This
module compares the pinned release with a target release and reports, without editing
anything:

1. every PANTHER family or subfamily id cited in the scanned files, with its status in
   the target release (unchanged, renamed, gone); and
2. every anchor that names representative members (module family descriptors and
   family-review subfamilies), with the family or subfamily those members fall into in
   each release, and a proposed id when the members agree.

The report is the input for remapping: a proposal is a suggestion for a curator, never
applied automatically, because re-pointing a family is a judgement about evolutionary
placement.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Set, Tuple

import yaml

from ai_gene_review.etl.panther_families import label_drift
from ai_gene_review.validation.module_validator import iter_family_member_uses

PANTHER_ID_RE = re.compile(r"\bPTHR\d{5}(?::SF\d+)?\b")

# Files whose PANTHER ids are claims this repo makes (not fetched metadata).
DEFAULT_SCAN_GLOBS: Tuple[str, ...] = (
    "modules/**/*.yaml",
    "interpro/panther/*/*-review.yaml",
    "rules/**/*.yaml",
)


@dataclass(frozen=True)
class IdChange:
    """How one family or subfamily id fares in the target release."""

    accession: str
    status: str  # unchanged | renamed | gone | not_in_current
    current_name: Optional[str] = None
    target_name: Optional[str] = None
    drift: Optional[str] = None  # label_drift() of a rename: cosmetic | partial | divergent


def classify_id(
    accession: str, current: Mapping[str, str], target: Mapping[str, str]
) -> IdChange:
    """Compare one bare id's name in the current and target releases.

    >>> cur = {"PTHR1:SF1": "PROTEIN SUFA", "PTHR1:SF2": "TISSUE ALPHA-L-FUCOSIDASE",
    ...        "PTHR1:SF3": "X"}
    >>> tgt = {"PTHR1:SF1": "IRON-SULFUR CLUSTER ASSEMBLY PROTEIN SUFA",
    ...        "PTHR1:SF2": "SODIUM/HYDROGEN EXCHANGER 2"}
    >>> classify_id("PTHR1:SF1", cur, tgt).drift
    'cosmetic'
    >>> classify_id("PTHR1:SF2", cur, tgt).drift
    'divergent'
    >>> classify_id("PTHR1:SF3", cur, tgt).status, classify_id("PTHR9", cur, tgt).status
    ('gone', 'not_in_current')
    """
    if accession not in current:
        return IdChange(accession, "not_in_current", target_name=target.get(accession))
    name = current[accession]
    if accession not in target:
        return IdChange(accession, "gone", current_name=name)
    if target[accession] == name:
        return IdChange(accession, "unchanged", name, name)
    return IdChange(
        accession, "renamed", name, target[accession], label_drift(name, target[accession])
    )


def cited_ids(paths: Iterable[Path], root: Path) -> Dict[str, Set[str]]:
    """Map each bare PANTHER family or subfamily id to the files (relative to ``root``) citing it.

    >>> import tempfile
    >>> d = Path(tempfile.mkdtemp())
    >>> _ = (d / "m.yaml").write_text("id: PANTHER:PTHR10024:SF344\\nalso: PTHR10024\\n")
    >>> cited_ids([d / "m.yaml"], d)
    {'PTHR10024:SF344': {'m.yaml'}, 'PTHR10024': {'m.yaml'}}
    """
    found: Dict[str, Set[str]] = {}
    for path in paths:
        for accession in PANTHER_ID_RE.findall(path.read_text(errors="replace")):
            found.setdefault(accession, set()).add(str(path.relative_to(root)))
    return found


@dataclass(frozen=True)
class Anchor:
    """A declared PANTHER id together with the proteins said to belong to it."""

    file: str
    path: str
    declared: Tuple[str, ...]  # bare ids
    members: Tuple[str, ...]  # bare UniProt accessions


def _bare(curie: str) -> str:
    return curie.split(":", 1)[1] if curie.startswith(("PANTHER:", "UniProtKB:")) else curie


def module_anchors(data: Any, file: str) -> List[Anchor]:
    """Family descriptors in a module that declare a PANTHER id and name members.

    >>> data = {"parts": [{"family": {
    ...     "term": {"id": "PANTHER:PTHR11801:SF43"},
    ...     "representative_members": [{"term": {"id": "UniProtKB:P42224"}}]}}]}
    >>> module_anchors(data, "m.yaml")[0].declared, module_anchors(data, "m.yaml")[0].members
    (('PTHR11801:SF43',), ('P42224',))
    """
    return [
        Anchor(
            file,
            use.path,
            tuple(sorted(_bare(c) for c in use.declared_family_curies)),
            tuple(sorted(use.representative_accessions)),
        )
        for use in iter_family_member_uses(data)
    ]


def family_review_anchors(data: Any, file: str) -> List[Anchor]:
    """Subfamilies in a family review that name representative members.

    >>> data = {"subfamilies": [{"subfamily_id": "PANTHER:PTHR11801:SF43",
    ...     "representative_members": [{"id": "UniProtKB:P42224"}, {"id": "PMID:1"}]}]}
    >>> family_review_anchors(data, "f.yaml")[0].members
    ('P42224',)
    """
    anchors: List[Anchor] = []
    if not isinstance(data, dict):
        return anchors
    for index, sub in enumerate(data.get("subfamilies") or []):
        if not isinstance(sub, dict) or not isinstance(sub.get("subfamily_id"), str):
            continue
        members = sorted(
            _bare(member["id"])
            for member in sub.get("representative_members") or []
            if isinstance(member, dict)
            and isinstance(member.get("id"), str)
            and member["id"].startswith("UniProtKB:")
        )
        if members:
            anchors.append(
                Anchor(file, f"$.subfamilies[{index}]", (_bare(sub["subfamily_id"]),), tuple(members))
            )
    return anchors


@dataclass(frozen=True)
class Remap:
    """Where an anchor's members fall in the target release, and what that suggests."""

    # Bump-driven: remap | split | unresolved. Pre-existing or out of scope, counted
    # but not listed: unchanged | split_in_current | not_classified | multiple_declared.
    status: str
    proposed: Optional[str] = None
    current: Dict[str, str] = field(default_factory=dict)
    target: Dict[str, str] = field(default_factory=dict)
    mismatched_in_current: bool = False


# Remap statuses the bump itself causes; only these anchors are listed in the report.
BUMP_DRIVEN = frozenset({"remap", "split", "unresolved"})


def _at_level(family_sf: str, subfamily_level: bool) -> str:
    return family_sf if subfamily_level else family_sf.split(":", 1)[0]


def propose_remap(
    anchor: Anchor, current_index: Mapping[str, str], target_index: Mapping[str, str]
) -> Remap:
    """Propose the target-release id for an anchor from its members' classification.

    A proposal is made only when every member found in the target release agrees.
    Members split across ids, or missing from the classification files, are told
    apart from the same state already present in the current release, which the
    bump did not cause.

    >>> a = Anchor("m.yaml", "$", ("PTHR1:SF5",), ("P1", "P2"))
    >>> propose_remap(a, {"P1": "PTHR1:SF5"}, {"P1": "PTHR1:SF5", "P2": "PTHR1:SF5"}).status
    'unchanged'
    >>> r = propose_remap(a, {"P1": "PTHR1:SF5"}, {"P1": "PTHR1:SF9", "P2": "PTHR1:SF9"})
    >>> r.status, r.proposed
    ('remap', 'PTHR1:SF9')
    >>> propose_remap(a, {"P1": "PTHR1:SF5"}, {"P1": "PTHR1:SF9", "P2": "PTHR1:SF8"}).status
    'split'
    >>> both = {"P1": "PTHR1:SF5", "P2": "PTHR1:SF6"}
    >>> propose_remap(a, both, {"P1": "PTHR1:SF9", "P2": "PTHR1:SF8"}).status
    'split_in_current'
    >>> propose_remap(a, {"P1": "PTHR1:SF5"}, {}).status, propose_remap(a, {}, {}).status
    ('unresolved', 'not_classified')
    >>> fam = Anchor("m.yaml", "$", ("PTHR1",), ("P1",))
    >>> propose_remap(fam, {"P1": "PTHR2:SF1"}, {"P1": "PTHR1:SF3"}).mismatched_in_current
    True
    """
    current = {acc: current_index[acc] for acc in anchor.members if acc in current_index}
    target = {acc: target_index[acc] for acc in anchor.members if acc in target_index}
    if len(anchor.declared) != 1:
        return Remap("multiple_declared", current=current, target=target)
    declared = anchor.declared[0]
    subfamily_level = ":" in declared
    mismatched = bool(current) and declared not in {
        _at_level(v, subfamily_level) for v in current.values()
    }
    if not target:
        status = "unresolved" if current else "not_classified"
        return Remap(status, current=current, target=target, mismatched_in_current=mismatched)
    levels = {_at_level(v, subfamily_level) for v in target.values()}
    if len(levels) > 1:
        already_split = len({_at_level(v, subfamily_level) for v in current.values()}) > 1
        status = "split_in_current" if already_split else "split"
        return Remap(status, current=current, target=target, mismatched_in_current=mismatched)
    (proposed,) = levels
    status = "unchanged" if proposed == declared else "remap"
    return Remap(
        status,
        None if status == "unchanged" else proposed,
        current,
        target,
        mismatched,
    )


def collect_anchors(root: Path) -> List[Anchor]:
    """All anchors in ``modules/`` and the family reviews under ``interpro/panther/``."""
    anchors: List[Anchor] = []
    for path in sorted(root.glob("modules/**/*.yaml")):
        anchors.extend(module_anchors(yaml.safe_load(path.read_text()), str(path.relative_to(root))))
    for path in sorted(root.glob("interpro/panther/*/*-review.yaml")):
        anchors.extend(
            family_review_anchors(yaml.safe_load(path.read_text()), str(path.relative_to(root)))
        )
    return anchors


def build_report(
    current_release: str,
    target_release: str,
    cited: Mapping[str, Set[str]],
    current_names: Mapping[str, str],
    target_names: Mapping[str, str],
    anchors: Iterable[Anchor],
    current_index: Mapping[str, str],
    target_index: Mapping[str, str],
) -> Dict[str, Any]:
    """Assemble the dry-run report as plain data (ready for YAML)."""
    changes = [classify_id(acc, current_names, target_names) for acc in sorted(cited)]
    id_counts = Counter(
        f"renamed_{c.drift}" if c.status == "renamed" else c.status for c in changes
    )
    remaps = [(anchor, propose_remap(anchor, current_index, target_index)) for anchor in anchors]
    remap_counts = Counter(remap.status for _, remap in remaps)
    return {
        "current_release": current_release,
        "target_release": target_release,
        "summary": {
            "cited_ids": len(changes),
            "ids": dict(sorted(id_counts.items())),
            "anchors": len(remaps),
            "anchor_remaps": dict(sorted(remap_counts.items())),
            "anchors_mismatched_in_current": sum(r.mismatched_in_current for _, r in remaps),
        },
        "ids": [
            {
                "id": f"PANTHER:{c.accession}",
                "status": c.status,
                **({"drift": c.drift} if c.drift else {}),
                **({"current_name": c.current_name} if c.current_name else {}),
                **({"target_name": c.target_name} if c.target_name else {}),
                "cited_in": sorted(cited[c.accession]),
            }
            for c in changes
            if c.status != "unchanged"
        ],
        "anchors": [
            {
                "file": anchor.file,
                "path": anchor.path,
                "declared": [f"PANTHER:{d}" for d in anchor.declared],
                "status": remap.status,
                **({"proposed": f"PANTHER:{remap.proposed}"} if remap.proposed else {}),
                **({"mismatched_in_current": True} if remap.mismatched_in_current else {}),
                f"members_{current_release}": remap.current,
                f"members_{target_release}": remap.target,
            }
            for anchor, remap in remaps
            if remap.status in BUMP_DRIVEN or remap.mismatched_in_current
        ],
    }
