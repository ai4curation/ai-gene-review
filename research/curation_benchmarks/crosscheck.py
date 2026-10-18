"""Cross-check published manual-curation benchmark datasets against this repo.

For every item a benchmark scored, find the GOA rows in genes/*/*/*-goa.tsv
that cite the same publication for the same gene product, and report how our
review (the matching existing_annotations entry) judged each row.

Inputs (downloaded into raw/, see README.md):
  raw/keseler2014/Supplemental.xlsx     EcoCyc + CGD fact validation
  raw/cusick2009/dataset{2,3}.xls       human PPI recuration
  camon2005_iaa.yaml                    transcribed from Camon 2005 Additional File 1

Usage: uv run --with xlrd python -I research/curation_benchmarks/crosscheck.py
"""

import csv
import glob
import os
import sys
from collections import defaultdict

import openpyxl
import xlrd
import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "crosscheck")


def gene_dirs(org):
    return {os.path.basename(d).upper(): d for d in glob.glob(os.path.join(ROOT, "genes", org, "*"))}


def load_gene(d):
    """Return (goa rows, {(term, ref, evidence): action}) for one gene folder."""
    sym = os.path.basename(d)
    goa = []
    p = os.path.join(d, f"{sym}-goa.tsv")
    if os.path.exists(p):
        with open(p) as fh:
            goa = list(csv.DictReader(fh, delimiter="\t"))
    actions = {}
    p = os.path.join(d, f"{sym}-ai-review.yaml")
    if os.path.exists(p):
        with open(p) as fh:
            doc = yaml.load(fh, Loader=Loader) or {}
        for a in doc.get("existing_annotations") or []:
            key = ((a.get("term") or {}).get("id"), a.get("original_reference_id"), a.get("evidence_type"))
            actions[key] = (a.get("review") or {}).get("action")
    return goa, actions


def rows_for(d, pmid, accession=None):
    goa, actions = load_gene(d)
    out = []
    for r in goa:
        if r["REFERENCE"] != f"PMID:{pmid}":
            continue
        if accession and r["GENE PRODUCT ID"].split("-")[0] != accession:
            continue
        key = (r["GO TERM"], r["REFERENCE"], r["GO EVIDENCE CODE"])
        out.append({
            "go_term": r["GO TERM"],
            "go_name": r["GO NAME"],
            "evidence": r["GO EVIDENCE CODE"],
            "with_from": r["WITH/FROM"],
            "qualifier": r["QUALIFIER"],
            "assigned_by": r["ASSIGNED BY"],
            "our_action": actions.get(key, "NOT_IN_REVIEW"),
        })
    return out


def keseler():
    wb = openpyxl.load_workbook(os.path.join(RAW, "keseler2014", "Supplemental.xlsx"), read_only=True)
    results = []
    for sheet, org in [("EcoCyc", "ECOLI"), ("CGD", "CANAL")]:
        dirs = gene_dirs(org)
        for r in list(wb[sheet].iter_rows(values_only=True))[1:]:
            if not r[3]:
                continue
            gene_id, gene, _protein, fact, score, modify, pub, vcom, dcom = r[:9]
            final = str(modify if modify not in (None, "X") else score).strip().lower()
            pmid = str(pub).strip() if isinstance(pub, (int, float)) or str(pub).strip().isdigit() else None
            if pmid and pmid.endswith(".0"):
                pmid = pmid[:-2]
            d = dirs.get(str(gene).upper())
            results.append({
                "database": sheet,
                "gene_id": gene_id,
                "gene": gene,
                "fact": str(fact).strip(),
                "validator_score": str(score).strip(),
                "adjudicated": modify,
                "final_correct": final == "yes",
                "pmid": pmid,
                "validator_comment": vcom,
                "database_comment": dcom,
                "in_repo": bool(d),
                "goa_rows_citing_pmid": rows_for(d, pmid) if d and pmid else [],
            })
    return results


def human_accessions():
    """Gene symbol (upper) -> UniProt accession, from the review files' id field."""
    out = {}
    for p in glob.glob(os.path.join(ROOT, "genes", "human", "*", "*-ai-review.yaml")):
        with open(p) as fh:
            for line in fh:
                if line.startswith("id:"):
                    out[os.path.basename(os.path.dirname(p)).upper()] = line.split(":", 1)[1].strip()
                    break
    return out


def cusick():
    dirs = gene_dirs("human")
    accs = human_accessions()
    results = []
    for i, label in [(2, "LC-multiple"), (3, "LC-random")]:
        s = xlrd.open_workbook(os.path.join(RAW, "cusick2009", f"dataset{i}.xls")).sheet_by_index(0)
        h = s.row_values(0)
        for n in range(1, s.nrows):
            r = dict(zip(h, s.row_values(n)))
            a = r.get("Gene Symbol A") or r.get("Interactor A GeneSymbol")
            b = r.get("Gene Symbol B") or r.get("Interactor B GeneSymbol")
            pub = r.get("Pubmed ID") or r.get("Publication")
            if not a or not pub:
                continue
            pmid = str(int(pub)) if isinstance(pub, float) else str(pub).strip()
            err = str(r.get("Error", "")).strip()
            hits = {}
            for g, partner in ((a, b), (b, a)):
                d = dirs.get(str(g).upper())
                if d:
                    rows = rows_for(d, pmid)
                    pacc = accs.get(str(partner).upper())
                    for row in rows:
                        # None when the partner has no review folder, so its accession is unknown here
                        row["with_names_scored_partner"] = (pacc in row["with_from"]) if pacc else None
                    hits[g] = rows
            results.append({
                "dataset": label,
                "gene_a": a,
                "gene_b": b,
                "pmid": pmid,
                "assay": r.get("Name of assay") or r.get("Interaction Assay"),
                "bona_fide": r.get("Is int bonafide?") or r.get("Is the interaction bonafide?"),
                "species_a": r.get("ProteinA species") or r.get("Protein A Species"),
                "species_b": r.get("ProteinB species") or r.get("Protein B Species"),
                "error": err if err.lower() not in ("", "none") else None,
                "comment": r.get("Comments"),
                "goa_rows_citing_pmid": hits,
            })
    return results


def camon():
    with open(os.path.join(HERE, "camon2005_iaa.yaml")) as fh:
        pairs = yaml.safe_load(fh)["pairs"]
    acc2dir = {}
    for p in glob.glob(os.path.join(ROOT, "genes", "human", "*", "*-ai-review.yaml")):
        with open(p) as fh:
            for line in fh:
                if line.startswith("id:"):
                    acc2dir[line.split(":", 1)[1].strip()] = os.path.dirname(p)
                    break
    for p in pairs:
        d = acc2dir.get(p["uniprot"])
        p["gene_folder"] = os.path.relpath(d, ROOT) if d else None
        p["goa_rows_citing_pmid"] = rows_for(d, p["pmid"], p["uniprot"]) if d else []
    return pairs


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fn in [("keseler2014", keseler), ("cusick2009", cusick), ("camon2005", camon)]:
        data = fn()
        with open(os.path.join(OUT, f"{name}.yaml"), "w") as fh:
            yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True, width=120)
        print(f"{name}: {len(data)} items -> crosscheck/{name}.yaml", file=sys.stderr)


if __name__ == "__main__":
    main()
