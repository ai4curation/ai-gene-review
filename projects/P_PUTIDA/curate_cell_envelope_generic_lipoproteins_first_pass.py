#!/usr/bin/env python3
"""First-pass curate PSEPK generic lipoprotein/signal-peptide spillovers."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_TSV = ROOT / "projects/P_PUTIDA/batches/module_cell_envelope_division_generic_lipoprotein_signal_spillovers.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0016020": {"id": "GO:0016020", "label": "membrane"},
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_lines(path: Path) -> list[str]:
    return read_text(path).splitlines()


def first_line(path: Path, *needles: str) -> str:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    raise ValueError(f"No line in {path} contains all needles: {needles}")


def optional_first_line(path: Path, *needles: str) -> str | None:
    for line in read_lines(path):
        if all(needle in line for needle in needles):
            return line
    return None


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def evidence_support(gene: str) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [
        support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   ")),
    ]
    for marker in (
        ("DR   PROSITE; PS51257; PROKAR_LIPOPROTEIN; 1.",),
        ("KW   Lipoprotein",),
        ("KW   Signal",),
        ("FT   SIGNAL",),
        ("KW   Coiled coil",),
        ("FT   COILED",),
    ):
        line = optional_first_line(uniprot, *marker)
        if line:
            data.append(support(file_id(gene, "uniprot.txt"), line))
    data.extend(
        [
            support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  protein_description:")),
            support(file_id(gene, "deep-research-asta.md"), "  protein_family: Not specified in UniProt"),
            support(file_id(gene, "deep-research-asta.md"), "  protein_domains: Not specified in UniProt"),
        ]
    )
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    for ref_id in (file_id(gene, "goa.tsv"), file_id(gene, "uniprot.txt"), file_id(gene, "deep-research-asta.md")):
        if ref_id in seen:
            continue
        refs.append(
            {
                "id": ref_id,
                "title": {
                    file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
                    file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
                    file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
                }[ref_id],
                "findings": [],
            }
        )
    return refs


def role_for(gene: str) -> str:
    text = read_text(GENE_ROOT / gene / f"{gene}-uniprot.txt")
    if "KW   Coiled coil" in text or "FT   COILED" in text:
        return "coiled-coil predicted lipoprotein candidate"
    if "FT   SIGNAL" in text or "KW   Signal" in text:
        return "SignalP-supported predicted lipoprotein candidate"
    if "DR   PROSITE; PS51257; PROKAR_LIPOPROTEIN; 1." in text:
        return "PROSITE-supported predicted lipoprotein candidate"
    return "predicted lipoprotein candidate"


def description_for(gene: str, role: str) -> str:
    return (
        f"{gene} encodes an uncharacterized {role} in Pseudomonas putida KT2440. "
        "Available first-pass evidence supports only a broad membrane/envelope placement; "
        "no specific molecular function, substrate, partner complex, or pathway role is resolved."
    )


def new_membrane_annotation(gene: str) -> dict:
    return {
        "term": TERM["GO:0016020"],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": "located_in",
        "review": {
            "summary": "A broad membrane localization is the only supported first-pass GO candidate.",
            "action": "NEW",
            "reason": (
                "UniProt identifies the protein as a lipoprotein or signal-peptide-bearing lipoprotein candidate, "
                "and Asta did not retrieve a specific family, domain, literature-backed function, or pathway hypothesis. "
                "Use broad membrane placement and leave outer-membrane specificity and molecular function unresolved."
            ),
            "supported_by": evidence_support(gene),
        },
    }


def core_for(gene: str, role: str) -> dict:
    return {
        "description": role,
        "locations": [TERM["GO:0016020"]],
        "supported_by": evidence_support(gene),
    }


def apply_review(gene: str, accession: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    role = role_for(gene)
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = description_for(gene, role)
    data["references"] = reference_list(data.get("references") or [], gene, accession)
    existing = data.get("existing_annotations") or []
    unexpected = [
        annotation.get("term", {}).get("id")
        for annotation in existing
        if annotation.get("review", {}).get("action") != "NEW"
    ]
    if unexpected:
        raise ValueError(f"{gene} unexpectedly has non-NEW GOA annotations: {unexpected}")
    data["existing_annotations"] = [
        annotation
        for annotation in existing
        if not (
            annotation.get("term", {}).get("id") == "GO:0016020"
            and annotation.get("review", {}).get("action") == "NEW"
        )
    ]
    data["existing_annotations"].append(new_membrane_annotation(gene))
    data["core_functions"] = [core_for(gene, role)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"Is {gene} a mature membrane-anchored lipoprotein in KT2440, and does it have a "
                "condition-specific envelope partner or phenotype?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Verify {gene} localization and lipidation experimentally, then test deletion/complemented strains "
                "under outer-membrane, osmotic, desiccation, and envelope-stress conditions before assigning a "
                "pathway-specific GO process."
            ),
            "experiment_type": "targeted membrane localization, lipidation, and envelope-stress phenotype assay",
        }
    ]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str, accession: str) -> None:
    role = role_for(gene)
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    product_line = first_line(uniprot, "DE   ")
    marker = optional_first_line(uniprot, "DR   PROSITE; PS51257; PROKAR_LIPOPROTEIN; 1.")
    if not marker:
        marker = optional_first_line(uniprot, "KW   Signal") or optional_first_line(uniprot, "KW   Lipoprotein") or product_line
    note = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass generic lipoprotein/signal-peptide spillover curation.",
        description_for(gene, role),
        "",
        f"Primary provenance: UniProt identifies the protein as a lipoprotein candidate "
        f"[{file_id(gene, 'uniprot.txt')} \"{product_line}\"; {file_id(gene, 'uniprot.txt')} \"{marker}\"].",
        f"Asta retrieval did not resolve a specific functional family or domain "
        f"[{file_id(gene, 'deep-research-asta.md')} \"  protein_family: Not specified in UniProt\"; "
        f"{file_id(gene, 'deep-research-asta.md')} \"  protein_domains: Not specified in UniProt\"].",
        "",
        "Decision: add only broad membrane localization and keep molecular function, outer-membrane specificity, and pathway role unresolved.",
    ]
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(note) + "\n", encoding="utf-8")


def main() -> None:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            gene = row["gene"]
            accession = row["uniprot_accession"]
            apply_review(gene, accession)
            write_notes(gene, accession)
            print(f"Curated {gene}")


if __name__ == "__main__":
    main()
