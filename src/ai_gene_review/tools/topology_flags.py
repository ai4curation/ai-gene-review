"""Pilot: combine full-length DeepTMHMM2 results with UniProt and FRR:0004.

Emits review flags only. No GO NOT assertion or gene-review mutation is performed.
An optional, manually curated evidence ledger can distinguish corroborated source
conflicts from predictor counterexamples. Evidence applies to the exact sequence
and assayed context, not every isoform, fragment or cellular protein population.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import yaml
from Bio import SeqIO

from ai_gene_review.tools.function_requirements import (
    ProteinFeatures, Verdict, evaluate, load_rules, parse_uniprot_flatfile, term_closures,
)


def prediction_features(prediction: dict, sequence: str) -> dict:
    """A missing/truncated prediction cannot serve as evidence of absence."""
    segments = prediction.get("segments", [])
    if not segments or len(prediction.get("topology_string", "")) != len(sequence):
        raise ValueError("Missing or incomplete topology prediction")
    position = 1
    for segment in segments:
        if segment["start"] != position or segment["end"] < position:
            raise ValueError("Topology segments must cover the sequence without gaps or overlaps")
        position = segment["end"] + 1
    if position != len(sequence) + 1:
        raise ValueError("Topology segment coverage differs from sequence length")
    tm = sum(s["name"] in {"TMhelix", "Beta sheet"} for s in segments)
    # The upstream exported topology uses M for alpha TM and B for beta strands.
    if bool(tm) != any(c in prediction["topology_string"] for c in "MB"):
        raise ValueError("Unrecognized or inconsistent membrane-spanning segment encoding")
    return {"tm": tm, "surface": sum(s["name"] in {"interfacial", "reentrant"} for s in segments)}


def evidence_state(entry: dict | None, sequence_hash: str) -> str:
    """Require explicit identity, scope and sources; do not mine conclusions from prose."""
    if entry is None:
        return "UNRESOLVED"
    if entry["sequence_sha256"] != sequence_hash:
        raise ValueError("Corroborating evidence belongs to a different sequence")
    if (entry["scope"] != "canonical_chain_in_assayed_context"
            or not entry.get("supported_by") or not entry.get("context")):
        raise ValueError("Corroborating evidence needs explicit scope and references")
    if entry["geometry"] not in {"NONSPANNING", "SPANNING"}:
        raise ValueError("Unknown evidence geometry")
    return entry["geometry"]


def conflict_verdict(geometry: str) -> str:
    return {"NONSPANNING": "CORROBORATED_TOPOLOGY_CONFLICT",
            "SPANNING": "PREDICTOR_COUNTEREXAMPLE",
            "UNRESOLVED": "REVIEW_CONFLICT"}[geometry]


def protein_flags(features: ProteinFeatures, predicted: dict, geometry: str,
                  ld_claims: list[dict]) -> list[dict]:
    """Flag source disagreements and context questions, never organelle disjointness."""
    flags = []
    if features.transmembrane_segments and not predicted["tm"] and predicted["surface"]:
        flags.append(dict(rule_id="DTM2:0001", verdict=conflict_verdict(geometry),
                          claim="UniProt TRANSMEM versus a full-length IF/RE-only prediction",
                          reason="Check spanning topology; IF/RE does not exclude membrane association or monotopic integral insertion."))
    if ld_claims and (features.transmembrane_segments or predicted["tm"]):
        flags.append(dict(rule_id="DTM2:0002", verdict="CONTEXT_CHECK",
                          claim="Lipid-droplet location plus a spanning-topology claim",
                          reason="Check whether the same form directly occupies the droplet monolayer, rather than an ER-contact pool, a tethered partner or an alternate topology.",
                          location_claims=ld_claims))
    return flags


def taxon_flags(taxon_ids: list[str], membrane_types: list[str]) -> list[dict]:
    """A narrow organism constraint, added after the human pilot exposed plastid calls."""
    impossible = sorted(set(membrane_types) & {"Chloroplast outer membrane", "Chloroplast inner membrane"})
    if "9606" in taxon_ids and impossible:
        return [dict(rule_id="DTM2:0003", verdict="TAXON_CONFLICT",
                     claim="Human protein assigned a chloroplast membrane",
                     reason="Human cells have no chloroplasts. Reject this compartment prediction; this does not determine the protein's actual topology or location.",
                     predicted_membrane_types=impossible)]
    return []


def intramembrane_flags(regions: list[dict], segments: list[dict]) -> list[dict]:
    """Compare the same residue interval; separate IF and TM regions can coexist."""
    overlaps = [dict(uniprot_intramembrane=region, predicted_span=segment)
                for region in regions for segment in segments
                if segment["name"] in {"TMhelix", "Beta sheet"}
                and max(region["start"], segment["start"]) <= min(region["end"], segment["end"])]
    if overlaps:
        return [dict(rule_id="DTM2:0004", verdict="REVIEW_CONFLICT",
                     claim="Predicted span overlaps a UniProt INTRAMEM region",
                     reason="Check insertion geometry for the overlapping residues and the same biological context. A spanning segment elsewhere is compatible with an intramembrane region.",
                     overlapping_regions=overlaps)]
    return []


def transporter_flag(rule: dict, closure: set[str], row: dict,
                     features: ProteinFeatures, predicted: dict, geometry: str) -> dict | None:
    """Reuse the existing qualifier, term, exemption and family scope of FRR:0004."""
    if (row["QUALIFIER"].startswith("NOT") or row["QUALIFIER"] not in rule["qualifiers"]
            or row["GO TERM"] not in closure or predicted["tm"]):
        return None
    original = evaluate(rule, features)
    return dict(rule_id=rule["id"], verdict=(conflict_verdict(geometry)
                if geometry == "SPANNING" or original == Verdict.SATISFIED else "REQUIREMENT_REVIEW"),
                claim=f'{row["QUALIFIER"]} {row["GO TERM"]} {row["GO NAME"]}',
                reason="No span is predicted. Evaluate the actual transport role, family evidence, complex contribution and independent topology before drawing a negative conclusion.",
                original_frr_verdict=original.value, original_reference=row["REFERENCE"],
                original_evidence=row["GO EVIDENCE CODE"], original_qualifier=row["QUALIFIER"])


def retained_ld_claims(review: dict) -> list[dict]:
    claims = []
    for a in review.get("existing_annotations", []):
        if str(a.get("qualifier", "")).startswith("NOT"):
            continue
        action = a.get("review", {}).get("action")
        terms = a.get("review", {}).get("proposed_replacement_terms", []) if action == "MODIFY" else [a["term"]]
        if action in {"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "MODIFY"} and any(t["id"] == "GO:0005811" for t in terms):
            claims.append({"reference": a["original_reference_id"], "evidence": a["evidence_type"],
                           "qualifier": a.get("qualifier", "unspecified"), "action": action})
    return claims


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True, help="Benchmark API output directory")
    parser.add_argument("--evidence", type=Path, help="Manually curated topology evidence ledger")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ledger = yaml.safe_load(args.evidence.read_text())["proteins"] if args.evidence else {}
    rules = load_rules(args.repo / "rules/function_requirements/function-requirement-rules.yaml")
    rule = next(r for r in rules if r["id"] == "FRR:0004")
    closure = term_closures([rule])[rule["id"]]
    rows = list(csv.DictReader(args.manifest.open(), delimiter="\t"))
    runs = json.loads((args.predictions / "timings.json").read_text())["runs"]
    run_hashes = {r["id"]: r["sequence_sha256"] for r in runs if r["repeat"] == 1}
    output = []
    for row in rows:
        source = args.repo / row["source"]
        record = SeqIO.read(source, "swiss")
        sequence = str(record.seq)
        digest = hashlib.sha256(sequence.encode()).hexdigest()
        if record.id != row["accession"] or digest != row["sequence_sha256"]:
            raise ValueError(f"Input identity/sequence mismatch: {row['gene']}")
        if run_hashes.get(record.id) != digest:
            raise ValueError(f"Prediction run sequence mismatch: {row['gene']}")
        prediction_file = args.predictions / f"{record.id}.r1.json"
        prediction = json.loads(prediction_file.read_text())[0]
        if prediction["id"] != record.id:
            raise ValueError("Prediction accession mismatch")
        predicted = prediction_features(prediction, sequence)
        features = parse_uniprot_flatfile(source.read_text())
        entry = ledger.get(record.id)
        geometry = evidence_state(entry, digest)
        review = yaml.safe_load((source.parent / f"{row['gene']}-ai-review.yaml").read_text())
        flags = protein_flags(features, predicted, geometry, retained_ld_claims(review))
        flags.extend(taxon_flags(record.annotations.get("ncbi_taxid", []), prediction["membrane_types"]))
        regions = [{"start": int(f.location.start) + 1, "end": int(f.location.end)}
                   for f in record.features if f.type == "INTRAMEM" and not f.location.ref]
        flags.extend(intramembrane_flags(regions, prediction["segments"]))
        with (source.parent / f"{row['gene']}-goa.tsv").open() as stream:
            for annotation in csv.DictReader(stream, delimiter="\t"):
                # Never transfer canonical topology to a separately keyed isoform.
                if annotation["GENE PRODUCT ID"] != record.id:
                    continue
                flag = transporter_flag(rule, closure, annotation, features, predicted, geometry)
                if flag:
                    matches = [a for a in review.get("existing_annotations", [])
                               if a["term"]["id"] == annotation["GO TERM"]
                               and a["original_reference_id"] == annotation["REFERENCE"]
                               and a["evidence_type"] == annotation["GO EVIDENCE CODE"]
                               and a.get("qualifier", annotation["QUALIFIER"]) == annotation["QUALIFIER"]]
                    flag["review_actions"] = sorted({a.get("review", {}).get("action", "PENDING") for a in matches})
                    flags.append(flag)
        for flag in flags:
            output.append(dict(gene=row["gene"], accession=record.id, sequence_sha256=digest,
                               predicted_spans=predicted["tm"], predicted_if_re=predicted["surface"],
                               uniprot_spans=features.transmembrane_segments,
                               curated_geometry=geometry, corroboration=entry,
                               prediction_source=str(prediction_file), **flag))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"status": "PILOT", "emits_go_not": False,
                                      "proteins_evaluated": len(rows), "flags": output}, indent=2) + "\n")
    print(f"Evaluated {len(rows)} proteins; {len(output)} flags on {len({r['gene'] for r in output})} proteins. No GO assertions emitted.")


if __name__ == "__main__":
    main()
