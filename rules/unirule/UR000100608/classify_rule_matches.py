#!/usr/bin/env python3
"""Classify the UniProtKB entries annotated by HAMAP MF_01093 (UniRule UR000100608).

Fetches, live from the UniProt REST API, every entry whose annotation evidence
cites the HAMAP rule (query ``source:MF_01093``) and, for comparison, every entry
matching the HAMAP family signature (``xref:hamap-MF_01093``). Each entry is
classified from its own sequence:

* ANCHORED: length >= LENGTH_CUTOFF and a hydrophobic segment (max Kyte-Doolittle
  19-residue window >= KD_TM) in the C-terminal CTERM_WINDOW residues. This is the
  membrane-associated, operon-encoded MtrA.
* SOLUBLE: length < LENGTH_CUTOFF and no such C-terminal hydrophobic segment.
  These are the cytoplasmic MtrA homologues (PMID:27324530 uses < 215 aa).
* AMBIGUOUS: the two criteria disagree.

For each entry the script records which rule consequents it carries (cell membrane
location, TRANSMEM features and their position, EC 7.2.1.4, the 8-subunit SUBUNIT
text, GO:0005886 / GO:0030269). Nothing is hardcoded; counts follow the current
UniProt release.

Usage (from the repository root):
    python3 rules/unirule/UR000100608/classify_rule_matches.py \
        > rules/unirule/UR000100608/rule_matches.tsv \
        2> rules/unirule/UR000100608/summary.txt

Dependencies: Python standard library + requests.
"""

from __future__ import annotations

import csv
import io
import re
import sys

import requests

API = "https://rest.uniprot.org/uniprotkb/search"
RULE_QUERY = "source:MF_01093"
FAMILY_QUERY = "xref:hamap-MF_01093"
FIELDS = [
    "accession",
    "reviewed",
    "organism_name",
    "lineage",
    "length",
    "fragment",
    "ft_transmem",
    "cc_subcellular_location",
    "ec",
    "cc_subunit",
    "go_c",
    "go_f",
    "go_p",
    "cc_cofactor",
    "cc_function",
    "cc_pathway",
    "ft_binding",
    "keyword",
    "sequence",
]
LENGTH_CUTOFF = 215  # PMID:27324530: < 215 aa = cytoplasmic MtrA homologue
CTERM_WINDOW = 60  # residues at the C-terminus searched for an anchor
KD_WINDOW = 19
KD_TM = 1.6  # classic Kyte-Doolittle TM threshold for a 19-residue window

KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}


def fetch(query: str) -> list[dict]:
    """Return all TSV rows for a UniProtKB query, following pagination links."""
    rows: list[dict] = []
    params = {"query": query, "fields": ",".join(FIELDS), "format": "tsv", "size": 500}
    url: str | None = API
    while url:
        r = requests.get(url, params=params, timeout=120)
        r.raise_for_status()
        rows.extend(csv.DictReader(io.StringIO(r.text), delimiter="\t"))
        params = None  # the next link already carries the query
        nxt = re.search(r'<([^>]+)>;\s*rel="next"', r.headers.get("Link", ""))
        url = nxt.group(1) if nxt else None
    return rows


def max_kd(seq: str) -> tuple[float, int]:
    """Max mean KD over 19-residue windows; returns (score, 1-based start)."""
    best, pos = float("-inf"), 0
    for i in range(0, max(0, len(seq) - KD_WINDOW) + 1):
        w = seq[i : i + KD_WINDOW]
        s = sum(KD.get(a, 0.0) for a in w) / len(w)
        if s > best:
            best, pos = s, i + 1
    return best, pos


def tm_spans(ft: str) -> list[tuple[int, int]]:
    return [(int(a), int(b)) for a, b in re.findall(r"TRANSMEM (\d+)\.\.(\d+)", ft or "")]


def classify(row: dict) -> dict:
    seq = row["Sequence"]
    n = len(seq)
    cterm = seq[-CTERM_WINDOW:] if n > CTERM_WINDOW else seq
    ckd, cpos = max_kd(cterm)
    cpos_abs = n - len(cterm) + cpos
    wkd, wpos = max_kd(seq)
    long_ = n >= LENGTH_CUTOFF
    anchor = ckd >= KD_TM
    if long_ and anchor:
        cls = "ANCHORED"
    elif not long_ and not anchor:
        cls = "SOLUBLE"
    else:
        cls = "AMBIGUOUS"
    spans = tm_spans(row["Transmembrane"])
    internal = [s for s in spans if s[1] < n - CTERM_WINDOW]
    go_c = row.get("Gene Ontology (cellular component)", "")
    go_f = row.get("Gene Ontology (molecular function)", "")
    go_p = row.get("Gene Ontology (biological process)", "")
    kws = {k.strip() for k in row.get("Keywords", "").split(";")}
    lineage = row.get("Taxonomic lineage", "")
    cls_m = re.search(r"(Methano\w+|Thermococci|Archaeoglobi|\w+) \(class\)", lineage)
    return {
        "accession": row["Entry"],
        "reviewed": "reviewed" if row["Reviewed"] == "reviewed" else "unreviewed",
        "organism": row["Organism"],
        "class": cls_m.group(1) if cls_m else "",
        "length": n,
        "fragment": row.get("Fragment", ""),
        "cterm_max_kd": f"{ckd:.2f}",
        "cterm_max_kd_start": cpos_abs,
        "whole_max_kd": f"{wkd:.2f}",
        "whole_max_kd_start": wpos,
        "classification": cls,
        "transmem": ";".join(f"{a}-{b}" for a, b in spans),
        "transmem_internal": ";".join(f"{a}-{b}" for a, b in internal),
        "cell_membrane": "yes" if "Cell membrane" in row["Subcellular location [CC]"] else "no",
        "ec_7_2_1_4": "yes" if "7.2.1.4" in row["EC number"] else "no",
        "subunit_8": "yes" if "composed of 8 subunits" in row["Subunit structure"] else "no",
        "go_plasma_membrane": "yes" if "GO:0005886" in go_c else "no",
        "go_h4mpt_smt": "yes" if "GO:0030269" in go_f else "no",
        "cofactor_cobamide": "yes" if "cob(I)amide" in row.get("Cofactor", "") else "no",
        "function_na_translocating": "yes" if "sodium-ion translocating" in row.get("Function [CC]", "") else "no",
        "pathway_methanogenesis": "yes" if "methanogenesis" in row.get("Pathway", "") else "no",
        "binding_cobamide": "yes" if "cob(I)amide" in row.get("Binding site", "") else "no",
        "kw_cell_membrane": "yes" if "Cell membrane" in kws else "no",
        "kw_transmembrane": "yes" if "Transmembrane" in kws else "no",
        "kw_translocase": "yes" if "Translocase" in kws else "no",
        "kw_methanogenesis": "yes" if "Methanogenesis" in kws else "no",
        "go_one_carbon": "yes" if "GO:0006730" in go_p else "no",
        "go_methanogenesis_co2": "yes" if "GO:0019386" in go_p else "no",
    }


def main() -> None:
    rule_rows = fetch(RULE_QUERY)
    family_accs = {r["Entry"] for r in fetch(FAMILY_QUERY)}
    out = [classify(r) for r in rule_rows]
    out.sort(key=lambda d: (d["classification"], d["length"], d["accession"]))
    w = csv.DictWriter(sys.stdout, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(out)

    rule_accs = {d["accession"] for d in out}
    log = sys.stderr.write
    log(f"query {RULE_QUERY!r}: {len(out)} entries annotated by the rule\n")
    log(f"query {FAMILY_QUERY!r}: {len(family_accs)} entries matching the signature\n")
    log(f"  signature matches without rule annotation: {sorted(family_accs - rule_accs)}\n")
    log(f"  rule-annotated entries without the signature xref: {sorted(rule_accs - family_accs)}\n")
    for cls in ("ANCHORED", "SOLUBLE", "AMBIGUOUS"):
        sub = [d for d in out if d["classification"] == cls]
        if not sub:
            log(f"\n{cls}: 0\n")
            continue
        lens = [d["length"] for d in sub]
        log(f"\n{cls}: {len(sub)} (reviewed {sum(d['reviewed'] == 'reviewed' for d in sub)}),"
            f" length {min(lens)}-{max(lens)}\n")
        for key in ("cell_membrane", "ec_7_2_1_4", "subunit_8", "function_na_translocating",
                    "pathway_methanogenesis", "cofactor_cobamide", "binding_cobamide",
                    "kw_cell_membrane", "kw_transmembrane", "kw_translocase", "kw_methanogenesis",
                    "go_plasma_membrane", "go_h4mpt_smt", "go_one_carbon", "go_methanogenesis_co2"):
            log(f"  {key}: {sum(d[key] == 'yes' for d in sub)}\n")
        log(f"  with any TRANSMEM: {sum(bool(d['transmem']) for d in sub)}\n")
        log(f"  with a TRANSMEM outside the C-terminal {CTERM_WINDOW} residues: "
            f"{sum(bool(d['transmem_internal']) for d in sub)}\n")
        classes: dict[str, int] = {}
        for d in sub:
            classes[d["class"]] = classes.get(d["class"], 0) + 1
        log(f"  taxonomic classes: {dict(sorted(classes.items()))}\n")
        log(f"  accessions: {' '.join(d['accession'] for d in sub)}\n")
    hist: dict[int, int] = {}
    for d in out:
        b = d["length"] // 10 * 10
        hist[b] = hist.get(b, 0) + 1
    log("\nlength histogram (10-aa bins): " + ", ".join(f"{k}:{v}" for k, v in sorted(hist.items())) + "\n")


if __name__ == "__main__":
    main()
