#!/usr/bin/env python3
"""First-pass curation for the ppu02025 Gac/Csr/Crp global-regulation bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/global_biofilm_regulation_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "dna_binding": {"id": "GO:0003677", "label": "DNA binding"},
    "dna_binding_tf": {"id": "GO:0003700", "label": "DNA-binding transcription factor activity"},
    "cis_reg_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "tf_activator": {"id": "GO:0001216", "label": "DNA-binding transcription activator activity"},
    "positive_transcription": {"id": "GO:0045893", "label": "positive regulation of DNA-templated transcription"},
    "transcription": {"id": "GO:0006351", "label": "DNA-templated transcription"},
    "transcription_regulation": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "sequence_specific_dna": {"id": "GO:0043565", "label": "sequence-specific DNA binding"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "camp_binding": {"id": "GO:0030552", "label": "cAMP binding"},
    "mrna_binding": {"id": "GO:0048027", "label": "mRNA 5'-UTR binding"},
    "rna_binding": {"id": "GO:0003723", "label": "RNA binding"},
    "negative_translation": {"id": "GO:0045947", "label": "negative regulation of translational initiation"},
    "positive_translation": {"id": "GO:0045948", "label": "positive regulation of translational initiation"},
    "mrna_catabolism": {"id": "GO:0006402", "label": "mRNA catabolic process"},
    "carbohydrate_regulation": {"id": "GO:0006109", "label": "regulation of carbohydrate metabolic process"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "positive_biofilm": {"id": "GO:1900192", "label": "positive regulation of single-species biofilm formation"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
}


CRP = {
    "id": "Q88QR4",
    "description": (
        "crp (PP_0424) encodes a CRP/FNR-family cAMP-responsive DNA-binding transcription "
        "regulator in Pseudomonas putida KT2440. The protein has an N-terminal cyclic "
        "nucleotide-binding domain and a C-terminal CRP-type helix-turn-helix DNA-binding "
        "domain, and CollecTF-derived annotations support transcription cis-regulatory-region "
        "binding and transcription activator activity."
    ),
    "uniprot": "DE   SubName: Full=DNA-binding transcriptional dual regulator",
    "asta": "Protein Description:** SubName: Full=DNA-binding transcriptional dual regulator",
    "extra": [
        "DR   GO; GO:0030552; F:cAMP binding; IEA:UniProtKB-KW.",
        "DR   GO; GO:0001216; F:DNA-binding transcription activator activity; IMP:CollecTF.",
        "DR   GO; GO:0000976; F:transcription cis-regulatory region binding; IMP:CollecTF.",
        "DR   InterPro; IPR000595; cNMP-bd_dom.",
        "DR   InterPro; IPR012318; HTH_CRP.",
        "DR   Pfam; PF00027; cNMP_binding; 1.",
        "DR   Pfam; PF13545; HTH_Crp_2; 1.",
    ],
    "reviews": {
        "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is redundant with the more informative transcription-factor and cis-regulatory-region binding annotations.", None),
        "GO:0003700": ("ACCEPT", "DNA-binding transcription factor activity matches the CRP-type HTH output domain.", None),
        "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is plausible for a soluble transcription regulator but is not the core regulatory function.", None),
        "GO:0006351": ("MARK_AS_OVER_ANNOTATED", "Generic DNA-templated transcription is too broad for a transcription regulator.", None),
        "GO:0006355": ("MARK_AS_OVER_ANNOTATED", "Generic transcription regulation is less informative than the positive regulation and activator terms.", None),
        "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex is consistent with DNA-bound CRP but is a complex state rather than the core molecular function.", None),
        "GO:0043565": ("MARK_AS_OVER_ANNOTATED", "Sequence-specific DNA binding is redundant with transcription cis-regulatory region binding.", None),
        "GO:0045893": ("ACCEPT", "Positive regulation of transcription is supported for this CRP-family activator context.", None),
        "GO:0000976": ("ACCEPT", "Transcription cis-regulatory region binding is directly supported by the CollecTF-derived annotations.", None),
        "GO:0001216": ("ACCEPT", "DNA-binding transcription activator activity is directly supported by the CollecTF-derived annotations.", None),
    },
    "new_annotations": [
        {
            "term": TERMS["camp_binding"],
            "evidence_type": "IEA",
            "original_reference_id": "file:PSEPK/crp/crp-uniprot.txt",
            "qualifier": "enables",
            "summary": "cAMP binding is a key missing molecular-function call for this CRP-family regulator.",
            "reason": "UniProt keyword evidence and the cNMP-binding domain support cAMP binding as part of the core CRP regulatory mechanism.",
        }
    ],
    "core_functions": [
        {
            "description": "CRP/FNR-family cAMP-binding regulatory input through an N-terminal cyclic nucleotide-binding domain.",
            "molecular_function": TERMS["camp_binding"],
        },
        {
            "description": "CRP-family DNA-binding transcription activator that binds cis-regulatory DNA and positively regulates target transcription.",
            "molecular_function": TERMS["tf_activator"],
            "directly_involved_in": [TERMS["positive_transcription"]],
        },
    ],
    "suggested_question": "Which KT2440 biofilm or motility promoters are direct Crp targets under cAMP-responsive conditions?",
    "suggested_experiment": "Perform Crp ChIP-seq or CUT&RUN together with RNA-seq under low- and high-cAMP conditions and validate selected biofilm/motility promoters by reporter assay.",
    "experiment_type": "ChIP-seq and transcriptional reporter assay",
}


CSR_IDS = {
    "csrA__Q88M29": ("Q88M29", "PP_1746", "ECO:0000256"),
    "csrA__Q88G93": ("Q88G93", "PP_3832", "ECO:0000255"),
    "csrA__Q88EJ0": ("Q88EJ0", "PP_4472", "ECO:0000256"),
}


def csr_config(gene: str, accession: str, locus: str, eco: str) -> dict:
    return {
        "id": accession,
        "ordered_locus": locus,
        "description": (
            f"{gene} ({locus}) encodes a CsrA/RsmA-family post-transcriptional regulator in "
            "Pseudomonas putida KT2440. It is a small cytoplasmic mRNA-binding protein predicted "
            "to bind 5-prime UTRs and regulate translation initiation and mRNA stability, placing "
            "it in the Csr/Rsm branch downstream of Gac signaling."
        ),
        "uniprot": "DE   RecName: Full=Translational regulator CsrA",
        "asta": "Protein Description:** RecName: Full=Translational regulator CsrA",
        "extra": [
            "CC   -!- FUNCTION: A key translational regulator that binds mRNA to regulate",
            "CC       translation initiation and/or mRNA stability. Mediates global changes",
            "CC       Usually binds in the 5'-UTR; binding at or near the",
            "CC       Shine-Dalgarno sequence prevents ribosome-binding, repressing",
            "CC       translation, binding elsewhere in the 5'-UTR can activate translation",
            "CC       and/or stabilize the mRNA. Its function is antagonized by small RNA(s).",
            "CC   -!- SUBCELLULAR LOCATION: Cytoplasm",
            "CC   -!- SIMILARITY: Belongs to the CsrA/RsmA family.",
            "DR   InterPro; IPR003751; CsrA.",
            "DR   Pfam; PF02599; CsrA; 1.",
        ],
        "reviews": {
            "GO:0003723": ("MARK_AS_OVER_ANNOTATED", "Generic RNA binding is redundant with the more specific mRNA 5-prime UTR binding term.", None),
            "GO:0005737": ("KEEP_AS_NON_CORE", "Cytoplasm is appropriate for a soluble CsrA/RsmA-family regulator but is not the core function.", None),
            "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is appropriate for a soluble CsrA/RsmA-family regulator but is not the core function.", None),
            "GO:0006109": ("KEEP_AS_NON_CORE", "Carbohydrate-metabolism regulation is a plausible CsrA-family output but is not the core molecular role of this paralog.", None),
            "GO:0006402": ("KEEP_AS_NON_CORE", "mRNA catabolism is a plausible target-dependent output of CsrA/RsmA-family mRNA binding but is less central than translational initiation regulation.", None),
            "GO:0045947": ("ACCEPT", "Negative regulation of translational initiation is a core CsrA/RsmA-family output when binding overlaps the ribosome-binding region.", None),
            "GO:0045948": ("ACCEPT", "Positive regulation of translational initiation is a target-dependent CsrA/RsmA-family output when binding elsewhere in the 5-prime UTR stabilizes or activates translation.", None),
            "GO:0048027": ("ACCEPT", "mRNA 5-prime UTR binding is the most specific existing molecular-function term for this CsrA/RsmA-family regulator.", None),
        },
        "core_functions": [
            {
                "description": "CsrA/RsmA-family mRNA 5-prime UTR-binding regulator of translation initiation.",
                "molecular_function": TERMS["mrna_binding"],
                "directly_involved_in": [TERMS["negative_translation"], TERMS["positive_translation"]],
                "locations": [TERMS["cytosol"]],
            }
        ],
        "suggested_question": f"Which mRNA targets are specific to the {locus} CsrA paralog, and how redundant is it with the other KT2440 CsrA/RsmA-family paralogs?",
        "suggested_experiment": f"Perform tagged {locus} RNA immunoprecipitation followed by sequencing and compare target sets with the other KT2440 CsrA paralogs.",
        "experiment_type": "RIP-seq or CLIP-seq target mapping",
    }


GENES = {"crp": CRP} | {gene: csr_config(gene, *args) for gene, args in CSR_IDS.items()}


ASTA_ONLY = {
    "gacS": ("Q88MC3", "Protein Description:** RecName: Full=histidine kinase"),
    "gacA": ("Q88FJ6", "Protein Description:** RecName: Full=Response regulator GacA"),
}

KNOWN_REFERENCE_TITLES = {
    "PMID:22081386": "Involvement of the global Crp regulator in cyclic AMP-dependent utilization of aromatic amino acids by Pseudomonas putida.",
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
        rows: dict[str, dict[str, str]] = {}
        for row in csv.DictReader(handle, delimiter="\t"):
            rows.setdefault(row["GO TERM"], row)
        return rows


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
        if ref_id in KNOWN_REFERENCE_TITLES:
            ref["title"] = KNOWN_REFERENCE_TITLES[ref_id]


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


def make_new_annotation(gene: str, cfg: dict, spec: dict) -> dict:
    return {
        "term": spec["term"],
        "evidence_type": spec["evidence_type"],
        "original_reference_id": spec["original_reference_id"],
        "qualifier": spec["qualifier"],
        "review": {
            "summary": spec["summary"],
            "action": "NEW",
            "reason": spec["reason"],
            "supported_by": base_support(gene, cfg),
        },
    }


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    aliases = []
    if cfg.get("ordered_locus") and cfg["ordered_locus"] != gene:
        aliases.append(cfg["ordered_locus"])
    if aliases:
        data["aliases"] = aliases
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['id']})", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['id']})", cfg["asta"])
    normalize_go_ref_titles(data)

    existing = []
    new_specs = {spec["term"]["id"]: spec for spec in cfg.get("new_annotations", [])}
    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in cfg["reviews"]:
            if go_id not in new_specs:
                raise KeyError(f"Unhandled annotation {go_id} for {gene}")
            annotation["review"] = make_new_annotation(gene, cfg, new_specs[go_id])["review"]
        else:
            annotation["review"] = make_review(gene, cfg, rows, go_id)
        existing.append(annotation)

    existing_ids = {ann["term"]["id"] for ann in existing}
    for spec in new_specs.values():
        if spec["term"]["id"] not in existing_ids:
            existing.append(make_new_annotation(gene, cfg, spec))
    data["existing_annotations"] = existing

    for core in cfg["core_functions"]:
        core["supported_by"] = base_support(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["suggested_question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["suggested_experiment"], "experiment_type": cfg["experiment_type"]}
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def add_asta_reference(gene: str, accession: str, supporting_text: str) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    ensure_reference(
        data,
        asta_ref(gene),
        f"Asta retrieval report for {gene} ({accession})",
        supporting_text,
    )
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Added Asta reference to {path.relative_to(ROOT)}")


def annoton(
    gene: str,
    label: str,
    role: str,
    function: dict | None = None,
    processes: list[dict] | None = None,
    locations: list[dict] | None = None,
) -> dict:
    node = {
        "id": label.lower()
        .replace(":", "")
        .replace(",", "")
        .replace("'", "")
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [{"preferred_term": term["label"], "term": term} for term in (processes or [])],
        "locations": [{"preferred_term": term["label"], "term": term} for term in (locations or [])],
        "role_description": role,
    }
    if function:
        node["function"] = {"preferred_term": function["label"], "term": function}
    return node


def build_module() -> None:
    module = {
        "id": "MODULE:global_biofilm_regulation_boundary",
        "title": "Global Gac/Csr/Crp biofilm-regulation boundary",
        "description": (
            "Boundary module for the global Gac/Csr/Crp regulatory sub-bucket selected from "
            "KEGG ppu02025 biofilm formation in Pseudomonas putida KT2440. It combines the "
            "GacS/GacA phosphorelay, CsrA/RsmA-family post-transcriptional regulators, and "
            "the CRP-family cAMP-responsive transcription regulator Crp as global regulatory "
            "context rather than a single linear pathway."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv",
                "title": "PSEPK ppu02025 biofilm partition table",
                "statement": "The partition table selects crp, gacS, uvrY/gacA, and three CsrA paralogs as the global Gac/Csr/Crp biofilm-regulation bucket.",
            },
        ]
        + [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": f"The {gene} review supports its global regulatory boundary role.",
            }
            for gene in ["crp", "gacS", "gacA", "csrA__Q88M29", "csrA__Q88G93", "csrA__Q88EJ0"]
        ],
        "notes": (
            "The ppu02025 row names the response regulator as uvrY, while the local review folder is "
            "gacA with uvrY as an alias. The three CsrA/RsmA-family paralogs are retained as distinct "
            "accession-scoped review folders because all three use csrA as the UniProt gene name."
        ),
        "module": {
            "id": "global_biofilm_regulation_boundary",
            "label": "Global Gac/Csr/Crp biofilm-regulation boundary",
            "module_type": "REGULATORY_STEP",
            "concepts": [
                {"preferred_term": term["label"], "term": term}
                for term in [
                    TERMS["phosphorelay"],
                    TERMS["sensor_kinase"],
                    TERMS["response_regulator"],
                    TERMS["dna_binding_tf"],
                    TERMS["tf_activator"],
                    TERMS["camp_binding"],
                    TERMS["mrna_binding"],
                    TERMS["negative_translation"],
                    TERMS["positive_translation"],
                    TERMS["positive_biofilm"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "plasma membrane",
                        "term": TERMS["plasma_membrane"],
                        "description": "GacS is a membrane sensor kinase.",
                    },
                    {
                        "preferred_term": "cytosol",
                        "term": TERMS["cytosol"],
                        "description": "GacA, Crp, and CsrA-family regulators act inside the cell.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "GacS/GacA two-component input",
                    "node": {
                        "id": "gacs_gaca_phosphorelay",
                        "label": "GacS/GacA phosphorelay",
                        "module_type": "REGULATORY_STEP",
                        "description": "Membrane sensor kinase and response-regulator output for Gac/Rsm control.",
                        "annotons": [
                            annoton("gacS", "gacS: membrane phosphorelay sensor kinase", "GacS sensor kinase input.", function=TERMS["sensor_kinase"], processes=[TERMS["phosphorelay"]], locations=[TERMS["plasma_membrane"]]),
                            annoton("gacA", "gacA/uvrY: response-regulator transcriptional activator", "GacA response-regulator output.", function=TERMS["response_regulator"], processes=[TERMS["phosphorelay"], TERMS["positive_biofilm"]]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "CsrA/RsmA post-transcriptional regulators",
                    "node": {
                        "id": "csra_rsma_post_transcriptional_regulators",
                        "label": "CsrA/RsmA post-transcriptional regulators",
                        "module_type": "REGULATORY_STEP",
                        "description": "Small mRNA 5-prime UTR-binding regulators that modulate translation initiation.",
                        "annotons": [
                            annoton("csrA__Q88M29", "csrA__Q88M29: CsrA/RsmA-family regulator", "PP_1746 CsrA-family paralog.", function=TERMS["mrna_binding"], processes=[TERMS["negative_translation"], TERMS["positive_translation"]], locations=[TERMS["cytosol"]]),
                            annoton("csrA__Q88G93", "csrA__Q88G93: CsrA/RsmA-family regulator", "PP_3832 CsrA-family paralog.", function=TERMS["mrna_binding"], processes=[TERMS["negative_translation"], TERMS["positive_translation"]], locations=[TERMS["cytosol"]]),
                            annoton("csrA__Q88EJ0", "csrA__Q88EJ0: CsrA/RsmA-family regulator", "PP_4472 CsrA-family paralog.", function=TERMS["mrna_binding"], processes=[TERMS["negative_translation"], TERMS["positive_translation"]], locations=[TERMS["cytosol"]]),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Crp cAMP-responsive transcription regulator",
                    "node": {
                        "id": "crp_camp_transcription_regulator",
                        "label": "Crp cAMP-responsive transcription regulator",
                        "module_type": "REGULATORY_STEP",
                        "description": "CRP-family cAMP-responsive DNA-binding transcription regulator.",
                        "annotons": [
                            annoton("crp", "crp: cAMP-responsive transcription activator", "CRP-family transcription regulator.", function=TERMS["tf_activator"], processes=[TERMS["positive_transcription"]], locations=[TERMS["cytosol"]]),
                        ],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    for gene, (accession, supporting_text) in ASTA_ONLY.items():
        add_asta_reference(gene, accession, supporting_text)
    build_module()


if __name__ == "__main__":
    main()
