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


def bc4go_annotations():
    """(pmid, gene symbol upper) -> list of BC4GO gold annotations (training + development sets)."""
    import xml.etree.ElementTree as ET

    out = defaultdict(list)
    base = os.path.join(RAW, "bc4go")
    paths = glob.glob(os.path.join(base, "BC4GO Corpus Training Set v1", "Annotations", "*.xml"))
    paths += glob.glob(os.path.join(base, "bc4go_dev_v081213", "annotations", "*.xml"))
    for p in paths:
        split = "training" if "Training" in p else "development"
        for doc in ET.parse(p).getroot().iter("document"):
            pmid = doc.findtext("id")
            for ann in doc.iter("annotation"):
                inf = {i.get("key"): (i.text or "") for i in ann.findall("infon")}
                gene = inf.get("gene", "")
                symbol, _, geneid = gene.rpartition("(")
                label, _, goid = inf.get("go-term", "").rpartition("|")
                out[(pmid, symbol.strip().upper())].append({
                    "split": split,
                    "gene": gene,
                    "ncbi_gene": geneid.rstrip(")"),
                    "go_term": goid,
                    "go_name": label,
                    "evidence": inf.get("goevidence"),
                    "sentence": ann.findtext("text"),
                })
    return out


def bc4go():
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A, PART_OF

    go = get_adapter("sqlite:obo:go")
    preds = [IS_A, PART_OF]
    anc = {}

    def ancestors(t):
        if t not in anc:
            anc[t] = set(go.ancestors(t, predicates=preds, reflexive=False)) if t.startswith("GO:") else set()
        return anc[t]

    def current(t):
        """Follow replaced_by for terms obsoleted since 2013 (e.g. GO:0030529 -> GO:1990904)."""
        repl = go.entity_metadata_map(t).get("IAO:0100001") if t.startswith("GO:") else None
        return repl[0] if repl else t

    def relation(a, b):
        a = current(a)
        if a == b:
            return "exact"
        if b in ancestors(a):
            return "bc4go_more_specific"
        if a in ancestors(b):
            return "goa_more_specific"
        return None

    # BC4GO genes carry NCBI Gene ids; join on those, not symbols (fly Cdc42 is not mouse Cdc42)
    gold = defaultdict(list)
    for (pmid, _sym), anns in bc4go_annotations().items():
        for a in anns:
            gold[(pmid, a["ncbi_gene"])].append(a)
    folders = defaultdict(list)
    for d in glob.glob(os.path.join(ROOT, "genes", "*", "*")):
        up = os.path.join(d, f"{os.path.basename(d)}-uniprot.txt")
        if os.path.exists(up):
            with open(up) as fh:
                for line in fh:
                    if line.startswith("DR   GeneID;"):
                        folders[line.split(";")[1].strip()].append(d)

    results = []
    for (pmid, geneid), anns in sorted(gold.items()):
        sym = anns[0]["gene"]
        for d in folders.get(geneid, []):
            goa_rows = rows_for(d, pmid)
            if not goa_rows:
                continue
            bc_terms = {}
            for a in anns:
                bc_terms.setdefault(a["go_term"], {**a, "sentences": []})["sentences"].append(a["sentence"])
            comparisons = []
            for t, a in bc_terms.items():
                best = [(relation(t, r["go_term"]), r) for r in goa_rows]
                best = [x for x in best if x[0]]
                comparisons.append({
                    "bc4go_term": t,
                    "bc4go_term_current": current(t),
                    "bc4go_name": a["go_name"],
                    # NONE marks a "summary type" sentence: states what was found, not how,
                    # so it cannot support a complete annotation on its own (Van Auken 2014)
                    "bc4go_evidence": a["evidence"],
                    "bc4go_sentences": a["sentences"],
                    "goa_matches": [
                        {"relation": rel, "go_term": r["go_term"], "go_name": r["go_name"],
                         "evidence": r["evidence"], "our_action": r["our_action"]}
                        for rel, r in best
                    ],
                })
            goa_only = [r for r in goa_rows if not any(relation(t, r["go_term"]) for t in bc_terms)]
            results.append({
                "pmid": pmid,
                "gene": sym,
                "gene_folder": os.path.relpath(d, ROOT),
                "bc4go_terms": comparisons,
                "goa_rows_not_in_bc4go": goa_only,
            })
    return results


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fn in [("keseler2014", keseler), ("cusick2009", cusick), ("camon2005", camon), ("bc4go", bc4go)]:
        data = fn()
        with open(os.path.join(OUT, f"{name}.yaml"), "w") as fh:
            yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True, width=120)
        print(f"{name}: {len(data)} items -> crosscheck/{name}.yaml", file=sys.stderr)


if __name__ == "__main__":
    main()
