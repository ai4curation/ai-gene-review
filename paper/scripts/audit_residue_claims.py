"""Scripted audit of residue-loss arguments made in review prose.

The original survey behind the residue-claim validator (4 of 17 "lacks the catalytic
residue" claims made about intact sites: CASP12, LPA, AZIN1, HSPA13) was done by hand and
its list of 17 was not preserved. This script re-runs the harvest reproducibly:

1. Find every existing-annotation row whose review summary or reason asserts that the
   protein lacks, lost or has a degenerate catalytic / active-site residue.
2. For each such gene, record whether the review also carries structured residue claims
   (checked by ai_gene_review.validation.gene_residue_claims), and whether the protein's
   own UniProt record annotates an active site (FT ACT_SITE).
3. Flag rows where prose asserts loss, the protein's own record annotates an active site,
   and no structured claim exists. A flag is a lead for re-checking, not a verdict: UniProt
   annotates ACT_SITE by similarity too, and a protein can keep the site and still lose
   activity for other reasons.

Outputs: paper/release/residue_loss_prose_claims.tsv, paper/generated/stats_audit.{tex,json}
"""
import csv, glob, json, os, re
from concurrent.futures import ProcessPoolExecutor
import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PAPER = os.path.join(ROOT, "paper")
NAMED = ["CASP12", "LPA", "AZIN1", "HSPA13"]   # the four intact-site cases recorded in the schema

# Mechanism claims: a named catalytic / active-site residue or site is lost. Plain statements that a
# protein is "catalytically inactive" or a "pseudoenzyme" are counted separately (INACTIVE) and are not
# flagged: AZIN1 is genuinely inactive; the survey's error was blaming a residue it actually keeps.
LOSS = re.compile(
    r"\b(lacks?|lacking|lost|loses|loss of|missing|absent|devoid of|without|replaced|substitut\w+)\b[^.;]{0,40}?"
    r"\b(?:catalytic|active[- ]site)\s+(?:residues?|cysteines?|serines?|histidines?|aspartates?|glutamates?|lysines?|"
    r"tyrosines?|nucleophiles?|triad|dyad|motif|site)\b"
    r"|\b(lacks?|lacking|lost|loss of|missing|absent|without)\b[^.;]{0,30}?\bnucleophil\w*", re.I)
INACTIVE = re.compile(r"\b(catalytically (?:inactive|dead|inert|incompetent)|degenerate (?:active|catalytic) site|pseudo-?enzyme)\b", re.I)
STRONG = ("ECO:0000255", "ECO:0000269")   # sequence-analysis (motif/ProRule) or experimental ACT_SITE

def act_sites(folder):
    """(strong, all) counts of FT ACT_SITE features on the protein's own UniProt record."""
    for f in glob.glob(os.path.join(folder, "*-uniprot.txt")):
        lines = open(f, errors="replace").read().splitlines()
        strong = total = 0
        for i, line in enumerate(lines):
            if line.startswith("FT   ACT_SITE"):
                total += 1
                block = " ".join(lines[i + 1:i + 4])
                strong += any(e in block.split("|")[0] if "evidence=" in block else False for e in STRONG)
        return strong, total
    return 0, 0

def one(path):
    try:
        with open(path) as fh:
            d = yaml.load(fh, Loader=Loader)
    except Exception:
        return []
    if not isinstance(d, dict):
        return []
    org = os.path.relpath(path, ROOT).split(os.sep)[1]
    gene = d.get("gene_symbol")
    rows, structured = [], 0
    n_inactive_rows = [0]
    for a in d.get("existing_annotations") or []:
        if not isinstance(a, dict):
            continue
        r = a.get("review") or {}
        pr = r.get("propagation_review") or {}
        structured += len(pr.get("residue_claims") or []) if isinstance(pr, dict) else 0
        text = " ".join(str(r.get(k) or "") for k in ("summary", "reason"))
        m = LOSS.search(text)
        if INACTIVE.search(text):
            n_inactive_rows[0] += 1
        if m:
            s = max(0, m.start() - 80)
            rows.append({"organism": org, "gene": gene, "id": d.get("id"), "term_id": (a.get("term") or {}).get("id"),
                         "term_label": (a.get("term") or {}).get("label"), "evidence_type": a.get("evidence_type"),
                         "action": r.get("action"), "snippet": " ".join(text[s:m.end() + 80].split())})
    if not rows:
        return [{"_inactive_only": n_inactive_rows[0]}] if n_inactive_rows[0] else []
    strong, total = act_sites(os.path.dirname(path))
    for row in rows:
        row["gene_structured_claims"] = structured
        row["uniprot_act_sites"] = total
        row["uniprot_act_sites_strong"] = strong
        row["flag"] = strong > 0 and structured == 0
    rows[0]["_inactive_rows"] = n_inactive_rows[0]
    return rows

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml")))
    with ProcessPoolExecutor() as ex:
        raw = [r for rs in ex.map(one, files, chunksize=50) for r in rs]
    n_inactive = sum(r.get("_inactive_only", 0) + r.get("_inactive_rows", 0) for r in raw)
    rows = [{k: v for k, v in r.items() if not k.startswith("_")} for r in raw if "_inactive_only" not in r]
    os.makedirs(os.path.join(PAPER, "release"), exist_ok=True)
    with open(os.path.join(PAPER, "release", "residue_loss_prose_claims.tsv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader(); w.writerows(rows)
    genes = {(r["organism"], r["gene"]) for r in rows}
    gstruct = {(r["organism"], r["gene"]) for r in rows if r["gene_structured_claims"]}
    gact = {(r["organism"], r["gene"]) for r in rows if r["uniprot_act_sites"]}
    gflag = {(r["organism"], r["gene"]) for r in rows if r["flag"]}
    named = {g: [r for r in rows if r["gene"] == g and r["organism"] == "human"] for g in NAMED}
    macros = {
        "nAuditRows": f"{len(rows):,}", "nAuditGenes": f"{len(genes):,}",
        "nAuditGenesStructured": f"{len(gstruct):,}", "nAuditGenesActSite": f"{len(gact):,}",
        "nAuditGenesFlagged": f"{len(gflag):,}", "nAuditRowsFlagged": f"{sum(r['flag'] for r in rows):,}",
        "nAuditNamedStillProse": str(sum(1 for g in NAMED if named[g])),
        "nAuditInactiveRows": f"{n_inactive:,}",
    }
    with open(os.path.join(PAPER, "generated", "stats_audit.tex"), "w") as fh:
        fh.write("% generated by scripts/audit_residue_claims.py -- do not edit\n")
        for k, v in sorted(macros.items()):
            fh.write(f"\\newcommand{{\\{k}}}{{{v}}}\n")
    with open(os.path.join(PAPER, "generated", "stats_audit.json"), "w") as fh:
        json.dump({**macros, "named_cases": {g: [(r["term_id"], r["action"]) for r in v] for g, v in named.items()}}, fh, indent=1)
    print(json.dumps(macros, indent=1))
    for g, v in named.items():
        print(g, [(r["term_id"], r["action"], r["snippet"][:90]) for r in v][:3])

if __name__ == "__main__":
    main()
