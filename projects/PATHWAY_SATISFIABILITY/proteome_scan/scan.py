"""Scan UniProt proteomes against every module: which are realized, and where are the holes?

The oracle is the proteome's own first-pass UniProt annotation: per protein, its GO
ids and its PANTHER, InterPro, NCBIfam and Pfam cross-references. The logic is the
module engine (``ai_gene_review.module_logic``); only the predicate is new.

A step (atom) is scored against one proteome at four levels, best first:

* ``named``         - a UniProt accession the module names is in this proteome;
* ``function``      - a protein is annotated to a required GO molecular function or
  an is_a/part_of descendant;
* ``selector``      - a protein carries a family or domain selector of the step,
  exactly as the module states it (a PANTHER family or subfamily, InterPro, NCBIfam, Pfam);
* ``parent_family`` - the step selects a PANTHER subfamily and a protein is in the
  same family but another subfamily.

``strict`` satisfaction accepts ``named`` and ``function``, and ``selector`` for a
step that requires no function (a structural subunit); ``lenient`` also accepts
``selector`` for a step that does. A step that holds only leniently is an
**annotation hole**: a member of the step's family is present but nothing in the
proteome is annotated to the step's function; the members are listed as candidates.
A step with a function or a family/domain selector that nothing matches is a
**missing step**. ``parent_family`` never satisfies a step, because another subfamily
is usually a paralog with another substrate; its members are listed on the missing
step as ``paralog_candidates``, which is also how a subfamily selector that is too
narrow for this lineage shows up. A step grounded only by accessions of
another organism, or by a selector a protein table cannot answer (an RFAM RNA
family, a PANTHER PTN node), is **unevaluable** here; such steps are assumed to hold when deciding
whether a module is blocked, so they never produce a hole.

Module status, per proteome:

* ``SATISFIED``            - holds strictly, with no unevaluable step in the way;
* ``SATISFIED_BY_FAMILY``  - holds only leniently (every blocking step is an annotation hole);
* ``UNEVALUABLE``          - holds only if unevaluable steps are assumed present;
* ``NEAR_COMPLETE``        - at most ``--max-gaps`` innermost gaps and at least
  ``--min-fraction`` of evaluable steps hold;
* ``INCOMPLETE``           - some evaluable step holds, but not near complete;
* ``ABSENT``               - no evaluable step holds.

Taxon scope follows the module's root ``context.taxa``: ``in_clade`` (a listed taxon
is in the proteome's lineage), ``undeclared`` (none listed), ``other_organism`` (only
single organisms outside the lineage, which say where the module was curated) and
``out_of_clade`` (a listed clade excludes the proteome).

Presence is an upper bound: a GO annotation or family hit permits a step, it does not
show the pathway runs. Family-level hits do not separate paralogs.

Usage (from the repository root)::

    uv run python projects/PATHWAY_SATISFIABILITY/proteome_scan/scan.py \
        UP000000625 UP000035170 -o projects/PATHWAY_SATISFIABILITY/proteome_scan/results

Each output file gives status counts for every module by scope, and per-module detail
only for in-scope modules (``in_clade`` or ``undeclared``) that have an annotation hole
or a missing step. Downloads are cached in the git-ignored ``.cache/proteome_scan``.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from ai_gene_review.module_logic import (
    Atom,
    Circuit,
    compile_module_file,
    gap_report,
    is_satisfied,
    iter_atoms,
)

UNIPROT = "https://rest.uniprot.org"
GO_OBO = "https://purl.obolibrary.org/obo/go/go-basic.obo"
CACHE = Path(".cache/proteome_scan")
FIELDS = "accession,reviewed,gene_primary,gene_oln,protein_name,go_id,xref_panther,xref_interpro,xref_ncbifam,xref_pfam"
BINOMIAL = re.compile(r"^[A-Z][a-z]+ [a-z]")
#: Selector prefixes a UniProt protein table can answer; RFAM and PANTHER PTN nodes are not.
INDEXED = ("PANTHER:PTHR", "InterPro:", "NCBIfam:", "Pfam:")
LEVELS = ("named", "function", "selector", "parent_family")
MAX_CANDIDATES = 6


def cached(name: str, url: str) -> str:
    """Return the text at ``url``, downloading it once into the cache."""
    path = CACHE / name
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(url, timeout=600) as resp:
            path.write_bytes(resp.read())
    return path.read_text()


def go_descendants() -> tuple[dict[str, set[str]], dict[str, str], dict[str, str]]:
    """Children by is_a/part_of, alt_id -> primary id, and labels, from go-basic."""
    children: dict[str, set[str]] = defaultdict(set)
    alt: dict[str, str] = {}
    labels: dict[str, str] = {}
    for stanza in cached("go-basic.obo", GO_OBO).split("\n[Term]\n")[1:]:
        stanza = stanza.split("\n[Typedef]")[0]
        term = ""
        for line in stanza.splitlines():
            if line.startswith("id: "):
                term = line[4:]
            elif line.startswith("name: "):
                labels[term] = line[6:]
            elif line.startswith("alt_id: "):
                alt[line[8:]] = term
            elif line.startswith("is_a: "):
                children[line[6:16]].add(term)
            elif line.startswith("relationship: part_of "):
                children[line[22:32]].add(term)
    return children, alt, labels


def closure(term: str, children: dict[str, set[str]]) -> set[str]:
    """``term`` and all its is_a/part_of descendants.

    >>> sorted(closure("a", {"a": {"b"}, "b": {"c"}}))
    ['a', 'b', 'c']
    """
    seen, stack = {term}, [term]
    while stack:
        for child in children.get(stack.pop(), ()):
            if child not in seen:
                seen.add(child)
                stack.append(child)
    return seen


@dataclass
class Proteome:
    upid: str
    organism: str
    taxon_id: int
    lineage: set[str]
    proteins: dict[str, dict] = field(default_factory=dict)
    by_go: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))
    by_selector: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))


def split(value: str) -> list[str]:
    """Split a UniProt multi-value TSV cell.

    >>> split("PTHR1;PTHR1:SF2;"), split("GO:1; GO:2")
    (['PTHR1', 'PTHR1:SF2'], ['GO:1', 'GO:2'])
    """
    return [x.strip() for x in (value or "").split(";") if x.strip()]


def load_proteome(upid: str) -> Proteome:
    info = json.loads(cached(f"{upid}.json", f"{UNIPROT}/proteomes/{upid}.json"))
    taxon = info["taxonomy"]["taxonId"]
    tax = json.loads(cached(f"taxon-{taxon}.json", f"{UNIPROT}/taxonomy/{taxon}.json"))
    lineage = {f"NCBITaxon:{taxon}"} | {f"NCBITaxon:{x['taxonId']}" for x in tax.get("lineage", [])}
    params = urllib.parse.urlencode({"query": f"proteome:{upid}", "format": "tsv", "fields": FIELDS})
    proteome = Proteome(upid, info["taxonomy"]["scientificName"], taxon, lineage)
    rows = csv.DictReader(io.StringIO(cached(f"{upid}.tsv", f"{UNIPROT}/uniprotkb/stream?{params}")), delimiter="\t")
    for row in rows:
        accession = row["Entry"]
        proteome.proteins[accession] = {
            "accession": accession,
            "gene": row["Gene Names (primary)"] or row["Gene Names (ordered locus)"],
            "name": re.sub(r" \(.*", "", row["Protein names"]),
            "reviewed": row["Reviewed"] == "reviewed",
        }
        for go in split(row["Gene Ontology IDs"]):
            proteome.by_go[go].add(accession)
        for prefix, column in (("PANTHER", "PANTHER"), ("InterPro", "InterPro"), ("NCBIfam", "NCBIfam"), ("Pfam", "Pfam")):
            for identifier in split(row[column]):
                proteome.by_selector[f"{prefix}:{identifier}"].add(accession)
    return proteome


class Oracle:
    """Score atoms against one proteome; results are cached per atom."""

    def __init__(self, proteome: Proteome, children: dict[str, set[str]], alt: dict[str, str]):
        self.proteome, self.children, self.alt = proteome, children, alt
        self._closures: dict[str, set[str]] = {}
        self._scores: dict[Atom, dict[str, set[str]]] = {}

    def function_hits(self, term: str) -> set[str]:
        term = self.alt.get(term, term)
        if term not in self._closures:
            self._closures[term] = closure(term, self.children)
        hits: set[str] = set()
        for descendant in self._closures[term]:
            hits |= self.proteome.by_go.get(descendant, set())
        return hits

    def score(self, atom: Atom) -> dict[str, set[str]]:
        """Proteins supporting ``atom`` at each level."""
        if atom not in self._scores:
            support: dict[str, set[str]] = {level: set() for level in LEVELS}
            support["named"] = {u.split("-")[0] for u in atom.uniprots} & self.proteome.proteins.keys()
            for term in atom.function_ids:
                support["function"] |= self.function_hits(term)
            for selector in (*atom.family_ids, *atom.domain_ids):
                support["selector"] |= self.proteome.by_selector.get(selector, set())
                if selector.startswith("PANTHER:PTHR") and ":SF" in selector:
                    parent = selector.rpartition(":SF")[0]
                    support["parent_family"] |= self.proteome.by_selector.get(parent, set())
            support["parent_family"] -= support["selector"]
            self._scores[atom] = support
        return self._scores[atom]

    def level(self, atom: Atom) -> str | None:
        """The best level at which ``atom`` holds; ``parent_family`` is not holding."""
        support = self.score(atom)
        return next((level for level in LEVELS[:3] if support[level]), None)

    def strict(self, atom: Atom) -> bool:
        level = self.level(atom)
        return level in ("named", "function") or (level == "selector" and not atom.function_ids)

    def evaluable(self, atom: Atom) -> bool:
        """True when this proteome could show the step present or absent."""
        selectors = (*atom.family_ids, *atom.domain_ids)
        return bool(atom.function_ids or self.score(atom)["named"] or any(s.startswith(INDEXED) for s in selectors))


def scope(doc: dict, lineage: set[str]) -> str:
    """Taxon scope of a module's root ``context.taxa`` for a proteome lineage.

    >>> taxa = lambda *t: {"module": {"context": {"taxa": [{"term": {"id": i, "label": l}} for i, l in t]}}}
    >>> scope(taxa(("NCBITaxon:2", "Bacteria")), {"NCBITaxon:2"})
    'in_clade'
    >>> scope(taxa(("NCBITaxon:9606", "Homo sapiens")), {"NCBITaxon:2"})
    'other_organism'
    >>> scope(taxa(("NCBITaxon:33208", "Metazoa")), {"NCBITaxon:2"}), scope({"module": {}}, set())
    ('out_of_clade', 'undeclared')
    """
    taxa = [t.get("term") or {} for t in ((doc["module"].get("context") or {}).get("taxa") or [])]
    taxa = [t for t in taxa if str(t.get("id", "")).startswith("NCBITaxon:")]
    if not taxa:
        return "undeclared"
    if any(t["id"] in lineage for t in taxa):
        return "in_clade"
    if all(BINOMIAL.match(t.get("label") or "") for t in taxa):
        return "other_organism"
    return "out_of_clade"


def describe(proteome: Proteome, accessions: set[str]) -> list[dict]:
    """Up to ``MAX_CANDIDATES`` proteins, reviewed first."""
    proteins = sorted((proteome.proteins[a] for a in accessions), key=lambda p: (not p["reviewed"], p["accession"]))
    return [{k: v for k, v in p.items() if v not in ("", False)} for p in proteins[:MAX_CANDIDATES]]


def scan_module(circuit: Circuit, oracle: Oracle, labels: dict[str, str], max_gaps: int, min_fraction: float) -> dict:
    atoms = list(dict.fromkeys(iter_atoms(circuit)))
    evaluable = [a for a in atoms if oracle.evaluable(a)]
    levels = {a: oracle.level(a) for a in atoms}

    strict = oracle.strict

    def lenient(atom: Atom) -> bool:
        return levels[atom] is not None

    def optimistic(atom: Atom) -> bool:
        return lenient(atom) or not oracle.evaluable(atom)

    holding = [a for a in evaluable if lenient(a)]
    result: dict = {
        "steps": len(atoms),
        "evaluable_steps": len(evaluable),
        "steps_holding": len(holding),
        "steps_by_level": dict(Counter(levels[a] for a in holding)),
    }
    if is_satisfied(circuit, strict):
        result["status"] = "SATISFIED"
        return result
    gaps = gap_report(circuit, optimistic)
    fraction = len(holding) / len(evaluable) if evaluable else 0.0
    if is_satisfied(circuit, lenient):
        result["status"] = "SATISFIED_BY_FAMILY"
    elif not gaps:
        result["status"] = "UNEVALUABLE"
    elif not holding:
        result["status"] = "ABSENT"
        return result
    elif len(gaps) <= max_gaps and fraction >= min_fraction:
        result["status"] = "NEAR_COMPLETE"
    else:
        result["status"] = "INCOMPLETE"
        result["gaps"] = len(gaps)
        return result

    # Annotation holes: steps that block the strict reading and hold only through a family member.
    holes = []
    for gap in gap_report(circuit, strict):
        for atom in gap.absent:
            support = oracle.score(atom)
            if not lenient(atom):
                continue
            level = levels[atom]
            holes.append({
                "step": atom.node_id,
                "label": atom.label,
                "function": [f"{t} {labels.get(t, '')}".strip() for t in atom.function_ids],
                "basis": level,
                "selectors": [s for s in (*atom.family_ids, *atom.domain_ids) if oracle.proteome.by_selector.get(s)],
                "candidate_count": len(support[level]),
                "candidates": describe(oracle.proteome, support[level]),
            })
    if holes:
        result["annotation_holes"] = list({h["step"]: h for h in holes}.values())
    if gaps:
        result["missing_steps"] = [
            {
                "gap": "/".join(gap.path),
                "layer": gap.layer,
                "partial": gap.partial,
                "absent": [
                    {
                        "step": a.node_id,
                        "label": a.label,
                        "function": [f"{t} {labels.get(t, '')}".strip() for t in a.function_ids],
                        "selectors": [*a.family_ids, *a.domain_ids],
                        "paralog_candidates": describe(oracle.proteome, oracle.score(a)["parent_family"]),
                    }
                    for a in gap.absent
                    if oracle.evaluable(a)
                ],
            }
            for gap in gaps
        ]
    return result


def scan(upid: str, modules: list[tuple[str, dict, Circuit]], go, max_gaps: int, min_fraction: float) -> dict:
    children, alt, labels = go
    proteome = load_proteome(upid)
    oracle = Oracle(proteome, children, alt)
    results = {}
    for stem, doc, circuit in modules:
        entry = {"scope": scope(doc, proteome.lineage), **scan_module(circuit, oracle, labels, max_gaps, min_fraction)}
        results[stem] = entry
    proteins = proteome.proteins.values()
    counts: dict[str, Counter] = defaultdict(Counter)
    for entry in results.values():
        counts[entry["scope"]][entry["status"]] += 1
    return {
        "proteome": upid,
        "organism": proteome.organism,
        "taxon": f"NCBITaxon:{proteome.taxon_id}",
        "proteins": len(proteome.proteins),
        "reviewed": sum(p["reviewed"] for p in proteins),
        "with_go": len(set().union(*proteome.by_go.values())) if proteome.by_go else 0,
        "with_panther": len(set().union(*(v for k, v in proteome.by_selector.items() if k.startswith("PANTHER:")), set())),
        "status_by_scope": {s: dict(c) for s, c in sorted(counts.items())},
        # Detail only where a curator has something to act on: in-scope modules with a hole or a gap.
        "modules": {
            stem: entry
            for stem, entry in results.items()
            if entry["scope"] in ("in_clade", "undeclared")
            and (entry.get("annotation_holes") or entry.get("missing_steps"))
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("upids", nargs="+", help="UniProt proteome ids")
    parser.add_argument("--modules", type=Path, default=Path("modules"))
    parser.add_argument("-o", "--output", type=Path, required=True, help="output directory, one YAML per proteome")
    parser.add_argument("--max-gaps", type=int, default=2)
    parser.add_argument("--min-fraction", type=float, default=0.75)
    args = parser.parse_args(argv)
    go = go_descendants()
    modules = []
    for path in sorted(args.modules.glob("*.yaml")):
        modules.append((path.stem, yaml.safe_load(path.read_text()), compile_module_file(path)))
    args.output.mkdir(parents=True, exist_ok=True)
    for upid in args.upids:
        report = scan(upid, modules, go, args.max_gaps, args.min_fraction)
        (args.output / f"{upid}.yaml").write_text(yaml.safe_dump(report, sort_keys=False, width=200))
        print(upid, report["organism"], report["proteins"], report["status_by_scope"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
