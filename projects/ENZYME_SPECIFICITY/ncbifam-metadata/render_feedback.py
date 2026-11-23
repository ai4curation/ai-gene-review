"""Build FEEDBACK.md, the NCBIfam change list, from the check output and the triage.

Checks first, and fails rather than writing a misleading report:

* every ``unrelated``, ``narrower`` and ``no_go_for_model_ec`` pair in
  ``release_table_check.yaml`` has a triage entry, and every verdict is a known one;
* conversely, every triaged (model, GO term) pair is one of those flagged pairs, unless
  its entry is marked ``source: sweep`` (a model the EC comparison cannot catch);
* every triaged (model, GO term) pair exists in the NCBIfam release table;
* every ``better`` term exists in the GO database and is not obsolete.

    uv run python projects/ENZYME_SPECIFICITY/ncbifam-metadata/render_feedback.py
"""

from __future__ import annotations

import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

import yaml

from ai_gene_review.validation.enzyme_family_cutoff import NCBIfam

sys.path.insert(0, str(Path(__file__).parent))
from check_release_table import GoHierarchy, refseq_hits  # noqa: E402

from ai_gene_review.validation.enzyme_family_cutoff import is_complete_ec  # noqa: E402

HERE = Path(__file__).parent
CACHE = Path(".cache")
GO_DB = Path.home() / ".data" / "oaklib" / "go.db"
REPORTED = ["WRONG_REACTION", "WRONG_COFACTOR", "EC_SUSPECT", "CHECK"]
VERDICTS = set(REPORTED) | {"ACCEPTABLE"}
TRIAGED = {"unrelated", "narrower", "no_go_for_model_ec"}
TITLES = {
    "WRONG_REACTION": "GO term names a different enzyme's reaction",
    "WRONG_COFACTOR": "GO term names the same transformation with another cofactor, donor or acceptor",
    "EC_SUSPECT": "The GO term fits the product name; the EC number does not",
    "CHECK": "Unclear from names alone",
}


def go_label(db: sqlite3.Connection, go: str) -> tuple[str | None, bool]:
    """GO label and whether the term is deprecated, from the semsql GO database."""
    label = db.execute(
        "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'", (go,)
    ).fetchone()
    deprecated = db.execute(
        "SELECT 1 FROM statements WHERE subject=? AND predicate='owl:deprecated' "
        "AND value='true'",
        (go,),
    ).fetchone()
    return (label[0] if label else None), bool(deprecated)


MAX_CANDIDATES = 10


def candidate_text(
    ec_numbers: list[str], hierarchy: GoHierarchy, go_db: sqlite3.Connection
) -> str:
    """The GO terms that cross-reference a model's own EC numbers, or why none are shown.

    Computed from the model itself, not from the check's pair records, so a model added
    by hand from the sweep gets the same treatment as a flagged one. A partial EC would
    match a whole EC subclass, so its terms are not offered; a complete EC beside it
    still is. An empty result means no GO term carries the EC as a cross-reference,
    not that GO lacks a term for the reaction: many GO terms cross-reference only Rhea.

    >>> class Hierarchy:
    ...     def terms_for_ec(self, ec):
    ...         return {"3.4.16.4": {"GO:0009002"}}.get(ec, set())
    >>> db = sqlite3.connect(":memory:")
    >>> _ = db.execute("CREATE TABLE statements (subject, predicate, value)")
    >>> _ = db.execute("INSERT INTO statements VALUES ('GO:0009002', 'rdfs:label', 'x')")
    >>> candidate_text([], Hierarchy(), db)
    '(model has no EC)'
    >>> candidate_text(["2.1.2.-"], Hierarchy(), db)
    '(partial EC 2.1.2.-; not listed)'
    >>> candidate_text(["3.5.4.4"], Hierarchy(), db)
    '(no GO term cross-references EC 3.5.4.4)'
    >>> candidate_text(["3.4.16.4", "3.4.21.-"], Hierarchy(), db)
    'GO:0009002 x (partial EC 3.4.21.- not listed)'
    >>> candidate_text(["3.4.16.4", "3.5.4.4"], Hierarchy(), db)
    'EC 3.4.16.4: GO:0009002 x / EC 3.5.4.4: (no GO term cross-references it)'
    """
    if not ec_numbers:
        return "(model has no EC)"
    partial = [ec for ec in ec_numbers if not is_complete_ec(ec)]
    complete = [ec for ec in ec_numbers if is_complete_ec(ec)]
    if not complete:
        return f"(partial EC {', '.join(partial)}; not listed)"

    def describe(ec: str, name: str) -> str:
        terms = sorted(hierarchy.terms_for_ec(ec))
        if not terms:
            return f"(no GO term cross-references {name})"
        if len(terms) > MAX_CANDIDATES:
            return f"({len(terms)} terms under EC {ec}; too broad to list)"
        return "; ".join(f"{t} {go_label(go_db, t)[0]}" for t in terms)

    # with several ECs, each EC's terms are labelled, so a suspect EC can be told apart
    if len(complete) == 1:
        text = describe(complete[0], f"EC {complete[0]}")
    else:
        text = " / ".join(f"EC {ec}: {describe(ec, 'it')}" for ec in complete)
    if partial:
        text += f" (partial EC {', '.join(partial)} not listed)"
    return text


def main() -> None:
    """Check the triage against the data, then write FEEDBACK.md."""
    check = yaml.safe_load((HERE / "release_table_check.yaml").read_text())
    triage = yaml.safe_load((HERE / "triage.yaml").read_text())["triage"]
    families = {f.accession: f for f in NCBIfam(CACHE / "ncbifam").families}
    go_db = sqlite3.connect(GO_DB)
    hierarchy = GoHierarchy(GO_DB)
    hits = refseq_hits(CACHE / "ncbifam")
    flagged = [r for r in check["pairs"] if r["placement"] in TRIAGED]
    pair_of = {(r["model"], r["go"]): r for r in flagged}

    errors = []
    covered = set()
    for t in triage:
        if t["verdict"] not in VERDICTS:
            errors.append(f"unknown verdict {t['verdict']} for {t['models']}")
        for m in t["models"]:
            if m not in families:
                errors.append(f"{m}: not in the release table")
                continue
            if m not in hits:
                errors.append(f"{m}: no RefSeq hit count in the release table")
            if t["go"] != "various":
                covered.add((m, t["go"]))
                if t["go"] not in families[m].go_terms:
                    errors.append(f"{m}: does not carry {t['go']}")
                if (m, t["go"]) not in pair_of and t.get("source") != "sweep":
                    errors.append(
                        f"{m} {t['go']}: not a flagged pair and not marked source: sweep"
                    )
            elif t.get("source") == "sweep":
                errors.append(f"{m}: a sweep addition must name its GO term")
            else:
                # "various" dismisses only the model's own flagged pairs, nothing else
                covered.update(k for k in pair_of if k[0] == m)
        if "better" in t and t["verdict"] == "EC_SUSPECT":
            errors.append(
                f"{t['models']}: EC_SUSPECT keeps the term, so takes no better"
            )
        if "better" in t:
            label, deprecated = go_label(go_db, t["better"])
            if label is None or deprecated:
                errors.append(f"better term {t['better']} missing or obsolete")
            t["better_label"] = label
    for r in flagged:
        if (r["model"], r["go"]) not in covered:
            errors.append(f"untriaged {r['placement']} pair {r['model']} {r['go']}")
    if errors:
        sys.exit("triage does not match the data:\n  " + "\n  ".join(errors))

    by_verdict: dict[str, list[dict]] = defaultdict(list)
    for t in triage:
        by_verdict[t["verdict"]].append(t)
    meta = check["meta"]
    lines = [
        "# NCBIfam GO metadata: proposed changes",
        "",
        "Generated by `render_feedback.py` from `release_table_check.yaml` and the "
        "curated `triage.yaml`; do not edit by hand.",
        "",
        f"NCBIfam release {meta['ncbifam_release']}. Each row is a model in "
        "`hmm_PGAP.tsv` whose GO term disagrees with the model's own product name or "
        "EC number. Verdicts are judged from names and GO definitions, not checked "
        "against literature: they are proposals for NCBIfam curators to confirm. "
        "RefSeq hits are the release table's `n_refseq_protein_hits`. `proposed` is a "
        "curator's replacement where one was checked; `GO terms for the model's EC` "
        "lists, unreviewed, the terms that cross-reference the model's own EC numbers. "
        "`no GO term cross-references EC …` means no GO term carries that EC as a "
        "cross-reference; GO often has a term for the reaction all the same, "
        "cross-referenced only to Rhea, as `proposed` shows for adenosine deaminase. "
        "A partial EC would match a whole subclass, so its terms are not listed. A model with several ECs has each EC's "
        "terms labelled. In the EC_SUSPECT section the suspect EC's terms are evidence "
        "for the verdict, not proposals. The RefSeq column is summed over the "
        "distinct models in each verdict; a model in two verdicts counts in both, so the "
        "rows are not additive.",
        "",
        "| verdict | entries | models | RefSeq hits |",
        "|---|---|---|---|",
    ]
    for v in REPORTED + ["ACCEPTABLE"]:
        entries = by_verdict.get(v, [])
        models = {m for t in entries for m in t["models"]}
        lines.append(
            f"| {v} | {len(entries)} | {len(models)} | "
            f"{sum(hits.get(m, 0) for m in models)} |"
        )
    for v in REPORTED:
        entries = sorted(
            by_verdict.get(v, []),
            key=lambda t: -sum(hits.get(m, 0) for m in t["models"]),
        )
        lines.extend(["", f"## {TITLES[v]} ({len(entries)})", ""])
        # in EC_SUSPECT the model's EC is the suspect, so its terms are evidence, not proposals
        ec_column = (
            "GO terms for the (suspect) EC"
            if v == "EC_SUSPECT"
            else "GO terms for the model's EC"
        )
        lines.append(
            f"| model, product name (EC) | GO term | proposed | {ec_column} | note |"
        )
        lines.append("|---|---|---|---|---|")
        for t in entries:
            go = t["go"]
            label = go_label(go_db, go)[0] if go != "various" else ""
            better = f"{t['better']} {t['better_label']}" if "better" in t else "check"
            if v == "EC_SUSPECT":
                better = "keep the term; check the EC"
            # one line per model: grouped models can differ in name, EC and candidates
            models, candidates = [], []
            for m in t["models"]:
                f = families[m]
                models.append(
                    f"{m} {f.product_name} ({', '.join(f.ec_numbers) or 'no EC'})"
                )
                candidates.append(candidate_text(f.ec_numbers, hierarchy, go_db))
            if len(set(candidates)) == 1:
                prefix = "(all models) " if len(candidates) > 1 else ""
                candidates = [prefix + candidates[0]]
            lines.append(
                f"| {'<br>'.join(models)} | {go} {label} | {better} | "
                f"{'<br>'.join(candidates)} | {t['note']} |"
            )
    lines.extend(
        [
            "",
            f"{len(by_verdict.get('ACCEPTABLE', []))} further entries were triaged "
            "`ACCEPTABLE` (bifunctional models, dual-substrate names, partial or "
            "secondary activities, EC reclassifications) and are listed in "
            "`triage.yaml` only.",
        ]
    )
    (HERE / "FEEDBACK.md").write_text("\n".join(lines) + "\n")
    print("wrote FEEDBACK.md", file=sys.stderr)


if __name__ == "__main__":
    main()
