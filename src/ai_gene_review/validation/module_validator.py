"""Term-label, GO-branch, and PTN validation for module YAML files.

The repository delegates gene-review term-label checking to the external
``linkml-term-validator``, but that tool only inspects slots bound to dynamic
enums or binding constraints. ``ModuleReview`` has neither, so the ``term``
descriptors scattered through a module document (``concepts``, ``function``,
``substrates``/``products``, ``locations``, ``processes``,
``anatomical_locations``, ...) are otherwise unchecked: a wrong label sails
through structural validation.

This validator closes that gap. It walks a module YAML, collects every
``{id, label}`` term, routes each id by prefix through the same
``conf/oak_config.yaml`` mapping used for gene reviews, resolves the id with
OAK, and reports:

* an ERROR when the provided label does not match the ontology's primary label
  or any of its aliases (case-insensitively), and
* an ERROR when the id cannot be found in the configured ontology.

Prefixes mapped to ``null`` (e.g. ``PMID``, ``UniProtKB``, ``file``) are skipped
silently; prefixes absent from the config are skipped with a warning, matching
the documented ``oak_config.yaml`` semantics.

It also enforces **bundle-scoped conformance**: any node declaring
``conforms_to`` a template motif is checked (via ``module_qc``) so that an
``error``-severity mismatch -- a wrong/missing tier, a broken relay topology,
or an unresolvable template -- blocks validation, while declared
``WITH_DEVIATIONS`` deviations surface as advisory warnings.

For direct terms in slots whose GO aspect is known, this validator also checks
the expected GO branch: molecular-function slots (``function`` and
``required_function``), biological-process slots (``processes``),
cellular-location slots (``locations`` and context cellular components), and
protein-complex slots. Generic descriptor terms remain ID/label-only checked.

PANTHER grounding is checked on three independent axes, because no single one is
sufficient:

* **Family/subfamily identity and label** (``PTHR12345``, ``PTHR12345:SF7``) are
  resolved through ``interpro/panther/panther.obo``, built from PANTHER's own HMM
  classifications (see ``ai_gene_review.etl.panther_families``). PANTHER offers no
  term-lookup service and InterPro indexes only families, so without this local
  artifact subfamily ids cannot be checked at all.
* **Ancestral nodes** in ``family.ancestral_nodes`` are checked against local
  ``interpro/panther/*/*-paint.tsv`` slices: a declared PTN must be a well-formed
  exact PTN id with a positive, non-negated IBD row. PTNs *cited as evidence*
  ``source_id`` are also checked, but only for attestation (PAINT slice or a
  machine-fetched ``*-goa.tsv``), since IRD/IKR nodes are legitimate provenance.
* **Family membership**: a descriptor's declared family must actually contain the
  protein it names in ``representative_members``, per PANTHER's sequence
  classification (``interpro/panther/panther-members.tsv``). This is the only
  check that separates a *mis-grounded* family from a merely *mislabelled* one --
  label checking alone cannot tell an invented label on the right family from a
  plausible label on the wrong one.

GO overlap, cross-family scope, GO_REF evidence, seed overlap, and partial member
agreement remain advisory warnings so the validator surfaces curation drift
without making module validation brittle.

Module taxon context is also checked for scope/provenance conflation: taxa must
name in-vivo taxa or clades, not experimental systems such as cell lines. Cell
line evidence belongs in evidence statements, not in ``context.taxa`` labels.

It also runs an **advisory reaction-chaining check**: for each ``PRECEDES``
connection it resolves both reactions' GO molecular-function terms to RHEA (via
the GO->RHEA mapping) and warns when the upstream reaction's product is not the
downstream reaction's substrate. This NEVER blocks; a ``chaining_status``
override on the connection (e.g. ``KNOWLEDGE_GAP``, ``MAPPING_GAP``) acknowledges
a real break and suppresses its warning.

Structural (schema) validation is handled separately by ``linkml-validate``
(see ``just validate-modules``); this module adds term-label, GO-branch, PTN,
taxon-scope, conformance, and chaining checking.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional, Set, Tuple

import yaml

from ai_gene_review.etl.panther_families import (
    label_drift,
    load_member_index,
    load_subfamily_counts,
)

# A resolver answers: given a CURIE, return (status, primary_label, aliases).
# status is "ok" when the id resolved, "not_found" when the ontology was
# consulted but the id is absent, and "unavailable" when the ontology itself
# could not be loaded/queried (e.g. transient download failure) - the latter is
# advisory so CI does not go red on flaky ontology fetches. Implemented as a
# plain callable so it can be dependency-injected in tests without mocking.
Resolver = Callable[[str], Tuple[str, Optional[str], Set[str]]]

# A branch resolver answers: given a child GO id and required root GO id, return
# "ok", "not_in_branch", "not_found", or "unavailable".
BranchResolver = Callable[[str, str], str]

PTN_ID_RE = re.compile(r"^PANTHER:PTN\d+$")
# Anchored on word boundaries so a PTN embedded in a longer token (an
# accession that merely contains "PTN1234") is not read as attestation.
BARE_PTN_RE = re.compile(r"\bPTN\d+\b")
PANTHER_FAMILY_RE = re.compile(r"^PANTHER:(PTHR\d+)(?::SF\d+)?$")
TAXON_EXPERIMENTAL_SYSTEM_RE = re.compile(
    r"\b("
    r"defined\s+in|"
    r"cell[-\s]?lines?|"
    r"cell\s+culture|"
    r"cultured\s+cells?|"
    r"in\s+vitro|"
    r"assays?\s+in|"
    r"assayed\s+in|"
    r"HEK[-\s]?293|"
    r"293T|"
    r"HeLa|"
    r"K562|"
    r"A549|"
    r"U2OS|"
    r"MCF[-\s]?7"
    r")\b",
    re.IGNORECASE,
)

PaintIndex = Dict[str, List["PaintAnnotationRow"]]
_PAINT_INDEX_CACHE: Dict[Path, PaintIndex] = {}
_GOA_PTN_CACHE: Dict[Path, Set[str]] = {}
# OAK adapters are expensive to build (the PANTHER OBO is ~14 MB), and the CLI
# validates many files per process, so cache them for the process lifetime.
_ADAPTER_CACHE: Dict[str, object] = {}
_FAILED_ADAPTERS: Set[str] = set()


@dataclass(frozen=True)
class GoBranchConstraint:
    """Expected GO branch for a direct term in a known module slot."""

    root_id: str
    branch_label: str


@dataclass(frozen=True)
class TypedGoTerm:
    """A direct GO term occurrence in a slot with a known expected branch."""

    path: str
    curie: str
    label: str
    constraint: GoBranchConstraint


@dataclass(frozen=True)
class ModuleGoAssertion:
    """A nearby module GO assertion that an ancestral PTN may support."""

    path: str
    aspect: str
    curie: str


@dataclass(frozen=True)
class AncestralNodeUse:
    """A module use of a PANTHER/PAINT ancestral node."""

    path: str
    ptn_curie: str
    family_curie: Optional[str]
    family_term_curies: frozenset[str]
    representative_uniprot_accessions: frozenset[str]
    asserted_go_terms: Tuple[ModuleGoAssertion, ...]
    has_go_ref_0000033: bool
    # Assertions from the NEAREST enclosing ancestor that makes any. The full
    # ``asserted_go_terms`` set reaches to the module root, which is fine for an
    # advisory overlap hint but far too wide for a blocking error -- the same
    # nearest-enclosing-scope argument the taxon check needs.
    #
    # Deliberately has NO default: it drives a blocking check, so a construction
    # site that forgot to populate it would silently disable that check rather
    # than fail. Required means a new caller cannot fail open by omission.
    nearest_asserted_go_terms: Tuple[ModuleGoAssertion, ...]


@dataclass(frozen=True)
class PaintAnnotationRow:
    """One row from a local ``*-paint.tsv`` PAINT slice."""

    family: str
    node_curie: str
    go_id: str
    aspect: str
    evidence: str
    negated: bool
    seeds: str
    source_path: Path

    @property
    def uniprot_seed_accessions(self) -> Set[str]:
        """Return UniProtKB accessions from the PAINT seed field."""
        accessions: Set[str] = set()
        for seed in self.seeds.split("|"):
            if seed.startswith("UniProtKB:"):
                accessions.add(seed.split(":", 1)[1])
        return accessions


GO_BRANCH_CONSTRAINTS: Dict[str, GoBranchConstraint] = {
    # MolecularFunctionDescriptor-bearing participant/function slots.
    "function": GoBranchConstraint("GO:0003674", "molecular function"),
    "required_function": GoBranchConstraint("GO:0003674", "molecular function"),
    # BiologicalProcessDescriptor-bearing annoton slot.
    "processes": GoBranchConstraint("GO:0008150", "biological process"),
    # CellularComponentDescriptor-bearing location slots. Use GO:0110165 to
    # mirror GOCellularLocationEnum, excluding protein-containing complexes.
    "locations": GoBranchConstraint("GO:0110165", "cellular anatomical entity"),
    "cellular_components": GoBranchConstraint(
        "GO:0110165", "cellular anatomical entity"
    ),
    "source_location": GoBranchConstraint(
        "GO:0110165", "cellular anatomical entity"
    ),
    "destination_location": GoBranchConstraint(
        "GO:0110165", "cellular anatomical entity"
    ),
    # ProteinComplexDescriptor-bearing participant slot.
    "protein_complex": GoBranchConstraint("GO:0032991", "protein-containing complex"),
}

GO_ASPECT_BY_SLOT: Dict[str, str] = {
    "function": "F",
    "required_function": "F",
    "processes": "P",
    "locations": "C",
    "cellular_components": "C",
    "source_location": "C",
    "destination_location": "C",
    "protein_complex": "C",
}


@dataclass
class ModuleValidationResult:
    """Result of validating a single module file's term labels."""

    path: Path
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """True when there are no errors (warnings are advisory)."""
        return not self.errors


def iter_terms(obj: object) -> Iterator[Tuple[str, str]]:
    """Yield every ontology ``(id, label)`` pair from a parsed module document.

    In the schema, ontology grounding only ever appears as the value of a
    ``term`` key (``Descriptor.term``, range ``Term``). Module *nodes* and
    *annotons* also carry ``id``/``label`` fields, but those are
    document-scoped identifiers, not ontology terms, so they must NOT be
    collected. We therefore yield only dicts reached via a ``term`` key that
    carry a string ``id`` and ``label``.

    >>> doc = {"term": {"id": "GO:1", "label": "x"}}
    >>> list(iter_terms(doc))
    [('GO:1', 'x')]
    >>> list(iter_terms({"id": "some_node", "label": "a node"}))
    []
    """
    for _path, curie, label in iter_terms_with_paths(obj):
        yield (curie, label)


def iter_terms_with_paths(
    obj: object, path: str = "$"
) -> Iterator[Tuple[str, str, str]]:
    """Yield ``(yaml_path, id, label)`` for every ontology term descriptor.

    Same selection rules as :func:`iter_terms`, but carrying the YAML path so a
    caller can act on one specific descriptor. Paths are built exactly as in
    :func:`iter_family_member_uses`, so the two can be cross-referenced.

    >>> list(iter_terms_with_paths({"a": {"term": {"id": "GO:1", "label": "x"}}}))
    [('$.a.term', 'GO:1', 'x')]
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if (
                key == "term"
                and isinstance(value, dict)
                and isinstance(value.get("id"), str)
                and isinstance(value.get("label"), str)
            ):
                yield (f"{path}.term", value["id"], value["label"])
            if key == "family_terms":
                for index, item in enumerate(_as_list(value)):
                    if (
                        isinstance(item, dict)
                        and isinstance(item.get("id"), str)
                        and isinstance(item.get("label"), str)
                    ):
                        yield (
                            f"{path}.family_terms[{index}]",
                            item["id"],
                            item["label"],
                        )
            yield from iter_terms_with_paths(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from iter_terms_with_paths(item, f"{path}[{index}]")


def _as_list(value: object) -> List[object]:
    """Return ``value`` as a list, treating null as empty."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def iter_typed_go_terms(obj: object, path: str = "$") -> Iterator[TypedGoTerm]:
    """Yield direct terms in module slots with known GO branch expectations.

    Generic descriptor terms are intentionally not yielded here: ``concepts``,
    ``substrates``, ``products``, ``cargo``, etc. can legitimately reference
    terms from any GO aspect or from non-GO ontologies. Direct terms under
    slots like ``function`` and ``processes`` have a known aspect and therefore
    get branch-checked.

    >>> doc = {"function": {"term": {"id": "GO:1", "label": "x"}}}
    >>> [(t.path, t.curie, t.constraint.root_id) for t in iter_typed_go_terms(doc)]
    [('$.function.term', 'GO:1', 'GO:0003674')]
    >>> list(iter_typed_go_terms({"concepts": [{"term": {"id": "GO:1", "label": "x"}}]}))
    []
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            child_path = f"{path}.{key}"
            constraint = GO_BRANCH_CONSTRAINTS.get(key)
            if constraint is not None:
                values = _as_list(value)
                for index, descriptor in enumerate(values):
                    if not isinstance(descriptor, dict):
                        continue
                    descriptor_path = (
                        f"{child_path}[{index}]" if isinstance(value, list) else child_path
                    )
                    term = descriptor.get("term")
                    if (
                        isinstance(term, dict)
                        and isinstance(term.get("id"), str)
                        and isinstance(term.get("label"), str)
                    ):
                        yield TypedGoTerm(
                            path=f"{descriptor_path}.term",
                            curie=term["id"],
                            label=term["label"],
                            constraint=constraint,
                        )
            yield from iter_typed_go_terms(value, child_path)
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from iter_typed_go_terms(item, f"{path}[{index}]")


def iter_taxon_descriptors(obj: object, path: str = "$") -> Iterator[Tuple[str, dict]]:
    """Yield every descriptor under module ``taxa``/``taxon`` slots.

    Taxon context should describe the in-vivo biological scope of a module, not
    the experimental system used to discover it.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            child_path = f"{path}.{key}"
            if key == "taxa":
                for index, descriptor in enumerate(_as_list(value)):
                    if isinstance(descriptor, dict):
                        yield (
                            f"{child_path}[{index}]"
                            if isinstance(value, list)
                            else child_path,
                            descriptor,
                        )
            elif key == "taxon":
                for index, descriptor in enumerate(_as_list(value)):
                    if isinstance(descriptor, dict):
                        yield (
                            f"{child_path}[{index}]"
                            if isinstance(value, list)
                            else child_path,
                            descriptor,
                        )
            yield from iter_taxon_descriptors(value, child_path)
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from iter_taxon_descriptors(item, f"{path}[{index}]")


def _iter_direct_go_assertions(obj: object, path: str) -> Iterator[ModuleGoAssertion]:
    """Yield direct GO assertions from known typed slots on one module object."""
    if not isinstance(obj, dict):
        return

    for slot_name, aspect in GO_ASPECT_BY_SLOT.items():
        if slot_name not in obj:
            continue
        value = obj[slot_name]
        for index, descriptor in enumerate(_as_list(value)):
            if not isinstance(descriptor, dict):
                continue
            descriptor_path = (
                f"{path}.{slot_name}[{index}]"
                if isinstance(value, list)
                else f"{path}.{slot_name}"
            )
            term = descriptor.get("term")
            if (
                isinstance(term, dict)
                and isinstance(term.get("id"), str)
                and term["id"].startswith("GO:")
            ):
                yield ModuleGoAssertion(
                    path=f"{descriptor_path}.term",
                    aspect=aspect,
                    curie=term["id"],
                )


def _direct_family_curie(family: dict) -> Optional[str]:
    """Return the direct PANTHER family term id for a family descriptor."""
    term = family.get("term")
    if isinstance(term, dict) and isinstance(term.get("id"), str):
        return term["id"]
    return None


def _family_term_curies(family: dict) -> frozenset[str]:
    """Return PANTHER family ids accepted for a family descriptor."""
    curies: Set[str] = set()
    direct_curie = _direct_family_curie(family)
    if direct_curie:
        curies.add(direct_curie)

    for family_term in _as_list(family.get("family_terms")):
        if not isinstance(family_term, dict):
            continue
        curie = family_term.get("id")
        if isinstance(curie, str):
            curies.add(curie)
    return frozenset(curies)


def _representative_uniprot_accessions(family: dict) -> frozenset[str]:
    """Return direct UniProtKB accessions from ``representative_members``."""
    accessions: Set[str] = set()
    for representative in _as_list(family.get("representative_members")):
        if not isinstance(representative, dict):
            continue
        term = representative.get("term")
        if not isinstance(term, dict):
            continue
        curie = term.get("id")
        if isinstance(curie, str) and curie.startswith("UniProtKB:"):
            accessions.add(curie.split(":", 1)[1])
    return frozenset(accessions)


def _has_go_ref_0000033(descriptor: dict) -> bool:
    """True if a descriptor has a direct GO_REF:0000033 evidence item."""
    for evidence in _as_list(descriptor.get("evidence")):
        if isinstance(evidence, dict) and evidence.get("source_id") == "GO_REF:0000033":
            return True
    return False


def iter_ancestral_node_uses(
    obj: object,
    path: str = "$",
    ancestors: Tuple[Tuple[str, dict], ...] = (),
) -> Iterator[AncestralNodeUse]:
    """Yield every module use of ``family.ancestral_nodes`` with context.

    Two GO-assertion sets are carried, because they serve checks of different
    severity. ``asserted_go_terms`` collects direct typed slots from every
    enclosing ancestor (annotons, complex units, protein-complex descriptors) up
    to the module root -- wide enough to be a useful *advisory* overlap hint.
    ``nearest_asserted_go_terms`` keeps only those from the closest ancestor that
    makes any assertion at all, which is what a *blocking* check must use: an
    assertion several levels up is not this descriptor's claim.
    """
    if isinstance(obj, dict):
        ancestral_nodes = obj.get("ancestral_nodes")
        if isinstance(ancestral_nodes, list):
            family_curie = _direct_family_curie(obj)
            family_term_curies = _family_term_curies(obj)
            representative_accessions = _representative_uniprot_accessions(obj)

            asserted_terms: List[ModuleGoAssertion] = []
            nearest_terms: List[ModuleGoAssertion] = []
            seen_assertions: Set[Tuple[str, str, str]] = set()
            for ancestor_path, ancestor in reversed(ancestors):
                found = list(_iter_direct_go_assertions(ancestor, ancestor_path))
                if found and not nearest_terms:
                    nearest_terms = found
                for assertion in found:
                    key = (assertion.path, assertion.aspect, assertion.curie)
                    if key not in seen_assertions:
                        seen_assertions.add(key)
                        asserted_terms.append(assertion)

            for index, node_descriptor in enumerate(ancestral_nodes):
                node_path = f"{path}.ancestral_nodes[{index}]"
                ptn_curie = "<missing>"
                if isinstance(node_descriptor, dict):
                    term = node_descriptor.get("term")
                    if isinstance(term, dict) and isinstance(term.get("id"), str):
                        ptn_curie = term["id"]
                yield AncestralNodeUse(
                    path=f"{node_path}.term",
                    ptn_curie=ptn_curie,
                    family_curie=family_curie,
                    family_term_curies=family_term_curies,
                    representative_uniprot_accessions=representative_accessions,
                    asserted_go_terms=tuple(asserted_terms),
                    nearest_asserted_go_terms=tuple(nearest_terms),
                    has_go_ref_0000033=(
                        isinstance(node_descriptor, dict)
                        and _has_go_ref_0000033(node_descriptor)
                    ),
                )

        for key, value in obj.items():
            yield from iter_ancestral_node_uses(
                value,
                f"{path}.{key}",
                ancestors + ((path, obj),),
            )
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from iter_ancestral_node_uses(item, f"{path}[{index}]", ancestors)


def _paint_node_curie(node: str) -> str:
    """Normalize a PAINT TSV node id to the module CURIE form."""
    return node if node.startswith("PANTHER:") else f"PANTHER:{node}"


def load_paint_index(panther_dir: Path) -> PaintIndex:
    """Load local PANTHER PAINT TSV slices into a PTN-indexed mapping."""
    panther_dir = Path(panther_dir)
    try:
        cache_key = panther_dir.resolve()
    except OSError:
        cache_key = panther_dir
    if cache_key in _PAINT_INDEX_CACHE:
        return _PAINT_INDEX_CACHE[cache_key]

    index: PaintIndex = {}
    if not panther_dir.exists():
        _PAINT_INDEX_CACHE[cache_key] = index
        return index

    for tsv_path in sorted(panther_dir.glob("PTHR*/PTHR*-paint.tsv")):
        with open(tsv_path, newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            for row in reader:
                node = row.get("node")
                if not node:
                    continue
                node_curie = _paint_node_curie(node)
                index.setdefault(node_curie, []).append(
                    PaintAnnotationRow(
                        family=str(row.get("family") or ""),
                        node_curie=node_curie,
                        go_id=str(row.get("go_id") or ""),
                        aspect=str(row.get("aspect") or ""),
                        evidence=str(row.get("evidence") or ""),
                        negated=str(row.get("negated") or "").lower() == "true",
                        seeds=str(row.get("seeds") or ""),
                        source_path=tsv_path,
                    )
                )
    _PAINT_INDEX_CACHE[cache_key] = index
    return index


def _is_panther_subfamily(curie: str) -> bool:
    """True for a subfamily CURIE such as ``PANTHER:PTHR13337:SF6``.

    The prefix colon makes a naive ``":" in curie`` test useless here.

    >>> _is_panther_subfamily("PANTHER:PTHR13337:SF6")
    True
    >>> _is_panther_subfamily("PANTHER:PTHR13337")
    False
    """
    match = PANTHER_FAMILY_RE.match(curie)
    if match is None:
        return False
    return curie != f"PANTHER:{match.group(1)}"


def _panther_family_base(curie: Optional[str]) -> Optional[str]:
    """Return the PTHR family id from a PANTHER family/subfamily CURIE."""
    if curie is None:
        return None
    match = PANTHER_FAMILY_RE.match(curie)
    if not match:
        return None
    return match.group(1)


def _format_limited(values: Set[str], limit: int = 8) -> str:
    """Format a set of short strings for validation messages."""
    ordered = sorted(values)
    if len(ordered) <= limit:
        return ", ".join(ordered)
    return ", ".join(ordered[:limit]) + f", ... (+{len(ordered) - limit} more)"


GoAncestors = Callable[[str], Set[str]]


def _assertion_is_lost(
    assertion: ModuleGoAssertion,
    lost: Set[Tuple[str, str]],
    go_ancestors: Optional[GoAncestors],
) -> bool:
    """True if the assertion is a lost term, or a descendant of one.

    A descendant of a struck-out term is at least as contradicted as the term
    itself -- losing "receptor tyrosine kinase activity" also rules out any
    specialisation of it.
    """
    if (assertion.aspect, assertion.curie) in lost:
        return True
    if go_ancestors is None:
        return False
    ancestors = go_ancestors(assertion.curie)
    return any(
        aspect == assertion.aspect and go_id in ancestors for aspect, go_id in lost
    )


def _go_terms_agree(
    asserted: Tuple[ModuleGoAssertion, ...],
    supported: Set[Tuple[str, str]],
    go_ancestors: Optional[GoAncestors],
) -> bool:
    """True if any asserted term is equal to, or related by ancestry to, a node term."""
    for assertion in asserted:
        for aspect, go_id in supported:
            if aspect != assertion.aspect:
                continue
            if go_id == assertion.curie:
                return True
            if go_ancestors is None:
                continue
            if assertion.curie in go_ancestors(go_id):
                return True
            if go_id in go_ancestors(assertion.curie):
                return True
    return False


def validate_paint_ptns(
    uses: List[AncestralNodeUse],
    paint_index: PaintIndex,
    go_ancestors: Optional[GoAncestors] = None,
) -> Tuple[List[str], List[str]]:
    """Validate module PTN declarations against local PAINT IBD TSV rows."""
    errors: List[str] = []
    warnings: List[str] = []

    for use in uses:
        if not PTN_ID_RE.match(use.ptn_curie):
            errors.append(
                f"{use.path}: expected ancestral node id PANTHER:PTN<digits>, "
                f"got {use.ptn_curie}"
            )
            continue

        rows = paint_index.get(use.ptn_curie, [])
        if not rows:
            errors.append(
                f"{use.path}: {use.ptn_curie} not found in local "
                "interpro/panther/*/*-paint.tsv PAINT index"
            )
            continue

        positive_ibd_rows = [
            row for row in rows if row.evidence == "IBD" and not row.negated
        ]
        if not positive_ibd_rows:
            evidence_seen = _format_limited(
                {
                    f"{'NOT|' if row.negated else ''}{row.evidence}:{row.go_id}"
                    for row in rows
                }
            )
            errors.append(
                f"{use.path}: {use.ptn_curie} has no positive non-negated IBD "
                f"row in local PAINT TSVs; found {evidence_seen or 'no rows'}"
            )
            continue

        # A node may record that a function was LOST on this lineage (IRD/IKR, or
        # an explicit NOT). Inheriting the very term PAINT struck out inverts the
        # evolutionary inference: pseudoenzymes are exactly the case where the
        # ancestral activity is gone while the fold and the family membership
        # remain, so this must block rather than advise.
        lost = {
            (row.aspect, row.go_id)
            for row in rows
            if (row.negated or row.evidence in ("IRD", "IKR")) and row.go_id
        }
        # Support detection walks GO ancestry, so loss detection must too, or the
        # check is trivially evaded by asserting a *descendant* of the struck-out
        # term. Only descendants count: asserting an ancestor of a lost term
        # (e.g. "molecular_function" over a lost kinase activity) is broader than
        # what was lost and is not contradicted by it.
        contradicted = [
            assertion
            for assertion in use.nearest_asserted_go_terms
            if _assertion_is_lost(assertion, lost, go_ancestors)
        ]
        if contradicted:
            struck = _format_limited(
                {f"{a.aspect}:{a.curie}" for a in contradicted}
            )
            retained = _format_limited(
                {
                    f"{row.aspect}:{row.go_id}"
                    for row in positive_ibd_rows
                    if row.go_id
                }
            )
            errors.append(
                f"{use.path}: the module asserts {struck} but PAINT records that "
                f"term as LOST (IRD/IKR) at {use.ptn_curie}, so this node cannot "
                f"support inheriting it. Terms the node does retain: {retained}."
            )
            continue

        if not use.has_go_ref_0000033:
            warnings.append(
                f"{use.path}: {use.ptn_curie} is backed by PAINT IBD rows but "
                "the ancestral node descriptor lacks evidence source_id "
                "GO_REF:0000033"
            )

        family_bases = {
            base
            for curie in use.family_term_curies
            if (base := _panther_family_base(curie)) is not None
        }
        invalid_family_curies = {
            curie
            for curie in use.family_term_curies
            if _panther_family_base(curie) is None
        }
        paint_families = {row.family for row in positive_ibd_rows if row.family}
        if family_bases and not family_bases.intersection(paint_families):
            warnings.append(
                f"{use.path}: {use.ptn_curie} IBD rows belong to "
                f"{_format_limited({f'PANTHER:{f}' for f in paint_families})}; "
                "enclosing family terms are "
                f"{_format_limited(set(use.family_term_curies))}. Document "
                "cross-family scope if intentional."
            )
        elif invalid_family_curies:
            warnings.append(
                f"{use.path}: enclosing family ids "
                f"{_format_limited(invalid_family_curies)} are not PANTHER "
                "PTHR/PTHR:SF CURIEs, so family consistency was not checked "
                "for those ids"
            )

        if use.asserted_go_terms:
            supported = {
                (row.aspect, row.go_id)
                for row in positive_ibd_rows
                if row.aspect and row.go_id
            }
            asserted = {
                f"{assertion.aspect}:{assertion.curie}"
                for assertion in use.asserted_go_terms
            }
            ibd_terms = {f"{aspect}:{go_id}" for aspect, go_id in supported}
            # Exact equality is too strict: a node annotated to a child term does
            # support a parent claim (and vice versa is a documented
            # generalisation), so only a term with no ancestry relation at all is
            # worth surfacing.
            if not _go_terms_agree(use.asserted_go_terms, supported, go_ancestors):
                asserted_aspects = {a.aspect for a in use.asserted_go_terms}
                node_aspects = {aspect for aspect, _ in supported}
                missing_aspects = asserted_aspects - node_aspects
                if missing_aspects:
                    # The commonest shape: the node attests the pathway role but
                    # nothing in the molecular-function aspect being claimed.
                    warnings.append(
                        f"{use.path}: {use.ptn_curie} attests nothing in GO aspect "
                        f"{'/'.join(sorted(missing_aspects))}, so it cannot be the "
                        f"evidence for {_format_limited(asserted)}; its IBD rows "
                        f"cover {_format_limited(ibd_terms)}. The claim needs "
                        "separate support."
                    )
                else:
                    warnings.append(
                        f"{use.path}: {use.ptn_curie} supports "
                        f"{_format_limited(ibd_terms)}, which has no ancestry "
                        f"relation to the module's {_format_limited(asserted)}"
                    )

        if use.representative_uniprot_accessions:
            seed_accessions: Set[str] = set()
            all_seeds: Set[str] = set()
            for row in positive_ibd_rows:
                seed_accessions.update(row.uniprot_seed_accessions)
                all_seeds.update(s for s in row.seeds.split("|") if s.strip())
            if not seed_accessions.intersection(use.representative_uniprot_accessions):
                representatives = _format_limited(
                    set(use.representative_uniprot_accessions)
                )
                if not seed_accessions:
                    # PAINT seeds are model-organism ids (MGI, SGD, FB, WB, ...)
                    # as often as UniProtKB ones, so an empty UniProt seed set
                    # makes the comparison vacuous rather than negative.
                    warnings.append(
                        f"{use.path}: seed overlap not checked -- this node's IBD "
                        f"seeds carry no UniProtKB accession "
                        f"({_format_limited(all_seeds) or 'no seeds'}), so they "
                        f"cannot be compared with {representatives}"
                    )
                else:
                    warnings.append(
                        f"{use.path}: no representative UniProtKB accession "
                        f"({representatives}) appears among IBD seed UniProtKB "
                        f"accessions ({_format_limited(seed_accessions)})"
                    )

    return errors, warnings


@dataclass(frozen=True)
class FamilyMemberUse:
    """A module family descriptor together with its representative members."""

    path: str
    declared_family_curies: frozenset[str]
    representative_accessions: frozenset[str]
    ancestral_node_curies: frozenset[str] = frozenset()


def count_ungrounded_families(obj: object) -> int:
    """Count family descriptors that name members but assert no PANTHER id.

    Omitting an id is the correct conservative move when the family cannot be
    established (see CLAUDE.md), so this is a visibility counter, not a defect:
    it keeps the size of the "not yet grounded" backlog countable by tooling
    without creating a mechanism that could suppress a real error.
    """
    total = 0
    if isinstance(obj, dict):
        family = obj.get("family")
        if isinstance(family, dict):
            term = family.get("term")
            has_id = isinstance(term, dict) and isinstance(term.get("id"), str)
            if not has_id and _representative_uniprot_accessions(family):
                total += 1
        for value in obj.values():
            total += count_ungrounded_families(value)
    elif isinstance(obj, list):
        for item in obj:
            total += count_ungrounded_families(item)
    return total


def iter_family_member_uses(
    obj: object, path: str = "$"
) -> Iterator[FamilyMemberUse]:
    """Yield every family descriptor that names representative UniProt members.

    Only descriptors carrying both a PANTHER family/subfamily id and at least one
    ``representative_members`` UniProtKB accession are yielded; anything else
    cannot be cross-checked.
    """
    if isinstance(obj, dict):
        family_curies = {
            curie
            for curie in _family_term_curies(obj)
            if _panther_family_base(curie) is not None
        }
        accessions = _representative_uniprot_accessions(obj)
        if family_curies and accessions:
            nodes = set()
            for node_descriptor in _as_list(obj.get("ancestral_nodes")):
                if not isinstance(node_descriptor, dict):
                    continue
                term = node_descriptor.get("term")
                if isinstance(term, dict) and isinstance(term.get("id"), str):
                    if PTN_ID_RE.match(term["id"]):
                        nodes.add(term["id"])
            yield FamilyMemberUse(
                path=f"{path}.term",
                declared_family_curies=frozenset(family_curies),
                representative_accessions=frozenset(accessions),
                ancestral_node_curies=frozenset(nodes),
            )
        for key, value in obj.items():
            yield from iter_family_member_uses(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from iter_family_member_uses(item, f"{path}[{index}]")


# A family split into at least this many subfamilies tells you little about any
# individual member, so grounding a specific functional claim on it is imprecise
# even when the id is correct. Advisory only -- narrowing to the subfamily is a
# curation judgement, not a correctness fix.
HETEROGENEOUS_FAMILY_SUBFAMILIES = 20

def _paint_corroborated_families(
    use: FamilyMemberUse, paint_index: Optional[PaintIndex]
) -> Set[str]:
    """Families that PAINT itself assigns to this descriptor's ancestral nodes."""
    if not paint_index:
        return set()
    families: Set[str] = set()
    for node_curie in use.ancestral_node_curies:
        for row in paint_index.get(node_curie, []):
            if row.family:
                families.add(row.family)
    return families


def validate_family_members(
    uses: List[FamilyMemberUse],
    member_index: Dict[str, str],
    paint_index: Optional[PaintIndex] = None,
    subfamily_counts: Optional[Dict[str, int]] = None,
) -> Tuple[List[str], List[str]]:
    """Check that a declared PANTHER family really contains its own members.

    Label checking alone cannot distinguish a *wrong label on the right family*
    from a *plausible label on the wrong family*: both look like a mismatch, and
    a label that happens to match nothing is indistinguishable from one that was
    invented. This check is the independent signal -- PANTHER's own sequence
    classification says which family each UniProt accession belongs to, so a
    descriptor that names ``PTHR11375`` while its representative member sits in
    ``PTHR13337`` is provably mis-grounded regardless of how its label reads.

    Accessions absent from the (pruned) index are not checkable and degrade to a
    warning, so a newly cited protein never fails the build spuriously.
    """
    errors: List[str] = []
    warnings: List[str] = []

    for use in uses:
        declared_bases = {
            base
            for curie in use.declared_family_curies
            if (base := _panther_family_base(curie)) is not None
        }
        known = {
            accession: member_index[accession]
            for accession in use.representative_accessions
            if accession in member_index
        }
        if not known:
            warnings.append(
                f"{use.path}: none of the representative members "
                f"({_format_limited(set(use.representative_accessions))}) are in "
                "interpro/panther/panther-members.tsv, so family membership was "
                "not checked; refresh with `just refresh-panther-members`"
            )
            continue

        member_bases = {family_sf.split(":", 1)[0] for family_sf in known.values()}
        if declared_bases & member_bases:
            # Precision advisory: the id is right, but if every member resolves
            # to one subfamily of a large family, the subfamily is the sharper
            # grounding for a specific functional claim.
            member_subfamilies = {v for v in known.values() if ":" in v}
            declared_at_subfamily = any(
                _is_panther_subfamily(curie) for curie in use.declared_family_curies
            )
            if (
                subfamily_counts
                and len(member_subfamilies) == 1
                and not declared_at_subfamily
            ):
                subfamily = next(iter(member_subfamilies))
                base = subfamily.split(":", 1)[0]
                count = subfamily_counts.get(base, 0)
                if count >= HETEROGENEOUS_FAMILY_SUBFAMILIES:
                    warnings.append(
                        f"{use.path}: PANTHER:{base} is split into {count} "
                        f"subfamilies; every representative member here is in "
                        f"PANTHER:{subfamily}. Consider grounding on the "
                        "subfamily, which identifies the protein rather than "
                        "just its superfamily."
                    )
            # A descriptor may deliberately group proteins PANTHER splits across
            # families (a functional grouping rather than a strict family), so
            # partial agreement is advisory, not an error.
            outside = {
                accession: family_sf
                for accession, family_sf in known.items()
                if family_sf.split(":", 1)[0] not in declared_bases
            }
            if outside:
                listed = ", ".join(
                    f"{accession} is in PANTHER:{family_sf}"
                    for accession, family_sf in sorted(outside.items())
                )
                warnings.append(
                    f"{use.path}: some representative members fall outside the "
                    f"declared family -- {listed}. Confirm the grouping is "
                    "intentional, or split the descriptor."
                )
            continue
        actual = ", ".join(
            f"{accession} is in PANTHER:{family_sf}"
            for accession, family_sf in sorted(known.items())
        )
        declared = _format_limited({f"PANTHER:{base}" for base in declared_bases})
        # UniProt and PAINT genuinely disagree about some proteins' family. When
        # the descriptor also declares a PAINT ancestral node that PAINT itself
        # places in the declared family, the grounding is corroborated by a
        # second machine source and the disagreement is reported, not enforced.
        if declared_bases & _paint_corroborated_families(use, paint_index):
            warnings.append(
                f"{use.path}: PANTHER's sequence classification puts {actual}, "
                f"not in the declared {declared}, but the descriptor's PAINT "
                "ancestral node(s) are in the declared family; the two PANTHER "
                "sources disagree for this protein. Document which one the "
                "module follows."
            )
            continue
        errors.append(
            f"{use.path}: declared PANTHER family {declared} does not contain "
            f"its own representative member(s) -- {actual}. Either the family "
            "id or the representative member is wrong."
        )

    return errors, warnings


def iter_cited_ptn_sources(obj: object, path: str = "$") -> Iterator[Tuple[str, str]]:
    """Yield ``(path, PTN curie)`` for every PTN cited as an evidence source.

    ``family.ancestral_nodes`` is not the only place a PTN is asserted: evidence
    items cite them directly via ``source_id``, and those were previously
    unchecked, so a node that does not exist -- or exists but carries no PAINT
    support -- could be cited as provenance with nothing to catch it.

    >>> doc = {"evidence": [{"source_id": "PANTHER:PTN1"}, {"source_id": "PMID:1"}]}
    >>> list(iter_cited_ptn_sources(doc))
    [('$.evidence[0].source_id', 'PANTHER:PTN1')]
    """
    if isinstance(obj, dict):
        source_id = obj.get("source_id")
        if isinstance(source_id, str) and PTN_ID_RE.match(source_id):
            yield (f"{path}.source_id", source_id)
        for key, value in obj.items():
            yield from iter_cited_ptn_sources(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from iter_cited_ptn_sources(item, f"{path}[{index}]")


def load_goa_attested_ptns(genes_dir: Path) -> Set[str]:
    """Collect every PTN id appearing in a machine-fetched ``*-goa.tsv``.

    GOA files are downloaded from QuickGO, never authored, so the PTN ids in
    their with/from columns are trusted by construction -- the same asymmetry
    the project already applies to existing-annotation term ids. They are also
    a *broader* attestation than the local PAINT slices: GOA's IBA data can name
    an ancestral node that the current ``IBD.gaf`` snapshot no longer carries, so
    without this a real, machine-sourced id would be reported as fabricated.
    """
    genes_dir = Path(genes_dir)
    if genes_dir in _GOA_PTN_CACHE:
        return _GOA_PTN_CACHE[genes_dir]
    attested: Set[str] = set()
    if genes_dir.exists():
        for goa_path in genes_dir.rglob("*-goa.tsv"):
            attested.update(
                f"PANTHER:{node}"
                for node in BARE_PTN_RE.findall(goa_path.read_text(errors="replace"))
            )
    _GOA_PTN_CACHE[genes_dir] = attested
    return attested


def validate_cited_ptn_sources(
    cited: List[Tuple[str, str]],
    paint_index: PaintIndex,
    goa_attested: Optional[Set[str]] = None,
) -> List[str]:
    """Error for evidence-cited PTNs attested by neither PAINT nor GOA.

    Unlike ``validate_paint_ptns`` this does not require positive IBD support:
    an ``IRD``/``IKR`` node is legitimate provenance, and a node attested only by
    GOA is legitimate too (see :func:`load_goa_attested_ptns`). It requires only
    that the id be attested *somewhere machine-sourced* rather than authored --
    which is precisely what a fabricated node id would fail.
    """
    errors: List[str] = []
    attested = goa_attested or set()
    for path, curie in cited:
        if paint_index.get(curie) or curie in attested:
            continue
        errors.append(
            f"{path}: {curie} is cited as an evidence source but appears in "
            "neither the local interpro/panther/*/*-paint.tsv PAINT index nor "
            "any machine-fetched genes/**/*-goa.tsv; fetch the family with "
            "`just fetch-panther-paint <FAMILY>` or correct the id"
        )
    return errors


def compare_label(
    curie: str, provided: str, primary: Optional[str], aliases: Set[str]
) -> Optional[str]:
    """Return an error message if ``provided`` does not match the ontology.

    A match is exact or case-insensitive against the primary label or any alias.

    >>> compare_label("X:1", "root", "root", set()) is None
    True
    >>> compare_label("X:1", "wrong", "root", set()) is not None
    True
    """
    candidates = {c for c in ([primary] if primary else []) + list(aliases)}
    if provided in candidates:
        return None
    lowered = {c.lower() for c in candidates}
    if provided.lower() in lowered:
        return None
    shown = primary if primary is not None else "<no label>"
    message = (
        f"Label mismatch for {curie}: module says '{provided}' "
        f"but ontology label is '{shown}'"
    )
    # A label naming a different entity entirely is weak evidence of a typo and
    # strong evidence of a wrong id -- an id guessed at random is still a
    # hallucination when it happens to resolve. Say so, so the reader fixes the
    # id rather than "correcting" the label and cementing the wrong grounding.
    if primary and label_drift(provided, primary) == "divergent":
        message += (
            ". These name different entities, which usually means the ID is "
            "wrong rather than the label -- verify the ID before changing the "
            "label"
        )
    return message


def validate_terms(
    terms: List[Tuple[str, str]],
    adapter_map: Dict[str, Optional[str]],
    resolver: Resolver,
    label_aliases: Optional[Dict[str, Set[str]]] = None,
) -> Tuple[List[str], List[str]]:
    """Validate a list of ``(id, label)`` terms, returning (errors, warnings).

    ``adapter_map`` maps a prefix to an OAK adapter string, to ``None`` (skip
    silently), or omits it (skip with a warning). ``resolver`` performs the
    actual ontology lookup for configured prefixes. ``label_aliases`` adds
    explicitly reviewed labels when the configured ontology snapshot lags the
    authoritative source.
    """
    errors: List[str] = []
    warnings: List[str] = []
    unconfigured_seen: Set[str] = set()

    for curie, label in terms:
        if PTN_ID_RE.match(curie):
            # PTN ancestral nodes share the PANTHER prefix but are not in the
            # PANTHER OBO (which covers families/subfamilies). They get a
            # stronger check than existence in validate_paint_ptns: a declared
            # node must carry real, positive, non-negated PAINT IBD support.
            continue
        prefix = curie.split(":", 1)[0] if ":" in curie else curie
        if prefix not in adapter_map:
            if prefix not in unconfigured_seen:
                unconfigured_seen.add(prefix)
                warnings.append(
                    f"Prefix '{prefix}' (e.g. {curie}) is not in oak_config.yaml; "
                    f"term label not validated"
                )
            continue
        if adapter_map[prefix] is None:
            continue  # explicitly skipped (null), no warning
        status, primary, aliases = resolver(curie)
        if status == "unavailable":
            warnings.append(
                f"Could not consult ontology for {curie} "
                f"(ontology unavailable); label not validated"
            )
            continue
        if status == "not_found":
            errors.append(f"Term id {curie} not found in configured ontology")
            continue
        accepted_aliases = set(aliases)
        if label_aliases:
            accepted_aliases.update(label_aliases.get(curie, set()))
        err = compare_label(curie, label, primary, accepted_aliases)
        if err:
            errors.append(err)

    return errors, warnings


def validate_go_branches(
    terms: List[TypedGoTerm],
    branch_resolver: BranchResolver,
) -> Tuple[List[str], List[str]]:
    """Validate known-slot GO terms against their expected ontology branch."""
    errors: List[str] = []
    warnings: List[str] = []

    for term in terms:
        if not term.curie.startswith("GO:"):
            errors.append(
                f"{term.path}: expected {term.constraint.branch_label} GO term "
                f"under {term.constraint.root_id}, got {term.curie}"
            )
            continue

        status = branch_resolver(term.curie, term.constraint.root_id)
        if status == "ok":
            continue
        if status == "unavailable":
            warnings.append(
                f"Could not consult GO branch hierarchy for {term.curie} at "
                f"{term.path}; branch not validated"
            )
            continue
        if status == "not_found":
            # Term-label validation already reports the missing id; avoid a
            # redundant branch error for the same bad CURIE.
            continue
        errors.append(
            f"{term.path}: expected {term.constraint.branch_label} GO term under "
            f"{term.constraint.root_id}, got {term.curie} ({term.label})"
        )

    return errors, warnings


def validate_taxon_context(doc: object) -> List[str]:
    """Return errors for taxon labels that encode experimental systems."""
    errors: List[str] = []
    for path, descriptor in iter_taxon_descriptors(doc):
        text_fields: List[Tuple[str, str]] = []
        preferred_term = descriptor.get("preferred_term")
        if isinstance(preferred_term, str):
            text_fields.append(("preferred_term", preferred_term))
        term = descriptor.get("term")
        if isinstance(term, dict) and isinstance(term.get("label"), str):
            text_fields.append(("term.label", term["label"]))

        for field_name, text in text_fields:
            if TAXON_EXPERIMENTAL_SYSTEM_RE.search(text):
                errors.append(
                    f"{path}.{field_name}: taxon context must name an in-vivo "
                    f"taxon or clade, not an experimental system/provenance "
                    f"label ({text!r}); put cell-line or assay evidence in "
                    f"evidence statements"
                )
    return errors


def load_oak_adapter_map(
    config_path: Path, project_root: Optional[Path] = None
) -> Dict[str, Optional[str]]:
    """Load the prefix -> adapter mapping from an ``oak_config.yaml``.

    Adapter strings naming a repo-relative artifact (e.g.
    ``simpleobo:interpro/panther/panther.obo``) are rewritten to absolute paths
    so validation works regardless of the caller's working directory.
    """
    with open(config_path) as f:
        data = yaml.safe_load(f) or {}
    adapters = data.get("ontology_adapters", {})
    if project_root is None:
        project_root = Path(__file__).resolve().parents[3]
    return {
        str(k): (None if v is None else _absolutize_adapter(str(v), project_root))
        for k, v in adapters.items()
    }


def _absolutize_adapter(adapter_string: str, project_root: Path) -> str:
    """Resolve a repo-relative artifact path inside an OAK adapter string.

    Only rewrites when the descriptor names a file that actually exists under
    ``project_root``; scheme-only strings such as ``sqlite:obo:go`` or
    ``ols:chebi`` are left untouched.

    >>> _absolutize_adapter("ols:chebi", Path("/repo"))
    'ols:chebi'
    >>> _absolutize_adapter("sqlite:obo:go", Path("/repo"))
    'sqlite:obo:go'
    """
    scheme, separator, descriptor = adapter_string.partition(":")
    if not separator or not descriptor:
        return adapter_string
    candidate = Path(descriptor)
    if candidate.is_absolute():
        return adapter_string
    resolved = project_root / candidate
    if not resolved.exists():
        return adapter_string
    return f"{scheme}:{resolved}"


def load_term_label_aliases(config_path: Path) -> Dict[str, Set[str]]:
    """Load reviewed label aliases used to bridge stale ontology snapshots."""
    with open(config_path) as f:
        data = yaml.safe_load(f) or {}
    raw_aliases = data.get("term_label_aliases", {})
    return {
        str(curie): {str(label) for label in labels}
        for curie, labels in raw_aliases.items()
        if isinstance(labels, list)
    }


def _get_cached_adapter(adapter_string: str):
    """Return a process-wide cached OAK adapter, or None if it cannot load.

    Adapters are cached across files, not per ``validate_module_file`` call: the
    CLI validates hundreds of modules in one process, and re-instantiating an
    adapter each time means re-parsing its backing artifact every file (the
    PANTHER OBO alone is ~14 MB, several seconds a pop). Failures are remembered
    too so a broken/unreachable ontology is not retried once per term.
    """
    from oaklib import get_adapter  # imported lazily; heavy dependency

    if adapter_string in _FAILED_ADAPTERS:
        return None
    if adapter_string not in _ADAPTER_CACHE:
        # External system (ontology download/db): tolerate failures and degrade
        # to "unavailable" rather than crashing the whole run.
        try:
            _ADAPTER_CACHE[adapter_string] = get_adapter(adapter_string)
        except Exception:  # noqa: BLE001 - external system
            _FAILED_ADAPTERS.add(adapter_string)
            return None
    return _ADAPTER_CACHE[adapter_string]


def _build_oak_resolver(adapter_map: Dict[str, Optional[str]]) -> Resolver:
    """Build a resolver backed by real OAK adapters (lazily created, cached).

    Adapter creation and lookups touch external ontology databases, so failures
    (network/download issues) degrade to ``not_found`` would be wrong here;
    instead such terms are treated as resolvable-but-unknown and reported by the
    caller. We keep one adapter per adapter string.
    """
    def get(adapter_string: str):
        return _get_cached_adapter(adapter_string)

    def resolve(curie: str) -> Tuple[str, Optional[str], Set[str]]:
        prefix = curie.split(":", 1)[0]
        adapter_string = adapter_map[prefix]
        assert adapter_string is not None  # routed only for configured prefixes
        adapter = get(adapter_string)
        if adapter is None:
            return ("unavailable", None, set())
        try:  # external system: ontology query may fail transiently
            primary = adapter.label(curie)
            if primary is None:
                return ("not_found", None, set())
            aliases: Set[str] = set()
            # entity_aliases includes synonyms; tolerate adapters lacking it.
            alias_fn = getattr(adapter, "entity_aliases", None)
            if callable(alias_fn):
                aliases = {a for a in alias_fn(curie) if isinstance(a, str)}
            return ("ok", primary, aliases)
        except Exception:  # noqa: BLE001 - external system
            return ("unavailable", None, set())

    return resolve


def _build_go_branch_resolver(adapter_map: Dict[str, Optional[str]]) -> BranchResolver:
    """Build an OAK-backed GO branch resolver for known module slots."""
    adapter_string = adapter_map.get("GO")

    def get_go_adapter():
        if adapter_string is None:
            return None
        return _get_cached_adapter(adapter_string)

    def resolve(curie: str, root_id: str) -> str:
        go_adapter = get_go_adapter()
        if go_adapter is None:
            return "unavailable"
        try:  # external system: ontology query may fail transiently
            if go_adapter.label(curie) is None:
                return "not_found"
            if curie == root_id:
                return "not_in_branch"
            ancestors = set(
                go_adapter.ancestors(curie, predicates=["rdfs:subClassOf"])
            )
            return "ok" if root_id in ancestors else "not_in_branch"
        except Exception:  # noqa: BLE001 - external system
            return "unavailable"

    return resolve


def _build_go_ancestor_resolver(
    adapter_map: Dict[str, Optional[str]],
) -> Optional[GoAncestors]:
    """Build a cached GO ancestor lookup, or None when GO is unavailable."""
    adapter_string = adapter_map.get("GO")
    if adapter_string is None:
        return None
    cache: Dict[str, Set[str]] = {}

    def ancestors(curie: str) -> Set[str]:
        if curie not in cache:
            adapter = _get_cached_adapter(adapter_string)
            if adapter is None:
                return {curie}
            try:  # external system: ontology query may fail transiently
                cache[curie] = set(
                    adapter.ancestors(curie, predicates=["rdfs:subClassOf", "BFO:0000050"])
                )
            except Exception:  # noqa: BLE001 - external system
                return {curie}
        return cache[curie]

    return ancestors


def _unavailable_go_branch_resolver(curie: str, root_id: str) -> str:
    """Offline test helper used when only label resolution is injected."""
    return "unavailable"


def validate_module_file(
    path: Path,
    config_path: Optional[Path] = None,
    resolver: Optional[Resolver] = None,
    branch_resolver: Optional[BranchResolver] = None,
    paint_index: Optional[PaintIndex] = None,
    panther_dir: Optional[Path] = None,
    member_index: Optional[Dict[str, str]] = None,
) -> ModuleValidationResult:
    """Validate term labels in a single module YAML file.

    ``resolver`` may be injected for testing; otherwise a real OAK-backed
    resolver is built from ``config_path`` (defaults to ``conf/oak_config.yaml``
    relative to the repository root). ``paint_index`` may also be injected for
    PTN tests; otherwise local ``interpro/panther`` TSVs are loaded lazily only
    when a module declares ancestral nodes.
    """
    path = Path(path)
    project_root = Path(__file__).resolve().parents[3]
    if config_path is None:
        config_path = project_root / "conf" / "oak_config.yaml"
    adapter_map = load_oak_adapter_map(config_path)
    label_aliases = load_term_label_aliases(config_path)

    with open(path) as f:
        doc = yaml.safe_load(f)

    typed_go_terms = list(iter_typed_go_terms(doc))
    resolver_was_injected = resolver is not None
    if resolver is None:
        resolver = _build_oak_resolver(adapter_map)

    if member_index is None:
        member_index = load_member_index(
            project_root / "interpro" / "panther" / "panther-members.tsv"
        )
    if paint_index is None:
        if panther_dir is None:
            panther_dir = project_root / "interpro" / "panther"
        paint_index = load_paint_index(panther_dir)

    member_errors, member_warnings = validate_family_members(
        list(iter_family_member_uses(doc)),
        member_index,
        paint_index,
        subfamily_counts=load_subfamily_counts(
            project_root / "interpro" / "panther" / "panther.obo"
        ),
    )

    terms = list(iter_terms(doc))
    errors, warnings = validate_terms(terms, adapter_map, resolver, label_aliases)
    errors.extend(member_errors)
    warnings.extend(member_warnings)
    errors.extend(validate_taxon_context(doc))
    if branch_resolver is None:
        branch_resolver = (
            _unavailable_go_branch_resolver
            if resolver_was_injected
            else _build_go_branch_resolver(adapter_map)
        )
    branch_errors, branch_warnings = validate_go_branches(
        typed_go_terms, branch_resolver
    )
    errors.extend(branch_errors)
    warnings.extend(branch_warnings)

    ptn_uses = list(iter_ancestral_node_uses(doc))
    cited_ptns = list(iter_cited_ptn_sources(doc))
    if ptn_uses or cited_ptns:
        ptn_errors, ptn_warnings = validate_paint_ptns(
            ptn_uses, paint_index, _build_go_ancestor_resolver(adapter_map)
        )
        errors.extend(ptn_errors)
        warnings.extend(ptn_warnings)
        errors.extend(
            validate_cited_ptn_sources(
                cited_ptns,
                paint_index,
                load_goa_attested_ptns(project_root / "genes"),
            )
        )


    # Conformance: verify every `conforms_to` bundle against its template motif.
    # Templates are sibling module files, so they are resolved from the file's
    # own directory. Errors block; warnings/info are advisory.
    conformance_errors, conformance_warnings = validate_conformance(doc, path.parent)
    errors.extend(conformance_errors)
    warnings.extend(conformance_warnings)

    # Reaction chaining: advisory only (never blocks). A `chaining_status`
    # override on a connection acknowledges a known gap and suppresses its
    # warning. Resolution touches the GO/RHEA ontology DBs, so it degrades to
    # "no findings" when those are unavailable.
    warnings.extend(validate_chaining(doc))

    # Reference titles: every literature reference (PMID/DOI ``id``/``source_id``
    # paired with a ``title``) must match the fetched/cached publication title
    # (normalized). Mismatches block; unfetchable references degrade to warnings.
    title_errors, title_warnings = validate_reference_titles(doc)
    errors.extend(title_errors)
    warnings.extend(title_warnings)

    # Supporting-text snippets: every EvidenceItem literature quote (PMID/DOI
    # source_id paired with supporting_text) must be a verbatim (normalized)
    # substring of the cached publication. Mismatches block; unfetchable or
    # uncached references degrade to advisory warnings.
    st_errors, st_warnings = validate_supporting_text(doc)
    errors.extend(st_errors)
    warnings.extend(st_warnings)

    return ModuleValidationResult(path=path, errors=errors, warnings=warnings)


# Literature source_id prefixes whose supporting_text quotes are checked
# verbatim against a cached publication. Everything else (GO, file:, PANTHER,
# Reactome, UniProtKB, ...) is provenance grounding, not a fetchable quote.
_LITERATURE_PREFIXES = {"PMID", "DOI"}


def iter_evidence_snippets(obj: object) -> Iterator[Tuple[str, str]]:
    """Yield ``(source_id, supporting_text)`` for every EvidenceItem-like dict.

    An EvidenceItem is recognised structurally as any mapping carrying both a
    ``source_id`` and a non-empty ``supporting_text``. Only literature sources
    (``PMID:``/``DOI:``) are yielded, since only those have a fetchable text to
    check the quote against.

    >>> doc = {"evidence": [{"source_id": "PMID:1", "supporting_text": "x"},
    ...                     {"source_id": "GO:0001", "supporting_text": "y"}]}
    >>> list(iter_evidence_snippets(doc))
    [('PMID:1', 'x')]
    """
    if isinstance(obj, dict):
        source_id = obj.get("source_id")
        supporting_text = obj.get("supporting_text")
        if (
            isinstance(source_id, str)
            and isinstance(supporting_text, str)
            and supporting_text.strip()
        ):
            prefix = source_id.split(":", 1)[0].upper()
            if prefix in _LITERATURE_PREFIXES:
                yield (source_id, supporting_text)
        for value in obj.values():
            yield from iter_evidence_snippets(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_evidence_snippets(item)


def iter_reference_titles(obj: object) -> Iterator[Tuple[str, str]]:
    """Yield ``(reference_id, title)`` for every literature reference with a title.

    A reference is any mapping carrying a literature identifier -- ``id`` (top
    level ``references:`` list) or ``source_id`` (inline ``EvidenceItem``) with a
    ``PMID:``/``DOI:`` prefix -- alongside a non-empty ``title``. Non-literature
    ids (``GO:``, ``file:``, ``PANTHER:``, local node ids, ``MODULE:...``) are
    ignored: they have no fetchable publication title to check against.

    >>> doc = {"references": [{"id": "PMID:1", "title": "A"}],
    ...        "module": {"id": "notch", "label": "Notch",
    ...                   "evidence": [{"source_id": "GO:1", "title": "grounding"}]}}
    >>> list(iter_reference_titles(doc))
    [('PMID:1', 'A')]
    """
    if isinstance(obj, dict):
        ref_id = obj.get("id") or obj.get("source_id")
        title = obj.get("title")
        if (
            isinstance(ref_id, str)
            and isinstance(title, str)
            and title.strip()
            and ref_id.split(":", 1)[0].upper() in _LITERATURE_PREFIXES
        ):
            yield (ref_id, title)
        for value in obj.values():
            yield from iter_reference_titles(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_reference_titles(item)


def _build_supporting_text_validator(publications_dir: Optional[Path]):
    """Build linkml-reference-validator's SupportingTextValidator over the cache.

    Returns ``(validator, publications_dir)`` or ``(None, publications_dir)`` when
    the optional dependency is not installed, so callers degrade gracefully.
    """
    if publications_dir is None:
        publications_dir = Path(__file__).resolve().parents[3] / "publications"
    try:
        from linkml_reference_validator.models import ReferenceValidationConfig
        from linkml_reference_validator.validation.supporting_text_validator import (
            SupportingTextValidator,
        )
    except ImportError:
        return None, publications_dir
    config = ReferenceValidationConfig(
        cache_dir=publications_dir,
        fetch_full_text=False,
    )
    return SupportingTextValidator(config), publications_dir


def _is_unfetchable(message: str) -> bool:
    """True when a validation failure is a fetch/availability problem, not a mismatch."""
    lowered = message.lower()
    return "could not fetch" in lowered or "no records found" in lowered


def validate_supporting_text(
    doc: object,
    publications_dir: Optional[Path] = None,
) -> Tuple[List[str], List[str]]:
    """Verify every EvidenceItem literature quote against the cached publication.

    Uses ``linkml-reference-validator``'s own ``SupportingTextValidator`` (the
    same normalize + deterministic-substring matcher gene reviews use), reading
    from the ``publications/`` cache. Returns ``(errors, warnings)``:

    - a quote that is not a substring of the fetched/cached publication is an
      **error** (blocks validation);
    - a reference that cannot be fetched or is not cached is a **warning**
      (advisory, so offline/rate-limited runs do not hard-fail).

    The check is a no-op (returns empty) when the reference validator is not
    installed, so it degrades gracefully.
    """
    if not isinstance(doc, dict):
        return [], []
    snippets = list(iter_evidence_snippets(doc))
    if not snippets:
        return [], []

    validator, _ = _build_supporting_text_validator(publications_dir)
    if validator is None:
        return [], []

    errors: List[str] = []
    warnings: List[str] = []
    for source_id, supporting_text in snippets:
        try:
            result = validator.validate(supporting_text, source_id)
        except Exception as exc:  # noqa: BLE001 - external publication service
            warnings.append(
                f"Supporting text unverified ({source_id}): fetch failed: "
                f"{type(exc).__name__}: {exc}"
            )
            continue
        if result.is_valid:
            continue
        message = str(getattr(result, "message", "") or "")
        if _is_unfetchable(message):
            warnings.append(f"Supporting text unverified ({source_id}): {message}")
        else:
            errors.append(f"Supporting text mismatch ({source_id}): {message}")
    return errors, warnings


def validate_reference_titles(
    doc: object,
    publications_dir: Optional[Path] = None,
) -> Tuple[List[str], List[str]]:
    """Verify every literature reference title against the cited publication.

    For each ``PMID:``/``DOI:`` reference that carries a ``title`` (in the top
    level ``references:`` list or an inline ``EvidenceItem``), the title is
    compared (normalized) with the fetched/cached publication title using the
    same matcher gene reviews use. Returns ``(errors, warnings)``:

    - a title that does not match the publication is an **error** (blocks;
      catches wrong PMIDs and stale/abbreviated titles);
    - a reference that cannot be fetched or is not cached is a **warning**.

    A no-op when the reference validator is not installed.
    """
    if not isinstance(doc, dict):
        return [], []
    refs = list(dict.fromkeys(iter_reference_titles(doc)))  # de-dupe, keep order
    if not refs:
        return [], []

    validator, _ = _build_supporting_text_validator(publications_dir)
    if validator is None:
        return [], []

    errors: List[str] = []
    warnings: List[str] = []
    for ref_id, title in refs:
        try:
            result = validator.validate_title(ref_id, title)
        except Exception as exc:  # noqa: BLE001 - external publication service
            warnings.append(
                f"Reference title unverified ({ref_id}): fetch failed: "
                f"{type(exc).__name__}: {exc}"
            )
            continue
        if result.is_valid:
            continue
        message = str(getattr(result, "message", "") or "")
        if _is_unfetchable(message):
            warnings.append(f"Reference title unverified ({ref_id}): {message}")
        else:
            errors.append(f"Reference title mismatch ({ref_id}): {message}")
    return errors, warnings


def validate_chaining(doc: object) -> List[str]:
    """Return advisory chaining warnings for a module document.

    Only ``warning``-severity findings are surfaced (an unacknowledged break
    where the upstream reaction's product is not the downstream substrate).
    ``info`` findings -- verified continuity or an acknowledged ``chaining_status``
    gap -- are not reported. This check NEVER produces errors.
    """
    from ai_gene_review.module_qc import reaction_chaining_findings

    if not isinstance(doc, dict):
        return []
    return [
        f"Reaction chaining: {f['message']}"
        for f in reaction_chaining_findings(doc)
        if f.get("severity") == "warning"
    ]


def validate_conformance(doc: object, modules_dir: Path) -> Tuple[List[str], List[str]]:
    """Check every ``conforms_to`` bundle against its template motif.

    Returns ``(errors, warnings)`` where ``error``-severity conformance
    violations block validation and ``warning``/``info`` ones are advisory.
    Templates are resolved relative to ``modules_dir`` (the document's own
    directory, since template motifs are sibling module files).
    """
    # Imported here to avoid a heavy import at module load and any import cycle.
    from ai_gene_review.module_qc import conformance_violations

    if not isinstance(doc, dict):
        return [], []

    errors: List[str] = []
    warnings: List[str] = []
    for violation in conformance_violations(doc, modules_dir=modules_dir):
        message = (
            f"Conformance [{violation['node_id']} -> {violation['template']}]: "
            f"{violation['message']}"
        )
        if violation["severity"] == "error":
            errors.append(message)
        else:
            warnings.append(message)
    return errors, warnings


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point: validate one or more module files. Returns exit code."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate module (ModuleReview) YAML term labels, GO branches, and conformance."
    )
    parser.add_argument("files", nargs="+", type=Path, help="Module YAML files")
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=None,
        help="Path to oak_config.yaml (default: conf/oak_config.yaml)",
    )
    args = parser.parse_args(argv)

    exit_code = 0
    ungrounded = 0
    for path in args.files:
        with open(path) as handle:
            ungrounded += count_ungrounded_families(yaml.safe_load(handle))
        result = validate_module_file(path, config_path=args.config)
        for w in result.warnings:
            print(f"⚠️  WARN  {path}: {w}")
        for e in result.errors:
            print(f"❌ ERROR {path}: {e}")
        if result.is_valid:
            print(f"✅ {path}: term labels OK ({len(result.warnings)} warnings)")
        else:
            exit_code = 1

    if ungrounded:
        print(
            f"ℹ️  {ungrounded} family descriptor(s) name representative members but "
            "assert no PANTHER id (correct when the family cannot be established)"
        )
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
