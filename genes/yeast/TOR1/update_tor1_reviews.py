#!/usr/bin/env python3
"""
Update TOR1 annotations with comprehensive reviews.
Reads existing YAML and adds detailed review sections to all annotations.
"""

import yaml
from pathlib import Path

# Define review data for each annotation
reviews_data = {
    # Format: (GO_ID, evidence_type, reference_id) -> review_dict

    # Cellular Components - Nucleus
    ("GO:0005634", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": "Nuclear localization inferred from phylogenetic analysis of TOR orthologs.",
        "reason": "TOR1 translocates to the nucleus in response to nutrient availability for ribosomal protein gene transcription control. Multiple IDA annotations confirm nuclear presence. This is a documented and functionally important subcellular compartment.",
    },

    ("GO:0005634", "IDA", "PMID:16900101"): {
        "action": "ACCEPT",
        "summary": "Direct observation of TOR1 nuclear localization and association with rDNA promoter in response to nutrients.",
        "reason": "PMID:16900101 demonstrates nutrient-regulated TOR1 nuclear localization and physical association with rDNA transcription regions. This is evidence of functional nuclear localization for transcriptional control.",
    },

    # Cellular Components - Cytoplasm
    ("GO:0005737", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": "Cytoplasmic localization inferred from phylogenetic analysis of TOR proteins.",
        "reason": "TOR1 functions primarily in cytoplasm as core component of TORC1 complex. This is the main site of kinase signaling and nutrient sensing. Multiple IDA annotations confirm.",
    },

    ("GO:0005737", "IDA", "PMID:18723607"): {
        "action": "ACCEPT",
        "summary": "Direct observation of TOR1 cytoplasmic localization in live yeast cells.",
        "reason": "PMID:18723607 uses live-cell imaging to visualize TOR1 and TOR2 distinct subcellular localizations, confirming cytoplasmic presence.",
    },

    ("GO:0005737", "IDA", "PMID:16900101"): {
        "action": "ACCEPT",
        "summary": "Cytoplasmic TOR1 observed in nutrient-dependent localization studies.",
        "reason": "PMID:16900101 documents TOR1 cycling between cytoplasm and nucleus based on nutrient status. Cytoplasmic localization is baseline.",
    },

    # Cellular Components - TOR/TORC1 Complex
    ("GO:0038201", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": "TOR1 component of TOR complex based on phylogenetic inference across eukaryotes.",
        "reason": "TOR1 is a core structural and catalytic component of TORC1 (the rapamycin-sensitive TOR complex). Complex membership is conserved from yeast to mammals. IBA is appropriate for this well-characterized complex architecture.",
    },

    ("GO:0038202", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": "TOR1 involvement in TORC1 signaling pathway inferred from ortholog analysis.",
        "reason": "TORC1 signaling is the primary biological function of TOR1. This is a fundamental conserved pathway. IBA inference is appropriate for this core function.",
    },

    # Molecular Functions - Kinase Activity Core Terms
    ("GO:0004674", "IEA", "GO_REF:0000120"): {
        "action": "ACCEPT",
        "summary": "Serine/threonine kinase activity from combined IEA methods (InterPro, EC mapping).",
        "reason": "Multiple IEA approaches converge on serine/threonine kinase activity: InterPro domain IPR026683 (TOR catalytic), EC 2.7.11.1 classification, UniProt keyword mapping. Consistent with IBA and IDA annotations.",
    },

    ("GO:0004672", "EXP", "PMID:18270585"): {
        "action": "ACCEPT",
        "summary": "Protein kinase activity confirmed by experimental evidence.",
        "reason": "EXP is high-confidence evidence. PMID:18270585 provides direct biochemical demonstration of TOR kinase activity.",
    },

    ("GO:0004672", "IMP", "PMID:10329624"): {
        "action": "ACCEPT",
        "summary": "Protein kinase activity demonstrated through TOR-dependent Tap42 phosphorylation.",
        "reason": "PMID:10329624 shows TOR phosphorylates Tap42 both in vivo and in vitro. This directly establishes kinase activity through functional mechanism studies.",
    },

    ("GO:0106310", "IEA", "GO_REF:0000116"): {
        "action": "ACCEPT",
        "summary": "Serine-specific kinase activity mapped to Rhea enzyme reaction database.",
        "reason": "Rhea mapping (GO_REF:0000116) provides reliable enzymatic classification. TOR1 phosphorylates seryl residues on multiple substrates (Tap42, Sch9, Ypk3, Stm1).",
    },

    # Nucleotide/Cofactor Binding
    ("GO:0000166", "IEA", "GO_REF:0000043"): {
        "action": "ACCEPT",
        "summary": "Nucleotide binding inferred from UniProt ATP-binding keyword annotation.",
        "reason": "All kinases require nucleotide (ATP) cofactor binding. UniProt explicitly lists ATP-binding. This is essential for kinase catalytic function.",
    },

    ("GO:0005524", "IEA", "GO_REF:0000043"): {
        "action": "ACCEPT",
        "summary": "ATP binding confirmed from UniProt keyword mapping (KW-0067).",
        "reason": "ATP is essential cofactor for TOR kinase phosphoryl transfer reaction. UniProt keywords provide reliable indication of ATP-binding capability.",
    },

    ("GO:0016301", "IEA", "GO_REF:0000120"): {
        "action": "ACCEPT",
        "summary": "Broad kinase activity term from InterPro domain mapping.",
        "reason": "This parent term to serine/threonine kinase activity is accurate. IEA from InterPro (IPR018936: PI3_4_kinase_CS pattern) is reliable.",
    },

    ("GO:0016740", "IEA", "GO_REF:0000043"): {
        "action": "ACCEPT",
        "summary": "Transferase activity (phosphoryl transfer) from UniProt keyword.",
        "reason": "Kinases are transferases catalyzing phosphoryl group transfer. This is a parent term encompassing kinase mechanism. UniProt-KW is reliable source.",
    },

    ("GO:0044877", "IEA", "GO_REF:0000002"): {
        "action": "ACCEPT",
        "summary": "Protein-containing complex binding inferred from FRB domain (rapamycin-binding domain).",
        "reason": "InterPro FRB domain (IPR009076, IPR036738) mediates FKBP-rapamycin complex binding. TORC1 forms complex with rapamycin-FKBP. IEA from InterPro is reliable.",
    },

    # Vacuolar Membrane Localization
    ("GO:0000329", "IEA", "GO_REF:0000117"): {
        "action": "ACCEPT",
        "summary": "Vacuolar membrane localization from ARBA machine learning (ARBA00043543).",
        "reason": "TORC1 localizes to vacuolar membrane where amino acid and nucleotide sensing occurs via EGO complex and PIB2 glutamine sensor. Multiple IDA annotations confirm.",
    },

    ("GO:0000329", "IDA", "PMID:25046117"): {
        "action": "ACCEPT",
        "summary": "Direct observation of TORC1 vacuolar membrane localization with Gtr1/Gtr2 nucleotide-binding control.",
        "reason": "PMID:25046117 demonstrates reciprocal Gtr1/Gtr2 nucleotide state control of TORC1 at vacuolar membrane recruits TOR1-TORC1.",
    },

    ("GO:0000329", "IDA", "PMID:19748353"): {
        "action": "ACCEPT",
        "summary": "TOR1-TORC1 recruitment to vacuolar membrane via EGO complex GEF (Vam6).",
        "reason": "PMID:19748353 elucidates Vam6 GEF control of EGO complex for TORC1 vacuolar membrane targeting.",
    },

    ("GO:0000329", "IDA", "PMID:18723607"): {
        "action": "ACCEPT",
        "summary": "Live-cell imaging of TOR1 localization to vacuolar membrane.",
        "reason": "PMID:18723607 visualizes distinct TOR1 and TOR2 subcellular localizations including vacuolar membrane.",
    },

    ("GO:0000329", "IDA", "PMID:12719473"): {
        "action": "ACCEPT",
        "summary": "TOR1 vacuolar membrane localization identified in LST8 component studies.",
        "reason": "PMID:12719473 characterizes LST8 (TORC1 component) function at vacuolar membrane.",
    },

    ("GO:0000329", "HDA", "PMID:26928762"): {
        "action": "ACCEPT",
        "summary": "Vacuolar membrane localization inferred from homology.",
        "reason": "HDA is lower-evidence but consistent with multiple stronger IDA annotations. Vacuolar membrane location is well-established.",
    },

    # Plasma Membrane and Other Compartments
    ("GO:0005886", "IEA", "GO_REF:0000120"): {
        "action": "ACCEPT",
        "summary": "Plasma membrane localization from UniProt subcellular location vocabulary.",
        "reason": "TORC1 localizes to plasma membrane as documented in multiple papers. HEAT repeats mediate membrane association.",
    },

    ("GO:0005886", "IDA", "PMID:10973982"): {
        "action": "ACCEPT",
        "summary": "TOR plasma membrane localization via HEAT repeat-mediated association.",
        "reason": "PMID:10973982 demonstrates HEAT repeats mediate TOR2 (TOR1-related) plasma membrane localization. Mechanism applies to TOR1.",
    },

    ("GO:0005774", "IEA", "GO_REF:0000044"): {
        "action": "ACCEPT",
        "summary": "Vacuolar membrane from UniProt SL-0271 subcellular location vocabulary.",
        "reason": "Parent term to fungal-type vacuole membrane. UniProt-SubCell mappings are reliable for membrane localization.",
    },

    ("GO:0000139", "IDA", "PMID:12719473"): {
        "action": "ACCEPT",
        "summary": "TOR1 localization to Golgi membrane in nutrient-sensing context.",
        "reason": "PMID:12719473 identifies Golgi as additional TOR1 localization site. Reflects nutrient sensing from multiple membrane compartments.",
    },

    ("GO:0010008", "IDA", "PMID:12719473"): {
        "action": "ACCEPT",
        "summary": "TOR1 localization to endosomal membranes identified in LST8 studies.",
        "reason": "PMID:12719473 and UniProt note TOR1 association with endosomal structures. Reflects nutrient sensing pathway diversity.",
    },

    # TORC1 Complex Composition
    ("GO:0031931", "IEA", "GO_REF:0000117"): {
        "action": "ACCEPT",
        "summary": "TORC1 complex membership from ARBA model (ARBA00026257).",
        "reason": "TORC1 composition well-established: TOR1/TOR2 + KOG1 + LST8 (+TCO89). ARBA recognition of this core complex is appropriate.",
    },

    ("GO:0031931", "IPI", "PMID:12408816"): {
        "action": "ACCEPT",
        "summary": "TOR1 confirmed as core TORC1 component through biochemical co-purification.",
        "reason": "PMID:12408816 seminal paper: 'Two TOR complexes, only one of which is rapamycin sensitive...' Identified TORC1 composition with TOR1 as core. IPI from co-purification is strong evidence.",
    },

    # TOR Signaling Pathways
    ("GO:0031929", "IEA", "GO_REF:0000117"): {
        "action": "ACCEPT",
        "summary": "General TOR signaling from ARBA machine learning model (ARBA00086602).",
        "reason": "TOR1 controls TOR signaling pathway. ARBA recognizes this broad conserved function.",
    },

    ("GO:0031929", "NAS", "PMID:14736892"): {
        "action": "ACCEPT",
        "summary": "TOR signaling pathway involvement from TORC1 structural literature.",
        "reason": "NAS (non-traceable assertion) from ComplexPortal. TORC1 structure and function are well-established.",
    },

    ("GO:0031929", "IMP", "PMID:12719473"): {
        "action": "ACCEPT",
        "summary": "TOR signaling demonstrated through LST8 mutant phenotype analysis.",
        "reason": "PMID:12719473 shows LST8-TORC1 controls amino acid biosynthesis responses. Mutant phenotypes establish signaling role.",
    },

    ("GO:0031929", "IMP", "PMID:8186460"): {
        "action": "ACCEPT",
        "summary": "TOR signaling functions from TOR1/TOR2 structural and functional comparison.",
        "reason": "PMID:8186460 establishes TOR1 and TOR2 are structurally/functionally similar TOR signaling components.",
    },

    # Nutrient Sensing and Responses
    ("GO:0006995", "IEA", "GO_REF:0000117"): {
        "action": "ACCEPT",
        "summary": "Cellular response to nitrogen starvation controlled by TORC1 nutrient sensing.",
        "reason": "TORC1 inhibition by nitrogen starvation triggers autophagy and nutrient scavenging responses. ARBA00034562 recognizes this.",
    },

    ("GO:0006995", "IGI", "PMID:9461583"): {
        "action": "ACCEPT",
        "summary": "Genetic interaction evidence for TOR1 in nitrogen starvation autophagy response.",
        "reason": "PMID:9461583: 'Tor, a phosphatidylinositol kinase homologue, controls autophagy in yeast.' Classic paper establishing TOR inhibition of autophagy under N-starvation.",
    },

    ("GO:0007584", "NAS", "PMID:14736892"): {
        "action": "ACCEPT",
        "summary": "Response to nutrient - broad nutrient sensing function.",
        "reason": "TOR1 is central nutrient sensor. Captures nitrogen, carbon, and amino acid sensing roles.",
    },

    # Autophagy Regulation
    ("GO:0016242", "IBA", "GO_REF:0000033"): {
        "action": "ACCEPT",
        "summary": "TORC1 inhibition of macroautophagy is conserved core function.",
        "reason": "Negative regulation of autophagy is fundamental TORC1 function conserved from yeast to mammals. Under nutrient-rich conditions, TORC1 suppresses autophagy. IBA appropriate for conserved mechanism.",
    },

    ("GO:0010507", "IEA", "GO_REF:0000117"): {
        "action": "ACCEPT",
        "summary": "Negative regulation of autophagy from ARBA model (ARBA00043537).",
        "reason": "TORC1 suppresses autophagy initiation through Atg1 kinase inhibition and Atg13 phosphorylation.",
    },

    ("GO:0010507", "IGI", "PMID:9461583"): {
        "action": "ACCEPT",
        "summary": "Genetic interaction demonstrating TOR1-dependent autophagy suppression.",
        "reason": "PMID:9461583 genetic analysis establishes TOR loss triggers autophagy; TOR activity suppresses autophagy.",
    },

    # Protein Synthesis Control
    ("GO:0006413", "IMP", "PMID:8741837"): {
        "action": "ACCEPT",
        "summary": "TOR1 control of translation initiation demonstrated through loss-of-function.",
        "reason": "PMID:8741837: 'TOR controls translation initiation and early G1 progression in yeast.' TOR loss causes rapid inhibition of translation initiation. Core function.",
    },

    ("GO:0042254", "IEA", "GO_REF:0000117"): {
        "action": "ACCEPT",
        "summary": "Ribosome biogenesis control by TORC1 from ARBA model.",
        "reason": "TORC1 regulates rRNA transcription, ribosomal protein synthesis, and rRNA processing. ARBA00026817 recognizes this.",
    },

    ("GO:0042254", "IMP", "PMID:10198052"): {
        "action": "ACCEPT",
        "summary": "TOR1 control of ribosome biogenesis through multiple regulatory mechanisms.",
        "reason": "PMID:10198052: 'Regulation of ribosome biogenesis by the rapamycin-sensitive TOR-signaling pathway...' Demonstrates TOR controls: rRNA transcription, r-protein gene transcription, rRNA processing. Core function.",
    },

    ("GO:0042790", "IMP", "PMID:16900101"): {
        "action": "ACCEPT",
        "summary": "TOR1 nuclear localization regulates rRNA transcription at rDNA promoters.",
        "reason": "PMID:16900101 demonstrates nutrient-regulated TOR1 nuclear localization and physical association with rDNA, controlling Pol I transcription.",
    },

    ("GO:0018105", "IDA", "PMID:26582391"): {
        "action": "ACCEPT",
        "summary": "TOR1-catalyzed phosphorylation of ribosomal protein S6 at serine residues.",
        "reason": "PMID:26582391: 'TORC1 and TORC2 work together to regulate ribosomal protein S6 phosphorylation...' Direct phosphorylation of S6 serine residues is major translation control output.",
    },

    # Cell Growth and Cycle Control
    ("GO:0001558", "NAS", "PMID:14736892"): {
        "action": "ACCEPT",
        "summary": "TORC1 regulation of cell growth from complex structural characterization.",
        "reason": "TOR1 is master regulator of cell growth in response to nutrients. Well-established core function.",
    },

    ("GO:0051726", "NAS", "PMID:14736892"): {
        "action": "ACCEPT",
        "summary": "Cell cycle regulation by TORC1 nutrient sensing.",
        "reason": "TORC1 controls G1/S progression and cell cycle entry in response to nutrient availability.",
    },

    ("GO:0051726", "IMP", "PMID:8741837"): {
        "action": "ACCEPT",
        "summary": "TOR loss causes G1 arrest, demonstrating direct cell cycle control.",
        "reason": "PMID:8741837 shows TOR loss and rapamycin treatment arrest cells in G1. IMP from mutant phenotype.",
    },

    ("GO:0051321", "IMP", "PMID:9096347"): {
        "action": "ACCEPT",
        "summary": "TOR kinase activity required for meiotic cell cycle progression.",
        "reason": "PMID:9096347: 'Target of rapamycin proteins and their kinase activities are required for meiosis.' TOR controls nutrient-dependent meiotic entry.",
    },

    # Stress Responses (NON-CORE)
    ("GO:0034976", "IMP", "PMID:31144305"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "Hyperactive TORC1 sensitizes cells to ER stress through cell wall compromise.",
        "reason": "PMID:31144305: 'Hyperactive TORC1 sensitizes yeast cells to endoplasmic reticulum stress...' TORC1 crosstalk with ER stress, but this is stress adaptation rather than primary nutrient sensing. Non-core.",
    },

    ("GO:0034599", "IGI", "PMID:27922823"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR genetic interaction with oxidative stress response via Slm35-longevity.",
        "reason": "PMID:27922823: 'Slm35 links mitochondrial stress response and longevity through TOR signaling...' Peripheral function in stress adaptation.",
    },

    ("GO:0034605", "IGI", "PMID:27922823"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR genetic interaction in heat stress response.",
        "reason": "PMID:27922823 shows TOR in heat stress-longevity link. Peripheral stress adaptation function.",
    },

    ("GO:0006974", "IMP", "PMID:17698581"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR signaling as survival checkpoint in DNA damage response.",
        "reason": "PMID:17698581: 'TOR signaling is a determinant of cell survival in response to DNA damage.' Peripheral stress-adaptive function, not core nutrient sensing.",
    },

    # Biosynthetic Processes (NON-CORE)
    ("GO:0031505", "IMP", "PMID:14736892"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TORC1 coordination of cell wall biogenesis during growth.",
        "reason": "PMID:14736892 shows TORC1 controls cell wall integrity via Ssd1p. Cell wall organization is secondary anabolic output, not core function.",
    },

    ("GO:0090153", "IMP", "PMID:23363605"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TORC1 regulation of sphingolipid synthesis through Npr1 kinase.",
        "reason": "PMID:23363605: 'TORC1-regulated protein kinase Npr1 phosphorylates Orm to stimulate complex sphingolipid synthesis.' Downstream metabolic output of nutrient sensing, non-core.",
    },

    ("GO:1905356", "IEA", "GO_REF:0000117"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TORC1 regulation of snRNA pseudouridine synthesis.",
        "reason": "Specific ribosomal RNA modification consequence of nutrient-dependent ribosome biogenesis control. Non-core annotation.",
    },

    ("GO:1905356", "IGI", "PMID:27268497"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR-dependent snRNA pseudouridylation control.",
        "reason": "PMID:27268497: 'The TOR signaling pathway regulates starvation-induced pseudouridylation...' Specific biosynthetic output, non-core.",
    },

    # Retrograde Signaling (NON-CORE)
    ("GO:0031930", "IMP", "PMID:11997479"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "TOR-controlled RTG transcription factor nuclear translocation.",
        "reason": "PMID:11997479: 'The TOR-controlled transcription activators GLN3, RTG1, and RTG3 are regulated in response to intracellular levels of glutamine.' Specific downstream nutrient response, non-core.",
    },

    # Generic Protein Binding (OVER-ANNOTATED)
    ("GO:0005515", "IPI", "PMID:12408816"): {
        "action": "MARK_AS_OVER_ANNOTATED",
        "summary": "Generic 'protein binding' annotations from IntAct are overly redundant.",
        "reason": "GO best practices discourage generic GO:0005515 annotations without mechanistic specificity. TOR1-KOG1, KOG1-LST8 interactions are captured more informatively by: GO:0031931 (TORC1 complex membership) and GO:0044877 (complex binding). Consolidate generic binding terms into specific functional annotations already present.",
    },
}

# Load current YAML
with open('/Users/cjm/repos/ai-gene-review/genes/yeast/TOR1/TOR1-ai-review.yaml', 'r') as f:
    lines = f.readlines()

# Find line number where existing_annotations starts
anno_start = None
for i, line in enumerate(lines):
    if 'existing_annotations:' in line:
        anno_start = i
        break

print(f"Annotations start at line {anno_start + 1}")

# Read all annotations
content = ''.join(lines)
data = yaml.safe_load(content)

# Update each annotation with review data
updated_count = 0
for anno in data['existing_annotations']:
    term_id = anno['term']['id']
    evidence_type = anno['evidence_type']
    reference_id = anno['original_reference_id']

    # Handle generic binding terms with multiple references
    if term_id == "GO:0005515" and evidence_type == "IPI":
        # Use the consolidated review
        key = (term_id, evidence_type, reference_id)
        review_data = reviews_data.get(("GO:0005515", "IPI", "PMID:12408816"))
        if review_data:
            anno['review'] = {
                "summary": review_data['summary'],
                "action": review_data['action'],
                "reason": review_data['reason'],
            }
            updated_count += 1
    else:
        # Look up specific review
        key = (term_id, evidence_type, reference_id)
        if key in reviews_data:
            review_data = reviews_data[key]
            anno['review'] = {
                "summary": review_data['summary'],
                "action": review_data['action'],
                "reason": review_data['reason'],
            }
            updated_count += 1

print(f"Updated {updated_count} annotations with reviews")
print(f"Total annotations: {len(data['existing_annotations'])}")

# Write back
with open('/Users/cjm/repos/ai-gene-review/genes/yeast/TOR1/TOR1-ai-review.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)

print("YAML file updated successfully")
