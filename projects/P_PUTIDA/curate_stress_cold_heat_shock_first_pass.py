#!/usr/bin/env python3
"""First-pass curate the PSEPK cold/heat-shock spillover stress split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_DIR = ROOT / "projects" / "P_PUTIDA" / "batches"
BATCH_TSV = BATCH_DIR / "module_stress_detoxification_cold_heat_shock_chaperone_spillovers.tsv"
PARTITION_TSV = BATCH_DIR / "module_stress_detoxification_partition.tsv"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERM = {
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0009408": {"id": "GO:0009408", "label": "response to heat"},
    "GO:0051082": {"id": "GO:0051082", "label": "unfolded protein binding"},
}


GENE_INFO = {
    "capB": {
        "role": "cold-shock-domain nucleic-acid-binding protein",
        "description": (
            "capB encodes a small cytosolic cold-shock-domain protein in Pseudomonas putida KT2440. "
            "It contains a CspA-like cold-shock/OB-fold nucleic-acid-binding domain and is best treated "
            "as a cold-shock-domain nucleic-acid-binding protein; the first-pass evidence does not resolve "
            "a specific RNA or DNA target."
        ),
        "primary_function": TERM["GO:0003676"],
        "locations": [TERM["GO:0005829"]],
        "processes": [],
        "new_terms": [],
    },
    "cspA-I": {
        "role": "major cold-shock-domain nucleic-acid-binding protein",
        "description": (
            "cspA-I encodes a small cytosolic major cold-shock protein in Pseudomonas putida KT2440. "
            "Its CspA-like cold-shock/OB-fold domain supports nucleic-acid binding, consistent with "
            "a cold-shock-domain protein whose specific RNA or DNA targets remain unresolved."
        ),
        "primary_function": TERM["GO:0003676"],
        "locations": [TERM["GO:0005829"]],
        "processes": [],
        "new_terms": [],
    },
    "ibpA": {
        "role": "HSP20-family small heat-shock holdase candidate",
        "description": (
            "ibpA encodes a predicted HSP20-family small heat shock protein in Pseudomonas putida KT2440. "
            "It contains an alpha-crystallin/HSP20 domain and is best treated as a putative stress-responsive "
            "holdase chaperone that binds non-native or unfolded proteins, while its specific KT2440 clients "
            "remain unknown."
        ),
        "primary_function": TERM["GO:0051082"],
        "locations": [],
        "processes": [],
        "new_terms": ["GO:0051082"],
    },
    "PP_3313": {
        "role": "HSP20-family small heat-shock holdase candidate",
        "description": (
            "PP_3313 encodes a predicted HSP20-family small heat shock protein in Pseudomonas putida KT2440. "
            "It contains an alpha-crystallin/HSP20 domain and an HSP21-like family assignment, supporting "
            "a putative heat-responsive holdase chaperone that binds non-native or unfolded proteins."
        ),
        "primary_function": TERM["GO:0051082"],
        "locations": [],
        "processes": [TERM["GO:0009408"]],
        "new_terms": ["GO:0051082"],
    },
    "PP_3314": {
        "role": "HSP20-family small heat-shock holdase candidate",
        "description": (
            "PP_3314 encodes a predicted HSP20-family small heat shock protein in Pseudomonas putida KT2440. "
            "It contains an alpha-crystallin/HSP20 domain and is best treated as a putative stress-responsive "
            "holdase chaperone that binds non-native or unfolded proteins, while its specific KT2440 clients "
            "remain unknown."
        ),
        "primary_function": TERM["GO:0051082"],
        "locations": [],
        "processes": [],
        "new_terms": ["GO:0051082"],
    },
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


def first_prefixed_lines(path: Path, prefix: str, limit: int = 3) -> list[str]:
    return [line for line in read_lines(path) if line.startswith(prefix)][:limit]


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def goa_support(gene: str, term_id: str) -> dict[str, str] | None:
    line = optional_first_line(GENE_ROOT / gene / f"{gene}-goa.tsv", term_id)
    if not line:
        return None
    return support(file_id(gene, "goa.tsv"), line)


def add_unique(items: list[dict[str, str]], item: dict[str, str]) -> None:
    if item["supporting_text"] not in {existing["supporting_text"] for existing in items}:
        items.append(item)


def uniprot_evidence(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    data = [support(file_id(gene, "uniprot.txt"), first_line(uniprot, "DE   "))]
    if term_id:
        line = optional_first_line(uniprot, f"DR   GO; {term_id};")
        if line:
            add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    for marker in (
        ("CC   -!- SUBCELLULAR LOCATION:",),
        ("CC   -!- SIMILARITY:",),
        ("DR   PANTHER;",),
        ("DR   Pfam;",),
        ("FT   DOMAIN",),
    ):
        line = optional_first_line(uniprot, *marker)
        if line:
            add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    for line in first_prefixed_lines(uniprot, "DR   InterPro;", 4):
        add_unique(data, support(file_id(gene, "uniprot.txt"), line))
    return data


def asta_evidence(gene: str) -> list[dict[str, str]]:
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    data = [support(file_id(gene, "deep-research-asta.md"), first_line(asta, "  uniprot_accession:"))]
    for marker in ("  protein_description:", "  protein_family:", "  protein_domains:"):
        line = optional_first_line(asta, marker)
        if line:
            add_unique(data, support(file_id(gene, "deep-research-asta.md"), line))
    return data


def standard_support(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    data: list[dict[str, str]] = []
    if term_id:
        goa = goa_support(gene, term_id)
        if goa:
            data.append(goa)
    data.extend(uniprot_evidence(gene, term_id))
    data.extend(asta_evidence(gene))
    return data


def reference_list(existing_refs: list[dict], gene: str, accession: str) -> list[dict]:
    refs: list[dict] = []
    seen = set()
    for ref in existing_refs:
        ref_id = ref["id"]
        seen.add(ref_id)
        refs.append(ref)
    titles = {
        file_id(gene, "goa.tsv"): f"QuickGO GOA annotations for {gene} ({accession})",
        file_id(gene, "uniprot.txt"): f"UniProtKB entry for {gene} ({accession})",
        file_id(gene, "deep-research-asta.md"): f"Asta retrieval report for {gene} ({accession})",
    }
    for ref_id, title in titles.items():
        if ref_id not in seen:
            refs.append({"id": ref_id, "title": title, "findings": []})
    return refs


def review_for_annotation(gene: str, term_id: str) -> dict:
    if term_id == "GO:0003676":
        return {
            "summary": "The cold-shock/OB-fold domain evidence supports a conservative nucleic-acid-binding annotation.",
            "action": "ACCEPT",
            "reason": (
                "The GOA row is an InterPro2GO call from cold-shock-domain records. Because the evidence does not "
                "resolve a specific RNA or DNA target for this KT2440 protein, nucleic acid binding is the right "
                "first-pass level of specificity."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    if term_id == "GO:0005737":
        return {
            "summary": "Cytoplasmic localization is compatible with the soluble bacterial cold-shock protein context.",
            "action": "ACCEPT",
            "reason": "The GOA row comes from UniProt subcellular-location mapping and is consistent with the UniProt cytoplasm annotation.",
            "supported_by": standard_support(gene, term_id),
        }
    if term_id == "GO:0005829":
        return {
            "summary": "Cytosolic localization is reasonable for this small soluble cold-shock protein.",
            "action": "ACCEPT",
            "reason": "The ARBA-derived cytosol row is compatible with the UniProt cytoplasmic localization and the soluble CspA-like domain context.",
            "supported_by": standard_support(gene, term_id),
        }
    if term_id == "GO:0009408":
        return {
            "summary": "Response to heat is supported as process context for this HSP20-family heat-shock protein.",
            "action": "ACCEPT",
            "reason": (
                "The GOA row is an InterPro2GO annotation from the HSP21-like/HSP20 family assignment. The review retains "
                "this as heat-stress process context and adds unfolded protein binding separately as the direct molecular function."
            ),
            "supported_by": standard_support(gene, term_id),
        }
    raise ValueError(f"No review rule for {gene} {term_id}")


def new_annotation(gene: str, term_id: str) -> dict:
    term = TERM[term_id]
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": "enables",
        "review": {
            "summary": f"First-pass evidence supports adding {term['label']} for this {GENE_INFO[gene]['role']}.",
            "action": "NEW",
            "reason": (
                "The current GOA is empty or lacks a molecular-function row. The recommendation is conservative and follows "
                "the local PSEPK HSP20 precedent: alpha-crystallin/HSP20 and HSP20-like chaperone domain evidence supports "
                "unfolded-protein-binding/holdase context, while specific clients remain unresolved."
            ),
            "supported_by": standard_support(gene, None),
        },
    }


def core_for(gene: str) -> dict:
    info = GENE_INFO[gene]
    core = {
        "description": info["role"],
        "molecular_function": info["primary_function"],
        "supported_by": standard_support(gene, info["primary_function"]["id"]),
    }
    if info["locations"]:
        core["locations"] = info["locations"]
    if info["processes"]:
        core["directly_involved_in"] = info["processes"]
    return core


def apply_review(gene: str, accession: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(read_text(path))
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = GENE_INFO[gene]["description"]
    data["references"] = reference_list(data.get("references") or [], gene, accession)
    existing = data.get("existing_annotations") or []
    retained = []
    seen_new = {annotation.get("term", {}).get("id") for annotation in existing if annotation.get("review", {}).get("action") == "NEW"}
    for annotation in existing:
        if annotation.get("review", {}).get("action") == "NEW":
            retained.append(annotation)
            continue
        annotation["review"] = review_for_annotation(gene, annotation["term"]["id"])
        retained.append(annotation)
    for term_id in GENE_INFO[gene]["new_terms"]:
        if term_id not in seen_new:
            retained.append(new_annotation(gene, term_id))
    data["existing_annotations"] = retained
    data["core_functions"] = [core_for(gene)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What are the physiological targets and stress conditions that define the KT2440 role of {gene}?"
            )
        }
    ]
    if GENE_INFO[gene]["primary_function"]["id"] == "GO:0003676":
        experiment = (
            f"Measure {gene} binding to candidate RNA and single-stranded DNA substrates in vitro, then pair a clean "
            "deletion/complementation strain with cold-shock transcriptome or growth assays."
        )
        experiment_type = "nucleic-acid-binding and cold-shock phenotype assay"
    else:
        experiment = (
            f"Compare wild-type and {gene} deletion/complemented strains for heat-stress survival and insoluble protein "
            "accumulation, then test purified protein for holdase protection of model unfolded substrates."
        )
        experiment_type = "heat-stress phenotype and holdase assay"
    data["suggested_experiments"] = [{"experiment_type": experiment_type, "description": experiment}]
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120), encoding="utf-8")


def write_notes(gene: str) -> None:
    info = GENE_INFO[gene]
    evidence = standard_support(gene, info["primary_function"]["id"])
    lines = [
        f"# {gene} notes",
        "",
        "2026-07-10: First-pass cold/heat-shock stress-bucket curation.",
        info["description"],
        "",
        "Primary provenance:",
    ]
    for item in evidence[:8]:
        lines.append(f"- [{item['reference_id']} \"{item['supporting_text']}\"]")
    lines.extend(
        [
            "",
            "Decision: keep the call at the family/domain-supported level. Cold-shock proteins are retained as "
            "nucleic-acid-binding CSD proteins without a specific RNA/DNA target; HSP20-family proteins are treated as "
            "putative unfolded-protein-binding holdases without assigning specific clients.",
        ]
    )
    (GENE_ROOT / gene / f"{gene}-notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_batch_status(path: Path, genes: set[str]) -> None:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    if not rows:
        return
    for row in rows:
        if row["gene"] in genes:
            row["recommended_action"] = "COMPLETED_REUSE_EXISTING"
            row["bucket_status"] = "CURATED"
            row["review_status"] = "PRESENT"
            row["curation_status"] = "CURATED"
            row["asta_research_status"] = "PRESENT"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = list(csv.DictReader(BATCH_TSV.open(encoding="utf-8"), delimiter="\t"))
    genes = {row["gene"] for row in rows}
    for row in rows:
        gene = row["gene"]
        apply_review(gene, row["uniprot_accession"])
        write_notes(gene)
        print(f"Curated {gene}")
    update_batch_status(BATCH_TSV, genes)
    update_batch_status(PARTITION_TSV, genes)


if __name__ == "__main__":
    main()
