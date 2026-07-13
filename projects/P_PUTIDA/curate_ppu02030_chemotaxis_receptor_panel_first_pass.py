#!/usr/bin/env python3
"""First-pass curation for ppu02030 named MCP receptor panel genes."""

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


def review(summary: str, action: str, reason: str, supported_by: list[dict[str, str]]) -> dict:
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


GO_REF_INTERPRO = {
    "id": "GO_REF:0000002",
    "title": "Gene Ontology annotation through association of InterPro records with GO terms",
    "findings": [],
}
GO_REF_SUBCELL = {
    "id": "GO_REF:0000044",
    "title": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping",
    "findings": [],
}
GO_REF_ARBA = {
    "id": "GO_REF:0000117",
    "title": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "findings": [],
}
GO_REF_COMBINED = {
    "id": "GO_REF:0000120",
    "title": "Combined Automated Annotation using Multiple IEA Methods",
    "findings": [],
}


GENES = {
    "mcpH": {
        "accession": "Q88R14",
        "aliases": [],
        "description": (
            "mcpH encodes an inner-membrane methyl-accepting chemotaxis protein that "
            "directly recognizes metabolizable purine derivatives, including purine, "
            "adenine, guanine, xanthine, hypoxanthine, and uric acid, and mediates "
            "chemotaxis toward these purine-degradation pathway intermediates."
        ),
        "ligand_summary": "metabolizable purine derivatives",
        "specific_function": (
            "McpH is a purine-derivative chemoreceptor that binds purine, adenine, "
            "guanine, xanthine, hypoxanthine, and uric acid and mediates chemotaxis "
            "toward these purine-degradation intermediates."
        ),
        "pmid": "PMID:26355499",
        "pmid_title": (
            "Identification of a chemoreceptor that specifically mediates chemotaxis "
            "toward metabolizable purine derivatives."
        ),
        "pmid_findings": [
            (
                "McpH recognizes purine and purine derivatives.",
                "recognizes purine and its derivatives",
            ),
            (
                "Loss of mcpH abolishes chemotaxis toward the identified McpH ligands.",
                "Mutation of mcpH abolished chemotaxis",
            ),
        ],
        "uniprot_findings": [
            (
                "UniProt describes McpH as a chemoreceptor for purine-degradation intermediates.",
                "McpH is a chemoreceptor that binds and responds",
            ),
            (
                "UniProt records the relevant ligand set.",
                "guanine and adenine",
            ),
        ],
        "core_support": [
            ref("PMID:26355499", "recognizes purine and its derivatives"),
            ref("PMID:26355499", "Mutation of mcpH abolished chemotaxis"),
        ],
        "has_receptor_mf_goa": False,
    },
    "ctpL": {
        "accession": "Q88QD2",
        "aliases": [],
        "description": (
            "ctpL encodes a predicted membrane methyl-accepting chemotaxis protein in "
            "Pseudomonas putida KT2440. Unlike the other named receptors in this panel, "
            "the fetched first-pass evidence supports MCP-family receptor architecture "
            "and chemotaxis signaling but does not resolve a KT2440 ligand or signaling "
            "branch for CtpL."
        ),
        "ligand_summary": "unresolved chemoeffector",
        "specific_function": (
            "CtpL is an unresolved methyl-accepting chemotaxis receptor candidate with "
            "MCPsignal/HAMP-domain architecture. Its ligand specificity remains a "
            "module-level knowledge gap in KT2440."
        ),
        "pmid": None,
        "pmid_title": None,
        "pmid_findings": [],
        "uniprot_findings": [
            (
                "UniProt identifies CtpL as a methyl-accepting chemotaxis protein.",
                "SubName: Full=Methyl-accepting chemotaxis protein CtpL",
            ),
            (
                "The entry carries membrane-protein annotation.",
                "Multi-pass membrane protein",
            ),
        ],
        "core_support": [
            ref("UniProt:Q88QD2", "SubName: Full=Methyl-accepting chemotaxis protein CtpL"),
            ref("UniProt:Q88QD2", "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt."),
        ],
        "has_receptor_mf_goa": True,
    },
    "mcpU": {
        "accession": "Q88NI1",
        "aliases": [],
        "description": (
            "mcpU encodes an inner-membrane methyl-accepting chemotaxis receptor for "
            "polyamines. The receptor binds putrescine, cadaverine, spermidine, "
            "agmatine, and related amines and mediates chemotaxis toward polyamine "
            "signals that also contribute to plant-root colonization phenotypes."
        ),
        "ligand_summary": "polyamines",
        "specific_function": (
            "McpU is a polyamine chemoreceptor that binds putrescine, cadaverine, "
            "spermidine, agmatine, and lower-affinity amines, mediating chemotaxis "
            "toward these ligands."
        ),
        "pmid": "PMID:26662997",
        "pmid_title": (
            "Assessment of the contribution of chemoreceptor-based signalling to biofilm formation."
        ),
        "pmid_findings": [
            (
                "McpU mediates chemotaxis toward polyamines.",
                "McpU, was found to mediate chemotaxis",
            ),
            (
                "The McpU ligand-binding domain binds key polyamines.",
                "McpU-LBD specifically binds putrescine",
            ),
        ],
        "uniprot_findings": [
            (
                "UniProt describes McpU as a polyamine chemoreceptor.",
                "McpU is a chemoreceptor that binds and mediates chemotaxis",
            ),
            (
                "UniProt records the root-colonization phenotype.",
                "Mutation decreases plant root colonization",
            ),
        ],
        "core_support": [
            ref("PMID:26662997", "McpU, was found to mediate chemotaxis"),
            ref("PMID:26662997", "McpU-LBD specifically binds putrescine"),
        ],
        "has_receptor_mf_goa": False,
    },
    "mcpG": {
        "accession": "Q88N45",
        "aliases": ["pctA"],
        "description": (
            "mcpG encodes an inner-membrane methyl-accepting chemotaxis receptor that "
            "specifically recognizes gamma-aminobutyric acid (GABA). It mediates "
            "GABA chemotaxis and contributes to plant-root colonization behavior in "
            "Pseudomonas putida KT2440."
        ),
        "ligand_summary": "GABA",
        "specific_function": (
            "McpG is a GABA-specific chemoreceptor whose ligand-binding domain binds "
            "GABA tightly and whose deletion reduces GABA-dependent chemotaxis and "
            "root-colonization phenotypes."
        ),
        "pmid": "PMID:25921834",
        "pmid_title": "Specific gamma-aminobutyrate chemotaxis in pseudomonads with different lifestyle.",
        "pmid_findings": [
            (
                "McpG is identified as a GABA-specific chemoreceptor in KT2440.",
                "identification of McpG as a specific GABA chemoreceptor",
            ),
            (
                "Loss of mcpG reduces root colonization that depends on chemotaxis through agar.",
                "deletion of mcpG reduced root colonization",
            ),
        ],
        "uniprot_findings": [
            (
                "UniProt describes McpG as a GABA chemoreceptor.",
                "McpG is a specific gamma-aminobutyric acid (GABA)",
            ),
            (
                "UniProt records reduced GABA chemotaxis and root colonization for mutants.",
                "in GABA chemotaxis and reduces root colonization",
            ),
        ],
        "core_support": [
            ref("PMID:25921834", "identification of McpG as a specific GABA chemoreceptor"),
            ref("PMID:25921834", "deletion of mcpG reduced root colonization"),
        ],
        "has_receptor_mf_goa": True,
    },
    "mcpA": {
        "accession": "Q88KP1",
        "aliases": ["pctB"],
        "description": (
            "mcpA encodes an inner-membrane methyl-accepting chemotaxis receptor for "
            "L-amino acids. The receptor binds multiple proteinogenic amino acids and "
            "mediates amino-acid chemotaxis, with a secondary biofilm phenotype noted "
            "for mutants."
        ),
        "ligand_summary": "L-amino acids",
        "specific_function": (
            "McpA is an L-amino-acid chemoreceptor that binds a panel of proteinogenic "
            "amino acids and mediates chemotaxis toward those compounds."
        ),
        "pmid": "PMID:26662997",
        "pmid_title": (
            "Assessment of the contribution of chemoreceptor-based signalling to biofilm formation."
        ),
        "pmid_findings": [
            (
                "McpA binds multiple proteinogenic amino acids.",
                "McpA, specifically binds 12",
            ),
            (
                "McpA mediates chemotaxis toward those amino acids.",
                "different proteinogenic amino acids and mediates chemotaxis",
            ),
        ],
        "uniprot_findings": [
            (
                "UniProt describes McpA as an amino-acid chemoreceptor.",
                "McpA is a chemoreceptor that binds to 12 different L-amino",
            ),
            (
                "UniProt records the biofilm phenotype for mcpA mutation.",
                "maximal biofilm formation earlier than wild type",
            ),
        ],
        "core_support": [
            ref("PMID:26662997", "McpA, specifically binds 12"),
            ref("PMID:26662997", "different proteinogenic amino acids and mediates chemotaxis"),
        ],
        "has_receptor_mf_goa": False,
    },
    "mcpP": {
        "accession": "Q88IY8",
        "aliases": [],
        "description": (
            "mcpP encodes an inner-membrane methyl-accepting chemotaxis receptor for "
            "short-chain C2 and C3 carboxylic acids. The receptor ligand-binding "
            "domain recognizes acetate, pyruvate, propionate, and L-lactate, and "
            "McpP is the major chemoreceptor for chemotaxis toward these compounds."
        ),
        "ligand_summary": "C2 and C3 carboxylic acids",
        "specific_function": (
            "McpP is the major KT2440 chemoreceptor for acetate, pyruvate, propionate, "
            "and L-lactate."
        ),
        "pmid": "PMID:26048936",
        "pmid_title": "Identification of a Chemoreceptor for C2 and C3 Carboxylic Acids.",
        "pmid_findings": [
            (
                "The McpP ligand-binding domain recognizes acetate, pyruvate, propionate, and L-lactate.",
                "recombinant McpP LBD recognizes acetate, pyruvate, propionate",
            ),
            (
                "Loss of mcpP strongly reduces chemotaxis toward these ligands.",
                "Deletion of the mcpP gene resulted in a dramatic reduction in chemotaxis",
            ),
        ],
        "uniprot_findings": [
            (
                "UniProt describes the C2/C3 carboxylate ligand profile.",
                "McpP is a chemoreceptor that responds specifically to some",
            ),
            (
                "UniProt records reduced chemotaxis in mcpP mutants.",
                "largely reduces chemotaxis to acetate",
            ),
        ],
        "core_support": [
            ref("PMID:26048936", "recombinant McpP LBD recognizes acetate, pyruvate, propionate"),
            ref(
                "PMID:26048936",
                "Deletion of the mcpP gene resulted in a dramatic reduction in chemotaxis",
            ),
        ],
        "has_receptor_mf_goa": True,
    },
    "mcpQ": {
        "accession": "Q88D09",
        "aliases": [],
        "description": (
            "mcpQ encodes an inner-membrane methyl-accepting chemotaxis receptor that "
            "recognizes citrate, especially citrate divalent-metal complexes. It works "
            "alongside broad-range McpS to cover citrate/TCA-cycle chemotaxis signals."
        ),
        "ligand_summary": "citrate and citrate/metal complexes",
        "specific_function": (
            "McpQ is a citrate and citrate/metal-complex chemoreceptor that responds "
            "preferentially to citrate/Mg(2+) and related complexes."
        ),
        "pmid": "PMID:26463109",
        "pmid_title": (
            "McpQ is a specific citrate chemoreceptor that responds preferentially to "
            "citrate/metal ion complexes."
        ),
        "pmid_findings": [
            (
                "McpQ specifically recognizes citrate and citrate/metal complexes.",
                "McpS paralogue McpQ recognizes specifically citrate",
            ),
            (
                "Loss of mcpQ dramatically reduces chemotaxis toward citrate/Mg(2+).",
                "mcpQ inactivation caused a dramatic reduction",
            ),
        ],
        "uniprot_findings": [
            (
                "UniProt describes McpQ as a citrate/metal-complex chemoreceptor.",
                "McpQ recognizes specifically citrate and citrate/metal",
            ),
            (
                "UniProt records reduced citrate/Mg(2+) chemotaxis for mutants.",
                "in the chemotaxis toward citrate/Mg(2+) complexes",
            ),
        ],
        "core_support": [
            ref("PMID:26463109", "McpS paralogue McpQ recognizes specifically citrate"),
            ref("PMID:26463109", "mcpQ inactivation caused a dramatic reduction"),
        ],
        "has_receptor_mf_goa": False,
    },
}


def references_for(gene: str, cfg: dict) -> list[dict]:
    accession = cfg["accession"]
    refs = [GO_REF_INTERPRO, GO_REF_SUBCELL]
    refs.append(GO_REF_COMBINED if cfg["has_receptor_mf_goa"] else GO_REF_ARBA)
    refs.append(
        {
            "id": f"UniProt:{accession}",
            "title": f"UniProt entry {accession} for Pseudomonas putida KT2440 {gene}",
            "findings": [
                {"statement": statement, "supporting_text": text}
                for statement, text in cfg["uniprot_findings"]
            ],
        }
    )
    if cfg["pmid"]:
        refs.append(
            {
                "id": cfg["pmid"],
                "title": cfg["pmid_title"],
                "findings": [
                    {
                        "statement": statement,
                        "supporting_text": text,
                        "reference_section_type": "ABSTRACT",
                    }
                    for statement, text in cfg["pmid_findings"]
                ],
            }
        )
    refs.append(
        {
            "id": f"file:PSEPK/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": (
                        "Asta retrieval was checked for this first pass. For this "
                        "receptor panel, direct UniProt-linked receptor literature "
                        "or UniProt/domain evidence was more useful for curation "
                        "than the broad retrieval snippets."
                    )
                }
            ],
        }
    )
    return refs


def reviews_for(gene: str, cfg: dict) -> dict[str, dict]:
    accession = cfg["accession"]
    uniprot = f"UniProt:{accession}"
    ligand = cfg["ligand_summary"]
    mf_support = [
        ref(uniprot, "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt."),
    ]
    if cfg["pmid"]:
        mf_support.extend(cfg["core_support"][:1])
    else:
        mf_support.extend(cfg["core_support"])
    reviews = {
        "GO:0005886": review(
            "The receptor is a bacterial cell/inner-membrane methyl-accepting chemotaxis protein.",
            "ACCEPT",
            "Plasma membrane is the GO cellular-component term used for bacterial cell membrane, and the MCP architecture supports membrane localization.",
            [
                ref(uniprot, "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell."),
                ref(uniprot, "Multi-pass membrane protein")
                if gene == "ctpL"
                else ref(uniprot, "TRANSMEM"),
            ],
        ),
        "GO:0006935": review(
            f"The chemotaxis process annotation is appropriate for this {ligand} MCP receptor.",
            "ACCEPT",
            (
                f"{gene} is a methyl-accepting chemotaxis receptor in the named "
                f"KT2440 receptor panel. The ligand is {ligand}; for ctpL the ligand "
                "remains unresolved, but the MCP-family evidence supports a "
                "chemotaxis receptor role."
            ),
            cfg["core_support"] if cfg["pmid"] else mf_support,
        ),
        "GO:0007165": review(
            "Signal transduction is correct but less informative than chemotaxis and receptor activity.",
            "KEEP_AS_NON_CORE",
            "MCP receptors transduce ligand information across the membrane, but the specific biological role is chemotaxis.",
            [
                ref(uniprot, "transduce a signal from the outside to the inside of the cell")
                if gene != "ctpL"
                else ref(uniprot, "DR   GO; GO:0007165; P:signal transduction; IEA:UniProtKB-KW.")
            ],
        ),
        "GO:0016020": review(
            "Generic membrane is less informative than the retained plasma/cell-membrane term.",
            "MARK_AS_OVER_ANNOTATED",
            "The more specific GO:0005886 plasma membrane annotation captures the relevant bacterial cell-membrane localization.",
            [ref(uniprot, "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.")],
        ),
    }
    if cfg["has_receptor_mf_goa"]:
        reviews["GO:0004888"] = review(
            "Transmembrane signaling receptor activity is the appropriate broad molecular-function term for an MCP chemoreceptor.",
            "ACCEPT",
            (
                "GO lacks substrate-specific bacterial MCP receptor activity terms for "
                "these chemoeffectors, so GO:0004888 is the best available MF term."
            ),
            mf_support,
        )
    return reviews


def core_function_for(gene: str, cfg: dict) -> dict:
    support = cfg["core_support"] if cfg["pmid"] else cfg["core_support"]
    support.append(ref(f"UniProt:{cfg['accession']}", "DR   InterPro; IPR004089; MCPsignal_dom."))
    return {
        "description": cfg["specific_function"],
        "molecular_function": {
            "id": "GO:0004888",
            "label": "transmembrane signaling receptor activity",
        },
        "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
        "locations": [{"id": "GO:0005886", "label": "plasma membrane"}],
        "supported_by": support,
    }


def questions_for(gene: str, cfg: dict) -> list[dict[str, str]]:
    if gene == "ctpL":
        return [
            {
                "question": (
                    "What chemoeffector, if any, is sensed by KT2440 CtpL, and does it "
                    "signal through the main Che cluster or another chemosensory branch?"
                )
            }
        ]
    return [
        {
            "question": (
                f"How does {gene} specificity for {cfg['ligand_summary']} integrate with "
                "the other KT2440 MCP receptors during mixed root-exudate or nutrient gradients?"
            )
        }
    ]


def experiments_for(gene: str, cfg: dict) -> list[dict[str, str]]:
    if gene == "ctpL":
        return [
            {
                "description": (
                    "Express and purify the CtpL ligand-binding region, screen candidate "
                    "nutrients and root-exudate compounds by thermal shift or ITC, and "
                    "test matching ctpL deletion chemotaxis phenotypes."
                ),
                "experiment_type": "ligand-binding screen and chemotaxis assay",
            }
        ]
    return [
        {
            "description": (
                f"Compare wild type, {gene} deletion, and complemented strains in "
                f"quantitative chemotaxis assays toward {cfg['ligand_summary']} alone "
                "and in mixtures with other characterized MCP ligands."
            ),
            "experiment_type": "quantitative chemotaxis assay",
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    if cfg["aliases"]:
        data["aliases"] = cfg["aliases"]
    data["description"] = cfg["description"]
    reviews = reviews_for(gene, cfg)
    for annotation in data["existing_annotations"]:
        annotation["review"] = reviews[annotation["term"]["id"]]
    data["references"] = references_for(gene, cfg)
    data["core_functions"] = [core_function_for(gene, cfg)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = questions_for(gene, cfg)
    data["suggested_experiments"] = experiments_for(gene, cfg)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=88),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
