#!/usr/bin/env python3
"""First-pass curation for regulation-bucket two-component proteins."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
BATCH_TSV = (
    ROOT
    / "projects"
    / "P_PUTIDA"
    / "batches"
    / "module_regulation_signal_transduction_two_component_sensors_response_regulators.tsv"
)
MODULE_PATH = ROOT / "modules" / "orphan_two_component_regulators_boundary.yaml"
SPECIES = "PSEPK"

EXISTING_CURATED = {"colR"}

SENSOR_GENES = {
    "PP_0270",
    "PP_0409",
    "PP_0769",
    "colS",
    "PP_1013",
    "PP_1350",
    "PP_2127",
    "PP_2348",
    "PP_2354",
    "PP_2402",
    "yiaZ",
    "PP_2906",
    "PP_2944",
    "PP_3371",
    "PP_3420",
    "PP_3421",
    "PP_3728",
    "PP_3761",
    "PP_3968",
    "PP_4505",
    "PP_4695",
}

DNA_BINDING_RESPONSE_GENES = {
    "gltR-I",
    "colR",
    "gltR-II",
    "PP_1635",
    "PP_2126",
    "PP_2165",
    "PP_2347",
    "agmR",
    "exaE",
    "PP_2907",
    "PP_3419",
    "PP_3454",
    "PP_3551",
    "aruR",
    "PP_5241",
}

RECEIVER_ONLY_GENES = {
    "PP_0215",
    "PP_0355",
    "PP_0768",
    "PP_2355",
    "PP_2942",
    "PP_3484",
    "PP_3762",
    "PP_3833",
    "PP_3969",
    "PP_5240",
    "PP_5324",
    "PP_5471",
}

NEW_PROMOTER_BINDING_GENES = {"PP_1635", "agmR", "PP_3551", "PP_5241"}
NEW_SENSOR_KINASE_GENES = {"PP_2944"}
NEW_RESPONSE_REGULATOR_GENES = (DNA_BINDING_RESPONSE_GENES | RECEIVER_ONLY_GENES) - EXISTING_CURATED


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERMS = {
    "GO:0000155": term("GO:0000155", "phosphorelay sensor kinase activity"),
    "GO:0000156": term("GO:0000156", "phosphorelay response regulator activity"),
    "GO:0000160": term("GO:0000160", "phosphorelay signal transduction system"),
    "GO:0000166": term("GO:0000166", "nucleotide binding"),
    "GO:0000976": term("GO:0000976", "transcription cis-regulatory region binding"),
    "GO:0001216": term("GO:0001216", "DNA-binding transcription activator activity"),
    "GO:0001217": term("GO:0001217", "DNA-binding transcription repressor activity"),
    "GO:0003677": term("GO:0003677", "DNA binding"),
    "GO:0004673": term("GO:0004673", "protein histidine kinase activity"),
    "GO:0005524": term("GO:0005524", "ATP binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0005886": term("GO:0005886", "plasma membrane"),
    "GO:0006351": term("GO:0006351", "DNA-templated transcription"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0007165": term("GO:0007165", "signal transduction"),
    "GO:0007234": term("GO:0007234", "osmosensory signaling via phosphorelay pathway"),
    "GO:0008081": term("GO:0008081", "phosphoric diester hydrolase activity"),
    "GO:0009927": term("GO:0009927", "histidine phosphotransfer kinase activity"),
    "GO:0016020": term("GO:0016020", "membrane"),
    "GO:0016301": term("GO:0016301", "kinase activity"),
    "GO:0016740": term("GO:0016740", "transferase activity"),
    "GO:0016772": term("GO:0016772", "transferase activity, transferring phosphorus-containing groups"),
    "GO:0022857": term("GO:0022857", "transmembrane transporter activity"),
    "GO:0030295": term("GO:0030295", "protein kinase activator activity"),
    "GO:0032993": term("GO:0032993", "protein-DNA complex"),
    "GO:0043565": term("GO:0043565", "sequence-specific DNA binding"),
    "GO:0045892": term("GO:0045892", "negative regulation of DNA-templated transcription"),
    "GO:0045893": term("GO:0045893", "positive regulation of DNA-templated transcription"),
    "GO:0046983": term("GO:0046983", "protein dimerization activity"),
    "GO:0055085": term("GO:0055085", "transmembrane transport"),
}

GENERIC_KINASE_PARENT_TERMS = {"GO:0016301", "GO:0016740", "GO:0016772"}
LOCATION_TERMS = {"GO:0005737", "GO:0005829", "GO:0005886", "GO:0016020"}
ATP_BINDING_TERMS = {"GO:0000166", "GO:0005524"}
TRANSPORTER_SIDE_TERMS = {"GO:0022857", "GO:0055085"}


def read_batch_rows() -> dict[str, dict[str, str]]:
    with BATCH_TSV.open(encoding="utf-8") as handle:
        return {row["gene"]: row for row in csv.DictReader(handle, delimiter="\t")}


BATCH_ROWS = read_batch_rows()
GENES = list(BATCH_ROWS)


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8").splitlines()


def first_line(path: Path, *needles: str) -> str | None:
    for line in lines(path):
        if all(needle in line for needle in needles):
            return line.strip()
    return None


def support(ref_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": ref_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item["supporting_text"] and item not in items:
        items.append(item)


def goa_rows(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "goa.tsv")
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def goa_ids(gene: str) -> set[str]:
    return {row["GO TERM"] for row in goa_rows(gene) if row.get("GO TERM")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def matching_goa_row(gene: str, annotation: dict) -> dict[str, str] | None:
    go_id = annotation.get("term", {}).get("id")
    evidence = annotation.get("evidence_type")
    reference = annotation.get("original_reference_id")
    for row in goa_rows(gene):
        if (
            row.get("GO TERM") == go_id
            and row.get("GO EVIDENCE CODE") == evidence
            and row.get("REFERENCE") == reference
        ):
            return row
    for row in goa_rows(gene):
        if row.get("GO TERM") == go_id:
            return row
    return None


def first_goa_support(gene: str, go_id: str) -> dict[str, str] | None:
    for row in goa_rows(gene):
        if row.get("GO TERM") == go_id:
            return support(file_id(gene, "goa.tsv"), goa_quote(row))
    return None


def uniprot_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "uniprot.txt")
    items: list[dict[str, str]] = []
    for needle in ("DE   RecName:", "DE   SubName:", "GN   Name=", "GN   OrderedLocusNames="):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "uniprot.txt"), line))
            if needle.startswith("DE"):
                break
    for line in lines(path):
        if (
            line.startswith("DR   InterPro;")
            or line.startswith("DR   Pfam;")
            or line.startswith("DR   NCBIfam;")
            or line.startswith("DR   CDD;")
            or line.startswith("FT   DOMAIN")
            or line.startswith("FT                   /note=")
            or line.startswith("CC   -!- FUNCTION:")
            or line.startswith("KW   DNA-binding")
            or line.startswith("KW   Transcription")
            or line.startswith("KW   Transcription regulation")
            or line.startswith("KW   Kinase")
            or line.startswith("KW   Transferase")
            or line.startswith("KW   Two-component regulatory system")
            or line.startswith("KW   Membrane")
            or line.startswith("KW   Cell membrane")
            or line.startswith("KW   Cell inner membrane")
        ):
            add_support(items, support(file_id(gene, "uniprot.txt"), line.strip()))
        if len(items) >= 16:
            break
    return items


def asta_support_lines(gene: str) -> list[dict[str, str]]:
    path = gene_file(gene, "deep-research-asta.md")
    items: list[dict[str, str]] = []
    for needle in ("protein_description:", "**Protein Description:**", "- **Protein Description:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
            break
    for needle in ("protein_family:", "protein_domains:", "- **Protein Family:**", "- **Key Domains:**"):
        line = first_line(path, needle)
        if line:
            add_support(items, support(file_id(gene, "deep-research-asta.md"), line))
    return items


def evidence_for(gene: str, go_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if go_id:
        add_support(items, first_goa_support(gene, go_id))
    for item in uniprot_support_lines(gene):
        add_support(items, item)
    for item in asta_support_lines(gene):
        add_support(items, item)
    return items


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
        if ref_id.startswith("GO_REF:") and str(ref.get("title", "")).startswith("TODO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref_id}"


def role_class(gene: str) -> str:
    if gene in SENSOR_GENES:
        return "sensor"
    if gene in DNA_BINDING_RESPONSE_GENES:
        return "dna_response"
    if gene in RECEIVER_ONLY_GENES:
        return "receiver"
    raise KeyError(gene)


def product_name(gene: str) -> str:
    return BATCH_ROWS[gene]["protein_name"]


def description_for(gene: str) -> str:
    product = product_name(gene)
    if gene == "colS":
        return (
            "colS encodes the predicted sensor histidine kinase partner of the ColRS two-component "
            "system in Pseudomonas putida KT2440. Its histidine kinase and membrane-associated "
            "sensor architecture support a phosphorelay input role upstream of response-regulator "
            "control of envelope and metal-stress physiology."
        )
    if gene == "PP_2942":
        return (
            "PP_2942 encodes a CheY-like receiver-domain response regulator with an HD-GYP "
            "phosphodiesterase-like output domain in Pseudomonas putida KT2440. The architecture "
            "places it at the interface of two-component signaling and cyclic-di-GMP turnover, but "
            "its activating signal, partner proteins, and physiological substrate remain unresolved."
        )
    if gene == "PP_3419":
        return (
            "PP_3419 encodes a predicted sigma-54-dependent transcriptional regulator with a "
            "CheY-like receiver domain, AAA+ ATPase module, and HTH/Fis DNA-binding output in "
            "Pseudomonas putida KT2440. The domain architecture supports phosphorelay-modulated "
            "transcriptional regulation, but the upstream sensor and target regulon are unresolved."
        )
    if gene == "PP_4695":
        return (
            "PP_4695 encodes a predicted membrane histidine kinase with PAS sensory, "
            "sodium:solute-symporter-like, HisKA, and HATPase domains in Pseudomonas putida KT2440. "
            "The best-supported conserved role is two-component sensor kinase signaling, while any "
            "transport output or sensed ligand remains unresolved."
        )
    if role_class(gene) == "sensor":
        return (
            f"{gene} encodes a predicted sensor histidine kinase in Pseudomonas putida KT2440. "
            "Histidine kinase catalytic domains and, for many family members, membrane or sensory "
            "domains support a two-component phosphorelay role that detects an input cue and passes "
            "phosphate to a response regulator. The specific cue and cognate response regulator are "
            "not established from the current annotations."
        )
    if role_class(gene) == "dna_response":
        return (
            f"{gene} encodes a predicted DNA-binding response regulator in Pseudomonas putida KT2440. "
            "A CheY-like receiver domain and a helix-turn-helix output domain support a "
            "phosphorelay-dependent transcriptional regulatory role, with the upstream sensor, "
            "input signal, and target regulon unresolved."
        )
    return (
        f"{gene} encodes a predicted CheY-like receiver-domain response regulator in Pseudomonas "
        "putida KT2440. The sequence supports a two-component phosphorelay response-regulator role, "
        "but no specific output domain, input signal, or downstream pathway has been established."
    )


def review_text(gene: str, go_id: str) -> tuple[str, str, str]:
    cls = role_class(gene)
    if go_id == "GO:0000155":
        return (
            "ACCEPT",
            "Sensor histidine kinase activity is the supported core molecular function.",
            "The UniProt/Asta product and HisKA/HATPase domain evidence support a two-component sensor histidine kinase role.",
        )
    if go_id == "GO:0000156":
        if cls == "sensor":
            return (
                "KEEP_AS_NON_CORE",
                "Receiver-domain response-regulator activity is plausible as a secondary domain-level feature of this hybrid sensor kinase.",
                "The protein is primarily annotated as a histidine kinase; the receiver annotation is retained as non-core hybrid-phosphorelay context.",
            )
        return (
            "ACCEPT",
            "Phosphorelay response-regulator activity is the supported core molecular function.",
            "The CheY-like receiver-domain evidence supports a two-component response-regulator role.",
        )
    if go_id == "GO:0000160":
        return (
            "ACCEPT",
            "Phosphorelay signal transduction is the appropriate process context for this two-component protein.",
            "The product and domain evidence support participation in a bacterial His-Asp phosphorelay.",
        )
    if go_id == "GO:0000976":
        return (
            "ACCEPT",
            "Promoter or cis-regulatory-region binding fits the DNA-binding response-regulator output domain.",
            "The receiver plus OmpR/PhoB, LuxR/GerE, or HTH/Fis output architecture supports promoter-directed transcriptional regulation.",
        )
    if go_id == "GO:0003677":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "Generic DNA binding is less informative than response-regulator promoter-binding or transcription-regulator terms.",
            "The protein is a DNA-binding response regulator, so the broad DNA-binding parent term should not be treated as the main function.",
        )
    if go_id == "GO:0004673":
        return (
            "ACCEPT",
            "Protein histidine kinase activity is the specific catalytic activity of the sensor kinase domain.",
            "HisKA and HATPase domain evidence supports histidine autokinase activity.",
        )
    if go_id in ATP_BINDING_TERMS:
        return (
            "KEEP_AS_NON_CORE",
            "Nucleotide or ATP binding is expected for the kinase or sigma-54 activator domain but is not the most informative functional assignment.",
            "This binding annotation is retained as domain/cofactor context while the core role is captured by phosphorelay or transcriptional regulatory terms.",
        )
    if go_id in LOCATION_TERMS:
        return (
            "KEEP_AS_NON_CORE",
            "The localization is plausible but secondary to the two-component signaling role.",
            "Keep the cellular-location annotation as context rather than treating it as the core function of the gene product.",
        )
    if go_id == "GO:0006351":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "DNA-templated transcription is too broad for a response-regulator output.",
            "The more informative process is regulation of DNA-templated transcription by a response-regulator DNA-binding domain.",
        )
    if go_id == "GO:0006355":
        if cls == "sensor":
            return (
                "KEEP_AS_NON_CORE",
                "The sensor kinase can influence transcription through its response regulator, but this is indirect pathway context.",
                "The core molecular role remains sensor histidine kinase activity rather than direct transcriptional regulation.",
            )
        return (
            "ACCEPT",
            "Regulation of DNA-templated transcription fits the DNA-binding response-regulator output.",
            "The receiver and HTH-family output domains support phosphorelay-dependent transcriptional regulation.",
        )
    if go_id == "GO:0007165":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "Generic signal transduction is less informative than two-component phosphorelay signaling.",
            "The family/domain evidence supports the more specific phosphorelay signal transduction context.",
        )
    if go_id == "GO:0007234":
        return (
            "MARK_AS_OVER_ANNOTATED",
            "The osmosensory pathway label is more specific than the available evidence supports for this KT2440 protein.",
            "Retain generic two-component phosphorelay signaling, but do not infer an osmosensory cue from family propagation alone.",
        )
    if go_id == "GO:0008081":
        return (
            "KEEP_AS_NON_CORE",
            "The HD-GYP domain supports a phosphodiesterase-like side activity, but the in vivo substrate and regulatory output are unresolved.",
            "The annotation is retained as non-core catalytic context pending evidence for cyclic-di-GMP or related substrate turnover.",
        )
    if go_id == "GO:0009927":
        return (
            "ACCEPT",
            "Histidine phosphotransfer activity is compatible with a multidomain two-component sensor protein.",
            "The sensor kinase architecture includes phosphorelay domains that support histidine phosphotransfer context.",
        )
    if go_id in GENERIC_KINASE_PARENT_TERMS:
        return (
            "MARK_AS_OVER_ANNOTATED",
            "This parent catalytic term is less informative than protein histidine kinase or phosphorelay sensor kinase activity.",
            "The HisKA/HATPase architecture supports the more specific two-component sensor kinase function.",
        )
    if go_id in TRANSPORTER_SIDE_TERMS:
        return (
            "MARK_AS_OVER_ANNOTATED",
            "The transporter-like region does not establish a core transmembrane transport function for this histidine kinase.",
            "The protein is best curated as a sensor histidine kinase; any transport role or substrate remains unresolved.",
        )
    if go_id == "GO:0030295":
        return (
            "KEEP_AS_NON_CORE",
            "Protein kinase activator activity is retained only as secondary regulatory context for the hybrid kinase architecture.",
            "The direct supported molecular role remains the histidine kinase/phosphorelay machinery.",
        )
    if go_id == "GO:0032993":
        return (
            "KEEP_AS_NON_CORE",
            "Protein-DNA complex membership is plausible for DNA-bound response regulators but is not the core molecular role.",
            "Promoter binding and response-regulator activity capture the functional role more directly.",
        )
    if go_id == "GO:0043565":
        return (
            "ACCEPT",
            "Sequence-specific DNA binding fits the HTH/Fis output domain of the sigma-54 regulator.",
            "The sigma-54 enhancer-binding regulator architecture supports DNA-binding transcriptional regulation.",
        )
    if go_id == "GO:0046983":
        return (
            "KEEP_AS_NON_CORE",
            "Dimerization is plausible for sensor-kinase signaling but is secondary to the phosphorelay catalytic role.",
            "Keep the annotation as structural context rather than the main functional assignment.",
        )
    raise KeyError(f"Unhandled GO term {go_id} for {gene}")


def make_review(gene: str, annotation: dict) -> dict:
    go_id = annotation["term"]["id"]
    action, summary, reason = review_text(gene, go_id)
    items: list[dict[str, str]] = []
    row = matching_goa_row(gene, annotation)
    if row:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_quote(row)))
    for item in evidence_for(gene):
        add_support(items, item)
    return {"summary": summary, "action": action, "reason": reason, "supported_by": items}


def new_annotation(gene: str, term_id: str, qualifier: str, summary: str, reason: str) -> dict:
    return {
        "term": TERMS[term_id],
        "evidence_type": "IEA",
        "original_reference_id": file_id(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": evidence_for(gene),
        },
    }


def remove_authored_new_annotations(data: dict) -> None:
    authored_ids = {"GO:0000155", "GO:0000156", "GO:0000976"}
    data["existing_annotations"] = [
        annotation
        for annotation in data.get("existing_annotations", [])
        if not (
            annotation.get("term", {}).get("id") in authored_ids
            and annotation.get("review", {}).get("action") == "NEW"
        )
    ]


def add_needed_new_annotations(gene: str, data: dict) -> None:
    existing_ids = {annotation.get("term", {}).get("id") for annotation in data.get("existing_annotations", [])}
    if gene in NEW_RESPONSE_REGULATOR_GENES and "GO:0000156" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                gene,
                "GO:0000156",
                "enables",
                "Receiver-domain response-regulator activity should be recorded for this two-component protein.",
                "The UniProt and Asta product/domain evidence identify a CheY-like receiver-domain response regulator.",
            )
        )
        existing_ids.add("GO:0000156")
    if gene in NEW_SENSOR_KINASE_GENES and "GO:0000155" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                gene,
                "GO:0000155",
                "enables",
                "Sensor histidine kinase activity should be represented for this histidine kinase.",
                "The UniProt and Asta product/domain evidence support a sensor histidine kinase role.",
            )
        )
        existing_ids.add("GO:0000155")
    if gene in NEW_PROMOTER_BINDING_GENES and "GO:0000976" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                gene,
                "GO:0000976",
                "enables",
                "Promoter-region binding should be represented for this DNA-binding response regulator.",
                "The receiver plus LuxR/GerE or OmpR/PhoB-like DNA-binding output architecture supports transcription cis-regulatory region binding.",
            )
        )


def core_functions(gene: str) -> list[dict]:
    cls = role_class(gene)
    if cls == "sensor":
        return [
            {
                "description": "Sensor histidine kinase activity in a two-component phosphorelay branch.",
                "molecular_function": TERMS["GO:0000155"],
                "directly_involved_in": [TERMS["GO:0000160"]],
                "supported_by": evidence_for(gene, "GO:0000155")
                if "GO:0000155" in goa_ids(gene)
                else evidence_for(gene, "GO:0004673"),
            }
        ]
    if gene == "PP_3419":
        return [
            {
                "description": "Receiver-domain response-regulator activity modulating a sigma-54 transcriptional activator.",
                "molecular_function": TERMS["GO:0000156"],
                "directly_involved_in": [TERMS["GO:0000160"]],
                "supported_by": evidence_for(gene),
            },
            {
                "description": "Sequence-specific DNA binding by the HTH/Fis output domain of a sigma-54 regulator.",
                "molecular_function": TERMS["GO:0043565"],
                "directly_involved_in": [TERMS["GO:0006355"]],
                "supported_by": evidence_for(gene, "GO:0043565"),
            },
        ]
    cores = [
        {
            "description": "Response-regulator receiver activity in a two-component phosphorelay branch.",
            "molecular_function": TERMS["GO:0000156"],
            "directly_involved_in": [TERMS["GO:0000160"]],
            "supported_by": evidence_for(gene, "GO:0000156"),
        }
    ]
    if cls == "dna_response":
        cores.append(
            {
                "description": "DNA-binding transcriptional regulation by a response-regulator output domain.",
                "molecular_function": TERMS["GO:0000976"],
                "directly_involved_in": [TERMS["GO:0006355"]],
                "supported_by": evidence_for(gene, "GO:0000976"),
            }
        )
    return cores


def suggested_question(gene: str) -> str:
    if gene == "PP_2942":
        return "Does PP_2942 have active HD-GYP cyclic-di-GMP phosphodiesterase activity, and what signal controls it?"
    if gene == "PP_4695":
        return "Does the sodium:solute-symporter-like region of PP_4695 sense or transport a specific ligand, or is it a sensory input module?"
    if role_class(gene) == "sensor":
        return f"What input signal and response-regulator partner define the {gene} phosphorelay branch in KT2440?"
    if role_class(gene) == "dna_response":
        return f"What upstream sensor and target regulon define the {gene} response-regulator branch in KT2440?"
    return f"What output pathway and partner proteins are controlled by the {gene} receiver-domain response regulator?"


def suggested_experiment(gene: str) -> str:
    if role_class(gene) == "sensor":
        return (
            f"Construct a {gene} deletion and catalytic histidine mutant, then test phosphotransfer to "
            "adjacent or candidate response regulators under candidate stress and nutrient conditions."
        )
    if role_class(gene) == "dna_response":
        return (
            f"Construct a {gene} deletion and phospho-acceptor mutant, profile transcript changes, "
            "and test binding to candidate promoters by EMSA or ChIP-seq."
        )
    return (
        f"Construct a {gene} deletion and receiver-site mutant, then use phosphoproteomics or "
        "interaction assays to identify the cognate kinase and downstream output."
    )


def curate_gene(gene: str) -> None:
    if gene in EXISTING_CURATED:
        print(f"Preserved existing curated review for {gene}")
        return
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    row = BATCH_ROWS[gene]
    product_line = first_line(gene_file(gene, "uniprot.txt"), "DE   RecName:") or first_line(
        gene_file(gene, "uniprot.txt"), "DE   SubName:"
    )
    asta_line = first_line(gene_file(gene, "deep-research-asta.md"), "protein_description:")

    data["gene_symbol"] = gene
    if row["ordered_locus"] and row["ordered_locus"] != gene:
        data["aliases"] = [row["ordered_locus"]]
    data["status"] = "DRAFT"
    data["description"] = description_for(gene)
    ensure_reference(data, file_id(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, file_id(gene, "uniprot.txt"), f"UniProtKB entry for {gene} ({row['uniprot_accession']})", product_line)
    ensure_reference(data, file_id(gene, "deep-research-asta.md"), f"Asta retrieval report for {gene} ({row['uniprot_accession']})", asta_line)
    normalize_go_ref_titles(data)

    remove_authored_new_annotations(data)
    for annotation in data.get("existing_annotations", []):
        annotation["review"] = make_review(gene, annotation)
    add_needed_new_annotations(gene, data)

    data["core_functions"] = core_functions(gene)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene)}]
    data["suggested_experiments"] = [
        {
            "description": suggested_experiment(gene),
            "experiment_type": "targeted two-component or transcriptional regulatory assay",
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def module_term(go_id: str) -> dict:
    item = TERMS[go_id]
    return {"preferred_term": item["label"], "term": item}


def annoton(gene: str, label: str, function_id: str, process_ids: list[str], role: str) -> dict:
    return {
        "id": slug(label),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [module_term(go_id) for go_id in process_ids],
        "locations": [],
        "role_description": role,
        "function": module_term(function_id),
    }


def grouped_part(order: int, role: str, node_id: str, label: str, description: str, annotons: list[dict]) -> dict:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": label,
            "module_type": "SIGNALING_PATHWAY",
            "description": description,
            "annotons": annotons,
        },
    }


def build_new_module_parts(start_order: int) -> list[dict]:
    colrs = grouped_part(
        start_order,
        "ColRS curated anchor branch",
        "regulation_signal_transduction_tcs_colrs_anchor_branch",
        "ColRS two-component branch",
        "Named ColRS branch retained as the curated anchor inside the regulation-bucket TCS extension.",
        [
            annoton(
                "colS",
                "colS: sensor histidine kinase",
                "GO:0000155",
                ["GO:0000160"],
                "Sensor histidine kinase partner of the ColRS branch.",
            ),
            annoton(
                "colR",
                "colR: DNA-binding response regulator",
                "GO:0000156",
                ["GO:0000160", "GO:0006355"],
                "Curated DNA-binding response regulator output of the ColRS branch.",
            ),
        ],
    )
    colrs["node"]["connections"] = [
        {
            "source": "cols_sensor_histidine_kinase",
            "target": "colr_dna_binding_response_regulator",
            "connection_type": "PROVIDES_INPUT_FOR",
            "description": "ColS is the cognate upstream sensor histidine kinase for ColR in the ColRS branch.",
        }
    ]

    sensors = [
        gene
        for gene in GENES
        if gene in SENSOR_GENES and gene != "colS"
    ]
    dna_response = [
        gene
        for gene in GENES
        if gene in DNA_BINDING_RESPONSE_GENES and gene != "colR"
    ]
    receivers = [gene for gene in GENES if gene in RECEIVER_ONLY_GENES]

    return [
        colrs,
        grouped_part(
            start_order + 1,
            "Generic histidine kinase sensors from regulation bucket",
            "regulation_signal_transduction_tcs_sensor_kinase_group",
            "Generic two-component sensor histidine kinases",
            "Predicted histidine kinases with unresolved input cues and response-regulator partners.",
            [
                annoton(
                    gene,
                    f"{gene}: sensor histidine kinase",
                    "GO:0000155",
                    ["GO:0000160"],
                    "Predicted sensor histidine kinase with unresolved cue and output branch.",
                )
                for gene in sensors
            ],
        ),
        grouped_part(
            start_order + 2,
            "DNA-binding response regulators from regulation bucket",
            "regulation_signal_transduction_tcs_dna_binding_response_regulator_group",
            "Generic DNA-binding response regulators",
            "Predicted response regulators with receiver and DNA-binding output domains but unresolved regulons.",
            [
                annoton(
                    gene,
                    f"{gene}: DNA-binding response regulator",
                    "GO:0000156",
                    ["GO:0000160", "GO:0006355"],
                    "Predicted DNA-binding response regulator with unresolved sensor and target regulon.",
                )
                for gene in dna_response
            ],
        ),
        grouped_part(
            start_order + 3,
            "Receiver-only and noncanonical response regulators",
            "regulation_signal_transduction_tcs_receiver_only_response_regulator_group",
            "Receiver-only or noncanonical response regulators",
            "CheY-like receiver-domain proteins whose output pathways or partner proteins remain unresolved.",
            [
                annoton(
                    gene,
                    f"{gene}: receiver-domain response regulator",
                    "GO:0000156",
                    ["GO:0000160"],
                    "Receiver-domain response regulator with unresolved output pathway.",
                )
                for gene in receivers
            ],
        ),
    ]


def ensure_module_evidence(doc: dict) -> None:
    evidence = doc.setdefault("evidence", [])
    source_id = "file:projects/P_PUTIDA/batches/module_regulation_signal_transduction_two_component_sensors_response_regulators.tsv"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK regulation-bucket two-component split",
                "statement": (
                    "The functional-bucket partition groups 48 histidine kinases, response regulators, "
                    "and hybrid two-component proteins for conservative generic TCS curation."
                ),
            }
        )


def ensure_module_concepts(doc: dict) -> None:
    concepts = doc.setdefault("module", {}).setdefault("concepts", [])
    existing = {item.get("term", {}).get("id") for item in concepts}
    for go_id in ["GO:0000155", "GO:0000156", "GO:0000160", "GO:0000976", "GO:0004673", "GO:0006355", "GO:0008081"]:
        if go_id not in existing:
            concepts.append(module_term(go_id))
            existing.add(go_id)


def update_module_description(doc: dict) -> None:
    addition = (
        " The module also includes a regulation/signal-transduction functional-bucket extension "
        "for 48 KT2440 two-component proteins, grouped as the ColRS anchor branch, generic "
        "sensor kinases, DNA-binding response regulators, and receiver-only or noncanonical "
        "response regulators with unresolved cues and regulons."
    )
    description = doc.get("description", "")
    if "functional-bucket extension for 48 KT2440 two-component proteins" not in description:
        doc["description"] = description.rstrip() + addition
    notes = doc.get("notes", "")
    note_addition = (
        " The regulation-bucket extension keeps transporter-like, HD-GYP, ATP-binding, "
        "localization, and osmosensory side annotations out of the core pathway claim unless "
        "gene-specific evidence resolves the output."
    )
    if "regulation-bucket extension keeps transporter-like" not in notes:
        doc["notes"] = notes.rstrip() + note_addition


def build_module_extension() -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    ensure_module_evidence(doc)
    ensure_module_concepts(doc)
    update_module_description(doc)
    parts = doc.setdefault("module", {}).setdefault("parts", [])
    parts[:] = [
        part
        for part in parts
        if not str(part.get("node", {}).get("id", "")).startswith("regulation_signal_transduction_tcs_")
    ]
    max_order = max((int(part.get("order", 0)) for part in parts), default=0)
    parts.extend(build_new_module_parts(max_order + 1))
    MODULE_PATH.write_text(
        yaml.dump(doc, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Extended {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    expected = SENSOR_GENES | DNA_BINDING_RESPONSE_GENES | RECEIVER_ONLY_GENES
    missing = sorted(set(GENES) - expected)
    extra = sorted(expected - set(GENES))
    if missing or extra:
        raise RuntimeError(f"Classification mismatch missing={missing} extra={extra}")
    for gene in GENES:
        curate_gene(gene)
    build_module_extension()


if __name__ == "__main__":
    main()
