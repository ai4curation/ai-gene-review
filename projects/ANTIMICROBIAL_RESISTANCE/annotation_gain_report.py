#!/usr/bin/env python3
"""Report the candidate GO annotations UniProt would gain from the ARO->GO mappings.

For every UniProtKB entry that carries a CARD cross-reference (``DR CARD`` -> an ARO id), apply the
curated ARO->GO mappings (propagated along ARO ``is_a`` and ``participates_in``) and compare the proposed GO terms to
the entry's existing GO annotations. A proposed term that is not already annotated is a *candidate new
annotation* (a lead for a curator, not an automatic assertion).

Input: a TSV snapshot of UniProt CARD-cross-referenced entries
(``data/uniprot_card_xrefs.tsv``; columns Entry / CARD / Gene Ontology IDs), refreshable from the
UniProt REST API. The ARO release comes from ``.cache/aro/aro.obo`` (``just fetch-aro``); a
mapping applies along ARO ``is_a`` (gene families) and along ``participates_in`` (mechanism
terms), see ``aro_release.applicable_subjects``.

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

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import typer
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aro_release import DEFAULT_CACHE, MINI_OBO, AroOntology, applicable_subjects  # noqa: E402,F401

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
    """Map each candidate (object) GO id -> the set of its is_a descendant GO ids (excluding self).

    Only is_a is followed. For a BP candidate a part_of child would also subsume it; that does not
    arise for the current rows (the one BP target, GO:0046677, is suppressed by its is_a children).
    """
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    adapter = get_adapter(adapter_string)
    index: dict[str, set[str]] = {}
    for go_id in {m["object_id"] for m in mappings}:
        index[go_id] = set(adapter.descendants(go_id, predicates=[IS_A])) - {go_id}
    return index


RESISTANCE_VARIANT = "ARO:0000031"  # antibiotic resistance gene variant or mutant


def propose(onto: AroOntology, aros: list[str], by_subject: dict[str, list[tuple[str, str, str]]]):
    """Return ``go_id -> (mapped_subject, relation, predicate, go_label, gene_aro)`` for one entry.

    ``gene_aro`` is the entry's own ARO term (one of ``aros``) that produced the proposal.

    Relations follow :func:`aro_release.applicable_subjects`; when several mapped subjects
    give the same GO term the most specific provenance wins (exact > narrower > participates_in).

    >>> aro = AroOntology.from_obo_text(MINI_OBO)
    >>> by_subject = {"ARO:2": [("GO:0008800", "beta-lactamase activity", "RO:0002327")],
    ...               "ARO:10": [("GO:0046677", "response to antibiotic", "skos:relatedMatch")]}
    >>> sorted((g, v[1], v[4]) for g, v in propose(aro, ["ARO:4"], by_subject).items())
    [('GO:0008800', 'narrower', 'ARO:4'), ('GO:0046677', 'participates_in', 'ARO:4')]
    """
    rank = {"exact": 0, "narrower": 1, "participates_in": 2}
    proposed: dict[str, tuple[str, str, str, str, str]] = {}
    for aro in aros:
        for subj, relation in applicable_subjects(onto, aro).items():
            for go_id, go_label, pred in by_subject.get(subj, []):
                if go_id not in proposed or rank[relation] < rank[proposed[go_id][1]]:
                    proposed[go_id] = (subj, relation, pred, go_label, aro)
    return proposed


def compute(mappings, onto: AroOntology, uniprot_rows, go_descendants=None):
    """Return candidate-new-annotation rows and aggregate counters.

    ``go_descendants`` (optional): GO id -> is_a descendant set, used to suppress a candidate when
    the entry already carries a more specific term (subsumption-aware filtering).
    """
    by_subject: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for m in mappings:
        by_subject[m["subject_id"]].append((m["object_id"], m.get("object_label", ""), m["predicate_id"]))

    candidate_rows: list[dict] = []
    entries_matched = 0
    entries_gained = set()
    matched_by_go: Counter = Counter()
    new_by_go: Counter = Counter()
    already_by_go: Counter = Counter()
    redundant_by_go: Counter = Counter()
    new_by_family: Counter = Counter()
    matched_by_subject: Counter = Counter()
    matched_by_relation: Counter = Counter()
    by_row: Counter = Counter()  # (subject, go_id, verdict) -> n; verdict in matched/new/already/redundant

    for acc, aros, existing in uniprot_rows:
        proposed = propose(onto, aros, by_subject)
        if proposed:
            entries_matched += 1
        for go_id, (subj, relation, pred, go_label, gene_aro) in proposed.items():
            matched_by_go[go_id] += 1
            matched_by_subject[subj] += 1
            matched_by_relation[relation] += 1
            verdict = classify_candidate(go_id, existing, go_descendants)
            by_row[(subj, go_id, "matched")] += 1
            by_row[(subj, go_id, verdict)] += 1
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
                    "gene_aro_id": gene_aro,
                    # is_a only: False means "not an is_a descendant of ARO:0000031", not a proven negative
                    "gene_is_resistance_variant": RESISTANCE_VARIANT in onto.isa_ancestors_or_self(gene_aro),
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
        "matched_by_go": matched_by_go,
        "new_by_go": new_by_go,
        "already_by_go": already_by_go,
        "redundant_by_go": redundant_by_go,
        "new_by_family": new_by_family,
        "matched_by_subject": matched_by_subject,
        "matched_by_relation": matched_by_relation,
        "by_row": by_row,
    }
    return candidate_rows, stats


def write_row_stats(path: Path, mappings: list[dict], by_row: Counter) -> None:
    """Write one line per GO mapping row: how many entries it matched and what became of them.

    A row credited with 0 proposals either reaches no CARD-cross-referenced entry, or every entry it
    reaches gets the same GO term from a more specific mapped ARO term.
    """
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["subject_id", "object_id", "matched", "new", "already", "redundant"])
        for m in mappings:
            key = (m["subject_id"], m["object_id"])
            w.writerow([*key, *(by_row[(*key, v)] for v in ("matched", "new", "already", "redundant"))])


def go_label_lookup(mappings: list[dict]) -> dict[str, str]:
    return {m["object_id"]: m.get("object_label", "") for m in mappings}


def aro_label_lookup(mappings: list[dict]) -> dict[str, str]:
    return {m["subject_id"]: m.get("subject_label", "") for m in mappings}


def render_md(stats, mappings, release_label: str) -> str:
    go_labels = go_label_lookup(mappings)
    aro_labels = aro_label_lookup(mappings)
    rel = stats["matched_by_relation"]
    lines = [
        "---",
        'title: "Annotation-gain report: applying the ARO→GO mappings to UniProt"',
        "---",
        "",
        "# Annotation-gain report: applying the ARO→GO mappings to UniProt",
        "",
        "Candidate GO annotations that UniProtKB entries with a CARD cross-reference would gain from the",
        "curated [`aro2go.sssom.yaml`](aro2go.sssom.yaml) mappings. These are **leads for a curator, not",
        "automatic assertions**. \"New\" = the proposed GO term is not already present in the entry's UniProt",
        "GO annotations (any evidence code) **and** is not subsumed by a more specific term the entry",
        "already has (subsumption-aware filtering).",
        "",
        f"Generated by `annotation_gain_report.py` against **{release_label}** from a UniProt snapshot",
        "(see `data/uniprot_card_xrefs.tsv`). A mapping on a gene-family term reaches the entry along ARO",
        "`is_a` (`exact` / `narrower`); a mapping on a resistance-mechanism term reaches it along",
        "`is_a* ∘ participates_in ∘ is_a*` (`participates_in`), the relation ARO uses to join gene",
        "families to mechanisms.",
        "",
        "## Summary",
        "",
        f"- UniProtKB entries with a CARD cross-reference: **{stats['entries_total']:,}**",
        f"- Entries matched by ≥1 mapping: **{stats['entries_matched']:,}**",
        f"- (entry, GO term) proposals by relation: exact **{rel['exact']:,}**, narrower "
        f"**{rel['narrower']:,}**, participates_in **{rel['participates_in']:,}**",
        f"- Entries gaining ≥1 **new** candidate GO annotation: **{stats['entries_gained']:,}**",
        f"- Total candidate new annotations: **{stats['candidates_total']:,}**",
        f"- Suppressed as redundant (entry already has a more specific term): "
        f"**{sum(stats['redundant_by_go'].values()):,}**",
        "",
        "## Candidate annotations by GO term",
        "",
        "| GO term | label | entries matched | new | already annotated | suppressed (subsumed) |",
        "|---------|-------|----------------:|----:|------------------:|----------------------:|",
    ]
    for go_id in sorted(stats["matched_by_go"], key=lambda g: (-stats["new_by_go"].get(g, 0), -stats["matched_by_go"][g], g)):
        lines.append(
            f"| {go_id} | {go_labels.get(go_id, '')} | {stats['matched_by_go'][go_id]:,} | "
            f"{stats['new_by_go'].get(go_id, 0):,} | {stats['already_by_go'].get(go_id, 0):,} | "
            f"{stats['redundant_by_go'].get(go_id, 0):,} |"
        )
    lines += [
        "",
        "## By mapped ARO term",
        "",
        "Each (entry, GO term) proposal is credited to the most specific mapped ARO term that gave it.",
        "",
        "| mapped ARO | label | proposals | new annotations |",
        "|------------|-------|----------:|----------------:|",
    ]
    for subj, n in sorted(stats["matched_by_subject"].items(), key=lambda kv: (-stats["new_by_family"].get(kv[0], 0), -kv[1], kv[0])):
        lines.append(f"| {subj} | {aro_labels.get(subj, '')} | {n:,} | {stats['new_by_family'].get(subj, 0):,} |")
    lines.append("")
    return "\n".join(lines)


def main(
    sssom: Path = typer.Option(..., help="ARO->GO SSSOM mapping file"),
    uniprot: Path = typer.Option(..., help="UniProt CARD-xref TSV snapshot"),
    out_md: Path = typer.Option(...),
    out_tsv: Path = typer.Option(...),
    out_stats: Path = typer.Option(
        None, help="Per-mapping-row counts (matched/new/already/redundant) TSV, read by render_sssom_html.py"
    ),
    aro_cache: Path = typer.Option(DEFAULT_CACHE, help="Fetched CARD release (just fetch-aro)"),
    go_adapter: str = typer.Option("sqlite:obo:go"),
    subsumption: bool = typer.Option(
        True, help="Suppress a candidate when the entry already has a more specific (is_a descendant) GO term"
    ),
) -> None:
    """Report the candidate GO annotations UniProt would gain from the ARO->GO mappings."""
    from aro_release import Release

    release = Release(aro_cache)
    release.require()
    meta = release.metadata
    onto = AroOntology.from_obo(release.obo)
    mappings = load_go_mappings(sssom)
    go_descendants = build_go_descendant_index(mappings, go_adapter) if subsumption else None
    uniprot_rows = read_uniprot_tsv(uniprot)
    candidate_rows, stats = compute(mappings, onto, uniprot_rows, go_descendants)

    out_tsv.parent.mkdir(parents=True, exist_ok=True)
    # New columns go at the end: gene reviews quote whole rows of this file as supporting_text.
    cols = [
        "uniprot_acc", "gene_aro_id", "mapped_aro_id", "aro_relation", "predicate_id", "go_id", "go_label",
        "gene_is_resistance_variant",
    ]
    with out_tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(sorted(candidate_rows, key=lambda r: (r["go_id"], r["uniprot_acc"])))

    if out_stats:
        write_row_stats(out_stats, mappings, stats["by_row"])
    release_label = f"CARD {meta['card_version']} (ARO {meta['aro_date']})"
    out_md.write_text(render_md(stats, mappings, release_label) + "\n")
    typer.echo(
        f"# {stats['entries_total']} entries; {stats['entries_matched']} matched; "
        f"{stats['entries_gained']} gain >=1 new; {stats['candidates_total']} candidate annotations."
    )


if __name__ == "__main__":
    typer.run(main)
