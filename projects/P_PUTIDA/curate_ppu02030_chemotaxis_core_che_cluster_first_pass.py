#!/usr/bin/env python3
"""First-pass curation for the ppu02030 core Che chemotaxis cluster."""

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


def apply_reviews(gene: str, description: str, references: list[dict], reviews: dict[str, dict], core_functions: list[dict], questions: list[str], experiments: list[str], aliases: list[str] | None = None) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    if aliases:
        data["aliases"] = aliases
    data["description"] = description
    for annotation in data["existing_annotations"]:
        term_id = annotation["term"]["id"]
        annotation["review"] = reviews[term_id]
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


def curate_pp_4332() -> None:
    uniprot = "UniProt:Q88EX0"
    references = [
        {
            "id": "GO_REF:0000002",
            "title": "Gene Ontology annotation through association of InterPro records with GO terms",
            "findings": [],
        },
        {"id": "GO_REF:0000118", "title": "TreeGrafter-generated GO annotations", "findings": []},
        {
            "id": "GO_REF:0000120",
            "title": "Combined Automated Annotation using Multiple IEA Methods",
            "findings": [],
        },
        {
            "id": uniprot,
            "title": "UniProt entry Q88EX0 for Pseudomonas putida KT2440 PP_4332",
            "findings": [
                {
                    "statement": "UniProt identifies PP_4332 as a CheW-domain chemotaxis protein in the KT2440 chemotaxis cluster.",
                    "supporting_text": "SubName: Full=Chemotaxis protein CheW",
                },
                {
                    "statement": "The sequence has conserved CheW-family domain evidence.",
                    "supporting_text": "DR   InterPro; IPR039315; CheW.",
                },
            ],
        },
        {
            "id": "file:PSEPK/PP_4332/PP_4332-deep-research-asta.md",
            "title": "Asta retrieval report for PP_4332 in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt/domain context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0005829": review(
            "Cytosol is plausible for a soluble CheW-domain adaptor, but the available evidence is a broad electronic localization rather than a specific polar chemosensory-array localization.",
            "KEEP_AS_NON_CORE",
            "The term is not misleading, but the core biological role of PP_4332 is participation in chemotaxis signaling rather than generic cytosolic residence.",
            [ref(uniprot, "DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter.")],
        ),
        "GO:0006935": review(
            "Chemotaxis is the appropriate process call for this CheW-domain protein.",
            "ACCEPT",
            "PP_4332 is annotated as a chemotaxis protein CheW and carries CheW-family domain signatures; CheW proteins act as adaptor/scaffold components in bacterial chemotaxis signaling complexes.",
            [
                ref(uniprot, "SubName: Full=Chemotaxis protein CheW"),
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:InterPro."),
                ref(uniprot, "DR   Pfam; PF01584; CheW; 1."),
            ],
        ),
        "GO:0007165": review(
            "Signal transduction is directionally correct but too broad for a CheW-family chemotaxis adaptor.",
            "MARK_AS_OVER_ANNOTATED",
            "The more informative annotation is chemotaxis. The broad parent signal-transduction term does not add useful specificity for this first-pass review.",
            [ref(uniprot, "DR   GO; GO:0007165; P:signal transduction; IEA:InterPro.")],
        ),
    }
    core_functions = [
        {
            "description": "PP_4332 is a CheW-family chemotaxis adaptor/scaffold candidate in the PP_4332-PP_4340 Che cluster. Its first-pass core role is participation in bacterial chemotaxis signaling, likely helping couple methyl-accepting chemotaxis receptors to the CheA/CheY phosphorelay.",
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "supported_by": [
                ref(uniprot, "SubName: Full=Chemotaxis protein CheW"),
                ref(uniprot, "DR   InterPro; IPR039315; CheW."),
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:InterPro."),
            ],
        }
    ]
    apply_reviews(
        "PP_4332",
        "PP_4332 encodes a predicted CheW-family chemotaxis protein in Pseudomonas putida KT2440. The protein is a small soluble CheW-like domain protein in the core PP_4332-PP_4340 chemosensory cluster. Its likely role is as an adaptor/scaffold component of the bacterial chemotaxis signaling array, linking receptor input to CheA-mediated phosphorelay signaling rather than acting as an enzyme.",
        references,
        reviews,
        core_functions,
        [
            "Does PP_4332 bind CheA and specific methyl-accepting chemotaxis receptors in the KT2440 core chemosensory array?",
            "Is PP_4332 functionally redundant with the adjacent CheW-domain protein PP_4333, or do the two adaptors support different receptor subsets?",
        ],
        [
            "Construct a PP_4332 deletion and assay swimming chemotaxis toward defined attractants and root-exudate mixtures.",
            "Test PP_4332 interaction with CheA and representative KT2440 MCPs using pull-down or bacterial two-hybrid assays.",
        ],
    )


def curate_pp_4333() -> None:
    uniprot = "UniProt:Q88EW9"
    references = [
        {
            "id": "GO_REF:0000002",
            "title": "Gene Ontology annotation through association of InterPro records with GO terms",
            "findings": [],
        },
        {
            "id": uniprot,
            "title": "UniProt entry Q88EW9 for Pseudomonas putida KT2440 PP_4333",
            "findings": [
                {
                    "statement": "UniProt identifies PP_4333 as a CheW-domain protein.",
                    "supporting_text": "SubName: Full=CheW domain protein",
                },
                {
                    "statement": "The C-terminal part of PP_4333 carries the conserved CheW-like domain.",
                    "supporting_text": 'FT                   /note="CheW-like"',
                },
            ],
        },
        {
            "id": "file:PSEPK/PP_4333/PP_4333-deep-research-asta.md",
            "title": "Asta retrieval report for PP_4333 in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt/domain context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0006935": review(
            "Chemotaxis is an appropriate first-pass process annotation for this CheW-domain protein in the core Che cluster.",
            "ACCEPT",
            "The protein has a CheW-like domain and is already mapped electronically to chemotaxis. The exact division of labor with PP_4332 remains unresolved, but the chemotaxis process annotation is biologically plausible.",
            [
                ref(uniprot, "SubName: Full=CheW domain protein"),
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:InterPro."),
                ref(uniprot, "DR   Pfam; PF01584; CheW; 1."),
            ],
        ),
        "GO:0007165": review(
            "Signal transduction is true at a high level but too broad for this CheW-domain chemotaxis protein.",
            "MARK_AS_OVER_ANNOTATED",
            "Chemotaxis is the more informative process annotation; the broad signal-transduction parent should not be treated as a core annotation.",
            [ref(uniprot, "DR   GO; GO:0007165; P:signal transduction; IEA:InterPro.")],
        ),
    }
    core_functions = [
        {
            "description": "PP_4333 is a CheW-like chemotaxis adaptor/accessory candidate in the PP_4332-PP_4340 Che cluster. The C-terminal CheW-like domain supports a role in bacterial chemotaxis signaling, but the specific receptor or CheA partner set is unresolved.",
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "supported_by": [
                ref(uniprot, "SubName: Full=CheW domain protein"),
                ref(uniprot, 'FT                   /note="CheW-like"'),
                ref(uniprot, "DR   GO; GO:0006935; P:chemotaxis; IEA:InterPro."),
            ],
        }
    ]
    apply_reviews(
        "PP_4333",
        "PP_4333 encodes a predicted CheW-domain protein in Pseudomonas putida KT2440. The protein has a C-terminal CheW-like domain and is part of the same core chemosensory cluster as PP_4332, CheB1, CheA, CheZ, and CheY. It is best treated in this first pass as a chemotaxis adaptor/accessory candidate, with its precise relationship to the shorter PP_4332 CheW protein left as a module-level knowledge gap.",
        references,
        reviews,
        core_functions,
        [
            "Does PP_4333 function as a second CheW adaptor in the core chemosensory cluster, or does its N-terminal extension confer a specialized regulatory role?",
            "Which MCPs, if any, preferentially require PP_4333 rather than PP_4332 for CheA coupling?",
        ],
        [
            "Compare PP_4332, PP_4333, and double mutants in swimming chemotaxis assays across representative organic-acid and amino-acid attractants.",
            "Map PP_4333 interaction partners within the KT2440 Che cluster by affinity purification or proximity labeling.",
        ],
    )


def curate_cheb1() -> None:
    uniprot = "UniProt:Q88EW5"
    references = [
        {
            "id": "GO_REF:0000002",
            "title": "Gene Ontology annotation through association of InterPro records with GO terms",
            "findings": [],
        },
        {
            "id": "GO_REF:0000104",
            "title": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
            "findings": [],
        },
        {
            "id": "GO_REF:0000120",
            "title": "Combined Automated Annotation using Multiple IEA Methods",
            "findings": [],
        },
        {
            "id": uniprot,
            "title": "UniProt entry Q88EW5 for Pseudomonas putida KT2440 CheB1",
            "findings": [
                {
                    "statement": "UniProt describes CheB1 as a chemotaxis response-regulator hydrolase that modifies methyl-accepting chemotaxis proteins.",
                    "supporting_text": "Involved in chemotaxis. Part of a chemotaxis signal transduction system that modulates chemotaxis in response to various stimuli.",
                },
                {
                    "statement": "The two annotated catalytic activities are protein-glutamate methylesterase and protein-glutamine glutaminase.",
                    "supporting_text": "Catalyzes the demethylation of specific methylglutamate residues introduced into the chemoreceptors",
                },
            ],
        },
        {
            "id": "file:PSEPK/cheB1/cheB1-deep-research-asta.md",
            "title": "Asta retrieval report for cheB1 in Pseudomonas putida KT2440",
            "findings": [
                {
                    "statement": "Asta retrieval was checked; it did not identify curation-changing organism-specific literature beyond the UniProt/domain context used in this first pass."
                }
            ],
        },
    ]
    reviews = {
        "GO:0000156": review(
            "CheB1 has the receiver-domain response-regulator architecture and is phosphorylated by CheA, so this response-regulator activity is appropriate.",
            "ACCEPT",
            "Although the methylesterase/glutaminase catalytic activities are the most specific molecular functions, CheB1 also acts as a CheA-phosphorylated response regulator whose phosphorylation activates methylesterase activity.",
            [
                ref(uniprot, "CC   -!- PTM: Phosphorylated by CheA."),
                ref(uniprot, "regulatory domain activates the methylesterase activity."),
                ref(uniprot, "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver."),
            ],
        ),
        "GO:0000160": review(
            "CheB1 participates in the CheA-dependent chemotaxis phosphorelay.",
            "ACCEPT",
            "The protein is a CheA-phosphorylated response regulator in the chemotaxis signal-transduction system.",
            [
                ref(uniprot, "Part of a chemotaxis signal transduction system that modulates chemotaxis in response to various stimuli."),
                ref(uniprot, "CC   -!- PTM: Phosphorylated by CheA."),
            ],
        ),
        "GO:0005737": review(
            "Cytoplasm is an appropriate localization for this soluble CheB-family response-regulator hydrolase.",
            "ACCEPT",
            "UniProt assigns CheB1 to the cytoplasm, consistent with a soluble chemotaxis-adaptation enzyme that acts on receptor methylation state from the cytoplasmic side of the signaling array.",
            [ref(uniprot, "CC   -!- SUBCELLULAR LOCATION: Cytoplasm")],
        ),
        "GO:0006935": review(
            "Chemotaxis is the core process context for CheB1.",
            "ACCEPT",
            "CheB1 modifies methyl-accepting chemotaxis proteins and is part of the Che signal-transduction system, making chemotaxis an appropriate core biological-process annotation.",
            [
                ref(uniprot, "Involved in chemotaxis."),
                ref(uniprot, "methyl-accepting chemotaxis proteins or MCP"),
            ],
        ),
        "GO:0007165": review(
            "Signal transduction is correct but too broad compared with the more informative chemotaxis and phosphorelay process annotations.",
            "MARK_AS_OVER_ANNOTATED",
            "The specific CheB1 context is chemotaxis adaptation in the Che phosphorelay; the high-level signal-transduction parent should not be treated as a core annotation.",
            [ref(uniprot, "Part of a chemotaxis signal transduction system that modulates chemotaxis in response to various stimuli.")],
        ),
        "GO:0008984": review(
            "Protein-glutamate methylesterase activity is a core CheB1 catalytic function.",
            "ACCEPT",
            "CheB1 demethylates methylglutamate residues in methyl-accepting chemotaxis proteins, reversing CheR-mediated receptor methylation during chemotaxis adaptation.",
            [
                ref(uniprot, "Catalyzes the demethylation of specific methylglutamate residues introduced into the chemoreceptors"),
                ref(uniprot, "EC=3.1.1.61"),
            ],
        ),
        "GO:0050568": review(
            "Protein-glutamine glutaminase activity is a core CheB1 catalytic function.",
            "ACCEPT",
            "CheB-family proteins also deamidate specific receptor glutamine residues to glutamate, establishing methyl-acceptor sites in the chemotaxis adaptation system.",
            [
                ref(uniprot, "Also mediates the irreversible deamidation of specific glutamine residues to glutamic acid."),
                ref(uniprot, "EC=3.5.1.44"),
            ],
        ),
    }
    core_functions = [
        {
            "description": "CheB1 is the CheA-regulated chemotaxis-adaptation methylesterase. It demethylates specific methylglutamate residues on methyl-accepting chemotaxis proteins, opposing CheR-mediated receptor methylation and tuning receptor sensitivity.",
            "molecular_function": {"id": "GO:0008984", "label": "protein-glutamate methylesterase activity"},
            "directly_involved_in": [
                {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
                {"id": "GO:0006935", "label": "chemotaxis"},
            ],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "supported_by": [
                ref(uniprot, "Catalyzes the demethylation of specific methylglutamate residues introduced into the chemoreceptors"),
                ref(uniprot, "CC   -!- PTM: Phosphorylated by CheA."),
            ],
        },
        {
            "description": "CheB1 also deamidates specific methyl-accepting chemotaxis protein glutamine residues to glutamate, creating receptor sites that can participate in methylation-dependent adaptation.",
            "molecular_function": {"id": "GO:0050568", "label": "protein-glutamine glutaminase activity"},
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
            "supported_by": [
                ref(uniprot, "Also mediates the irreversible deamidation of specific glutamine residues to glutamic acid."),
            ],
        },
    ]
    apply_reviews(
        "cheB1",
        "CheB1 is the chemotaxis receptor-adaptation enzyme of the PP_4332-PP_4340 Che cluster in Pseudomonas putida KT2440. It is a CheB-family response-regulator hydrolase with an N-terminal receiver domain and a C-terminal catalytic methylesterase domain. CheA-dependent phosphorylation activates its methylesterase activity, allowing CheB1 to demethylate methyl-accepting chemotaxis proteins and to deamidate selected receptor glutamine residues, thereby tuning receptor sensitivity during chemotaxis.",
        references,
        reviews,
        core_functions,
        [
            "Which KT2440 methyl-accepting chemotaxis proteins are the direct in vivo substrates of CheB1?",
            "How is adaptation divided between CheB1 and the other CheB-like paralogs in P. putida KT2440?",
        ],
        [
            "Measure methylesterase and glutaminase activity of purified CheB1 on representative KT2440 MCP cytoplasmic domains.",
            "Compare chemotaxis adaptation kinetics in cheB1 single mutants and combinations with other CheB/CheR paralogs.",
        ],
        aliases=["PP_4337"],
    )


def main() -> None:
    curate_pp_4332()
    curate_pp_4333()
    curate_cheb1()


if __name__ == "__main__":
    main()
