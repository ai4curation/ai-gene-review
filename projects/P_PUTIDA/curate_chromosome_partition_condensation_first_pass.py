#!/usr/bin/env python3
"""First-pass curate the PSEPK chromosome partition/condensation boundary batch."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


TERMS = {
    "DNA_BINDING": {"id": "GO:0003677", "label": "DNA binding"},
    "ATP_BINDING": {"id": "GO:0005524", "label": "ATP binding"},
    "CHROMOSOME": {"id": "GO:0005694", "label": "chromosome"},
    "CYTOPLASM": {"id": "GO:0005737", "label": "cytoplasm"},
    "DNA_REPLICATION": {"id": "GO:0006260", "label": "DNA replication"},
    "CHROMOSOME_SEGREGATION": {"id": "GO:0007059", "label": "chromosome segregation"},
    "SISTER_CHROMATID_COHESION": {"id": "GO:0007062", "label": "sister chromatid cohesion"},
    "ATP_HYDROLYSIS": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "CHROMOSOME_CONDENSATION": {"id": "GO:0030261", "label": "chromosome condensation"},
    "CHROMOSOME_ORGANIZATION": {"id": "GO:0051276", "label": "chromosome organization"},
    "CELL_DIVISION": {"id": "GO:0051301", "label": "cell division"},
    "CHROMOSOME_SEPARATION": {"id": "GO:0051304", "label": "chromosome separation"},
    "SPORULATION_POSITIVE_REGULATION": {
        "id": "GO:0045881",
        "label": "positive regulation of sporulation resulting in formation of a cellular spore",
    },
}


def support(gene: str, filename: str, text: str) -> dict[str, str]:
    return {
        "reference_id": f"file:PSEPK/{gene}/{filename}",
        "supporting_text": text,
    }


def goa_support(gene: str, text: str) -> dict[str, str]:
    return support(gene, f"{gene}-goa.tsv", text)


def uniprot_support(gene: str, text: str) -> dict[str, str]:
    return support(gene, f"{gene}-uniprot.txt", text)


def set_review(entry: dict, summary: str, action: str, reason: str, supported_by: list[dict], replacements=None) -> None:
    review = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    entry["review"] = review


def ensure_references(doc: dict, gene: str, accession: str) -> None:
    existing: dict[str, dict] = {ref["id"]: ref for ref in doc.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        if any(ann.get("original_reference_id") == ref_id for ann in doc.get("existing_annotations", [])):
            existing.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})
    existing[f"file:PSEPK/{gene}/{gene}-goa.tsv"] = {
        "id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
        "title": f"QuickGO GOA annotations for {gene}",
        "findings": [],
    }
    existing[f"file:PSEPK/{gene}/{gene}-uniprot.txt"] = {
        "id": f"file:PSEPK/{gene}/{gene}-uniprot.txt",
        "title": f"UniProtKB entry for {gene} ({accession})",
        "findings": [],
    }
    existing[f"file:PSEPK/{gene}/{gene}-deep-research-asta.md"] = {
        "id": f"file:PSEPK/{gene}/{gene}-deep-research-asta.md",
        "title": f"Asta retrieval report for {gene} ({accession})",
        "findings": [
            {
                "statement": "Asta generated a retrieval-only report seeded with the UniProt accession and domain context.",
                "supporting_text": f"- **UniProt Accession:** {accession}",
            }
        ],
    }
    doc["references"] = list(existing.values())


DATA = {
    "parB": {
        "id": "P0A151",
        "description": "parB encodes the ParB/Spo0J-family origin-region chromosome partition protein of Pseudomonas putida KT2440. UniProt describes it as a probable chromosome-partitioning protein that binds the DNA origin region and localizes to both poles after DNA replication. In this boundary module it is treated as the origin-associated ParB component for chromosome segregation; the sporulation process annotation is an over-propagated Spo0J-family term that is not a Pseudomonas-specific role.",
        "reviews": {
            "GO:0003677": (
                "ACCEPT",
                "DNA binding is a core molecular-function annotation for ParB.",
                "ParB-family partition proteins bind origin-region/parS DNA, and the InterPro-supported GOA row assigns DNA binding.",
                [goa_support("parB", "GO:0003677\tDNA binding"), uniprot_support("parB", "to the DNA origin of replication")],
                None,
            ),
            "GO:0005694": (
                "ACCEPT",
                "Chromosome localization is appropriate for an origin-region ParB partition protein.",
                "The TreeGrafter chromosome component annotation is consistent with UniProt's chromosome-partitioning description and origin-DNA binding.",
                [goa_support("parB", "GO:0005694\tchromosome"), uniprot_support("parB", "Involved in chromosome partition")],
                None,
            ),
            "GO:0007059": (
                "ACCEPT",
                "Chromosome segregation is the core biological process for ParB.",
                "UniProt describes ParB as involved in chromosome partition and GOA assigns chromosome segregation through TreeGrafter.",
                [goa_support("parB", "GO:0007059\tchromosome segregation"), uniprot_support("parB", "Involved in chromosome partition")],
                None,
            ),
            "GO:0045881": (
                "REMOVE",
                "The sporulation annotation is an inappropriate family-level spillover for P. putida parB.",
                "The supported local role is chromosome partition/origin-DNA binding; the GOA sporulation term comes from the ParB/Spo0J family context and is not a KT2440 chromosome-partition function.",
                [
                    goa_support("parB", "GO:0045881\tpositive regulation of sporulation resulting in formation of a cellular spore"),
                    uniprot_support("parB", "Involved in chromosome partition"),
                    uniprot_support("parB", "Belongs to the ParB family."),
                ],
                None,
            ),
        },
        "core_functions": [
            {
                "description": "Origin-region ParB/Spo0J-family DNA-binding chromosome partition protein involved in chromosome segregation.",
                "molecular_function": TERMS["DNA_BINDING"],
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "locations": [TERMS["CHROMOSOME"]],
                "supported_by": [
                    uniprot_support("parB", "Involved in chromosome partition"),
                    uniprot_support("parB", "to the DNA origin of replication"),
                    goa_support("parB", "GO:0007059\tchromosome segregation"),
                ],
            }
        ],
        "questions": ["Is PP_0002 the missing Soj/ParA-like ATPase partner for the origin-proximal parB locus in KT2440?"],
    },
    "PP_0002": {
        "id": "P0A149",
        "description": "PP_0002 encodes an origin-proximal uncharacterized P-loop/AAA-family protein immediately adjacent to parB. UniProt notes similarity to Bacillus subtilis Soj, and InterPro/PANTHER assign DNA partitioning ATPase and AAA-family signatures. This makes PP_0002 the strongest hole-filling candidate for the ParA/Soj side of the parB chromosome-partition locus, but it remains functionally uncharacterized in KT2440.",
        "core_functions": [
            {
                "description": "Putative Soj/ParA-like DNA-partitioning ATPase candidate adjacent to parB; likely part of the origin-region chromosome-partition system, but still unresolved experimentally.",
                "molecular_function": TERMS["ATP_HYDROLYSIS"],
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "supported_by": [
                    uniprot_support("PP_0002", "To B.subtilis soj."),
                    uniprot_support("PP_0002", "DR   InterPro; IPR050678; DNA_Partitioning_ATPase."),
                    uniprot_support("PP_0002", "DR   InterPro; IPR027417; P-loop_NTPase."),
                    uniprot_support("PP_0002", "DR   PANTHER; PTHR13696:SF52; PARA FAMILY PROTEIN CT_582; 1."),
                ],
            }
        ],
        "questions": ["Does PP_0002 bind ATP and function with ParB at the KT2440 origin-region partition locus, or is it a retained but nonessential ParA-like paralog?"],
    },
    "PP_0693": {
        "id": "Q88Q05",
        "description": "PP_0693 encodes a large coiled-coil MksF-family protein annotated by UniProt's automated name model as a chromosome partitioning protein ParA, but its domain evidence is MksF/condensinMksF rather than a ParA-family P-loop ATPase. It is retained in the chromosome partition/condensation boundary as a likely MksEF-family condensin-associated candidate whose precise KT2440 role is unresolved.",
        "core_functions": [
            {
                "description": "Candidate MksF/condensin-family chromosome organization factor; no catalytic molecular function is asserted in this first pass.",
                "directly_involved_in": [TERMS["CHROMOSOME_ORGANIZATION"]],
                "supported_by": [
                    uniprot_support("PP_0693", "DR   InterPro; IPR047714; MksF_put-like."),
                    uniprot_support("PP_0693", "DR   NCBIfam; NF040859; condensinMksF; 1."),
                    uniprot_support("PP_0693", "KW   Coiled coil"),
                ],
            }
        ],
        "questions": ["Does PP_0693 form a MksEF condensin-associated module with PP_0694 in P. putida KT2440?"],
    },
    "PP_0694": {
        "id": "Q88Q04",
        "description": "PP_0694 encodes an MksE/MukE-like protein adjacent to the MksF-like PP_0693. The UniProt automated name is a generic chromosome-partitioning protein, but the stronger evidence is MksE, MukE_N, and condensinMksE domain classification. It is therefore curated as an unresolved MksE-family chromosome organization/condensation candidate rather than as a ParA ATPase.",
        "core_functions": [
            {
                "description": "Candidate MksE/MukE-like condensin-associated chromosome organization factor paired with PP_0693.",
                "directly_involved_in": [TERMS["CHROMOSOME_ORGANIZATION"]],
                "supported_by": [
                    uniprot_support("PP_0694", "DR   InterPro; IPR053841; MksE."),
                    uniprot_support("PP_0694", "DR   InterPro; IPR042038; MukE_N."),
                    uniprot_support("PP_0694", "DR   NCBIfam; NF040858; condensinMksE; 1."),
                ],
            }
        ],
        "questions": ["Is PP_0694 the MksE partner of PP_0693, and does the pair act in chromosome organization rather than plasmid-like partitioning?"],
    },
    "PP_2161": {
        "id": "Q88KX8",
        "description": "PP_2161 encodes a short DUF4404/coiled-coil protein that UniProt's automated name model labels as chromosome partitioning protein ParA, but it lacks the canonical ParA/P-loop ATPase signatures seen in PP_0002 and other ParA-family loci. It is retained as an unresolved chromosome-partition bucket candidate, not as a confident ATPase or core ParA component.",
        "core_functions": [
            {
                "description": "Unresolved short DUF4404 coiled-coil protein currently only weakly connected to chromosome partitioning by automated naming.",
                "supported_by": [
                    uniprot_support("PP_2161", "DR   InterPro; IPR025516; DUF4404."),
                    uniprot_support("PP_2161", "DR   Pfam; PF14357; DUF4404; 1."),
                    uniprot_support("PP_2161", "KW   Coiled coil"),
                ],
            }
        ],
        "questions": ["Is PP_2161 a real chromosome-partition accessory protein, or an automated-name false positive from the broad functional bucket?"],
    },
    "PP_2412": {
        "id": "Q88K79",
        "description": "PP_2412 encodes a ParA-family P-loop/AAA protein with InterPro DNA_Partitioning_ATPase and PANTHER ParA-family signatures. No GOA annotations were present in this first pass, so it is treated as a candidate DNA-partitioning ATPase whose specific chromosomal, plasmid, or mobile-element context remains unresolved.",
        "core_functions": [
            {
                "description": "Candidate ParA-family DNA-partitioning ATPase; pathway assignment should remain provisional until its genomic context and partner proteins are resolved.",
                "molecular_function": TERMS["ATP_HYDROLYSIS"],
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "supported_by": [
                    uniprot_support("PP_2412", "DR   InterPro; IPR050678; DNA_Partitioning_ATPase."),
                    uniprot_support("PP_2412", "DR   InterPro; IPR027417; P-loop_NTPase."),
                    uniprot_support("PP_2412", "DR   PANTHER; PTHR13696:SF52; PARA FAMILY PROTEIN CT_582; 1."),
                ],
            }
        ],
        "questions": ["Does PP_2412 participate in chromosome segregation in KT2440, or does it belong to a paralogous plasmid/mobile-element partition system?"],
    },
    "PP_3700": {
        "id": "Q88GM1",
        "description": "PP_3700 encodes an AAA/P-loop protein named as an ATPase involved in chromosome partitioning and additionally carries Cro/C1-type helix-turn-helix DNA-binding signatures. Its only seeded GOA term is DNA binding, which is supported by the HTH domain. The broader chromosome-partition role is plausible but should remain provisional until a partner/context is established.",
        "reviews": {
            "GO:0003677": (
                "ACCEPT",
                "DNA binding is supported for PP_3700.",
                "The GOA row is InterPro-derived from a lambda-like DNA-binding domain, and UniProt records Cro/C1-type HTH and Lambda DNA-binding superfamily signatures.",
                [
                    goa_support("PP_3700", "GO:0003677\tDNA binding"),
                    uniprot_support("PP_3700", "DR   InterPro; IPR001387; Cro/C1-type_HTH."),
                    uniprot_support("PP_3700", "DR   InterPro; IPR010982; Lambda_DNA-bd_dom_sf."),
                ],
                None,
            )
        },
        "core_functions": [
            {
                "description": "DNA-binding AAA/P-loop candidate partition ATPase with an HTH domain; likely chromosome-partition related but unresolved at the module level.",
                "molecular_function": TERMS["DNA_BINDING"],
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "supported_by": [
                    goa_support("PP_3700", "GO:0003677\tDNA binding"),
                    uniprot_support("PP_3700", "SubName: Full=ATPases involved in chromosome partitioning"),
                    uniprot_support("PP_3700", "DR   InterPro; IPR001387; Cro/C1-type_HTH."),
                    uniprot_support("PP_3700", "DR   InterPro; IPR025669; AAA_dom."),
                ],
            }
        ],
        "questions": ["What is the cognate DNA site or partner protein for PP_3700, and is its partition ATPase role chromosomal or plasmid/mobile-element associated?"],
    },
    "smc": {
        "id": "Q88F23",
        "description": "smc encodes the bacterial structural maintenance of chromosomes protein Smc. UniProt/HAMAP describes it as required for chromosome condensation and partitioning, with ATP-hydrolysis domains at the termini, a hinge domain, and long coiled coils. In KT2440 it is the core SMC condensin subunit of the Smc-ScpA-ScpB chromosome organization/segregation machinery.",
        "reviews": {
            "GO:0003677": (
                "ACCEPT",
                "DNA binding is appropriate for bacterial Smc.",
                "UniRule assigns DNA binding to Smc, which functions on chromosomal DNA during condensation and partitioning.",
                [goa_support("smc", "GO:0003677\tDNA binding"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                None,
            ),
            "GO:0005524": (
                "KEEP_AS_NON_CORE",
                "ATP binding is correct but less informative than ATP hydrolysis activity.",
                "Smc has terminal ATP-hydrolysis domains; ATP binding is a supporting feature rather than the most informative core molecular function.",
                [goa_support("smc", "GO:0005524\tATP binding"), uniprot_support("smc", "globular domains required for ATP hydrolysis")],
                None,
            ),
            "GO:0005694": (
                "ACCEPT",
                "Chromosome is an appropriate location/context for Smc activity.",
                "Smc is required for chromosome condensation and partitioning, and InterPro assigns chromosome localization.",
                [goa_support("smc", "GO:0005694\tchromosome"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                None,
            ),
            "GO:0005737": (
                "ACCEPT",
                "Cytoplasm localization is appropriate for bacterial Smc.",
                "UniProt/HAMAP records Smc as cytoplasmic.",
                [goa_support("smc", "GO:0005737\tcytoplasm"), uniprot_support("smc", "SUBCELLULAR LOCATION: Cytoplasm")],
                None,
            ),
            "GO:0006260": (
                "KEEP_AS_NON_CORE",
                "DNA replication is a plausible secondary context but not the core Smc function.",
                "The supported core role is chromosome condensation, organization, and partitioning; DNA replication is retained as non-core propagated context.",
                [goa_support("smc", "GO:0006260\tDNA replication"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                None,
            ),
            "GO:0007059": (
                "ACCEPT",
                "Chromosome segregation is a core Smc process annotation.",
                "UniProt/HAMAP explicitly describes Smc as required for chromosome partitioning.",
                [goa_support("smc", "GO:0007059\tchromosome segregation"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                None,
            ),
            "GO:0007062": (
                "MODIFY",
                "Sister chromatid cohesion is too eukaryotic/specific for the bacterial Smc condensin role.",
                "For KT2440 Smc, chromosome organization and chromosome condensation capture the supported bacterial role more directly than sister chromatid cohesion.",
                [goa_support("smc", "GO:0007062\tsister chromatid cohesion"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                [TERMS["CHROMOSOME_ORGANIZATION"], TERMS["CHROMOSOME_CONDENSATION"]],
            ),
            "GO:0016887": (
                "ACCEPT",
                "ATP hydrolysis activity is the most informative molecular function for Smc.",
                "UniProt/HAMAP records ATP-hydrolysis domains and InterPro assigns ATP hydrolysis activity.",
                [goa_support("smc", "GO:0016887\tATP hydrolysis activity"), uniprot_support("smc", "globular domains required for ATP hydrolysis")],
                None,
            ),
            "GO:0030261": (
                "ACCEPT",
                "Chromosome condensation is a core Smc process annotation.",
                "UniProt/HAMAP describes Smc as required for chromosome condensation and partitioning.",
                [goa_support("smc", "GO:0030261\tchromosome condensation"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                None,
            ),
            "GO:0051276": (
                "ACCEPT",
                "Chromosome organization is an appropriate broad core process for Smc.",
                "Smc is the central bacterial SMC condensin subunit organizing chromosomes for condensation and partitioning.",
                [goa_support("smc", "GO:0051276\tchromosome organization"), uniprot_support("smc", "Required for chromosome condensation and partitioning.")],
                None,
            ),
        },
        "core_functions": [
            {
                "description": "ATP-hydrolyzing SMC condensin subunit required for bacterial chromosome condensation, organization, and segregation.",
                "molecular_function": TERMS["ATP_HYDROLYSIS"],
                "directly_involved_in": [TERMS["CHROMOSOME_CONDENSATION"], TERMS["CHROMOSOME_ORGANIZATION"], TERMS["CHROMOSOME_SEGREGATION"]],
                "locations": [TERMS["CYTOPLASM"], TERMS["CHROMOSOME"]],
                "supported_by": [
                    uniprot_support("smc", "Required for chromosome condensation and partitioning."),
                    uniprot_support("smc", "globular domains required for ATP hydrolysis"),
                    goa_support("smc", "GO:0016887\tATP hydrolysis activity"),
                    goa_support("smc", "GO:0030261\tchromosome condensation"),
                ],
            }
        ],
        "questions": ["What are the localization dynamics of Smc and its ScpA/ScpB partners during the P. putida KT2440 cell cycle?"],
    },
    "PP_4334": {
        "id": "Q88EW8",
        "description": "PP_4334 encodes a ParA-family P-loop/AAA protein with DNA_Partitioning_ATPase and PANTHER plasmid-partitioning-protein-related signatures. With no seeded GOA rows and no clear partner in this first pass, it is retained as a candidate partition ATPase rather than assigned confidently to the core chromosomal ParAB system.",
        "core_functions": [
            {
                "description": "Candidate ParA-family DNA-partitioning ATPase, possibly plasmid/mobile-element associated rather than core chromosomal.",
                "molecular_function": TERMS["ATP_HYDROLYSIS"],
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "supported_by": [
                    uniprot_support("PP_4334", "DR   InterPro; IPR050678; DNA_Partitioning_ATPase."),
                    uniprot_support("PP_4334", "DR   InterPro; IPR027417; P-loop_NTPase."),
                    uniprot_support("PP_4334", "DR   PANTHER; PTHR13696:SF69; PLASMID PARTITIONING PROTEIN-RELATED; 1."),
                ],
            }
        ],
        "questions": ["Is PP_4334 associated with a plasmid/mobile-element partition module rather than the primary chromosome partition system?"],
    },
    "PP_4497": {
        "id": "Q88EG7",
        "description": "PP_4497 encodes the ScpB-family segregation and condensation protein B immediately upstream of scpA. Its InterPro/PANTHER/Pfam signatures support a Smc-ScpAB condensin accessory subunit involved in chromosome separation/segregation rather than an independent catalytic protein.",
        "reviews": {
            "GO:0051304": (
                "ACCEPT",
                "Chromosome separation is appropriate for ScpB-family PP_4497.",
                "PP_4497 carries ScpB chromosome-segregation signatures and sits next to scpA in the Smc-ScpAB condensin submodule.",
                [
                    goa_support("PP_4497", "GO:0051304\tchromosome separation"),
                    uniprot_support("PP_4497", "DR   InterPro; IPR005234; ScpB_csome_segregation."),
                    uniprot_support("PP_4497", "DR   PANTHER; PTHR34298:SF2; SEGREGATION AND CONDENSATION PROTEIN B; 1."),
                ],
                None,
            )
        },
        "core_functions": [
            {
                "description": "ScpB-family accessory subunit of the bacterial Smc-ScpAB condensin machinery involved in chromosome separation/segregation.",
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "supported_by": [
                    goa_support("PP_4497", "GO:0051304\tchromosome separation"),
                    uniprot_support("PP_4497", "DR   InterPro; IPR005234; ScpB_csome_segregation."),
                    uniprot_support("PP_4497", "KW   Chromosome partition"),
                ],
            }
        ],
        "questions": ["Should PP_4497 be assigned the gene symbol scpB in project-level documentation for this organism?"],
    },
    "scpA": {
        "id": "Q88EG6",
        "description": "scpA encodes segregation and condensation protein A, the kleisin-like accessory component of the bacterial Smc-ScpA-ScpB condensin complex. UniProt/HAMAP states that ScpA participates in chromosomal partition during cell division and binds Smc with ScpB to support DNA association of the complex.",
        "reviews": {
            "GO:0005737": (
                "ACCEPT",
                "Cytoplasm is an appropriate location for ScpA.",
                "UniProt/HAMAP records ScpA as cytoplasmic and describes nucleoid-associated foci.",
                [goa_support("scpA", "GO:0005737\tcytoplasm"), uniprot_support("scpA", "SUBCELLULAR LOCATION: Cytoplasm")],
                None,
            ),
            "GO:0006260": (
                "KEEP_AS_NON_CORE",
                "DNA replication is plausible propagated context but not the core ScpA role.",
                "The more direct supported role is chromosomal partition/chromosome segregation through the Smc-ScpAB complex.",
                [goa_support("scpA", "GO:0006260\tDNA replication"), uniprot_support("scpA", "Participates in chromosomal partition during cell division.")],
                None,
            ),
            "GO:0007059": (
                "ACCEPT",
                "Chromosome segregation is a core process annotation for ScpA.",
                "UniProt/HAMAP describes ScpA as participating in chromosomal partition and as part of the ScpA/ScpB/Smc complex required for DNA association.",
                [goa_support("scpA", "GO:0007059\tchromosome segregation"), uniprot_support("scpA", "Participates in chromosomal partition during cell division.")],
                None,
            ),
        },
        "core_functions": [
            {
                "description": "ScpA kleisin-like accessory subunit of the Smc-ScpAB condensin complex participating in chromosomal partition during cell division.",
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"], TERMS["CELL_DIVISION"]],
                "locations": [TERMS["CYTOPLASM"]],
                "supported_by": [
                    uniprot_support("scpA", "Participates in chromosomal partition during cell division."),
                    uniprot_support("scpA", "Component of a cohesin-like complex composed of ScpA, ScpB and"),
                    goa_support("scpA", "GO:0007059\tchromosome segregation"),
                ],
            }
        ],
        "questions": ["Does ScpA form discrete nucleoid-associated foci in KT2440 as predicted from HAMAP-transferred evidence?"],
    },
    "PP_5070": {
        "id": "Q88CW0",
        "description": "PP_5070 encodes a ParA-family P-loop/AAA protein with InterPro DNA_Partitioning_ATPase and PANTHER ParA-family signatures. It has no seeded GOA annotations in this first pass and is retained as a candidate partition ATPase with unresolved chromosomal versus mobile-element context.",
        "core_functions": [
            {
                "description": "Candidate ParA-family DNA-partitioning ATPase; specific partner and biological context remain unresolved.",
                "molecular_function": TERMS["ATP_HYDROLYSIS"],
                "directly_involved_in": [TERMS["CHROMOSOME_SEGREGATION"]],
                "supported_by": [
                    uniprot_support("PP_5070", "DR   InterPro; IPR050678; DNA_Partitioning_ATPase."),
                    uniprot_support("PP_5070", "DR   InterPro; IPR027417; P-loop_NTPase."),
                    uniprot_support("PP_5070", "DR   PANTHER; PTHR13696:SF52; PARA FAMILY PROTEIN CT_582; 1."),
                ],
            }
        ],
        "questions": ["Does PP_5070 belong to a chromosome-partition module or a paralogous mobile-element/plasmid partition system?"],
    },
}


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    with path.open() as stream:
        doc = yaml.safe_load(stream)

    doc["id"] = cfg["id"]
    doc["gene_symbol"] = gene
    doc["product_type"] = "PROTEIN"
    doc["status"] = "DRAFT"
    doc["taxon"] = TAXON
    doc["description"] = cfg["description"]

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        if term_id in cfg.get("reviews", {}):
            action, summary, reason, supported_by, replacements = cfg["reviews"][term_id]
            set_review(ann, summary, action, reason, supported_by, replacements)

    doc["core_functions"] = cfg.get("core_functions", [])
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [{"question": question} for question in cfg.get("questions", [])]
    doc["suggested_experiments"] = [
        {
            "description": "Perform native-locus fluorescent tagging or pulldown/co-immunoprecipitation of the candidate partition/condensin protein and test colocalization or interaction with its predicted ParB, Smc, ScpA, or ScpB partner during the KT2440 cell cycle.",
            "experiment_type": "cell-cycle localization and protein-interaction assay",
        }
    ]

    ensure_references(doc, gene, cfg["id"])

    with path.open("w") as stream:
        yaml.safe_dump(doc, stream, sort_keys=False, width=1000)


def main() -> None:
    for gene, cfg in DATA.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
