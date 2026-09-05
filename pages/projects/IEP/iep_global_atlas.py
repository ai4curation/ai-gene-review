"""Build a global IEP atlas from QuickGO and measure the repo sample against it.

The companion script :mod:`iep_corpus_survey` only sees ``genes/*/*/*-goa.tsv``,
and a gene directory exists because somebody chose that gene for review. Its
"GOA view" is therefore a review-driven sample, not a sample of IEP. This script
supplies the denominator.

IEP is rare enough (~26k annotations in all of UniProt-GOA) that the *complete*
global set can simply be downloaded, so nothing here is itself a sample.

"IEP" is taken to mean *what a GAF calls IEP*, i.e. ECO:0000270 **and its
descendants** (``evidenceCodeUsage=descendants``). That matters: the specific
descendant classes are where the GORULE:0000006 aspect violations live, and
querying ``exact`` would hide them. The ECO class is kept per row so the two
populations can be separated.

Three things are computed:

1. **The global distribution** of IEP by GO term, GO branch, aspect, qualifier,
   assigning group, taxon and reference.
2. **The repo's sampling bias** -- local share versus global share for each
   stratum, so claims made from the reviewed corpus can be corrected.
3. **IEP dependence per term** -- for the most frequent IEP terms, what fraction
   of *all* annotations to that term are IEP. A term that is mostly IEP is one
   where the evidence code is load-bearing rather than corroborating.

It then writes a **stratified candidate list** of not-yet-reviewed genes drawn
across the global term distribution, including strata the repo currently misses,
rather than only the head of the distribution.

Run::

    uv run python projects/IEP/iep_global_atlas.py

Network access is required on first run; the QuickGO download is cached under
``projects/IEP/data/``.
"""

from __future__ import annotations

import csv
import datetime
import json
import random
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

from ai_gene_review.analysis.subtraction_report import make_go_ancestor_fn

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(__file__).resolve().parent / "data"
GLOBAL_TSV = DATA_DIR / "global_iep_annotations.tsv"
CANDIDATES_TSV = DATA_DIR / "iep_review_candidates.tsv"
OUT_PATH = Path(__file__).resolve().parent / "iep-global-atlas.md"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation"
IEP_ECO = "ECO:0000270"

#: Coarse GO branches, most specific first (see ``iep_corpus_survey``).
BRANCHES = [
    ("GO:0050896", "response to stimulus"),
    ("GO:0032502", "developmental process"),
    ("GO:0065007", "biological regulation"),
    ("GO:0008152", "metabolic process"),
    ("GO:0051179", "localization"),
    ("GO:0005575", "cellular component"),
    ("GO:0003674", "molecular function"),
]

#: How many of the most frequent global IEP terms to measure IEP dependence for.
N_DEPENDENCE_TERMS = 40

#: Candidate genes to sample per term stratum.
PER_STRATUM = 3

#: QuickGO's TSV download abbreviates the aspect; the repo's cached GOA files
#: spell it out. Normalise to the repo's vocabulary so the two are comparable.
ASPECTS = {
    "P": "biological_process",
    "F": "molecular_function",
    "C": "cellular_component",
}

TAXON_CACHE = DATA_DIR / "taxon_names.json"


def fetch_global_iep() -> list[dict]:
    """Download (once) and return every annotation a GAF would call IEP."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not GLOBAL_TSV.exists():
        fields = [
            "geneProductId",
            "symbol",
            "qualifier",
            "goId",
            "goAspect",
            "evidenceCode",
            "goEvidence",
            "reference",
            "taxonId",
            "assignedBy",
            "date",
        ]
        params = [
            ("evidenceCode", IEP_ECO),
            ("evidenceCodeUsage", "descendants"),
            ("downloadLimit", "2000000"),
        ] + [("selectedFields", f) for f in fields]
        url = f"{QUICKGO}/downloadSearch?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"Accept": "text/tsv"})
        with urllib.request.urlopen(req) as resp:
            GLOBAL_TSV.write_bytes(resp.read())
        print(f"Downloaded {GLOBAL_TSV.relative_to(REPO_ROOT)}")

    with open(GLOBAL_TSV, newline="") as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t")]
    rows = [r for r in rows if (r.get("GO EVIDENCE CODE") or "").strip() == "IEP"]
    for r in rows:
        aspect = (r.get("GO ASPECT") or "").strip()
        r["GO ASPECT"] = ASPECTS.get(aspect, aspect)
    return rows


def taxon_names(taxon_ids: set[str]) -> dict[str, str]:
    """NCBI taxon id -> scientific name, batched via eutils and cached on disk."""
    cache: dict[str, str] = {}
    if TAXON_CACHE.exists():
        cache = json.loads(TAXON_CACHE.read_text())
    missing = sorted(t for t in taxon_ids if t and t not in cache)
    for start in range(0, len(missing), 200):
        batch = missing[start : start + 200]
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=taxonomy&retmode=json"
            f"&id={','.join(batch)}"
        )
        with urllib.request.urlopen(url) as resp:
            result = json.load(resp)["result"]
        for uid in result.get("uids", []):
            cache[uid] = result[uid].get("scientificname") or uid
        for taxon in batch:
            cache.setdefault(taxon, taxon)
    if missing:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        TAXON_CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True))
    return cache


def annotation_count(term_id: str, evidence: str | None = None) -> int:
    """Total UniProt-GOA annotations to ``term_id``, optionally one evidence code.

    ``goUsage=exact`` keeps this a count of direct annotations to the term, so it
    is comparable with the IEP rows, which are also direct.
    """
    params = [("goId", term_id), ("goUsage", "exact"), ("limit", "1")]
    if evidence:
        params += [("evidenceCode", evidence), ("evidenceCodeUsage", "exact")]
    url = f"{QUICKGO}/search?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return int(json.load(resp).get("numberOfHits") or 0)


def local_iep_rows() -> list[dict]:
    """IEP rows from the repo's cached GOA files, with the gene directory tagged."""
    out: list[dict] = []
    for path in sorted(REPO_ROOT.glob("genes/*/*/*-goa.tsv")):
        with open(path, newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if (row.get("GO EVIDENCE CODE") or "").strip() != "IEP":
                    continue
                row["_species_dir"] = path.parent.parent.name
                row["_gene_dir"] = path.parent.name
                out.append(row)
    return out


def reviewed_gene_products() -> set[str]:
    """UniProt accessions that already have a gene directory in the repo."""
    accessions: set[str] = set()
    for path in REPO_ROOT.glob("genes/*/*/*-goa.tsv"):
        with open(path, newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                acc = (row.get("GENE PRODUCT ID") or "").strip()
                if acc:
                    accessions.add(acc)
                break
    return accessions


def classify_branch(term_id: str, ancestors) -> str:
    anc = ancestors(term_id)
    for root, label in BRANCHES:
        if root in anc:
            return label
    return "unclassified"


def pct(n: int, d: int) -> float:
    return 100.0 * n / d if d else 0.0


def bias_table(
    add,
    title: str,
    local: Counter,
    glob: Counter,
    n_local: int,
    n_global: int,
    top: int = 12,
) -> None:
    """Local-share vs global-share table for one stratum, ranked by global share."""
    add(f"### {title}")
    add("")
    add("| Stratum | Global rows | Global % | Repo rows | Repo % | Repo / global |")
    add("|---|---:|---:|---:|---:|---:|")
    keys = [k for k, _ in glob.most_common(top)]
    for k in keys:
        g, loc = glob[k], local.get(k, 0)
        gp, lp = pct(g, n_global), pct(loc, n_local)
        ratio = f"{lp / gp:.2f}x" if gp else "n/a"
        add(f"| {k} | {g:,} | {gp:.1f}% | {loc:,} | {lp:.1f}% | **{ratio}** |")
    missed = [k for k in keys if k not in local]
    if missed:
        add("")
        add(f"Absent from the repo entirely: {', '.join(missed)}.")
    add("")


def main() -> None:
    ancestors = make_go_ancestor_fn()
    glob_rows = fetch_global_iep()
    loc_rows = local_iep_rows()
    n_global, n_local = len(glob_rows), len(loc_rows)

    def col(rows, key):
        return Counter((r.get(key) or "").strip() for r in rows)

    g_terms = col(glob_rows, "GO TERM")
    l_terms = col(loc_rows, "GO TERM")
    g_aspect = col(glob_rows, "GO ASPECT")
    l_aspect = col(loc_rows, "GO ASPECT")
    g_group = col(glob_rows, "ASSIGNED BY")
    l_group = col(loc_rows, "ASSIGNED BY")
    g_qual = col(glob_rows, "QUALIFIER")
    l_qual = col(loc_rows, "QUALIFIER")
    g_ref = col(glob_rows, "REFERENCE")
    l_ref = col(loc_rows, "REFERENCE")

    tax_ids = {(r.get("TAXON ID") or "").strip() for r in glob_rows} | {
        (r.get("TAXON ID") or "").strip() for r in loc_rows
    }
    tax_names = taxon_names(tax_ids)

    def taxon_of(row: dict) -> str:
        tid = (row.get("TAXON ID") or "").strip()
        return tax_names.get(tid, tid)

    g_taxon = Counter(taxon_of(r) for r in glob_rows)
    l_taxon = Counter(taxon_of(r) for r in loc_rows)

    # ECO class split: exactly ECO:0000270 versus a more specific descendant.
    g_eco = col(glob_rows, "ECO ID")
    eco_aspect: dict[str, Counter[str]] = defaultdict(Counter)
    for r in glob_rows:
        eco_aspect[(r.get("ECO ID") or "").strip()][
            (r.get("GO ASPECT") or "").strip()
        ] += 1

    g_branch: Counter[str] = Counter()
    for term, n in g_terms.items():
        g_branch[classify_branch(term, ancestors)] += n
    l_branch: Counter[str] = Counter()
    for term, n in l_terms.items():
        l_branch[classify_branch(term, ancestors)] += n

    term_labels = label_map(g_terms, ancestors)

    # Reference concentration: how much of IEP comes from high-yield papers.
    ref_sizes = sorted(g_ref.values(), reverse=True)
    top10_refs = sum(ref_sizes[:10])
    singleton_refs = sum(1 for v in g_ref.values() if v == 1)

    # Genes carrying IEP, and how concentrated the per-gene load is.
    g_gene = col(glob_rows, "GENE PRODUCT ID")
    gene_sizes = sorted(g_gene.values(), reverse=True)
    heavy_genes = [g for g, n in g_gene.items() if n >= 5]
    heavy_rows = sum(g_gene[g] for g in heavy_genes)

    print(
        f"Global IEP: {n_global:,} rows, {len(g_gene):,} gene products, {len(g_terms):,} terms"
    )
    print(f"Repo IEP:   {n_local:,} rows ({pct(n_local, n_global):.1f}% of global)")

    print(f"Measuring IEP dependence for the top {N_DEPENDENCE_TERMS} terms...")
    dependence = []
    for term, iep_n in g_terms.most_common(N_DEPENDENCE_TERMS):
        total = annotation_count(term)
        dependence.append(
            (term, term_labels.get(term, ""), iep_n, total, pct(iep_n, total))
        )

    lines: list[str] = []
    add = lines.append
    add("---")
    add('title: "Global IEP atlas"')
    add("autolink_gene_symbols: false")
    add("---")
    add("")
    add("# Global IEP atlas")
    add("")
    snapshot = datetime.date.fromtimestamp(GLOBAL_TSV.stat().st_mtime).isoformat()
    add(
        "Generated by [`iep_global_atlas.py`](iep_global_atlas.py). The complete set of "
        f"**{n_global:,}** annotations that a GAF labels IEP, downloaded from QuickGO with "
        "`evidenceCode=ECO:0000270&evidenceCodeUsage=descendants` and then filtered to "
        "`GO EVIDENCE CODE == IEP`. This is the denominator for the review-driven sample "
        "measured in [iep-corpus-survey.md](iep-corpus-survey.md)."
    )
    add("")
    add(
        f"GOA snapshot: **{snapshot}** "
        "([`data/global_iep_annotations.tsv`](data/global_iep_annotations.tsv), committed so the "
        "figures below stay reproducible as GOA moves; delete it to re-download)."
    )
    add("")

    add("## Scale")
    add("")
    add("| | Global (UniProt-GOA) | Repo (`genes/*/*/*-goa.tsv`) | Coverage |")
    add("|---|---:|---:|---:|")
    add(
        f"| IEP annotations | {n_global:,} | {n_local:,} | {pct(n_local, n_global):.1f}% |"
    )
    add(
        f"| Gene products with IEP | {len(g_gene):,} | "
        f"{len({r['_gene_dir'] for r in loc_rows}):,} | "
        f"{pct(len({r['_gene_dir'] for r in loc_rows}), len(g_gene)):.1f}% |"
    )
    add(
        f"| Distinct GO terms | {len(g_terms):,} | {len(l_terms):,} | {pct(len(l_terms), len(g_terms)):.1f}% |"
    )
    add(
        f"| Distinct references | {len(g_ref):,} | {len(l_ref):,} | {pct(len(l_ref), len(g_ref)):.1f}% |"
    )
    add("")
    g_db = col(glob_rows, "GENE PRODUCT DB")
    add("Not all of it is in scope for a protein-centric review corpus:")
    add("")
    add("| Gene product database | IEP rows | Share | Distinct products |")
    add("|---|---:|---:|---:|")
    for db, n in g_db.most_common():
        prods = len(
            {r["GENE PRODUCT ID"] for r in glob_rows if r["GENE PRODUCT DB"] == db}
        )
        add(f"| {db} | {n:,} | {pct(n, n_global):.1f}% | {prods:,} |")
    add("")

    add("## What GAFs call IEP is not one ECO class")
    add("")
    exact_n = g_eco.get(IEP_ECO, 0)
    add(
        f"Of the {n_global:,} annotations a GAF labels IEP, **{exact_n:,}** "
        f"({pct(exact_n, n_global):.1f}%) are literally `ECO:0000270`; the remaining "
        f"**{n_global - exact_n:,}** ({pct(n_global - exact_n, n_global):.1f}%) use a more "
        "specific descendant class that collapses to IEP in the GAF projection. The aspect "
        "breakdown shows why this matters."
    )
    add("")
    add(
        "| ECO class | IEP rows | biological_process | molecular_function | cellular_component |"
    )
    add("|---|---:|---:|---:|---:|")
    for eco, n in g_eco.most_common(12):
        a = eco_aspect[eco]
        add(
            f"| {eco} | {n:,} | {a.get('biological_process', 0):,} "
            f"| {a.get('molecular_function', 0):,} | {a.get('cellular_component', 0):,} |"
        )
    add("")

    add("## Sampling bias of the reviewed corpus")
    add("")
    add(
        "`Repo / global` is the ratio of shares: 1.00x means the repo samples that stratum in "
        "proportion to its global frequency, >1 over-samples it, <1 under-samples it."
    )
    add("")
    bias_table(add, "By assigning group", l_group, g_group, n_local, n_global)
    bias_table(add, "By taxon", l_taxon, g_taxon, n_local, n_global)
    bias_table(add, "By GO aspect", l_aspect, g_aspect, n_local, n_global, top=5)
    bias_table(add, "By qualifier", l_qual, g_qual, n_local, n_global, top=8)
    bias_table(add, "By GO branch", l_branch, g_branch, n_local, n_global, top=8)

    add("### By GO term (global top 30)")
    add("")
    add("| GO term | Label | Global | Global % | Repo | Repo / global |")
    add("|---|---|---:|---:|---:|---:|")
    for term, g in g_terms.most_common(30):
        loc = l_terms.get(term, 0)
        gp, lp = pct(g, n_global), pct(loc, n_local)
        ratio = f"{lp / gp:.2f}x" if gp else "n/a"
        add(
            f"| {term} | {term_labels.get(term, '')} | {g:,} | {gp:.2f}% | {loc} | {ratio} |"
        )
    add("")

    add("## How dependent is each term on IEP?")
    add("")
    add(
        "For each of the most frequent IEP terms, the share of **all** direct UniProt-GOA "
        "annotations to that term that are IEP. A high share means IEP is the term's main "
        "support rather than corroboration for it."
    )
    add("")
    add("| GO term | Label | IEP | All evidence | IEP share |")
    add("|---|---|---:|---:|---:|")
    for term, label, iep_n, total, share in sorted(dependence, key=lambda t: -t[4]):
        add(f"| {term} | {label} | {iep_n:,} | {total:,} | **{share:.1f}%** |")
    add("")

    add("## Concentration")
    add("")
    add(
        f"- **References:** {len(g_ref):,} distinct references; the 10 highest-yield "
        f"account for {top10_refs:,} rows ({pct(top10_refs, n_global):.1f}%). "
        f"{singleton_refs:,} references ({pct(singleton_refs, len(g_ref)):.1f}%) contribute "
        "exactly one IEP annotation."
    )
    add(
        f"- **Genes:** {len(g_gene):,} gene products carry IEP; the "
        f"{len(heavy_genes):,} with 5 or more IEP rows "
        f"({pct(len(heavy_genes), len(g_gene)):.1f}% of them) account for {heavy_rows:,} rows "
        f"({pct(heavy_rows, n_global):.1f}%). Maximum for one gene product: {gene_sizes[0]}."
    )
    add("")
    add("### Highest-yield references")
    add("")
    add("| Reference | IEP rows | Gene products | Distinct terms |")
    add("|---|---:|---:|---:|")
    by_ref = defaultdict(list)
    for r in glob_rows:
        by_ref[(r.get("REFERENCE") or "").strip()].append(r)
    for ref, n in g_ref.most_common(15):
        rs = by_ref[ref]
        add(
            f"| {ref} | {n:,} | {len({x['GENE PRODUCT ID'] for x in rs}):,} "
            f"| {len({x['GO TERM'] for x in rs}):,} |"
        )
    add("")

    add("### Gene products with the largest IEP load")
    add("")
    add("| Gene product | Symbol | Taxon | IEP rows | In repo |")
    add("|---|---|---|---:|---|")
    sym = {r["GENE PRODUCT ID"]: (r.get("SYMBOL") or "") for r in glob_rows}
    tax = {r["GENE PRODUCT ID"]: taxon_of(r) for r in glob_rows}
    in_repo = reviewed_gene_products()
    for acc, n in g_gene.most_common(20):
        add(
            f"| {acc} | {sym.get(acc, '')} | {tax.get(acc, '')} | {n} "
            f"| {'yes' if acc in in_repo else 'no'} |"
        )
    add("")

    candidates = write_candidates(
        glob_rows, g_terms, term_labels, in_repo, ancestors, tax_names
    )
    add("## Stratified review candidates")
    add("")
    add(
        f"[`data/iep_review_candidates.tsv`](data/iep_review_candidates.tsv) holds "
        f"**{len(candidates):,}** not-yet-reviewed gene products sampled across the global term "
        f"distribution (up to {PER_STRATUM} per term, seeded for reproducibility) rather than "
        "only from the head of it, so the term strata the repo currently misses are represented."
    )
    add("")

    OUT_PATH.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT_PATH.relative_to(REPO_ROOT)}")
    print(
        f"Wrote {CANDIDATES_TSV.relative_to(REPO_ROOT)} ({len(candidates)} candidates)"
    )


def label_map(terms: Counter, ancestors) -> dict[str, str]:
    """GO id -> label, via OAK (the QuickGO TSV download leaves GO NAME empty)."""
    from oaklib import get_adapter

    adapter = get_adapter("sqlite:obo:go")
    ids = list(terms)
    return {t: (adapter.label(t) or "") for t in ids}


def write_candidates(
    glob_rows: list[dict],
    g_terms: Counter,
    term_labels: dict[str, str],
    in_repo: set[str],
    ancestors,
    tax_names: dict[str, str],
) -> list[dict]:
    """Sample unreviewed gene products across every global IEP term stratum."""
    rng = random.Random(20260727)
    by_term: dict[str, list[dict]] = defaultdict(list)
    for r in glob_rows:
        if r["GENE PRODUCT ID"] in in_repo:
            continue
        by_term[(r.get("GO TERM") or "").strip()].append(r)

    iep_load = Counter(r["GENE PRODUCT ID"] for r in glob_rows)
    out: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for term in sorted(by_term, key=lambda t: -g_terms[t]):
        rows = by_term[term]
        picks = rows if len(rows) <= PER_STRATUM else rng.sample(rows, PER_STRATUM)
        for r in picks:
            key = (r["GENE PRODUCT ID"], term)
            if key in seen:
                continue
            seen.add(key)
            out.append(
                {
                    "gene_product_id": r["GENE PRODUCT ID"],
                    "symbol": r.get("SYMBOL") or "",
                    "taxon_id": (r.get("TAXON ID") or "").strip(),
                    "taxon_name": tax_names.get((r.get("TAXON ID") or "").strip(), ""),
                    "go_term": term,
                    "go_label": term_labels.get(term, ""),
                    "go_branch": classify_branch(term, ancestors),
                    "qualifier": r.get("QUALIFIER") or "",
                    "reference": r.get("REFERENCE") or "",
                    "assigned_by": r.get("ASSIGNED BY") or "",
                    "global_term_frequency": g_terms[term],
                    "gene_iep_load": iep_load[r["GENE PRODUCT ID"]],
                }
            )

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(CANDIDATES_TSV, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(out)
    return out


if __name__ == "__main__":
    main()
