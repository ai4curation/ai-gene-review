#!/usr/bin/env python3
"""First-pass curation for ppu02024 QseBC-like two-component genes."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GENES = {
    "PP_2713": {
        "accession": "Q88JD6",
        "kind": "regulator",
        "description": (
            "PP_2713 encodes an OmpR/PhoB-family DNA-binding response regulator in "
            "Pseudomonas putida KT2440. It has a CheY-like receiver domain and a "
            "winged-helix DNA-binding domain, supporting a two-component "
            "phosphorelay regulator role with unresolved signal and target genes."
        ),
        "product_quote": "DE   SubName: Full=DNA-binding response regulator",
        "domain_quote": "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        "dna_domain_quote": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
        "asta_quote": "protein_description: 'SubName: Full=DNA-binding response regulator",
        "location": ("GO:0005829", "cytosol"),
        "dna_term": ("GO:0000976", "transcription cis-regulatory region binding"),
        "reg_process": ("GO:0006355", "regulation of DNA-templated transcription"),
    },
    "kdpE": {
        "accession": "Q88FE0",
        "kind": "regulator",
        "description": (
            "kdpE encodes a KdpE-like two-component DNA-binding response activator "
            "in Pseudomonas putida KT2440. It combines a response-regulator receiver "
            "domain with an OmpR/PhoB-type DNA-binding domain, consistent with "
            "phosphorelay-dependent transcriptional activation; the exact KT2440 "
            "signal branch represented in the ppu02024 umbrella remains unresolved."
        ),
        "product_quote": "DE   SubName: Full=Two-component system DNA-binding response activator KdpE",
        "domain_quote": "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        "dna_domain_quote": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
        "asta_quote": "protein_description: 'SubName: Full=Two-component system DNA-binding response activator",
        "location": ("GO:0005737", "cytoplasm"),
        "dna_term": ("GO:0000987", "cis-regulatory region sequence-specific DNA binding"),
        "reg_process": ("GO:0045893", "positive regulation of DNA-templated transcription"),
    },
    "qseB": {
        "accession": "Q88F73",
        "kind": "regulator",
        "description": (
            "qseB encodes a QseB-like two-component DNA-binding transcriptional "
            "activator in Pseudomonas putida KT2440. It has a response-regulator "
            "receiver domain and an OmpR/PhoB-type DNA-binding domain, supporting "
            "phosphorelay-dependent transcriptional regulation rather than direct "
            "quorum-signal synthesis or reception."
        ),
        "product_quote": "DE   SubName: Full=Two component system DNA-binding transcriptional activator QseB",
        "domain_quote": "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
        "dna_domain_quote": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
        "asta_quote": "protein_description: 'SubName: Full=Two component system DNA-binding transcriptional",
        "location": ("GO:0005737", "cytoplasm"),
        "dna_term": ("GO:0000976", "transcription cis-regulatory region binding"),
        "reg_process": ("GO:0006355", "regulation of DNA-templated transcription"),
    },
    "PP_2714": {
        "accession": "Q88JD5",
        "kind": "kinase",
        "description": (
            "PP_2714 encodes a predicted membrane histidine sensor kinase in "
            "Pseudomonas putida KT2440. Its HAMP, HisKA, and HATPase domains "
            "support a two-component phosphorelay sensor role, probably paired "
            "with the adjacent DNA-binding response regulator PP_2713."
        ),
        "product_quote": "DE   RecName: Full=histidine kinase",
        "domain_quote": "DR   InterPro; IPR005467; His_kinase_dom.",
        "sensor_quote": "DR   InterPro; IPR050428; TCS_sensor_his_kinase.",
        "asta_quote": "protein_description: 'RecName: Full=histidine kinase",
    },
    "PP_4224": {
        "accession": "Q88F74",
        "kind": "kinase",
        "description": (
            "PP_4224 encodes a predicted membrane histidine sensor kinase in "
            "Pseudomonas putida KT2440. Its HAMP, HisKA, and HATPase domains "
            "support a two-component phosphorelay sensor role, probably paired "
            "with the adjacent QseB-like response regulator qseB."
        ),
        "product_quote": "DE   RecName: Full=histidine kinase",
        "domain_quote": "DR   InterPro; IPR005467; His_kinase_dom.",
        "sensor_quote": "DR   InterPro; IPR050428; TCS_sensor_his_kinase.",
        "asta_quote": "protein_description: 'RecName: Full=histidine kinase",
    },
}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping",
    "GO_REF:0000104": "Automatic assignment of GO terms using UniRule and SAAS rules",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def file_ref(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def review(summary: str, action: str, reason: str, supported_by: list[dict[str, str]]) -> dict:
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_references(data: dict, gene: str, cfg: dict) -> None:
    refs = {entry["id"]: entry for entry in data.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        refs.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})

    findings = [
        {
            "statement": "UniProt product naming supports the first-pass two-component-system assignment.",
            "supporting_text": cfg["product_quote"],
        },
        {
            "statement": "Conserved domain annotation supports the phosphorelay role.",
            "supporting_text": cfg["domain_quote"],
        },
    ]
    if cfg["kind"] == "regulator":
        findings.append(
            {
                "statement": "The OmpR/PhoB DNA-binding domain supports transcription-regulator context.",
                "supporting_text": cfg["dna_domain_quote"],
            }
        )
    else:
        findings.append(
            {
                "statement": "The sensor histidine kinase family annotation supports a membrane sensor role.",
                "supporting_text": cfg["sensor_quote"],
            }
        )
    refs[file_ref(gene, "goa.tsv")] = {
        "id": file_ref(gene, "goa.tsv"),
        "title": f"QuickGO/GOA annotation table for {gene} in Pseudomonas putida KT2440",
        "findings": [],
    }
    refs[file_ref(gene, "uniprot.txt")] = {
        "id": file_ref(gene, "uniprot.txt"),
        "title": f"UniProt record {cfg['accession']} for {gene} in Pseudomonas putida KT2440",
        "findings": findings,
    }
    refs[file_ref(gene, "deep-research-asta.md")] = {
        "id": file_ref(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "Asta retrieval was checked for this first pass and recapitulates the UniProt/domain assignment.",
                "supporting_text": cfg["asta_quote"],
            }
        ],
    }
    data["references"] = list(refs.values())


def support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> list[dict[str, str]]:
    evidence = [
        ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
        ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
    ]
    if cfg["kind"] == "regulator":
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["dna_domain_quote"]))
    else:
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["sensor_quote"]))
    return evidence


def regulator_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0000156":
        return review(
            "Phosphorelay response-regulator activity is appropriate for the CheY-like receiver domain.",
            "ACCEPT",
            "The protein is a two-component response regulator with receiver-domain and OmpR/PhoB-family DNA-binding evidence.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0000160":
        return review(
            "Phosphorelay signal transduction is the correct process context for this response regulator.",
            "ACCEPT",
            "The receiver domain supports His-Asp phosphorelay signaling; the upstream signal and partner specificity remain unresolved in this first pass.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0000976":
        action = "KEEP_AS_NON_CORE" if "GO:0000987" in rows else "ACCEPT"
        reason = (
            "The more specific GO:0000987 sequence-specific cis-regulatory binding term is also present, so this broader binding term is retained as non-core."
            if action == "KEEP_AS_NON_CORE"
            else "The OmpR/PhoB-type DNA-binding domain supports cis-regulatory DNA binding by this response regulator."
        )
        return review(
            "Cis-regulatory region binding is consistent with the DNA-binding response-regulator architecture.",
            action,
            reason,
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0000987":
        return review(
            "Sequence-specific cis-regulatory DNA binding is appropriate for the KdpE-like response activator.",
            "ACCEPT",
            "The OmpR/PhoB-type DNA-binding domain and KdpE response-activator product description support specific regulatory DNA binding.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0003677":
        return review(
            "Generic DNA binding is true but less informative than the cis-regulatory DNA-binding terms.",
            "MARK_AS_OVER_ANNOTATED",
            "The protein is a DNA-binding response regulator, but GO:0000976 or GO:0000987 captures the regulatory binding role more precisely.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0005737":
        return review(
            "Cytoplasm localization is appropriate for this soluble response regulator.",
            "ACCEPT",
            "UniProt subcellular-location mapping places the response regulator in the cytoplasm.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), "CC   -!- SUBCELLULAR LOCATION: Cytoplasm"),
            ],
        )
    if go_id == "GO:0005829":
        action = "KEEP_AS_NON_CORE" if "GO:0005737" in rows else "ACCEPT"
        reason = (
            "Cytosol is compatible with the response-regulator role, but the UniProt cytoplasm annotation is used as the core location."
            if action == "KEEP_AS_NON_CORE"
            else "Cytosol localization is compatible with a soluble bacterial response regulator."
        )
        return review(
            "Cytosol localization is compatible with the soluble response-regulator role.",
            action,
            reason,
            [ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id]))],
        )
    if go_id == "GO:0006355":
        return review(
            "Regulation of DNA-templated transcription is appropriate for an OmpR/PhoB-family DNA-binding response regulator.",
            "ACCEPT",
            "The response-regulator receiver domain and regulatory DNA-binding domain support phosphorelay-dependent transcriptional regulation.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0032993":
        return review(
            "Protein-DNA complex membership is plausible but should not be treated as the stable core function.",
            "KEEP_AS_NON_CORE",
            "DNA-bound response regulators form protein-DNA complexes transiently during transcriptional regulation; molecular activity and process terms better capture the core function.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0042802":
        return review(
            "Identical protein binding is too generic for the core KdpE-like response-regulator function.",
            "MARK_AS_OVER_ANNOTATED",
            "Response-regulator dimerization may occur, but this generic binding term is less informative than phosphorelay response-regulator activity and regulatory DNA binding.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0045893":
        return review(
            "Positive regulation of DNA-templated transcription is appropriate for the KdpE response activator annotation.",
            "ACCEPT",
            "The KdpE product description and DNA-binding response-regulator domains support transcriptional activation, while the exact KT2440 target regulon remains unresolved.",
            support(gene, cfg, rows, go_id),
        )
    raise KeyError(f"Unhandled regulator term {go_id} for {gene}")


def kinase_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0000155":
        return review(
            "Phosphorelay sensor kinase activity is appropriate for this membrane histidine kinase.",
            "ACCEPT",
            "The HAMP/HisKA/HATPase sensor-kinase architecture supports a two-component sensor kinase role.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0000160":
        return review(
            "Phosphorelay signal transduction is the correct biological-process context for this sensor kinase.",
            "ACCEPT",
            "The protein has two-component sensor histidine kinase domains and is expected to feed a phosphorelay response-regulator branch.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0004673":
        return review(
            "Protein histidine kinase activity is appropriate for the EC 2.7.13.3 histidine kinase annotation.",
            "ACCEPT",
            "The UniProt record and GOA EC mapping support ATP-dependent phosphorylation of a histidine residue.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for the predicted membrane sensor kinase.",
            "ACCEPT",
            "The protein carries multiple transmembrane segments and membrane sensor-kinase architecture.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), "Multi-pass membrane protein"),
                ref(file_ref(gene, "uniprot.txt"), "FT   TRANSMEM"),
            ],
        )
    if go_id == "GO:0007165":
        return review(
            "Generic signal transduction is correct but less informative than phosphorelay signal transduction.",
            "KEEP_AS_NON_CORE",
            "The protein is a sensor kinase in a phosphorelay pathway; GO:0000160 captures that process more specifically.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0016020":
        return review(
            "Generic membrane localization is supported but less informative than plasma membrane.",
            "MARK_AS_OVER_ANNOTATED",
            "GOA also carries GO:0005886 plasma membrane, which better captures the bacterial membrane sensor localization.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0005886"])),
            ],
        )
    if go_id in {"GO:0016301", "GO:0016740", "GO:0016772"}:
        return review(
            "The generic kinase/transferase term is less informative than phosphorelay sensor kinase and protein histidine kinase activity.",
            "MARK_AS_OVER_ANNOTATED",
            "The specific two-component histidine kinase annotations capture the molecular role more accurately than this broad enzyme-class term.",
            support(gene, cfg, rows, go_id),
        )
    raise KeyError(f"Unhandled kinase term {go_id} for {gene}")


def core_functions(gene: str, cfg: dict) -> list[dict]:
    if cfg["kind"] == "kinase":
        return [
            {
                "description": "Membrane sensor histidine kinase for two-component phosphorelay signaling.",
                "molecular_function": {
                    "id": "GO:0000155",
                    "label": "phosphorelay sensor kinase activity",
                },
                "directly_involved_in": [
                    {"id": "GO:0000160", "label": "phosphorelay signal transduction system"}
                ],
                "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
                "supported_by": [
                    ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["sensor_quote"]),
                    ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
                ],
            }
        ]

    loc_id, loc_label = cfg["location"]
    dna_id, dna_label = cfg["dna_term"]
    reg_id, reg_label = cfg["reg_process"]
    return [
        {
            "description": "Response regulator receiver activity in a two-component phosphorelay.",
            "molecular_function": {
                "id": "GO:0000156",
                "label": "phosphorelay response regulator activity",
            },
            "directly_involved_in": [
                {"id": "GO:0000160", "label": "phosphorelay signal transduction system"}
            ],
            "locations": [{"id": loc_id, "label": loc_label}],
            "supported_by": [
                ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
            ],
        },
        {
            "description": "DNA-binding transcriptional regulation by an OmpR/PhoB-family response regulator.",
            "molecular_function": {"id": dna_id, "label": dna_label},
            "directly_involved_in": [{"id": reg_id, "label": reg_label}],
            "locations": [{"id": loc_id, "label": loc_label}],
            "supported_by": [
                ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["dna_domain_quote"]),
                ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
            ],
        },
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    data["description"] = cfg["description"]
    ensure_references(data, gene, cfg)

    reviewer = kinase_review if cfg["kind"] == "kinase" else regulator_review
    for annotation in data["existing_annotations"]:
        annotation["review"] = reviewer(gene, cfg, rows, annotation["term"]["id"])

    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": (
                f"What signal and target regulon define the {gene} two-component branch in KT2440, and is it linked to quorum-adjacent behavior or another stress/transport pathway?"
            )
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": (
                f"Construct {gene} deletion and complemented strains, profile transcriptional changes under candidate stress and community-growth conditions, and test phosphotransfer or DNA binding to candidate promoters."
            ),
            "experiment_type": "regulon profiling and two-component signaling assay",
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
