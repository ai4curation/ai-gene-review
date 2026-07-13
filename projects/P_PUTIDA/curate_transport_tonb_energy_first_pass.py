#!/usr/bin/env python3
"""First-pass curation for the TonB-ExbB-ExbD transport-energy split."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/tonb_dependent_transport_boundary.yaml"


TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


GENES = {
    "PP_0696": {
        "id": "Q88Q02",
        "description": (
            "PP_0696 encodes a predicted TonB-family energy-transducer protein. "
            "TonB proteins are inner-membrane-anchored, periplasm-spanning components "
            "that couple the ExbB/ExbD proton-motive-force motor to TonB-dependent "
            "outer-membrane receptors. The lightweight evidence supports TonB-like "
            "energy transduction, but the specific receptor set and substrates for "
            "this orphan TonB paralog are unresolved."
        ),
        "kind": "tonb",
        "uniprot_support": "DE   RecName: Full=Energy transducer TonB {ECO:0008006|Google:ProtNLM};",
        "asta_support": "- **Protein Description:** RecName: Full=Energy transducer TonB {ECO:0008006|Google:ProtNLM};",
        "annotations": [],
    },
    "PP_1512": {
        "id": "Q88MQ8",
        "description": (
            "PP_1512 encodes a predicted TonB-family energy-transducer protein. "
            "The protein is likely a TonB paralog involved in energizing one or more "
            "TonB-dependent outer-membrane receptors, but the cognate ExbB/ExbD "
            "partners, receptors, and transported substrates are not resolved from "
            "lightweight metadata."
        ),
        "kind": "tonb",
        "uniprot_support": "DE   RecName: Full=Energy transducer TonB {ECO:0008006|Google:ProtNLM};",
        "asta_support": "- **Protein Description:** RecName: Full=Energy transducer TonB {ECO:0008006|Google:ProtNLM};",
        "annotations": [],
    },
    "PP_1898": {
        "id": "Q88LN1",
        "description": (
            "PP_1898 encodes a MotA/TolQ/ExbB proton-channel-family inner-membrane "
            "protein. By family, it is best treated as an ExbB/TolQ-like proton-"
            "conducting energy-coupling subunit rather than a substrate-specific "
            "transporter or protein-import factor."
        ),
        "kind": "exbB_like",
        "uniprot_support": "DE   SubName: Full=MotA/TolQ/ExbB proton channel family protein {ECO:0000313|EMBL:AAN67517.1};",
        "domain_support": "DR   InterPro; IPR002898; MotA_ExbB_proton_chnl.",
        "location_support": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000256|ARBA:ARBA00004651};",
        "asta_support": "- **Protein Description:** SubName: Full=MotA/TolQ/ExbB proton channel family protein {ECO:0000313|EMBL:AAN67517.1};",
        "annotations": [
            ("GO:0005886", "plasma membrane", "IEA", "GO_REF:0000120", "located_in"),
            ("GO:0016020", "membrane", "IEA", "GO_REF:0000044", "located_in"),
            ("GO:0017038", "protein import", "IEA", "GO_REF:0000118", "involved_in"),
        ],
    },
    "PP_1899": {
        "id": "Q88LN0",
        "description": (
            "PP_1899 encodes an ExbD/TolR-family inner-membrane protein. It is a "
            "candidate energy-transduction partner for an ExbB/TolQ-like motor and "
            "TonB-dependent uptake system, not a standalone substrate transporter. "
            "The cognate receptor system and transported substrates remain unresolved."
        ),
        "kind": "exbD_like",
        "uniprot_support": "DE   SubName: Full=ExbD/TolR family protein {ECO:0000313|EMBL:AAN67518.1};",
        "domain_support": "DR   InterPro; IPR003400; ExbD.",
        "location_support": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000256|ARBA:ARBA00004162};",
        "asta_support": "- **Protein Description:** SubName: Full=ExbD/TolR family protein {ECO:0000313|EMBL:AAN67518.1};",
        "annotations": [
            ("GO:0005886", "plasma membrane", "IEA", "GO_REF:0000120", "located_in"),
            ("GO:0022857", "transmembrane transporter activity", "IEA", "GO_REF:0000002", "enables"),
            ("GO:0055085", "transmembrane transport", "IEA", "GO_REF:0000002", "involved_in"),
        ],
    },
    "exbD": {
        "id": "Q88C76",
        "description": (
            "exbD encodes the ExbD subunit of the canonical exbB-exbD-tonB locus. "
            "ExbD is an inner-membrane component of the TonB energy-transduction "
            "motor that works with ExbB and TonB to energize TonB-dependent "
            "outer-membrane receptors. It supports nutrient uptake by energy "
            "coupling rather than directly transporting substrates."
        ),
        "kind": "exbD",
        "uniprot_support": "DE   RecName: Full=Biopolymer transport protein ExbD {ECO:0000256|ARBA:ARBA00022090};",
        "domain_support": "DR   InterPro; IPR014170; TonB_ExbD_1.",
        "location_support": "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
        "asta_support": "- **Protein Description:** RecName: Full=Biopolymer transport protein ExbD {ECO:0000256|ARBA:ARBA00022090};",
        "annotations": [
            ("GO:0005886", "plasma membrane", "IEA", "GO_REF:0000120", "located_in"),
            ("GO:0016020", "membrane", "IEA", "GO_REF:0000002", "located_in"),
            ("GO:0022857", "transmembrane transporter activity", "IEA", "GO_REF:0000002", "enables"),
            ("GO:0055085", "transmembrane transport", "IEA", "GO_REF:0000002", "involved_in"),
        ],
    },
}


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


def review_for_annotation(gene: str, info: dict[str, object], go_id: str, label: str) -> dict[str, object]:
    uniprot_ref = ref_file(gene, "uniprot.txt")
    asta_ref = ref_file(gene, "deep-research-asta.md")
    kind = info["kind"]

    if go_id == "GO:0005886":
        return {
            "summary": "The protein is an inner-membrane TonB-system component, so plasma membrane localization is appropriate.",
            "action": "ACCEPT",
            "reason": "Bacterial inner membrane is represented by plasma membrane in GO, and the UniProt/Asta metadata support a membrane TonB-system protein.",
            "supported_by": [
                support(uniprot_ref, info.get("location_support", info["uniprot_support"])),
                support(asta_ref, info["asta_support"]),
            ],
        }
    if go_id == "GO:0016020":
        return {
            "summary": "Generic membrane localization is true but less informative than plasma/inner membrane localization.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The protein is a membrane TonB-system component, but the specific plasma membrane row carries the useful localization.",
            "supported_by": [
                support(uniprot_ref, info.get("location_support", info["uniprot_support"])),
                support(asta_ref, info["asta_support"]),
            ],
        }
    if go_id == "GO:0017038":
        return {
            "summary": "Protein import is not the core TonB-system role for this ExbB/TolQ-like protein.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "ExbB/TolQ-family proteins energize TonB-dependent outer-membrane uptake through proton-channel/energy-coupling activity; the protein-import keyword overstates a specialized or indirect consequence.",
            "supported_by": [
                support(uniprot_ref, info["uniprot_support"]),
                support(uniprot_ref, info["domain_support"]),
                support(asta_ref, info["asta_support"]),
            ],
        }
    if go_id == "GO:0022857" and kind in {"exbD_like", "exbD"}:
        return {
            "summary": "A generic substrate-transporter activity is misleading for an ExbD/TolR-family energy-coupling component.",
            "action": "MODIFY",
            "reason": "ExbD-family proteins contribute to TonB-dependent transport by energy transduction with ExbB/TonB rather than by directly transporting a substrate. Energy transducer activity is the better function-level replacement.",
            "proposed_replacement_terms": [term("GO:0031992", "energy transducer activity")],
            "supported_by": [
                support(uniprot_ref, info["uniprot_support"]),
                support(uniprot_ref, info["domain_support"]),
                support(asta_ref, info["asta_support"]),
            ],
        }
    if go_id == "GO:0055085":
        return {
            "summary": "Broad transmembrane transport is biologically related but not the direct molecular role of an ExbD-family subunit.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The ExbD-family protein contributes to TonB-dependent outer-membrane transport through the energy-transduction complex, so the broad process is retained only as non-core context.",
            "supported_by": [
                support(uniprot_ref, info["uniprot_support"]),
                support(uniprot_ref, info["domain_support"]),
                support(asta_ref, info["asta_support"]),
            ],
        }
    raise ValueError(f"Unhandled annotation {gene} {go_id} {label}")


def core_function(gene: str, info: dict[str, object]) -> dict[str, object]:
    uniprot_ref = ref_file(gene, "uniprot.txt")
    asta_ref = ref_file(gene, "deep-research-asta.md")
    kind = info["kind"]

    if kind in {"tonb"}:
        return {
            "description": "Predicted TonB-family energy transducer for TonB-dependent outer-membrane transport; receptor partners and substrates are unresolved.",
            "molecular_function": term("GO:0031992", "energy transducer activity"),
            "directly_involved_in": [term("GO:0055085", "transmembrane transport")],
            "supported_by": [
                support(uniprot_ref, info["uniprot_support"]),
                support(asta_ref, info["asta_support"]),
            ],
        }
    if kind == "exbB_like":
        return {
            "description": "ExbB/TolQ-like proton-channel-family membrane protein likely contributing to TonB-system energy coupling.",
            "molecular_function": term("GO:0015078", "proton transmembrane transporter activity"),
            "directly_involved_in": [term("GO:1902600", "proton transmembrane transport")],
            "locations": [term("GO:0005886", "plasma membrane")],
            "supported_by": [
                support(uniprot_ref, info["uniprot_support"]),
                support(uniprot_ref, info["domain_support"]),
                support(asta_ref, info["asta_support"]),
            ],
        }
    if kind in {"exbD_like", "exbD"}:
        return {
            "description": "ExbD/TolR-family inner-membrane energy-coupling component for a TonB-dependent transport system.",
            "molecular_function": term("GO:0031992", "energy transducer activity"),
            "directly_involved_in": [term("GO:0055085", "transmembrane transport")],
            "locations": [term("GO:0005886", "plasma membrane")],
            "supported_by": [
                support(uniprot_ref, info["uniprot_support"]),
                support(uniprot_ref, info["domain_support"]),
                support(asta_ref, info["asta_support"]),
            ],
        }
    raise ValueError(f"Unhandled core kind {gene} {kind}")


def references(gene: str, info: dict[str, object], annotations: list[tuple[str, str, str, str, str]]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    for ref_id in sorted({ann[3] for ann in annotations}):
        refs.append({"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []})

    uniprot_findings = [{"supporting_text": info["uniprot_support"]}]
    if "domain_support" in info:
        uniprot_findings.append({"supporting_text": info["domain_support"]})
    if "location_support" in info:
        uniprot_findings.append({"supporting_text": info["location_support"]})
    refs.append(
        {
            "id": ref_file(gene, "uniprot.txt"),
            "title": f"UniProtKB entry for {gene}",
            "findings": uniprot_findings,
        }
    )
    refs.append(
        {
            "id": ref_file(gene, "deep-research-asta.md"),
            "title": f"Asta retrieval report for {gene} ({info['id']})",
            "findings": [{"supporting_text": info["asta_support"]}],
        }
    )
    return refs


def write_gene(gene: str, info: dict[str, object]) -> None:
    annotations = info["annotations"]
    existing = []
    for go_id, label, evidence, ref_id, qualifier in annotations:
        existing.append(
            {
                "term": term(go_id, label),
                "evidence_type": evidence,
                "original_reference_id": ref_id,
                "qualifier": qualifier,
                "review": review_for_annotation(gene, info, go_id, label),
            }
        )

    doc = {
        "id": info["id"],
        "gene_symbol": gene,
        "product_type": "PROTEIN",
        "status": "DRAFT",
        "taxon": TAXON,
        "description": info["description"],
        "existing_annotations": existing,
        "references": references(gene, info, annotations),
        "core_functions": [core_function(gene, info)],
        "proposed_new_terms": [],
        "suggested_questions": [
            {
                "question": "Which TonB-dependent outer-membrane receptors, if any, are energized by this TonB-system paralog in KT2440?"
            },
            {
                "question": "What substrates or growth conditions require this paralog rather than the canonical exbB-exbD-tonB locus?"
            },
        ],
        "suggested_experiments": [
            {
                "description": "Construct single and combined deletion strains and assay growth under iron limitation, siderophore-dependent iron uptake, and uptake through candidate TonB-dependent receptors.",
                "experiment_type": "transport genetics",
            }
        ],
    }
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(gene: str, label: str, function: dict[str, str], process: dict[str, str] | None = None) -> dict[str, object]:
    entry: dict[str, object] = {
        "id": f"{gene}_tonb_energy_context",
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": label,
        "function": {"preferred_term": function["label"], "term": function},
        "locations": [{"preferred_term": "plasma membrane", "term": term("GO:0005886", "plasma membrane")}],
    }
    if process:
        entry["processes"] = [{"preferred_term": process["label"], "term": process}]
    return entry


def write_module() -> None:
    doc = {
        "id": "MODULE:tonb_dependent_transport_boundary",
        "title": "TonB-dependent transport energy-transduction boundary",
        "description": (
            "Boundary module for PSEPK TonB-ExbB-ExbD energy-transduction proteins. "
            "This first pass covers the canonical exbB-exbD-tonB locus plus orphan "
            "TonB and ExbB/ExbD-like paralogs from the transport/membrane/efflux "
            "partition. TonB-dependent outer-membrane receptor specificity is tracked "
            "as a separate queued receptor-panel split."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_tonb_exbb_exbd_energy_transduction.tsv",
                "title": "PSEPK transport/membrane/efflux TonB-ExbB-ExbD partition batch",
                "statement": "The transport/membrane/efflux partition separates TonB/ExbB/ExbD energy-transduction proteins from TonB-dependent receptors and generic membrane transporters.",
            },
            {
                "source_id": "PMID:11514511",
                "title": "Involvement of the TonB system in tolerance to solvents and drugs in Pseudomonas putida DOT-T1E",
                "statement": "The existing exbB and tonB reviews cite this Pseudomonas TonB-system study for exbB-exbD-tonB linkage and iron-limitation phenotypes in a close P. putida strain.",
            },
        ],
        "module": {
            "id": "tonb_dependent_transport_boundary",
            "label": "TonB-dependent transport energy-transduction boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {
                    "preferred_term": "energy transducer activity",
                    "term": term("GO:0031992", "energy transducer activity"),
                    "description": "TonB/ExbD energy transduction from the inner membrane to outer-membrane receptors.",
                },
                {
                    "preferred_term": "proton transmembrane transporter activity",
                    "term": term("GO:0015078", "proton transmembrane transporter activity"),
                    "description": "ExbB/TolQ-family proton-channel activity that couples proton motive force to TonB-system work.",
                },
                {
                    "preferred_term": "siderophore transport",
                    "term": term("GO:0015891", "siderophore transport"),
                    "description": "Representative TonB-dependent uptake process; receptor-specific substrate scope remains gene-specific.",
                },
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "plasma membrane",
                        "term": term("GO:0005886", "plasma membrane"),
                        "description": "ExbB/ExbD and TonB N termini are anchored in the bacterial inner membrane.",
                    },
                    {
                        "preferred_term": "outer membrane-bounded periplasmic space",
                        "term": term("GO:0030288", "outer membrane-bounded periplasmic space"),
                        "description": "TonB spans the periplasm to contact outer-membrane receptors.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "canonical exbB-exbD-tonB locus",
                    "node": {
                        "id": "canonical_exbb_exbd_tonb_locus",
                        "label": "Canonical ExbB-ExbD-TonB energy-transduction locus",
                        "module_type": "TRANSPORT_STEP",
                        "description": "Canonical PP_5306-PP_5308 TonB-system energy-transduction locus.",
                        "annotons": [
                            annoton("exbB", "exbB: ExbB proton-channel motor subunit", term("GO:0015078", "proton transmembrane transporter activity"), term("GO:1902600", "proton transmembrane transport")),
                            annoton("exbD", "exbD: ExbD energy-coupling subunit", term("GO:0031992", "energy transducer activity"), term("GO:0055085", "transmembrane transport")),
                            annoton("tonB", "tonB: TonB periplasmic energy transducer", term("GO:0031992", "energy transducer activity"), term("GO:0015891", "siderophore transport")),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "orphan TonB paralog candidates",
                    "node": {
                        "id": "orphan_tonb_paralog_candidates",
                        "label": "Orphan TonB energy-transducer candidates",
                        "module_type": "TRANSPORT_STEP",
                        "description": "TonB-like paralogs with unresolved receptor partners and substrate scope.",
                        "annotons": [
                            annoton("PP_0696", "PP_0696: TonB energy-transducer candidate", term("GO:0031992", "energy transducer activity"), term("GO:0055085", "transmembrane transport")),
                            annoton("PP_1512", "PP_1512: TonB energy-transducer candidate", term("GO:0031992", "energy transducer activity"), term("GO:0055085", "transmembrane transport")),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "orphan ExbB/ExbD-like pair",
                    "node": {
                        "id": "orphan_exbb_exbd_like_pair",
                        "label": "Orphan ExbB/ExbD-like energy-coupling pair",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_1898/PP_1899 ExbB/TolQ and ExbD/TolR-family pair candidate.",
                        "annotons": [
                            annoton("PP_1898", "PP_1898: ExbB/TolQ-like proton-channel candidate", term("GO:0015078", "proton transmembrane transporter activity"), term("GO:1902600", "proton transmembrane transport")),
                            annoton("PP_1899", "PP_1899: ExbD/TolR-like energy-coupling candidate", term("GO:0031992", "energy transducer activity"), term("GO:0055085", "transmembrane transport")),
                        ],
                    },
                },
            ],
        },
        "notes": (
            "This boundary intentionally separates energy transduction from the 30-gene "
            "TonB-dependent receptor panel. For orphan TonB and ExbB/ExbD-like paralogs, "
            "regulon, receptor partner, and substrate assignments remain open."
        ),
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    for gene, info in GENES.items():
        write_gene(gene, info)
    write_module()
    print(f"Wrote {len(GENES)} gene reviews and {MODULE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
