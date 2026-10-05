"""Regenerate selection tables from frozen API responses; no biological verdicts."""

import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
MODS = {"HGNC", "MGI", "RGD", "WormBase", "TAIR", "ZFIN", "Xenbase"}


def read_jsonl(name):
    with gzip.open(BASE / name, "rt") as stream:
        return [json.loads(line) for line in stream]


def write_csv(name, rows):
    with (BASE / name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def identifiers(record):
    return {
        (x["database"], x["id"])
        for x in record.get("uniProtKBCrossReferences", [])
        if x["database"] in MODS
    }


def main():
    selected = list(csv.DictReader((BASE / "selection.csv").open()))
    frozen = {r["accession"]: r for r in read_jsonl("api-snapshot.jsonl.gz")}
    searches = {
        r["target_accession"]: r for r in read_jsonl("reference-searches.jsonl.gz")
    }
    with gzip.open(BASE / "published-accessions.tsv.gz", "rt") as stream:
        published = {r["Entry"]: r for r in csv.DictReader(stream, delimiter="\t")}
    assert len(selected) == len({r["accession"] for r in selected}) == 20
    assert len({(r["species"], r["gene_symbol"]) for r in selected}) == 20
    cohort, statements, reference_rows, fasta = [], [], [], []
    for row in selected:
        acc = row["accession"]
        snapshot = frozen[acc]
        assert snapshot["prediction_status"] == snapshot["uniprot_status"] == 200
        prediction, uniprot = snapshot["prediction"], snapshot["uniprot"]
        assert prediction["primaryAccession"] == uniprot["primaryAccession"] == acc
        target_ids = identifiers(uniprot)
        matches = []
        for reference in searches[acc].get("response", {}).get("results", []):
            shared_ids = target_ids & identifiers(reference)
            # A synonym search is not enough: NARF also retrieves RNF138.
            if not shared_ids:
                continue
            matches.append(reference)
            reference_rows.append(
                {
                    "target_accession": acc,
                    "reference_accession": reference["primaryAccession"],
                    "shared_mod_ids": ";".join(
                        (v if v.startswith(k + ":") else f"{k}:{v}")
                        for k, v in sorted(shared_ids)
                    ),
                    "target_length": uniprot["sequence"]["length"],
                    "reference_length": reference["sequence"]["length"],
                    "identical_sequence": uniprot["sequence"]["value"]
                    == reference["sequence"]["value"],
                }
            )
        emitted = []

        def add(kind, obj, term_id="", text=""):
            emitted.append(
                {
                    "accession": acc,
                    "species": row["species"],
                    "gene_symbol": row["gene_symbol"],
                    "kind": kind,
                    "term_id": term_id,
                    "text": text,
                    "source_object": json.dumps(obj, sort_keys=True),
                    "status": "SELECTED_NOT_REVIEWED",
                }
            )

        for name_type, value in prediction.get("proteinDescription", {}).items():
            objects = value if isinstance(value, list) else [value]
            for obj in objects:
                if isinstance(obj, dict) and "fullName" in obj:
                    add("protein_name", obj, text=obj["fullName"]["value"])
        for ref in prediction.get("uniProtKBCrossReferences", []):
            if ref["database"] == "GO":
                label = next(
                    x["value"] for x in ref["properties"] if x["key"] == "GoTerm"
                )
                add("GO", ref, ref["id"], label)
        for comment in prediction.get("comments", []):
            if comment["commentType"] == "FUNCTION":
                for item in comment.get("texts", []):
                    add("function", item, text=item["value"])
            elif comment["commentType"] == "SUBCELLULAR LOCATION":
                for location in comment.get("subcellularLocations", []):
                    for key in ("location", "topology", "orientation"):
                        if key in location:
                            item = location[key]
                            add(key, item, item.get("id", ""), item["value"])
        assert emitted, acc
        statements.extend(emitted)
        counts = Counter(x["kind"] for x in emitted)
        row = dict(row)
        row.update(
            {
                "taxon_id": uniprot["organism"]["taxonId"],
                "organism": uniprot["organism"]["scientificName"],
                "mod_identifiers": ";".join(
                    (v if v.startswith(k + ":") else f"{k}:{v}")
                    for k, v in sorted(target_ids)
                ),
                "current_length": uniprot["sequence"]["length"],
                "published_list_length": published[acc]["Length"],
                "sequence_sha256": hashlib.sha256(
                    uniprot["sequence"]["value"].encode()
                ).hexdigest(),
                "same_gene_reviewed_references": ";".join(
                    x["primaryAccession"] for x in matches
                ),
                "reference_lengths": ";".join(
                    str(x["sequence"]["length"]) for x in matches
                ),
                "go_count": counts["GO"],
                "function_count": counts["function"],
                "location_count": counts["location"],
                "name_count": counts["protein_name"],
                "prediction_url": snapshot["prediction_url"],
                "sequence_url": snapshot["uniprot_url"],
                "status": "SELECTED_NOT_REVIEWED",
            }
        )
        cohort.append(row)
        fasta.append(
            f">{acc} {row['species']}/{row['gene_symbol']} current_UniProt_sequence\n{uniprot['sequence']['value']}\n"
        )
    write_csv("cohort.csv", cohort)
    write_csv("prediction-statements.csv", statements)
    write_csv("same-gene-references.csv", reference_rows)
    (BASE / "sequences.fasta").write_text("".join(fasta))
    summary = {
        "genes": len(cohort),
        "species_counts": dict(Counter(r["species"] for r in cohort)),
        "statement_counts": dict(Counter(r["kind"] for r in statements)),
        "genes_with_go_or_function": sum(
            bool(r["go_count"] or r["function_count"]) for r in cohort
        ),
        "genes_with_go": sum(bool(r["go_count"]) for r in cohort),
        "same_gene_reference_comparisons": len(reference_rows),
        "source_period": {
            "first": min(r["retrieved_at"] for r in frozen.values()),
            "last": max(r["retrieved_at"] for r in frozen.values()),
        },
        "status": "SELECTED_NOT_REVIEWED",
    }
    (BASE / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    files = [
        "selection.csv",
        "api-snapshot.jsonl.gz",
        "reference-searches.jsonl.gz",
        "published-accessions.tsv.gz",
        "cohort.csv",
        "prediction-statements.csv",
        "same-gene-references.csv",
        "sequences.fasta",
        "summary.json",
        "summarize.py",
    ]
    manifest = {
        "sources": [
            "https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv",
            "https://rest.uniprot.org/uniprotkb/protnlm/{accession}",
            "https://rest.uniprot.org/uniprotkb/{accession}.json",
        ],
        "checksums": {
            f: hashlib.sha256((BASE / f).read_bytes()).hexdigest() for f in files
        },
        "selection": "Purposive cross-species challenge set selected after inspecting predictions; not a random sample or an estimate of accuracy.",
        "sequence_scope": "Current exact-accession UniProt sequences. Prediction responses do not include the original model input sequence; identity to that historical input is not established.",
        "reference_scope": "Reviewed same-gene candidates require a shared MOD identifier. They are comparison records, not substitute prediction targets or automatic validation.",
        "review_scope": "Selection only. Proposed evolutionary comparators are not established orthologs or completed analyses.",
    }
    (BASE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
