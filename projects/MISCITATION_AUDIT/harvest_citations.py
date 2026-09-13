#!/usr/bin/env python3
"""Harvest and triage citation defects already recorded in gene-review YAML.

Reviewers record their judgement of each cited reference in
``references[].reference_review.correctness``. Two values mark a citation
defect:

- ``WRONG_IDENTIFIER`` -- the identifier resolves to a *different paper* than
  the one intended. This is the high-confidence, mechanically-checkable class.
- ``MISCITED`` -- the right paper, but it does not support the claim. Lower
  yield and more subjective.

These have accumulated one gene at a time and have never been aggregated. This
script builds a register keyed on the **citation** rather than the gene, which
matters because a single bad citation frequently contaminates several genes at
once (typically paralogs of one family, or partners in one complex).

The most actionable output is **contamination spread**: a citation that one
reviewer flagged as WRONG_IDENTIFIER, but which *other* gene reviews still cite
without a flag. Those are unreviewed instances of a known-bad citation.

Nothing about the outcome is hard-coded; if no defects are found the report
says so.

Usage:
    uv run python projects/MISCITATION_AUDIT/harvest_citations.py \
        --genes-dir genes --out-dir projects/MISCITATION_AUDIT/reports
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
from collections import Counter, defaultdict

import yaml

try:  # fast C loader if available
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader  # type: ignore

DEFECT_FLAGS = ("WRONG_IDENTIFIER", "MISCITED")
CONTEXT_FLAGS = ("DISPUTED", "LOW_QUALITY")


def gene_key(path: str) -> tuple[str, str]:
    """Return (species, gene) from genes/<species>/<gene>/<gene>-ai-review.yaml."""
    parts = path.split(os.sep)
    try:
        i = parts.index("genes")
        return parts[i + 1], parts[i + 2]
    except (ValueError, IndexError):
        return "?", os.path.basename(path)


def scan(genes_dir: str):
    """Collect per-citation flags and the full citation->genes usage map."""
    flags: list[dict] = []
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
        species, gene = gene_key(path)
        # A citation that appears as an annotation's original_reference_id came from
        # GOA; one that appears only in `references` was added by a reviewer. The
        # split decides who owns the fix: the assigning group, or us.
        goa_refs = {
            a.get("original_reference_id")
            for a in (doc.get("existing_annotations") or [])
            if isinstance(a, dict)
        }

        for ref in doc.get("references") or []:
            if not isinstance(ref, dict):
                continue
            rid = ref.get("id")
            if not rid:
                continue
            usage[rid].add((species, gene))

            rr = ref.get("reference_review") or {}
            correctness = rr.get("correctness")
            if correctness in DEFECT_FLAGS + CONTEXT_FLAGS:
                flags.append(
                    {
                        "species": species,
                        "gene": gene,
                        "citation": rid,
                        "correctness": correctness,
                        "source": "GOA" if rid in goa_refs else "review-only",
                        "relevance": rr.get("relevance") or "",
                        "cited_title": (ref.get("title") or "").replace("\n", " ").strip(),
                        "review_notes": (rr.get("review_notes") or "").replace("\n", " ").strip(),
                    }
                )
    return files, flags, usage


def build_register(flags: list[dict], usage: dict[str, set]):
    """One row per distinct citation flagged as a defect, with contamination spread."""
    by_citation: dict[str, list[dict]] = defaultdict(list)
    for f in flags:
        if f["correctness"] in DEFECT_FLAGS:
            by_citation[f["citation"]].append(f)

    rows = []
    for citation, fs in by_citation.items():
        flagged = {(f["species"], f["gene"]) for f in fs}
        all_users = usage.get(citation, set())
        unflagged = sorted(all_users - flagged)
        worst = "WRONG_IDENTIFIER" if any(f["correctness"] == "WRONG_IDENTIFIER" for f in fs) else "MISCITED"
        rows.append(
            {
                "citation": citation,
                "worst_flag": worst,
                "n_flagged_genes": len(flagged),
                "n_unflagged_users": len(unflagged),
                "flagged_genes": ";".join(f"{s}/{g}" for s, g in sorted(flagged)),
                "unflagged_users": ";".join(f"{s}/{g}" for s, g in unflagged),
                "example_note": max((f["review_notes"] for f in fs), key=len, default="")[:400],
            }
        )
    rows.sort(key=lambda r: (r["worst_flag"] != "WRONG_IDENTIFIER", -r["n_unflagged_users"], -r["n_flagged_genes"]))
    return rows


def write_report(out_dir: str, files: int, flags: list[dict], register: list[dict]) -> str:
    counts = Counter(f["correctness"] for f in flags)
    goa = sum(1 for f in flags if f["correctness"] in DEFECT_FLAGS and f["source"] == "GOA")
    ours = sum(1 for f in flags if f["correctness"] in DEFECT_FLAGS and f["source"] != "GOA")
    wrong = [r for r in register if r["worst_flag"] == "WRONG_IDENTIFIER"]
    miscited = [r for r in register if r["worst_flag"] == "MISCITED"]
    multi = [r for r in wrong if r["n_flagged_genes"] > 1]
    spreading = [r for r in wrong if r["n_unflagged_users"] > 0]

    lines = [
        "---",
        'title: "Citation defect register"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Citation defect register",
        "",
        f"Generated by `harvest_citations.py` over **{files}** review files.",
        "",
        f"Of the defect-flagged citations, **{goa}** came from GOA (they appear as an "
        f"annotation's `original_reference_id`, so the fix belongs to the assigning group) "
        f"and **{ours}** were added by a reviewer here.",
        "",
        "## Counts",
        "",
        "| Flag | Gene-level rows | Distinct citations |",
        "|---|---|---|",
        f"| WRONG_IDENTIFIER | {counts.get('WRONG_IDENTIFIER', 0)} | {len(wrong)} |",
        f"| MISCITED | {counts.get('MISCITED', 0)} | {len(miscited)} |",
        f"| DISPUTED | {counts.get('DISPUTED', 0)} | - |",
        f"| LOW_QUALITY | {counts.get('LOW_QUALITY', 0)} | - |",
        "",
    ]

    if not wrong:
        lines += ["No WRONG_IDENTIFIER citations found.", ""]
    else:
        lines += [
            f"## Citations poisoning more than one gene ({len(multi)})",
            "",
            "A single bad citation reused across paralogs or complex partners. One upstream",
            "correction clears every listed gene.",
            "",
            "| Citation | Genes |",
            "|---|---|",
        ]
        for r in multi:
            lines.append(f"| `{r['citation']}` | {r['flagged_genes'].replace(';', ', ')} |")
        lines.append("")

        lines += [
            f"## Contamination spread ({len(spreading)})",
            "",
            "Citations flagged WRONG_IDENTIFIER in at least one review that are **still cited",
            "without a flag** elsewhere. These are unreviewed instances of a known-bad citation",
            "and are the highest-value triage targets.",
            "",
        ]
        if not spreading:
            lines += ["None: every use of every known-bad citation has been flagged.", ""]
        else:
            lines += ["| Citation | Flagged in | Unflagged uses |", "|---|---|---|"]
            for r in spreading:
                lines.append(
                    f"| `{r['citation']}` | {r['flagged_genes'].replace(';', ', ')} "
                    f"| {r['unflagged_users'].replace(';', ', ')} |"
                )
            lines.append("")

        lines += [f"## All WRONG_IDENTIFIER citations ({len(wrong)})", "", "| Citation | Genes | Note |", "|---|---|---|"]
        for r in wrong:
            note = r["example_note"][:160].replace("|", "\\|")
            lines.append(f"| `{r['citation']}` | {r['flagged_genes'].replace(';', ', ')} | {note} |")
        lines.append("")

    path = os.path.join(out_dir, "REPORT.md")
    with open(path, "w") as fh:
        fh.write("\n".join(lines))
    return path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", default="genes")
    ap.add_argument("--out-dir", default="projects/MISCITATION_AUDIT/reports")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)

    files, flags, usage = scan(args.genes_dir)
    register = build_register(flags, usage)

    flags_path = os.path.join(args.out_dir, "citation_flags.tsv")
    with open(flags_path, "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "species", "gene", "citation", "correctness", "source", "relevance",
                "cited_title", "review_notes",
            ],
            delimiter="\t",
        )
        w.writeheader()
        w.writerows(sorted(flags, key=lambda f: (f["correctness"], f["species"], f["gene"])))

    reg_path = os.path.join(args.out_dir, "bad_citations.tsv")
    with open(reg_path, "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "citation", "worst_flag", "n_flagged_genes", "n_unflagged_users",
                "flagged_genes", "unflagged_users", "example_note",
            ],
            delimiter="\t",
        )
        w.writeheader()
        w.writerows(register)

    report = write_report(args.out_dir, files, flags, register)
    print(f"scanned {files} review files; {len(flags)} flagged citations; {len(register)} distinct defective citations")
    print(f"wrote {flags_path}\n      {reg_path}\n      {report}")


if __name__ == "__main__":
    main()
