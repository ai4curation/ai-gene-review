"""Tabulate the Sample record lines of the confirmed random-sample pairs.

Reads projects/DANRE_DUPLICATION/random_sample.tsv, takes the accepted
(Compara-confirmed) draws, finds each pair page under pairs/ and parses its
"**Sample record:**" line. Prints a markdown table and counts by fate, level
and evidence. Pairs without a page or a Sample record line are reported as
missing rather than guessed.

Usage (from repo root):
    uv run python projects/DANRE_DUPLICATION/scripts/tabulate_sample.py
"""

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path("projects/DANRE_DUPLICATION")
RECORD = re.compile(r"\*\*Sample record:\*\*\s*(.+)")


def pair_page(a: str, b: str) -> Path | None:
    a, b = a.replace(":", "_"), b.replace(":", "_")
    for x, y in ((a, b), (b, a)):
        page = ROOT / "pairs" / f"{x}_{y}" / f"{x}_{y}.md"
        if page.exists():
            return page
    return None


def main() -> None:
    rows = [r for r in csv.DictReader((ROOT / "random_sample.tsv").open(), delimiter="\t")
            if r["status"] == "accepted"]
    counts = {k: Counter() for k in ("fate", "level", "evidence")}
    print("| Draw | Pair | Compara node | Fate | Level | Evidence | Identity |")
    print("|---|---|---|---|---|---|---|")
    missing = []
    for r in rows:
        page = pair_page(r["gene_a"], r["gene_b"])
        m = RECORD.search(page.read_text()) if page else None
        if not m:
            missing.append(f"{r['gene_a']}/{r['gene_b']}")
            continue
        rec = dict(kv.strip().split("=", 1) for kv in m.group(1).split(";") if "=" in kv)
        for k in counts:
            counts[k][rec.get(k, "?")] += 1
        link = page.relative_to(ROOT).as_posix()
        print(f"| {r['draw']} | [{r['gene_a']} / {r['gene_b']}]({link}) | {r['compara_level']} | "
              f"{rec.get('fate')} | {rec.get('level')} | {rec.get('evidence')} | {rec.get('identity')} |")
    print(f"\nConfirmed pairs: {len(rows)}; tabulated: {len(rows) - len(missing)}")
    if missing:
        print("Missing Sample record: " + ", ".join(missing))
    for k, c in counts.items():
        print(f"\n{k}: " + ", ".join(f"{v} {n}" for v, n in c.most_common()))
    draws = list(csv.DictReader((ROOT / "random_sample.tsv").open(), delimiter="\t"))
    status = Counter(d["status"] for d in draws)
    print(f"\nDraws: {len(draws)}; " + ", ".join(f"{v} {n}" for v, n in status.most_common()))


if __name__ == "__main__":
    main()
