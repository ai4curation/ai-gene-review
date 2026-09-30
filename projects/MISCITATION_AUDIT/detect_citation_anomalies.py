#!/usr/bin/env python3
"""Mechanical detectors for citation defects that no reviewer has flagged yet.

The harvester (`harvest_citations.py`) aggregates defects reviewers already
found. This script looks for candidates *nobody has looked at*, using two cheap
signals that require no judgement:

**Check A -- unresolvable identifiers.** Every distinct PMID cited anywhere in
the reviews is checked against NCBI esummary. A PMID that returns no record
cannot support anything. (This is how `PMID:34521819` on STAT2 was caught.)
Requires network; PMIDs already present in `publications/` are skipped, since a
cached record is proof the identifier resolved.

**Check B -- paralog mismatch.** For a citation used by two or more genes of one
numbered symbol family (ELOVL1/2/3, NAA10/NAA40, TIM9/TIM10), the cached record
is searched for family-member symbols. If the paper names some members of the
family but *not* a gene citing it, that gene is a candidate paralog mismatch --
the signature of a citation copied across a family when it characterises only
one member. This is what makes PMID:10970790 (about ELOVL5) visible on ELOVL1,
ELOVL2 and ELOVL3. Bare co-citation across a family is NOT flagged: legitimate
family-wide papers are common, and are dumped to the TSV only.

Neither check asserts that a hit is wrong -- both produce candidates for a human
to adjudicate. If nothing is found the report says so.

Usage:
    uv run python projects/MISCITATION_AUDIT/detect_citation_anomalies.py \
        --genes-dir genes --publications-dir publications \
        --out-dir projects/MISCITATION_AUDIT/reports [--check-pubmed]
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict

import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader  # type: ignore

ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
# Trailing digits split a symbol into stem + index: ELOVL1 -> ("ELOVL", "1").
SYMBOL_RE = re.compile(r"^([A-Za-z][A-Za-z_.-]*?)(\d+)([A-Za-z]?)$")


def collect_usage(genes_dir: str) -> tuple[int, dict[str, set[tuple[str, str]]]]:
    usage: dict[str, set[tuple[str, str]]] = defaultdict(set)
    files = 0
    for path in sorted(glob.glob(os.path.join(genes_dir, "*", "*", "*-ai-review.yaml"))):
        try:
            with open(path) as fh:
                doc = yaml.load(fh, Loader=Loader)
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        files += 1
        parts = path.split(os.sep)
        i = parts.index("genes")
        species, gene = parts[i + 1], parts[i + 2]
        for ref in doc.get("references") or []:
            if isinstance(ref, dict) and ref.get("id"):
                usage[ref["id"]].add((species, gene))
    return files, usage


def cached_pmids(publications_dir: str) -> set[str]:
    out = set()
    for p in glob.glob(os.path.join(publications_dir, "PMID_*.md")):
        out.add(os.path.basename(p)[len("PMID_"):-len(".md")])
    return out


def check_pubmed(pmids: list[str], batch: int = 150, pause: float = 0.4) -> set[str]:
    """Return the subset of `pmids` for which NCBI returns no usable record."""
    missing: set[str] = set()
    for i in range(0, len(pmids), batch):
        chunk = pmids[i : i + batch]
        url = f"{ESUMMARY}?" + urllib.parse.urlencode(
            {"db": "pubmed", "retmode": "json", "id": ",".join(chunk)}
        )
        try:
            with urllib.request.urlopen(url, timeout=60) as fh:
                data = json.load(fh)
        except Exception as exc:  # network/parse failure is not evidence of absence
            print(f"  ! esummary batch {i // batch} failed ({exc}); skipping those {len(chunk)}")
            continue
        result = data.get("result") or {}
        for pmid in chunk:
            rec = result.get(pmid)
            if not isinstance(rec, dict) or rec.get("error") or not rec.get("title"):
                missing.add(pmid)
        time.sleep(pause)
    return missing


def family_clusters(usage: dict[str, set[tuple[str, str]]], min_members: int = 3) -> list[dict]:
    """Citations shared by >= min_members genes from one numbered symbol family."""
    rows = []
    for citation, genes in usage.items():
        stems: dict[tuple[str, str], set[str]] = defaultdict(set)
        for species, gene in genes:
            m = SYMBOL_RE.match(gene)
            if m:
                stems[(species, m.group(1).upper())].add(gene)
        for (species, stem), members in stems.items():
            if len(members) >= min_members:
                rows.append(
                    {
                        "citation": citation,
                        "species": species,
                        "family_stem": stem,
                        "n_members": len(members),
                        "members": ";".join(sorted(members)),
                    }
                )
    rows.sort(key=lambda r: -r["n_members"])
    return rows


def read_cached_text(publications_dir: str, citation: str) -> str | None:
    """Return cached publication text for a PMID/DOI citation, if present."""
    prefix, _, ident = citation.partition(":")
    if prefix.upper() == "PMID":
        name = f"PMID_{ident}.md"
    elif prefix.upper() == "DOI":
        name = f"DOI_{ident.replace('/', '_')}.md"
    else:
        return None
    path = os.path.join(publications_dir, name)
    if not os.path.exists(path):
        return None
    try:
        return open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None


def paralog_mismatches(
    usage: dict[str, set[tuple[str, str]]], publications_dir: str, min_members: int = 2
) -> list[dict]:
    """Citing genes absent from a paper that names other members of their family."""
    rows = []
    for citation, genes in usage.items():
        stems: dict[tuple[str, str], set[str]] = defaultdict(set)
        for species, gene in genes:
            m = SYMBOL_RE.match(gene)
            if m:
                stems[(species, m.group(1).upper())].add(gene)
        text = None
        for (species, stem), members in stems.items():
            if len(members) < min_members:
                continue
            if text is None:
                text = read_cached_text(publications_dir, citation)
                if text is None:
                    break  # no cached record; cannot judge this citation at all
                text = text.upper()
            # every symbol of this family the paper actually names
            named = set(re.findall(rf"\b{re.escape(stem)}\d+[A-Z]?\b", text))
            if not named:
                continue  # paper names no family member; nothing to compare
            # `absent` is a subset of `members`, so no size guard is meaningful here.
            absent = sorted(g for g in members if g.upper() not in named)
            if absent:
                rows.append(
                    {
                        "citation": citation,
                        "species": species,
                        "family_stem": stem,
                        "named_in_paper": ";".join(sorted(named)),
                        "citing_but_absent": ";".join(absent),
                        "n_absent": len(absent),
                    }
                )
    rows.sort(key=lambda r: -r["n_absent"])
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", default="genes")
    ap.add_argument("--publications-dir", default="publications")
    ap.add_argument("--out-dir", default="projects/MISCITATION_AUDIT/reports")
    ap.add_argument("--check-pubmed", action="store_true", help="run Check A (needs network)")
    ap.add_argument("--min-family", type=int, default=3)
    ap.add_argument(
        "--check-paralogs",
        action="store_true",
        help="run Check B (known low precision; see the project page before trusting output)",
    )
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)

    files, usage = collect_usage(args.genes_dir)
    all_pmids = sorted({r.split(":", 1)[1] for r in usage if r.startswith("PMID:")})
    cached = cached_pmids(args.publications_dir)
    uncached = [p for p in all_pmids if p not in cached]

    lines = [
        "---",
        'title: "Citation anomaly detectors"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Citation anomaly detectors",
        "",
        f"Generated by `detect_citation_anomalies.py` over **{files}** review files, "
        f"**{len(all_pmids)}** distinct PMIDs ({len(cached & set(all_pmids))} with a cached record).",
        "",
        "Both checks produce **candidates for adjudication, not verdicts**.",
        "",
    ]

    # ---- Check A ----
    lines += ["## Check A - unresolvable identifiers", ""]
    if not args.check_pubmed:
        lines += [
            f"Not run (pass `--check-pubmed`). {len(uncached)} cited PMIDs have no cached "
            "record and would be queried.",
            "",
        ]
        missing = []
    else:
        print(f"checking {len(uncached)} uncached PMIDs against NCBI ...")
        missing = sorted(check_pubmed(uncached))
        if not missing:
            lines += ["Every cited PMID resolved to a PubMed record.", ""]
        else:
            lines += [
                f"**{len(missing)}** cited PMIDs returned no PubMed record. An identifier that "
                "does not resolve cannot support any annotation.",
                "",
                "| PMID | Cited by |",
                "|---|---|",
            ]
            for p in missing:
                users = sorted(usage.get(f"PMID:{p}", set()))
                lines.append(f"| `PMID:{p}` | {', '.join(f'{s}/{g}' for s, g in users)} |")
            lines.append("")

    # ---- Check B ----
    clusters = family_clusters(usage, args.min_family) if args.check_paralogs else []
    mismatches = paralog_mismatches(usage, args.publications_dir) if args.check_paralogs else []
    lines += [
        "## Check B - paralog mismatch",
        "",
        "A citation whose cached record names some members of a numbered symbol family but "
        "**not** a gene that cites it. Candidates for a citation copied across a family that "
        "in fact characterises one member.",
        "",
        f"({len(clusters)} citation/family co-citation pairs were considered at >= "
        f"{args.min_family} members; bare co-citation is not itself a defect and is dumped to "
        "`family_clusters.tsv` only.)",
        "",
    ]
    if not args.check_paralogs:
        lines += [
            "Not run (pass `--check-paralogs`). This check is documented as low precision: it "
            "misses alias-renamed cases and its hits are dominated by legitimate complex-wide "
            "papers. It is opt-in so its output is not mistaken for a findings list.",
            "",
        ]
    elif not mismatches:
        lines += ["No paralog mismatches detected.", ""]
    else:
        lines += [
            f"**{len(mismatches)}** candidates.",
            "",
            "| Citation | Family | Named in paper | Cites it but absent |",
            "|---|---|---|---|",
        ]
        for r in mismatches[:80]:
            lines.append(
                f"| `{r['citation']}` | {r['species']} {r['family_stem']}* "
                f"| {r['named_in_paper'].replace(';', ', ')} "
                f"| **{r['citing_but_absent'].replace(';', ', ')}** |"
            )
        if len(mismatches) > 80:
            lines.append(f"| ... | ... | ... | {len(mismatches) - 80} more in the TSV |")
        lines.append("")

    if args.check_paralogs:
        with open(os.path.join(args.out_dir, "paralog_mismatches.tsv"), "w", newline="") as fh:
            w = csv.DictWriter(
                fh,
                fieldnames=[
                    "citation", "species", "family_stem", "named_in_paper",
                    "citing_but_absent", "n_absent",
                ],
                delimiter="\t",
            )
            w.writeheader()
            w.writerows(mismatches)

        with open(os.path.join(args.out_dir, "family_clusters.tsv"), "w", newline="") as fh:
            w = csv.DictWriter(
                fh,
                fieldnames=["citation", "species", "family_stem", "n_members", "members"],
                delimiter="\t",
            )
            w.writeheader()
            w.writerows(clusters)

    if args.check_pubmed:
        with open(os.path.join(args.out_dir, "unresolvable_pmids.tsv"), "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["pmid", "cited_by"])
            for p in missing:
                users = sorted(usage.get(f"PMID:{p}", set()))
                w.writerow([f"PMID:{p}", ";".join(f"{s}/{g}" for s, g in users)])

    path = os.path.join(args.out_dir, "ANOMALIES.md")
    with open(path, "w") as fh:
        fh.write("\n".join(lines))
    print(f"{len(clusters)} co-citation pairs; {len(mismatches)} paralog-mismatch candidates; wrote {path}")


if __name__ == "__main__":
    main()
