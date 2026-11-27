"""Reconcile OpenScientist adjudication verdicts with the current ProtNLM prediction reviews.

Inputs (in ``openscientist-reconciliation/``):

* ``openscientist-verdicts.tsv`` -- a transcription of every per-term verdict stated in
  ``openscientist-adjudication.md`` (round, gene, GO term, the report's outcome and the
  assessment code the report assigns). This is transcribed data, not computed results.
* ``override-rationale.tsv`` -- for rows where the current YAML differs from the report, an
  optional verbatim excerpt from the current YAML ``review.summary`` that states the reason
  for the current call. Each excerpt is checked to be a verbatim substring of the summary;
  an excerpt that does not match fails the run.

Output: ``openscientist-reconciliation.tsv`` with the current YAML assessment, whether the
YAML review cites the OpenScientist investigation, whether a per-gene OpenScientist report
exists on disk, and an agreement class:

* ``AGREE`` -- identical assessment code.
* ``SAME_DIRECTION`` -- different code in the same polarity group
  (supported = COR/CNN/LSP; uncertain = UNC; incorrect = NPI/PLI/REP).
* ``OVERRIDE`` -- the current YAML is in a different polarity group from the report.
* ``NO_VERDICT`` -- the report records no verdict (failed run).

The YAMLs are read only. Run: ``uv run python projects/PROTNLM_EVALUATION/reconcile_openscientist.py``.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import yaml

GROUP = {
    "COR": "supported",
    "CNN": "supported",
    "LSP": "supported",
    "UNC": "uncertain",
    "NPI": "incorrect",
    "PLI": "incorrect",
    "REP": "incorrect",
}


def load_predictions(root: Path) -> dict[tuple[str, str], dict]:
    """Index current ProtNLM prediction reviews by (accession, GO id)."""
    index: dict[tuple[str, str], dict] = {}
    for path in sorted(root.glob("genes/*/*/*-protnlm-predictions-review.yaml")):
        doc = yaml.safe_load(path.read_text())
        for prediction in doc.get("predictions") or []:
            key = (doc["id"], prediction["predicted_term"]["id"])
            index[key] = dict(
                path=path.relative_to(root).as_posix(),
                gene_dir=path.parent,
                accession=doc["id"],
                prediction=prediction,
            )
    return index


def cites_openscientist(prediction: dict) -> bool:
    """True when the review text or its evidence refers to the OpenScientist investigation."""
    text = yaml.safe_dump(prediction["review"]).lower()
    return "openscientist" in text or "-hypotheses/" in text


def reconcile(root: Path) -> tuple[list[dict], dict]:
    base = root / "projects/PROTNLM_EVALUATION/openscientist-reconciliation"
    verdicts = list(csv.DictReader((base / "openscientist-verdicts.tsv").open(), delimiter="\t"))
    rationale = {
        (r["accession"], r["term_id"]): r["verbatim_excerpt"]
        for r in csv.DictReader((base / "override-rationale.tsv").open(), delimiter="\t")
    }
    predictions = load_predictions(root)
    rows = []
    for verdict in verdicts:
        key = (verdict["accession"], verdict["term_id"])
        assert key in predictions, f"No current prediction review for {key}"
        current = predictions[key]
        prediction = current["prediction"]
        assert prediction["predicted_term"]["label"] == verdict["term_label"], key
        yaml_call = prediction["review"]["assessment"]
        os_call = verdict["os_assessment"]
        if not os_call:
            agreement = "NO_VERDICT"
        elif os_call == yaml_call:
            agreement = "AGREE"
        elif GROUP[os_call] == GROUP[yaml_call]:
            agreement = "SAME_DIRECTION"
        else:
            agreement = "OVERRIDE"
        excerpt = rationale.get(key, "")
        if excerpt:
            summary = " ".join(prediction["review"]["summary"].split())
            assert excerpt in summary, f"Rationale excerpt is not verbatim for {key}"
        report_dirs = sorted(
            p.relative_to(root).as_posix()
            for p in current["gene_dir"].glob("*-hypotheses/*/openscientist.md")
        )
        rows.append(
            dict(
                round=verdict["round"],
                gene=verdict["gene"],
                accession=verdict["accession"],
                term_id=verdict["term_id"],
                term_label=verdict["term_label"],
                os_outcome=verdict["os_outcome"],
                os_assessment=os_call,
                yaml_assessment=yaml_call,
                agreement=agreement,
                yaml_cites_openscientist=str(cites_openscientist(prediction)).lower(),
                openscientist_reports_on_disk=len(report_dirs),
                yaml_rationale_excerpt=excerpt,
                review_file=current["path"],
                report_line=verdict["report_line"],
            )
        )
    summary = dict(
        terms=len(rows),
        agreement=dict(Counter(r["agreement"] for r in rows)),
        transitions=dict(
            Counter(
                f"{r['os_assessment'] or '-'}->{r['yaml_assessment']}"
                for r in rows
                if r["agreement"] != "AGREE"
            )
        ),
        yaml_cites_openscientist=sorted(
            {r["accession"] for r in rows if r["yaml_cites_openscientist"] == "true"}
        ),
        genes=len({r["accession"] for r in rows}),
        genes_with_report_on_disk=len(
            {r["accession"] for r in rows if r["openscientist_reports_on_disk"]}
        ),
        overrides_with_rationale_excerpt=sum(
            1 for r in rows if r["agreement"] == "OVERRIDE" and r["yaml_rationale_excerpt"]
        ),
    )
    return rows, summary


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    rows, summary = reconcile(root)
    out = root / "projects/PROTNLM_EVALUATION/openscientist-reconciliation/openscientist-reconciliation.tsv"
    with out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    (out.parent / "openscientist-reconciliation-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    write_page(out.parent.parent / "openscientist-reconciliation.md", rows, summary)
    print(json.dumps(summary, indent=2))


def write_page(path: Path, rows: list[dict], summary: dict) -> None:
    """Write a generated Markdown table; the explanatory prose lives in the adjudication report."""
    agreement = Counter(r["agreement"] for r in rows)
    lines = [
        "---",
        "title: ProtNLM2 OpenScientist verdicts vs current reviews",
        "---",
        "# OpenScientist verdicts vs current prediction reviews",
        "",
        "[OpenScientist adjudication report](openscientist-adjudication.md) · "
        "[ProtNLM2 Evaluation](../PROTNLM_EVALUATION.md) · "
        "[Generator](reconcile_openscientist.py) · "
        "[Transcribed verdicts](openscientist-reconciliation/openscientist-verdicts.tsv) · "
        "[Reconciliation TSV](openscientist-reconciliation/openscientist-reconciliation.tsv)",
        "",
        "Generated by `reconcile_openscientist.py`; do not edit by hand. The OpenScientist column is "
        "transcribed from the adjudication report. The current column is read from each gene's "
        "`*-protnlm-predictions-review.yaml`. The current YAML assessment is the project's call of record.",
        "",
        f"**{summary['terms']} GO terms across {summary['genes']} genes:** "
        f"{agreement.get('AGREE', 0)} agree, {agreement.get('SAME_DIRECTION', 0)} differ within the same "
        f"polarity group, {agreement.get('OVERRIDE', 0)} are overridden by the current YAML, and "
        f"{agreement.get('NO_VERDICT', 0)} had no OpenScientist verdict. "
        f"Reviews citing the OpenScientist investigation: {', '.join(summary['yaml_cites_openscientist']) or 'none'}.",
        "",
        "Polarity groups: supported = COR/CNN/LSP; uncertain = UNC; incorrect = NPI/PLI/REP. "
        "The rationale column quotes the current review summary verbatim (checked by the generator). "
        "Where it is blank, no reason for the difference is recorded.",
        "",
        "| Round | Gene | GO term | OpenScientist | Current YAML | Status | Cites OpenScientist | Current review's stated rationale |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        rationale = f"\"{r['yaml_rationale_excerpt']}\"" if r["yaml_rationale_excerpt"] else ""
        if r["agreement"] == "OVERRIDE" and not rationale:
            rationale = "override not documented"
        os_call = r["os_assessment"] or "no verdict"
        lines.append(
            f"| {r['round']} | {r['gene']} | {r['term_id']} {r['term_label']} | {r['os_outcome']}: {os_call} | "
            f"{r['yaml_assessment']} | {r['agreement']} | {r['yaml_cites_openscientist']} | {rationale} |"
        )
    lines.append("")
    path.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
