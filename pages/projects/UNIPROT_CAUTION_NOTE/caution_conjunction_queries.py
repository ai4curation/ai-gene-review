#!/usr/bin/env python3
"""Two CAUTION-driven over-annotation detectors over the local gene corpus.

Both read genes/<sp>/<gene>/<gene>-goa.tsv (+ -uniprot.txt) and need no network
except a one-time GO load via oaklib.

QUERY A - "negated-child / positive-parent" conjunction
-------------------------------------------------------
Within one gene, flag every pair where a molecular-function term X is annotated
POSITIVELY while a more specific term Y (a descendant of X in GO) is annotated as
NOT. This is logically consistent (NOT propagates down, not up) but flags a
fold/domain-based parent annotation whose evidential basis may be gone - the
DPYSL5 pattern. Same-term conflicts (X == Y annotated both positive and NOT) are
reported separately as DIRECT conflicts.

QUERY B - "CAUTION PMID cited positively, never negated"
--------------------------------------------------------
For each gene whose UniProt CAUTION comment cites one or more PMIDs, check the
GOA: if such a PMID supports POSITIVE GO annotation(s) and there is NO NOT
annotation citing that same PMID, flag it. The curator's CAUTION caveat about
that paper may not be reflected as a negation in GO.

Outputs (regenerated): conjunction_hits.tsv, caution_pmid_unnegated.tsv,
caution_conjunction.md
"""
from __future__ import annotations
import csv, glob, re
from collections import defaultdict
from pathlib import Path
from oaklib import get_adapter

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[1]
IS_A = ["rdfs:subClassOf"]            # MF over-annotation is is_a propagation
PMID_RE = re.compile(r"PubMed:(\d+)", re.IGNORECASE)
ELECTRONIC = {"IEA", "IBA"}

def read_goa(path):
    """Yield dict rows for an -goa.tsv file."""
    with open(path) as fh:
        r = csv.reader(fh, delimiter="\t"); next(r, None)
        for row in r:
            if len(row) < 10: continue
            yield {"qual": row[3], "term": row[4], "name": row[5], "aspect": row[6],
                   "evidence": row[8], "ref": row[9]}

def caution_pmids(uniprot_path):
    """Return list of (caution_text, set(pmids)) for each CAUTION comment."""
    if not Path(uniprot_path).exists(): return []
    lines = Path(uniprot_path).read_text(errors="replace").splitlines()
    out, cur = [], None
    for ln in lines:
        if ln.startswith("CC   -!- CAUTION:"):
            if cur is not None: out.append(cur)
            cur = [ln[len("CC   -!- CAUTION:"):].strip()]
        elif cur is not None and ln.startswith("CC       "):
            cur.append(ln[len("CC       "):].strip())
        elif cur is not None:
            out.append(cur); cur = None
    if cur is not None: out.append(cur)
    res = []
    for chunk in out:
        text = " ".join(chunk)
        pmids = set(PMID_RE.findall(text))
        clean = re.sub(r"\{ECO:[^}]*\}", "", text)
        clean = re.sub(r"\s+", " ", clean).strip()
        res.append((clean, pmids))
    return res

def main():
    go = get_adapter("sqlite:obo:go")
    anc_cache = {}
    def ancestors(t):
        if t not in anc_cache:
            anc_cache[t] = set(go.ancestors(t, predicates=IS_A)) - {t}
        return anc_cache[t]

    files = sorted(glob.glob(str(REPO / "genes/*/*/*-goa.tsv")))
    conj_rows, direct_rows, b_rows = [], [], []

    for gf in files:
        gene = Path(gf).name[:-8]
        organism = Path(gf).parts[-3]
        rows = list(read_goa(gf))
        mf = [r for r in rows if r["aspect"] == "molecular_function"]
        pos = [r for r in mf if not r["qual"].startswith("NOT")]
        neg = [r for r in mf if r["qual"].startswith("NOT")]

        # ---- QUERY A ----
        if neg and pos:
            pos_by_term = {}
            for r in pos: pos_by_term.setdefault(r["term"], r)
            neg_by_term = {}
            for r in neg: neg_by_term.setdefault(r["term"], r)
            # experimentally-supported positive MF terms (non-electronic evidence)
            exp_pos_terms = {r["term"] for r in pos if r["evidence"] not in ELECTRONIC}
            for yt, yr in neg_by_term.items():
                ya = ancestors(yt)
                for xt, xr in pos_by_term.items():
                    if xt == yt:
                        direct_rows.append((organism, gene, xt, xr["name"], xr["evidence"], yr["evidence"]))
                    elif xt in ya:
                        # Is the parent X supported by any experimental positive term at or below X
                        # (other than via the NOT-ed child)? If not, X's specificity is unsupported
                        # and this is a DPYSL5-style strong over-annotation candidate.
                        supported = any(zt == xt or xt in ancestors(zt)
                                        for zt in exp_pos_terms if zt != yt)
                        conj_rows.append((organism, gene, xt, xr["name"], xr["evidence"],
                                          yt, yr["name"], yr["evidence"],
                                          "supported" if supported else "UNSUPPORTED"))

        # ---- QUERY B ----
        uni = gf[:-8] + "-uniprot.txt"
        cautions = caution_pmids(uni)
        if not cautions: continue
        # index GOA refs -> negated? positive?
        pos_refs = defaultdict(list)   # pmid -> [(term,name,evidence)]
        not_refs = set()               # pmids appearing on any NOT annotation
        for r in rows:
            m = PMID_RE.search(r["ref"]) or re.search(r"PMID:(\d+)", r["ref"])
            pm = None
            mm = re.search(r"PMID:(\d+)", r["ref"])
            if mm: pm = mm.group(1)
            if not pm: continue
            if r["qual"].startswith("NOT"): not_refs.add(pm)
            else: pos_refs[pm].append((r["term"], r["name"], r["evidence"], r["aspect"]))
        for ctext, cpmids in cautions:
            for pm in cpmids:
                if pm in pos_refs and pm not in not_refs:
                    terms = pos_refs[pm]
                    b_rows.append((organism, gene, pm, len(terms), ctext[:200],
                                   "; ".join(f"{t}({asp[0].upper()},{ev})" for t,_,ev,asp in terms[:6])))

    # ---- write TSVs ----
    with (OUT/"conjunction_hits.tsv").open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["organism","gene","positive_term","positive_name","pos_evidence",
                    "negated_term","negated_name","neg_evidence","parent_support"])
        for r in sorted(conj_rows): w.writerow(r)
    with (OUT/"caution_pmid_unnegated.tsv").open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["organism","gene","caution_pmid","n_pos_annotations","caution_text","positive_terms"])
        for r in sorted(b_rows): w.writerow(r)

    # ---- markdown ----
    conj_elec = [r for r in conj_rows if r[4] in ELECTRONIC]
    conj_strong = [r for r in conj_elec if r[8] == "UNSUPPORTED"]
    md = OUT/"caution_conjunction.md"
    with md.open("w") as fh:
        fh.write("---\ntitle: \"CAUTION conjunction & PMID-without-NOT queries\"\n---\n\n")
        fh.write("# CAUTION-driven over-annotation queries (local corpus)\n\n")
        fh.write("Auto-generated by `caution_conjunction_queries.py`. Do not edit by hand.\n\n")
        fh.write(f"Corpus: {len(files)} genes with GOA.\n\n")
        fh.write("## Query A - negated-child / positive-parent conjunctions\n\n")
        fh.write(f"- Conjunction hits (positive ancestor + NOT descendant): **{len(conj_rows)}** "
                 f"across {len({(r[0],r[1]) for r in conj_rows})} genes.\n")
        fh.write(f"- With an electronic (IEA/IBA) positive parent: **{len(conj_elec)}**.\n")
        fh.write(f"- **STRONG candidates** (electronic parent whose specificity has NO experimental "
                 f"positive support = DPYSL5 pattern): **{len(conj_strong)}**.\n")
        fh.write(f"- DIRECT same-term conflicts (term annotated both positive and NOT): "
                 f"**{len(direct_rows)}** across {len({(r[0],r[1]) for r in direct_rows})} genes.\n\n")
        fh.write("### STRONG over-annotation candidates (electronic parent, no experimental support)\n\n")
        fh.write("| Gene | positive parent (evidence) | NOT-ed child (evidence) |\n|---|---|---|\n")
        for o,g,xt,xn,xe,yt,yn,ye,sup in sorted(conj_strong):
            fh.write(f"| {o}/{g} | {xt} {xn} ({xe}) | {yt} {yn} ({ye}) |\n")
        fh.write("\n### Other electronic-parent conjunctions (parent likely legitimately retained)\n\n")
        fh.write("| Gene | positive parent (evidence) | NOT-ed child (evidence) | parent support |\n|---|---|---|---|\n")
        for o,g,xt,xn,xe,yt,yn,ye,sup in sorted(r for r in conj_elec if r[8]=="supported"):
            fh.write(f"| {o}/{g} | {xt} {xn} ({xe}) | {yt} {yn} ({ye}) | {sup} |\n")
        fh.write("\n### DIRECT same-term conflicts\n\n")
        fh.write("| Gene | term (positive evidence / NOT evidence) |\n|---|---|\n")
        for o,g,t,n,pe,ne in sorted(direct_rows):
            fh.write(f"| {o}/{g} | {t} {n} ({pe} vs NOT:{ne}) |\n")
        fh.write("\n## Query B - CAUTION PMID cited positively, never negated\n\n")
        fh.write(f"- Flagged (gene, PMID) pairs: **{len(b_rows)}** across "
                 f"{len({(r[0],r[1]) for r in b_rows})} genes.\n\n")
        fh.write("| Gene | CAUTION PMID | #pos | positive GO terms | CAUTION (truncated) |\n|---|---|--:|---|---|\n")
        for o,g,pm,n,ct,terms in sorted(b_rows):
            fh.write(f"| {o}/{g} | PMID:{pm} | {n} | {terms} | {ct.replace('|','/')} |\n")
    print(f"Query A: {len(conj_rows)} conjunctions ({len(conj_elec)} electronic), "
          f"{len(direct_rows)} direct conflicts")
    print(f"Query B: {len(b_rows)} CAUTION-PMID-without-NOT flags")
    print("wrote", md)

if __name__ == "__main__":
    main()
