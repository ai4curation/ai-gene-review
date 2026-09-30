#!/usr/bin/env python3
"""Audit the GO molecular-function representation of the human cytochrome P450s.

Three questions, all answered from live data (UniProtKB, QuickGO, rhea2go,
ec2go); nothing is hardcoded.

1. INFORMATIVENESS. Does each CYP carry a GO molecular-function term that says
   which reaction it catalyses, or only P450 boilerplate (``monooxygenase
   activity``, the ``oxidoreductase activity, acting on paired donors...``
   parents, ``heme binding``, ``iron ion binding``)?

   "Boilerplate" is decided from the data rather than a hand-list. For every
   catalytic term annotated to the family, count how many *other* annotated
   terms are its ``is_a`` descendants; the counts break sharply (a handful of
   family-wide hubs, then a long tail of activities with one or two children),
   and terms at or above ``--hub-threshold`` descendants are treated as hubs.
   The full count distribution is emitted in the summary so the break can be
   checked, and the threshold moved.

   Each CYP then falls in one of three tiers:
     * ``substrate-resolved``  -- carries a non-hub activity term that is also
       maximally specific within the family.
     * ``partially-resolved``  -- carries a non-hub activity term, but the
       family resolves that term further on other members.
     * ``unresolved``          -- every catalytic term it carries is a hub, so
       GO does not say which reaction it catalyses. These are the dark CYPs.

2. PROVENANCE. For the CYPs that do carry a specific activity term, what
   evidence is behind it (experimental, phylogenetic IBA, or electronic IEA)?
   A family whose specific terms rest on IBA is a family where GO's content is
   inherited rather than curated.

   The audit also records whether this repository already holds a gene review
   for each CYP (``--genes-dir``), so the tiers double as a curation worklist.

3. REACTION COVERAGE AND TERM GAPS. Which of the reactions UniProt curates onto
   these proteins reach GO through ``rhea2go``, which do not, and what kinds of
   chemistry do the unmapped ones represent? The chemistry classes are assigned
   by pattern-matching the reaction equation (see ``classify_reaction``); the
   classification is a heuristic summary, and the per-reaction table is emitted
   so it can be checked.

Usage:
    uv run python cyp_go_audit.py --out .
    uv run python cyp_go_audit.py --out . --query 'family:"cytochrome P450 family" AND organism_id:9606 AND reviewed:true'
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

UA = {"User-Agent": "ai-gene-review-cyp/1.0"}
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
RHEA2GO_URL = "https://current.geneontology.org/ontology/external2go/rhea2go"
EC2GO_URL = "https://current.geneontology.org/ontology/external2go/ec2go"

DEFAULT_QUERY = 'family:"cytochrome P450 family" AND organism_id:9606 AND reviewed:true'
BINDING_ROOT = "GO:0005488"
CATALYTIC_ROOT = "GO:0003824"
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HTP"}

_R2G = re.compile(r"RHEA:(\d+) > GO:(.+) ; (GO:\d+)")
_E2G = re.compile(r"EC:(\S+) > GO:(.+) ; (GO:\d+)")

# Reaction-chemistry patterns, applied in order to the product side of the
# equation. Heuristic: a summary aid, not an assertion about mechanism.
CHEMISTRY = [
    ("epoxidation", re.compile(r"epoxy", re.I)),
    ("aromatization (formate-releasing)", re.compile(r"\bformate\b", re.I)),
    ("S-oxidation", re.compile(r"S-oxide|sulfoxide", re.I)),
    ("N-oxidation/N-dealkylation", re.compile(r"\bN-oxide|N-desmethyl|N-demethyl", re.I)),
    ("O-dealkylation", re.compile(r"O-demethyl|O-desmethyl", re.I)),
    ("dehydration", re.compile(r"dehydrat", re.I)),
    ("oxo-formation (alcohol to aldehyde/ketone)", re.compile(r"\d+-oxo|-oxo-|oxodocosanoate|oxohexacosanoate", re.I)),
    ("hydroxylation", re.compile(r"hydroxy", re.I)),
]
SUBSTRATE_CLASSES = [
    ("steroid / sterol", re.compile(
        r"steroid|sterol|cholesterol|progesterone|androst|estr|testosterone|cortisol|"
        r"corticosterone|aldosterone|pregnen|calcidiol|calcitriol|vitamin D|androstan", re.I)),
    ("eicosanoid / PUFA", re.compile(
        r"eicosa|docosa|arachidon|icosa|linole|lipoxin|prostagland|leukotriene|hydroperoxy", re.I)),
    ("other fatty acid", re.compile(
        r"anoate|enoate|fatty acid|dodecanoate|tetradecanoate|hexadecanoate|octadecanoate", re.I)),
    ("retinoid", re.compile(r"retino|retinal", re.I)),
    ("xenobiotic / drug", re.compile(
        r"albendazole|fenbendazole|cineole|nitrophenol|coumarin|warfarin|caffeine|"
        r"nicotine|aflatoxin|benzo|toluene|debrisoquine|bufuralol|omeprazole|tolbutamide", re.I)),
    ("vitamin K / quinone", re.compile(r"phylloquinone|menaquinone|quinone|tocopherol", re.I)),
]


def _get(url: str, timeout: int = 120, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read().decode()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError("unreachable")


def load_external2go(url: str, pattern: re.Pattern) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for line in _get(url).splitlines():
        m = pattern.match(line)
        if m:
            out[m.group(1)].add(m.group(3))
    return out


def fetch_entries(query: str) -> list[dict]:
    params = urllib.parse.urlencode({
        "query": query,
        "fields": "accession,gene_primary,protein_name,cc_catalytic_activity,cc_disease,protein_existence",
        "format": "json", "size": 500,
    })
    data = json.loads(_get(f"{UNIPROT}?{params}"))
    entries = []
    for r in data.get("results", []):
        genes = r.get("genes") or [{}]
        gene = genes[0].get("geneName", {}).get("value", "")
        reactions, diseases = [], []
        for c in r.get("comments", []):
            if c.get("commentType") == "DISEASE" and c.get("disease", {}).get("diseaseId"):
                diseases.append(c["disease"]["diseaseId"])
            if c.get("commentType") != "CATALYTIC ACTIVITY":
                continue
            rx = c["reaction"]
            rhea = next((x["id"].split(":")[1] for x in rx.get("reactionCrossReferences", [])
                         if x["database"] == "Rhea" and x["id"].startswith("RHEA:")), None)
            if rhea:
                reactions.append({
                    "rhea": rhea, "name": rx.get("name", ""), "ec": rx.get("ecNumber", ""),
                    "experimental": any(e.get("evidenceCode") == "ECO:0000269"
                                        for e in rx.get("evidences", [])),
                })
        entries.append({
            "acc": r["primaryAccession"], "gene": gene,
            "protein": r.get("proteinDescription", {}).get("recommendedName", {})
                        .get("fullName", {}).get("value", ""),
            "existence": r.get("proteinExistence", ""),
            "diseases": diseases, "reactions": reactions,
        })
    return entries


def fetch_goa_mf(acc: str) -> list[dict]:
    params = urllib.parse.urlencode(
        {"geneProductId": acc, "aspect": "molecular_function", "limit": 200})
    data = json.loads(_get(f"{QUICKGO}/annotation/search?{params}"))
    return [{"go": a["goId"], "evidence": a.get("goEvidence", ""),
             "reference": a.get("reference", ""), "qualifier": a.get("qualifier", "")}
            for a in data.get("results", [])
            if not str(a.get("qualifier", "")).startswith("NOT")]


def fetch_terms(go_ids: set[str]) -> dict[str, dict]:
    """{id: {name, ancestors(is_a, incl. self)}} from QuickGO, batched."""
    out: dict[str, dict] = {}
    ids = sorted(go_ids)
    for i in range(0, len(ids), 50):
        chunk = ",".join(ids[i:i + 50])
        data = json.loads(_get(f"{QUICKGO}/ontology/go/terms/{chunk}/ancestors?relations=is_a"))
        for t in data.get("results", []):
            out[t["id"]] = {"name": t.get("name", ""),
                            "ancestors": set(t.get("ancestors", [])) | {t["id"]}}
    return out


def classify_reaction(equation: str) -> tuple[str, str]:
    chem = next((n for n, p in CHEMISTRY if p.search(equation)), "other/unclassified")
    sub = next((n for n, p in SUBSTRATE_CLASSES if p.search(equation)), "other/unclassified")
    return chem, sub


def audit(query: str, outdir: Path, hub_threshold: int = 20,
          genes_dir: Path = Path("genes/human")) -> dict:
    rhea2go = {k: sorted(v)[0] for k, v in
               load_external2go(RHEA2GO_URL, _R2G).items()}
    ec2go = load_external2go(EC2GO_URL, _E2G)
    entries = fetch_entries(query)

    goa: dict[str, list[dict]] = {}
    for e in entries:
        goa[e["acc"]] = fetch_goa_mf(e["acc"])
        time.sleep(0.2)

    terms = fetch_terms({a["go"] for rows in goa.values() for a in rows}
                        | {rhea2go[r["rhea"]] for e in entries for r in e["reactions"]
                           if r["rhea"] in rhea2go})

    annotated = {a["go"] for rows in goa.values() for a in rows}
    catalytic = {t for t in annotated
                 if CATALYTIC_ROOT in terms.get(t, {}).get("ancestors", set())}
    binding = {t for t in annotated
               if BINDING_ROOT in terms.get(t, {}).get("ancestors", set())}
    # descendant count within the family, then hubs vs substrate-naming activities
    desc_count = {t: sum(1 for o in catalytic if o != t and t in terms[o]["ancestors"])
                  for t in catalytic}
    hubs = {t for t, n in desc_count.items() if n >= hub_threshold}
    resolved = catalytic - hubs                       # names a substrate
    maximal = {t for t in resolved if desc_count[t] == 0}   # nothing below it here

    entry_rows, unresolved, gap_rows = [], [], []
    prov, tiers = Counter(), Counter()
    for e in entries:
        rows = goa[e["acc"]]
        mine = {a["go"] for a in rows}
        my_resolved = sorted(mine & resolved)
        my_hubs = sorted(mine & hubs)
        if not my_resolved:
            tier = "unresolved"
            unresolved.append(e)
        elif mine & maximal:
            tier = "substrate-resolved"
        else:
            tier = "partially-resolved"
        tiers[tier] += 1
        best = ""
        if my_resolved:
            evs = {a["evidence"] for a in rows if a["go"] in my_resolved}
            best = ("experimental" if evs & EXPERIMENTAL else
                    "IBA" if "IBA" in evs else
                    "other-inferred" if evs - {"IEA"} else "IEA")
            prov[best] += 1
        mapped = [r for r in e["reactions"] if r["rhea"] in rhea2go]
        # a mapped reaction's term is "reached" if the entry has it or a descendant
        closure = set().union(*(terms[t]["ancestors"] for t in mine)) if mine else set()
        for r in mapped:
            if rhea2go[r["rhea"]] not in closure:
                gap_rows.append([e["acc"], e["gene"], f"RHEA:{r['rhea']}",
                                 rhea2go[r["rhea"]], terms[rhea2go[r["rhea"]]]["name"]])
        entry_rows.append([
            e["acc"], e["gene"], e["existence"], len(e["reactions"]),
            sum(r["experimental"] for r in e["reactions"]), len(mapped),
            len(e["reactions"]) - len(mapped), tier, len(my_resolved), len(my_hubs),
            best or "none", ";".join(my_resolved),
            ";".join(terms[t]["name"] for t in my_resolved), ";".join(e["diseases"]),
            "yes" if _has_review(genes_dir, e["gene"]) else "no",
        ])

    # reaction-level table
    rx_entries: dict[str, list[str]] = defaultdict(list)
    rx_info: dict[str, dict] = {}
    for e in entries:
        for r in e["reactions"]:
            rx_info.setdefault(r["rhea"], r)
            rx_entries[r["rhea"]].append(e["gene"])
    rx_rows, chem_unmapped, chem_all = [], Counter(), Counter()
    for rx, r in sorted(rx_info.items(), key=lambda kv: -len(rx_entries[kv[0]])):
        chem, sub = classify_reaction(r["name"])
        go = rhea2go.get(rx, "")
        chem_all[(chem, sub)] += 1
        if not go:
            chem_unmapped[(chem, sub)] += 1
        rx_rows.append([f"RHEA:{rx}", r["name"], r["ec"], len(rx_entries[rx]),
                        ";".join(sorted(set(rx_entries[rx]))), go,
                        terms[go]["name"] if go else "",
                        ";".join(sorted(ec2go.get(r["ec"], set()))), chem, sub,
                        "yes" if r["experimental"] else "no"])

    outdir.mkdir(parents=True, exist_ok=True)
    _tsv(outdir / "cyp-entries.tsv",
         ["accession", "gene", "protein_existence", "n_reactions", "n_reactions_experimental",
          "n_mapped", "n_unmapped", "tier", "n_resolved_mf", "n_hub_mf",
          "resolved_mf_provenance", "resolved_mf_ids", "resolved_mf_labels",
          "diseases", "review_in_repo"], entry_rows)
    _tsv(outdir / "cyp-reactions.tsv",
         ["rhea", "equation", "ec", "n_genes", "genes", "rhea2go_id", "rhea2go_label",
          "ec2go_ids", "chemistry", "substrate_class", "experimental"], rx_rows)
    _tsv(outdir / "cyp-propagation-gaps.tsv",
         ["accession", "gene", "rhea", "mapped_go", "mapped_go_label"], gap_rows)
    _tsv(outdir / "cyp-chemistry.tsv",
         ["chemistry", "substrate_class", "n_reactions", "n_unmapped", "pct_unmapped"],
         [[c, s, n, chem_unmapped[(c, s)], f"{100 * chem_unmapped[(c, s)] / n:.0f}%"]
          for (c, s), n in chem_all.most_common()])

    summary = {
        "query": query,
        "entries": len(entries),
        "entries_with_reactions": sum(1 for e in entries if e["reactions"]),
        "reaction_annotations": sum(len(e["reactions"]) for e in entries),
        "experimental_reaction_annotations": sum(r["experimental"] for e in entries for r in e["reactions"]),
        "distinct_reactions": len(rx_info),
        "mapped_reactions": sum(1 for rx in rx_info if rx in rhea2go),
        "unmapped_reactions": sum(1 for rx in rx_info if rx not in rhea2go),
        "unmapped_reactions_no_ec": sum(1 for rx, r in rx_info.items()
                                        if rx not in rhea2go and not r["ec"]),
        "distinct_mf_terms": len(annotated),
        "catalytic_mf_terms": len(catalytic),
        "hub_threshold": hub_threshold,
        "catalytic_term_descendant_counts": [
            [t, terms[t]["name"], n] for t, n in
            sorted(desc_count.items(), key=lambda kv: -kv[1]) if n],
        "hub_terms": sorted((t, terms[t]["name"]) for t in hubs),
        "substrate_naming_mf_terms": len(resolved),
        "maximally_specific_mf_terms": len(maximal),
        "binding_mf_terms": len(binding),
        "tiers": dict(tiers),
        "reviews_in_repo": sum(1 for r in entry_rows if r[-1] == "yes"),
        "reviewed_genes": sorted(r[1] for r in entry_rows if r[-1] == "yes"),
        "unresolved_cyps": [[e["gene"], e["acc"], len(e["reactions"]), ";".join(e["diseases"])]
                            for e in sorted(unresolved, key=lambda x: -len(x["reactions"]))],
        "resolved_mf_provenance": dict(prov),
        "propagation_gap_pairs": len(gap_rows),
        "top_unmapped_chemistry": [[c, s, n] for (c, s), n in chem_unmapped.most_common(10)],
    }
    (outdir / "cyp-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def _has_review(genes_dir: Path, gene: str) -> bool:
    """True when this repo already holds a gene review for the symbol."""
    for base in (genes_dir, Path(__file__).resolve().parents[2] / genes_dir):
        if (base / gene / f"{gene}-ai-review.yaml").exists():
            return True
    return False


def _tsv(path: Path, header: list[str], rows) -> None:
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--query", default=DEFAULT_QUERY)
    ap.add_argument("--out", type=Path, default=Path("."))
    ap.add_argument("--genes-dir", type=Path, default=Path("genes/human"),
                    help="where to look for <GENE>/<GENE>-ai-review.yaml (relative to "
                         "the repo root) when recording existing review coverage")
    ap.add_argument("--hub-threshold", type=int, default=20,
                    help="a catalytic term with this many annotated is_a descendants "
                         "in the family counts as a boilerplate hub (default 20; the "
                         "summary reports the distribution the default is drawn from)")
    args = ap.parse_args()
    print(json.dumps(audit(args.query, args.out, args.hub_threshold, args.genes_dir), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
