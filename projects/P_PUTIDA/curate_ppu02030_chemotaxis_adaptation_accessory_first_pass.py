#!/usr/bin/env python3
"""First-pass curation for ppu02030 chemotaxis adaptation/accessory genes."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def review(
    summary: str,
    action: str,
    reason: str,
    supported_by: list[dict[str, str]] | None = None,
    proposed_replacement_terms: list[dict[str, str]] | None = None,
) -> dict:
    data: dict = {"summary": summary, "action": action, "reason": reason}
    if proposed_replacement_terms:
        data["proposed_replacement_terms"] = proposed_replacement_terms
    if supported_by:
        data["supported_by"] = supported_by
    return data


GO_REF_INTERPRO = {
    "id": "GO_REF:0000002",
    "title": "Gene Ontology annotation through association of InterPro records with GO terms",
    "findings": [],
}
GO_REF_UNIRULE_TRANSFER = {
    "id": "GO_REF:0000104",
    "title": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "findings": [],
}
GO_REF_COMBINED = {
    "id": "GO_REF:0000120",
    "title": "Combined Automated Annotation using Multiple IEA Methods",
    "findings": [],
}


def write_review(
    gene: str,
    description: str,
    references: list[dict],
    reviews: dict[str, dict],
    core_functions: list[dict],
    questions: list[str],
    experiments: list[str],
    aliases: list[str] | None = None,
) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    if aliases:
        data["aliases"] = aliases
    data["description"] = description
    for annotation in data["existing_annotations"]:
        annotation["review"] = reviews[annotation["term"]["id"]]
    data["references"] = references
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": question} for question in questions]
    data["suggested_experiments"] = [{"description": experiment} for experiment in experiments]
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=88),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def chev_like(gene: str, accession: str, product: str, subfamily: str) -> None:
    uniprot = f"UniProt:{accession}"
    references = [
        GO_REF_INTERPRO,
        {
            "id": uniprot,
            "title": f"UniProt entry {accession} for Pseudomonas putida KT2440 {gene}",
            "findings": [
                {
                    "statement": f"UniProt identifies {gene} as a CheV/CheW-response-regulator-like chemotaxis protein.",
                    "supporting_text": product,
                },
                {
                    "statement": "The protein carries both CheW-like and response-regulator receiver-domain signatures.",
                    "supporting_text": "DR   InterPro; IPR024181; Chemotax_regulator_CheV.",
                },
            ],
        },
        {
            "id": f"file:PSEPK/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt/domain context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0000160": review(
            "The phosphorelay process annotation is appropriate for a CheV-like protein with a response-regulator receiver domain.",
            "ACCEPT",
            "CheV-like proteins combine CheW-like coupling domains with a receiver domain, so the InterPro phosphorelay call is a reasonable first-pass process annotation.",
            [
                ref(uniprot, "DR   InterPro; IPR024181; Chemotax_regulator_CheV."),
                ref(uniprot, "DR   Pfam; PF00072; Response_reg; 1."),
                ref(uniprot, "DR   GO; GO:0000160; P:phosphorelay signal transduction system; IEA:InterPro."),
            ],
        ),
        "GO:0006935": review(
            "Chemotaxis is an appropriate process annotation for this CheV-like accessory protein.",
            "ACCEPT",
            "The protein is annotated as chemotaxis/CheV-like and carries CheW-like plus receiver-domain signatures associated with bacterial chemotaxis signaling.",
            [
                ref(uniprot, product),
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:InterPro."),
                ref(uniprot, "DR   Pfam; PF01584; CheW; 1."),
            ],
        ),
        "GO:0007165": review(
            "Signal transduction is true only as a broad parent term and adds little beyond chemotaxis and phosphorelay signaling.",
            "MARK_AS_OVER_ANNOTATED",
            "The more informative existing annotations are chemotaxis and phosphorelay signal transduction system; the broad signal-transduction parent should not be treated as core.",
            [ref(uniprot, "DR   GO; GO:0007165; P:signal transduction; IEA:InterPro.")],
        ),
    }
    core_functions = [
        {
            "description": f"{gene} is a CheV-like chemotaxis accessory candidate with an N-terminal CheW-like adaptor region and a C-terminal receiver domain. It is retained as part of the chemotaxis adaptation/accessory boundary rather than the core CheA/CheY/CheZ/CheB1 cluster.",
            "directly_involved_in": [
                {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
                {"id": "GO:0006935", "label": "chemotaxis"},
            ],
            "supported_by": [
                ref(uniprot, "DR   InterPro; IPR024181; Chemotax_regulator_CheV."),
                ref(uniprot, "DR   Pfam; PF01584; CheW; 1."),
                ref(uniprot, "DR   Pfam; PF00072; Response_reg; 1."),
            ],
        }
    ]
    write_review(
        gene,
        f"{gene} encodes a predicted CheV-like chemotaxis accessory protein in Pseudomonas putida KT2440. The protein has a CheW-like adaptor domain and a receiver-domain response-regulator region, consistent with a non-core chemotaxis signaling/adaptation role. Its specific receptor partners and relationship to the PP_4332-PP_4340 core Che cluster remain unresolved in this first pass.",
        references,
        reviews,
        core_functions,
        [
            f"Which methyl-accepting chemotaxis receptors require {gene} for signaling or adaptation?",
            f"Does {gene} act redundantly with the other CheV-like proteins in KT2440 or in a distinct chemosensory branch?",
        ],
        [
            f"Delete {gene} alone and in combination with other CheV-like genes, then measure chemotaxis toward malate, amino acids, and root-exudate mixtures.",
            f"Map {gene} interaction partners among KT2440 MCPs and CheA/CheW-like proteins.",
        ],
        aliases=[subfamily] if subfamily else None,
    )


def curate_pp3759() -> None:
    uniprot = "UniProt:Q88GG5"
    references = [
        GO_REF_INTERPRO,
        GO_REF_UNIRULE_TRANSFER,
        GO_REF_COMBINED,
        {
            "id": uniprot,
            "title": "UniProt entry Q88GG5 for Pseudomonas putida KT2440 PP_3759",
            "findings": [
                {
                    "statement": "UniProt identifies PP_3759 as a protein-glutamate methylesterase.",
                    "supporting_text": "RecName: Full=protein-glutamate methylesterase",
                },
                {
                    "statement": "The protein has CheB methylesterase-domain evidence but no explicit receiver-domain feature in the UniProt entry.",
                    "supporting_text": "DR   Pfam; PF01339; CheB_methylest; 1.",
                },
            ],
        },
        {
            "id": "file:PSEPK/PP_3759/PP_3759-deep-research-asta.md",
            "title": "Asta retrieval report for PP_3759 in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt/domain context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0000156": review(
            "The response-regulator activity call is likely over-propagated for this short CheB methylesterase-domain protein.",
            "REMOVE",
            "PP_3759 is 191 aa and the UniProt/Pfam evidence shown for this entry supports a CheB methylesterase catalytic domain rather than an N-terminal receiver-domain response regulator. The specific methylesterase annotation should be retained instead.",
            [
                ref(uniprot, "RecName: Full=protein-glutamate methylesterase"),
                ref(uniprot, "DR   Pfam; PF01339; CheB_methylest; 1."),
            ],
        ),
        "GO:0000160": review(
            "The phosphorelay process annotation is too specific for the available PP_3759 evidence.",
            "MARK_AS_OVER_ANNOTATED",
            "PP_3759 is plausibly a chemotaxis methylesterase, but the fetched evidence does not show a receiver domain or direct phosphorylation by CheA. Chemotaxis is the safer process term.",
            [
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:UniProtKB-UniRule."),
                ref(uniprot, "DR   Pfam; PF01339; CheB_methylest; 1."),
            ],
        ),
        "GO:0005737": review(
            "Cytoplasm is a plausible localization for a soluble CheB-like methylesterase.",
            "ACCEPT",
            "The annotation is broad but consistent with a cytoplasmic-side chemotaxis adaptation enzyme.",
            [ref(uniprot, "DR   GO; GO:0005737; C:cytoplasm; IEA:InterPro.")],
        ),
        "GO:0006935": review(
            "Chemotaxis is an appropriate process annotation for this CheB-like methylesterase.",
            "ACCEPT",
            "The protein has CheB methylesterase-domain evidence and a UniProt chemotaxis process annotation.",
            [
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:UniProtKB-UniRule."),
                ref(uniprot, "KW   Chemotaxis"),
            ],
        ),
        "GO:0008984": review(
            "Protein-glutamate methylesterase activity is the specific retained molecular function.",
            "ACCEPT",
            "The UniProt entry and EC/Rhea mapping support CheB-family demethylation of protein methylglutamate residues.",
            [
                ref(uniprot, "RecName: Full=protein-glutamate methylesterase"),
                ref(uniprot, "DR   GO; GO:0008984; F:protein-glutamate methylesterase activity; IEA:UniProtKB-EC."),
                ref(uniprot, "EC=3.1.1.61"),
            ],
        ),
        "GO:0016787": review(
            "Hydrolase activity is true but too broad for this enzyme.",
            "MARK_AS_OVER_ANNOTATED",
            "The specific protein-glutamate methylesterase activity already captures the relevant hydrolase chemistry.",
            [ref(uniprot, "DR   GO; GO:0008984; F:protein-glutamate methylesterase activity; IEA:UniProtKB-EC.")],
        ),
    }
    core_functions = [
        {
            "description": "PP_3759 is a CheB-like protein-glutamate methylesterase candidate in the chemotaxis adaptation/accessory boundary. It likely contributes to chemotaxis receptor demethylation, but the available first-pass evidence does not support treating it as a full receiver-domain response regulator.",
            "molecular_function": {"id": "GO:0008984", "label": "protein-glutamate methylesterase activity"},
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "supported_by": [
                ref(uniprot, "RecName: Full=protein-glutamate methylesterase"),
                ref(uniprot, "DR   Pfam; PF01339; CheB_methylest; 1."),
            ],
        }
    ]
    write_review(
        "PP_3759",
        "PP_3759 encodes a predicted CheB-like protein-glutamate methylesterase in Pseudomonas putida KT2440. Unlike full-length CheB1, the available UniProt/domain evidence for PP_3759 supports a compact methylesterase-domain protein rather than a complete CheA-phosphorylated receiver-domain response regulator. It is best treated as a chemotaxis adaptation/accessory methylesterase candidate.",
        references,
        reviews,
        core_functions,
        [
            "Which KT2440 MCPs are substrates for PP_3759, and does it act in the same chemotaxis branch as CheR3?",
            "Is PP_3759 regulated by protein-protein interaction rather than by CheA-dependent receiver-domain phosphorylation?",
        ],
        [
            "Assay PP_3759 methylesterase activity against methylated cytoplasmic domains of representative KT2440 MCPs.",
            "Compare chemotaxis adaptation kinetics in PP_3759, cheB1, and combined mutant backgrounds.",
        ],
    )


def curate_cher3() -> None:
    uniprot = "UniProt:Q88GG4"
    pmid = "PMID:23677992"
    references = [
        GO_REF_INTERPRO,
        {
            "id": uniprot,
            "title": "UniProt entry Q88GG4 for Pseudomonas putida KT2440 CheR3",
            "findings": [
                {
                    "statement": "UniProt identifies CheR3 as a putative CheR-family methyltransferase.",
                    "supporting_text": "RecName: Full=Putative methyltransferase Cher3",
                },
                {
                    "statement": "The UniProt disruption phenotype reports no effect on chemotaxis or biofilm formation.",
                    "supporting_text": "Mutation does not affect chemotaxis and biofilm formation.",
                },
            ],
        },
        {
            "id": pmid,
            "title": "High specificity in CheR methyltransferase function: CheR2 of Pseudomonas putida is essential for chemotaxis, whereas CheR1 is involved in biofilm formation.",
            "findings": [
                {
                    "statement": "CheR2, but not the other CheR paralogues, methylates McpS and McpT in the abstract-level cache.",
                    "supporting_text": "Methylation assays show that CheR2, but not the other paralogues, methylates the McpS and McpT chemotaxis receptors.",
                    "full_text_unavailable": True,
                }
            ],
        },
        {
            "id": "file:PSEPK/cheR3/cheR3-deep-research-asta.md",
            "title": "Asta retrieval report for cheR3 in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt and cached PMID context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0008757": review(
            "SAM-dependent methyltransferase activity is a conservative annotation for CheR3.",
            "ACCEPT",
            "CheR3 has CheR-family methyltransferase domains, but available first-pass evidence does not support the more specific McpS/McpT protein-glutamate O-methyltransferase assignment used for CheR2.",
            [
                ref(uniprot, "RecName: Full=Putative methyltransferase Cher3"),
                ref(uniprot, "DR   InterPro; IPR000780; CheR_MeTrfase."),
                ref(pmid, "Methylation assays show that CheR2, but not the other paralogues, methylates the McpS and McpT chemotaxis receptors."),
            ],
        )
    }
    core_functions = [
        {
            "description": "CheR3 is a CheR-family SAM-dependent methyltransferase candidate. Unlike CheR2, available first-pass evidence does not establish a chemotaxis-essential MCP substrate or biofilm phenotype for CheR3.",
            "molecular_function": {"id": "GO:0008757", "label": "S-adenosylmethionine-dependent methyltransferase activity"},
            "supported_by": [
                ref(uniprot, "RecName: Full=Putative methyltransferase Cher3"),
                ref(uniprot, "Mutation does not affect chemotaxis and biofilm formation."),
            ],
        }
    ]
    write_review(
        "cheR3",
        "CheR3 is a putative CheR-family SAM-dependent methyltransferase in Pseudomonas putida KT2440. It is related to chemotaxis receptor methyltransferases, but the available first-pass evidence distinguishes it from CheR2: the cached CheR paralog study reports CheR2 as the McpS/McpT methyltransferase and chemotaxis-essential paralog, while UniProt reports that cheR3 disruption does not affect chemotaxis or biofilm formation. CheR3 should therefore remain a methyltransferase candidate with unresolved biological target rather than a core chemotaxis methyltransferase.",
        references,
        reviews,
        core_functions,
        [
            "What is the in vivo substrate of CheR3, if any, in KT2440?",
            "Does CheR3 act under conditions or with receptors not tested in the CheR paralog study?",
        ],
        [
            "Test purified CheR3 against a broader panel of KT2440 MCP cytoplasmic domains and compare substrate specificity with CheR2.",
            "Profile chemotaxis and receptor methylation phenotypes for cheR3 under alternative growth conditions and attractant panels.",
        ],
    )


def curate_cher2() -> None:
    uniprot = "UniProt:Q88ER1"
    pmid = "PMID:23677992"
    references = [
        GO_REF_INTERPRO,
        GO_REF_COMBINED,
        {
            "id": uniprot,
            "title": "UniProt entry Q88ER1 for Pseudomonas putida KT2440 CheR2",
            "findings": [
                {
                    "statement": "UniProt describes CheR2 as the McpS chemotaxis receptor methyltransferase.",
                    "supporting_text": "Methylates the McpS chemotaxis receptor.",
                },
                {
                    "statement": "UniProt reports that cheR2 mutants are deficient in chemotaxis.",
                    "supporting_text": "Mutants are deficient in chemotaxis toward malate and casamino acids.",
                },
            ],
        },
        {
            "id": pmid,
            "title": "High specificity in CheR methyltransferase function: CheR2 of Pseudomonas putida is essential for chemotaxis, whereas CheR1 is involved in biofilm formation.",
            "findings": [
                {
                    "statement": "The abstract reports that CheR2 methylates McpS and McpT and that the CheR2 mutant is chemotaxis deficient.",
                    "supporting_text": "Methylation assays show that CheR2, but not the other paralogues, methylates the McpS and McpT chemotaxis receptors.",
                    "full_text_unavailable": True,
                }
            ],
        },
        {
            "id": "file:PSEPK/cheR2/cheR2-deep-research-asta.md",
            "title": "Asta retrieval report for cheR2 in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt and cached PMID context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0008757": review(
            "This broad SAM-dependent methyltransferase annotation is correct but less informative than the specific protein-glutamate O-methyltransferase term already present.",
            "MODIFY",
            "CheR2 methylates methyl-accepting chemotaxis receptors using SAM, but GO:0008983 captures the specific protein-glutamate methyltransferase chemistry better.",
            [
                ref(uniprot, "Methylation of the membrane-bound methyl-accepting chemotaxis proteins (MCP)"),
                ref(pmid, "Methylation assays show that CheR2, but not the other paralogues, methylates the McpS and McpT chemotaxis receptors."),
            ],
            [{"id": "GO:0008983", "label": "protein-glutamate O-methyltransferase activity"}],
        ),
        "GO:0008983": review(
            "Protein-glutamate O-methyltransferase activity is the core CheR2 molecular function.",
            "ACCEPT",
            "CheR2 methylates membrane-bound methyl-accepting chemotaxis proteins, with direct evidence for McpS and abstract-level evidence for McpT.",
            [
                ref(uniprot, "Methylates the McpS chemotaxis receptor."),
                ref(uniprot, "EC=2.1.1.80"),
                ref(pmid, "Methylation assays show that CheR2, but not the other paralogues, methylates the McpS and McpT chemotaxis receptors."),
            ],
        ),
    }
    core_functions = [
        {
            "description": "CheR2 is the chemotaxis receptor protein-glutamate O-methyltransferase for the KT2440 chemotaxis adaptation system. It methylates methyl-accepting chemotaxis proteins, including McpS, and cheR2 mutants are deficient in chemotaxis toward malate and casamino acids.",
            "molecular_function": {"id": "GO:0008983", "label": "protein-glutamate O-methyltransferase activity"},
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "supported_by": [
                ref(uniprot, "Methylates the McpS chemotaxis receptor."),
                ref(uniprot, "Mutants are deficient in chemotaxis toward malate and casamino acids."),
                ref(pmid, "The mutant in CheR2 was deficient in chemotaxis"),
            ],
        }
    ]
    write_review(
        "cheR2",
        "CheR2 is the chemotaxis receptor methyltransferase of Pseudomonas putida KT2440. It catalyzes SAM-dependent methylation of methyl-accepting chemotaxis proteins to form gamma-glutamyl methyl ester residues, with direct evidence for McpS and abstract-level evidence for McpT. CheR2 is the CheR paralog tied to chemotaxis in KT2440, as cheR2 mutants are deficient in chemotaxis toward malate and casamino acids, unlike cheR3.",
        references,
        reviews,
        core_functions,
        [
            "Which receptor panel beyond McpS/McpT depends on CheR2 under rhizosphere-like conditions?",
            "How does CheR2 substrate specificity map onto the named MCP receptor panel in ppu02030?",
        ],
        [
            "Measure CheR2 methylation of the KT2440 named MCP receptor panel using purified receptor cytoplasmic domains.",
            "Compare chemotaxis adaptation kinetics of cheR2 mutants across malate, amino-acid, and aromatic-acid attractants.",
        ],
        aliases=["PP_4392"],
    )


def main() -> None:
    chev_like("PP_0802", "Q88PP6", "SubName: Full=Chemotaxis protein", "PTHR47233:SF2")
    chev_like("PP_2128", "Q88L09", "SubName: Full=CheV-like chemotaxis protein", "PTHR47233:SF3")
    curate_pp3759()
    curate_cher3()
    curate_cher2()
    chev_like("PP_4393", "Q88ER0", "SubName: Full=Chemotaxis protein", "PTHR47233:SF3")


if __name__ == "__main__":
    main()
