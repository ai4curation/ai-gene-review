#!/usr/bin/env python3
"""First-pass curation for the ppu02024 PP_1722-PP_1726 phosphonate ABC import bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SPECIES = "PSEPK"
GENE_ROOT = ROOT / "genes" / SPECIES


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

PHOSPHONATE_TRANSPORT = {"id": "GO:0015716", "label": "organic phosphonate transport"}
PHOSPHONATE_TRANSPORTER = {
    "id": "GO:0015416",
    "label": "ABC-type phosphonate transporter activity",
}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "PP_1722": {
        "accession": "Q88M52",
        "kind": "atpase",
        "description": (
            "PP_1722 encodes the ATP-binding energy-coupling subunit of a predicted "
            "2-aminoethylphosphonate/phosphonate ABC import system in Pseudomonas putida "
            "KT2440. Its ABC transporter ATP-binding domains and local PP_1723/PP_1724 "
            "2-aminoethylphosphonate permeases support assignment to ATP-driven organic "
            "phosphonate uptake rather than to a generic transporter process."
        ),
        "product_quote": "DE   SubName: Full=ABC transporter, ATP-binding protein",
        "domain_quote": "DR   InterPro; IPR050093; ABC_SmlMolc_Importer.",
        "atp_domain_quote": "DR   InterPro; IPR003439; ABC_transporter-like_ATP-bd.",
        "asta_quote": "- **Protein Description:** SubName: Full=ABC transporter, ATP-binding protein",
    },
    "PP_1723": {
        "accession": "Q88M51",
        "kind": "permease",
        "description": (
            "PP_1723 encodes a multi-pass inner-membrane permease subunit of a predicted "
            "2-aminoethylphosphonate/phosphonate ABC import system in Pseudomonas putida "
            "KT2440. The product name, MetI-like ABC permease domain, and adjacent ATPase "
            "and second permease support a role as a membrane-channel component of organic "
            "phosphonate uptake."
        ),
        "product_quote": "DE   SubName: Full=2-aminoethylphosphonate transport system permease",
        "domain_quote": "DR   InterPro; IPR000515; MetI-like.",
        "tm_quote": "FT   TRANSMEM        14..36",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
        "asta_quote": "- **Protein Description:** SubName: Full=2-aminoethylphosphonate transport system permease",
    },
    "PP_1724": {
        "accession": "Q88M50",
        "kind": "permease",
        "description": (
            "PP_1724 encodes a multi-pass inner-membrane permease subunit of a predicted "
            "2-aminoethylphosphonate/phosphonate ABC import system in Pseudomonas putida "
            "KT2440. Its product name and MetI-like ABC permease domain support a role with "
            "PP_1722 and PP_1723 in organic phosphonate uptake."
        ),
        "product_quote": "DE   SubName: Full=ABC-type 2-aminoethylphosphonate transporter permease",
        "domain_quote": "DR   InterPro; IPR000515; MetI-like.",
        "tm_quote": "FT   TRANSMEM        12..35",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
        "asta_quote": "- **Protein Description:** SubName: Full=ABC-type 2-aminoethylphosphonate transporter permease",
    },
    "PP_1726": {
        "accession": "Q88M48",
        "kind": "binding",
        "description": (
            "PP_1726 encodes a predicted signal-peptide-bearing periplasmic solute-binding "
            "component of the PP_1722-PP_1724 2-aminoethylphosphonate/phosphonate ABC import "
            "system in Pseudomonas putida KT2440. The local transporter context supports "
            "organic phosphonate uptake, while the electronic thiamine-binding annotations "
            "appear to be over-propagated from the broad SBP_bac_6 family."
        ),
        "product_quote": "DE   SubName: Full=ABC transporter, periplasmic binding protein",
        "domain_quote": "DR   Pfam; PF13343; SBP_bac_6; 1.",
        "signal_quote": "FT   SIGNAL          1..22",
        "asta_quote": "- **Protein Description:** SubName: Full=ABC transporter, periplasmic binding protein",
    },
}


def file_ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def review(
    summary: str,
    action: str,
    reason: str,
    supported_by: list[dict[str, str]],
    proposed: list[dict] | None = None,
) -> dict:
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


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
            "statement": "UniProt product naming supports the first-pass phosphonate ABC importer assignment.",
            "supporting_text": cfg["product_quote"],
        },
        {
            "statement": "Domain annotation supports this subunit's role in an ABC import system.",
            "supporting_text": cfg["domain_quote"],
        },
    ]
    if cfg["kind"] == "atpase":
        findings.append(
            {
                "statement": "The ATP-binding domain supports an ABC energy-coupling role.",
                "supporting_text": cfg["atp_domain_quote"],
            }
        )
    elif cfg["kind"] == "permease":
        findings.extend(
            [
                {
                    "statement": "Predicted transmembrane helices support an inner-membrane permease role.",
                    "supporting_text": cfg["tm_quote"],
                },
                {
                    "statement": "UniProt subcellular-location annotation supports membrane localization.",
                    "supporting_text": cfg["location_quote"],
                },
            ]
        )
    else:
        findings.append(
            {
                "statement": "The signal peptide supports periplasmic localization for a Gram-negative solute-binding protein.",
                "supporting_text": cfg["signal_quote"],
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
                "statement": "Asta retrieval was checked for this first pass and recapitulates the UniProt product assignment.",
                "supporting_text": cfg["asta_quote"],
            }
        ],
    }
    data["references"] = list(refs.values())


def basic_support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> list[dict[str, str]]:
    evidence = [
        ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
        ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
    ]
    if cfg["kind"] == "atpase":
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["atp_domain_quote"]))
    elif cfg["kind"] == "permease":
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["tm_quote"]))
    else:
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["signal_quote"]))
    return evidence


def atpase_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0000166":
        return review(
            "Nucleotide binding is true but too generic for this ABC transporter ATPase.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has ATP binding and ATP hydrolysis annotations, while the local AEP/phosphonate importer context supports the more informative ABC-type phosphonate transporter activity.",
            basic_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0005524":
        return review(
            "ATP binding is correct mechanistic context for the ABC energy-coupling subunit.",
            "KEEP_AS_NON_CORE",
            "PP_1722 has ABC transporter ATP-binding domains, but ATP binding is a supporting activity rather than the substrate-specific core transporter function.",
            basic_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0016887":
        return review(
            "ATP hydrolysis activity is correct for the ABC ATPase subunit.",
            "KEEP_AS_NON_CORE",
            "ATP hydrolysis powers the importer, but the more informative function is ABC-type phosphonate transporter activity in the PP_1722-PP_1726 complex.",
            basic_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0022857":
        return review(
            "Generic transmembrane transporter activity captures the complex role but should be made substrate-specific.",
            "MODIFY",
            "The adjacent permeases are annotated as 2-aminoethylphosphonate transporter subunits and PP_1722 has ABC importer ATPase domains, supporting ABC-type phosphonate transporter activity as the more precise molecular-function term.",
            basic_support(gene, cfg, rows, go_id),
            [PHOSPHONATE_TRANSPORTER],
        )
    if go_id == "GO:0043190":
        return review(
            "ABC transporter complex membership is appropriate for this ATP-binding import subunit.",
            "ACCEPT",
            "The ABC small-molecule importer and ABC ATP-binding-domain signatures support PP_1722 as a component of an ABC transporter complex.",
            basic_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        return review(
            "Transmembrane transport is correct but too broad for this AEP/phosphonate importer ATPase.",
            "MODIFY",
            "The local PP_1722-PP_1726 block supports organic phosphonate transport rather than an unspecified transmembrane transport process.",
            basic_support(gene, cfg, rows, go_id),
            [PHOSPHONATE_TRANSPORT],
        )
    raise KeyError(f"Unhandled ATPase term {go_id}")


def permease_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
            "ACCEPT",
            "UniProt subcellular-location and transmembrane-segment predictions support inner/cell membrane localization, represented as GO:0005886.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["tm_quote"]),
            ],
        )
    if go_id == "GO:0016020":
        return review(
            "Generic membrane localization is supported but less informative than plasma membrane.",
            "MARK_AS_OVER_ANNOTATED",
            "The same GOA record has the more specific plasma membrane annotation for the bacterial inner-membrane permease.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0005886"])),
                ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]),
            ],
        )
    if go_id == "GO:0043190":
        return review(
            "ABC transporter complex membership is appropriate for this permease subunit.",
            "ACCEPT",
            "The product name, MetI-like permease domain, and transmembrane segments support PP_1723/PP_1724 as membrane subunits of an ABC importer.",
            basic_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        return review(
            "Transmembrane transport is correct but too broad for this AEP/phosphonate permease.",
            "MODIFY",
            "The UniProt product names identify the permeases as 2-aminoethylphosphonate transporter components, so organic phosphonate transport is the more informative biological-process term.",
            basic_support(gene, cfg, rows, go_id),
            [PHOSPHONATE_TRANSPORT],
        )
    raise KeyError(f"Unhandled permease term {go_id} for {gene}")


def binding_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0015888":
        return review(
            "The transporter-process idea is plausible, but thiamine specificity is not supported in this local locus.",
            "MODIFY",
            "PP_1726 is a signal-peptide-bearing ABC periplasmic binding protein next to AEP/phosphonate permeases. The TreeGrafter thiamine transport call should be replaced with organic phosphonate transport for this first-pass pathway context.",
            basic_support(gene, cfg, rows, go_id),
            [PHOSPHONATE_TRANSPORT],
        )
    if go_id == "GO:0030288":
        return review(
            "Periplasmic localization is appropriate for this signal-peptide-bearing ABC solute-binding protein.",
            "ACCEPT",
            "The N-terminal signal peptide and periplasmic binding-protein product description support localization in the Gram-negative periplasm.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["signal_quote"]),
            ],
        )
    if go_id == "GO:0030975":
        return review(
            "Thiamine binding is not supported by the local AEP/phosphonate ABC-import context.",
            "MODIFY",
            "The electronic TreeGrafter thiamine-binding call appears to come from broad SBP_bac_6 family transfer. In this locus, PP_1726 is better modeled as contributing to ABC-type phosphonate transporter activity.",
            basic_support(gene, cfg, rows, go_id),
            [PHOSPHONATE_TRANSPORTER],
        )
    if go_id == "GO:0030976":
        return review(
            "Thiamine pyrophosphate binding is likely an over-propagated SBP-family annotation for this periplasmic transporter component.",
            "REMOVE",
            "PP_1726 is a periplasmic ABC binding protein in an AEP/phosphonate transporter locus, not a cytosolic thiamine-pyrophosphate enzyme or cofactor-binding protein; the TreeGrafter TPP-binding assertion is not supported by the local evidence.",
            basic_support(gene, cfg, rows, go_id),
        )
    raise KeyError(f"Unhandled binding-protein term {go_id}")


def new_annotation(term: dict[str, str], qualifier: str, gene: str, cfg: dict, summary: str, reason: str) -> dict:
    supported_by = [
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
        ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
    ]
    if cfg["kind"] == "binding":
        supported_by.append(ref(file_ref(gene, "uniprot.txt"), cfg["signal_quote"]))
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_ref(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


def core_functions(gene: str, cfg: dict, rows: dict[str, dict[str, str]]) -> list[dict]:
    if cfg["kind"] == "atpase":
        return [
            {
                "description": "ATP-binding energy-coupling subunit of a predicted ABC-type 2-aminoethylphosphonate/phosphonate importer.",
                "molecular_function": PHOSPHONATE_TRANSPORTER,
                "directly_involved_in": [PHOSPHONATE_TRANSPORT],
                "in_complex": ABC_COMPLEX,
                "supported_by": [
                    ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0043190"])),
                    ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["atp_domain_quote"]),
                    ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
                ],
            }
        ]
    if cfg["kind"] == "permease":
        return [
            {
                "description": "Inner-membrane permease subunit contributing to ABC-type 2-aminoethylphosphonate/phosphonate import.",
                "contributes_to_molecular_function": PHOSPHONATE_TRANSPORTER,
                "directly_involved_in": [PHOSPHONATE_TRANSPORT],
                "locations": [PLASMA_MEMBRANE],
                "in_complex": ABC_COMPLEX,
                "supported_by": [
                    ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0043190"])),
                    ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                    ref(file_ref(gene, "uniprot.txt"), cfg["tm_quote"]),
                    ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
                ],
            }
        ]
    return [
        {
            "description": "Periplasmic solute-binding component predicted to contribute substrate capture for ABC-type 2-aminoethylphosphonate/phosphonate import.",
            "contributes_to_molecular_function": PHOSPHONATE_TRANSPORTER,
            "directly_involved_in": [PHOSPHONATE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "supported_by": [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0030288"])),
                ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["signal_quote"]),
                ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
            ],
        }
    ]


def suggested_questions(gene: str, cfg: dict) -> list[dict[str, str]]:
    return [
        {
            "question": f"Which organic phosphonate substrates are bound or transported by {gene}, and is 2-aminoethylphosphonate the physiological substrate of the PP_1722-PP_1726 importer?"
        }
    ]


def suggested_experiments(gene: str, cfg: dict) -> list[dict[str, str]]:
    return [
        {
            "description": f"Test growth, radiotracer or LC-MS uptake, and phosphate-limitation induction for a {gene} deletion strain on 2-aminoethylphosphonate and related organic phosphonates, with genetic complementation.",
            "experiment_type": "targeted transporter mutant substrate-uptake assay",
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    rows = goa_rows(gene)

    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_references(data, gene, cfg)

    for ann in data.get("existing_annotations", []):
        go_id = ann["term"]["id"]
        if cfg["kind"] == "atpase":
            ann["review"] = atpase_review(gene, cfg, rows, go_id)
        elif cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, rows, go_id)
        else:
            ann["review"] = binding_review(gene, cfg, rows, go_id)

    existing_ids = {ann["term"]["id"] for ann in data.get("existing_annotations", [])}
    if "GO:0015716" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                PHOSPHONATE_TRANSPORT,
                "involved_in",
                gene,
                cfg,
                "Organic phosphonate transport is a missing substrate-class process annotation for this predicted AEP/phosphonate ABC importer subunit.",
                "The local PP_1722-PP_1726 locus and AEP/phosphonate permease product names support organic phosphonate transport as the substrate-class process.",
            )
        )
    if cfg["kind"] != "atpase" and "GO:0015416" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                PHOSPHONATE_TRANSPORTER,
                "contributes_to",
                gene,
                cfg,
                "ABC-type phosphonate transporter activity is a missing substrate-specific activity annotation for this importer subunit.",
                "This subunit does not transport alone, but it contributes to the predicted ABC-type phosphonate importer complex.",
            )
        )
    if cfg["kind"] == "binding" and "GO:0043190" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                cfg,
                "ABC transporter complex membership is a useful missing annotation for the periplasmic binding component.",
                "Bacterial ABC importers include a substrate-binding protein that delivers ligand to the membrane transporter complex.",
            )
        )

    data["core_functions"] = core_functions(gene, cfg, rows)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene, cfg)
    data["suggested_experiments"] = suggested_experiments(gene, cfg)

    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
