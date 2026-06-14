#!/usr/bin/env python3
"""Inventory deposited PDB structures across all genes in the review pipeline.

Offline: parses the cached ``*-uniprot.txt`` records (UniProt ``DR PDB`` cross-
references) and the cached ``*-goa.tsv`` files. No network access required.

Outputs (written next to this script, in ``data/``):
  - pdb_inventory.tsv      one row per deposited PDB entry
  - pdb_gene_summary.tsv   one row per gene, with aggregate + prioritization signals

The "functional insight" prioritization rationale lives in ../PDB.md; the
offline signals computed here are:
  - structure coverage of the protein (fragment vs full-length)
  - experimental method / best resolution
  - how sparsely the gene is currently annotated with EXPERIMENTAL GO terms
    (a structure adds the most where we know the least)
These are combined with RCSB ligand/complex enrichment in enrich_rcsb.py.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
GENES = REPO / "genes"
OUTDIR = Path(__file__).resolve().parent / "data"
OUTDIR.mkdir(exist_ok=True)

# GO evidence codes that reflect direct experimental characterization
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}
HIGH_THROUGHPUT = {"HTP", "HDA", "HMP", "HGI", "HEP"}

# Organism codes treated as eukaryotic (so euk candidates aren't drowned out).
EUKARYOTES = {
    "human", "mouse", "rat", "worm", "yeast", "ARATH", "SCHPO", "SCHJY", "DANRE", "DROME",
    "XENTR", "CHICK", "BOVIN", "CRIGR", "DICDI", "CHLRE", "CANAL", "CANGA", "NEUCR", "ASPNG",
    "ASPRC", "PICST", "HYPJE", "PENCH", "PENEN", "MAIZE", "ORYSJ", "SOYBN", "SOLLC", "SOLTU",
    "VITVI", "WHEAT", "MEDTR", "POPTR", "PHYPA", "BRADI", "SORBI", "PHAVU", "THLAR", "TOBAC",
    "NICAT", "OCTBM", "OCTVU", "SEPOF", "EUPSC", "DAPPU", "RAMVA", "MISSI", "DESRO", "DOROP",
    "DORPE", "9POAL",
}

# Review actions that mark an annotation as contested/disputed.
CONTESTED_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
# Catalytic-activity labels: the pseudo-enzyme case where structure is decisive.
CATALYTIC = re.compile(
    r"(ase activity|catalytic activity|\bkinase\b|transferase|hydrolase|oxidase|reductase|"
    r"dehydrogenase|\bligase\b|\blyase\b|isomerase|synthase|synthetase|phosphatase|"
    r"peptidase|protease|demethylase|methyltransferase|deacetylase|nuclease|polymerase|"
    r"cyclase|dioxygenase|monooxygenase|oxidoreductase|decarboxylase|hydratase|aldolase|"
    r"esterase)", re.I)

# DR   PDB; 1AIE; X-ray; 1.50 A; A=326-356.
PDB_LINE = re.compile(
    r"^DR\s+PDB;\s*(?P<id>\S+);\s*(?P<method>[^;]+);\s*(?P<res>[^;]+);\s*(?P<chains>.+)\.\s*$"
)
RANGE = re.compile(r"=(\d+)-(\d+)")


@dataclass
class GeneRec:
    organism: str
    gene: str
    uniprot: str = ""
    length: int = 0
    pdb_entries: list = field(default_factory=list)
    # GOA-derived annotation signals
    exp_mf: int = 0
    exp_bp: int = 0
    exp_cc: int = 0
    exp_total: int = 0
    any_exp: bool = False
    aspect: dict = field(default_factory=dict)
    # review-derived contested-catalytic signal
    contested_cat_mf: list = field(default_factory=list)


def parse_uniprot(path: Path):
    organism = path.parent.parent.name
    gene = path.parent.name
    rec = GeneRec(organism=organism, gene=gene)
    text = path.read_text(errors="replace")
    for line in text.splitlines():
        if line.startswith("AC ") and not rec.uniprot:
            rec.uniprot = line.split()[1].rstrip(";")
        elif line.startswith("SQ "):
            m = re.search(r"SEQUENCE\s+(\d+)\s+AA", line)
            if m:
                rec.length = int(m.group(1))
        elif line.startswith("DR   PDB;"):
            m = PDB_LINE.match(line)
            if not m:
                continue
            pdb_id = m.group("id")
            method = m.group("method").strip()
            res = m.group("res").strip()
            chains = m.group("chains").strip()
            ranges = [(int(a), int(b)) for a, b in RANGE.findall(chains)]
            rec.pdb_entries.append((pdb_id, method, res, chains, ranges))
    return rec


def coverage_fraction(ranges, length):
    if not length or not ranges:
        return 0.0
    covered = set()
    for a, b in ranges:
        if b >= a:
            covered.update(range(a, b + 1))
    return min(1.0, len(covered) / length)


def parse_goa(path: Path, rec: GeneRec):
    if not path.exists():
        return
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            ev = (row.get("GO EVIDENCE CODE") or "").strip()
            aspect = (row.get("GO ASPECT") or "").strip()
            term = (row.get("GO TERM") or "").strip()
            if term:
                rec.aspect[term] = aspect
            if ev in EXPERIMENTAL:
                rec.any_exp = True
                rec.exp_total += 1
                if aspect == "molecular_function":
                    rec.exp_mf += 1
                elif aspect == "biological_process":
                    rec.exp_bp += 1
                elif aspect == "cellular_component":
                    rec.exp_cc += 1


def parse_review_contested(path: Path, rec: GeneRec):
    """Flag molecular-function CATALYTIC terms the review disputed (REMOVE/OVER)."""
    if not path.exists():
        return
    try:
        doc = yaml.safe_load(path.read_text())
    except Exception:
        return
    for ann in (doc or {}).get("existing_annotations", []) or []:
        term = (ann.get("term") or {})
        tid, lab = term.get("id"), term.get("label", "") or ""
        act = (ann.get("review") or {}).get("action")
        if (tid and act in CONTESTED_ACTIONS
                and rec.aspect.get(tid) == "molecular_function"
                and "binding" not in lab.lower()
                and CATALYTIC.search(lab)):
            rec.contested_cat_mf.append(f"{tid}|{lab}|{act}")


def main():
    uniprot_files = sorted(GENES.glob("*/*/*-uniprot.txt"))
    inv_rows = []
    gene_rows = []
    for up in uniprot_files:
        rec = parse_uniprot(up)
        if not rec.pdb_entries:
            continue
        goa = up.with_name(up.name.replace("-uniprot.txt", "-goa.tsv"))
        parse_goa(goa, rec)
        review = up.with_name(up.name.replace("-uniprot.txt", "-ai-review.yaml"))
        parse_review_contested(review, rec)

        max_cov = 0.0
        best_res = None
        methods = set()
        for (pdb_id, method, res, chains, ranges) in rec.pdb_entries:
            cov = coverage_fraction(ranges, rec.length)
            max_cov = max(max_cov, cov)
            methods.add(method)
            res_val = None
            rm = re.search(r"([\d.]+)\s*A", res)
            if rm:
                res_val = float(rm.group(1))
                if best_res is None or res_val < best_res:
                    best_res = res_val
            inv_rows.append({
                "organism": rec.organism,
                "gene": rec.gene,
                "uniprot": rec.uniprot,
                "length": rec.length,
                "pdb_id": pdb_id,
                "method": method,
                "resolution_A": f"{res_val:.2f}" if res_val is not None else "",
                "chains": chains,
                "coverage_frac": f"{cov:.3f}",
            })

        gene_rows.append({
            "organism": rec.organism,
            "gene": rec.gene,
            "uniprot": rec.uniprot,
            "is_eukaryote": int(rec.organism in EUKARYOTES),
            "length": rec.length,
            "n_pdb": len(rec.pdb_entries),
            "methods": ";".join(sorted(methods)),
            "best_resolution_A": f"{best_res:.2f}" if best_res is not None else "",
            "max_coverage_frac": f"{max_cov:.3f}",
            "exp_mf": rec.exp_mf,
            "exp_bp": rec.exp_bp,
            "exp_cc": rec.exp_cc,
            "exp_total": rec.exp_total,
            "any_experimental": int(rec.any_exp),
            "n_contested_cat_mf": len(rec.contested_cat_mf),
            "contested_cat_mf": ";".join(rec.contested_cat_mf),
        })

    inv_rows.sort(key=lambda r: (r["organism"], r["gene"], r["pdb_id"]))
    gene_rows.sort(key=lambda r: (-r["n_pdb"], r["organism"], r["gene"]))

    inv_path = OUTDIR / "pdb_inventory.tsv"
    with inv_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(inv_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(inv_rows)

    gene_path = OUTDIR / "pdb_gene_summary.tsv"
    with gene_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(gene_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(gene_rows)

    # Console summary
    n_genes = len(gene_rows)
    n_entries = len(inv_rows)
    by_org = {}
    for r in gene_rows:
        by_org[r["organism"]] = by_org.get(r["organism"], 0) + 1
    no_exp = sum(1 for r in gene_rows if not r["any_experimental"])
    no_exp_mf = sum(1 for r in gene_rows if r["exp_mf"] == 0)
    euk = sum(1 for r in gene_rows if r["is_eukaryote"])
    contested = sum(1 for r in gene_rows if r["n_contested_cat_mf"])
    print(f"Genes with >=1 PDB structure: {n_genes}")
    print(f"Total deposited PDB entries:  {n_entries}")
    print(f"Eukaryotic genes with structure:      {euk}")
    print(f"Genes with NO experimental GO at all: {no_exp}")
    print(f"Genes with NO experimental MF GO:     {no_exp_mf}")
    print(f"Genes w/ contested catalytic MF:      {contested}")
    print("Top organisms by #genes-with-structure:")
    for org, n in sorted(by_org.items(), key=lambda x: -x[1])[:10]:
        print(f"  {org:8s} {n}")
    print(f"\nWrote {inv_path.relative_to(REPO)}")
    print(f"Wrote {gene_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
