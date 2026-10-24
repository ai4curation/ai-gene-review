"""Join propagated GOA rows with donor-side facts, target context and reviews.

Every value here is derived from files on disk: the GOA cache, the gene review
YAML, and the donor cache written by
:mod:`ai_gene_review.tools.refresh_propagation_sources`. Nothing is fetched.
Where a donor was not resolved or not checked the row says so; it never
guesses a donor's identity or support.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

import yaml

from ai_gene_review.export.propagation_rows import (
    DONOR_EVIDENCE,
    EXPERIMENTAL,
    PREFIX_SPECIES,
    PropagatedRow,
    iter_propagated_rows,
    iter_target_evidence,
)

_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

DEFAULT_DATA_DIR = Path("projects/HOMOLOGY_PROPAGATION/data")

#: Row-level donor support, strongest first.
SUPPORT_ORDER = ["EXPERIMENTAL", "INFERRED_ONLY", "ABSENT", "NOT_CHECKED"]


def _read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


class DonorCache:
    """Read-only view of the donor cache."""

    def __init__(self, data_dir: Path) -> None:
        self.entities = {r["xref"]: r for r in _read_tsv(data_dir / "donor-entities.tsv")}
        self.annotations = {
            (r["accession"], r["term_id"]): r
            for r in _read_tsv(data_dir / "donor-annotations.tsv")
        }
        self.checked = {
            (r["accession"], r["term_id"])
            for r in _read_tsv(data_dir / "donor-annotations-checked.tsv")
        }
        self.ancestors: dict[str, set[str]] = {
            r["term_id"]: set(r["ancestors"].split())
            for r in _read_tsv(data_dir / "term-ancestors.tsv")
        }

    def support(self, xref: str, term: str) -> tuple[str, str]:
        """Return (support class, current donor evidence codes) for a donor.

        >>> cache = DonorCache(Path("/nonexistent"))
        >>> cache.support("UniProtKB:P1", "GO:1")
        ('NOT_CHECKED', '')
        """
        entity = self.entities.get(xref)
        if not entity:
            return "NOT_CHECKED", ""
        key = (entity["accession"], term)
        if key in self.annotations:
            codes = self.annotations[key]["evidence_codes"]
            if set(codes.split(",")) & EXPERIMENTAL:
                return "EXPERIMENTAL", codes
            return "INFERRED_ONLY", codes
        if key in self.checked:
            return "ABSENT", ""
        return "NOT_CHECKED", ""

    def relation(self, term: str, other: str) -> Optional[str]:
        """How ``other`` relates to ``term``: SAME, MORE_SPECIFIC or MORE_GENERAL."""
        if term == other:
            return "SAME"
        if term in self.ancestors.get(other, ()):
            return "MORE_SPECIFIC"
        if other in self.ancestors.get(term, ()):
            return "MORE_GENERAL"
        return None


def load_reviews(genes_dir: Path, species_dir: str, gene_dir: str) -> dict[tuple, dict]:
    """Index a gene review's existing annotations by (term, evidence, ref, negated)."""
    path = genes_dir / species_dir / gene_dir / f"{gene_dir}-ai-review.yaml"
    if not path.exists():
        return {}
    try:
        doc = yaml.load(path.read_text(encoding="utf-8"), Loader=_LOADER) or {}
    except yaml.YAMLError:
        return {}
    out: dict[tuple, dict] = {}
    for ann in doc.get("existing_annotations") or []:
        term = (ann.get("term") or {}).get("id")
        key = (term, ann.get("evidence_type"), ann.get("original_reference_id"),
               bool(ann.get("negated")))
        out.setdefault(key, ann)
    return out


def _best(values: list[str]) -> str:
    return min(values, key=SUPPORT_ORDER.index) if values else "NOT_CHECKED"


def _coverage(cache: DonorCache, term: str, others: set[str]) -> str:
    """Summarise how a target's other annotations relate to ``term``."""
    relations = {cache.relation(term, o) for o in others} - {None}
    for rel in ("SAME", "MORE_SPECIFIC", "MORE_GENERAL"):
        if rel in relations:
            return rel
    return "NONE"


def symbol_match(target: str, donors: list[dict[str, str]]) -> str:
    """Compare donor gene symbols to the target symbol.

    A different symbol is where paralog sourcing shows up (e.g. rat Calm1 as a
    donor for mouse Calm3); it is a prompt to look, not a verdict.

    >>> symbol_match("Calm3", [{"symbol": "CALM3"}])
    'SAME_SYMBOL'
    >>> symbol_match("Calm3", [{"symbol": "Calm1"}, {"symbol": "Calm3"}])
    'MIXED'
    >>> symbol_match("Calm3", [{"symbol": ""}])
    'UNRESOLVED'
    """
    symbols = [d.get("symbol", "").casefold() for d in donors if d.get("symbol")]
    if not symbols:
        return "UNRESOLVED"
    same = [s == target.casefold() for s in symbols]
    if all(same):
        return "SAME_SYMBOL"
    if any(same):
        return "MIXED"
    return "DIFFERENT_SYMBOL"


def collect_propagation_data(root: Path, data_dir: Optional[Path] = None) -> dict[str, Any]:
    """Build browser/stats rows for every propagated annotation under ``genes/``."""
    genes_dir = root / "genes"
    cache = DonorCache(root / (data_dir or DEFAULT_DATA_DIR))

    target_iba: dict[tuple[str, str], set[str]] = defaultdict(set)
    target_exp: dict[tuple[str, str], set[str]] = defaultdict(set)
    for species, gene, term, evidence in iter_target_evidence(genes_dir):
        if evidence == "IBA":
            target_iba[(species, gene)].add(term)
        elif evidence in EXPERIMENTAL:
            target_exp[(species, gene)].add(term)

    review_cache: dict[tuple[str, str], dict] = {}
    rows: list[dict[str, Any]] = []
    for r in iter_propagated_rows(genes_dir):
        gene_key = (r.species_dir, r.gene_dir)
        if gene_key not in review_cache:
            review_cache[gene_key] = load_reviews(genes_dir, *gene_key)
        rows.append(_row(r, cache, review_cache[gene_key],
                         target_iba[gene_key], target_exp[gene_key], genes_dir))
    return {"rows": rows}


def _donor(xref: str, cache: DonorCache) -> dict[str, str]:
    entity = cache.entities.get(xref)
    prefix = xref.split(":", 1)[0]
    if entity:
        return {"id": xref, "symbol": entity["symbol"],
                "organism": entity["organism"], "accession": entity["accession"]}
    return {"id": xref, "symbol": "", "organism": PREFIX_SPECIES.get(prefix, ""),
            "accession": ""}


def _organism_short(name: str) -> str:
    """'Homo sapiens (Human)' -> 'Homo sapiens'."""
    return name.split(" (", 1)[0].strip()


def _row(r: PropagatedRow, cache: DonorCache, reviews: dict, iba: set[str],
         exp: set[str], genes_dir: Path) -> dict[str, Any]:
    has_review = (genes_dir / r.species_dir / r.gene_dir
                  / f"{r.gene_dir}-ai-review.yaml").exists()
    row: dict[str, Any] = {
        "target": r.target_symbol,
        "target_id": r.target_id,
        "target_species": _organism_short(r.target_taxon_label),
        "species_dir": r.species_dir,
        "gene_dir": r.gene_dir,
        "term_id": r.term_id,
        "term_label": r.term_label,
        "aspect": r.aspect,
        "qualifier": r.qualifier,
        "evidence": r.evidence,
        "reference": r.reference,
        "method": r.method,
        "method_class": r.method_class,
        "assigned_by": r.assigned_by,
        "date": r.date,
        "nodes": r.nodes,
    }
    is_donor_row = r.evidence in DONOR_EVIDENCE or r.method_class == "ELECTRONIC_ORTHOLOGY"
    if is_donor_row:
        donors = [_donor(x, cache) for x in r.donors]
        supports = []
        for d in donors:
            support, codes = cache.support(d["id"], r.term_id)
            d["support"] = support
            d["codes"] = codes
            supports.append(support)
        row["donors"] = donors
        row["donor_species"] = sorted({_organism_short(d["organism"]) for d in donors
                                       if d["organism"]}) or ["unresolved"]
        row["donor_support"] = _best(supports)
        row["symbol_match"] = symbol_match(r.target_symbol, donors)
    else:
        # IBA/TreeGrafter: the donors are the PAINT seed genes behind a node.
        # Seeds are not resolved, so no donor_species: a partial list from MOD
        # prefixes would make the species facet look complete when it is not.
        row["donors"] = [{"id": x} for x in r.donors]
        row["donor_count"] = len(r.donors)
    if r.evidence != "IBA":
        row["iba_on_target"] = _coverage(cache, r.term_id, iba)
    row["experimental_on_target"] = _coverage(cache, r.term_id, exp)

    review = reviews.get((r.term_id, r.evidence, r.reference, r.negated))
    if has_review:
        row["review_link"] = (f"genes/{r.species_dir}/{r.gene_dir}/"
                              f"{r.gene_dir}-ai-review.html")
    if review:
        rv = review.get("review") or {}
        row["action"] = rv.get("action") or "PENDING"
        if rv.get("summary"):
            row["summary"] = str(rv["summary"])
        if rv.get("reason"):
            row["reason"] = str(rv["reason"])
        prop = rv.get("propagation_review") or {}
        if prop.get("root_cause"):
            row["root_cause"] = prop["root_cause"]
        if prop.get("failure_modes"):
            row["failure_modes"] = list(prop["failure_modes"])
    else:
        row["action"] = "NOT_IN_REVIEW" if has_review else "NO_REVIEW"
    return row
