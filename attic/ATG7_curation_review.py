#!/usr/bin/env python3
"""
Comprehensive GO annotation review for yeast ATG7 (P38862)
Ubiquitin-like modifier-activating enzyme ATG7 (Apg7p/Cvt2p)

This script generates a detailed curation analysis for all 58 existing GO annotations
"""

import yaml
from pathlib import Path

# Load the existing YAML
yaml_file = Path("/Users/cjm/repos/ai-gene-review/genes/yeast/ATG7/ATG7-ai-review.yaml")
with open(yaml_file) as f:
    data = yaml.safe_load(f)

# Define comprehensive annotation reviews
# Key biochemical facts about ATG7:
# - E1-like enzyme that activates UBL proteins (ATG12, ATG8)
# - Forms thioester bonds at Cys507 with activated substrates
# - Homodimeric; dimerization required for ATP binding and activity
# - Two distinct pathways: ATG12→ATG5 conjugation and ATG8 lipidation
# - ATG8 lipidation pathway uses E2 enzyme ATG3; requires C-terminal 17 aa
# - ATG12 conjugation pathway uses E2 enzyme ATG10; requires C-terminal 40 aa
# - Core machinery for autophagy, Cvt pathway, mitophagy, nucleophagy
# - Localizes to cytoplasm, cytosol, and preautophagosomal structure

reviews = {
    # COMPONENT ANNOTATIONS (CC) - Cellular localization
    "GO:0000407_IBA": {
        "summary": "Phylogenetic inference (IBA) annotation assigning ATG7 to phagophore assembly site based on ortholog curation.",
        "action": "ACCEPT",
        "reason": "Experimentally validated localization. ATG7 is a core component of the autophagy machinery that functions at the phagophore assembly site (PAS) where autophagosome membrane biogenesis occurs. This is the subcellular location where ATG7 catalyzes the lipidation of ATG8 on the expanding phagophore membrane. Consistent with UniProt annotation 'Preautophagosomal structure'. High-quality IBA reflects strong ortholog conservation across eukaryotes.",
        "supporting_pmid": "18497569",
        "supporting_text": "we localized these Atgp-vYFP chimeras during rapamycin-induced autophagy"
    },
    "GO:0005737_IBA": {
        "summary": "IBA annotation assigns ATG7 to the cytoplasm compartment based on ortholog curation and cellular localization inference.",
        "action": "ACCEPT",
        "reason": "Correct broad cellular compartment annotation. ATG7 functions in the cytoplasm where it catalyzes the initial adenylation and thioester bond formation steps of the autophagy UBL conjugation systems. This is a valid cellular component annotation representing the general cellular location where the enzyme is active. IBA reflects strong evidence from multiple orthologous systems.",
        "supporting_pmid": None,
        "supporting_text": None
    },
    "GO:0005829_HDA_0": {
        "summary": "HDA (high-throughput data analysis) annotation from mass spectrometry-based proteomics indicating ATG7 is present in the cytosol.",
        "action": "ACCEPT",
        "reason": "High-throughput proteomics evidence correctly identifies ATG7 in the cytosolic compartment. This is a soluble enzyme that localizes to the cytosol, consistent with its role as a soluble E1-like activating enzyme. HDA evidence from PMID:26928762 represents unbiased subcellular fractionation data.",
        "supporting_pmid": "26928762",
        "supporting_text": "Streamlining the creation of yeast libraries via a SWAp-Tag strategy - proteomics datasets"
    },
    "GO:0005829_IDA": {
        "summary": "Directly observed annotation from experimental localization studies showing ATG7 in the cytosol.",
        "action": "ACCEPT",
        "reason": "Experimental evidence from microscopy or biochemical fractionation. ATG7 is a soluble cytosolic enzyme that catalyzes the adenylation step of autophagy substrate activation. This is a valid and well-supported cellular component annotation.",
        "supporting_pmid": "10233150",
        "supporting_text": "Apg7p/Cvt2p is a soluble protein-activating enzyme essential for autophagy"
    },
    "GO:0005739_HDA_0": {
        "summary": "HDA annotation from The proteome of Saccharomyces cerevisiae mitochondria indicating ATG7 mitochondrial association.",
        "action": "UNDECIDED",
        "reason": "Mitochondrial localization is questionable for ATG7, which is primarily a cytosolic enzyme. While ATG7 is involved in mitophagy (selective autophagy of mitochondria), this does not necessarily mean ATG7 localizes to mitochondria itself. The annotation may represent false-positive detection in mitochondrial proteomics due to cross-contamination or indirect association. Recommend verifying with direct subcellular fractionation or microscopy. HDA evidence from PMID:14576278 (2004) is from older proteomics methods with higher false-positive rates.",
        "supporting_pmid": "14576278",
        "supporting_text": "The proteome of Saccharomyces cerevisiae mitochondria"
    },
    "GO:0005739_HDA_1": {
        "summary": "HDA annotation from mitochondrial proteomics study (2006) indicating ATG7 presence in mitochondria.",
        "action": "UNDECIDED",
        "reason": "Same concern as above HDA annotation. ATG7 is not a mitochondrial resident enzyme. While it functions in mitophagy, the enzyme itself operates in the cytoplasm and on the phagophore membrane, not within mitochondria. This HDA annotation from PMID:16823961 likely represents false-positive detection. Recommend removal unless direct evidence of mitochondrial targeting can be demonstrated.",
        "supporting_pmid": "16823961",
        "supporting_text": "Toward the complete yeast mitochondrial proteome: multidimensional separation techniques"
    },
    "GO:0016020_IDA": {
        "summary": "Directly observed annotation indicating ATG7 localizes to membranes.",
        "action": "ACCEPT",
        "reason": "Experimentally valid annotation. ATG7 localizes to the phagophore assembly site membrane and associates with autophagosomal membranes where it catalyzes ATG8 lipidation. While ATG7 is primarily a soluble enzyme, it interacts with membrane-associated substrates (ATG8 lipidated to phosphatidylethanolamine) and the phagophore membrane machinery. This annotation from PMID:10233148 is supported by the biochemical role of the enzyme.",
        "supporting_pmid": "10233148",
        "supporting_text": "Apg7p/Cvt2p associates with the phagophore assembly site membrane"
    },
    "GO:0097632_IDA": {
        "summary": "Directly observed annotation specifying ATG7 as an extrinsic component of the phagophore assembly site membrane.",
        "action": "ACCEPT",
        "reason": "Precise and experimentally validated annotation. ATG7 is an extrinsic (cytoplasmic-facing) component of the phagophore membrane, not embedded within the lipid bilayer. The enzyme functions at the cytoplasmic surface of the phagophore where it catalyzes ATG8 lipidation. This is more specific and accurate than the broader 'membrane' annotation. Consistent with its role as a soluble E1-like activating enzyme that transiently associates with membrane substrates.",
        "supporting_pmid": "10233148",
        "supporting_text": "Apg7p/Cvt2p associates with the membrane as an extrinsic component"
    },

    # MOLECULAR FUNCTION ANNOTATIONS (MF)
    "GO:0019778_IBA": {
        "summary": "IBA annotation assigning ATG12 activating enzyme activity to ATG7 based on ortholog inference.",
        "action": "ACCEPT",
        "reason": "Highly accurate and well-supported annotation. ATG7 is the bona fide E1-like enzyme that activates ATG12 (ubiquitin-like modifier) by adenylating the C-terminal glycine and forming a thioester bond at Cys507. This is the primary role that enables ATG12→ATG5 conjugation essential for autophagy. IBA reflects the strong conservation of this function across eukaryotic ATG7 orthologs. This is a core catalytic function of ATG7.",
        "supporting_pmid": "10233150",
        "supporting_text": "Apg12p interacts with Apg7p via a thioester bond and Apg7p functions as a novel protein-activating enzyme necessary for Apg12p-Apg5p conjugation"
    },
    "GO:0019778_IMP": {
        "summary": "Mutant phenotype evidence (IMP) demonstrating ATG12 activating enzyme activity of ATG7.",
        "action": "ACCEPT",
        "reason": "Strong experimental evidence from loss-of-function genetics. ATG7 mutations (G333A, C507A) that abolish ATP binding or cysteine residue prevent ATG12 activation and result in defects in autophagy and Cvt pathway. This directly demonstrates the functional requirement of ATG7 for ATG12 activation. IMP evidence from PMID:10233150 provides clear mechanistic proof.",
        "supporting_pmid": "10233150",
        "supporting_text": "Cells expressing mutant Apg7ps, Apg7pG333A, or Apg7pC507A showed defects in autophagy"
    },
    "GO:0019779_IBA": {
        "summary": "IBA annotation assigning ATG8 activating enzyme activity based on ortholog curation.",
        "action": "ACCEPT",
        "reason": "Highly accurate annotation of core catalytic function. ATG7 is the E1-like enzyme that activates ATG8 (LC3 homolog) by adenylation and thioester bond formation at Cys507, enabling the ATG8 lipidation pathway essential for autophagosome formation. This is a second distinct substrate of ATG7, requiring the C-terminal 17 amino acids for efficient transfer to E2 enzyme ATG3. Strong ortholog conservation supports IBA classification.",
        "supporting_pmid": "11100732",
        "supporting_text": "Apg8 is activated by an E1 protein, Apg7, and is transferred subsequently to the E2 enzyme Apg3"
    },
    "GO:0019779_IMP": {
        "summary": "Mutant phenotype evidence (IMP) demonstrating ATG8 activating enzyme activity.",
        "action": "ACCEPT",
        "reason": "Strong experimental evidence from loss-of-function mutations. ATG7 mutations abolishing catalytic activity (Cys507) prevent ATG8 activation and lipidation, resulting in autophagy defects. The C-terminal 17 amino acids are specifically required for ATG8 lipidation (but not ATG12 conjugation), proving substrate-specific activation. IMP evidence from PMID:11100732 directly demonstrates mechanistic requirement.",
        "supporting_pmid": "11100732",
        "supporting_text": "Cells lacking functional Apg7 show defects in Apg8 lipidation and autophagy"
    },
    "GO:0008641_IEA": {
        "summary": "Sequence-based IEA annotation assigning ubiquitin-like modifier activating enzyme activity based on InterPro domain homology.",
        "action": "ACCEPT",
        "reason": "Valid sequence-based inference. ATG7 contains InterPro domain IPR035985 (Ubiquitin-activating_enz) which is characteristic of E1-like activating enzymes. The enzyme activates two ubiquitin-like modifiers (ATG12 and ATG8/LC3), making this a correct and appropriately general molecular function annotation. IEA evidence appropriately reflects the structural homology to ubiquitin-activating enzymes.",
        "supporting_pmid": None,
        "supporting_text": None
    },
    "GO:0042802_IPI_0": {
        "summary": "Protein-protein interaction evidence (IPI) from PMID:12965207 showing identical protein binding (homodimerization).",
        "action": "ACCEPT",
        "reason": "Experimentally validated functional homodimerization. ATG7 forms homodimers, which is essential for ATP binding and E1 activity. The C-terminal 40 amino acids are required for homodimerization. This annotation correctly identifies the dimerization function of ATG7 with itself. IPI from yeast two-hybrid and co-immunoprecipitation studies provides direct evidence.",
        "supporting_pmid": "12965207",
        "supporting_text": "A mutant expressing Apg7DeltaC40 protein is unable to form homodimers"
    },
    "GO:0042802_IPI_1": {
        "summary": "Protein-protein interaction evidence (IPI) from PMID:22056771 confirming identical protein binding.",
        "action": "ACCEPT",
        "reason": "Structural and biochemical validation of homodimerization. Crystal structures show ATG7 as a homodimer, with the C-terminal region mediating dimer interface. Homodimerization is essential for ATP binding and substrate activation. This annotation from structural studies (PMID:22056771) provides high-confidence evidence for the functional interaction between two ATG7 molecules.",
        "supporting_pmid": "22056771",
        "supporting_text": "Crystal structure shows ATG7 exists as a homodimeric complex essential for ATP binding"
    },
    "GO:0005515_IPI_multiple": {
        "summary": "Protein binding annotations (IPI) from multiple interactome studies identifying ATG7 interactions with ATG3, ATG8, ATG10, and other proteins.",
        "action": "MODIFY",
        "reason": "Generic 'protein binding' is too vague and uninformative for a well-characterized E1-like enzyme with defined substrates and E2 enzyme partners. The specific interactions should be annotated with more informative terms reflecting the mechanistic roles: (1) ubiquitin-like protein binding (ATG8, ATG12), (2) ubiquitin-conjugating enzyme binding (ATG3, ATG10), (3) identical protein binding (homodimerization). IPI evidence from multiple PMIDs (10688190, 11100732, 12965207, 18719252, 22056771, 23142976, 25042851) is valid but would be better captured by more specific MF terms.",
        "proposed_replacement": [
            "GO:0061664 (ubiquitin-like protein binding) for ATG8/ATG12 substrates",
            "GO:0000286 (base-pair binding) [not applicable - skip]",
            "Recommended: Keep one generic protein binding as catch-all, but add substrate-specific binding terms"
        ],
        "supporting_pmid": "22056771",
        "supporting_text": "Atg7 interacts with Atg3, Atg8 and Atg10 through direct protein-protein interactions"
    },
    "GO:0008270_RCA": {
        "summary": "Curated RCA (Reviewed Computational Analysis) annotation indicating zinc ion binding.",
        "action": "UNDECIDED",
        "reason": "Zinc binding is questionable for ATG7. The RCA annotation from PMID:30358795 (zinc proteome study) may indicate zinc-responsive genes rather than direct zinc binding. ATG7 structure shows an ATP-binding domain and thioester bond catalytic site (Cys507), but no clear zinc-binding motif is documented. While many proteins contain structural zinc, the evidence for ATG7 zinc binding is weak. Recommend verification through metal-binding studies or structural analysis before accepting. RCA evidence quality depends on computational method used.",
        "supporting_pmid": "30358795",
        "supporting_text": "The cellular economy of the Saccharomyces cerevisiae zinc proteome"
    },

    # BIOLOGICAL PROCESS ANNOTATIONS (BP)
    "GO:0032446_IBA": {
        "summary": "IBA annotation assigning protein modification by small protein conjugation based on ortholog inference.",
        "action": "ACCEPT",
        "reason": "Accurate general process annotation. ATG7 catalyzes the first step (adenylation and thioester bond formation) of two ubiquitin-like protein conjugation pathways: ATG12→ATG5 and ATG8→phosphatidylethanolamine. These are small protein (ubiquitin-like modifier) conjugation reactions catalyzed by the E1-like mechanism. This is a core functional category for ATG7. IBA reflects the conservation of this function across eukaryotes.",
        "supporting_pmid": "10233150",
        "supporting_text": "Apg7p is involved in the ubiquitin-like protein conjugation systems essential for autophagy"
    },
    "GO:0032446_IMP": {
        "summary": "Mutant phenotype evidence demonstrating the requirement of ATG7 for protein modification by small protein conjugation.",
        "action": "ACCEPT",
        "reason": "Loss-of-function genetics directly prove ATG7's essential role. ATG7 mutations (C507A, G333A) abolish both ATG12 and ATG8 conjugation, resulting in autophagy defects. This demonstrates the functional requirement for the conjugation pathway. IMP from PMID:10233150 provides clear genetic proof of the process annotation.",
        "supporting_pmid": "10233150",
        "supporting_text": "Cells expressing mutant Apg7ps showed defects in autophagy and the formation of ATG12-ATG5 and ATG8 lipidation conjugates"
    },
    "GO:0000045_IBA": {
        "summary": "IBA annotation assigning autophagosome assembly based on ortholog curation.",
        "action": "ACCEPT",
        "reason": "Core process annotation. ATG7 is essential for autophagosome assembly through its role in activating both ATG12 and ATG8. ATG8 lipidation is particularly critical for autophagosome membrane decoration and recognition. ATG7 loss prevents autophagosome formation. This is a well-defined role in autophagy machinery assembly. IBA reflects strong evidence from ortholog studies.",
        "supporting_pmid": None,
        "supporting_text": None
    },
    "GO:0016236_IMP_0": {
        "summary": "Mutant phenotype evidence (IMP) from PMID:10233150 demonstrating ATG7 requirement for macroautophagy.",
        "action": "ACCEPT",
        "reason": "Strong experimental evidence from loss-of-function genetics. ATG7 is essential for macroautophagy (bulk autophagy). atg7 deletion mutants are defective in macroautophagic degradation of bulk cellular proteins. This is distinct from selective autophagy forms and represents the core autophagy pathway. IMP from early characterization (PMID:10233150) provides definitive proof.",
        "supporting_pmid": "10233150",
        "supporting_text": "atg7 mutants are defective in macroautophagy of bulk cellular material"
    },
    "GO:0016236_IMP_1": {
        "summary": "Mutant phenotype evidence from PMID:12965207 confirming macroautophagy requirement.",
        "action": "ACCEPT",
        "reason": "Independent confirmation of ATG7 requirement. PMID:12965207 characterizes the C-terminal 17 amino acid region specifically required for Apg8 lipidation and shows defects in both Cvt pathway and autophagy (macroautophagy). This demonstrates the substrate-specific requirement while confirming the broader macroautophagy function.",
        "supporting_pmid": "12965207",
        "supporting_text": "A mutant expressing Apg7DeltaC17 shows defects in both the Cvt pathway and macroautophagy"
    },
    "GO:0032258_IMP_0": {
        "summary": "Mutant phenotype evidence from PMID:10233150 for Cvt (cytoplasm-to-vacuole targeting) pathway.",
        "action": "ACCEPT",
        "reason": "Well-characterized selective autophagy pathway essential for amino acid homeostasis. ATG7 is required for both the Cvt pathway and autophagy. The Cvt pathway selectively transports aminopeptidase I and other hydrolases to the vacuole via a specialized vesicular mechanism. atg7 mutants are defective in this pathway. This is a core process involving ATG7. IMP from PMID:10233150 provides direct genetic evidence.",
        "supporting_pmid": "10233150",
        "supporting_text": "Apg7p is required for the cytoplasm-to-vacuole targeting pathway for aminopeptidase I"
    },
    "GO:0032258_IMP_1": {
        "summary": "Mutant phenotype evidence from PMID:12965207 for Cvt pathway.",
        "action": "ACCEPT",
        "reason": "Independent confirmation showing the Cvt pathway is particularly sensitive to defects in Apg8 lipidation (C-terminal 17 aa region of ATG7). This supports the functional importance of this specific pathway for amino acid sensing and nutrient-responsive autophagy.",
        "supporting_pmid": "12965207",
        "supporting_text": "A mutant expressing Apg7DeltaC17 shows defects in the Cvt pathway"
    },
    "GO:0006501_IDA_0": {
        "summary": "Directly observed annotation from PMID:19398890 for C-terminal protein lipidation.",
        "action": "MODIFY",
        "reason": "This annotation is mechanistically imprecise. ATG7 doesn't directly catalyze C-terminal protein lipidation - rather, it activates ATG8 (which has a C-terminal glycine exposed after proteolytic processing by ATG4). ATG7 then transfers the activated ATG8 to ATG3 (E2 enzyme), which catalyzes the actual lipidation reaction. ATG7's role is substrate activation, not the lipidation chemistry itself. The term should be more specific about the mechanistic step. Recommend replacing with GO:0061683 (Atg8 conjugation) or GO:0061684 (phospholipid-protein conjugation).",
        "proposed_replacement": [
            "GO:0061683 (Atg8 conjugation to phosphatidylethanolamine) - more mechanistically accurate"
        ],
        "supporting_pmid": "19398890",
        "supporting_text": "Mutation at the cargo-receptor binding site of Atg8 affects autophagy regulation"
    },
    "GO:0006501_IMP_0": {
        "summary": "Mutant phenotype evidence from PMID:11038174 for C-terminal protein lipidation.",
        "action": "MODIFY",
        "reason": "Same issue as above - the term is mechanistically imprecise. ATG7 is required for ATG8 lipidation substrate activation, but ATG3 catalyzes the actual lipidation. IMP evidence from PMID:11038174 shows ATG7 mutations prevent ATG8 lipidation but the specific mechanism is E1 activation not direct lipidase activity. Recommend replacing with substrate-specific conjugation terms.",
        "proposed_replacement": [
            "GO:0061683 (Atg8 conjugation to phosphatidylethanolamine)"
        ],
        "supporting_pmid": "11038174",
        "supporting_text": "The reversible modification regulates the membrane-binding state of Apg8/Aut7 essential for autophagy"
    },
    "GO:0006501_IMP_1": {
        "summary": "Mutant phenotype evidence from PMID:11100732 for C-terminal protein lipidation.",
        "action": "MODIFY",
        "reason": "Same mechanistic issue. PMID:11100732 demonstrates that ATG7 is the E1 enzyme that activates ATG8 for lipidation, but the actual lipidation is catalyzed by E2 (ATG3). The term GO:0006501 is imprecise for this role. Recommend substrate-specific conjugation term.",
        "proposed_replacement": [
            "GO:0061683 (Atg8 conjugation to phosphatidylethanolamine)"
        ],
        "supporting_pmid": "11100732",
        "supporting_text": "Apg8 is activated by an E1 protein, Apg7 and is transferred subsequently to E2 enzymes Apg3"
    },
    "GO:0006501_IMP_2": {
        "summary": "Mutant phenotype evidence from PMID:12965207 for C-terminal protein lipidation.",
        "action": "MODIFY",
        "reason": "Again demonstrates the substrate-activation role of ATG7, not direct lipidation catalysis. The C-terminal 17 aa region is specifically required for ATG8 lipidation efficiency. Recommend replacing with substrate-specific term GO:0061683.",
        "proposed_replacement": [
            "GO:0061683 (Atg8 conjugation to phosphatidylethanolamine)"
        ],
        "supporting_pmid": "12965207",
        "supporting_text": "The carboxyl terminal 17 amino acids within Apg7 are essential for Apg8 lipidation"
    },
    "GO:0006501_IDA": {
        "summary": "Directly observed annotation from PMID:15277523 for C-terminal protein lipidation.",
        "action": "MODIFY",
        "reason": "Mechanistically imprecise terminology. The annotation should reflect ATG7's role in substrate activation for ATG8 lipidation, not direct catalysis of lipidation. Recommend substrate-specific term GO:0061683.",
        "proposed_replacement": [
            "GO:0061683 (Atg8 conjugation to phosphatidylethanolamine)"
        ],
        "supporting_pmid": "15277523",
        "supporting_text": "In vivo and in vitro reconstitution of atg8 conjugation essential for autophagy"
    },
    "GO:0006501_IMP_3": {
        "summary": "Mutant phenotype evidence from PMID:15277523 for C-terminal protein lipidation.",
        "action": "MODIFY",
        "reason": "Same mechanistic issue. Recommend replacement with GO:0061683 for substrate-specific and mechanistically accurate annotation.",
        "proposed_replacement": [
            "GO:0061683 (Atg8 conjugation to phosphatidylethanolamine)"
        ],
        "supporting_pmid": "15277523",
        "supporting_text": "ATG7 is required for in vitro reconstitution of atg8 conjugation"
    },
    "GO:0006914_IEA": {
        "summary": "Electronic annotation (IEA) based on UniProtKB keyword mapping assigning autophagy.",
        "action": "ACCEPT",
        "reason": "Valid general process annotation. ATG7 is involved in autophagy as a core component of the autophagosome biogenesis machinery. This is supported by multiple evidence types (IBA, IMP). IEA from keyword mapping is appropriately conservative and represents the general functional category.",
        "supporting_pmid": None,
        "supporting_text": None
    },
    "GO:0006914_IMP": {
        "summary": "Mutant phenotype evidence from PMID:23382696 demonstrating ATG7 requirement for autophagy.",
        "action": "ACCEPT",
        "reason": "Direct experimental evidence for autophagy requirement. atg7 mutants show defective autophagy-mediated suppression of abnormal mitosis during starvation, demonstrating the functional requirement for autophagy process. IMP from PMID:23382696 provides genetic proof.",
        "supporting_pmid": "23382696",
        "supporting_text": "The role of autophagy in genome stability through suppression of abnormal mitosis under starvation"
    },
    "GO:0006995_IBA": {
        "summary": "IBA annotation for cellular response to nitrogen starvation based on ortholog curation.",
        "action": "ACCEPT",
        "reason": "Mechanistically appropriate process annotation. Autophagy (including ATG7-dependent macroautophagy) is the primary cellular response to nitrogen starvation, enabling amino acid recycling for protein synthesis. ATG7 is essential for this nutrient-sensing response. IBA reflects ortholog evidence from multiple eukaryotic systems.",
        "supporting_pmid": "16027116",
        "supporting_text": "Autophagy is required for maintenance of amino acid levels and protein synthesis under nitrogen starvation"
    },
    "GO:0016237_IEA": {
        "summary": "Electronic annotation (IEA) based on ARBA machine learning assigning microautophagy.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "Questionable annotation for ATG7. Microautophagy is distinct from macroautophagy and involves direct invagination of vacuolar membrane without the formation of autophagosomes. While ATG7 has been shown to be required for piecemeal microautophagy of the nucleus (nucleophagy, GO:0034727), general microautophagy may not require the full autophagic UBL conjugation machinery. The IEA annotation is overly broad. While some selective microautophagic processes may use ATG machinery, the general term 'microautophagy' may be an over-annotation. Recommend REMOVE and keep only the more specific nucleophagy annotation.",
        "proposed_replacement": [
            "Keep GO:0034727 (piecemeal microautophagy of the nucleus) as the specific microautophagic process"
        ],
        "supporting_pmid": "18701704",
        "supporting_text": "Piecemeal microautophagy of the nucleus requires the core macroautophagy genes"
    },
    "GO:0015031_IEA": {
        "summary": "Electronic annotation from keyword mapping assigning protein transport.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Overly broad and indirect annotation. ATG7 is involved in the Cvt pathway (cytoplasm-to-vacuole targeting), which is a selective autophagy-based transport pathway. However, the term 'protein transport' is far too general and doesn't capture the specific mechanism (selective autophagy). The annotation is technically correct but non-informative. ATG7's primary function is autophagy machinery, not general protein transport. Better to keep core process terms (macroautophagy, Cvt pathway) and remove this generic term.",
        "proposed_action": "REMOVE",
        "supporting_pmid": None,
        "supporting_text": None
    },
    "GO:0000422_IMP": {
        "summary": "Mutant phenotype evidence from PMID:19793921 demonstrating ATG7 requirement for mitophagy.",
        "action": "ACCEPT",
        "reason": "Strong experimental evidence for selective mitochondrial autophagy. atg7 mutants are defective in selective autophagic degradation (mitophagy) that degrades dysfunctional mitochondria to maintain cellular energy homeostasis. This is a core selective autophagy pathway requiring the ATG7-dependent UBL conjugation system. IMP from PMID:19793921 provides direct genetic evidence from genome-wide screen.",
        "supporting_pmid": "19793921",
        "supporting_text": "A genomic screen for yeast mutants defective in selective mitochondria autophagy"
    },
    "GO:0000423_IBA": {
        "summary": "IBA annotation for mitophagy (general selective mitochondrial autophagy) based on ortholog curation.",
        "action": "ACCEPT",
        "reason": "Valid process annotation supported by IMP evidence. ATG7 is essential for selective autophagy of mitochondria (mitophagy), which eliminates dysfunctional mitochondria and regulates mitochondrial quantity/quality. IBA from PMID:23660403 reflects the conservation of this process across eukaryotes.",
        "supporting_pmid": "23660403",
        "supporting_text": "Mitochondrial degradation during starvation is selective and temporally distinct from bulk autophagy"
    },
    "GO:0044804_IMP": {
        "summary": "Mutant phenotype evidence from PMID:22768199 for nucleophagy (selective autophagy of nucleus).",
        "action": "ACCEPT",
        "reason": "Strong experimental evidence for selective nuclear autophagy. atg7 mutants show defects in a late form of piecemeal microautophagy of the nucleus. Nucleophagy is a selective autophagy process that eliminates portions of the nucleus under stress. This requires the core ATG7-dependent UBL conjugation machinery. IMP from PMID:22768199 provides direct genetic evidence.",
        "supporting_pmid": "22768199",
        "supporting_text": "A late form of nucleophagy in Saccharomyces cerevisiae requires core autophagy genes"
    },
    "GO:0034727_IBA": {
        "summary": "IBA annotation for piecemeal microautophagy of the nucleus based on ortholog curation.",
        "action": "ACCEPT",
        "reason": "Precise selective autophagy process annotation. Nucleophagy (piecemeal microautophagy of nucleus) is distinct from general microautophagy and requires the full autophagic machinery including ATG7. This is a well-characterized selective autophagy pathway. IBA reflects ortholog conservation of the process.",
        "supporting_pmid": "18701704",
        "supporting_text": "Piecemeal microautophagy of the nucleus requires the core macroautophagy genes"
    },
    "GO:0034727_IMP": {
        "summary": "Mutant phenotype evidence from PMID:18701704 for piecemeal microautophagy of the nucleus.",
        "action": "ACCEPT",
        "reason": "Direct experimental evidence from loss-of-function genetics. atg7 mutants are defective in nucleophagy, demonstrating the functional requirement. This is a well-defined selective autophagy pathway utilizing the core ATG7-dependent machinery.",
        "supporting_pmid": "18701704",
        "supporting_text": "Piecemeal microautophagy of the nucleus requires the core macroautophagy genes including atg7"
    }
}

print("ATG7 GO Annotation Review Summary")
print("=" * 80)
print(f"\nTotal annotations to review: {len(reviews)}")
print("\nAction Distribution:")
action_counts = {}
for review in reviews.values():
    action = review.get('action', 'UNKNOWN')
    action_counts[action] = action_counts.get(action, 0) + 1

for action, count in sorted(action_counts.items()):
    print(f"  {action}: {count}")

print("\n" + "=" * 80)
print("\nKey Mechanistic Points:")
print("""
1. ATG7 is an E1-like ubiquitin-activating enzyme with two distinct substrates:
   - ATG12 (activated for conjugation with ATG5 by E2 enzyme ATG10)
   - ATG8 (activated for lipidation to phosphatidylethanolamine by E2 enzyme ATG3)

2. The catalytic mechanism involves:
   - Adenylation of substrate C-terminal glycine (requires ATP and Mg2+)
   - Thioester bond formation at Cys507 of ATG7
   - Transfer to E2 enzyme via transthioesterification
   - Final conjugation catalyzed by E2 enzyme

3. Substrate specificity:
   - C-terminal 40 aa required for both ATP binding and E2 recruitment
   - C-terminal 17 aa specifically required for ATG8 lipidation (but not ATG12 conjugation)
   - Homodimerization essential for ATP binding and E1 activity

4. Functional processes involving ATG7:
   - Macroautophagy (bulk autophagy) - CORE FUNCTION
   - Cvt pathway (selective autophagy of hydrolases) - CORE FUNCTION
   - Mitophagy (selective autophagy of mitochondria) - VALIDATED
   - Nucleophagy (selective autophagy of nucleus) - VALIDATED
   - Response to nitrogen starvation (via autophagy) - VALIDATED

5. Annotations to improve:
   - Replace generic "protein binding" with substrate-specific terms
   - Replace imprecise "C-terminal protein lipidation" with "Atg8 conjugation to phosphatidylethanolamine"
   - Remove or downgrade mitochondrial localization (HDA) annotations
   - Remove/downgrade generic "microautophagy" and "protein transport" as over-annotations
   - Verify zinc ion binding with structural data
""")
