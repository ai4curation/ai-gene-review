#!/usr/bin/env python3
"""Scale the CAUTION over-annotation queries UniProt-wide via the QuickGO API.

Inputs:
    caution_uniprot_reviewed.tsv   (from uniprot_api_survey.py; accession + caution text)
Pulls (cached):
    caution_mf_goa.tsv             molecular-function GOA for every CAUTION accession
Outputs:
    uniprot_wide_conjunctions.tsv  Query A hits (with STRONG triage + net-new flag)
    uniprot_wide_pmid.tsv          Query B hits (CAUTION-PMID cited positively, never negated)
    uniprot_wide_queries.md        summary

Query A: positive MF term X + NOT MF descendant Y in the same gene (GO ancestry via
oaklib). STRONG = electronic parent with no experimental positive support (DPYSL5
pattern). Query B: a PMID cited in the UniProt CAUTION that supports a positive MF
annotation but no NOT annotation. "net_new" = accession not already in genes/.
"""
from __future__ import annotations
import csv, glob, re, sys, time, json, urllib.request, urllib.parse
from collections import defaultdict
from pathlib import Path
from oaklib import get_adapter

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[1]
SURVEY = OUT / "caution_uniprot_reviewed.tsv"
GOA_CACHE = OUT / "caution_mf_goa.tsv"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
PMID_RE = re.compile(r"PubMed:(\d+)", re.IGNORECASE)
ELECTRONIC = {"IEA", "IBA"}
BATCH = 20

def local_accessions():
    acc = set()
    for p in REPO.glob("genes/*/*/*-uniprot.txt"):
        for line in p.read_text(errors="replace").splitlines():
            if line.startswith("AC "):
                acc.add(line[5:].split(";")[0].strip()); break
    return acc

def load_survey():
    """accession -> set(caution PMIDs)."""
    cp = {}
    with SURVEY.open() as fh:
        r = csv.reader(fh, delimiter="\t"); next(r, None)
        for row in r:
            if len(row) < 6: continue
            cp[row[0]] = set(PMID_RE.findall(row[5]))
    return cp

def get_json(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            if attempt == 4: raise
            time.sleep(2 ** (attempt + 1))

def pull_mf_goa(accessions):
    """Download MF annotations for all accessions (cached to TSV). One row per annotation."""
    if GOA_CACHE.exists():
        print(f"using cached {GOA_CACHE}", file=sys.stderr)
        return
    accs = sorted(accessions)
    with GOA_CACHE.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["accession", "qualifier", "goId", "goName", "evidence", "reference"])
        for i in range(0, len(accs), BATCH):
            batch = accs[i:i+BATCH]
            page = 1
            while True:
                params = {"geneProductId": ",".join(batch), "aspect": "molecular_function",
                          "limit": "200", "page": str(page)}
                d = get_json(QUICKGO + "?" + urllib.parse.urlencode(params))
                for r in d.get("results", []):
                    acc = r.get("geneProductId", "").split(":")[-1]
                    w.writerow([acc, r.get("qualifier"), r.get("goId"), r.get("goName"),
                                r.get("goEvidence"), r.get("reference")])
                pi = d.get("pageInfo") or {}
                if page >= (pi.get("total") or 1): break
                page += 1
            if (i // BATCH) % 25 == 0:
                print(f"  pulled {i+len(batch)}/{len(accs)} accessions", file=sys.stderr)
    print(f"wrote {GOA_CACHE}", file=sys.stderr)

def main():
    if not SURVEY.exists():
        sys.exit("Run uniprot_api_survey.py first (need caution_uniprot_reviewed.tsv).")
    caution_pmids = load_survey()
    pull_mf_goa(set(caution_pmids))

    # group GOA by accession
    by_acc = defaultdict(list)
    with GOA_CACHE.open() as fh:
        r = csv.DictReader(fh, delimiter="\t")
        for row in r:
            by_acc[row["accession"]].append(row)

    local = local_accessions()
    go = get_adapter("sqlite:obo:go")
    anc_cache = {}
    def anc(t):
        if t not in anc_cache:
            try: anc_cache[t] = set(go.ancestors(t, predicates=["rdfs:subClassOf"])) - {t}
            except Exception: anc_cache[t] = set()
        return anc_cache[t]

    conj, direct, brows = [], [], []
    for acc, anns in by_acc.items():
        net_new = "net_new" if acc not in local else "local"
        pos = [a for a in anns if not (a["qualifier"] or "").startswith("NOT")]
        neg = [a for a in anns if (a["qualifier"] or "").startswith("NOT")]
        # ---- Query A ----
        if pos and neg:
            pos_by = {};
            for a in pos: pos_by.setdefault(a["goId"], a)
            neg_by = {}
            for a in neg: neg_by.setdefault(a["goId"], a)
            exp_pos = {a["goId"] for a in pos if a["evidence"] not in ELECTRONIC}
            for yt, yr in neg_by.items():
                ya = anc(yt)
                for xt, xr in pos_by.items():
                    if xt == yt:
                        direct.append((net_new, acc, xt, xr["goName"], xr["evidence"], yr["evidence"]))
                    elif xt in ya:
                        supported = any(zt == xt or xt in anc(zt) for zt in exp_pos if zt != yt)
                        conj.append((net_new, acc, xt, xr["goName"], xr["evidence"],
                                     yt, yr["goName"], yr["evidence"],
                                     "supported" if supported else "UNSUPPORTED"))
        # ---- Query B (MF) ----
        cpmids = caution_pmids.get(acc, set())
        if not cpmids: continue
        pos_pmid = defaultdict(list); not_pmid = set()
        for a in anns:
            m = re.search(r"(?:PMID|PubMed):(\d+)", a["reference"] or "", re.I)
            if not m: continue
            pm = m.group(1)
            if (a["qualifier"] or "").startswith("NOT"): not_pmid.add(pm)
            else: pos_pmid[pm].append((a["goId"], a["goName"], a["evidence"]))
        for pm in cpmids:
            if pm in pos_pmid and pm not in not_pmid:
                terms = pos_pmid[pm]
                brows.append((net_new, acc, pm, len(terms),
                              "; ".join(f"{t}({ev})" for t,_,ev in terms[:6])))

    def wtsv(path, header, rows):
        with path.open("w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t"); w.writerow(header)
            for r in sorted(rows): w.writerow(r)
    wtsv(OUT/"uniprot_wide_conjunctions.tsv",
         ["scope","accession","pos_term","pos_name","pos_evidence","neg_term","neg_name","neg_evidence","parent_support"], conj)
    wtsv(OUT/"uniprot_wide_pmid.tsv",
         ["scope","accession","caution_pmid","n_pos","positive_mf_terms"], brows)

    strong = [r for r in conj if r[4] in ELECTRONIC and r[8] == "UNSUPPORTED"]
    strong_new = [r for r in strong if r[0] == "net_new"]
    b_new = [r for r in brows if r[0] == "net_new"]
    with (OUT/"uniprot_wide_queries.md").open("w") as fh:
        fh.write("---\ntitle: \"UniProt-wide CAUTION over-annotation queries\"\n---\n\n")
        fh.write("# UniProt-wide CAUTION over-annotation queries (QuickGO)\n\n")
        fh.write("Auto-generated by `uniprot_wide_queries.py`. Do not edit by hand.\n\n")
        fh.write(f"- CAUTION accessions surveyed: **{len(caution_pmids)}** "
                 f"(MF GOA pulled for {len(by_acc)} with >=1 MF annotation).\n")
        fh.write(f"- Query A conjunctions: **{len(conj)}**; STRONG: **{len(strong)}** "
                 f"(**{len(strong_new)}** in genes not yet in this repo).\n")
        fh.write(f"- Query A DIRECT same-term conflicts: **{len(direct)}**.\n")
        fh.write(f"- Query B (CAUTION-PMID positive, never negated): **{len(brows)}** "
                 f"(**{len(b_new)}** net-new).\n\n")
        fh.write("## Query A — STRONG over-annotation candidates, net-new genes\n\n")
        fh.write("| accession | positive parent (ev) | NOT-ed child (ev) |\n|---|---|---|\n")
        for sc,acc,xt,xn,xe,yt,yn,ye,su in sorted(strong_new)[:80]:
            fh.write(f"| {acc} | {xt} {xn} ({xe}) | {yt} {yn} ({ye}) |\n")
        fh.write("\n## Query B — net-new flags (CAUTION PMID, positive MF, no NOT)\n\n")
        fh.write("| accession | CAUTION PMID | #pos | positive MF terms |\n|---|---|--:|---|\n")
        for sc,acc,pm,n,terms in sorted(b_new)[:80]:
            fh.write(f"| {acc} | PMID:{pm} | {n} | {terms} |\n")
    print(f"Query A: {len(conj)} conjunctions, {len(strong)} STRONG ({len(strong_new)} net-new), {len(direct)} direct")
    print(f"Query B: {len(brows)} flags ({len(b_new)} net-new)")

if __name__ == "__main__":
    main()
