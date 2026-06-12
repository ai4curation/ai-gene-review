#!/usr/bin/env python3
"""Report the candidate GO annotations UniProt would gain from the ARO->GO mappings.

For every UniProtKB entry that carries a CARD cross-reference (``DR CARD`` -> an ARO id), apply the
curated ARO->GO mappings with **exact-or-narrower** propagation and compare the proposed GO terms to
the entry's existing GO annotations. A proposed term that is not already annotated is a *candidate new
annotation* (a lead for a curator, not an automatic assertion).

Input: a TSV snapshot of UniProt CARD-cross-referenced entries
(``data/uniprot_card_xrefs.tsv``; columns Entry / CARD / Gene Ontology IDs), refreshable from the
UniProt REST API. ARO hierarchy comes from OAK ``sqlite:obo:aro``.

Outputs:
- ``ANNOTATION_GAIN.md`` - human-readable summary.
- ``data/candidate_new_annotations.tsv`` - one row per (entry, candidate GO term).

Usage::

    uv run python projects/mappings/annotation_gain_report.py \
        --sssom projects/mappings/aro2go.sssom.yaml \
        --uniprot projects/mappings/data/uniprot_card_xrefs.tsv \
        --out-md projects/mappings/ANNOTATION_GAIN.md \
        --out-tsv projects/mappings/data/candidate_new_annotations.tsv
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ARO_RE = re.compile(r"ARO:\d+")
GO_RE = re.compile(r"GO:\d+")
UNIPROT_STREAM = (
    "https://rest.uniprot.org/uniprotkb/stream?"
    "query=%28database%3Acard%29&fields=accession,xref_card,go_id&format=tsv"
)


def load_go_mappings(sssom_path: Path) -> list[dict]:
    """Return the GO mappings (skipping sssom:NoTermFound gap rows)."""
    doc = yaml.safe_load(sssom_path.read_text())
    return [m for m in doc.get("mappings", []) if str(m.get("object_id", "")).startswith("GO:")]


def build_subtree_index(mappings: list[dict], adapter_string: str) -> dict[str, set[str]]:
    """Map each mapped ARO subject -> the set of ARO terms in its is_a subtree (incl. self)."""
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    adapter = get_adapter(adapter_string)
    subtree: dict[str, set[str]] = {}
    for subj in {m["subject_id"] for m in mappings}:
        try:
            desc = set(adapter.descendants(subj, predicates=[IS_A]))
        except Exception:
            desc = set()
        subtree[subj] = desc | {subj}
    return subtree


def read_uniprot_tsv(path: Path) -> list[tuple[str, list[str], set[str]]]:
    """Parse (accession, [ARO ids], {existing GO ids}) from the UniProt snapshot TSV."""
    rows: list[tuple[str, list[str], set[str]]] = []
    with path.open() as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("Entry\t"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            acc = parts[0].strip()
            aros = ARO_RE.findall(parts[1])
            existing = set(GO_RE.findall(parts[2])) if len(parts) > 2 else set()
            if acc and aros:
                rows.append((acc, aros, existing))
    return rows


def compute(mappings, subtree, uniprot_rows):
    """Yield candidate-new-annotation rows and return aggregate counters."""
    # subject -> list of (go_id, go_label, predicate_id)
    by_subject: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for m in mappings:
        by_subject[m["subject_id"]].append((m["object_id"], m.get("object_label", ""), m["predicate_id"]))

    candidate_rows: list[dict] = []
    entries_matched = 0
    entries_gained = set()
    new_by_go: Counter = Counter()
    already_by_go: Counter = Counter()
    new_by_family: Counter = Counter()

    for acc, aros, existing in uniprot_rows:
        entry_aro = aros[0]  # the determinant ARO (first CARD xref)
        matched = False
        # proposed: go_id -> (mapped_subject, relation, predicate, go_label)
        proposed: dict[str, tuple[str, str, str, str]] = {}
        for subj, members in subtree.items():
            if not any(a in members for a in aros):
                continue
            matched = True
            relation = "exact" if subj in aros else "narrower"
            for go_id, go_label, pred in by_subject[subj]:
                # keep the most specific provenance: prefer exact over narrower
                if go_id not in proposed or (relation == "exact" and proposed[go_id][1] == "narrower"):
                    proposed[go_id] = (subj, relation, pred, go_label)
        if matched:
            entries_matched += 1
        for go_id, (subj, relation, pred, go_label) in proposed.items():
            if go_id in existing:
                already_by_go[go_id] += 1
                continue
            entries_gained.add(acc)
            new_by_go[go_id] += 1
            new_by_family[subj] += 1
            candidate_rows.append(
                {
                    "uniprot_acc": acc,
                    "gene_aro_id": entry_aro,
                    "mapped_aro_id": subj,
                    "aro_relation": relation,
                    "predicate_id": pred,
                    "go_id": go_id,
                    "go_label": go_label,
                }
            )
    stats = {
        "entries_total": len(uniprot_rows),
        "entries_matched": entries_matched,
        "entries_gained": len(entries_gained),
        "candidates_total": len(candidate_rows),
        "new_by_go": new_by_go,
        "already_by_go": already_by_go,
        "new_by_family": new_by_family,
    }
    return candidate_rows, stats


def go_label_lookup(mappings: list[dict]) -> dict[str, str]:
    return {m["object_id"]: m.get("object_label", "") for m in mappings}


def aro_label_lookup(mappings: list[dict]) -> dict[str, str]:
    return {m["subject_id"]: m.get("subject_label", "") for m in mappings}


def render_md(stats, mappings) -> str:
    go_labels = go_label_lookup(mappings)
    aro_labels = aro_label_lookup(mappings)
    lines = [
        "# Annotation-gain report: applying the ARO→GO mappings to UniProt",
        "",
        "Candidate GO annotations that UniProtKB entries with a CARD cross-reference would gain from the",
        "curated [`aro2go.sssom.yaml`](aro2go.sssom.yaml) mappings (exact-or-narrower propagation). These",
        "are **leads for a curator, not automatic assertions**. \"New\" = the proposed GO term is not",
        "already present in the entry's UniProt GO annotations (any evidence code).",
        "",
        "Generated by `annotation_gain_report.py` from a UniProt snapshot (see `data/uniprot_card_xrefs.tsv`).",
        "",
        "## Summary",
        "",
        f"- UniProtKB entries with a CARD cross-reference: **{stats['entries_total']:,}**",
        f"- Entries matched by ≥1 mapping (exact or narrower): **{stats['entries_matched']:,}**",
        f"- Entries gaining ≥1 **new** candidate GO annotation: **{stats['entries_gained']:,}**",
        f"- Total candidate new annotations: **{stats['candidates_total']:,}**",
        "",
        "## New candidate annotations by GO term",
        "",
        "| GO term | label | entries gaining (new) | entries already annotated |",
        "|---------|-------|----------------------:|--------------------------:|",
    ]
    for go_id, n in stats["new_by_go"].most_common():
        lines.append(
            f"| {go_id} | {go_labels.get(go_id, '')} | {n:,} | {stats['already_by_go'].get(go_id, 0):,} |"
        )
    lines += [
        "",
        "## New candidate annotations by mapped ARO family/term",
        "",
        "| mapped ARO | label | new annotations |",
        "|------------|-------|----------------:|",
    ]
    for subj, n in stats["new_by_family"].most_common():
        lines.append(f"| {subj} | {aro_labels.get(subj, '')} | {n:,} |")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sssom", type=Path, required=True)
    ap.add_argument("--uniprot", type=Path, required=True, help="UniProt CARD-xref TSV snapshot")
    ap.add_argument("--aro-adapter", default="sqlite:obo:aro")
    ap.add_argument("--out-md", type=Path, required=True)
    ap.add_argument("--out-tsv", type=Path, required=True)
    args = ap.parse_args(argv)

    mappings = load_go_mappings(args.sssom)
    subtree = build_subtree_index(mappings, args.aro_adapter)
    uniprot_rows = read_uniprot_tsv(args.uniprot)
    candidate_rows, stats = compute(mappings, subtree, uniprot_rows)

    args.out_tsv.parent.mkdir(parents=True, exist_ok=True)
    cols = ["uniprot_acc", "gene_aro_id", "mapped_aro_id", "aro_relation", "predicate_id", "go_id", "go_label"]
    with args.out_tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(sorted(candidate_rows, key=lambda r: (r["go_id"], r["uniprot_acc"])))

    args.out_md.write_text(render_md(stats, mappings) + "\n")
    print(
        f"# {stats['entries_total']} entries; {stats['entries_matched']} matched; "
        f"{stats['entries_gained']} gain ≥1 new; {stats['candidates_total']} candidate annotations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
