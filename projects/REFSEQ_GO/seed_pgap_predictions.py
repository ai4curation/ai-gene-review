#!/usr/bin/env python3
"""Seed a ``GENE-pgap-predictions-review.yaml`` that treats NCBI PGAP GO as predictions.

For one UniProt accession, using the outputs of ``compare_refseq_goa.py``, this
writes into ``--out-dir``:

* ``<GENE>-pgap-predictions-review.yaml``: a PredictionReview scaffold with one
  prediction per PGAP GO term and per PGAP EC number. Every ``review`` is a
  placeholder (``summary: "TODO ..."``) for the curator to replace.
* ``<GENE>-pgap-prediction-evidence/``: the WP_ GenPept record (naming
  evidence, product, GO, EC) and ``pgap_models.yaml`` listing the naming
  model and every other NCBI HMM the protein matches with its GO, so the
  review can quote them as ``file:`` sources.

GO and EC are taken from the WP_ protein record, the freshest PGAP source; a
term the genome record lacks is flagged in its placeholder summary, and terms
only on the genome record are listed in the description. All PGAP terms are
seeded, including those GOA also has, so the file gives a
complete per-gene verdict on PGAP. For a term also in GOA, the assessment should
agree with the main review: CNN if accepted, LSP if too general, NPI if removed.

Usage::

    uv run python projects/REFSEQ_GO/seed_pgap_predictions.py \\
        --results-dir projects/REFSEQ_GO/results/PSEPK --accession Q88Q37 \\
        --gene PP_0661 --taxon-id 160488 --taxon-label "Pseudomonas putida KT2440" \\
        --out-dir /tmp/seeds/PP_0661
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

import typer
import yaml

from compare_refseq_goa import Closure, parse_genpept, read_hmm_pgap

app = typer.Typer(add_completion=False)

TERM_TYPE = {"F": "GO_MF", "P": "GO_BP", "C": "GO_CC"}


def genpept_record(text: str, wp: str) -> str:
    """The raw GenPept record for one WP_ accession from a multi-record file.

    >>> genpept_record("LOCUS A\\nVERSION     WP_1.1\\n//\\nLOCUS B\\nVERSION     WP_2.1\\n//", "WP_2.1")
    'LOCUS B\\nVERSION     WP_2.1\\n//\\n'
    """
    for record in text.split("//"):
        if re.search(rf"^VERSION\s+{re.escape(wp)}\s*$", record, re.M):
            return record.strip("\n") + "\n//\n"
    return ""


def ec_numbers(record: str) -> list[str]:
    """EC numbers on a GenPept record.

    >>> ec_numbers('  /EC_number="6.3.2.14"\\n  /EC_number="6.2.1.71"\\n')
    ['6.3.2.14', '6.2.1.71']
    """
    return re.findall(r'/EC_number="([^"]+)"', record)


@app.command()
def main(
    results_dir: Path = typer.Option(..., help="Output dir of compare_refseq_goa.py"),
    accession: str = typer.Option(..., help="UniProt accession"),
    gene: str = typer.Option(..., help="Gene folder name / symbol"),
    taxon_id: int = typer.Option(...),
    taxon_label: str = typer.Option(...),
    out_dir: Path = typer.Option(..., help="Where to write the seed files"),
    cache_dir: Path = typer.Option(Path(".cache/refseq_go")),
) -> None:
    summary = yaml.safe_load((results_dir / "summary.yaml").open())
    loci = {}
    with (results_dir / "loci.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if accession in row["uniprot_accessions"].split("|"):
                loci[row["locus"]] = row
    if not loci:
        raise typer.BadParameter(f"{accession} is not in {results_dir}/loci.tsv")
    wps = sorted(
        {w for r in loci.values() for w in r["refseq_proteins"].split("|") if w}
    )
    if not wps:
        raise typer.BadParameter(f"{accession} has no RefSeq protein in this run")
    proteins = {}
    with (results_dir / "ncbi_proteins.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            proteins[row["refseq_protein"]] = row

    # GO terms NCBI asserts, and the GOA terms for the same loci
    ncbi_terms: dict[str, str] = {}
    goa_terms: set[str] = set()
    with (results_dir / "term_comparison.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["locus"] not in loci:
                continue
            if row["side"] == "ncbi" and not row["source"].startswith("added:"):
                ncbi_terms[row["go_id"]] = row["aspect"]
            elif row["side"] == "goa":
                goa_terms.add(row["go_id"])

    assembly = summary["assembly"]
    sub = "wp" if summary["ncbi_source"] == "wp" else "live"
    gp_text = (cache_dir / assembly / sub / "wp_records.gp").read_text()
    records = {wp: genpept_record(gp_text, wp) for wp in wps}
    parsed = {wp: parse_genpept(rec).get(wp, {}) for wp, rec in records.items()}

    model_go, pfam_copies = read_hmm_pgap(cache_dir / "hmm_PGAP.tsv")
    hmm_rows = {}
    with (cache_dir / "hmm_PGAP.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            hmm_rows[row["#ncbi_accession"].split(".")[0]] = row
    matched = set()
    models_path = cache_dir / assembly / "uniprot_models.tsv"
    if models_path.exists():
        with models_path.open() as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row["Entry"] == accession:
                    ids = (row["NCBIfam"] or "") + ";" + (row["Pfam"] or "")
                    matched = {x.strip() for x in ids.split(";") if x.strip()}

    def model_entry(acc: str) -> dict:
        r = hmm_rows.get(acc, {})
        return {
            "model": acc,
            "family_type": r.get("family_type", ""),
            "product_name": r.get("product_name", ""),
            "go_terms": model_go.get(acc, []),
            "ec_numbers": [e for e in r.get("ec_numbers", "").split(",") if e],
        }

    other = []
    for m in sorted(matched):
        if m.startswith("PF"):
            other += [dict(model_entry(nf), wraps=m) for nf in pfam_copies.get(m, [])]
        else:
            other.append(model_entry(m))

    evidence_dir = out_dir / f"{gene}-pgap-prediction-evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    for wp, rec in records.items():
        (evidence_dir / f"{wp}.gp").write_text(rec)
    naming = {wp: parsed[wp].get("naming", "") for wp in wps}
    models_doc = {
        "accession": accession,
        "refseq_proteins": wps,
        "ncbi_source": summary["ncbi_source"],
        "annotation_release": summary.get("annotation_release"),
        "naming_model": naming,
        "naming_model_details": [
            model_entry(n.split(":", 1)[1].split(".")[0])
            for n in naming.values()
            if n.startswith("HMM:")
        ],
        "other_matched_ncbi_hmms": other,
        "note": "Other matched HMMs are InterPro's matches (UniProt NCBIfam/Pfam "
        "cross-references); PGAP passes on GO only from the naming model.",
    }
    (evidence_dir / "pgap_models.yaml").write_text(
        yaml.safe_dump(models_doc, sort_keys=False, width=100)
    )

    labels = Closure().adapter.label
    version = f"{summary.get('annotation_release')} ({summary['ncbi_source']}); GO from WP_ record"
    wp_terms: dict[str, str] = {}
    for wp in wps:
        for term, aspect in parsed[wp].get("go", []):
            wp_terms.setdefault(term, aspect)
    predictions = []
    for term, aspect in sorted(wp_terms.items(), key=lambda kv: (kv[1], kv[0])):
        notes = [
            "Also in GOA; agree with the main review."
            if term in goa_terms
            else "Not in GOA."
        ]
        if summary["ncbi_source"] != "wp" and term not in ncbi_terms:
            notes.append("Not on the genome record (newer WP_ record).")
        predictions.append(
            {
                "source_method": "NCBI PGAP",
                "source_version": version,
                "source_reference_id": "PMID:33270901",
                "predicted_term": {"id": term, "label": labels(term) or term},
                "predicted_term_type": TERM_TYPE[aspect],
                "review": {
                    "assessment": "UNC",
                    "confidence_score": 1,
                    "summary": "TODO: assess. " + " ".join(notes),
                },
            }
        )
    genome_only = (
        sorted(set(ncbi_terms) - set(wp_terms))
        if summary["ncbi_source"] != "wp"
        else []
    )
    for wp in wps:
        for ec in ec_numbers(records[wp]):
            predictions.append(
                {
                    "source_method": "NCBI PGAP",
                    "source_version": version,
                    "source_reference_id": "PMID:33270901",
                    "predicted_term": {"id": f"EC:{ec}", "label": f"EC {ec}"},
                    "predicted_term_type": "EC",
                    "review": {
                        "assessment": "UNC",
                        "confidence_score": 1,
                        "summary": "TODO: assess.",
                    },
                }
            )
    doc = {
        "id": accession,
        "gene_symbol": gene,
        "taxon": {"id": f"NCBITaxon:{taxon_id}", "label": taxon_label},
        "status": "DRAFT",
        "locus_tag": sorted(loci)[0],
        "description": "TODO: summary of how NCBI PGAP's GO and EC predictions for this gene "
        "compare with the evidence."
        + (
            f" (The genome record also carries {', '.join(genome_only)}, absent from the newer WP_ record.)"
            if genome_only
            else ""
        ),
        "source_documents": [f"{gene}-pgap-prediction-evidence/{wp}.gp" for wp in wps]
        + [f"{gene}-pgap-prediction-evidence/pgap_models.yaml"],
        "predictions": predictions,
    }
    out = out_dir / f"{gene}-pgap-predictions-review.yaml"
    out.write_text(yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True))
    typer.echo(
        f"{gene}: {len(predictions)} predictions ({len(wp_terms)} GO, "
        f"{len(predictions) - len(wp_terms)} EC); naming {naming}; genome-only {genome_only}"
    )


if __name__ == "__main__":
    app()
