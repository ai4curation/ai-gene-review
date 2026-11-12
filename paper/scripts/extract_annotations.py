"""Flatten every gene review's existing_annotations into one table.

Output: paper/data/annotations.tsv (one row per reviewed annotation) and
paper/data/reviews.tsv (one row per review file). Nothing is hardcoded:
all paper statistics derive from these tables.
"""
import csv, glob, os, sys
from concurrent.futures import ProcessPoolExecutor
import yaml

try:
    Loader = yaml.CSafeLoader
except AttributeError:
    Loader = yaml.SafeLoader

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "paper", "data")

def ref_source(ref):
    ref = ref or ""
    if ref.startswith("GO_REF:"):
        return ref
    return ref.split(":")[0] if ":" in ref else ref

def clade(path, taxon_id):
    """Coarse clade from the UniProt OC lineage lines in the gene folder."""
    oc = ""
    for f in glob.glob(os.path.join(os.path.dirname(path), "*-uniprot.txt")):
        with open(f, errors="replace") as fh:
            oc = " ".join(l[5:].strip() for l in fh if l.startswith("OC   "))
        break
    if taxon_id == "NCBITaxon:9606": return "Human"
    if oc.startswith("Viruses"): return "Viruses and phages"
    if oc.startswith("Archaea"): return "Archaea"
    if oc.startswith("Bacteria"): return "Bacteria"
    if not oc.startswith("Eukaryota"): return "Unknown"
    if "Mammalia" in oc: return "Other mammals"
    if "Metazoa" in oc: return "Other animals"
    if "Viridiplantae" in oc: return "Plants and algae"
    if "Fungi" in oc: return "Fungi"
    return "Protists"

def one(path):
    rel = os.path.relpath(path, ROOT)
    org = rel.split(os.sep)[1]
    try:
        with open(path) as fh:
            d = yaml.load(fh, Loader=Loader)
    except Exception as e:  # noqa
        return None, [], rel
    if not isinstance(d, dict):
        return None, [], rel
    anns = d.get("existing_annotations") or []
    grp = clade(path, (d.get("taxon") or {}).get("id"))
    rows = []
    for a in anns:
        if not isinstance(a, dict):
            continue
        t = a.get("term") or {}
        r = a.get("review") or {}
        rows.append({
            "organism": org, "clade": grp,
            "gene": d.get("gene_symbol"),
            "id": d.get("id"),
            "term_id": t.get("id"),
            "term_label": t.get("label"),
            "evidence_type": a.get("evidence_type"),
            "reference": a.get("original_reference_id"),
            "ref_source": ref_source(a.get("original_reference_id")),
            "negated": bool(a.get("negated")),
            "action": r.get("action") or "NONE",
            "n_replacements": len(r.get("proposed_replacement_terms") or []),
            "has_source_defects": bool(r.get("source_defects")),
        })
    rev = {
        "organism": org, "clade": grp, "gene": d.get("gene_symbol"), "id": d.get("id"),
        "path": rel, "n_annotations": len(rows),
        "n_core_functions": len(d.get("core_functions") or []),
        "n_references": len(d.get("references") or []),
        "n_proposed_new_terms": len(d.get("proposed_new_terms") or []),
        "n_knowledge_gaps": len(d.get("knowledge_gaps") or []),
        "n_gene_model_issues": len(d.get("gene_model_issues") or []),
    }
    return rev, rows, None

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml")))
    os.makedirs(OUT, exist_ok=True)
    revs, rows, bad = [], [], []
    with ProcessPoolExecutor() as ex:
        for rev, rs, err in ex.map(one, files, chunksize=50):
            if err:
                bad.append(err); continue
            revs.append(rev); rows.extend(rs)
    for name, data in (("reviews.tsv", revs), ("annotations.tsv", rows)):
        with open(os.path.join(OUT, name), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0].keys()), delimiter="\t")
            w.writeheader(); w.writerows(data)
    print(f"{len(revs)} reviews, {len(rows)} annotations, {len(bad)} unparseable", file=sys.stderr)

if __name__ == "__main__":
    main()
