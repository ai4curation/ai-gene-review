"""Compare curated MOD gene descriptions with ai-gene-review `description` fields.

Reads genes/<org>/<gene>/<gene>-descriptions.yaml (from
`ai-gene-review fetch-descriptions-bulk <org>`) and the matching
<gene>-ai-review.yaml, and writes a YAML table with, per gene:

- whether a curated (MOD-provided) description exists
- word counts of the MOD and AI descriptions
- MOD content terms (named genes/proteins, informative words) absent from the
  AI description: a crude, recall-oriented pointer to facts worth checking.
  It is a lexical heuristic, not a judgment of correctness.

With ``--findings-output`` it also collects the reviewer ``findings`` (gap,
discrepancy, insight) recorded in the descriptions files into one worklist,
grouped by category.

Usage:
    uv run python projects/MOD_DESCRIPTIONS/compare_descriptions.py worm \
        -o projects/MOD_DESCRIPTIONS/worm-comparison.yaml \
        --findings-output projects/MOD_DESCRIPTIONS/worm-findings.yaml
"""

import argparse
import re
from pathlib import Path

import yaml

STOP = set(
    """a an and are as at be been by for from has have in into is it its of on or
    that the their this to was were which with also both can during encodes encode
    encoded gene genes protein proteins function functions required involved activity
    activities role roles may other such normal normally well these those via through
    expressed expression including include includes predicted located localizes
    localize than not only one two several between within while where when
    """.split()
)


def content_terms(text: str) -> set[str]:
    """Lowercased informative tokens; keeps gene-like tokens such as cav-1 or rab-11.1.

    >>> sorted(content_terms("RAB-11.1 localizes to recycling endosomes and CAV-1 granules"))
    ['cav-1', 'endosomes', 'granules', 'rab-11.1', 'recycling']
    """
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-.][A-Za-z0-9]+)*", text)
    return {t.lower() for t in tokens if len(t) > 3 or "-" in t} - STOP


def stem(t: str) -> str:
    return re.sub(r"(ies|es|s|ing|ed|ation|ly)$", "", t)


def compare(org: str, genes_dir: Path) -> list[dict]:
    rows = []
    for dfile in sorted((genes_dir / org).glob("*/*-descriptions.yaml")):
        gene = dfile.parent.name
        d = yaml.safe_load(dfile.read_text()) or {}
        mod = next(
            (x["text"] for x in d.get("descriptions", []) if x.get("source") == "Alliance_Imported"),
            None,
        )
        rfile = dfile.parent / f"{gene}-ai-review.yaml"
        ai = ""
        if rfile.exists():
            ai = (yaml.safe_load(rfile.read_text()) or {}).get("description") or ""
        row = {
            "gene": gene,
            "has_mod_curated": mod is not None,
            "mod_words": len(mod.split()) if mod else 0,
            "ai_words": len(ai.split()),
        }
        if mod and ai:
            ai_stems = {stem(t) for t in content_terms(ai)}
            missing = sorted(t for t in content_terms(mod) if stem(t) not in ai_stems)
            mod_terms = content_terms(mod)
            row["mod_terms_missing_from_ai"] = missing
            row["mod_term_recall"] = round(1 - len(missing) / len(mod_terms), 2) if mod_terms else None
        rows.append(row)
    return rows


def collect_findings(org: str, genes_dir: Path) -> dict[str, list[dict]]:
    """Gather reviewer findings from every descriptions file, grouped by category."""
    out: dict[str, list[dict]] = {}
    for dfile in sorted((genes_dir / org).glob("*/*-descriptions.yaml")):
        d = yaml.safe_load(dfile.read_text()) or {}
        for f in d.get("findings") or []:
            out.setdefault(f["category"], []).append(
                {"gene": dfile.parent.name, "text": f["text"], "sources": f.get("sources") or []}
            )
    return dict(sorted(out.items()))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("organism")
    p.add_argument("--genes-dir", type=Path, default=Path("genes"))
    p.add_argument("-o", "--output", type=Path)
    p.add_argument("--findings-output", type=Path)
    a = p.parse_args()
    rows = compare(a.organism, a.genes_dir)
    with_mod = [r for r in rows if r["has_mod_curated"]]
    recalls = sorted(r["mod_term_recall"] for r in with_mod if r.get("mod_term_recall") is not None)
    summary = {
        "organism": a.organism,
        "genes_with_descriptions_file": len(rows),
        "genes_with_mod_curated_description": len(with_mod),
        "median_mod_words": sorted(r["mod_words"] for r in with_mod)[len(with_mod) // 2] if with_mod else None,
        "median_ai_words": sorted(r["ai_words"] for r in rows)[len(rows) // 2] if rows else None,
        "median_mod_term_recall": recalls[len(recalls) // 2] if recalls else None,
    }
    out = yaml.safe_dump({"summary": summary, "genes": rows}, sort_keys=False, width=100)
    if a.output:
        a.output.write_text(out)
    if a.findings_output:
        findings = collect_findings(a.organism, a.genes_dir)
        summary["findings"] = {k: len(v) for k, v in findings.items()}
        a.findings_output.write_text(yaml.safe_dump(findings, sort_keys=False, width=100))
    print(yaml.safe_dump(summary, sort_keys=False))


if __name__ == "__main__":
    main()
