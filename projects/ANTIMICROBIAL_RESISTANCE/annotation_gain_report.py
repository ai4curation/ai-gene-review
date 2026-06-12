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

    uv run python projects/ANTIMICROBIAL_RESISTANCE/annotation_gain_report.py \
        --sssom projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml \
        --uniprot projects/ANTIMICROBIAL_RESISTANCE/data/uniprot_card_xrefs.tsv \
        --out-md projects/ANTIMICROBIAL_RESISTANCE/ANNOTATION_GAIN.md \
        --out-tsv projects/ANTIMICROBIAL_RESISTANCE/data/candidate_new_annotations.tsv
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


def classify_candidate(
    go_id: str, existing: set[str], go_descendants: dict[str, set[str]] | None
) -> str:
    """Classify a proposed GO term against an entry's existing GO annotations.

    Returns one of:

    - ``"already"`` - the entry already has this exact term.
    - ``"redundant"`` - the entry already has a *more specific* (is_a descendant) term, so the
      proposed (more general) term would be a subsumption over-annotation.
    - ``"new"`` - a genuine candidate new annotation.

    ``go_descendants`` maps a GO id to the set of its is_a descendant GO ids (excluding self). If
    ``None``, subsumption is not checked and only exact-match suppression applies.

    >>> desc = {"GO:0034069": {"GO:0047663"}}  # 6'-N-acetyltransferase is_a aminoglycoside N-AT
    >>> classify_candidate("GO:0034069", {"GO:0047663", "GO:0046677"}, desc)
    'redundant'
    >>> classify_candidate("GO:0034069", {"GO:0046677"}, desc)
    'new'
    >>> classify_candidate("GO:0034069", {"GO:0034069"}, desc)
    'already'
    >>> classify_candidate("GO:0043838", {"GO:0016776"}, None)
    'new'
    """
    if go_id in existing:
        return "already"
    if go_descendants and (existing & go_descendants.get(go_id, set())):
        return "redundant"
    return "new"


def build_go_descendant_index(mappings: list[dict], adapter_string: str) -> dict[str, set[str]]:
    """Map each candidate (object) GO id -> the set of its is_a descendant GO ids (excluding self)."""
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    adapter = get_adapter(adapter_string)
    index: dict[str, set[str]] = {}
    for go_id in {m["object_id"] for m in mappings}:
        try:
            index[go_id] = set(adapter.descendants(go_id, predicates=[IS_A])) - {go_id}
        except Exception:
            index[go_id] = set()
    return index


def compute(mappings, subtree, uniprot_rows, go_descendants=None):
    """Yield candidate-new-annotation rows and return aggregate counters.

    ``go_descendants`` (optional): GO id -> is_a descendant set, used to suppress a candidate when
    the entry already carries a more specific term (subsumption-aware filtering).
    """
    # subject -> list of (go_id, go_label, predicate_id)
    by_subject: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for m in mappings:
        by_subject[m["subject_id"]].append((m["object_id"], m.get("object_label", ""), m["predicate_id"]))

    candidate_rows: list[dict] = []
    entries_matched = 0
    entries_gained = set()
    new_by_go: Counter = Counter()
    already_by_go: Counter = Counter()
    redundant_by_go: Counter = Counter()
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
            verdict = classify_candidate(go_id, existing, go_descendants)
            if verdict == "already":
                already_by_go[go_id] += 1
                continue
            if verdict == "redundant":
                redundant_by_go[go_id] += 1
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
        "redundant_by_go": redundant_by_go,
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
        "already present in the entry's UniProt GO annotations (any evidence code) **and** is not subsumed",
        "by a more specific term the entry already has (subsumption-aware filtering).",
        "",
        "Generated by `annotation_gain_report.py` from a UniProt snapshot (see `data/uniprot_card_xrefs.tsv`).",
        "",
        "## Summary",
        "",
        f"- UniProtKB entries with a CARD cross-reference: **{stats['entries_total']:,}**",
        f"- Entries matched by ≥1 mapping (exact or narrower): **{stats['entries_matched']:,}**",
        f"- Entries gaining ≥1 **new** candidate GO annotation: **{stats['entries_gained']:,}**",
        f"- Total candidate new annotations: **{stats['candidates_total']:,}**",
        f"- Suppressed as redundant (entry already has a more specific term): "
        f"**{sum(stats['redundant_by_go'].values()):,}**",
        "",
        "## New candidate annotations by GO term",
        "",
        "| GO term | label | entries gaining (new) | already annotated | suppressed (subsumed) |",
        "|---------|-------|----------------------:|------------------:|----------------------:|",
    ]
    go_ids = set(stats["new_by_go"]) | set(stats["redundant_by_go"]) | set(stats["already_by_go"])
    for go_id in sorted(go_ids, key=lambda g: stats["new_by_go"].get(g, 0), reverse=True):
        lines.append(
            f"| {go_id} | {go_labels.get(go_id, '')} | {stats['new_by_go'].get(go_id, 0):,} | "
            f"{stats['already_by_go'].get(go_id, 0):,} | {stats['redundant_by_go'].get(go_id, 0):,} |"
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
    ap.add_argument("--go-adapter", default="sqlite:obo:go")
    ap.add_argument(
        "--subsumption/--no-subsumption", dest="subsumption", default=True,
        action=argparse.BooleanOptionalAction,
        help="Suppress a candidate when the entry already has a more specific (is_a descendant) GO term",
    )
    args = ap.parse_args(argv)

    mappings = load_go_mappings(args.sssom)
    subtree = build_subtree_index(mappings, args.aro_adapter)
    go_descendants = build_go_descendant_index(mappings, args.go_adapter) if args.subsumption else None
    uniprot_rows = read_uniprot_tsv(args.uniprot)
    candidate_rows, stats = compute(mappings, subtree, uniprot_rows, go_descendants)

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
