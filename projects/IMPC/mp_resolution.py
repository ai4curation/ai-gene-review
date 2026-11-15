"""Classify IMPC significant phenotype calls by the biological level they report.

The level comes from two independent places:

1. The MP term's own OWL logical definition (equivalent-class axiom) in the
   MP release: which ontologies supply the bearer of the abnormal quality
   (GO molecular function / biological process / cellular component, CL cell
   type, UBERON anatomy, CHEBI/PR molecule, NBO behaviour).
2. The IMPReSS procedure the call came from, mapped to a readout class in the
   hand-curated ``procedure_readout_classes.yaml``.

Inputs (from ``fetch_impc.py`` plus two ontology downloads, all git-ignored):

    .cache/impc/genotype_phenotype.tsv
    .cache/impc/genes.tsv
    .cache/impc/mp.owl          (https://purl.obolibrary.org/obo/mp.owl)
    .cache/impc/go-basic.obo    (https://purl.obolibrary.org/obo/go/go-basic.obo)

Outputs (committed):

    projects/IMPC/results/mp_term_levels.tsv     one row per MP term IMPC uses
    projects/IMPC/results/level_summary.yaml     counts by level
    projects/IMPC/results/RESOLUTION.md          human-readable report

    uv run python projects/IMPC/mp_resolution.py
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import yaml

CACHE = Path(".cache/impc")
HERE = Path(__file__).parent
RESULTS = HERE / "results"

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
OWL = "{http://www.w3.org/2002/07/owl#}"
RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"
OBO = "http://purl.obolibrary.org/obo/"
HAS_MODIFIER = OBO + "RO_0002573"

# Prefixes that carry the quality or the axiom scaffolding, not the bearer.
SCAFFOLD = {"PATO", "RO", "BFO", "MP", "IAO", "UPHENO"}

GO_ROOTS = {
    "GO:0003674": "MF",
    "GO:0008150": "BP",
    "GO:0005575": "CC",
}
ORGANISMAL_BP = {
    "GO:0032501",  # multicellular organismal process
    "GO:0007610",  # behavior
    "GO:0048856",  # anatomical structure development
}
CELLULAR_BP = "GO:0009987"  # cellular process

# Finest level first; a call takes the finest level its MP term supports.
LEVELS = [
    "MOLECULAR_FUNCTION",
    "CELLULAR",
    "CIRCULATING_MOLECULE",
    "ORGAN_PROCESS",
    "ANATOMY",
    "BEHAVIOUR",
    "NO_LOGICAL_DEFINITION",
]


def curie(iri: str) -> str | None:
    if not iri.startswith(OBO):
        return None
    local = iri[len(OBO):]
    if "_" not in local:
        return None
    pfx, rest = local.split("_", 1)
    return f"{pfx}:{rest}"


def parse_mp_owl(path: Path) -> tuple[dict[str, set[str]], dict[str, str]]:
    """Return MP id -> bearer CURIEs from its equivalent-class axioms, and labels."""
    fillers: dict[str, set[str]] = {}
    labels: dict[str, str] = {}
    depth = 0
    for event, el in ET.iterparse(path, events=("start", "end")):
        if event == "start":
            depth += 1
            continue
        depth -= 1
        if depth != 1 or el.tag != OWL + "Class":
            continue
        about = el.get(RDF + "about", "")
        cid = curie(about)
        if cid is None:
            el.clear()
            continue
        lab = el.find(RDFS + "label")
        if lab is not None and lab.text:
            labels[cid] = lab.text
        if cid.startswith("MP:"):
            found: set[str] = set()
            for eq in el.findall(OWL + "equivalentClass"):
                for r in eq.iter(OWL + "Restriction"):
                    prop = r.find(OWL + "onProperty")
                    if prop is not None and prop.get(RDF + "resource") == HAS_MODIFIER:
                        continue
                    for node in r.iter():
                        for attr in (RDF + "resource", RDF + "about"):
                            c = curie(node.get(attr, ""))
                            if c and c.split(":")[0] not in SCAFFOLD:
                                found.add(c)
            if found:
                fillers[cid] = found
        el.clear()
    return fillers, labels


def parse_go(path: Path) -> tuple[dict[str, str], dict[str, set[str]]]:
    """Return GO id -> namespace root code, and GO id -> is_a/part_of ancestors."""
    parents: dict[str, set[str]] = defaultdict(set)
    ns: dict[str, str] = {}
    nsmap = {
        "molecular_function": "MF",
        "biological_process": "BP",
        "cellular_component": "CC",
    }
    cur = None
    for line in path.read_text().splitlines():
        if line == "[Term]":
            cur = None
        elif line.startswith("id: GO:"):
            cur = line[4:]
        elif cur and line.startswith("namespace: "):
            ns[cur] = nsmap.get(line[11:], "")
        elif cur and line.startswith("is_a: "):
            parents[cur].add(line[6:16])
        elif cur and line.startswith("relationship: part_of GO:"):
            parents[cur].add(line[22:32])
    anc: dict[str, set[str]] = {}

    def ancestors(t: str) -> set[str]:
        if t in anc:
            return anc[t]
        anc[t] = set()
        out = set()
        for p in parents.get(t, ()):
            out.add(p)
            out |= ancestors(p)
        anc[t] = out
        return out

    for t in ns:
        ancestors(t)
    return ns, anc


def level_of(fill: set[str], go_ns: dict[str, str], go_anc: dict[str, set[str]]) -> tuple[str, list[str]]:
    flags = set()
    for c in fill:
        pfx = c.split(":")[0]
        if pfx == "GO":
            n = go_ns.get(c)
            if n == "MF":
                flags.add("MOLECULAR_FUNCTION")
            elif n == "CC":
                # A complex measured in blood (circulating IgE, creatine kinase)
                # is a circulating molecule, not a cellular location.
                if "UBERON:0000178" in fill:
                    flags.add("CIRCULATING_MOLECULE")
                else:
                    flags.add("CELLULAR")
            elif n == "BP":
                a = go_anc.get(c, set()) | {c}
                if a & ORGANISMAL_BP:
                    flags.add("ORGAN_PROCESS")
                elif CELLULAR_BP in a:
                    flags.add("CELLULAR")
                else:
                    flags.add("ORGAN_PROCESS")
        elif pfx == "CL":
            flags.add("CELLULAR")
        elif pfx in {"CHEBI", "PR"}:
            flags.add("CIRCULATING_MOLECULE")
        elif pfx in {"UBERON", "MA", "EMAPA"}:
            flags.add("ANATOMY")
        elif pfx == "NBO":
            flags.add("BEHAVIOUR")
    if not flags:
        return "NO_LOGICAL_DEFINITION", []
    for lv in LEVELS:
        if lv in flags:
            return lv, sorted(flags)
    return "NO_LOGICAL_DEFINITION", []


def procedure_classes() -> list[tuple[re.Pattern, str]]:
    spec = yaml.safe_load((HERE / "procedure_readout_classes.yaml").read_text())
    return [(re.compile(r["pattern"], re.I), r["readout_class"]) for r in spec["rules"]]


def classify_procedure(name: str, rules) -> str:
    for pat, cls in rules:
        if pat.search(name):
            return cls
    return "UNCLASSIFIED"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    gp = pd.read_csv(CACHE / "genotype_phenotype.tsv", sep="\t")
    fillers, labels = parse_mp_owl(CACHE / "mp.owl")
    go_ns, go_anc = parse_go(CACHE / "go-basic.obo")
    rules = procedure_classes()

    rows = []
    for mp in sorted(gp.mp_term_id.dropna().unique()):
        f = fillers.get(mp, set())
        lv, flags = level_of(f, go_ns, go_anc)
        rows.append(
            {
                "mp_term_id": mp,
                "mp_term_name": labels.get(mp, ""),
                "level": lv,
                "level_flags": "|".join(flags),
                "bearers": "|".join(f"{c} {labels.get(c, '')}".strip() for c in sorted(f)),
                "n_calls": int((gp.mp_term_id == mp).sum()),
                "n_genes": int(gp.loc[gp.mp_term_id == mp, "marker_symbol"].nunique()),
            }
        )
    terms = pd.DataFrame(rows)
    terms.to_csv(RESULTS / "mp_term_levels.tsv", sep="\t", index=False)

    lvl = dict(zip(terms.mp_term_id, terms.level))
    gp["level"] = gp.mp_term_id.map(lvl)
    gp["readout_class"] = gp.procedure_name.map(lambda n: classify_procedure(str(n), rules))

    def gene_finest(levels: pd.Series) -> str:
        s = set(levels.dropna())
        for lv in LEVELS:
            if lv in s:
                return lv
        return "NO_LOGICAL_DEFINITION"

    per_gene = gp.groupby("marker_symbol")["level"].agg(gene_finest)
    summary = {
        "inputs": {
            "significant_calls": int(len(gp)),
            "genes_with_significant_call": int(gp.marker_symbol.nunique()),
            "distinct_mp_terms": int(len(terms)),
            "mp_terms_with_logical_definition": int((terms.level != "NO_LOGICAL_DEFINITION").sum()),
        },
        "calls_by_level": {k: int(v) for k, v in gp.level.value_counts().items()},
        "mp_terms_by_level": {k: int(v) for k, v in terms.level.value_counts().items()},
        "genes_by_finest_level": {k: int(v) for k, v in per_gene.value_counts().items()},
        "calls_by_readout_class": {k: int(v) for k, v in gp.readout_class.value_counts().items()},
        "genes_by_readout_class": {
            k: int(v) for k, v in gp.groupby("readout_class").marker_symbol.nunique().items()
        },
        "molecular_function_terms": terms.loc[
            terms.level == "MOLECULAR_FUNCTION", ["mp_term_id", "mp_term_name", "n_calls"]
        ].to_dict("records"),
    }
    cross = pd.crosstab(gp.readout_class, gp.level)
    (RESULTS / "level_summary.yaml").write_text(yaml.safe_dump(summary, sort_keys=False))
    cross.to_csv(RESULTS / "readout_class_by_level.tsv", sep="\t")

    top_cell = (
        terms[terms.level == "CELLULAR"].sort_values("n_genes", ascending=False).head(15)
    )
    gp_bp = terms[terms.level_flags.str.contains("ORGAN_PROCESS|CELLULAR", na=False)]
    lines = [
        "# IMPC phenotype calls by biological level (generated)",
        "",
        "Generated by `mp_resolution.py`; do not edit by hand.",
        "",
        f"- Significant genotype-phenotype calls: {summary['inputs']['significant_calls']:,}",
        f"- Genes with at least one call: {summary['inputs']['genes_with_significant_call']:,}",
        f"- Distinct MP terms used: {summary['inputs']['distinct_mp_terms']:,}"
        f" ({summary['inputs']['mp_terms_with_logical_definition']:,} with an OWL logical definition)",
        "",
        "## Calls by finest level of the MP term's logical definition",
        "",
        "| Level | Calls | MP terms | Genes (finest level reached) |",
        "|---|---:|---:|---:|",
    ]
    for lv in LEVELS:
        lines.append(
            f"| {lv} | {summary['calls_by_level'].get(lv, 0):,} | "
            f"{summary['mp_terms_by_level'].get(lv, 0):,} | "
            f"{summary['genes_by_finest_level'].get(lv, 0):,} |"
        )
    lines += [
        "",
        "## Calls by IMPReSS readout class (procedure_readout_classes.yaml)",
        "",
        "| Readout class | Calls | Genes |",
        "|---|---:|---:|",
    ]
    for k, v in summary["calls_by_readout_class"].items():
        lines.append(f"| {k} | {v:,} | {summary['genes_by_readout_class'][k]:,} |")
    lines += [
        "",
        "## MP terms whose logical definition names a GO molecular function",
        "",
    ]
    if summary["molecular_function_terms"]:
        for r in summary["molecular_function_terms"]:
            lines.append(f"- {r['mp_term_id']} {r['mp_term_name']} ({r['n_calls']} calls)")
    else:
        lines.append("None.")
    lines += [
        "",
        "## Most widely called CELLULAR-level MP terms",
        "",
        "| MP term | Bearer(s) | Genes |",
        "|---|---|---:|",
    ]
    for _, r in top_cell.iterrows():
        lines.append(f"| {r.mp_term_id} {r.mp_term_name} | {r.bearers} | {r.n_genes} |")
    lines += [
        "",
        f"MP terms whose definition names a GO process or component: {len(gp_bp)}"
        " (see `mp_term_levels.tsv`, column `bearers`).",
        "",
    ]
    (RESULTS / "RESOLUTION.md").write_text("\n".join(lines))
    print("\n".join(lines[:30]))


if __name__ == "__main__":
    main()
