"""Check that a module's concrete exemplars fit the process the module asserts.

The function check (``module_function_conformance``) compares an annoton's
molecular function with its exemplar. That misses an exemplar whose activity is
right and whose pathway is wrong: ADRB2, a Gs-coupled receptor, does have G
protein-coupled receptor activity, so it passed as the exemplar of a "Gq-coupled
receptor" annoton in a PLC-activating GPCR signaling module.

This check compares each exemplar's GOA biological-process rows with the process
its annoton sits under: the annoton's own ``processes`` when stated, otherwise
the GO process concepts of the nearest enclosing node that has any.

- ``PROCESS_SUPPORTED``: a positive GOA row at or under the expected process.
- ``PROCESS_SUPPORTED_BY_REVIEW``: no such GOA row, but the gene's own review
  asserts the process: a retained or ``NEW`` annotation, the replacement term of
  a ``MODIFY``, or a core function's ``directly_involved_in``. GOA lags the
  reviews, and a process the review already adds is not an exemplar problem.
- ``PROCESS_NOT_ANNOTATED``: none. Informational only, because downstream
  members of a pathway often lack the pathway term.
- ``SIBLING_PROCESS_ONLY``: none, and an experimental row under a sibling of the
  expected process (a term below one of its direct parents that is neither above
  nor below it). This is the ADRB2 shape. It is a warning only when the annoton's
  function is a signaling receptor or receptor ligand activity, because those
  participants decide which pathway a module is. Elsewhere it is informational:
  over the corpus most such rows are shared downstream components (GRB2 or JAK1
  in a receptor-specific module) whose GOA rows simply do not name that pathway.
- ``GOA_UNAVAILABLE``: the exemplar has no local GOA file.

A GOA row is a lead for choosing an exemplar, never evidence that a module claim
is true or false: annotation is incomplete, and a protein can act in two sibling
pathways. The check therefore never produces an error.
"""

from __future__ import annotations

import csv

import yaml
from yaml import CSafeLoader
from collections import Counter
from dataclasses import dataclass
from functools import cached_property, lru_cache
from pathlib import Path
from typing import Any, Callable, Iterator

from ai_gene_review.module_qc import as_list, base_accession, index_gene_reviews

TermSetLookup = Callable[[str], frozenset[str]]

BIOLOGICAL_PROCESS = "GO:0008150"
# Activities whose bearer determines which pathway is being described.
PATHWAY_DEFINING_FUNCTIONS = frozenset({"GO:0038023", "GO:0048018"})
IS_A = "rdfs:subClassOf"
PART_OF = "BFO:0000050"
# Evidence a curator read in a paper about this gene product. A sibling process
# known only by propagation or prediction is not grounds for a warning.
EXPERIMENTAL_CODES = frozenset(
    {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
)


@dataclass(frozen=True)
class GoProcessGraph:
    """The two GO lookups the check needs, injectable for tests.

    ``ancestors`` returns every is-a and part-of ancestor of a term, without the
    term itself. ``parents`` returns its direct is-a parents.
    """

    ancestors: TermSetLookup
    parents: TermSetLookup

    def is_at_or_under(self, term: str, ancestor: str) -> bool:
        """Whether ``term`` is ``ancestor`` or one of its descendants.

        >>> graph = GoProcessGraph(
        ...     ancestors=lambda t: frozenset({"GO:2"}) if t == "GO:1" else frozenset(),
        ...     parents=lambda t: frozenset(),
        ... )
        >>> graph.is_at_or_under("GO:1", "GO:2"), graph.is_at_or_under("GO:2", "GO:1")
        (True, False)
        >>> graph.is_at_or_under("GO:1", "GO:1")
        True
        """
        return term == ancestor or ancestor in self.ancestors(term)

    def is_sibling_branch(self, term: str, expected: str) -> bool:
        """Whether ``term`` lies below a direct parent of ``expected`` but off its line.

        >>> up = {"GO:plc": {"GO:gpcr"}, "GO:camp": {"GO:gpcr"}, "GO:gpcr": set()}
        >>> graph = GoProcessGraph(
        ...     ancestors=lambda t: frozenset(up.get(t, ())),
        ...     parents=lambda t: frozenset(up.get(t, ())),
        ... )
        >>> graph.is_sibling_branch("GO:camp", "GO:plc")
        True
        >>> graph.is_sibling_branch("GO:gpcr", "GO:plc")
        False
        """
        if self.is_at_or_under(term, expected) or self.is_at_or_under(expected, term):
            return False
        return bool(self.parents(expected) & self.ancestors(term))


class OakGoProcessGraph:
    """Lazy GO lookups over the SQLite GO snapshot, with a cached, reported failure.

    The lookups read the snapshot's ``entailed_edge`` (precomputed closure) and
    ``edge`` tables directly. Going through ``adapter.ancestors`` gives the same
    sets but walks the graph per term, which costs minutes over the whole module
    corpus. An adapter that is not SQL-backed is reported as a failure, not
    silently treated as an empty ontology.
    """

    _ANCESTORS = (
        "SELECT DISTINCT object FROM entailed_edge WHERE subject = :term "
        f"AND predicate IN ('{IS_A}', '{PART_OF}')"
    )
    _PARENTS = f"SELECT object FROM edge WHERE subject = :term AND predicate = '{IS_A}'"

    _LABEL = "SELECT value FROM rdfs_label_statement WHERE subject = :term"

    def __init__(self, adapter_string: str | None):
        self.adapter_string = adapter_string
        self.failure: str | None = None

    @cached_property
    def session(self) -> Any:
        """Open the snapshot once; record a failure and stop trying."""
        if self.adapter_string is None:
            return None
        from oaklib import get_adapter

        try:
            adapter = get_adapter(self.adapter_string)
        except Exception as error:  # External ontology construction can fail.
            self.failure = f"GO adapter could not be loaded ({type(error).__name__})."
            return None
        session = getattr(adapter, "session", None)
        if session is None:
            self.failure = "GO adapter is not SQL-backed; process fit was not checked."
        return session

    def _objects(self, query: str, curie: str) -> frozenset[str]:
        """Run one single-term lookup, excluding the term itself."""
        if self.failure or self.session is None:
            return frozenset()
        from sqlalchemy import text

        try:
            found = {
                row[0] for row in self.session.execute(text(query), {"term": curie})
            }
        except Exception as error:  # External ontology queries can also fail.
            self.failure = f"GO lookup failed ({type(error).__name__})."
            return frozenset()
        return frozenset(found) - {curie}

    @lru_cache(maxsize=65536)
    def ancestors(self, curie: str) -> frozenset[str]:
        """Is-a and part-of ancestors, excluding the term itself."""
        return self._objects(self._ANCESTORS, curie)

    @lru_cache(maxsize=65536)
    def parents(self, curie: str) -> frozenset[str]:
        """Direct is-a parents."""
        return self._objects(self._PARENTS, curie)

    @lru_cache(maxsize=65536)
    def label(self, curie: str) -> str | None:
        """The term's label, or None when it is unknown or the lookup failed."""
        if self.failure or self.session is None:
            return None
        from sqlalchemy import text

        try:
            row = self.session.execute(text(self._LABEL), {"term": curie}).first()
        except Exception as error:  # External ontology queries can also fail.
            self.failure = f"GO lookup failed ({type(error).__name__})."
            return None
        return row[0] if row else None

    @cached_property
    def graph(self) -> GoProcessGraph:
        """The lookups in the form the check consumes."""
        return GoProcessGraph(ancestors=self.ancestors, parents=self.parents)


@lru_cache(maxsize=8)
def oak_go_process_graph(
    adapter_string: str | None = "sqlite:obo:go",
) -> OakGoProcessGraph:
    """Share one lazy GO graph across the modules of a run."""
    return OakGoProcessGraph(adapter_string)


@lru_cache(maxsize=4096)
def load_goa_process_rows(goa_path: Path) -> tuple[tuple[str, str], ...]:
    """Read the positive biological-process rows of a ``GENE-goa.tsv`` file.

    Returns ``(GO id, evidence code)`` pairs. NOT rows are dropped: a negated row
    is not support, and whether it disputes a module is a separate question.
    """
    rows: list[tuple[str, str]] = []
    with goa_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row.get("GO ASPECT") != "biological_process":
                continue
            if "NOT" in (row.get("QUALIFIER") or "").split("|"):
                continue
            term = row.get("GO TERM")
            if term:
                rows.append((term, row.get("GO EVIDENCE CODE") or ""))
    return tuple(rows)


# Review actions that leave the annotated term standing as a claim about the gene.
_RETAINED_ACTIONS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "TOO_GENERAL"})


@lru_cache(maxsize=4096)
def load_review_asserted_terms(review_path: Path) -> frozenset[str]:
    """GO terms a gene review asserts of the gene, whatever GOA currently holds.

    Collects the term of every retained, non-negated annotation, the replacement
    terms of every ``MODIFY``, and each core function's ``directly_involved_in``.
    Terms of every aspect are returned; the caller keeps those under a process.
    """
    data = yaml.load(review_path.read_text(encoding="utf-8"), Loader=CSafeLoader)
    if not isinstance(data, dict):
        return frozenset()
    terms: set[str] = set()
    for annotation in as_list(data.get("existing_annotations")):
        if not isinstance(annotation, dict) or annotation.get("negated"):
            continue
        review = annotation.get("review")
        review = review if isinstance(review, dict) else {}
        action = review.get("action")
        if action in _RETAINED_ACTIONS:
            terms.update(_go_ids([annotation]))
        elif action == "MODIFY":
            for replacement in as_list(review.get("proposed_replacement_terms")):
                if isinstance(replacement, dict):
                    terms.update(_go_ids([{"term": replacement}]))
    for core in as_list(data.get("core_functions")):
        if isinstance(core, dict):
            for process in as_list(core.get("directly_involved_in")):
                if isinstance(process, dict):
                    terms.update(_go_ids([{"term": process}]))
    return frozenset(terms)


def _go_ids(holders: Any) -> list[str]:
    """GO ids of a list of descriptor holders (``concepts`` or ``processes``)."""
    ids: list[str] = []
    for holder in as_list(holders):
        term = holder.get("term") if isinstance(holder, dict) else None
        curie = term.get("id") if isinstance(term, dict) else None
        if isinstance(curie, str) and curie.startswith("GO:"):
            ids.append(curie)
    return ids


def _exemplars(participant: Any) -> Iterator[tuple[dict[str, Any], str]]:
    """Concrete proteins named by a participant, with how each was named.

    The scope is ``member`` for a protein that is itself the participant and
    ``family_representative`` for one a curator chose to illustrate a family.
    """
    if not isinstance(participant, dict):
        return
    for key in ("gene", "gene_product"):
        holder = participant.get(key)
        if isinstance(holder, dict):
            yield holder, "member"
    family = participant.get("family")
    if isinstance(family, dict):
        for member in as_list(family.get("representative_members")):
            if isinstance(member, dict):
                yield member, "family_representative"
    complex_holder = participant.get("protein_complex")
    if isinstance(complex_holder, dict):
        for unit in as_list(complex_holder.get("active_units")):
            if isinstance(unit, dict):
                yield from _exemplars(unit.get("participant"))


def _annotons_with_expected(
    node: Any, inherited: list[str], graph: GoProcessGraph
) -> Iterator[tuple[dict[str, Any], list[str]]]:
    """Yield each annoton with the processes it is expected to take part in."""
    if not isinstance(node, dict):
        return
    own = [
        c
        for c in _go_ids(node.get("concepts"))
        if BIOLOGICAL_PROCESS in graph.ancestors(c)
    ]
    expected = own or inherited
    for annoton in as_list(node.get("annotons")):
        if isinstance(annoton, dict):
            stated = _go_ids(annoton.get("processes"))
            yield annoton, stated or expected
    for part in as_list(node.get("parts")):
        if isinstance(part, dict):
            yield from _annotons_with_expected(part.get("node"), expected, graph)
    for variant_set in as_list(node.get("variant_sets")):
        if isinstance(variant_set, dict):
            for variant in as_list(variant_set.get("variants")):
                yield from _annotons_with_expected(variant, expected, graph)


def _is_pathway_defining(annoton: dict[str, Any], graph: GoProcessGraph) -> bool:
    """Whether the annoton's function is a receptor or receptor-ligand activity."""
    function = annoton.get("function")
    curie = _go_ids([function])[0] if _go_ids([function]) else None
    if curie is None:
        return False
    return bool(PATHWAY_DEFINING_FUNCTIONS & ({curie} | graph.ancestors(curie)))


def _assess(
    rows: tuple[tuple[str, str], ...],
    expected: list[str],
    graph: GoProcessGraph,
    pathway_defining: bool,
) -> tuple[str, str, list[str]]:
    """Classify one exemplar's process rows against the expected processes."""
    if any(graph.is_at_or_under(term, want) for term, _ in rows for want in expected):
        return "PROCESS_SUPPORTED", "info", []
    siblings = sorted(
        {
            term
            for term, evidence in rows
            if evidence in EXPERIMENTAL_CODES
            and any(graph.is_sibling_branch(term, want) for want in expected)
        }
    )
    if siblings:
        return (
            "SIBLING_PROCESS_ONLY",
            "warning" if pathway_defining else "info",
            siblings,
        )
    return "PROCESS_NOT_ANNOTATED", "info", []


def _message(status: str, expected: list[str], siblings: list[str]) -> str:
    """Explain a status in terms a curator can act on."""
    wanted = ", ".join(expected)
    if status == "SIBLING_PROCESS_ONLY":
        return (
            f"GOA has no annotation of this exemplar at or under {wanted}, but has "
            f"experimental annotation under a sibling process ({', '.join(siblings)}). "
            "Check that the exemplar belongs in this branch; GOA is a lead here, "
            "not proof that the choice is wrong."
        )
    if status == "PROCESS_SUPPORTED_BY_REVIEW":
        return (
            f"GOA has no annotation of this exemplar at or under {wanted}, but its "
            "gene review asserts the process."
        )
    if status == "PROCESS_NOT_ANNOTATED":
        return f"GOA has no annotation of this exemplar at or under {wanted}."
    if status == "GOA_UNAVAILABLE":
        return "No local GOA file for this exemplar; process fit was not checked."
    return f"GOA annotates this exemplar at or under {wanted}."


def module_process_conformance(
    data: dict[str, Any],
    *,
    gene_index: dict[str, Path] | None = None,
    genes_dir: Path = Path("genes"),
    graph: GoProcessGraph | None = None,
) -> dict[str, Any]:
    """Compare every concrete exemplar with the process its annoton sits under.

    ``gene_index`` maps a base UniProt accession to its gene review path; the GOA
    file is read from the same folder. ``graph`` may be injected for tests;
    otherwise the local GO snapshot is used, and a failure to load it yields no
    rows and a ``failure`` message instead of false negatives.
    """
    oak: OakGoProcessGraph | None = None
    if graph is None:
        oak = oak_go_process_graph()
        graph = oak.graph
    if gene_index is None:
        gene_index = index_gene_reviews(genes_dir)

    rows: list[dict[str, Any]] = []
    for annoton, expected in _annotons_with_expected(data.get("module"), [], graph):
        if not expected:
            continue
        seen: set[str] = set()
        pathway_defining = _is_pathway_defining(annoton, graph)
        # Whether the annoton names the process itself or inherits a node concept.
        process_source = "annoton" if _go_ids(annoton.get("processes")) else "node"
        evidence_ids = [
            str(item["source_id"])
            for item in as_list(annoton.get("evidence"))
            if isinstance(item, dict) and item.get("source_id")
        ]
        for exemplar, scope in _exemplars(annoton.get("participant")):
            term = exemplar.get("term")
            curie = term.get("id") if isinstance(term, dict) else None
            accession = base_accession(curie) if isinstance(curie, str) else None
            if (
                not accession
                or not str(curie).startswith("UniProtKB:")
                or accession in seen
            ):
                continue
            seen.add(accession)
            review_path = gene_index.get(accession)
            goa_path = (
                review_path.parent
                / review_path.name.replace("-ai-review.yaml", "-goa.tsv")
                if review_path is not None
                else None
            )
            siblings: list[str]
            if goa_path is None or not goa_path.exists():
                status, severity, siblings = "GOA_UNAVAILABLE", "info", []
            else:
                status, severity, siblings = _assess(
                    load_goa_process_rows(goa_path), expected, graph, pathway_defining
                )
                if status != "PROCESS_SUPPORTED" and review_path is not None:
                    asserted = load_review_asserted_terms(review_path)
                    if any(
                        graph.is_at_or_under(term, want)
                        for term in asserted
                        for want in expected
                    ):
                        status, severity, siblings = (
                            "PROCESS_SUPPORTED_BY_REVIEW",
                            "info",
                            [],
                        )
            rows.append(
                {
                    "annoton_id": str(annoton.get("id") or ""),
                    "participant_id": curie,
                    "participant_label": exemplar.get("preferred_term"),
                    "scope": scope,
                    "pathway_defining": pathway_defining,
                    "process_source": process_source,
                    "evidence_ids": evidence_ids,
                    "review_path": review_path.as_posix() if review_path else None,
                    "expected_process_ids": expected,
                    "sibling_process_ids": siblings,
                    "status": status,
                    "severity": severity,
                    "message": _message(status, expected, siblings),
                }
            )
    failure = oak.failure if oak is not None else None
    if failure:
        rows = []
    return {
        "rows": rows,
        "counts": dict(Counter(row["status"] for row in rows)),
        "total": len(rows),
        "warnings": sum(row["severity"] == "warning" for row in rows),
        "failure": failure,
    }
