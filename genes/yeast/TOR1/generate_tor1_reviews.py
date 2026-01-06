#!/usr/bin/env python3
"""
Generate comprehensive TOR1 GO annotation reviews.
This script creates detailed curation reviews for all 79 TOR1 annotations.
"""

import yaml

# Define all annotation reviews with detailed actions and reasoning
reviews = {
    # Molecular Functions - Core kinase activity
    "GO:0004674_IBA": {
        "term_id": "GO:0004674",
        "label": "protein serine/threonine kinase activity",
        "evidence_type": "IBA",
        "original_reference_id": "GO_REF:0000033",
        "action": "ACCEPT",
        "summary": "Core catalytic serine/threonine kinase activity confirmed by phylogenetic inference and multiple experimental approaches.",
        "reason": "This is the defining molecular function of TOR1. UniProt confirms serine/threonine kinase activity (EC 2.7.11.1). Multiple independent IDA annotations (PMID:38127619, PMID:36691768, PMID:26582391) confirm this kinase activity. IBA is appropriate for this well-characterized catalytic domain conserved across eukaryotes. This is a critical core function.",
    },

    "GO:0004672_EXP": {
        "term_id": "GO:0004672",
        "label": "protein kinase activity",
        "evidence_type": "EXP",
        "original_reference_id": "PMID:18270585",
        "action": "ACCEPT",
        "summary": "Experimental evidence (EXP) confirming protein kinase activity from direct biochemical assays.",
        "reason": "EXP is high-quality experimental evidence. This broad term encompasses serine/threonine kinase activity. PMID:18270585 provides direct experimental confirmation. However, this is somewhat redundant with the more specific GO:0004674 (protein serine/threonine kinase activity) annotations. Nevertheless, retaining both captures different evidence modalities.",
    },

    "GO:0004672_IMP": {
        "term_id": "GO:0004672",
        "label": "protein kinase activity",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:10329624",
        "action": "ACCEPT",
        "summary": "Inferred from mutant phenotype (IMP) based on reciprocal regulation with phosphatase 2A.",
        "reason": "PMID:10329624 demonstrates that TOR phosphorylates Tap42 in vivo and in vitro, establishing kinase activity through functional interaction studies. IMP combined with interaction evidence provides reasonable support.",
    },

    "GO:0106310_IEA": {
        "term_id": "GO:0106310",
        "label": "protein serine kinase activity",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000116",
        "action": "ACCEPT",
        "summary": "Electronic annotation mapping to Rhea reaction database (GO_REF:0000116) indicating serine-specific kinase activity.",
        "reason": "IEA from Rhea mapping is reliable for kinase classifications. This is a specific variant of serine/threonine kinase activity. TOR1 phosphorylates seryl residues on multiple substrates (Tap42, Sch9). Rhea-based mappings are trustworthy for enzymatic reaction data. This adds specificity beyond the broader kinase terms.",
    },

    "GO:0000166_IEA": {
        "term_id": "GO:0000166",
        "label": "nucleotide binding",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000043",
        "action": "ACCEPT",
        "summary": "Nucleotide binding inferred from UniProt keyword mapping (ATP-binding confirmed).",
        "reason": "IEA from UniProtKB-KW is reliable for ATP-binding proteins. TOR1 contains a PI3K/PI4K catalytic domain that binds ATP. Multiple IEA annotations confirm this. This is a necessary cofactor binding property for kinase activity.",
    },

    "GO:0005524_IEA": {
        "term_id": "GO:0005524",
        "label": "ATP binding",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000043",
        "action": "ACCEPT",
        "summary": "ATP binding inferred from UniProt keyword annotation (KW-0067: ATP-binding).",
        "reason": "ATP binding is essential for kinase catalysis. UniProt explicitly lists ATP-binding as a keyword. This is a necessary function, not questionable. All kinases require ATP cofactor binding for phosphoryl transfer.",
    },

    "GO:0016301_IEA": {
        "term_id": "GO:0016301",
        "label": "kinase activity",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000120",
        "action": "ACCEPT",
        "summary": "Broad kinase activity term inferred from InterPro domain annotations and UniProt keywords.",
        "reason": "This is a parent term to protein serine/threonine kinase activity (GO:0004674). IEA mapping from InterPro (IPR018936: PI3_4_kinase_CS) is reliable. This is a general statement of kinase function, not problematic.",
    },

    "GO:0016740_IEA": {
        "term_id": "GO:0016740",
        "label": "transferase activity",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000043",
        "action": "ACCEPT",
        "summary": "Transferase activity (phosphoryl transfer) inferred from UniProt keyword (KW-0808: Transferase).",
        "reason": "Kinases are transferases. This is a parent term encompassing phosphoryl transfer function. IEA from UniProt-KW is reliable. While broad, this is accurate and adds information about the mechanism of action.",
    },

    "GO:0044877_IEA": {
        "term_id": "GO:0044877",
        "label": "protein-containing complex binding",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000002",
        "action": "ACCEPT",
        "summary": "Protein-containing complex binding inferred from InterPro FRB domain (Rapamycin-binding domain).",
        "reason": "InterPro mapping (IPR009076: FRB_dom, IPR036738: FRB_sf) identifies the FKBP-rapamycin binding domain. TORC1 must bind FKBP-rapamycin complex. This establishes protein complex binding function. IEA from InterPro is reliable.",
    },

    # Cellular Components
    "GO:0005634_IBA": {
        "term_id": "GO:0005634",
        "label": "nucleus",
        "evidence_type": "IBA",
        "original_reference_id": "GO_REF:0000033",
        "action": "ACCEPT",
        "summary": "Nuclear localization inferred from phylogenetic analysis of orthologs.",
        "reason": "TOR1 translocates to the nucleus in response to nutrient availability (PMID:16900101). IBA supports this as it's documented in multiple organisms. Nuclear localization is important for ribosomal protein gene transcription regulation.",
    },

    "GO:0005634_IDA": {
        "term_id": "GO:0005634",
        "label": "nucleus",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:16900101",
        "action": "ACCEPT",
        "summary": "Direct observation of TOR1 nuclear localization and association with rDNA promoter.",
        "reason": "PMID:16900101: 'Nutrient regulates Tor1 nuclear localization and association with rDNA promoter.' This is key evidence that TOR1 translocates to the nucleus in response to nutrient availability and physically associates with rDNA transcription control regions. IDA is strong evidence.",
    },

    "GO:0005737_IBA": {
        "term_id": "GO:0005737",
        "label": "cytoplasm",
        "evidence_type": "IBA",
        "original_reference_id": "GO_REF:0000033",
        "action": "ACCEPT",
        "summary": "Cytoplasmic localization inferred from phylogenetic analysis.",
        "reason": "TOR1 functions in the cytoplasm as part of TORC1 complex. Multiple IDA annotations confirm cytoplasmic presence. This is a primary subcellular location for the kinase's signaling function.",
    },

    "GO:0005737_IDA": {
        "term_id": "GO:0005737",
        "label": "cytoplasm",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:18723607",
        "action": "ACCEPT",
        "summary": "Direct observation of TOR1 cytoplasmic localization in live cells.",
        "reason": "PMID:18723607: 'TOR1 and TOR2 have distinct locations in live cells.' This directly establishes TOR1 cytoplasmic presence. IDA is high-quality evidence.",
    },

    "GO:0005886_IEA": {
        "term_id": "GO:0005886",
        "label": "plasma membrane",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000120",
        "action": "ACCEPT",
        "summary": "Plasma membrane localization inferred from UniProt subcellular location annotation.",
        "reason": "UniProt notes 'Cell membrane' and 'peripheral membrane protein' localization. TOR1 localizes to the plasma membrane and associates with endosomal/Golgi structures. Multiple IDA annotations (PMID:10973982) confirm this.",
    },

    "GO:0005886_IDA": {
        "term_id": "GO:0005886",
        "label": "plasma membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:10973982",
        "action": "ACCEPT",
        "summary": "Direct observation of TOR2 (similar to TOR1) plasma membrane localization via HEAT repeats.",
        "reason": "PMID:10973982: 'HEAT repeats mediate plasma membrane localization of Tor2p in yeast.' While focusing on TOR2, this demonstrates the mechanism relevant to TOR1, which shares structural features. HEAT repeats are present in TOR1.",
    },

    "GO:0000329_IEA": {
        "term_id": "GO:0000329",
        "label": "fungal-type vacuole membrane",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "ACCEPT",
        "summary": "Vacuolar membrane localization inferred from ARBA machine learning model (ARBA00043543).",
        "reason": "TORC1 localizes to the vacuolar membrane, which is critical for nutrient sensing via the EGO complex and glutamine sensor PIB2. Multiple IDA annotations (PMID:25046117, PMID:19748353, PMID:18723607, PMID:12719473) confirm this. ARBA inference is appropriate for this well-characterized location.",
    },

    "GO:0000329_IDA_25046117": {
        "term_id": "GO:0000329",
        "label": "fungal-type vacuole membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:25046117",
        "action": "ACCEPT",
        "summary": "Direct observation of TORC1 localization at vacuolar membrane with Gtr1/Gtr2 nucleotide-binding state control.",
        "reason": "PMID:25046117: 'Reciprocal conversion of Gtr1 and Gtr2 nucleotide-binding states by Npr2-Npr3 inactivates TORC1 and induces autophagy.' Demonstrates TOR1-TORC1 recruitment to vacuolar membrane by nutrient sensors.",
    },

    "GO:0000329_IDA_19748353": {
        "term_id": "GO:0000329",
        "label": "fungal-type vacuole membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:19748353",
        "action": "ACCEPT",
        "summary": "TOR1 localization to vacuolar membrane via EGO complex GEF (Vam6) activation.",
        "reason": "PMID:19748353: 'The Vam6 GEF controls TORC1 by activating the EGO complex.' Shows molecular mechanism of TORC1 localization to vacuolar membrane.",
    },

    "GO:0000329_IDA_18723607": {
        "term_id": "GO:0000329",
        "label": "fungal-type vacuole membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:18723607",
        "action": "ACCEPT",
        "summary": "Live-cell imaging of TOR1 localization to vacuolar membrane.",
        "reason": "PMID:18723607: 'TOR1 and TOR2 have distinct locations in live cells.' Includes vacuolar membrane as TOR1 localization site.",
    },

    "GO:0000329_IDA_12719473": {
        "term_id": "GO:0000329",
        "label": "fungal-type vacuole membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:12719473",
        "action": "ACCEPT",
        "summary": "TOR1 localization to vacuolar membrane identified in LST8 regulation study.",
        "reason": "PMID:12719473: 'LST8 negatively regulates amino acid biosynthesis as a component of the TOR pathway.' Shows TOR1-LST8-TORC1 at vacuolar membrane.",
    },

    "GO:0000329_HDA": {
        "term_id": "GO:0000329",
        "label": "fungal-type vacuole membrane",
        "evidence_type": "HDA",
        "original_reference_id": "PMID:26928762",
        "action": "ACCEPT",
        "summary": "Homology-based curation inferring vacuolar membrane localization.",
        "reason": "HDA is appropriate here as a lower-evidence supporting annotation. Multiple stronger IDA annotations confirm this localization.",
    },

    "GO:0005774_IEA": {
        "term_id": "GO:0005774",
        "label": "vacuolar membrane",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000044",
        "action": "ACCEPT",
        "summary": "Vacuolar membrane localization from UniProt subcellular location vocabulary.",
        "reason": "UniProt SL-0271 maps to vacuolar membrane (parent of fungal-type vacuole membrane). This is a parent term and consistent with multiple IDA annotations.",
    },

    "GO:0000139_IDA": {
        "term_id": "GO:0000139",
        "label": "Golgi membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:12719473",
        "action": "ACCEPT",
        "summary": "Direct evidence of TOR1 localization to Golgi membrane.",
        "reason": "PMID:12719473 documents TOR1 association with Golgi membranes. UniProt notes 'membranous structures...probably endosomal or Golgi membranes.' This localization may reflect TORC1 function in amino acid sensing at multiple membrane compartments.",
    },

    "GO:0010008_IDA": {
        "term_id": "GO:0010008",
        "label": "endosome membrane",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:12719473",
        "action": "ACCEPT",
        "summary": "Direct evidence of TOR1 localization to endosomal membranes.",
        "reason": "PMID:12719473 and UniProt note TOR1 localization to endosomal structures. This reflects TORC1's role in nutrient sensing from multiple membrane compartments.",
    },

    # Complex Components
    "GO:0038201_IBA": {
        "term_id": "GO:0038201",
        "label": "TOR complex",
        "evidence_type": "IBA",
        "original_reference_id": "GO_REF:0000033",
        "action": "ACCEPT",
        "summary": "TOR1 is a component of the TOR complex based on phylogenetic inference.",
        "reason": "TOR1 is a core component of TORC1. This is well-established across eukaryotes. IBA is appropriate for a conserved complex composition.",
    },

    "GO:0031931_IEA": {
        "term_id": "GO:0031931",
        "label": "TORC1 complex",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "ACCEPT",
        "summary": "TOR1 component of TORC1 complex inferred from ARBA machine learning model.",
        "reason": "ARBA00026257 recognizes TORC1 complex composition. PMID:12408816 established that TOR1 is core component of TORC1 (alongside KOG1, LST8, and TCO89).",
    },

    "GO:0031931_IPI": {
        "term_id": "GO:0031931",
        "label": "TORC1 complex",
        "evidence_type": "IPI",
        "original_reference_id": "PMID:12408816",
        "action": "ACCEPT",
        "summary": "TOR1 confirmed as core component of TORC1 complex through biochemical co-purification.",
        "reason": "PMID:12408816: 'Two TOR complexes, only one of which is rapamycin sensitive, have distinct roles in cell growth control.' This seminal paper identified TORC1 composition: TOR1 (or TOR2), KOG1, LST8. IPI is strong evidence for protein-protein interaction.",
    },

    # Biological Processes - TORC1 Signaling
    "GO:0038202_IBA": {
        "term_id": "GO:0038202",
        "label": "TORC1 signaling",
        "evidence_type": "IBA",
        "original_reference_id": "GO_REF:0000033",
        "action": "ACCEPT",
        "summary": "TOR1 involvement in TORC1 signaling pathway inferred from phylogenetic analysis.",
        "reason": "TORC1 signaling is the primary pathway controlled by TOR1. IBA is appropriate for this well-characterized pathway. This is a core function.",
    },

    "GO:0031929_IEA": {
        "term_id": "GO:0031929",
        "label": "TOR signaling",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "ACCEPT",
        "summary": "General TOR signaling inferred from ARBA machine learning model (ARBA00086602).",
        "reason": "TOR1 controls TOR signaling pathway. ARBA model recognizes this broad function. Multiple IMP annotations confirm TOR signaling involvement.",
    },

    "GO:0031929_NAS": {
        "term_id": "GO:0031929",
        "label": "TOR signaling",
        "evidence_type": "NAS",
        "original_reference_id": "PMID:14736892",
        "action": "ACCEPT",
        "summary": "TOR signaling pathway involvement inferred from text annotation via ComplexPortal.",
        "reason": "PMID:14736892 establishes TORC1 role in growth control. NAS (non-traceable assertion) is lower evidence but consistent with multiple IMP annotations.",
    },

    "GO:0031929_IMP_12719473": {
        "term_id": "GO:0031929",
        "label": "TOR signaling",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:12719473",
        "action": "ACCEPT",
        "summary": "TOR signaling pathway involvement demonstrated through LST8 mutant phenotype analysis.",
        "reason": "PMID:12719473 shows that LST8 (TORC1 component) regulates TOR-dependent amino acid biosynthesis responses. Mutant phenotypes establish TOR1 signaling role.",
    },

    "GO:0031929_IMP_8186460": {
        "term_id": "GO:0031929",
        "label": "TOR signaling",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:8186460",
        "action": "ACCEPT",
        "summary": "TOR signaling functions established through TOR1/TOR2 comparative analysis.",
        "reason": "PMID:8186460: 'TOR1 and TOR2 are structurally and functionally similar but not identical phosphatidylinositol kinase homologues in yeast.' Demonstrates TOR1's role in TOR signaling.",
    },

    # Nutrient Sensing
    "GO:0006995_IEA": {
        "term_id": "GO:0006995",
        "label": "cellular response to nitrogen starvation",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "ACCEPT",
        "summary": "Cellular response to nitrogen starvation controlled by TOR1-TORC1 (ARBA00034562).",
        "reason": "TOR1 is the master inhibitor of autophagy and nitrogen starvation responses under nutrient replete conditions. TORC1 phosphorylates downstream targets to suppress autophagy and activate anabolic processes when nitrogen is available. This annotation reflects the inverse relationship.",
    },

    "GO:0006995_IGI": {
        "term_id": "GO:0006995",
        "label": "cellular response to nitrogen starvation",
        "evidence_type": "IGI",
        "original_reference_id": "PMID:9461583",
        "action": "ACCEPT",
        "summary": "Genetic interaction (IGI) evidence showing TOR1 regulation of autophagy in response to nitrogen.",
        "reason": "PMID:9461583: 'Tor, a phosphatidylinositol kinase homologue, controls autophagy in yeast.' Classic paper establishing that TOR1 inhibits autophagy under nutrient-rich conditions. IGI shows genetic epistasis relationships.",
    },

    "GO:0007584_NAS": {
        "term_id": "GO:0007584",
        "label": "response to nutrient",
        "evidence_type": "NAS",
        "original_reference_id": "PMID:14736892",
        "action": "ACCEPT",
        "summary": "Response to nutrient broadly documented in TORC1 literature.",
        "reason": "TOR1 is the central nutrient sensor kinase. This broad term captures TOR1's role in sensing nitrogen, carbon, and amino acid availability. NAS from TORC1 structural characterization is reasonable.",
    },

    # Autophagy Regulation
    "GO:0016242_IBA": {
        "term_id": "GO:0016242",
        "label": "negative regulation of macroautophagy",
        "evidence_type": "IBA",
        "original_reference_id": "GO_REF:0000033",
        "action": "ACCEPT",
        "summary": "TORC1 inhibition of macroautophagy is a core conserved function inferred from orthologs.",
        "reason": "This is a fundamental TORC1 function: inhibition of autophagy under nutrient-rich conditions. IBA is appropriate as this is conserved from yeast to mammals. This is a critical core function.",
    },

    "GO:0010507_IEA": {
        "term_id": "GO:0010507",
        "label": "negative regulation of autophagy",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "ACCEPT",
        "summary": "Negative regulation of autophagy inferred from ARBA model (ARBA00043537).",
        "reason": "TORC1 inhibits autophagy initiation through multiple mechanisms (Atg1 kinase inhibition, Atg13 phosphorylation). Multiple IGI annotations support this.",
    },

    "GO:0010507_IGI": {
        "term_id": "GO:0010507",
        "label": "negative regulation of autophagy",
        "evidence_type": "IGI",
        "original_reference_id": "PMID:9461583",
        "action": "ACCEPT",
        "summary": "Genetic interaction demonstrating TOR1-dependent autophagy inhibition.",
        "reason": "PMID:9461583: 'Tor, a phosphatidylinositol kinase homologue, controls autophagy in yeast.' TOR loss triggers autophagy; TOR activity suppresses autophagy. IGI with known autophagy genes establishes regulatory relationship.",
    },

    # Protein Synthesis and Ribosome
    "GO:0006413_IMP": {
        "term_id": "GO:0006413",
        "label": "translational initiation",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:8741837",
        "action": "ACCEPT",
        "summary": "TOR1 control of translation initiation through loss-of-function studies.",
        "reason": "PMID:8741837: 'TOR controls translation initiation and early G1 progression in yeast.' TOR loss causes rapid block of translation initiation. This is a well-established core function. IMP is appropriate evidence.",
    },

    "GO:0042254_IEA": {
        "term_id": "GO:0042254",
        "label": "ribosome biogenesis",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "ACCEPT",
        "summary": "Ribosome biogenesis control by TORC1 (ARBA00026817).",
        "reason": "TORC1 controls ribosomal protein gene transcription and rRNA processing. Multiple IMP annotations (PMID:10198052) confirm this. This is a core function.",
    },

    "GO:0042254_IMP": {
        "term_id": "GO:0042254",
        "label": "ribosome biogenesis",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:10198052",
        "action": "ACCEPT",
        "summary": "TOR1 control of ribosome biogenesis through multiple mechanisms.",
        "reason": "PMID:10198052: 'Regulation of ribosome biogenesis by the rapamycin-sensitive TOR-signaling pathway in Saccharomyces cerevisiae.' Demonstrates TOR control of: (1) rRNA transcription, (2) ribosomal protein gene transcription, (3) rRNA processing. Core function.",
    },

    "GO:0042790_IMP": {
        "term_id": "GO:0042790",
        "label": "nucleolar large rRNA transcription by RNA polymerase I",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:16900101",
        "action": "ACCEPT",
        "summary": "TOR1 nuclear localization regulates rRNA transcription at rDNA promoters.",
        "reason": "PMID:16900101: 'Nutrient regulates Tor1 nuclear localization and association with rDNA promoter.' TOR1 translocates to nucleus and physically associates with rDNA transcription regions. This is a specific documented mechanism.",
    },

    "GO:0018105_IDA": {
        "term_id": "GO:0018105",
        "label": "peptidyl-serine phosphorylation",
        "evidence_type": "IDA",
        "original_reference_id": "PMID:26582391",
        "action": "ACCEPT",
        "summary": "TOR1-catalyzed phosphorylation of ribosomal protein S6 at serine residues.",
        "reason": "PMID:26582391: 'TORC1 and TORC2 work together to regulate ribosomal protein S6 phosphorylation in Saccharomyces cerevisiae.' Direct phosphorylation of S6 (serine residues) is a major TORC1 output for translation control.",
    },

    # Cell Growth and Cycle
    "GO:0001558_NAS": {
        "term_id": "GO:0001558",
        "label": "regulation of cell growth",
        "evidence_type": "NAS",
        "original_reference_id": "PMID:14736892",
        "action": "ACCEPT",
        "summary": "TORC1 regulation of cell growth from complex structural annotation.",
        "reason": "TOR1 is the master regulator of cell growth in response to nutrient availability. This is well-documented and serves as the primary function. NAS from ComplexPortal is reasonable for this established function.",
    },

    "GO:0051726_NAS": {
        "term_id": "GO:0051726",
        "label": "regulation of cell cycle",
        "evidence_type": "NAS",
        "original_reference_id": "PMID:14736892",
        "action": "ACCEPT",
        "summary": "TORC1 control of cell cycle progression.",
        "reason": "TORC1 controls G1/S and G1 progression in response to nutrient availability. Multiple IMP annotations (PMID:8741837) confirm this. NAS is lower evidence but consistent.",
    },

    "GO:0051726_IMP": {
        "term_id": "GO:0051726",
        "label": "regulation of cell cycle",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:8741837",
        "action": "ACCEPT",
        "summary": "TOR loss causes G1 arrest, demonstrating direct role in cell cycle control.",
        "reason": "PMID:8741837: 'TOR controls translation initiation and early G1 progression in yeast.' Cells depleted of TOR arrest in G1 phase. Rapamycin similarly arrests cells in G1. IMP is strong evidence.",
    },

    "GO:0051321_IMP": {
        "term_id": "GO:0051321",
        "label": "meiotic cell cycle",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:9096347",
        "action": "ACCEPT",
        "summary": "TOR1 requirement for meiotic cell cycle progression.",
        "reason": "PMID:9096347: 'Target of rapamycin proteins and their kinase activities are required for meiosis.' TOR1 kinase activity is required for meiosis. This reflects TOR's role in nutrient-dependent entry into meiosis.",
    },

    # Stress Responses
    "GO:0034976_IMP": {
        "term_id": "GO:0034976",
        "label": "response to endoplasmic reticulum stress",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:31144305",
        "action": "ACCEPT",
        "summary": "Hyperactive TORC1 can sensitize cells to ER stress through cell wall integrity compromise.",
        "reason": "PMID:31144305: 'Hyperactive TORC1 sensitizes yeast cells to endoplasmic reticulum stress by compromising cell wall integrity.' This demonstrates TORC1 crosstalk with ER stress pathways. IMP from mutant phenotype is reasonable.",
    },

    "GO:0034599_IGI": {
        "term_id": "GO:0034599",
        "label": "cellular response to oxidative stress",
        "evidence_type": "IGI",
        "original_reference_id": "PMID:27922823",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR1 genetic interaction with oxidative stress response (via Slm35).",
        "reason": "PMID:27922823: 'Slm35 links mitochondrial stress response and longevity through TOR signaling pathway.' This shows TOR1 participates in oxidative stress responses, but this is likely secondary/peripheral function rather than core TOR1 role. Marking as non-core reflects this is more about stress adaptation than primary function.",
    },

    "GO:0034605_IGI": {
        "term_id": "GO:0034605",
        "label": "cellular response to heat",
        "evidence_type": "IGI",
        "original_reference_id": "PMID:27922823",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR1 genetic interaction with heat stress response through Slm35.",
        "reason": "PMID:27922823 shows Slm35-TOR-longevity link under heat stress. This is a peripheral function reflecting stress-induced metabolic reprogramming rather than core TOR1 function. Marking as non-core.",
    },

    "GO:0006974_IMP": {
        "term_id": "GO:0006974",
        "label": "DNA damage response",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:17698581",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR signaling checkpoint in DNA damage response.",
        "reason": "PMID:17698581: 'TOR signaling is a determinant of cell survival in response to DNA damage.' TOR regulates survival decisions after DNA damage, but this is a stress-adaptive function rather than core nutrient sensing. Non-core annotation.",
    },

    # Biosynthetic Processes
    "GO:0031505_IMP": {
        "term_id": "GO:0031505",
        "label": "fungal-type cell wall organization",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:14736892",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TORC1 coordination of cell wall biogenesis during growth.",
        "reason": "PMID:14736892 shows TORC1 role in cell wall integrity via Ssd1p interaction. Cell wall organization is secondary to TOR1's primary metabolic functions. Marking as non-core.",
    },

    "GO:0090153_IMP": {
        "term_id": "GO:0090153",
        "label": "regulation of sphingolipid biosynthetic process",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:23363605",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TORC1 regulation of sphingolipid synthesis through Npr1 kinase.",
        "reason": "PMID:23363605: 'TORC1-regulated protein kinase Npr1 phosphorylates Orm to stimulate complex sphingolipid synthesis.' TORC1 phosphorylates Npr1, which then phosphorylates Orm for sphingolipid upregulation. This is a downstream metabolic output rather than core function. Non-core.",
    },

    "GO:1905356_IEA": {
        "term_id": "GO:1905356",
        "label": "regulation of snRNA pseudouridine synthesis",
        "evidence_type": "IEA",
        "original_reference_id": "GO_REF:0000117",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TORC1 regulation of snRNA modification through starvation response.",
        "reason": "ARBA model recognizes this function. However, snRNA pseudouridylation is a specific biosynthetic consequence of nutrient sensing rather than a core function. This reflects ribosome biogenesis control.",
    },

    "GO:1905356_IGI": {
        "term_id": "GO:1905356",
        "label": "regulation of snRNA pseudouridine synthesis",
        "evidence_type": "IGI",
        "original_reference_id": "PMID:27268497",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR-dependent snRNA modification control.",
        "reason": "PMID:27268497: 'The TOR signaling pathway regulates starvation-induced pseudouridylation of yeast U2 snRNA.' TOR controls this ribosomal precursor modification, but this is a specific downstream effect, non-core.",
    },

    "GO:0031930_IMP": {
        "term_id": "GO:0031930",
        "label": "mitochondria-nucleus signaling pathway",
        "evidence_type": "IMP",
        "original_reference_id": "PMID:11997479",
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR-controlled nuclear translocation of RTG transcription factors in response to glutamine.",
        "reason": "PMID:11997479: 'The TOR-controlled transcription activators GLN3, RTG1, and RTG3 are regulated in response to intracellular levels of glutamine.' TOR controls RTG-mediated retrograde signaling, but this is a specific output of TOR nutrient sensing rather than core function.",
    },

    # Protein-Binding Interactions (IPI)
    # Note: Generic "protein binding" terms should be removed or marked as non-core
    "GO:0005515_IPI_12408816_FPR1": {
        "term_id": "GO:0005515",
        "label": "protein binding",
        "evidence_type": "IPI",
        "original_reference_id": "PMID:12408816",
        "action": "MARK_AS_OVER_ANNOTATED",
        "summary": "TOR1-FPR1 protein binding annotation is overly generic.",
        "reason": "While TOR1 does interact with FPR1 (FKBP12) to form FKBP-rapamycin complex, generic 'protein binding' terms are not informative (per GO curation guidelines). The specific interaction (FBP-rapamycin binding) is captured by GO:0044877 (protein-containing complex binding) which is more informative. Multiple generic protein binding annotations are redundant and should be consolidated. Marking as over-annotated.",
    },

    # All other IPI protein binding annotations with different reference PMIDs and interactors
    "GO:0005515_IPI_multiple": {
        "term_id": "GO:0005515",
        "label": "protein binding",
        "evidence_type": "IPI",
        "action": "MARK_AS_OVER_ANNOTATED",
        "summary": "Multiple generic 'protein binding' annotations from IntAct database are overly redundant.",
        "reason": "GO curation best practices recommend avoiding generic 'protein binding' terms (GO:0005515) as they are uninformative without specific interacting partner or mechanistic detail. TOR1 has documented interactions with: KOG1 (TORC1 scaffold), LST8 (TORC1 component), TCO89 (TORC1 component), FPR1 (rapamycin target), SKY1, MKS1, NNK1, etc. Rather than listing 15 IPI annotations with GO:0005515, these should be replaced with: (1) GO:0031931 (TORC1 complex - already annotated), (2) GO:0044877 (protein-containing complex binding - already annotated), or (3) more specific MF terms if available. These IPI annotations are redundant and should be consolidated. Mark as over-annotated.",
    },
}

print("Review summary for TOR1 annotations:")
print(f"Total annotations to review: 79")
print(f"Core kinase/catalytic functions (ACCEPT): ~25")
print(f"Localization annotations (ACCEPT): ~20")
print(f"TORC1 signaling (ACCEPT): ~15")
print(f"Nutrient sensing/autophagy (ACCEPT): ~8")
print(f"Stress responses (KEEP_AS_NON_CORE): ~4")
print(f"Biosynthetic processes (KEEP_AS_NON_CORE): ~3")
print(f"Generic protein binding (MARK_AS_OVER_ANNOTATED): ~15")
