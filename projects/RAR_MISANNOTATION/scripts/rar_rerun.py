"""Rerun the Wei et al. 2020 taxon-specific annotation rate ratio (RAR) screen on current GOA.

Method, following the paper (PMID:32470107) and its supplement (Text S1, Tables S1-S2):

* The same 20 species as Table S1, grouped into five kingdoms (Animals, Archaea,
  Bacteria, Fungi, Plants), plus a phylum-level comparison of vertebrates against
  invertebrates within Animals.
* For a GO term q and a taxon t, the annotation rate is the number of proteins in t
  annotated with q divided by the number of proteins in t with any annotation (in any
  aspect).
* RAR is the lowest non-zero rate divided by the highest rate. The taxon with the
  lowest non-zero rate is the one the term is potentially misannotated to (Table S2,
  footnote a). Terms annotated in only one taxon have no RAR.
* The p-value is the exact two-sided rate ratio test between those two taxa (the
  authors' rateratio.py, a port of the R rateratio.test package), with Benjamini-
  Hochberg correction over all terms that have a RAR.
* Terms with RAR < 0.1 are flagged; every flagged annotation still needs a human pass
  and the comparator check before it is called an error.

Counts use asserted (direct) annotations, excluding NOT rows, by default; pass
--propagate to count a protein for every is_a/part_of ancestor of its terms as well.
The paper does not say which it used.

Inputs are the current GOA proteome GAFs and go-basic.obo, downloaded to the
git-ignored .cache/rar/. Output: projects/RAR_MISANNOTATION/data/rar_rerun_<scope>.yaml.

Run from the repository root:
    uv run python projects/RAR_MISANNOTATION/scripts/rar_rerun.py
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml
from scipy.stats import binom

GOA = "https://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/"
OBO = "https://purl.obolibrary.org/obo/go/go-basic.obo"
CACHE = Path(".cache/rar")
OUT_DIR = Path("projects/RAR_MISANNOTATION/data")

# Table S1 species -> (kingdom, phylum, GOA proteome file). The Arabidopsis proteome
# has two GOA files; 217288 is the long-standing one.
SPECIES = {
    9606: ("Animals", "Vertebrates", "25.H_sapiens.goa"),
    10090: ("Animals", "Vertebrates", "59.M_musculus.goa"),
    9031: ("Animals", "Vertebrates", "4825697.G_gallus_2.goa"),
    7227: ("Animals", "Invertebrates", "17.D_melanogaster.goa"),
    6239: ("Animals", "Invertebrates", "9.C_elegans.goa"),
    83333: ("Bacteria", None, "18.E_coli_MG1655.goa"),
    272563: ("Bacteria", None, "25374.C_difficile_630.goa"),
    224308: ("Bacteria", None, "6.B_subtilis_168.goa"),
    85962: ("Bacteria", None, "23.H_pylori_26695.goa"),
    243273: ("Bacteria", None, "31.M_genitalium.goa"),
    208963: ("Bacteria", None, "25692.P_aeruginosa_UCBPP-PA14.goa"),
    99287: ("Bacteria", None, "69.S_typhimurium_ATCC_700720.goa"),
    267377: ("Archaea", None, "942.M_maripaludis_S2.goa"),
    330779: ("Archaea", None, "21860.S_acidocaldarius.goa"),
    273075: ("Archaea", None, "42.T_acidophilum.goa"),
    559292: ("Fungi", None, "71242.S_cerevisiae_ATCC_204508.goa"),
    284812: ("Fungi", None, "78.S_pombe.goa"),
    237561: ("Fungi", None, "22024.C_albicans_SC5314.goa"),
    3702: ("Plants", None, "217288.A_thaliana.goa"),
    88036: ("Plants", None, "34463.S_moellendorffii.goa"),
}
KINGDOMS = ["Animals", "Archaea", "Bacteria", "Fungi", "Plants"]
ROOTS = {"GO:0003674", "GO:0008150", "GO:0005575"}  # ND rows on roots assert no function
MAX_FLAGGED = 3
PHYLA = ["Vertebrates", "Invertebrates"]


def fetch(url: str, dest: Path) -> Path:
    """Download url to dest unless it is already cached."""
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(dest.suffix + ".part")
        req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
        with urllib.request.urlopen(req, timeout=600) as r, open(tmp, "wb") as fh:
            while chunk := r.read(1 << 20):
                fh.write(chunk)
        tmp.rename(dest)
    return dest


def read_obo(path: Path) -> tuple[dict, dict, dict]:
    """Return labels, aspects and is_a/part_of parents for non-obsolete terms."""
    labels, aspects, parents = {}, {}, defaultdict(set)
    ns = {"biological_process": "BP", "molecular_function": "MF", "cellular_component": "CC"}
    cur, obsolete = None, False
    for line in path.read_text().splitlines() + ["[Term]"]:
        if line.startswith("["):
            if cur and obsolete:
                labels.pop(cur, None)
                aspects.pop(cur, None)
                parents.pop(cur, None)
            cur, obsolete = None, False
            continue
        if line.startswith("id: GO:"):
            cur = line[4:].strip()
        elif cur is None:
            continue
        elif line.startswith("name: "):
            labels[cur] = line[6:].strip()
        elif line.startswith("namespace: "):
            aspects[cur] = ns.get(line[11:].strip())
        elif line.startswith("is_a: "):
            parents[cur].add(line[6:16])
        elif line.startswith("relationship: part_of "):
            parents[cur].add(line[22:32])
        elif line.startswith("is_obsolete: true"):
            obsolete = True
    return labels, aspects, parents


QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/constraints"
UNIPROT_TAXON = "https://rest.uniprot.org/taxonomy/{taxid}.json"


def get_json(url: str) -> object:
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": "ai-gene-review"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def taxon_constraints(terms: list[str]) -> dict[str, list[dict]]:
    """GO taxon constraints (own and inherited) per term, from QuickGO; cached."""
    path = CACHE / "taxon_constraints.json"
    cache = json.loads(path.read_text()) if path.exists() else {}
    todo = [t for t in terms if t not in cache]
    for i in range(0, len(todo), 25):
        batch = todo[i:i + 25]
        for r in get_json(QUICKGO.format(ids=",".join(batch))).get("results", []):
            # A constraint can name several taxa as a union, e.g. taxId "2, 2157, 4751".
            cache[r["id"]] = [
                {"relationship": c["relationship"],
                 "taxa": [f"NCBITaxon:{x.strip()}" for x in str(c["taxId"]).split(",")],
                 "taxon_label": c.get("taxName"), "on_term": c.get("ancestorId")}
                for c in r.get("taxonConstraints", [])
            ]
        for t in batch:
            cache.setdefault(t, [])
    path.write_text(json.dumps(cache, indent=0, sort_keys=True))
    return cache


def lineages(taxids) -> dict[int, set[str]]:
    """NCBITaxon CURIEs of each species and all its ancestors, from UniProt; cached."""
    path = CACHE / "lineages.json"
    cache = json.loads(path.read_text()) if path.exists() else {}
    for t in taxids:
        if str(t) not in cache:
            d = get_json(UNIPROT_TAXON.format(taxid=t))
            cache[str(t)] = [t] + [x["taxonId"] for x in d.get("lineage", [])]
    path.write_text(json.dumps(cache))
    return {int(k): {f"NCBITaxon:{x}" for x in v} for k, v in cache.items()}


def violates(constraints: list[dict], lineage: set[str]) -> list[str]:
    """Constraints the taxon breaks: outside every only_in_taxon, or inside a never_in_taxon."""
    only = [c for c in constraints if c["relationship"] == "only_in_taxon"]
    broken = [c for c in constraints
              if c["relationship"] == "never_in_taxon" and lineage & set(c["taxa"])]
    if only and not any(lineage & set(c["taxa"]) for c in only):
        broken += only
    return [describe(c) for c in broken]


def describe(c: dict) -> str:
    return f"{c['relationship']} {' or '.join(c['taxa'])} ({c['taxon_label']})"


def ancestors(term: str, parents: dict, memo: dict) -> set:
    """All is_a/part_of ancestors of term, including itself."""
    if term not in memo:
        out = {term}
        for p in parents.get(term, ()):
            out |= ancestors(p, parents, memo)
        memo[term] = out
    return memo[term]


def read_gaf(path: Path):
    """Yield (protein, term, evidence, reference, assigned_by, with_from) for non-NOT GAF rows."""
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 15 or "NOT" in f[3].split("|"):
                continue
            yield f"{f[0]}:{f[1]}", f[4], f[6], f[5], f[14], f[7]


def rate_ratio_p(y: int, n: int, x: int, m: int) -> float:
    """Exact two-sided rate ratio test for y/n against x/m (Fay 2010; authors' rateratio.py)."""
    p = n / (n + m)
    less = binom.cdf(y, x + y, p)
    greater = 1 - binom.cdf(y - 1, x + y, p)
    return float(min(1.0, 2 * min(less, greater)))


def bh(pvals: list[float]) -> list[float]:
    """Benjamini-Hochberg adjusted p-values, in input order."""
    order = sorted(range(len(pvals)), key=lambda i: pvals[i])
    q = [0.0] * len(pvals)
    prev = 1.0
    for rank, i in reversed(list(enumerate(order, start=1))):
        prev = min(prev, pvals[i] * len(pvals) / rank)
        q[i] = prev
    return q


def reviewed_index() -> dict[str, str]:
    """Map UniProt accession -> review path for gene reviews in this repository."""
    idx = {}
    for p in Path("genes").glob("*/*/*-ai-review.yaml"):
        with open(p) as fh:
            for line in fh:
                if line.startswith("id: "):
                    idx[line[4:].strip()] = str(p)
                    break
    return idx


def screen(groups: list[str], group_of: dict, annots: dict, proteins_by_group: dict,
           threshold: float) -> list[dict]:
    """Compute RAR for every term over the given groups and return flagged rows."""
    counts = defaultdict(lambda: defaultdict(set))
    for (prot, term), _rows in annots.items():
        g = group_of.get(prot)
        if g in groups:
            counts[term][g].add(prot)
    totals = {g: len(proteins_by_group[g]) for g in groups}
    rows = []
    for term, by_g in counts.items():
        rates = {g: len(by_g[g]) / totals[g] for g in groups if by_g.get(g)}
        if len(rates) < 2:
            continue
        lo = min(rates, key=rates.get)
        hi = max(rates, key=rates.get)
        rows.append({
            "term": term, "low": lo, "high": hi, "rar": rates[lo] / rates[hi],
            "p": rate_ratio_p(len(by_g[lo]), totals[lo], len(by_g[hi]), totals[hi]),
            "counts": {g: len(by_g.get(g, ())) for g in groups},
            "low_proteins": sorted(by_g[lo]),
        })
    for r, q in zip(rows, bh([r["p"] for r in rows])):
        r["q"] = q
    flagged = [r for r in rows if r["rar"] < threshold]
    flagged.sort(key=lambda r: r["rar"])
    return flagged, len(rows), totals


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--propagate", action="store_true", help="count ancestor terms too")
    ap.add_argument("--threshold", type=float, default=0.1)
    args = ap.parse_args()

    labels, aspects, parents = read_obo(fetch(OBO, CACHE / "go-basic.obo"))
    obo_version = next((ln.split(": ", 1)[1] for ln in (CACHE / "go-basic.obo").read_text().splitlines()[:5]
                        if ln.startswith("data-version")), "unknown")
    memo: dict = {}
    annots: dict = defaultdict(list)  # (protein, term) -> [(evidence, ref, assigned_by)]
    species_of, kingdom_of, phylum_of = {}, {}, {}
    prot_by_k, prot_by_p = defaultdict(set), defaultdict(set)
    gaf_dates = {}
    for taxid, (kingdom, phylum, fname) in SPECIES.items():
        path = fetch(GOA + fname, CACHE / "goa" / fname)
        with open(path) as fh:
            head = "".join(next(fh) for _ in range(12))
        m = re.search(r"date-generated:\s*(\S+)", head) or re.search(r"Generated:\s*(\S+)", head)
        gaf_dates[fname] = m.group(1) if m else "unknown"
        for prot, term, ev, ref, by, wf in read_gaf(path):
            if term not in labels:
                continue
            species_of[prot], kingdom_of[prot] = taxid, kingdom
            prot_by_k[kingdom].add(prot)
            if phylum:
                phylum_of[prot] = phylum
                prot_by_p[phylum].add(prot)
            terms = ancestors(term, parents, memo) if args.propagate else {term}
            for t in terms:
                annots[(prot, t)].append((ev, ref, by, wf) if t == term else ("inferred-ancestor", ref, by, ""))

    reviewed = reviewed_index()
    prior = yaml.safe_load(open(OUT_DIR / "rar_supplement_cases.yaml"))["cases"]
    prior_terms = {c["go_id"] for c in prior}

    def render(flagged, n_tested, totals, groups, level):
        out = []
        for r in flagged:
            annotations = []
            for prot in r["low_proteins"]:
                acc = prot.split(":", 1)[1]
                for ev, ref, by, wf in sorted(set(annots[(prot, r["term"])])):
                    annotations.append({
                        "protein": prot, "taxon": f"NCBITaxon:{species_of[prot]}",
                        "evidence": ev, "reference": ref, "assigned_by": by,
                        **({"with_from": wf} if wf else {}),
                        **({"gene_review": reviewed[acc]} if acc in reviewed else {}),
                    })
            out.append({
                "go_id": r["term"], "label": labels[r["term"]], "aspect": aspects[r["term"]],
                "flagged_taxon": r["low"], "highest_taxon": r["high"],
                "annotated_protein_counts": r["counts"],
                "rate_ratio": float(f"{r['rar']:.3g}"),
                "p_value": float(f"{r['p']:.3g}"), "q_value": float(f"{r['q']:.3g}"),
                "flagged_in_2019_or_2018": r["term"] in prior_terms,
                "flagged_annotations": annotations,
            })
        return {"level": level, "groups": groups, "annotated_proteins_per_group": totals,
                "terms_with_rate_ratio": n_tested, "flagged_terms": len(out), "terms": out}

    k = screen(KINGDOMS, kingdom_of, annots, prot_by_k, args.threshold)
    p = screen(PHYLA, phylum_of, annots, prot_by_p, args.threshold)
    scope = "propagated" if args.propagate else "direct"
    doc = {
        "source": {
            "method": "PMID:32470107 (Wei et al. 2020), rerun on current GOA",
            "generated_by": "projects/RAR_MISANNOTATION/scripts/rar_rerun.py",
            "run_date": date.today().isoformat(),
            "counting": scope, "threshold": args.threshold,
            "go_version": obo_version, "goa_files": gaf_dates,
            "note": "Flags are candidates for manual review, not confirmed errors.",
        },
        "kingdom": render(*k, KINGDOMS, "kingdom"),
        "phylum": render(*p, PHYLA, "phylum"),
    }
    full = CACHE / f"rar_rerun_{scope}_full.yaml"
    full.write_text(yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True))
    # The committed file keeps the review candidates: significant flags (q < 0.05) on a
    # non-root term where the flagged taxon has at most MAX_FLAGGED proteins, i.e. a few
    # stray annotations against an established distribution elsewhere.
    for lvl in ("kingdom", "phylum"):
        d = doc[lvl]
        sig = [t for t in d["terms"] if t["q_value"] < 0.05]
        keep = [t for t in sig if t["go_id"] not in ROOTS
                and t["annotated_protein_counts"][t["flagged_taxon"]] <= MAX_FLAGGED]
        print(f"{lvl}: {d['terms_with_rate_ratio']} terms with a RAR; {d['flagged_terms']} below "
              f"{args.threshold} ({len(sig)} with q < 0.05; {len(keep)} candidates); "
              f"totals {d['annotated_proteins_per_group']}")
        d["significant_terms"] = len(sig)
        d["candidate_terms"] = len(keep)
        d["terms"] = keep
    # Annotations that break a taxon constraint GO already has need no judgement.
    cand_terms = sorted({t["go_id"] for lvl in ("kingdom", "phylum") for t in doc[lvl]["terms"]})
    cons = taxon_constraints(cand_terms)
    lin = lineages(SPECIES)
    n_viol = 0
    for lvl in ("kingdom", "phylum"):
        for t in doc[lvl]["terms"]:
            if cons.get(t["go_id"]):
                t["go_taxon_constraints"] = [describe(c) for c in cons[t["go_id"]]]
            for a in t["flagged_annotations"]:
                broken = violates(cons.get(t["go_id"], []), lin[int(a["taxon"].split(":")[1])])
                if broken:
                    a["violates_go_taxon_constraint"] = broken
                    n_viol += 1
    print(f"{n_viol} candidate annotations break an existing GO taxon constraint")
    doc["source"]["candidate_filter"] = (
        f"q < 0.05, not a root term, at most {MAX_FLAGGED} proteins in the flagged taxon; "
        f"the unfiltered output is written to {full}")
    out = OUT_DIR / f"rar_rerun_{scope}_candidates.yaml"
    out.write_text(yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True))
    print(f"wrote {out} and {full}")


if __name__ == "__main__":
    main()
