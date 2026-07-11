#!/usr/bin/env python3
"""First-pass curation for ppu02010 type-I-secretion ABC exporter candidates."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/type_i_protein_secretion_abc_boundary.yaml")


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": uniprot_ref(gene), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": asta_ref(gene), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, statement: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            findings = ref.setdefault("findings", [])
            if supporting_text and not any(f.get("supporting_text") == supporting_text for f in findings):
                findings.append({"statement": statement, "supporting_text": supporting_text})
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"statement": statement, "supporting_text": supporting_text})
    refs.append(ref)


def review(
    gene: str,
    term_id: str,
    label: str,
    summary: str,
    action: str,
    reason: str,
    *,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if extra_support:
        supported_by.extend(extra_support)
    data = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        data["proposed_replacement_terms"] = deepcopy(proposed)
    return data


def new_annotation(gene: str, term: dict, qualifier: str, summary: str, reason: str, supported_by: list[dict]) -> dict:
    return {
        "term": deepcopy(term),
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PROTEOLYSIS = {"id": "GO:0006508", "label": "proteolysis"}
PEPTIDASE = {"id": "GO:0008233", "label": "peptidase activity"}
OLIGOPEPTIDE_TRANSPORTER = {"id": "GO:0015421", "label": "ABC-type oligopeptide transporter activity"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
TYPE_I_PROCESS = {"id": "GO:0030253", "label": "protein secretion by the type I secretion system"}
TYPE_I_COMPLEX = {"id": "GO:0030256", "label": "type I protein secretion system complex"}
LIPID_TRANSPORTER = {"id": "GO:0034040", "label": "ATPase-coupled lipid transmembrane transporter activity"}
OLIGOPEPTIDE_TRANSPORT = {"id": "GO:0035672", "label": "oligopeptide transmembrane transport"}
ATPASE_COUPLED = {"id": "GO:0042626", "label": "ATPase-coupled transmembrane transporter activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
ABC_TYPE = {"id": "GO:0140359", "label": "ABC-type transporter activity"}


GENES = {
    "paxB": {
        "accession": "Q88RG3",
        "locus": "PP_0167",
        "class": "type_i",
        "description": (
            "paxB encodes a predicted cell-membrane type-I-secretion ABC exporter component. "
            "The protein has a fused ABC transmembrane domain, ABC ATP-binding domain, "
            "ATPase_T1SS domain, Type_1_exporter signature, and C39 peptidase domain. "
            "The first-pass core call is an ATP-driven type-I-secretion exporter candidate, "
            "with toxin substrate identity unresolved."
        ),
        "product": "Full=Toxin secretion ATP-binding protein",
        "asta_product": "Full=Toxin secretion ATP-binding protein",
        "t1ss": "InterPro; IPR017750; ATPase_T1SS.",
        "exporter": "InterPro; IPR039421; Type_1_exporter.",
        "peptidase": "InterPro; IPR005074; Peptidase_C39.",
        "abc_tm": "ABC transmembrane type-1",
        "abc": "ABC transporter",
        "location": "Cell membrane",
        "module_role": "Predicted toxin-secretion type-I ABC exporter candidate.",
    },
    "PP_0804": {
        "accession": "Q88PP4",
        "locus": "PP_0804",
        "class": "type_i",
        "description": (
            "PP_0804 encodes a predicted fused ABC permease/ATPase component of a protein "
            "secretion ABC efflux system. UniProt and InterPro support a cell-membrane "
            "type-I-exporter architecture with ATPase_T1SS and C39 peptidase-family domains. "
            "Oligopeptide-transporter annotations are treated as TreeGrafter spillover; the "
            "more defensible first-pass process is type-I protein secretion with the exported "
            "substrate unresolved."
        ),
        "product": "Full=Protein secretion ABC efflux system, permease and ATP-binding protein",
        "asta_product": "Full=Protein secretion ABC efflux system, permease and ATP-binding protein",
        "t1ss": "InterPro; IPR017750; ATPase_T1SS.",
        "exporter": "InterPro; IPR039421; Type_1_exporter.",
        "peptidase": "InterPro; IPR005074; Peptidase_C39.",
        "abc_tm": "ABC transmembrane type-1",
        "abc": "ABC transporter",
        "location": "Cell membrane",
        "module_role": "Predicted protein-secretion type-I ABC exporter candidate.",
    },
    "aprDA": {
        "accession": "Q88JT7",
        "locus": "PP_2560",
        "class": "type_i",
        "description": (
            "aprDA encodes a predicted cell-membrane type-I-secretion ABC exporter component "
            "for an alkaline-protease secretion system. The record has AprD-like ABC "
            "transmembrane and ATPase_T1SS_PrtD-like signatures and GOA already places it in "
            "the type I protein secretion system. The first-pass core call is ATP-driven "
            "type-I protein secretion rather than lipid transport."
        ),
        "product": "Full=Alkaline protease secretion transporter ATP-binding protein",
        "asta_product": "Full=Alkaline protease secretion transporter ATP-binding protein",
        "t1ss": "InterPro; IPR010128; ATPase_T1SS_PrtD-like.",
        "exporter": "InterPro; IPR039421; Type_1_exporter.",
        "aprd": "InterPro; IPR047957; ABC_AprD-like_6TM.",
        "abc_tm": "ABC transmembrane type-1",
        "abc": "ABC transporter",
        "location": "Cell membrane",
        "module_role": "Predicted alkaline-protease type-I secretion ABC exporter.",
    },
    "cyaB": {
        "accession": "Q88DA0",
        "locus": "PP_4927",
        "class": "type_i",
        "description": (
            "cyaB encodes a predicted cell-membrane type-I-secretion ABC exporter/processing "
            "component with HlyB/CyaB-like ATPase_T1SS, ABC transmembrane, ABC ATP-binding, "
            "and C39 peptidase-family domains. The first-pass core call is ATP-driven type-I "
            "protein secretion, with cyclolysin-like substrate processing retained as "
            "domain-supported but not promoted as a broader proteolysis pathway."
        ),
        "product": "Full=Cyclolysin secretion/processing ATP-binding protein CyaB",
        "asta_product": "Full=Cyclolysin secretion/processing ATP-binding protein CyaB",
        "t1ss": "InterPro; IPR010132; ATPase_T1SS_HlyB.",
        "exporter": "InterPro; IPR039421; Type_1_exporter.",
        "peptidase": "InterPro; IPR005074; Peptidase_C39.",
        "peptidase_like": "InterPro; IPR039395; Peptidase_C39-like_A.",
        "abc_tm": "ABC transmembrane type-1",
        "abc": "ABC transporter",
        "location": "Cell membrane",
        "module_role": "Predicted cyclolysin-like type-I secretion ABC exporter/processing component.",
    },
    "PP_2240": {
        "accession": "Q88KQ0",
        "locus": "PP_2240",
        "class": "generic",
        "description": (
            "PP_2240 encodes an unresolved fused cell-membrane ABC efflux transporter with "
            "ABC transmembrane and ATP-binding domains. Current first-pass evidence supports "
            "generic ABC-type ATP-dependent transmembrane transport, but does not identify a "
            "substrate or connect the protein to the type-I protein secretion candidates."
        ),
        "product": "Full=ABC efflux transporter, permease/ATP-binding protein",
        "asta_product": "Full=ABC efflux transporter, permease/ATP-binding protein",
        "abc_tm": "ABC transmembrane type-1",
        "abc": "ABC transporter",
        "subd": "InterPro; IPR050835; ABC_transporter_sub-D.",
        "location": "Cell membrane",
        "module_role": "Unresolved generic fused ABC efflux transporter; not added to the type-I-secretion module.",
    },
}


def type_i_support(gene: str, cfg: dict) -> list[dict]:
    keys = ["product", "t1ss", "exporter", "abc_tm", "abc", "location"]
    if "aprd" in cfg:
        keys.append("aprd")
    support = [support_uniprot(gene, cfg[key]) for key in keys]
    support.append(support_asta(gene, cfg["asta_product"]))
    return support


def generic_support(gene: str, cfg: dict) -> list[dict]:
    support = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg["abc_tm"]),
        support_uniprot(gene, cfg["abc"]),
        support_uniprot(gene, cfg["subd"]),
        support_uniprot(gene, cfg["location"]),
        support_asta(gene, cfg["asta_product"]),
    ]
    return support


def type_i_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    t_support = type_i_support(gene, cfg)
    peptidase_support = [
        support_uniprot(gene, cfg["product"]),
        support_uniprot(gene, cfg.get("peptidase", cfg.get("peptidase_like", cfg["product"]))),
    ]
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but less specific than ATP binding for this ABC exporter.",
            "MODIFY",
            "The protein carries an ABC ATP-binding transporter domain; ATP binding is the more specific term.",
            [ATP_BINDING],
            [support_uniprot(gene, cfg["abc"]), support_uniprot(gene, cfg["product"])],
        ),
        "GO:0005524": (
            "ATP binding is appropriate for this ABC exporter component.",
            "ACCEPT",
            "The product is an ATP-binding ABC transporter/permease component with an ABC transporter domain.",
            None,
            [support_uniprot(gene, cfg["abc"]), support_uniprot(gene, cfg["product"])],
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this bacterial cell-membrane exporter.",
            "ACCEPT",
            "UniProt places the protein in the cell membrane and predicts transmembrane regions.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["abc_tm"])],
        ),
        "GO:0006508": (
            "Proteolysis is retained as non-core domain-associated processing context.",
            "KEEP_AS_NON_CORE",
            "The protein has a C39 peptidase-family domain, but the core annotation for this locus is type-I secretion/export rather than general proteolysis.",
            None,
            peptidase_support,
        ),
        "GO:0008233": (
            "Peptidase activity is plausible C39-domain processing context but not the main exporter function.",
            "KEEP_AS_NON_CORE",
            "The C39 peptidase-family domain supports possible substrate processing; substrate-specific evidence is not strong enough to make this the core function.",
            None,
            peptidase_support,
        ),
        "GO:0015421": (
            "The oligopeptide-transporter call is likely a TreeGrafter substrate-class spillover.",
            "MODIFY",
            "UniProt names this as a protein secretion ABC efflux system and InterPro supports a type-I exporter, not an oligopeptide uptake transporter.",
            [ABC_TYPE],
            t_support,
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane.",
            "MARK_AS_OVER_ANNOTATED",
            "The record has the more specific bacterial plasma/cell membrane annotation.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["abc_tm"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is appropriate for the ABC ATPase portion of this exporter.",
            "ACCEPT",
            "The protein carries an ABC transporter ATP-binding domain and type-I-secretion ATPase-family signatures.",
            None,
            t_support,
        ),
        "GO:0030253": (
            "Type-I protein secretion is the best-supported process annotation.",
            "ACCEPT",
            "The protein name and Type_1_exporter/T1SS ATPase domains support a type-I secretion exporter role.",
            None,
            t_support,
        ),
        "GO:0030256": (
            "Type-I protein secretion system complex membership is appropriate.",
            "ACCEPT",
            "This fused membrane ABC ATPase/permease is a predicted type-I secretion system component.",
            None,
            t_support,
        ),
        "GO:0034040": (
            "Lipid-transporter activity is unsupported for this type-I protein secretion exporter.",
            "REMOVE",
            "The local product and InterPro evidence support protein secretion/type-I export, not lipid transport.",
            [ABC_TYPE],
            t_support,
        ),
        "GO:0035672": (
            "Oligopeptide transmembrane transport is unsupported for this protein secretion exporter.",
            "MODIFY",
            "The product and InterPro evidence support type-I protein secretion; no oligopeptide substrate evidence was found.",
            [TYPE_I_PROCESS],
            t_support,
        ),
        "GO:0042626": (
            "ATPase-coupled transmembrane transporter activity is consistent with the ABC exporter architecture.",
            "KEEP_AS_NON_CORE",
            "This is a broad mechanistic parent relative to the more informative type-I secretion process and ABC-type transporter activity.",
            None,
            t_support,
        ),
        "GO:0043190": (
            "ABC transporter complex membership is retained as broad complex context.",
            "ACCEPT" if gene in {"paxB", "PP_0804"} else "MODIFY",
            "The protein is a fused ABC exporter. For entries that already carry type-I-complex GOA, GO:0030256 is more informative; otherwise the broader ABC complex term is retained at the gene-review surface.",
            None if gene in {"paxB", "PP_0804"} else [TYPE_I_COMPLEX],
            t_support,
        ),
        "GO:0055085": (
            "Transmembrane transport is retained as broad transporter process context.",
            "ACCEPT" if gene in {"paxB", "PP_0804"} else "MODIFY",
            "The product and domains support a type-I-secretion interpretation, but only entries with type-I-secretion GOA are narrowed to GO:0030253 in the existing-annotation review.",
            None if gene in {"paxB", "PP_0804"} else [TYPE_I_PROCESS],
            t_support,
        ),
        "GO:0140359": (
            "ABC-type transporter activity is appropriate for this fused ABC exporter.",
            "ACCEPT",
            "UniProt/InterPro support ABC transmembrane and ATP-binding transporter domains.",
            None,
            t_support,
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def generic_review(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    g_support = generic_support(gene, cfg)
    mapping = {
        "GO:0000166": (
            "Nucleotide binding is true but less specific than ATP binding.",
            "MODIFY",
            "The protein carries an ABC transporter ATP-binding domain; ATP binding is more specific.",
            [ATP_BINDING],
            [support_uniprot(gene, cfg["abc"]), support_uniprot(gene, cfg["product"])],
        ),
        "GO:0005524": (
            "ATP binding is appropriate for this fused ABC transporter.",
            "ACCEPT",
            "UniProt/InterPro support an ABC transporter ATP-binding domain.",
            None,
            g_support,
        ),
        "GO:0005886": (
            "Plasma membrane localization is appropriate for this bacterial membrane ABC transporter.",
            "ACCEPT",
            "UniProt places the protein in the cell membrane and predicts an ABC transmembrane domain.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["abc_tm"])],
        ),
        "GO:0016020": (
            "Membrane localization is true but less informative than plasma membrane.",
            "MARK_AS_OVER_ANNOTATED",
            "The record has the more specific plasma membrane annotation.",
            None,
            [support_uniprot(gene, cfg["location"]), support_uniprot(gene, cfg["abc_tm"])],
        ),
        "GO:0016887": (
            "ATP hydrolysis activity is appropriate for the ABC ATPase portion of the protein.",
            "ACCEPT",
            "The protein carries an ABC transporter ATP-binding domain and conserved ABC transporter signatures.",
            None,
            g_support,
        ),
        "GO:0043190": (
            "ABC transporter complex membership is retained as broad component context.",
            "KEEP_AS_NON_CORE",
            "The protein is a fused ABC membrane/ATPase transporter, but the substrate and partner context are unresolved.",
            None,
            g_support,
        ),
        "GO:0055085": (
            "Transmembrane transport is a broad but defensible process annotation.",
            "ACCEPT",
            "The product is an ABC efflux transporter with transmembrane and ATPase domains, although the substrate is unknown.",
            None,
            g_support,
        ),
        "GO:0140359": (
            "ABC-type transporter activity is the best-supported molecular-function annotation.",
            "ACCEPT",
            "UniProt/InterPro support a fused ABC transmembrane and ATP-binding transporter architecture.",
            None,
            g_support,
        ),
    }
    summary, action, reason, proposed, support = mapping[term_id]
    return review(gene, term_id, label, summary, action, reason, proposed=proposed, extra_support=support)


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]
    if cfg["class"] == "type_i" and gene in {"paxB", "PP_0804"}:
        doc["existing_annotations"] = [
            ann
            for ann in doc.get("existing_annotations", [])
            if not (
                ann.get("original_reference_id") == uniprot_ref(gene)
                and ann.get("term", {}).get("id") in {"GO:0030253", "GO:0030256"}
            )
        ]

    ensure_reference(
        doc,
        uniprot_ref(gene),
        f"UniProtKB entry for {gene}",
        "UniProt product/domain/subcellular-location evidence used for first-pass curation.",
        cfg["product"],
    )
    ensure_reference(
        doc,
        asta_ref(gene),
        f"Asta retrieval report for {gene}",
        "Asta retrieval confirmed the target product string but did not add strong gene-specific literature beyond database-derived context.",
        cfg["asta_product"],
    )

    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        if cfg["class"] == "type_i":
            ann["review"] = type_i_review(gene, cfg, term["id"], term["label"])
        else:
            ann["review"] = generic_review(gene, cfg, term["id"], term["label"])

    if cfg["class"] == "type_i":
        t_support = type_i_support(gene, cfg)
        existing_ids = {ann["term"]["id"] for ann in doc["existing_annotations"]}
        process_term = TYPE_I_PROCESS if "GO:0030253" in existing_ids else TRANSMEMBRANE_TRANSPORT
        complex_term = TYPE_I_COMPLEX if "GO:0030256" in existing_ids else ABC_COMPLEX
        doc["core_functions"] = [
            {
                "description": cfg["module_role"],
                "molecular_function": ATP_HYDROLYSIS,
                "contributes_to_molecular_function": ABC_TYPE,
                "directly_involved_in": [process_term],
                "locations": [PLASMA_MEMBRANE],
                "in_complex": complex_term,
                "supported_by": t_support,
            }
        ]
        doc["suggested_questions"] = [
            {"question": f"What is the physiological substrate exported by {gene} in P. putida KT2440?"},
            {"question": f"Which membrane-fusion and outer-membrane-channel partners form the complete {gene}-containing type-I secretion system?"},
        ]
        doc["suggested_experiments"] = [
            {
                "description": f"Delete {gene} and test secretion of candidate RTX/toxin/protease substrates under inducing growth conditions.",
                "experiment_type": "targeted secretion phenotype assay",
            },
            {
                "description": f"Use co-immunoprecipitation or tagged-complex purification to identify the cognate adaptor and outer-membrane channel for {gene}.",
                "experiment_type": "transporter complex mapping",
            },
        ]
    else:
        g_support = generic_support(gene, cfg)
        doc["core_functions"] = [
            {
                "description": cfg["module_role"],
                "molecular_function": ABC_TYPE,
                "directly_involved_in": [TRANSMEMBRANE_TRANSPORT],
                "locations": [PLASMA_MEMBRANE],
                "supported_by": g_support,
            }
        ]
        doc["suggested_questions"] = [
            {"question": "What substrate or pathway context explains the PP_2240 ABCD-like efflux-transporter architecture?"},
            {"question": "Does PP_2240 act as a standalone fused transporter or partner with additional local membrane/adapter proteins?"},
        ]
        doc["suggested_experiments"] = [
            {
                "description": "Profile transport phenotypes of a PP_2240 deletion under membrane-stress, lipid, cobalamin, and xenobiotic conditions.",
                "experiment_type": "substrate-range phenotype screen",
            },
            {
                "description": "Use comparative neighborhood analysis and interaction assays to identify possible PP_2240 substrate or partner context.",
                "experiment_type": "comparative genomics and interaction assay",
            },
        ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=False, width=1000))
    print(f"Wrote {path}")


def write_module() -> None:
    module = {
        "id": "MODULE:type_i_protein_secretion_abc_boundary",
        "title": "Type I protein secretion ABC exporter boundary",
        "description": (
            "Boundary module for Pseudomonas putida KT2440 ppu02010 ABC-exporter candidates with type-I-protein-secretion signatures. "
            "The module records PaxB, PP_0804, AprDA, and CyaB as fused membrane ABC ATPase/permease proteins with T1SS or Type_1_exporter domains, while keeping exact exported substrates and cognate adaptor/outer-membrane-channel partners unresolved. Generic ABCD-like singleton PP_2240 is curated separately and is not included here."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02010",
                "title": "ABC transporters - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02010 includes several fused ABC exporter candidates with secretion/toxin product names.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
                "title": "PSEPK ppu02010 ABC-transporter partition batch",
                "statement": "The ppu02010 partition records C04, C15, C34, and C64 as secretion/toxin/cyclolysin ABC-exporter candidates.",
            },
            {
                "source_id": "UniProtKB:Q88RG3",
                "title": "paxB toxin secretion ATP-binding protein",
                "statement": "UniProt names PaxB as a toxin secretion ATP-binding protein and records ATPase_T1SS, Type_1_exporter, ABC transmembrane, and ABC transporter domains.",
            },
            {
                "source_id": "UniProtKB:Q88PP4",
                "title": "PP_0804 protein secretion ABC efflux system component",
                "statement": "UniProt names PP_0804 as a protein secretion ABC efflux system permease/ATP-binding protein and records ATPase_T1SS and Type_1_exporter domains.",
            },
            {
                "source_id": "UniProtKB:Q88JT7",
                "title": "aprDA alkaline protease secretion transporter",
                "statement": "UniProt names AprDA as an alkaline protease secretion transporter ATP-binding protein and records AprD-like and T1SS transporter domains.",
            },
            {
                "source_id": "UniProtKB:Q88DA0",
                "title": "cyaB cyclolysin secretion/processing ATP-binding protein",
                "statement": "UniProt names CyaB as a cyclolysin secretion/processing ATP-binding protein and records HlyB-like T1SS and C39 peptidase-family domains.",
            },
        ],
        "module": {
            "id": "type_i_protein_secretion_abc_boundary",
            "label": "Type I protein secretion ABC exporter boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                {
                    "preferred_term": "protein secretion by the type I secretion system",
                    "term": TYPE_I_PROCESS,
                    "description": "ATP-dependent export of protein substrates through type-I secretion machinery.",
                },
                {
                    "preferred_term": "type I protein secretion system complex",
                    "term": TYPE_I_COMPLEX,
                    "description": "Type-I secretion complex context for the fused ABC exporter candidates.",
                },
                {
                    "preferred_term": "ATP hydrolysis activity",
                    "term": ATP_HYDROLYSIS,
                    "description": "ATP hydrolysis by fused ABC ATP-binding domains.",
                },
                {
                    "preferred_term": "ABC-type transporter activity",
                    "term": ABC_TYPE,
                    "description": "ABC-type transporter activity shared by the fused exporter candidates.",
                },
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "bacterial plasma membrane",
                        "term": PLASMA_MEMBRANE,
                        "description": "The exporter candidates are predicted bacterial cell-membrane proteins.",
                    }
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Fused type-I-secretion ABC exporter candidates",
                    "node": {
                        "id": "type_i_secretion_abc_exporter_candidates",
                        "label": "PSEPK type-I-secretion ABC exporter candidates",
                        "module_type": "TRANSPORT_STEP",
                        "description": "Fused ABC ATPase/permease proteins with type-I-secretion signatures from the ppu02010 ABC-transporter umbrella map. Substrate identities and complete tripartite partner sets remain unresolved.",
                        "annotons": [
                            {
                                "id": "paxB_type_i_secretion_exporter_candidate",
                                "label": "paxB: predicted toxin-secretion ABC exporter",
                                "participant": {"selector_type": "GENE", "gene": {"preferred_term": "paxB"}},
                                "role_description": "Predicted toxin-secretion type-I ABC exporter candidate.",
                            },
                            {
                                "id": "PP_0804_type_i_secretion_exporter_candidate",
                                "label": "PP_0804: predicted protein-secretion ABC exporter",
                                "participant": {"selector_type": "GENE", "gene": {"preferred_term": "PP_0804"}},
                                "role_description": "Predicted protein-secretion ABC efflux component with T1SS signatures.",
                            },
                            {
                                "id": "aprDA_type_i_secretion_exporter",
                                "label": "aprDA: alkaline-protease secretion ABC exporter",
                                "participant": {"selector_type": "GENE", "gene": {"preferred_term": "aprDA"}},
                                "role_description": "Predicted AprD-like ABC exporter for alkaline-protease type-I secretion.",
                            },
                            {
                                "id": "cyaB_type_i_secretion_processing_exporter",
                                "label": "cyaB: cyclolysin secretion/processing ABC exporter",
                                "participant": {"selector_type": "GENE", "gene": {"preferred_term": "cyaB"}},
                                "role_description": "Predicted HlyB/CyaB-like type-I secretion ABC exporter/processing component.",
                            },
                        ],
                    },
                }
            ],
        },
        "notes": (
            "This is a boundary module for ABC exporter candidates with T1SS signatures. It should not be read as evidence that P. putida KT2440 secretes a specific toxin, cyclolysin, or alkaline protease under standard conditions without direct substrate and partner evidence."
        ),
    }
    for annoton in module["module"]["parts"][0]["node"]["annotons"]:
        annoton["function"] = {"preferred_term": "ATP hydrolysis activity", "term": ATP_HYDROLYSIS}
        annoton["processes"] = [{"preferred_term": "protein secretion by the type I secretion system", "term": TYPE_I_PROCESS}]
        annoton["locations"] = [{"preferred_term": "plasma membrane", "term": PLASMA_MEMBRANE}]
    MODULE_PATH.write_text(yaml.safe_dump(module, sort_keys=False, allow_unicode=False, width=1000))
    print(f"Wrote {MODULE_PATH}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    write_module()


if __name__ == "__main__":
    main()
