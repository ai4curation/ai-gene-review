"""Run inputs and scoring for benchmark conditions.

``export`` writes what each condition needs:

* ``<id>.fasta``: UniProt-style headers, so ``peptalk --context blind`` sends
  the sequence alone, ``organism`` adds OS=/OX=, and ``full`` adds the
  accession and name;
* ``<id>-claims.tsv``: one ``ask-function`` claim per target, NOT target and
  decoy, for ``peptalk ask``;
* ``baseline-goa/<ACC>-goa.tsv``: the protein's baseline-release annotations
  in the repository's GENE-goa.tsv layout, to seed an ai-gene-review review
  (the AGENT_REVIEW condition) without the post-cutoff rows it is tested on.

``score`` tallies verdicts per condition, query role and item from peptalk
JSONL records and from ai-gene-review reviews.
"""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Iterable, Iterator
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.benchmark.checks import (
    REVIEW_CONTESTS,
    REVIEW_KEEPS,
    Context,
    find_review,
)
from ai_gene_review.benchmark.sources import Annotation

GOA_COLUMNS = (
    "GENE PRODUCT DB",
    "GENE PRODUCT ID",
    "SYMBOL",
    "QUALIFIER",
    "GO TERM",
    "GO NAME",
    "GO ASPECT",
    "ECO ID",
    "GO EVIDENCE CODE",
    "REFERENCE",
    "WITH/FROM",
    "TAXON ID",
    "TAXON NAME",
    "ASSIGNED BY",
    "GENE NAME",
    "DATE",
)
ASPECT_NAMES = {
    "F": "molecular_function",
    "P": "biological_process",
    "C": "cellular_component",
}
CLAIM_COLUMNS = ("id", "task", "term", "label", "position", "residue")
VERDICTS = ("yes", "no", "uncertain")


def fasta_id(item: dict) -> str:
    """UniProt-style FASTA id for an item.

    >>> fasta_id({"protein": "UniProtKB:P00533", "entry_name": "EGFR_HUMAN"})
    'sp|P00533|EGFR_HUMAN'
    """
    return f"sp|{item['protein'].split(':', 1)[1]}|{item['entry_name']}"


def fasta_record(item: dict, taxon: dict) -> str:
    """FASTA record with a UniProt-style header.

    >>> item = {"protein": "UniProtKB:P1", "entry_name": "X_HUMAN", "protein_name": "Kinase X",
    ...         "gene_symbol": "X", "sequence_version": 2, "sequence": "MKV"}
    >>> print(fasta_record(item, {"id": "NCBITaxon:9606", "label": "Homo sapiens"}), end="")
    >sp|P1|X_HUMAN Kinase X OS=Homo sapiens OX=9606 GN=X SV=2
    MKV
    """
    header = (
        f">{fasta_id(item)} {item.get('protein_name', '')} OS={taxon.get('label', '')} "
        f"OX={taxon['id'].split(':', 1)[1]} GN={item.get('gene_symbol', '')} SV={item['sequence_version']}"
    )
    sequence = item["sequence"]
    lines = [sequence[i : i + 60] for i in range(0, len(sequence), 60)]
    return header + "\n" + "\n".join(lines) + "\n"


def queries(item: dict) -> Iterator[tuple[str, str, str]]:
    """(term id, label, role) for every term asked about an item."""
    for target in item["target_annotations"]:
        role = "NEGATED_TARGET" if target.get("negated") else "TARGET"
        yield target["term"]["id"], target["term"].get("label") or "", role
    for decoy in item.get("decoys") or []:
        yield decoy["term"]["id"], decoy["term"].get("label") or "", "DECOY"


def claims_rows(items: Iterable[dict]) -> list[str]:
    """peptalk ``ask`` claims TSV lines (header first), one per distinct term per item."""
    rows = ["\t".join(CLAIM_COLUMNS)]
    for item in items:
        for term in dict.fromkeys((term, label) for term, label, _ in queries(item)):
            rows.append(
                "\t".join((fasta_id(item), "ask-function", term[0], term[1], "", ""))
            )
    return rows


def goa_row(a: Annotation, ctx: Context, taxon: dict) -> str:
    """A baseline annotation in the GENE-goa.tsv layout (no ECO id: GAF rows carry none)."""
    qualifier = ("NOT|" if a.negated else "") + a.qualifier
    db, acc = a.protein.split(":", 1)
    return "\t".join(
        (
            db,
            acc,
            a.symbol,
            qualifier,
            a.term,
            ctx.ontology.label(a.term) or "",
            ASPECT_NAMES.get(a.aspect, a.aspect),
            "",
            a.evidence,
            a.reference,
            a.with_from,
            taxon["id"].split(":", 1)[1],
            taxon.get("label", ""),
            a.assigned_by,
            a.name,
            a.date,
        )
    )


def export(
    benchmark: dict, ctx: Context, out_dir: Path
) -> tuple[list[Path], list[str]]:
    """Write the FASTA, claims TSV and baseline GOA files.

    Returns the paths written and the ids of items skipped for lack of a
    pinned sequence (they will score as missing).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    taxon = benchmark["spec"]["taxon"]
    items = [i for i in benchmark["items"] if i.get("sequence")]
    skipped = [i["id"] for i in benchmark["items"] if not i.get("sequence")]
    fasta = out_dir / f"{benchmark['id']}.fasta"
    fasta.write_text("".join(fasta_record(i, taxon) for i in items))
    claims = out_dir / f"{benchmark['id']}-claims.tsv"
    claims.write_text("\n".join(claims_rows(items)) + "\n")
    written = [fasta, claims]
    goa_dir = out_dir / "baseline-goa"
    goa_dir.mkdir(exist_ok=True)
    for item in items:
        rows = ctx.baseline.get(item["protein"], [])
        path = goa_dir / f"{item['protein'].split(':', 1)[1]}-goa.tsv"
        path.write_text(
            "\n".join(["\t".join(GOA_COLUMNS)] + [goa_row(a, ctx, taxon) for a in rows])
            + "\n"
        )
        written.append(path)
    return written, skipped


def condition_name(conditions: list[dict], context: str, model: str | None) -> str:
    """Spec condition matching a peptalk context and model, else ``context:model``.

    >>> conds = [{"name": "blind-fable", "context": "BLIND", "model": "claude-fable-5-2"}]
    >>> condition_name(conds, "blind", "claude-fable-5-2"), condition_name(conds, "full", "m")
    ('blind-fable', 'full:m')
    """
    for condition in conditions:
        if condition["context"] == context.upper() and condition.get("model") in (
            None,
            model,
        ):
            return condition["name"]
    return f"{context}:{model}"


Verdicts = dict[
    tuple[str, str, str, str], str
]  # (condition, model, item_id, term or SHUFFLED|term) -> verdict


def peptalk_verdicts(benchmark: dict, records: Iterable[dict]) -> Verdicts:
    """Verdicts from peptalk ``ask`` JSONL records (shuffled-control records keyed with a SHUFFLED| prefix)."""
    by_fasta = {fasta_id(i): i["id"] for i in benchmark["items"] if i.get("entry_name")}
    conditions = benchmark["spec"].get("conditions") or []
    verdicts: Verdicts = {}
    for record in records:
        item_id = by_fasta.get(record.get("id", ""))
        term = (record.get("params") or {}).get("term")
        if item_id is None or term is None or record.get("task") != "ask-function":
            continue
        name = condition_name(
            conditions, record.get("context", ""), record.get("model")
        )
        key_term = (
            term if record.get("condition", "real") == "real" else f"SHUFFLED|{term}"
        )
        verdict = (record.get("answer") or {}).get("verdict")
        verdicts[(name, record.get("model") or "", item_id, key_term)] = (
            verdict if verdict in VERDICTS else "missing"
        )
    return verdicts


CORE_FUNCTION_SLOTS = (
    "molecular_function",
    "contributes_to_molecular_function",
    "directly_involved_in",
    "locations",
    "in_complex",
)


def review_claims(review: dict) -> tuple[set[str], set[str]]:
    """Terms a review asserts (kept rows, MODIFY rows and their replacements, core functions) and contests.

    >>> kept, contested = review_claims({
    ...     "existing_annotations": [
    ...         {"term": {"id": "GO:1"}, "review": {"action": "MODIFY",
    ...          "proposed_replacement_terms": [{"id": "GO:2"}]}},
    ...         {"term": {"id": "GO:3"}, "review": {"action": "REMOVE"}}],
    ...     "core_functions": [{"in_complex": {"id": "GO:4"}}]})
    >>> sorted(kept), sorted(contested)
    (['GO:1', 'GO:2', 'GO:4'], ['GO:3'])
    """
    kept: set[str] = set()
    contested: set[str] = set()
    for row in review.get("existing_annotations") or []:
        decision = row.get("review") or {}
        action = decision.get("action")
        term = (row.get("term") or {}).get("id")
        if not term or row.get("negated"):
            continue
        if action in REVIEW_KEEPS or action == "MODIFY":
            kept.add(term)
            kept |= {
                t["id"]
                for t in decision.get("proposed_replacement_terms") or []
                if t.get("id", "").startswith("GO:")
            }
        elif action in REVIEW_CONTESTS:
            contested.add(term)
    for core in review.get("core_functions") or []:
        for slot in CORE_FUNCTION_SLOTS:
            values = core.get(slot) or []
            for value in values if isinstance(values, list) else [values]:
                if isinstance(value, dict) and value.get("id"):
                    kept.add(value["id"])
    return kept, contested - kept


def review_verdicts(
    benchmark: dict, ctx: Context, genes_dir: Path, condition: str
) -> Verdicts:
    """Verdicts from ai-gene-review reviews on targets and NOT targets.

    A term is "yes" when an asserted term entails it, "no" when the review
    contests a row to it or asserts nothing that entails it. Decoys are
    recorded as "missing": a review is not asked about them, so its silence
    is not a measured "no" comparable with the peptalk conditions.
    """
    verdicts: Verdicts = {}
    for item in benchmark["items"]:
        path = find_review(
            genes_dir, item.get("gene_symbol"), item["protein"].split(":", 1)[1]
        )
        if path is None:
            continue
        kept, contested = review_claims(yaml.safe_load(path.read_text()))
        for term, _, role in queries(item):
            if role == "DECOY":
                verdict = "missing"
            elif term in contested:
                verdict = "no"
            elif any(
                term in ctx.ontology.ancestors(ctx.ontology.resolve(k)) for k in kept
            ):
                verdict = "yes"
            else:
                verdict = "no"
            verdicts[(condition, "", item["id"], term)] = verdict
    return verdicts


def score(benchmark: dict, verdicts: Verdicts, inputs: list[str]) -> dict[str, Any]:
    """ScoreReport dict from verdicts."""
    runs = sorted({(c, m) for c, m, _, _ in verdicts})
    overall: dict[tuple[str, str, str], Counter] = {}
    per_item: list[dict] = []
    for condition, model in runs:
        shuffled_asked = any(
            c == condition and m == model and t.startswith("SHUFFLED|")
            for c, m, _, t in verdicts
        )
        for item in benchmark["items"]:
            asked = list(queries(item))
            if shuffled_asked:
                asked += [
                    (f"SHUFFLED|{t}", label, "SHUFFLED_TARGET")
                    for t, label, role in asked
                    if role == "TARGET"
                ]
            item_counts: dict[str, Counter] = {}
            for term, _, role in asked:
                verdict = verdicts.get((condition, model, item["id"], term), "missing")
                item_counts.setdefault(role, Counter())[verdict] += 1
                overall.setdefault((condition, model, role), Counter())[verdict] += 1
            for role, counts in sorted(item_counts.items()):
                per_item.append(score_row(condition, model, role, counts, item["id"]))
    return {
        "benchmark_id": benchmark["id"],
        "generated": date.today().isoformat(),
        "inputs": inputs,
        "condition_scores": [
            score_row(c, m, r, counts) for (c, m, r), counts in sorted(overall.items())
        ],
        "item_scores": per_item,
    }


def score_row(
    condition: str, model: str, role: str, counts: Counter, item_id: str | None = None
) -> dict:
    """ConditionScore dict.

    >>> score_row("blind", "m", "TARGET", Counter(yes=2, missing=1))
    {'condition': 'blind', 'model': 'm', 'role': 'TARGET', 'n': 3, 'n_yes': 2, 'n_no': 0, 'n_uncertain': 0, 'n_missing': 1}
    """
    row: dict[str, Any] = {"condition": condition}
    if model:
        row["model"] = model
    if item_id:
        row["item_id"] = item_id
    row.update(
        {
            "role": role,
            "n": sum(counts.values()),
            "n_yes": counts["yes"],
            "n_no": counts["no"],
            "n_uncertain": counts["uncertain"],
            "n_missing": counts["missing"],
        }
    )
    return row


def read_jsonl(paths: Iterable[Path]) -> Iterator[dict]:
    """JSON objects from JSONL files, skipping non-JSON lines (peptalk prints a TSV summary too)."""
    for path in paths:
        for line in path.read_text().splitlines():
            if line.startswith("{"):
                yield json.loads(line)


def score_markdown(report: dict) -> str:
    """Condition-by-role table of a ScoreReport."""
    lines = [
        f"# Scores: {report['benchmark_id']}",
        "",
        "| condition | model | role | n | yes | no | uncertain | missing |",
        "|---|---|---|---|---|---|---|---|",
    ]
    lines += [
        f"| {r['condition']} | {r.get('model', '')} | {r['role']} | {r['n']} | {r['n_yes']} | {r['n_no']} | "
        f"{r['n_uncertain']} | {r['n_missing']} |"
        for r in report["condition_scores"]
    ]
    return "\n".join(lines) + "\n"
