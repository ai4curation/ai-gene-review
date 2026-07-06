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

For PANTHER/PAINT ancestral nodes declared in ``family.ancestral_nodes``, this
validator checks local ``interpro/panther/*/*-paint.tsv`` slices directly: a
declared PTN must be a well-formed exact PTN id and must have a positive,
non-negated IBD row. GO overlap, family consistency, GO_REF evidence, and
representative seed overlap are currently advisory warnings so the validator can
surface curation drift without making module validation brittle.

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
    if isinstance(obj, dict):
        for key, value in obj.items():
            if (
                key == "term"
                and isinstance(value, dict)
                and isinstance(value.get("id"), str)
                and isinstance(value.get("label"), str)
            ):
                yield (value["id"], value["label"])
            if key == "family_terms":
                for item in _as_list(value):
                    if (
                        isinstance(item, dict)
                        and isinstance(item.get("id"), str)
                        and isinstance(item.get("label"), str)
                    ):
                        yield (item["id"], item["label"])
            yield from iter_terms(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_terms(item)


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

    The GO assertions collected here are intentionally *nearby* module
    assertions: direct typed slots on enclosing annotons, complex units, or
    protein-complex descriptors. They are used only for advisory PTN/GO overlap
    warnings, not as hard validation.
    """
    if isinstance(obj, dict):
        ancestral_nodes = obj.get("ancestral_nodes")
        if isinstance(ancestral_nodes, list):
            family_curie = _direct_family_curie(obj)
            family_term_curies = _family_term_curies(obj)
            representative_accessions = _representative_uniprot_accessions(obj)

            asserted_terms: List[ModuleGoAssertion] = []
            seen_assertions: Set[Tuple[str, str, str]] = set()
            for ancestor_path, ancestor in reversed(ancestors):
                for assertion in _iter_direct_go_assertions(ancestor, ancestor_path):
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


def validate_paint_ptns(
    uses: List[AncestralNodeUse],
    paint_index: PaintIndex,
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
            exact_matches = [
                assertion
                for assertion in use.asserted_go_terms
                if (assertion.aspect, assertion.curie) in supported
            ]
            if not exact_matches:
                asserted = {
                    f"{assertion.aspect}:{assertion.curie}"
                    for assertion in use.asserted_go_terms
                }
                ibd_terms = {f"{aspect}:{go_id}" for aspect, go_id in supported}
                warnings.append(
                    f"{use.path}: {use.ptn_curie} has no exact GO overlap with "
                    f"nearby module GO assertions ({_format_limited(asserted)}); "
                    f"positive IBD rows support {_format_limited(ibd_terms)}"
                )

        if use.representative_uniprot_accessions:
            seed_accessions: Set[str] = set()
            for row in positive_ibd_rows:
                seed_accessions.update(row.uniprot_seed_accessions)
            if not seed_accessions.intersection(use.representative_uniprot_accessions):
                warnings.append(
                    f"{use.path}: no representative UniProtKB accession "
                    f"({_format_limited(set(use.representative_uniprot_accessions))}) "
                    f"appears among IBD seed UniProtKB accessions "
                    f"({_format_limited(seed_accessions) or 'none'})"
                )

    return errors, warnings


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
    return (
        f"Label mismatch for {curie}: module says '{provided}' "
        f"but ontology label is '{shown}'"
    )


def validate_terms(
    terms: List[Tuple[str, str]],
    adapter_map: Dict[str, Optional[str]],
    resolver: Resolver,
) -> Tuple[List[str], List[str]]:
    """Validate a list of ``(id, label)`` terms, returning (errors, warnings).

    ``adapter_map`` maps a prefix to an OAK adapter string, to ``None`` (skip
    silently), or omits it (skip with a warning). ``resolver`` performs the
    actual ontology lookup for configured prefixes.
    """
    errors: List[str] = []
    warnings: List[str] = []
    unconfigured_seen: Set[str] = set()

    for curie, label in terms:
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
        err = compare_label(curie, label, primary, aliases)
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


def load_oak_adapter_map(config_path: Path) -> Dict[str, Optional[str]]:
    """Load the prefix -> adapter mapping from an ``oak_config.yaml``."""
    with open(config_path) as f:
        data = yaml.safe_load(f) or {}
    adapters = data.get("ontology_adapters", {})
    return {str(k): (None if v is None else str(v)) for k, v in adapters.items()}


def _build_oak_resolver(adapter_map: Dict[str, Optional[str]]) -> Resolver:
    """Build a resolver backed by real OAK adapters (lazily created, cached).

    Adapter creation and lookups touch external ontology databases, so failures
    (network/download issues) degrade to ``not_found`` would be wrong here;
    instead such terms are treated as resolvable-but-unknown and reported by the
    caller. We keep one adapter per adapter string.
    """
    from oaklib import get_adapter  # imported lazily; heavy dependency

    cache: Dict[str, object] = {}
    # Adapter strings that failed to load are remembered so we don't retry (and
    # re-log) them per term.
    failed: Set[str] = set()

    def get(adapter_string: str):
        if adapter_string in failed:
            return None
        if adapter_string not in cache:
            # External system (ontology download/db): tolerate failures and
            # degrade to "unavailable" rather than crashing the whole run.
            try:
                cache[adapter_string] = get_adapter(adapter_string)
            except Exception:  # noqa: BLE001 - external system
                failed.add(adapter_string)
                return None
        return cache[adapter_string]

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
    from oaklib import get_adapter  # imported lazily; heavy dependency

    adapter_string = adapter_map.get("GO")
    adapter = None
    adapter_failed = False

    def get_go_adapter():
        nonlocal adapter, adapter_failed
        if adapter_failed:
            return None
        if adapter is None:
            if adapter_string is None:
                adapter_failed = True
                return None
            try:
                adapter = get_adapter(adapter_string)
            except Exception:  # noqa: BLE001 - external system
                adapter_failed = True
                return None
        return adapter

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

    with open(path) as f:
        doc = yaml.safe_load(f)

    terms = list(iter_terms(doc))
    typed_go_terms = list(iter_typed_go_terms(doc))
    resolver_was_injected = resolver is not None
    if resolver is None:
        resolver = _build_oak_resolver(adapter_map)
    errors, warnings = validate_terms(terms, adapter_map, resolver)
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
    if ptn_uses:
        if paint_index is None:
            if panther_dir is None:
                panther_dir = project_root / "interpro" / "panther"
            paint_index = load_paint_index(panther_dir)
        ptn_errors, ptn_warnings = validate_paint_ptns(ptn_uses, paint_index)
        errors.extend(ptn_errors)
        warnings.extend(ptn_warnings)

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

    return ModuleValidationResult(path=path, errors=errors, warnings=warnings)


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
    for path in args.files:
        result = validate_module_file(path, config_path=args.config)
        for w in result.warnings:
            print(f"⚠️  WARN  {path}: {w}")
        for e in result.errors:
            print(f"❌ ERROR {path}: {e}")
        if result.is_valid:
            print(f"✅ {path}: term labels OK ({len(result.warnings)} warnings)")
        else:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
