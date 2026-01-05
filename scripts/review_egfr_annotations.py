#!/usr/bin/env python3
"""
Script to systematically review EGFR GO annotations and assign curation actions.
Based on deep research and UniProt evidence for EGFR (P00533).
"""

import yaml
import sys
from pathlib import Path

# Define review decisions for each GO term category
# EGFR Core Functions:
# - Receptor tyrosine kinase (EC 2.7.10.1)
# - EGF binding
# - Plasma membrane localization
# - MAPK/ERK cascade regulation
# - Dimerization

CORE_FUNCTIONS = {
    # Molecular Function - CORE
    "GO:0004714": {  # transmembrane receptor protein tyrosine kinase activity
        "action": "ACCEPT",
        "summary": "EGFR is a receptor tyrosine kinase (EC 2.7.10.1) that phosphorylates tyrosine residues on substrate proteins following ligand-induced dimerization. This is a core molecular function.",
        "reason": "Transmembrane receptor protein tyrosine kinase activity is the defining enzymatic function of EGFR. The kinase domain catalyzes ATP-dependent phosphorylation of tyrosine residues."
    },
    "GO:0004713": {  # protein tyrosine kinase activity
        "action": "ACCEPT",
        "summary": "EGFR possesses protein tyrosine kinase activity, phosphorylating itself and downstream substrates upon activation.",
        "reason": "Protein tyrosine kinase activity is fundamental to EGFR signaling. This is the parent term of transmembrane receptor protein tyrosine kinase activity and accurately describes EGFR function."
    },
    "GO:0005006": {  # epidermal growth factor receptor activity
        "action": "ACCEPT",
        "summary": "EGFR is the prototypical EGF receptor, binding EGF and related ligands to initiate signaling cascades controlling proliferation, survival, and differentiation.",
        "reason": "This is the most specific molecular function term for EGFR and is definitionally correct."
    },
    "GO:0048408": {  # epidermal growth factor binding
        "action": "ACCEPT",
        "summary": "EGFR binds EGF through its extracellular domain (subdomains I and III), which induces receptor dimerization and activation.",
        "reason": "EGF binding is the canonical ligand-binding function of EGFR. Crystal structures confirm EGF binds domains I and III of the extracellular region."
    },
    "GO:0005524": {  # ATP binding
        "action": "ACCEPT",
        "summary": "EGFR binds ATP in its kinase domain active site to catalyze phosphorylation reactions.",
        "reason": "ATP binding is essential for EGFR kinase activity. The ATP-binding pocket in the kinase domain is the target of many therapeutic inhibitors."
    },
    "GO:0016301": {  # kinase activity
        "action": "ACCEPT",
        "summary": "EGFR has kinase activity, a parent term of protein tyrosine kinase activity.",
        "reason": "This is a general parent term that accurately describes EGFR function, though more specific terms are preferred."
    },
    "GO:0004672": {  # protein kinase activity
        "action": "ACCEPT",
        "summary": "EGFR has protein kinase activity, phosphorylating protein substrates on tyrosine residues.",
        "reason": "Accurate parent term for the protein tyrosine kinase activity of EGFR."
    },
    "GO:0016740": {  # transferase activity
        "action": "ACCEPT",
        "summary": "EGFR has transferase activity as it transfers phosphate groups from ATP to protein substrates.",
        "reason": "Very general parent term but accurate for EGFR kinase function."
    },
    "GO:0000166": {  # nucleotide binding
        "action": "ACCEPT",
        "summary": "EGFR binds nucleotides (ATP) for its kinase activity.",
        "reason": "General parent term for ATP binding, accurate for EGFR."
    },

    # Cellular Component - CORE locations
    "GO:0005886": {  # plasma membrane
        "action": "ACCEPT",
        "summary": "EGFR is a transmembrane receptor that localizes to the plasma membrane where it binds extracellular ligands and initiates intracellular signaling.",
        "reason": "Plasma membrane localization is essential for EGFR function as a cell surface receptor. EGFR resides at the plasma membrane to receive extracellular growth factor signals."
    },
    "GO:0016020": {  # membrane
        "action": "ACCEPT",
        "summary": "EGFR is an integral membrane protein spanning the plasma membrane with extracellular ligand-binding and intracellular kinase domains.",
        "reason": "EGFR is a type I transmembrane protein; membrane localization is fundamental to its structure and function."
    },
    "GO:0009986": {  # cell surface
        "action": "ACCEPT",
        "summary": "EGFR localizes to the cell surface where it is accessible for ligand binding.",
        "reason": "Cell surface localization is consistent with EGFR function as a receptor for extracellular growth factors."
    },
    "GO:0005768": {  # endosome
        "action": "ACCEPT",
        "summary": "EGFR localizes to endosomes following ligand-induced internalization. EGFR continues signaling from early endosomes and is subsequently sorted for recycling or lysosomal degradation.",
        "reason": "Endosomal localization is part of normal EGFR trafficking and signaling. EGFR signals from endosomes and trafficking modulates signal duration."
    },
    "GO:0010008": {  # endosome membrane
        "action": "ACCEPT",
        "summary": "EGFR localizes to endosome membranes during receptor trafficking after internalization.",
        "reason": "After ligand-induced endocytosis, EGFR is found on endosome membranes where it continues to signal."
    },
    "GO:0031901": {  # early endosome membrane
        "action": "ACCEPT",
        "summary": "EGFR localizes to early endosome membranes following internalization, where it continues to signal.",
        "reason": "Early endosome membrane localization is well-documented for EGFR trafficking."
    },
    "GO:0030139": {  # endocytic vesicle
        "action": "ACCEPT",
        "summary": "EGFR is internalized via endocytic vesicles following ligand binding.",
        "reason": "Endocytic vesicle localization is part of normal EGFR internalization."
    },
    "GO:0030669": {  # clathrin-coated endocytic vesicle membrane
        "action": "ACCEPT",
        "summary": "EGFR undergoes clathrin-mediated endocytosis and localizes to clathrin-coated vesicles.",
        "reason": "Clathrin-mediated endocytosis is a major route for EGFR internalization."
    },
    "GO:0043235": {  # receptor complex
        "action": "ACCEPT",
        "summary": "EGFR forms homo- and heterodimeric receptor complexes upon ligand binding, which is required for kinase activation.",
        "reason": "EGFR dimerization into receptor complexes is essential for signal transduction. EGFR forms homodimers and heterodimers with ERBB2, ERBB3, ERBB4."
    },
    "GO:0016323": {  # basolateral plasma membrane
        "action": "ACCEPT",
        "summary": "In polarized epithelial cells, EGFR localizes to the basolateral plasma membrane.",
        "reason": "EGFR shows polarized distribution in epithelial cells, localizing to basolateral membranes."
    },
    "GO:0009925": {  # basal plasma membrane
        "action": "ACCEPT",
        "summary": "EGFR localizes to the basal plasma membrane in polarized cells.",
        "reason": "Basal plasma membrane localization is consistent with EGFR function in polarized cells."
    },

    # Biological Process - CORE signaling
    "GO:0007173": {  # epidermal growth factor receptor signaling pathway
        "action": "ACCEPT",
        "summary": "EGFR is the initiating receptor of the EGF receptor signaling pathway, binding EGF family ligands and activating downstream signaling cascades.",
        "reason": "This is the defining biological process for EGFR - it is the primary receptor that initiates this pathway."
    },
    "GO:0043410": {  # positive regulation of MAPK cascade
        "action": "ACCEPT",
        "summary": "EGFR positively regulates the MAPK cascade through recruitment of GRB2-SOS and activation of RAS-RAF-MEK-ERK signaling.",
        "reason": "MAPK/ERK pathway activation is a core downstream signaling output of EGFR. This is well-established."
    },
    "GO:0000165": {  # MAPK cascade
        "action": "ACCEPT",
        "summary": "EGFR participates in the MAPK cascade by activating RAS-RAF-MEK-ERK signaling upon ligand binding.",
        "reason": "MAPK cascade activation is a principal downstream effect of EGFR signaling."
    },
    "GO:0070374": {  # positive regulation of ERK1 and ERK2 cascade
        "action": "ACCEPT",
        "summary": "EGFR positively regulates ERK1/2 cascade through RAS-RAF-MEK-ERK signaling axis.",
        "reason": "ERK1/2 activation is a core readout of EGFR signaling through the MAPK pathway."
    },
    "GO:0007169": {  # cell surface receptor protein tyrosine kinase signaling pathway
        "action": "ACCEPT",
        "summary": "EGFR is a cell surface receptor protein tyrosine kinase that initiates signaling upon ligand binding.",
        "reason": "This is the parent pathway term that accurately describes EGFR function."
    },
    "GO:0007165": {  # signal transduction
        "action": "ACCEPT",
        "summary": "EGFR mediates signal transduction from extracellular growth factors to intracellular signaling cascades.",
        "reason": "Signal transduction is a core function of EGFR as a receptor tyrosine kinase."
    },
    "GO:0038134": {  # ERBB2-EGFR signaling pathway
        "action": "ACCEPT",
        "summary": "EGFR heterodimerizes with ERBB2 to form signaling complexes with distinct downstream effects.",
        "reason": "EGFR-ERBB2 heterodimers are an important signaling unit with enhanced signaling capacity."
    },
    "GO:0042059": {  # negative regulation of epidermal growth factor receptor signaling pathway
        "action": "ACCEPT",
        "summary": "EGFR participates in negative regulation of its own signaling through internalization and degradation mechanisms.",
        "reason": "EGFR signaling is subject to negative feedback through receptor internalization, ubiquitination by CBL, and lysosomal degradation."
    },
    "GO:0045742": {  # positive regulation of epidermal growth factor receptor signaling pathway
        "action": "ACCEPT",
        "summary": "EGFR itself positively regulates the EGF receptor signaling pathway as the initiating receptor.",
        "reason": "EGFR activation initiates and sustains EGF receptor signaling."
    },
}

# Non-core but valid functions (downstream effects, pleiotropic)
NON_CORE_FUNCTIONS = {
    "GO:0030182": {  # neuron differentiation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling influences neuron differentiation, a downstream developmental effect.",
        "reason": "Neuron differentiation is a downstream developmental process influenced by EGFR signaling, not a core molecular function."
    },
    "GO:0043066": {  # negative regulation of apoptotic process
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes cell survival by activating anti-apoptotic pathways including PI3K-AKT.",
        "reason": "Anti-apoptotic effects are downstream consequences of EGFR-PI3K-AKT signaling, not a core function."
    },
    "GO:0050679": {  # positive regulation of epithelial cell proliferation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes epithelial cell proliferation, a key downstream effect in epithelial tissues.",
        "reason": "Epithelial cell proliferation is a major physiological outcome of EGFR signaling but represents a downstream effect."
    },
    "GO:0008284": {  # positive regulation of cell population proliferation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes cell proliferation through MAPK and PI3K pathways.",
        "reason": "Cell proliferation is a downstream phenotypic effect of EGFR signaling."
    },
    "GO:0008283": {  # cell population proliferation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling influences cell proliferation.",
        "reason": "Cell proliferation is a downstream effect of EGFR activation."
    },
    "GO:0042127": {  # regulation of cell population proliferation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR regulates cell proliferation through downstream signaling.",
        "reason": "General cell proliferation regulation is a downstream effect."
    },
    "GO:0030335": {  # positive regulation of cell migration
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes cell migration through various downstream effectors.",
        "reason": "Cell migration is a downstream cellular behavior influenced by EGFR signaling."
    },
    "GO:0030307": {  # positive regulation of cell growth
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes cell growth.",
        "reason": "Cell growth regulation is a downstream effect of EGFR activation."
    },
    "GO:0043491": {  # phosphatidylinositol 3-kinase/protein kinase B signal transduction (PI3K/AKT)
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR activates PI3K-AKT signaling through recruitment of PI3K to phosphotyrosine docking sites.",
        "reason": "PI3K-AKT pathway activation is a major downstream signaling axis of EGFR, but is not the core function."
    },
    "GO:0051897": {  # positive regulation of PI3K/protein kinase B signal transduction
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR positively regulates PI3K-AKT signaling.",
        "reason": "PI3K-AKT regulation is downstream of EGFR activation."
    },
    "GO:0090037": {  # positive regulation of protein kinase C signaling
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR activates PKC signaling through PLC-gamma activation.",
        "reason": "PKC signaling regulation is downstream of EGFR-PLC-gamma activation."
    },
    "GO:1900087": {  # positive regulation of G1/S transition of mitotic cell cycle
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes G1/S cell cycle transition.",
        "reason": "Cell cycle regulation is a downstream effect of EGFR proliferative signaling."
    },
    "GO:0001934": {  # positive regulation of protein phosphorylation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR promotes protein phosphorylation through its kinase activity and downstream signaling.",
        "reason": "This is a general downstream effect of EGFR signaling."
    },
    "GO:0033138": {  # positive regulation of peptidyl-serine phosphorylation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling leads to downstream serine phosphorylation events.",
        "reason": "Serine phosphorylation regulation is a downstream effect of EGFR signaling cascades."
    },
    "GO:0042327": {  # positive regulation of phosphorylation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR promotes phosphorylation through its kinase activity.",
        "reason": "General phosphorylation regulation is downstream of EGFR kinase activity."
    },
    "GO:0050730": {  # regulation of peptidyl-tyrosine phosphorylation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR regulates tyrosine phosphorylation of substrates.",
        "reason": "While related to EGFR kinase activity, this describes regulatory outcomes."
    },
    "GO:0045944": {  # positive regulation of transcription by RNA polymerase II
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling leads to transcriptional activation of target genes.",
        "reason": "Transcriptional regulation is a downstream effect of EGFR signaling pathways."
    },
    "GO:1902895": {  # positive regulation of miRNA transcription
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling regulates miRNA transcription.",
        "reason": "miRNA regulation is a downstream transcriptional effect."
    },
    "GO:0090263": {  # positive regulation of canonical Wnt signaling pathway
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling can crosstalk with and regulate Wnt signaling.",
        "reason": "Wnt pathway crosstalk is a secondary/downstream effect of EGFR."
    },
    "GO:0000902": {  # cell morphogenesis
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling influences cell morphogenesis.",
        "reason": "Cell morphogenesis is a downstream developmental effect."
    },
    "GO:0071364": {  # cellular response to epidermal growth factor stimulus
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR mediates cellular responses to EGF.",
        "reason": "This describes the cellular response, not the core receptor function."
    },
    "GO:0071363": {  # cellular response to growth factor stimulus
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR mediates cellular responses to growth factors.",
        "reason": "General growth factor response is downstream of receptor activation."
    },
    "GO:0071392": {  # cellular response to estradiol stimulus
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR can be activated in response to estradiol through crosstalk mechanisms.",
        "reason": "Estradiol response represents crosstalk/secondary activation, not core function."
    },
    "GO:0071230": {  # cellular response to amino acid stimulus
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling responds to amino acid availability.",
        "reason": "Amino acid response is a contextual regulatory effect."
    },
    "GO:0010467": {  # gene expression
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling regulates gene expression.",
        "reason": "Gene expression regulation is a downstream effect of EGFR signaling."
    },
    "GO:0007166": {  # cell surface receptor signaling pathway
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR participates in cell surface receptor signaling.",
        "reason": "This general term is accurate but less specific than EGFR signaling pathway terms."
    },
}

# Developmental/tissue-specific processes - non-core
DEVELOPMENTAL_PROCESSES = {
    "GO:0001892": {  # embryonic placenta development
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling contributes to embryonic placenta development.",
        "reason": "Developmental process downstream of EGFR signaling in specific tissues."
    },
    "GO:0001942": {  # hair follicle development
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling is required for hair follicle development.",
        "reason": "Tissue-specific developmental process regulated by EGFR."
    },
    "GO:0008544": {  # epidermis development
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling is critical for epidermis development.",
        "reason": "Developmental process in EGFR's namesake tissue, but represents downstream effects."
    },
    "GO:0007435": {  # salivary gland morphogenesis
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling contributes to salivary gland development.",
        "reason": "Tissue-specific developmental process."
    },
    "GO:0048546": {  # digestive tract morphogenesis
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling influences digestive tract development.",
        "reason": "Developmental process downstream of EGFR signaling."
    },
    "GO:0060571": {  # morphogenesis of an epithelial fold
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling contributes to epithelial fold morphogenesis.",
        "reason": "Developmental morphogenesis process."
    },
    "GO:0061029": {  # eyelid development in camera-type eye
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling is involved in eyelid development.",
        "reason": "Tissue-specific developmental process."
    },
    "GO:0021795": {  # cerebral cortex cell migration
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling influences cortical cell migration during development.",
        "reason": "Developmental process in the nervous system."
    },
    "GO:0050673": {  # epithelial cell proliferation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR promotes epithelial cell proliferation.",
        "reason": "Cell type-specific proliferation effect."
    },
    "GO:0048146": {  # positive regulation of fibroblast proliferation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes fibroblast proliferation.",
        "reason": "Cell type-specific downstream effect."
    },
    "GO:1905208": {  # negative regulation of cardiocyte differentiation
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling negatively regulates cardiocyte differentiation.",
        "reason": "Cell type-specific developmental effect."
    },
    "GO:0007611": {  # learning or memory
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling may influence learning and memory processes.",
        "reason": "High-level behavioral phenotype, represents very downstream effects."
    },
    "GO:0001503": {  # ossification
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling may influence bone formation.",
        "reason": "Developmental process in bone tissue."
    },
    "GO:0098609": {  # cell-cell adhesion
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling influences cell-cell adhesion.",
        "reason": "Downstream cellular behavior."
    },
}

# Terms to REMOVE (uninformative)
REMOVE_TERMS = {
    "GO:0005515": {  # protein binding
        "action": "REMOVE",
        "summary": "Generic 'protein binding' term provides no specific information about EGFR molecular function.",
        "reason": "Per GO curation guidelines, 'protein binding' is uninformative and should be replaced with more specific binding terms. EGFR interacts with many proteins including ligands (EGF), dimerization partners (ERBB2-4), adaptors (GRB2, SHC), and signaling molecules, but this generic term does not capture any specific binding activity."
    },
}

# Terms to keep but mark as potentially over-annotated
OVER_ANNOTATED = {
    "GO:0004709": {  # MAP kinase kinase kinase activity
        "action": "MARK_AS_OVER_ANNOTATED",
        "summary": "EGFR is not a direct MAP3K. EGFR activates the MAPK cascade but acts upstream of RAF (the actual MAP3K).",
        "reason": "EGFR is a receptor tyrosine kinase that activates RAS, which then activates RAF (the MAP3K). EGFR itself does not have MAP3K activity."
    },
    "GO:0003690": {  # double-stranded DNA binding
        "action": "MARK_AS_OVER_ANNOTATED",
        "summary": "Nuclear EGFR has been reported to associate with chromatin, but direct DNA binding is controversial.",
        "reason": "While nuclear EGFR has been described, its direct DNA binding role is not well-established and may be indirect through transcription factor interactions."
    },
    "GO:0003682": {  # chromatin binding
        "action": "KEEP_AS_NON_CORE",
        "summary": "Nuclear EGFR has been reported to bind chromatin and regulate transcription.",
        "reason": "Nuclear EGFR has been described in some contexts, but this is not a core function of EGFR."
    },
}

# Additional localization terms
ADDITIONAL_LOCALIZATIONS = {
    "GO:0005634": {  # nucleus
        "action": "KEEP_AS_NON_CORE",
        "summary": "Nuclear EGFR has been described in certain contexts and may have transcriptional roles.",
        "reason": "Nuclear EGFR is documented but represents a minor, context-dependent localization rather than core EGFR function."
    },
    "GO:0005829": {  # cytosol
        "action": "ACCEPT",
        "summary": "EGFR cytoplasmic domain resides in the cytosol and signals to cytosolic proteins.",
        "reason": "The intracellular kinase domain of EGFR is in the cytosol."
    },
    "GO:0005737": {  # cytoplasm
        "action": "ACCEPT",
        "summary": "EGFR intracellular domain localizes to the cytoplasm.",
        "reason": "The cytoplasmic portion of EGFR containing the kinase domain is localized in the cytoplasm."
    },
    "GO:0005794": {  # Golgi apparatus
        "action": "ACCEPT",
        "summary": "EGFR transits through the Golgi during biosynthesis and trafficking.",
        "reason": "EGFR is processed through the secretory pathway including the Golgi."
    },
    "GO:0000139": {  # Golgi membrane
        "action": "ACCEPT",
        "summary": "EGFR localizes to Golgi membranes during biosynthesis.",
        "reason": "Part of normal EGFR trafficking through the secretory pathway."
    },
    "GO:0005789": {  # endoplasmic reticulum membrane
        "action": "ACCEPT",
        "summary": "EGFR is synthesized and processed in the ER membrane.",
        "reason": "Part of normal EGFR biosynthesis in the secretory pathway."
    },
    "GO:0005576": {  # extracellular region
        "action": "ACCEPT",
        "summary": "The EGFR extracellular domain is exposed to the extracellular region.",
        "reason": "The ligand-binding ectodomain of EGFR is in the extracellular region."
    },
    "GO:0031965": {  # nuclear membrane
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been reported at the nuclear membrane in certain contexts.",
        "reason": "Nuclear membrane localization is not a primary EGFR localization."
    },
    "GO:0048471": {  # perinuclear region of cytoplasm
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR may localize to perinuclear regions during trafficking.",
        "reason": "Perinuclear localization may occur during endocytic trafficking."
    },
    "GO:0045121": {  # membrane raft
        "action": "ACCEPT",
        "summary": "EGFR localizes to membrane rafts/lipid rafts in the plasma membrane.",
        "reason": "EGFR partitioning into membrane rafts affects its signaling."
    },
    "GO:0032587": {  # ruffle membrane
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR localizes to membrane ruffles during cell migration.",
        "reason": "Ruffle localization is associated with EGFR-induced cell migration."
    },
    "GO:0097708": {  # intracellular vesicle
        "action": "ACCEPT",
        "summary": "EGFR is found in intracellular vesicles during trafficking.",
        "reason": "Part of EGFR endocytic trafficking."
    },
    "GO:0097489": {  # multivesicular body, internal vesicle lumen
        "action": "ACCEPT",
        "summary": "EGFR is sorted into multivesicular bodies for lysosomal degradation.",
        "reason": "MVB sorting is part of EGFR downregulation pathway."
    },
    "GO:0030054": {  # cell junction
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR may localize to cell junctions.",
        "reason": "Cell junction localization is context-dependent."
    },
    "GO:0005925": {  # focal adhesion
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR localizes to focal adhesions during cell migration.",
        "reason": "Focal adhesion localization is associated with EGFR-mediated migration."
    },
    "GO:0032991": {  # protein-containing complex
        "action": "ACCEPT",
        "summary": "EGFR forms protein complexes with signaling partners.",
        "reason": "EGFR exists in multiprotein signaling complexes."
    },
    "GO:0005615": {  # extracellular space
        "action": "KEEP_AS_NON_CORE",
        "summary": "Soluble EGFR ectodomain isoforms may be released to extracellular space.",
        "reason": "Truncated soluble EGFR isoforms exist but this is not the primary EGFR form."
    },
    "GO:0036064": {  # ciliary basal body
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been detected at ciliary basal bodies.",
        "reason": "Ciliary localization is context-specific."
    },
    "GO:0005929": {  # cilium
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been detected in cilia.",
        "reason": "Ciliary localization is context-specific."
    },
    "GO:0097225": {  # sperm midpiece
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been detected in sperm midpiece.",
        "reason": "Sperm-specific localization."
    },
    "GO:0097228": {  # sperm principal piece
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been detected in sperm principal piece.",
        "reason": "Sperm-specific localization."
    },
    "GO:0097229": {  # sperm end piece
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been detected in sperm end piece.",
        "reason": "Sperm-specific localization."
    },
}

# Binding activities
BINDING_ACTIVITIES = {
    "GO:0042802": {  # identical protein binding
        "action": "ACCEPT",
        "summary": "EGFR undergoes homodimerization, binding to itself as part of the activation mechanism.",
        "reason": "EGFR homodimerization is essential for kinase activation. Ligand binding promotes EGFR-EGFR homodimer formation."
    },
    "GO:0019899": {  # enzyme binding
        "action": "ACCEPT",
        "summary": "EGFR binds to downstream enzymes including kinases and phosphatases.",
        "reason": "EGFR interacts with various enzymes as part of signaling."
    },
    "GO:0019900": {  # kinase binding
        "action": "ACCEPT",
        "summary": "EGFR binds to kinases including SRC family kinases and downstream signaling kinases.",
        "reason": "EGFR interacts with multiple kinases in signaling complexes."
    },
    "GO:0019903": {  # protein phosphatase binding
        "action": "ACCEPT",
        "summary": "EGFR binds to protein phosphatases that regulate its phosphorylation state.",
        "reason": "EGFR is regulated by phosphatases including PTPN1, PTPN2, and PTPN12."
    },
    "GO:0031625": {  # ubiquitin protein ligase binding
        "action": "ACCEPT",
        "summary": "EGFR binds to CBL E3 ubiquitin ligase, which ubiquitinates EGFR for endocytosis and degradation.",
        "reason": "CBL binding to EGFR is critical for receptor downregulation."
    },
    "GO:0045296": {  # cadherin binding
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR binds to cadherins, linking to cell adhesion regulation.",
        "reason": "Cadherin binding represents crosstalk between EGFR and cell adhesion."
    },
    "GO:0051117": {  # ATPase binding
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR may bind to ATPases.",
        "reason": "ATPase binding is not a primary EGFR function."
    },
    "GO:0051015": {  # actin filament binding
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR has been reported to bind actin filaments.",
        "reason": "Actin binding may be involved in EGFR trafficking/localization."
    },
    "GO:0004888": {  # transmembrane signaling receptor activity
        "action": "ACCEPT",
        "summary": "EGFR is a transmembrane signaling receptor.",
        "reason": "This accurately describes EGFR as a transmembrane receptor."
    },
    "GO:0030296": {  # protein tyrosine kinase activator activity
        "action": "ACCEPT",
        "summary": "EGFR can activate other tyrosine kinases through heterodimerization (especially ERBB2).",
        "reason": "EGFR activates ERBB2 kinase activity through heterodimer formation."
    },
    "GO:0070435": {  # Shc-EGFR complex
        "action": "ACCEPT",
        "summary": "EGFR forms a complex with SHC adaptor protein.",
        "reason": "SHC binding to phosphorylated EGFR is a key signaling event."
    },
}

# Miscellaneous processes
MISC_PROCESSES = {
    "GO:0046718": {  # symbiont entry into host cell (viral entry)
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR can serve as a receptor for viral entry, including some herpesviruses.",
        "reason": "Viral receptor function is not a normal physiological function of EGFR."
    },
    "GO:0001618": {  # virus receptor activity
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR can act as a receptor for certain viruses.",
        "reason": "Virus receptor activity is not a core physiological function."
    },
    "GO:0006511": {  # ubiquitin-dependent protein catabolic process
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR undergoes ubiquitin-dependent degradation.",
        "reason": "EGFR is ubiquitinated and degraded, but this describes its regulation rather than function."
    },
    "GO:0016567": {  # protein ubiquitination
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR is ubiquitinated by CBL for endocytosis and degradation.",
        "reason": "Describes EGFR regulation, not its enzymatic function."
    },
    "GO:0070086": {  # ubiquitin-dependent endocytosis
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR undergoes ubiquitin-dependent endocytosis.",
        "reason": "Describes EGFR trafficking/regulation."
    },
    "GO:0042908": {  # xenobiotic transport
        "action": "MARK_AS_OVER_ANNOTATED",
        "summary": "EGFR involvement in xenobiotic transport is not well-established.",
        "reason": "This annotation is likely over-interpretation; EGFR is not a transporter."
    },
    "GO:0051205": {  # protein insertion into membrane
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR is inserted into the membrane during biosynthesis.",
        "reason": "Describes EGFR biogenesis rather than function."
    },
    "GO:0070141": {  # response to UV-A
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR can be activated by UV-A exposure.",
        "reason": "UV-A activation is a stress response, not normal physiological activation."
    },
    "GO:0045739": {  # positive regulation of DNA repair
        "action": "KEEP_AS_NON_CORE",
        "summary": "Nuclear EGFR has been implicated in DNA repair regulation.",
        "reason": "DNA repair regulation is a non-canonical nuclear EGFR function."
    },
    "GO:0045740": {  # positive regulation of DNA replication
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling promotes DNA replication through proliferative signaling.",
        "reason": "DNA replication regulation is downstream of EGFR proliferative signaling."
    },
    "GO:0042177": {  # negative regulation of protein catabolic process
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling can inhibit protein catabolism.",
        "reason": "Downstream effect of EGFR survival signaling."
    },
    "GO:1903078": {  # positive regulation of protein localization to plasma membrane
        "action": "KEEP_AS_NON_CORE",
        "summary": "EGFR signaling can regulate protein localization to plasma membrane.",
        "reason": "Downstream cellular effect."
    },
}


def load_yaml(filepath):
    """Load YAML file."""
    with open(filepath) as f:
        return yaml.safe_load(f)


def save_yaml(data, filepath):
    """Save YAML file."""
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=100, sort_keys=False)


def get_review_for_term(go_id):
    """Get the review decision for a GO term."""
    all_reviews = {
        **CORE_FUNCTIONS,
        **NON_CORE_FUNCTIONS,
        **DEVELOPMENTAL_PROCESSES,
        **REMOVE_TERMS,
        **OVER_ANNOTATED,
        **ADDITIONAL_LOCALIZATIONS,
        **BINDING_ACTIVITIES,
        **MISC_PROCESSES,
    }
    return all_reviews.get(go_id)


def main():
    yaml_path = Path("genes/human/EGFR/EGFR-ai-review.yaml")

    # Load the YAML
    data = load_yaml(yaml_path)

    # Track statistics
    stats = {
        "total": 0,
        "reviewed": 0,
        "already_reviewed": 0,
        "no_match": 0,
        "by_action": {}
    }

    # Review each annotation
    for annotation in data.get("existing_annotations", []):
        stats["total"] += 1

        go_id = annotation.get("term", {}).get("id")
        current_action = annotation.get("review", {}).get("action")

        # Skip if already reviewed
        if current_action and current_action != "PENDING":
            stats["already_reviewed"] += 1
            continue

        # Get review decision
        review = get_review_for_term(go_id)

        if review:
            annotation["review"] = {
                "summary": review["summary"],
                "action": review["action"],
                "reason": review["reason"]
            }
            stats["reviewed"] += 1
            action = review["action"]
            stats["by_action"][action] = stats["by_action"].get(action, 0) + 1
        else:
            stats["no_match"] += 1
            print(f"No review found for: {go_id} ({annotation.get('term', {}).get('label')})")

    # Update description
    data["description"] = (
        "Epidermal growth factor receptor (EGFR/ERBB1/HER1) is a receptor tyrosine kinase "
        "(EC 2.7.10.1) that binds EGF family ligands (EGF, TGF-alpha, amphiregulin, betacellulin, "
        "epiregulin, epigen, HB-EGF) to initiate signal transduction cascades controlling cell "
        "proliferation, survival, differentiation, and migration. Upon ligand binding, EGFR "
        "undergoes homo- or heterodimerization (with ERBB2, ERBB3, ERBB4), which activates the "
        "intracellular tyrosine kinase domain through trans-autophosphorylation. Phosphorylated "
        "tyrosine residues in the C-terminal tail serve as docking sites for SH2/PTB domain-containing "
        "adaptor proteins (GRB2, SHC, etc.), leading to activation of RAS-RAF-MEK-ERK (MAPK), "
        "PI3K-AKT, PLCgamma-PKC, and STAT signaling pathways. EGFR localizes primarily to the "
        "plasma membrane and continues signaling from early endosomes after clathrin-mediated "
        "endocytosis. Receptor downregulation occurs through CBL-mediated ubiquitination and "
        "lysosomal degradation. EGFR mutations and overexpression drive multiple cancers including "
        "non-small cell lung cancer, colorectal cancer, and glioblastoma."
    )

    # Set status to COMPLETE
    data["status"] = "COMPLETE"

    # Save the updated YAML
    save_yaml(data, yaml_path)

    # Print statistics
    print(f"\nReview Statistics:")
    print(f"  Total annotations: {stats['total']}")
    print(f"  Already reviewed: {stats['already_reviewed']}")
    print(f"  Newly reviewed: {stats['reviewed']}")
    print(f"  No match found: {stats['no_match']}")
    print(f"\nActions assigned:")
    for action, count in sorted(stats["by_action"].items()):
        print(f"  {action}: {count}")


if __name__ == "__main__":
    main()
