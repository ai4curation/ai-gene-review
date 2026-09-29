#!/usr/bin/env python3
"""Explore how RHEA reactions reach GO for promiscuous enzyme families.

Companion to ``rhea_ec_specificity.py`` (which measures specificity collapse
over the whole of ``rhea2go``). This script looks at the same question family
by family, for enzyme families that act on many substrates and for which
UniProt therefore records many substrate-specific RHEA reactions per protein:

* ``haloalkane`` -- microbial haloalkane dehalogenases (EC 3.8.1.5), reviewed
  entries in any organism.
* ``ces`` -- human carboxylesterases (CES1, CES2, CES3, CES4A, CES5A), the
  liver/intestine drug- and lipid-ester hydrolases.
* ``cyp`` -- human cytochrome P450s (UniProt family "cytochrome P450 family").

For each family it fetches, live:

1. Reviewed UniProtKB entries and their ``CATALYTIC ACTIVITY`` lines (RHEA id,
   EC, and whether the evidence is experimental, ECO:0000269).
2. ``rhea2go`` and ``ec2go`` from current.geneontology.org.
3. The GOA molecular-function annotations of every entry from QuickGO,
   including which rows come from the RHEA pipeline (``GO_REF:0000116``).
4. ``is_a`` ancestor closures from QuickGO, so a mapped term counts as present
   when the entry carries it or any ``is_a`` descendant of it.

It then reports, per family: how many distinct reactions are annotated, how
many of them have a ``rhea2go`` target, how many GO terms those targets
collapse onto, how many GOA rows RHEA contributes, and a closure-aware
reverse gap (entries carrying a mapped reaction but neither the mapped term
nor any descendant of it).

Nothing is hardcoded; every number comes from the live sources. Run:

    uv run python rhea_family_explorer.py                  # all three families
    uv run python rhea_family_explorer.py --family cyp --out families/
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

UA = {"User-Agent": "ai-gene-review-rhea/1.0"}
RHEA2GO_URL = "https://current.geneontology.org/ontology/external2go/rhea2go"
EC2GO_URL = "https://current.geneontology.org/ontology/external2go/ec2go"
UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
RHEA_GO_REF = "GO_REF:0000116"
EXPERIMENTAL_ECO = "ECO:0000269"

FAMILIES = {
    "haloalkane": {
        "title": "Haloalkane dehalogenases (EC 3.8.1.5, all organisms)",
        "query": "ec:3.8.1.5 AND reviewed:true",
    },
    "ces": {
        "title": "Human carboxylesterases (CES1-5)",
        "query": "(gene_exact:CES1 OR gene_exact:CES2 OR gene_exact:CES3 OR "
        "gene_exact:CES4A OR gene_exact:CES5A) AND organism_id:9606 AND reviewed:true",
        # gene_exact also matches synonyms (MT2A has the alias CES3); keep primaries only
        "genes": {"CES1", "CES2", "CES3", "CES4A", "CES5A"},
    },
    "cyp": {
        "title": "Human cytochrome P450s",
        "query": 'family:"cytochrome P450 family" AND organism_id:9606 AND reviewed:true',
    },
}

_R2G = re.compile(r"RHEA:(\d+) > GO:(.+) ; (GO:\d+)")
_E2G = re.compile(r"EC:(\S+) > GO:(.+) ; (GO:\d+)")


def _get(url: str, timeout: int = 120, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode()
        except Exception:  # network hiccup: back off and retry
            if attempt == retries - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError("unreachable")


def load_rhea2go() -> dict[str, tuple[str, str]]:
    out = {}
    for line in _get(RHEA2GO_URL).splitlines():
        m = _R2G.match(line)
        if m:
            out[m.group(1)] = (m.group(3), m.group(2))
    return out


def load_ec2go() -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for line in _get(EC2GO_URL).splitlines():
        m = _E2G.match(line)
        if m:
            out[m.group(1)].add(m.group(3))
    return out


def fetch_entries(query: str) -> list[dict]:
    """Reviewed UniProt entries with their catalytic-activity reactions."""
    params = urllib.parse.urlencode(
        {
            "query": query,
            "fields": "accession,gene_primary,organism_name,cc_catalytic_activity",
            "format": "json",
            "size": 500,
        }
    )
    data = json.loads(_get(f"{UNIPROT_URL}?{params}"))
    entries = []
    for r in data.get("results", []):
        genes = r.get("genes") or [{}]
        gene = genes[0].get("geneName", {}).get("value") or genes[0].get(
            "orderedLocusNames", [{}]
        )[0].get("value", "")
        reactions = []
        for c in r.get("comments", []):
            if c.get("commentType") != "CATALYTIC ACTIVITY":
                continue
            rx = c["reaction"]
            rhea = next(
                (x["id"].split(":")[1] for x in rx.get("reactionCrossReferences", [])
                 if x["database"] == "Rhea" and x["id"].startswith("RHEA:")),
                None,
            )
            if not rhea:
                continue
            ecos = {e.get("evidenceCode") for e in rx.get("evidences", [])}
            reactions.append(
                {
                    "rhea": rhea,
                    "name": rx.get("name", ""),
                    "ec": rx.get("ecNumber", ""),
                    "experimental": EXPERIMENTAL_ECO in ecos,
                }
            )
        entries.append(
            {
                "acc": r["primaryAccession"],
                "gene": gene,
                "organism": r.get("organism", {}).get("scientificName", ""),
                "reactions": reactions,
            }
        )
    return entries


def fetch_goa_mf(acc: str) -> list[dict]:
    params = urllib.parse.urlencode(
        {"geneProductId": acc, "aspect": "molecular_function", "limit": 200}
    )
    data = json.loads(_get(f"{QUICKGO}/annotation/search?{params}"))
    return [
        {
            "go": a["goId"],
            "evidence": a.get("goEvidence", ""),
            "reference": a.get("reference", ""),
            "qualifier": a.get("qualifier", ""),
        }
        for a in data.get("results", [])
    ]


def fetch_isa_ancestors(go_ids: set[str]) -> dict[str, set[str]]:
    """{term: set of is_a ancestors incl. itself} via QuickGO, batched."""
    out: dict[str, set[str]] = {}
    ids = sorted(go_ids)
    for i in range(0, len(ids), 50):
        chunk = ",".join(ids[i : i + 50])
        data = json.loads(_get(f"{QUICKGO}/ontology/go/terms/{chunk}/ancestors?relations=is_a"))
        for t in data.get("results", []):
            out[t["id"]] = set(t.get("ancestors", [])) | {t["id"]}
    return out


def fetch_labels(go_ids: set[str]) -> dict[str, str]:
    out = {}
    ids = sorted(go_ids)
    for i in range(0, len(ids), 50):
        data = json.loads(_get(f"{QUICKGO}/ontology/go/terms/{','.join(ids[i:i + 50])}"))
        for t in data.get("results", []):
            out[t["id"]] = t["name"]
    return out


def analyse(name: str, spec: dict, rhea2go, ec2go, outdir: Path | None) -> dict:
    entries = fetch_entries(spec["query"])
    if "genes" in spec:
        entries = [e for e in entries if e["gene"] in spec["genes"]]
    goa: dict[str, list[dict]] = {}
    for e in entries:
        goa[e["acc"]] = fetch_goa_mf(e["acc"])
        time.sleep(0.2)

    all_terms = {a["go"] for rows in goa.values() for a in rows}
    all_terms |= {rhea2go[r["rhea"]][0] for e in entries for r in e["reactions"] if r["rhea"] in rhea2go}
    closure = fetch_isa_ancestors(all_terms)
    labels = fetch_labels(all_terms)

    # reaction-level view
    rx_info: dict[str, dict] = {}
    rx_entries: dict[str, set[str]] = defaultdict(set)
    for e in entries:
        for r in e["reactions"]:
            rx_info.setdefault(r["rhea"], r)
            rx_entries[r["rhea"]].add(e["acc"])
    mapped = {rx for rx in rx_info if rx in rhea2go}
    go_targets = Counter(rhea2go[rx][0] for rx in mapped)

    # GOA rows contributed by the RHEA pipeline
    rhea_rows = [(acc, a["go"]) for acc, rows in goa.items() for a in rows if a["reference"] == RHEA_GO_REF]

    # entry-level closure-aware reverse gap + generic-only flag
    entry_rows = []
    gap_rows = []
    for e in entries:
        present = {a["go"] for a in goa[e["acc"]] if not a["qualifier"].startswith("NOT")}
        present_closure = set().union(*(closure.get(t, {t}) for t in present)) if present else set()
        mapped_terms = {rhea2go[r["rhea"]][0] for r in e["reactions"] if r["rhea"] in rhea2go}
        missing = sorted(t for t in mapped_terms if t not in present_closure)
        for t in missing:
            rxs = [r["rhea"] for r in e["reactions"] if rhea2go.get(r["rhea"], ("",))[0] == t]
            gap_rows.append([e["acc"], e["gene"], t, labels.get(t, ""), ";".join("RHEA:" + x for x in rxs)])
        n_exp = sum(r["experimental"] for r in e["reactions"])
        n_unmapped = sum(r["rhea"] not in rhea2go for r in e["reactions"])
        entry_rows.append(
            [
                e["acc"], e["gene"], e["organism"], len(e["reactions"]), n_exp,
                len(e["reactions"]) - n_unmapped, n_unmapped, len(mapped_terms),
                len(present), sum(1 for a in goa[e["acc"]] if a["reference"] == RHEA_GO_REF),
                len(missing),
            ]
        )

    reaction_rows = []
    for rx, r in sorted(rx_info.items(), key=lambda kv: -len(rx_entries[kv[0]])):
        go = rhea2go.get(rx)
        ec_terms = ec2go.get(r["ec"], set()) if r["ec"] else set()
        reaction_rows.append(
            [
                f"RHEA:{rx}", r["name"], r["ec"], len(rx_entries[rx]),
                go[0] if go else "", go[1] if go else "",
                ";".join(sorted(ec_terms)),
                "same" if go and go[0] in ec_terms else ("differs" if go and ec_terms else ""),
            ]
        )

    summary = {
        "family": name,
        "title": spec["title"],
        "entries": len(entries),
        "entries_with_rhea": sum(1 for e in entries if e["reactions"]),
        "reaction_annotations": sum(len(e["reactions"]) for e in entries),
        "experimental_reaction_annotations": sum(r["experimental"] for e in entries for r in e["reactions"]),
        "distinct_reactions": len(rx_info),
        "mapped_reactions": len(mapped),
        "unmapped_reactions": len(rx_info) - len(mapped),
        "unmapped_reactions_without_ec": sum(
            1 for rx, r in rx_info.items() if rx not in rhea2go and not r["ec"]
        ),
        "entries_all_reactions_unmapped": sum(
            1 for e in entries if e["reactions"] and all(r["rhea"] not in rhea2go for r in e["reactions"])
        ),
        "distinct_go_targets": len(go_targets),
        "top_go_targets": [
            (go, labels.get(go, ""), n) for go, n in go_targets.most_common(8)
        ],
        "goa_mf_rows": sum(len(v) for v in goa.values()),
        "goa_rows_from_rhea": len(rhea_rows),
        "entries_with_closure_gap": len({g[0] for g in gap_rows}),
        "closure_gap_pairs": len(gap_rows),
    }

    if outdir:
        outdir.mkdir(parents=True, exist_ok=True)
        _tsv(outdir / f"{name}-entries.tsv",
             ["accession", "gene", "organism", "n_reactions", "n_reactions_experimental",
              "n_mapped", "n_unmapped", "n_distinct_mapped_go", "n_goa_mf_terms",
              "n_goa_rows_from_rhea", "n_closure_gap_terms"], entry_rows)
        _tsv(outdir / f"{name}-reactions.tsv",
             ["rhea", "equation", "ec", "n_entries", "rhea2go_id", "rhea2go_label",
              "ec2go_ids", "rhea_vs_ec2go"], reaction_rows)
        _tsv(outdir / f"{name}-entry-reactions.tsv",
             ["accession", "gene", "rhea", "equation", "ec", "experimental", "rhea2go_id"],
             [[e["acc"], e["gene"], f"RHEA:{r['rhea']}", r["name"], r["ec"],
               "yes" if r["experimental"] else "no", rhea2go.get(r["rhea"], ("",))[0]]
              for e in entries for r in e["reactions"]])
        _tsv(outdir / f"{name}-closure-gaps.tsv",
             ["accession", "gene", "missing_go", "missing_go_label", "via_reactions"], gap_rows)
        (outdir / f"{name}-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def _tsv(path: Path, header: list[str], rows: list[list]) -> None:
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--family", choices=sorted(FAMILIES), action="append")
    ap.add_argument("--out", type=Path, help="directory for per-family TSV/JSON output")
    args = ap.parse_args()
    rhea2go, ec2go = load_rhea2go(), load_ec2go()
    for name in args.family or list(FAMILIES):
        s = analyse(name, FAMILIES[name], rhea2go, ec2go, args.out)
        print(json.dumps(s, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
