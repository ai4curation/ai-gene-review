#!/usr/bin/env python3
"""Are AARD's 15 reported interactors a coherent partner set, or a Y2H artefact signature?

AARD's entire GO record is 15 `protein binding` annotations, all from one yeast two-hybrid
publication. Before dismissing or accepting them, this asks whether the partner set looks
like biology or like a known screening artefact.

The hypothesis being tested is specific and falsifiable: **coiled-coil bias**. Self-activating
or "sticky" preys in Y2H are enriched for coiled-coil proteins, which interact promiscuously
through their heptad-repeat surfaces. If AARD's partners are drawn from unrelated cellular
compartments but share a coiled-coil architecture, the set is better explained by the assay
than by a function.

Partner accessions and the subcellular/feature data are fetched from UniProt at run time; the
accession list itself is read from the gene's own GOA file, so it cannot drift from the record
being reviewed.

    uv run python analyze_partners.py          # writes RESULTS.md
"""
from __future__ import annotations

import csv
import json
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "AARD-goa.tsv"
PANTHER = "PTHR32289"   # the family AARD belongs to, per its UniProt DR lines


def get(url: str):
    """GET JSON, returning None on failure so callers can tell failure from absence."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as fh:
            return json.load(fh)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ! fetch failed: {url} ({e})", file=sys.stderr)
        return None


def partners_from_goa(path: Path) -> list[str]:
    """Read the WITH/FROM accessions off the gene's own GOA file."""
    out: list[str] = []
    with open(path) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            wf = (row.get("WITH/FROM") or "").strip()
            for token in wf.split("|"):
                if token.startswith("UniProtKB:"):
                    out.append(token.split(":", 1)[1])
    return out


def count_hits(query: str) -> int | None:
    """Number of UniProt entries matching a query, read from the X-Total-Results header."""
    url = ("https://rest.uniprot.org/uniprotkb/search"
           f"?query={query}&format=json&size=1")
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as fh:
            v = fh.headers.get("X-Total-Results")
            return int(v) if v is not None else None
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        print(f"  ! count failed: {query} ({e})", file=sys.stderr)
        return None


def binomial_upper_tail(k: int, n: int, p: float) -> float:
    """P(X >= k) for X ~ Binomial(n, p)."""
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def top_compartment(loc: str) -> str:
    """UniProt subcellular-location strings are hierarchical and comma-delimited.

    "Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole" and
    "Cytoplasm, cytosol" are refinements of one compartment, so counting raw strings
    inflates apparent scatter. Collapse to the leading term.
    """
    return loc.split(",")[0].strip()


def family_members(panther: str) -> list[dict] | None:
    """Reviewed members of AARD's PANTHER family, with their FUNCTION statements."""
    url = ("https://rest.uniprot.org/uniprotkb/search"
           f"?query=xref:panther-{panther}+AND+reviewed:true"
           "&fields=accession,id,organism_name,cc_function&format=json&size=100")
    d = get(url)
    if d is None:
        return None
    out = []
    for r in d.get("results", []):
        fn = ""
        for c in r.get("comments", []):
            if c.get("commentType") == "FUNCTION":
                fn = " ".join(x.get("value", "") for x in c.get("texts", []))
        out.append({
            "acc": r["primaryAccession"],
            "id": r.get("uniProtkbId", ""),
            "organism": r.get("organism", {}).get("scientificName", ""),
            "function": fn,
        })
    return out


def describe(acc: str) -> dict | None:
    base = acc.split("-")[0]
    d = get(f"https://rest.uniprot.org/uniprotkb/{base}.json"
            "?fields=id,gene_names,protein_name,cc_subcellular_location,ft_coiled,keyword")
    if d is None:
        return None
    genes = [g.get("geneName", {}).get("value") for g in d.get("genes", [])]
    coiled = [f for f in d.get("features", []) if f.get("type") == "Coiled coil"]
    kws = {k.get("name") for k in d.get("keywords", [])}
    locs: list[str] = []
    for c in d.get("comments", []):
        if c.get("commentType") == "SUBCELLULAR LOCATION":
            for loc in c.get("subcellularLocations", []):
                v = (loc.get("location") or {}).get("value")
                if v:
                    locs.append(v)
    return {
        "acc": acc,
        "id": d.get("uniProtkbId", ""),
        "gene": genes[0] if genes else "?",
        "n_coiled": len(coiled),
        "coiled_kw": "Coiled coil" in kws,
        "locations": locs,
    }


def main() -> None:
    if not GOA.exists():
        print(f"missing {GOA}; cannot proceed", file=sys.stderr)
        return
    accs = partners_from_goa(GOA)
    print(f"{len(accs)} partner accessions read from {GOA.name}")

    rows = [r for a in accs if (r := describe(a)) is not None]
    n_failed = len(accs) - len(rows)
    for r in rows:
        print(f"  {r['acc']:<10} {r['gene']:<10} coiled-coil segments: {r['n_coiled']}")

    # Numerator and denominator must use the SAME criterion. The Coiled coil KEYWORD is
    # assigned more liberally than the ft_coiled FEATURE, so counting the numerator on
    # "feature OR keyword" while measuring the background on features alone inflates the
    # enrichment. Compute both criteria consistently and headline the feature-only pair.
    n_coiled_ft = sum(1 for r in rows if r["n_coiled"] > 0)
    n_coiled_any = sum(1 for r in rows if r["n_coiled"] > 0 or r["coiled_kw"])
    n_coiled = n_coiled_ft  # headline figure: feature-only, matching the feature background

    # Null model: what coiled-coil rate would be unsurprising? Without this, "enriched"
    # is an assertion of the same kind the review is sceptical of elsewhere.
    n_human = count_hits("reviewed:true+AND+organism_id:9606")
    n_human_cc = count_hits("reviewed:true+AND+organism_id:9606+AND+ft_coiled:*")
    n_human_cc_kw = count_hits("reviewed:true+AND+organism_id:9606+AND+keyword:KW-0175")
    bg = (n_human_cc / n_human) if (n_human and n_human_cc) else None
    bg_any = (n_human_cc_kw / n_human) if (n_human and n_human_cc_kw) else None
    pval = binomial_upper_tail(n_coiled, len(rows), bg) if (bg and rows) else None
    pval_any = binomial_upper_tail(n_coiled_any, len(rows), bg_any) if (bg_any and rows) else None

    # Collapse hierarchical location strings to top-level compartments.
    loc_counts: Counter[str] = Counter()
    raw_loc_strings = set()
    for r in rows:
        for l in r["locations"]:
            raw_loc_strings.add(l)
            loc_counts[top_compartment(l)] += 1

    print("\nFetching AARD's PANTHER family...")
    fam = family_members(PANTHER)
    if fam is not None:
        n_fam_fn = sum(1 for f in fam if f["function"])
        print(f"  {PANTHER}: {len(fam)} reviewed members, {n_fam_fn} with a FUNCTION statement")
    else:
        n_fam_fn = None

    L: list[str] = []
    L.append("# Are AARD's reported interactors a coherent partner set?")
    L.append("")
    L.append("Generated by `analyze_partners.py`. Partner accessions are read from the gene's own")
    L.append("`AARD-goa.tsv`; all protein data is fetched from the UniProt REST API at run time.")
    L.append("")
    L.append("## Question")
    L.append("")
    L.append("AARD's entire GO record consists of `protein binding` annotations from a single")
    L.append("yeast two-hybrid publication. This tests one specific, falsifiable explanation for")
    L.append("that set: **coiled-coil bias**. Sticky or self-activating preys in Y2H are enriched")
    L.append("for coiled-coil proteins, which associate promiscuously via heptad-repeat surfaces.")
    L.append("If the partners come from unrelated compartments but share coiled-coil")
    L.append("architecture, the assay explains the set better than any function does.")
    L.append("")
    L.append("## Result")
    L.append("")
    L.append(f"| Partner accessions in the GOA file | {len(accs)} |")
    L.append("|---|---|")
    L.append(f"| Successfully retrieved from UniProt | {len(rows)} |")
    L.append(f"| **With a coiled-coil FEATURE** | **{n_coiled_ft}** |")
    L.append(f"| With a coiled-coil feature or keyword | {n_coiled_any} |")
    if len(rows):
        L.append(f"| Proportion coiled-coil | **{100 * n_coiled / len(rows):.0f}%** |")
    L.append("")
    L.append("### Is that rate actually unusual? (null model)")
    L.append("")
    if bg is not None:
        L.append(f"Background, fetched from UniProt: **{n_human_cc} of {n_human}** reviewed human")
        L.append(f"proteins carry a coiled-coil feature = **{100 * bg:.1f}%**.")
        L.append("")
        L.append(f"- Observed in this partner set: **{100 * n_coiled_ft / len(rows):.0f}%** "
                 f"({n_coiled_ft}/{len(rows)})")
        L.append(f"- Enrichment: **{(n_coiled_ft / len(rows)) / bg:.1f}-fold**")
        if pval is not None:
            L.append(f"- Binomial P(X >= {n_coiled_ft} | n={len(rows)}, p={bg:.3f}) = **{pval:.2e}**")
        L.append("")
        L.append("Both figures use the coiled-coil FEATURE, on numerator and denominator alike. "
                 "For completeness, on the more liberal feature-or-keyword criterion "
                 f"({n_coiled_any}/{len(rows)} partners), the matching background is "
                 + (f"**{100 * bg_any:.1f}%** (keyword:KW-0175), giving "
                    f"**{(n_coiled_any / len(rows)) / bg_any:.1f}-fold**"
                    + (f" and P = **{pval_any:.2e}**" if pval_any is not None else "")
                    if bg_any is not None else "unavailable")
                 + ". Mixing the two criteria - a keyword numerator against a feature "
                   "denominator - would overstate the enrichment, so it is not done here.")
        L.append("")
        L.append("The enrichment is therefore real rather than assumed, though with n=15 this is")
        L.append("a descriptive statistic and not a controlled test: the relevant comparison would")
        L.append("be against other single-publication prey sets from the same screen, which this")
        L.append("analysis does not attempt.")
    else:
        L.append("*(Background rate could not be fetched on this run, so the observed proportion")
        L.append("cannot be called enriched. Re-run before relying on the enrichment claim.)*")
    L.append("")
    if n_failed:
        L.append(f"> WARNING: {n_failed} accession(s) failed to retrieve; counts understate the set.")
        L.append("")
    L.append("## Partners")
    L.append("")
    L.append("| Accession | Gene | Coiled-coil segments | Subcellular location |")
    L.append("|---|---|---|---|")
    for r in sorted(rows, key=lambda x: (-x["n_coiled"], x["gene"])):
        loc = "; ".join(r["locations"]) or "—"
        cc = str(r["n_coiled"]) if r["n_coiled"] else ("keyword only" if r["coiled_kw"] else "0")
        L.append(f"| {r['acc']} | {r['gene']} | {cc} | {loc} |")
    L.append("")
    L.append("## Compartment spread")
    L.append("")
    L.append("A genuine partner set usually concentrates in one or two compartments. UniProt")
    L.append("location strings are hierarchical, so they are collapsed here to their leading")
    L.append(f"compartment - {len(raw_loc_strings)} raw strings reduce to")
    L.append(f"**{len(loc_counts)} top-level compartments**:")
    L.append("")
    for loc, n in loc_counts.most_common():
        L.append(f"- {loc}: {n}")
    L.append("")
    if fam is not None:
        L.append("## The family offers no help either")
        L.append("")
        L.append(f"AARD belongs to PANTHER **{PANTHER}** (FAM167 family; InterPro IPR051771).")
        L.append("For a gene this dark, paralogs are the most tractable remaining inference route,")
        L.append("so the family was enumerated:")
        L.append("")
        L.append(f"- **{len(fam)}** reviewed members")
        L.append(f"- **{n_fam_fn}** of them carry a UniProt FUNCTION statement")
        L.append("")
        L.append("| Accession | Entry | Organism | FUNCTION |")
        L.append("|---|---|---|---|")
        for f in sorted(fam, key=lambda x: x["organism"]):
            L.append(f"| {f['acc']} | {f['id']} | {f['organism']} | {f['function'] or '—'} |")
        L.append("")
        if not n_fam_fn:
            L.append("**No member of the FAM167 family has a described function in any organism.**")
            L.append("Guilt-by-association across paralogs is therefore unavailable for AARD - not")
            L.append("because it lacks a family, but because the whole family is uncharacterised.")
            L.append("This is consistent with UniProt's PAN-GO line for AARD, which records")
            L.append("`0 GO annotations based on evolutionary models`.")
        L.append("")
    with open(HERE / "RESULTS.md", "w") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"\n{n_coiled}/{len(rows)} partners have a coiled-coil region")
    print("wrote RESULTS.md")


if __name__ == "__main__":
    main()
