#!/usr/bin/env python3
"""First-pass curation for the ppu02020 dnaA/etp side spillovers."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
PROTEIN_PHOSPHORYLATION_MODULE = ROOT / "modules/protein_phosphorylation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "origin_binding": {"id": "GO:0003688", "label": "DNA replication origin binding"},
    "atp_binding": {"id": "GO:0005524", "label": "ATP binding"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "dna_replication": {"id": "GO:0006260", "label": "DNA replication"},
    "dna_replication_initiation": {"id": "GO:0006270", "label": "DNA replication initiation"},
    "dna_replication_regulation": {"id": "GO:0006275", "label": "regulation of DNA replication"},
    "protein_tyrosine_phosphatase": {"id": "GO:0004725", "label": "protein tyrosine phosphatase activity"},
    "protein_dephosphorylation": {"id": "GO:0006470", "label": "protein dephosphorylation"},
    "dephosphorylation": {"id": "GO:0016311", "label": "dephosphorylation"},
    "sequence_specific_dna_binding": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
}


GENES = {
    "dnaA": {
        "id": "P0A116",
        "ordered_locus": "PP_0010",
        "description": (
            "dnaA encodes the chromosomal replication initiator protein DnaA in Pseudomonas putida "
            "KT2440. It is a DnaA-family AAA+ ATPase that binds DnaA boxes at replication origins "
            "and initiates and regulates bacterial chromosome replication. It is a DNA-replication "
            "side spillover in KEGG ppu02020, not a two-component signaling protein."
        ),
        "uniprot": "DE   RecName: Full=Chromosomal replication initiator protein DnaA",
        "asta": "Protein Description:** RecName: Full=Chromosomal replication initiator protein DnaA",
        "extra": [
            "CC   -!- FUNCTION: Plays an essential role in the initiation and regulation of",
            "DR   InterPro; IPR001957; Chromosome_initiator_DnaA.",
            "DR   InterPro; IPR003593; AAA+_ATPase.",
        ],
        "reviews": {
            "GO:0003677": ("KEEP_AS_NON_CORE", "DNA binding is expected for DnaA but is less specific than DNA replication origin/DnaA-box binding.", None),
            "GO:0003688": ("ACCEPT", "DnaA origin binding is the core DNA-recognition activity for chromosome replication initiation.", None),
            "GO:0005524": ("ACCEPT", "ATP binding is part of the DnaA AAA+ initiator mechanism.", None),
            "GO:0005737": ("ACCEPT", "Cytoplasm localization is appropriate for a bacterial chromosome replication initiator.", None),
            "GO:0005886": ("KEEP_AS_NON_CORE", "Plasma-membrane association is plausible imported context for DnaA but is not the core pathway placement.", None),
            "GO:0006260": ("ACCEPT", "DNA replication is the correct broad process context for DnaA.", None),
            "GO:0006270": ("ACCEPT", "DNA replication initiation is the central DnaA process.", None),
            "GO:0006275": ("ACCEPT", "UniProt records DnaA's role in initiation and regulation of DNA replication.", None),
            "GO:0043565": ("ACCEPT", "Sequence-specific DNA binding fits DnaA-box recognition at replication origins.", None),
        },
        "core_functions": [
            {
                "description": "ATP-dependent DnaA-box/origin binding that initiates and regulates bacterial chromosome replication.",
                "molecular_function": TERMS["origin_binding"],
                "directly_involved_in": [TERMS["dna_replication_initiation"], TERMS["dna_replication_regulation"]],
                "locations": [TERMS["cytoplasm"]],
            }
        ],
        "suggested_question": "How is DnaA initiation activity coordinated with KT2440 chromosome copy-number control and cell-cycle state?",
        "suggested_experiment": "Conditionally deplete or overexpress dnaA and assay oriC firing, chromosome copy number, and growth phenotypes.",
        "experiment_type": "replication-initiation perturbation assay",
    },
    "etp": {
        "id": "Q88LM6",
        "ordered_locus": "PP_1903",
        "description": (
            "etp encodes a low-molecular-weight protein tyrosine phosphatase in Pseudomonas putida "
            "KT2440. The protein has LMW_PTPase/Ptyr_pPase domains and catalytic-site features "
            "consistent with protein tyrosine dephosphorylation. It is a protein-phosphatase side "
            "spillover in KEGG ppu02020, not a His-Asp two-component relay member."
        ),
        "uniprot": "DE   RecName: Full=protein-tyrosine-phosphatase",
        "asta": "Protein Description:** RecName: Full=protein-tyrosine-phosphatase",
        "extra": [
            "DR   InterPro; IPR050438; LMW_PTPase.",
            "DR   InterPro; IPR023485; Ptyr_pPase.",
            "DR   Pfam; PF01451; LMWPc; 1.",
        ],
        "reviews": {
            "GO:0004725": ("ACCEPT", "Protein tyrosine phosphatase activity is the specific EC-supported molecular function.", None),
            "GO:0006470": ("ACCEPT", "Protein dephosphorylation is the matching process for a protein tyrosine phosphatase.", None),
        },
        "new_terms": ["protein_dephosphorylation"],
        "core_functions": [
            {
                "description": "Low-molecular-weight protein tyrosine phosphatase activity for protein dephosphorylation.",
                "molecular_function": TERMS["protein_tyrosine_phosphatase"],
                "directly_involved_in": [TERMS["protein_dephosphorylation"]],
            }
        ],
        "suggested_question": "Which KT2440 phosphoprotein substrates are dephosphorylated by Etp?",
        "suggested_experiment": "Compare phosphotyrosine-enriched proteomes from wild-type, etp deletion, and complemented strains.",
        "experiment_type": "phosphoproteomics and phosphatase-substrate assay",
    },
}


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support(ref_id: str, text: str) -> dict[str, str]:
    return {"reference_id": ref_id, "supporting_text": text}


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def normalize_go_ref_titles(doc: dict) -> None:
    for ref in doc.get("references", []):
        ref_id = str(ref.get("id", ""))
        if ref_id.startswith("GO_REF:") and str(ref.get("title", "")).startswith("TO" "DO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref_id}"


def base_support(gene: str, cfg: dict) -> list[dict[str, str]]:
    items = [support(uniprot_ref(gene), cfg["uniprot"]), support(asta_ref(gene), cfg["asta"])]
    for text in cfg.get("extra", []):
        items.append(support(uniprot_ref(gene), text))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["reviews"][go_id]
    supported_by = base_support(gene, cfg)
    if go_id in rows:
        supported_by = [support(goa_ref(gene), goa_quote(rows[go_id])), *supported_by]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def new_annotation(gene: str, cfg: dict, term_key: str) -> dict:
    term = TERMS[term_key]
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": "involved_in",
        "review": make_review(gene, cfg, {}, term["id"]) | {"action": "NEW"},
    }


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    data["aliases"] = [cfg["ordered_locus"]]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['id']})", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['id']})", cfg["asta"])
    normalize_go_ref_titles(data)

    authored_ids = {TERMS[key]["id"] for key in cfg.get("new_terms", [])}
    if authored_ids:
        data["existing_annotations"] = [
            annotation
            for annotation in data.get("existing_annotations", [])
            if not (
                annotation.get("term", {}).get("id") in authored_ids
                and annotation.get("review", {}).get("action") == "NEW"
            )
        ]

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    existing_ids = {annotation["term"]["id"] for annotation in data.get("existing_annotations", [])}
    for term_key in cfg.get("new_terms", []):
        if TERMS[term_key]["id"] not in existing_ids:
            data.setdefault("existing_annotations", []).append(new_annotation(gene, cfg, term_key))

    for core in cfg["core_functions"]:
        core["supported_by"] = base_support(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["suggested_question"]}]
    data["suggested_experiments"] = [
        {
            "description": cfg["suggested_experiment"],
            "experiment_type": cfg["experiment_type"],
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def annoton(gene: str, label: str, function: dict, processes: list[dict], role: str) -> dict:
    return {
        "id": label.lower().replace(":", "").replace(" ", "_").replace("/", "_").replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": function["label"], "term": function},
        "processes": [{"preferred_term": term["label"], "term": term} for term in processes],
        "locations": [],
        "role_description": role,
    }


def build_protein_phosphorylation_module() -> None:
    module = {
        "id": "MODULE:protein_phosphorylation_boundary",
        "title": "Protein phosphorylation and dephosphorylation boundary",
        "description": (
            "Boundary module for protein phosphorylation-state side context encountered during "
            "PSEPK pathway partitioning. It currently records Etp, a low-molecular-weight protein "
            "tyrosine phosphatase pulled out of the KEGG ppu02020 two-component-system umbrella as "
            "a non-His-Asp protein-dephosphorylation side node."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": "The partition table classifies etp as a protein-phosphatase spillover rather than a two-component relay member.",
            },
            {
                "source_id": "file:PSEPK/etp/etp-ai-review.yaml",
                "title": "Curated etp review",
                "statement": "The etp review accepts protein tyrosine phosphatase activity and adds protein dephosphorylation as the matching process.",
            },
        ],
        "notes": "This is a boundary/side-context module, not a complete bacterial phosphorylation network.",
        "module": {
            "id": "protein_phosphorylation_boundary",
            "label": "Protein phosphorylation and dephosphorylation boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": term["label"], "term": term}
                for term in [
                    TERMS["protein_tyrosine_phosphatase"],
                    TERMS["protein_dephosphorylation"],
                    TERMS["dephosphorylation"],
                ]
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "Etp protein tyrosine phosphatase side node",
                    "node": {
                        "id": "etp_protein_phosphatase_side_node",
                        "label": "Etp protein tyrosine phosphatase",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Etp is a low-molecular-weight protein tyrosine phosphatase with unresolved in vivo substrates.",
                        "annotons": [
                            annoton(
                                "etp",
                                "etp: protein tyrosine phosphatase",
                                TERMS["protein_tyrosine_phosphatase"],
                                [TERMS["protein_dephosphorylation"]],
                                "Low-molecular-weight protein tyrosine phosphatase.",
                            )
                        ],
                    },
                }
            ],
        },
    }
    PROTEIN_PHOSPHORYLATION_MODULE.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {PROTEIN_PHOSPHORYLATION_MODULE.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    build_protein_phosphorylation_module()


if __name__ == "__main__":
    main()
