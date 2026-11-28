"""Run inputs and scoring for benchmark conditions.

``export`` writes generic inputs that any predictor can use:

* ``<id>.fasta``: UniProt-style headers, so a predictor (or its runner) can
  withhold the header (BLIND), keep only OS=/OX= (ORGANISM) or show it all
  (FULL);
* ``<id>-claims.yaml``: a ClaimSet, one claim per target, NOT target and decoy,
  without its role;
* ``baseline-goa/<ACC>-goa.tsv``: the protein's baseline-release annotations
  in the repository's GENE-goa.tsv layout, to seed an ai-gene-review review
  (the AGENT_REVIEW condition) without the post-cutoff rows it is tested on.

``score`` tallies generic Prediction records (``benchmark.predictions``) per
condition, predictor, query role and item. Native predictor outputs are
converted by ``benchmark.importers`` first.
"""

from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.benchmark.checks import Context
from ai_gene_review.benchmark.predictions import (
    SHUFFLED,
    Verdicts,
    claims,
    fasta_id,
    queries,
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
    """Write the FASTA, ClaimSet and baseline GOA files.

    Returns the paths written and the ids of items skipped for lack of a
    pinned sequence (they will score as missing).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    taxon = benchmark["spec"]["taxon"]
    items = [i for i in benchmark["items"] if i.get("sequence")]
    skipped = [i["id"] for i in benchmark["items"] if not i.get("sequence")]
    fasta = out_dir / f"{benchmark['id']}.fasta"
    fasta.write_text("".join(fasta_record(i, taxon) for i in items))
    claims_path = out_dir / f"{benchmark['id']}-claims.yaml"
    claims_path.write_text(
        yaml.safe_dump(
            {"benchmark_id": benchmark["id"], "claims": claims(items)},
            sort_keys=False,
            allow_unicode=True,
            width=100,
        )
    )
    written = [fasta, claims_path]
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


def score(benchmark: dict, verdicts: Verdicts, inputs: list[str]) -> dict[str, Any]:
    """ScoreReport dict from verdicts keyed (condition, predictor, item, term)."""
    runs = sorted({(c, p) for c, p, _, _ in verdicts})
    overall: dict[tuple[str, str, str], Counter] = {}
    per_item: list[dict] = []
    for condition, predictor in runs:
        shuffled_asked = any(
            c == condition and p == predictor and t.startswith(SHUFFLED)
            for c, p, _, t in verdicts
        )
        for item in benchmark["items"]:
            asked = list(queries(item))
            if shuffled_asked:
                asked += [
                    (SHUFFLED + t, label, "SHUFFLED_TARGET")
                    for t, label, role in asked
                    if role == "TARGET"
                ]
            item_counts: dict[str, Counter] = {}
            for term, _, role in asked:
                verdict = verdicts.get(
                    (condition, predictor, item["id"], term), "missing"
                )
                item_counts.setdefault(role, Counter())[verdict] += 1
                overall.setdefault((condition, predictor, role), Counter())[
                    verdict
                ] += 1
            for role, counts in sorted(item_counts.items()):
                per_item.append(
                    score_row(condition, predictor, role, counts, item["id"])
                )
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
    condition: str,
    predictor: str,
    role: str,
    counts: Counter,
    item_id: str | None = None,
) -> dict:
    """ConditionScore dict.

    >>> score_row("blind", "p", "TARGET", Counter(yes=2, missing=1))
    {'condition': 'blind', 'predictor': 'p', 'role': 'TARGET', 'n': 3, 'n_yes': 2, 'n_no': 0, 'n_uncertain': 0, 'n_missing': 1}
    """
    row: dict[str, Any] = {"condition": condition, "predictor": predictor}
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


def score_markdown(report: dict) -> str:
    """Condition-by-predictor-by-role table of a ScoreReport."""
    lines = [
        f"# Scores: {report['benchmark_id']}",
        "",
        "| condition | predictor | role | n | yes | no | uncertain | missing |",
        "|---|---|---|---|---|---|---|---|",
    ]
    lines += [
        f"| {r['condition']} | {r['predictor']} | {r['role']} | {r['n']} | {r['n_yes']} | {r['n_no']} | "
        f"{r['n_uncertain']} | {r['n_missing']} |"
        for r in report["condition_scores"]
    ]
    return "\n".join(lines) + "\n"
