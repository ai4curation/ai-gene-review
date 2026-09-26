"""Generate the dated homology-propagation statistics page.

Writes ``projects/HOMOLOGY_PROPAGATION/propagation-stats.md`` from the same
rows as the propagation browser, so project pages can link to current numbers
instead of embedding counts that go stale. Every table is computed; nothing is
hard-coded.
"""

from __future__ import annotations

import argparse
import datetime
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

from ai_gene_review.export.propagation_export import (
    DEFAULT_DATA_DIR,
    SUPPORT_ORDER,
    collect_propagation_data,
)

ACTIONS = ["ACCEPT", "KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "MODIFY",
           "REMOVE", "UNDECIDED"]
NEGATIVE = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}
IBA_BUCKETS = [
    ("SAME", "IBA to the same term"),
    ("MORE_SPECIFIC", "IBA to a more specific term (already entails the ISO row)"),
    ("MORE_GENERAL", "IBA only to a more general term (ISO adds specificity)"),
    ("NONE", "No related IBA (ISO adds a new assertion)"),
]
OTHER_EVIDENCE = [
    ("SAME", "Experimental to the same term"),
    ("MORE_SPECIFIC", "Experimental to a more specific term"),
    ("MORE_GENERAL", "Experimental only to a more general term"),
    ("NONE", "No related experimental annotation"),
]


def _reviewed(row: dict[str, Any]) -> bool:
    return row.get("action") in ACTIONS


def _pct(n: int, d: int) -> str:
    return f"{100 * n / d:.0f}%" if d else "–"


def _table(headers: list[str], rows: Iterable[Sequence[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join("---" if i == 0 else "---:" for i in range(len(headers))) + "|"]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def _action_breakdown(rows: list[dict[str, Any]], key: Callable[[dict], str],
                      order: list[str] | None = None, label: str = "") -> str:
    """Rows per group: total, reviewed, and the review-action mix."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        groups[key(r)].append(r)
    keys = [k for k in order if groups.get(k)] if order else sorted(
        groups, key=lambda k: (-len(groups[k]), k))
    out = []
    for k in keys:
        g = groups.get(k, [])
        reviewed = [r for r in g if _reviewed(r)]
        c = Counter(r["action"] for r in reviewed)
        out.append([k, len(g), len(reviewed), *(c.get(a, 0) for a in ACTIONS),
                    _pct(sum(c[a] for a in NEGATIVE), len(reviewed))])
    return _table([label, "Annotations", "Reviewed", *ACTIONS, "REMOVE/OVER/MODIFY"], out)


def species_pair(row: dict[str, Any]) -> str:
    donors = row.get("donor_species") or ["unresolved"]
    return f"{' + '.join(donors)} → {row['target_species']}"


def _merge_symbol_match(values: set[str]) -> str:
    """Combine per-donor symbol matches for one annotation.

    >>> _merge_symbol_match({"SAME_SYMBOL", "DIFFERENT_SYMBOL"})
    'MIXED'
    >>> _merge_symbol_match({"DIFFERENT_SYMBOL", "UNRESOLVED"})
    'DIFFERENT_SYMBOL'
    """
    resolved = values - {"UNRESOLVED"}
    if not resolved:
        return "UNRESOLVED"
    if resolved <= {"SAME_SYMBOL"}:
        return "SAME_SYMBOL"
    if resolved <= {"DIFFERENT_SYMBOL"}:
        return "DIFFERENT_SYMBOL"
    return "MIXED"


def annotation_units(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collapse per-donor GOA rows into one record per annotation.

    Pipelines such as GO_REF:0000096 emit one GOA line per donor, and all of
    them join to the same review entry. Statistics count annotations, so rows
    sharing the review join key -- (gene, term, evidence, reference, negated),
    as in ``load_reviews`` -- are merged. Lines that differ only in a
    non-negating qualifier (``located_in`` vs ``is_active_in``) also join one
    review entry, so they merge too. Donors and donor species are unioned,
    donor support takes the strongest value, and symbol matches combine (a
    same-symbol plus a different-symbol donor is MIXED).
    """
    groups: dict[tuple, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        key = (r["species_dir"], r["gene_dir"], r["term_id"], r["evidence"],
               r["reference"], r["qualifier"].startswith("NOT"))
        groups[key].append(r)
    units = []
    for group in groups.values():
        unit = dict(group[0])
        unit["donor_lines"] = len(group)
        unit["donors"] = list({d["id"]: d for r in group for d in r.get("donors", [])}.values())
        if "donor_species" in unit:
            species = sorted({s for r in group for s in r.get("donor_species", [])})
            if len(species) > 1:
                species = [s for s in species if s != "unresolved"]
            unit["donor_species"] = species
        if "donor_support" in unit:
            unit["donor_support"] = min((r["donor_support"] for r in group),
                                        key=SUPPORT_ORDER.index)
            unit["symbol_match"] = _merge_symbol_match({r["symbol_match"] for r in group})
        units.append(unit)
    return units


def render(rows: list[dict[str, Any]], metadata: dict[str, Any]) -> str:
    """Render the statistics markdown from per-donor browser rows."""
    donor_line_count = len(rows)
    rows = annotation_units(rows)
    iso = [r for r in rows if r["evidence"] == "ISO"]
    donor_rows = [r for r in rows if "donor_support" in r]
    parts = [
        "---",
        'title: "Homology Propagation Statistics"',
        "---",
        "# Homology Propagation Statistics",
        "",
        f"Generated {metadata['generated']} by `just propagation-stats` from the cached GOA",
        f"files under `genes/` (donor cache refreshed {metadata.get('donor_cache', '–')}).",
        "Counts cover every gene with a cached GOA file. The unit is one annotation",
        "(gene, term, evidence, reference, negation): pipelines that emit one GOA line",
        "per donor, or split one annotation across qualifiers, are merged",
        f"({donor_line_count:,} GOA lines → {len(rows):,} annotations).",
        "*Reviewed* annotations are those matched to an `existing_annotations` entry",
        "with a final review action.",
        "These numbers are regenerated; do not copy them into project prose.",
        "Browse the rows in the [propagation browser](../../app/propagation/index.html).",
        "",
        "## All propagation methods",
        "",
        _action_breakdown(rows, lambda r: f"{r['evidence']} · {r['method']}", label="Method"),
        "",
        "## ISO: donor species → target species",
        "",
        _action_breakdown(iso, species_pair, label="Donor → target"),
        "",
        "## ISO: does the donor still carry the term?",
        "",
        "Donor support is the donor's current evidence for the exact transferred term",
        "(QuickGO). `INFERRED_ONLY` means the donor itself only has inferred support —",
        "typically a transfer of a transfer. `ABSENT` means the donor was checked and no",
        "longer carries the term.",
        "",
        _action_breakdown(iso, lambda r: r.get("donor_support", "NOT_CHECKED"),
                          order=["EXPERIMENTAL", "INFERRED_ONLY", "ABSENT", "NOT_CHECKED"],
                          label="Donor support"),
        "",
        "## ISO: donor symbol vs target symbol",
        "",
        "A different donor symbol flags paralog or multi-locus sourcing (for example rat",
        "Calm1/Calm2 as donors for mouse Calm3). `MIXED` means the annotation has both a",
        "namesake donor and a differently named one. It prompts a check; it is not a verdict.",
        "",
        _action_breakdown(iso, lambda r: r.get("symbol_match", "UNRESOLVED"),
                          order=["SAME_SYMBOL", "MIXED", "DIFFERENT_SYMBOL", "UNRESOLVED"],
                          label="Symbol match"),
        "",
        "## What does ISO add on top of IBA?",
        "",
        "For each ISO row, the closest IBA annotation on the same target (GO is_a/part_of",
        "closure). Rows in the first two buckets are already implied by PAINT; the last two",
        "are what ISO contributes beyond IBA.",
        "",
    ]
    by_aspect: dict[str, Counter[str]] = defaultdict(Counter)
    for r in iso:
        by_aspect[r["aspect"]][r.get("iba_on_target", "NONE")] += 1
    aspects = sorted(by_aspect)
    total = Counter(r.get("iba_on_target", "NONE") for r in iso)
    parts.append(_table(
        ["IBA on target", *aspects, "All ISO", "Share"],
        [[label, *(by_aspect[a][k] for a in aspects), total[k], _pct(total[k], len(iso))]
         for k, label in IBA_BUCKETS]))
    parts += ["", "Review outcome by IBA coverage (reviewed ISO rows):", "",
              _action_breakdown(iso, lambda r: r.get("iba_on_target", "NONE"),
                                order=[k for k, _ in IBA_BUCKETS], label="IBA on target"),
              "", "ISO rows not implied by IBA, split by the target's own experimental evidence:", ""]
    beyond = [r for r in iso if r.get("iba_on_target") in {"MORE_GENERAL", "NONE"}]
    parts.append(_action_breakdown(beyond, lambda r: r["experimental_on_target"],
                                   order=[k for k, _ in OTHER_EVIDENCE],
                                   label="Experimental on target"))
    parts += ["", "## Recorded propagation reviews", "",
              "Structured `review.propagation_review` classifications (all methods).", ""]
    rc = Counter(r["root_cause"] for r in rows if r.get("root_cause"))
    fm = Counter(m for r in rows for m in r.get("failure_modes", []))
    parts.append(_table(["Root cause", "Annotations"], rc.most_common()) if rc else "_None recorded._")
    parts += ["", _table(["Failure mode", "Annotations"], fm.most_common()) if fm else "", ""]
    parts += ["## Donor coverage", "",
              f"{sum(1 for r in donor_rows if r.get('donor_support') != 'NOT_CHECKED'):,} of "
              f"{len(donor_rows):,} donor-based annotations have at least one donor checked.", ""]
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output", type=Path,
                        default=Path("projects/HOMOLOGY_PROPAGATION/propagation-stats.md"))
    args = parser.parse_args()
    rows = collect_propagation_data(args.root, args.data_dir)["rows"]
    meta_path = args.root / args.data_dir / "refresh-metadata.json"
    donor_meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    text = render(rows, {"generated": datetime.date.today().isoformat(),
                         "donor_cache": donor_meta.get("refreshed", "never")})
    output = args.output if args.output.is_absolute() else args.root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {output} ({len(rows)} GOA lines)")


if __name__ == "__main__":
    main()
