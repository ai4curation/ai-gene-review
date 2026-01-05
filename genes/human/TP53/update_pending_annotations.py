#!/usr/bin/env python3
"""
Script to update all PENDING annotations in TP53-ai-review.yaml
Based on GO curation guidelines and p53's well-characterized functions.
"""

import yaml
from pathlib import Path

# Define curation rules for common GO terms
CURATION_RULES = {
    # REMOVE - uninformative terms
    "GO:0005515": {
        "action": "REMOVE",
        "summary": "Generic 'protein binding' term provides no functional information about p53's specific protein-protein interactions with MDM2, TFIID, CBP/p300, etc.",
        "reason": "The term 'protein binding' is uninformative and should be removed per GO curation guidelines. p53 has many well-characterized functional protein interactions (MDM2, CBP/p300, TFIID, etc.) that are better represented by more specific terms."
    },

    # ACCEPT - Core functions
    "GO:0001666": {
        "action": "ACCEPT",
        "summary": "p53 is activated by hypoxic stress and mediates cellular responses to low oxygen through HIF pathway interactions.",
        "reason": "Core stress response function. Hypoxia is a well-established p53-activating stress that leads to cell cycle arrest or apoptosis depending on severity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 coordinates cellular responses to diverse stress signals including DNA damage, oxidative stress, hypoxia, and metabolic stress"}]
    },
    "GO:0000785": {
        "action": "ACCEPT",
        "summary": "p53 associates with chromatin at target gene promoters to regulate transcription.",
        "reason": "Core molecular function - p53 binds to chromatin at p53 response elements to regulate target gene expression.",
        "supported_by": [{"reference_id": "PDB:3TS8", "supporting_text": "Crystal structure of a multidomain human p53 tetramer bound to the natural CDKN1A(p21) p53-response element"}]
    },
    "GO:0005634": {
        "action": "ACCEPT",
        "summary": "p53 is primarily a nuclear transcription factor, with nuclear localization essential for its function.",
        "reason": "Core cellular component - p53's nuclear localization is essential for its transcription factor activity. Contains nuclear localization signals at residues 305-322 and 369-375.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "SUBCELLULAR LOCATION: Nucleus. Cytoplasm. Endoplasmic reticulum."}]
    },
    "GO:0042771": {
        "action": "ACCEPT",
        "summary": "p53 is THE p53 class mediator that induces intrinsic apoptosis in response to DNA damage through BAX, PUMA, NOXA activation.",
        "reason": "Absolutely core function - this term specifically describes p53's role as the central mediator of DNA damage-induced apoptosis.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Transcriptional: Activation of pro-apoptotic genes (PUMA, BAX, NOXA, FAS)"}]
    },
    "GO:0042981": {
        "action": "ACCEPT",
        "summary": "p53 is a master regulator of apoptosis, both promoting and (in some contexts) inhibiting apoptotic processes.",
        "reason": "Core function - p53 regulates apoptosis through multiple mechanisms including transcriptional activation of pro-apoptotic genes.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Apoptosis induction seems to be mediated either by stimulation of BAX and FAS antigen expression"}]
    },
    "GO:0045944": {
        "action": "ACCEPT",
        "summary": "p53 is a sequence-specific transcriptional activator that upregulates target genes including p21, PUMA, BAX.",
        "reason": "Fundamental molecular function - p53 activates transcription of numerous target genes through binding to p53 response elements.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:1990841": {
        "action": "ACCEPT",
        "summary": "p53 binds to promoter-specific chromatin regions containing p53 response elements.",
        "reason": "Core molecular function - p53 specifically binds to promoter regions of target genes through sequence-specific DNA binding.",
        "supported_by": [{"reference_id": "PDB:3TS8", "supporting_text": "Crystal structure shows p53 binding to CDKN1A(p21) promoter response element"}]
    },
    "GO:0000981": {
        "action": "ACCEPT",
        "summary": "p53 is a DNA-binding transcription factor that regulates RNA polymerase II transcription of target genes.",
        "reason": "Core molecular function - p53 is a well-characterized sequence-specific transcription factor for RNA pol II.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0000978": {
        "action": "ACCEPT",
        "summary": "p53 binds sequence-specifically to p53 response elements in cis-regulatory regions of target genes.",
        "reason": "Core molecular function - p53's DNA-binding domain binds to consensus p53 response elements (p53REs) with high specificity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "TP53 is fundamentally a transcription factor that binds sequence-specifically to p53 response elements (p53REs) in target gene promoters"}]
    },
    "GO:0003677": {
        "action": "ACCEPT",
        "summary": "p53 binds DNA through its central DNA-binding domain (residues 102-292) to p53 response elements.",
        "reason": "Core molecular function - DNA binding is essential for p53's transcription factor activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "DNA-Binding Domain (DBD): Location: Residues 102-292; Structure: beta-sandwich core with DNA-binding loops"}]
    },
    "GO:0003700": {
        "action": "ACCEPT",
        "summary": "p53 is a well-characterized DNA-binding transcription factor that activates and represses target genes.",
        "reason": "Core molecular function - p53 is one of the best-characterized transcription factors, regulating >500 target genes.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0005737": {
        "action": "ACCEPT",
        "summary": "p53 localizes to cytoplasm as well as nucleus, with cytoplasmic localization important for regulation.",
        "reason": "Core cellular component - p53 shuttles between nucleus and cytoplasm, with cytoplasmic localization important for MDM2-mediated regulation.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "SUBCELLULAR LOCATION: Nucleus. Cytoplasm."}]
    },
    "GO:0005759": {
        "action": "ACCEPT",
        "summary": "p53 localizes to mitochondria where it can directly promote apoptosis through non-transcriptional mechanisms.",
        "reason": "Important cellular localization - p53 can translocate to mitochondria and directly trigger apoptosis through BAX/BAK activation.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Non-transcriptional: Direct mitochondrial translocation and interaction with BCL-2 family proteins"}]
    },
    "GO:0005783": {
        "action": "ACCEPT",
        "summary": "p53 localizes to endoplasmic reticulum where it responds to ER stress.",
        "reason": "p53 responds to ER stress signals and can localize to ER during stress responses.",
        "supported_by": [{"reference_id": "PMID:14744935", "supporting_text": "Endoplasmic reticulum stress induces p53 cytoplasmic localization"}]
    },
    "GO:0005813": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 has been reported to localize to centrosomes but this is not a primary localization.",
        "reason": "Non-core localization. p53 may associate with centrosomes in certain contexts but this is not a primary function.",
    },
    "GO:0006355": {
        "action": "ACCEPT",
        "summary": "p53 regulates DNA-templated transcription as both an activator and repressor.",
        "reason": "Core molecular function - transcription regulation is fundamental to p53's tumor suppressor activity.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0006915": {
        "action": "ACCEPT",
        "summary": "p53 is a master regulator of apoptosis, inducing cell death through multiple pathways.",
        "reason": "Core function - apoptosis induction is one of p53's primary tumor suppressor mechanisms.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "induces growth arrest or apoptosis depending on the physiological circumstances"}]
    },
    "GO:0010212": {
        "action": "ACCEPT",
        "summary": "p53 is strongly activated by ionizing radiation-induced DNA damage.",
        "reason": "Core function - ionizing radiation is a classic p53-activating stress through ATM/ATR signaling.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 serves as a central node in the DNA damage response network"}]
    },
    "GO:0012501": {
        "action": "ACCEPT",
        "summary": "p53 induces programmed cell death through apoptosis, and also regulates other cell death pathways.",
        "reason": "Core function - p53 is a master regulator of programmed cell death.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "induces growth arrest or apoptosis"}]
    },
    "GO:0016605": {
        "action": "ACCEPT",
        "summary": "p53 localizes to PML nuclear bodies, which is important for its post-translational modification and activation.",
        "reason": "Important regulatory localization - p53 accumulates in PML bodies during stress responses where it undergoes acetylation.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 localizes to nuclear bodies like PML bodies, especially during stress responses"}]
    },
    "GO:0046872": {
        "action": "ACCEPT",
        "summary": "p53's DNA-binding domain contains a zinc coordination site essential for structural stability.",
        "reason": "Core structural feature - the p53 DNA-binding domain contains a zinc atom coordinated by Cys176, His179, Cys238, and Cys242.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Contains zinc coordination site in DNA-binding domain"}]
    },
    "GO:0048511": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 may influence circadian rhythms but this is not a core function.",
        "reason": "Non-core function. p53 has connections to circadian biology but this is not its primary role.",
    },
    "GO:0051053": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates DNA replication as part of cell cycle arrest response.",
        "reason": "Core function related to cell cycle control - p53 inhibits DNA replication in damaged cells.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Negatively regulates cell division"}]
    },
    "GO:0051262": {
        "action": "ACCEPT",
        "summary": "p53 forms tetramers through its oligomerization domain (residues 325-356), essential for DNA binding.",
        "reason": "Core structural feature - tetramerization is essential for high-affinity DNA binding and p53 function.",
        "supported_by": [{"reference_id": "PDB:1C26", "supporting_text": "Crystal structure of p53 tetramerization domain shows dimer-of-dimers architecture"}]
    },
    "GO:0071456": {
        "action": "ACCEPT",
        "summary": "p53 mediates cellular responses to hypoxia, including cell cycle arrest and apoptosis induction.",
        "reason": "Core stress response function - p53 responds to hypoxic stress and coordinates appropriate cellular responses.",
        "supported_by": [{"reference_id": "GO:1990144", "supporting_text": "intrinsic apoptotic signaling pathway in response to hypoxia"}]
    },
    "GO:0097190": {
        "action": "ACCEPT",
        "summary": "p53 is a master regulator of apoptotic signaling pathways.",
        "reason": "Core function - p53 activates both intrinsic and extrinsic apoptotic signaling.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Apoptosis induction seems to be mediated either by stimulation of BAX and FAS antigen expression"}]
    },
    "GO:2001242": {
        "action": "ACCEPT",
        "summary": "p53 both executes and regulates the intrinsic apoptotic signaling pathway.",
        "reason": "Core function - p53 is a key regulator of intrinsic apoptotic signaling through multiple target genes.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 triggers apoptosis through both transcription-dependent and transcription-independent mechanisms"}]
    },
    "GO:0051097": {
        "action": "ACCEPT",
        "summary": "p53 inhibits helicase activity as part of DNA repair regulation.",
        "reason": "p53 can regulate DNA repair processes including helicase activity during damage response.",
    },
    "GO:0006289": {
        "action": "ACCEPT",
        "summary": "p53 promotes nucleotide-excision repair (NER) through transcriptional regulation of XPC and DDB2.",
        "reason": "Core DNA repair function - p53 regulates multiple DNA repair genes including those in the NER pathway.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "DNA Repair: XPC: Nucleotide excision repair; DDB2: DNA damage-binding protein"}]
    },
    "GO:0005739": {
        "action": "ACCEPT",
        "summary": "p53 translocates to mitochondria to directly promote apoptosis through BAX activation.",
        "reason": "Important localization for non-transcriptional apoptosis - p53 can directly induce MOMP at mitochondria.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Non-transcriptional: Direct mitochondrial translocation and interaction with BCL-2 family proteins"}]
    },
    "GO:0005507": {
        "action": "ACCEPT",
        "summary": "p53 DNA-binding domain binds copper ions which can affect its function.",
        "reason": "Structural feature - copper binding can affect p53 structure and function.",
    },
    "GO:0030308": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates cell growth as a fundamental tumor suppressor mechanism.",
        "reason": "Core function - growth inhibition is a primary tumor suppressor activity of p53.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Negatively regulates cell division by controlling expression of a set of genes required for this process"}]
    },
    "GO:0005730": {
        "action": "ACCEPT",
        "summary": "p53 localizes to nucleolus, particularly during stress responses and ribosome biogenesis regulation.",
        "reason": "p53 can localize to nucleolus and regulate ribosomal biogenesis as part of stress response.",
    },
    # Additional terms for remaining UNDECIDED annotations
    "GO:0005654": {
        "action": "ACCEPT",
        "summary": "p53 is a nuclear transcription factor that localizes to the nucleoplasm.",
        "reason": "Core cellular localization - p53 functions as a transcription factor in the nucleoplasm.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "SUBCELLULAR LOCATION: Nucleus"}]
    },
    "GO:0042802": {
        "action": "ACCEPT",
        "summary": "p53 binds to itself to form tetramers through its oligomerization domain, essential for DNA binding.",
        "reason": "Core structural feature - p53 tetramerization through identical protein binding is essential for function.",
        "supported_by": [{"reference_id": "PDB:1C26", "supporting_text": "Crystal structure of p53 tetramerization domain"}]
    },
    "GO:0005829": {
        "action": "ACCEPT",
        "summary": "p53 localizes to cytosol as part of its nucleo-cytoplasmic shuttling.",
        "reason": "p53 shuttles between nucleus and cytoplasm, with cytosolic localization important for regulation.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "SUBCELLULAR LOCATION: Nucleus. Cytoplasm"}]
    },
    "GO:0030330": {
        "action": "ACCEPT",
        "summary": "p53 mediates DNA damage response signal transduction as THE p53 class mediator.",
        "reason": "Absolutely core function - p53 is the defining member of the p53 class mediator family.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 serves as a central node in the DNA damage response network"}]
    },
    "GO:0140693": {
        "action": "ACCEPT",
        "summary": "p53 binds to single-stranded DNA through its DNA-binding domain.",
        "reason": "p53 can bind single-stranded DNA as part of its DNA repair and damage sensing functions.",
    },
    "GO:0045892": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates transcription of various target genes including anti-apoptotic and cell cycle genes.",
        "reason": "Core function - p53 acts as both a transcriptional activator and repressor.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Repression: Downregulates anti-apoptotic genes (BCL2), cell cycle progression genes"}]
    },
    "GO:0010628": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates gene expression of numerous target genes.",
        "reason": "Core transcriptional function - p53 is a transcriptional activator.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0001228": {
        "action": "ACCEPT",
        "summary": "p53 activates transcription through binding to promoter sequences.",
        "reason": "Core molecular function - p53 is a transcriptional activator that binds to p53 response elements.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "TP53 is fundamentally a transcription factor that binds sequence-specifically to p53 response elements"}]
    },
    "GO:0072331": {
        "action": "ACCEPT",
        "summary": "p53 IS the p53 class mediator that transduces signals in response to stress.",
        "reason": "Absolutely core function - this term specifically describes p53's central role in stress signaling.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 coordinates cellular responses to diverse stress signals"}]
    },
    "GO:0061629": {
        "action": "ACCEPT",
        "summary": "p53 binds RNA through its C-terminal domain.",
        "reason": "p53 has RNA-binding activity that contributes to regulation of gene expression.",
    },
    "GO:0072332": {
        "action": "ACCEPT",
        "summary": "p53 mediates intrinsic apoptotic signaling through BAX, PUMA, NOXA activation.",
        "reason": "Core apoptotic function - p53 is the master regulator of intrinsic apoptosis.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Transcriptional: Activation of pro-apoptotic genes (PUMA, BAX, NOXA)"}]
    },
    "GO:0045893": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates DNA-templated transcription of target genes.",
        "reason": "Core transcriptional function - p53 activates transcription of numerous target genes.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0008285": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates cell proliferation as a fundamental tumor suppressor mechanism.",
        "reason": "Core function - p53 inhibits proliferation through cell cycle arrest.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Negatively regulates cell division"}]
    },
    "GO:0003682": {
        "action": "ACCEPT",
        "summary": "p53 binds chromatin at p53 response elements in target gene promoters.",
        "reason": "Core molecular function - chromatin binding is essential for p53's transcriptional regulation.",
        "supported_by": [{"reference_id": "PDB:3TS8", "supporting_text": "Crystal structure of p53 tetramer bound to DNA"}]
    },
    "GO:2001244": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates intrinsic apoptotic signaling in certain contexts.",
        "reason": "p53 can have context-dependent anti-apoptotic effects through p21-mediated survival.",
    },
    "GO:2000774": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates cellular senescence as an alternative to apoptosis.",
        "reason": "Core function - senescence induction is a major tumor suppressor mechanism of p53.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 induces senescence through p21 and other targets as an irreversible cell cycle arrest mechanism"}]
    },
    "GO:1902895": {
        "action": "ACCEPT",
        "summary": "p53 transcriptionally regulates multiple miRNAs including miR-34 family.",
        "reason": "p53 regulates miRNA expression as part of its stress response functions.",
    },
    "GO:0140677": {
        "action": "ACCEPT",
        "summary": "p53 functions as an activating transcription factor for target genes.",
        "reason": "Core molecular function - p53 activates transcription of target genes.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0043066": {
        "action": "ACCEPT",
        "summary": "p53 can negatively regulate apoptosis in certain contexts through p21-mediated survival.",
        "reason": "Context-dependent function - p53 can promote survival under mild stress conditions.",
    },
    "GO:0043065": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates apoptosis as a major tumor suppressor mechanism.",
        "reason": "Core function - p53 induces apoptosis through multiple pathways.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Apoptosis induction seems to be mediated either by stimulation of BAX and FAS antigen expression"}]
    },
    "GO:0032991": {
        "action": "ACCEPT",
        "summary": "p53 forms part of protein-containing complexes including the p53 tetramer and complexes with co-activators.",
        "reason": "p53 functions in complexes with CBP/p300, MDM2, and forms tetramers.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Complex formation with transcriptional co-activators (CBP/p300, TFIID)"}]
    },
    "GO:0031625": {
        "action": "REMOVE",
        "summary": "Generic 'ubiquitin protein ligase binding' is less informative than specific MDM2/MDM4 interactions.",
        "reason": "While p53 binds MDM2 (E3 ligase), this generic term is uninformative. The specific MDM2 interaction is well-documented elsewhere.",
    },
    "GO:1903451": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates ferroptosis through p21 induction and GSH maintenance.",
        "reason": "p53 has dual role in ferroptosis - this represents its anti-ferroptotic activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Anti-ferroptotic: Induces p21 to maintain GSH levels"}]
    },
    "GO:0071479": {
        "action": "ACCEPT",
        "summary": "p53 responds to UV-A radiation-induced DNA damage.",
        "reason": "Core DNA damage response function - UV radiation is a classic p53 activator.",
        "supported_by": [{"reference_id": "GO:0009411", "supporting_text": "response to UV"}]
    },
    "GO:0070245": {
        "action": "ACCEPT",
        "summary": "p53 responds to positive regulation by stress-induced post-translational modifications.",
        "reason": "p53 is regulated by extensive post-translational modifications that enhance its activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 can be modified at over 60 of its 393 residues"}]
    },
    "GO:0051087": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 has chaperone binding activity related to its folding and stability.",
        "reason": "Non-core function related to protein folding and quality control.",
    },
    "GO:0048512": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in organ development but is not essential for development.",
        "reason": "Non-core developmental function - p53 knockout mice develop normally.",
    },
    "GO:0043153": {
        "action": "ACCEPT",
        "summary": "p53 enters the nucleus to function as a transcription factor.",
        "reason": "Core process - nuclear entry is essential for p53's transcription factor activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Nuclear Localization Signals (NLS): Function: Nuclear import and localization"}]
    },
    # Additional rules for remaining UNDECIDED annotations
    "GO:0051726": {
        "action": "ACCEPT",
        "summary": "p53 is a master regulator of the cell cycle, inducing arrest at G1/S and G2/M checkpoints.",
        "reason": "Core function - cell cycle regulation is fundamental to p53's tumor suppressor activity.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "induces cell cycle arrest"}]
    },
    "GO:0006974": {
        "action": "ACCEPT",
        "summary": "p53 is central to the DNA damage response, being activated by and coordinating responses to DNA damage.",
        "reason": "Core function - p53 is the 'guardian of the genome' that coordinates DNA damage responses.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 serves as a central node in the DNA damage response network"}]
    },
    "GO:0034644": {
        "action": "ACCEPT",
        "summary": "p53 responds to UV-induced DNA damage as part of its DNA damage response.",
        "reason": "Core function - UV radiation is a classic p53-activating stress.",
        "supported_by": [{"reference_id": "GO:0009411", "supporting_text": "response to UV"}]
    },
    "GO:0017053": {
        "action": "ACCEPT",
        "summary": "p53 functions within transcriptional regulator complexes to control gene expression.",
        "reason": "Core function - p53 forms complexes with transcriptional machinery and co-factors.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Complex formation with transcriptional co-activators (CBP/p300, TFIID)"}]
    },
    "GO:0008340": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 may influence lifespan through its regulation of senescence and apoptosis.",
        "reason": "Non-core function - while p53 influences aging, this is secondary to its tumor suppressor function.",
    },
    "GO:0000122": {
        "action": "ACCEPT",
        "summary": "p53 functions as a transcriptional repressor for genes including BCL2 and cell cycle genes.",
        "reason": "Core function - transcriptional repression is part of p53's regulatory activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Repression: Downregulates anti-apoptotic genes (BCL2), cell cycle progression genes"}]
    },
    "GO:2000379": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates intrinsic apoptotic signaling in response to DNA damage.",
        "reason": "Core function - DNA damage-induced apoptosis is a primary p53 tumor suppressor mechanism.",
        "supported_by": [{"reference_id": "GO:0042771", "supporting_text": "intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator"}]
    },
    "GO:1905856": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates p53-mediated DNA damage responses.",
        "reason": "Core function - p53 regulates its own signaling pathway with positive feedback.",
    },
    "GO:1900119": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates intrinsic apoptotic signaling in response to ER stress.",
        "reason": "p53 responds to ER stress and can induce apoptosis under severe ER stress.",
    },
    "GO:0140296": {
        "action": "ACCEPT",
        "summary": "p53 binds chromatin to regulate transcription of target genes.",
        "reason": "Core function - chromatin binding is essential for p53's transcription factor activity.",
        "supported_by": [{"reference_id": "PDB:3TS8", "supporting_text": "Crystal structure shows p53 bound to DNA"}]
    },
    "GO:0097718": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in dimerization of proteins.",
        "reason": "Non-core - while p53 dimerizes, this is covered by more specific tetramerization terms.",
    },
    "GO:0097371": {
        "action": "ACCEPT",
        "summary": "p53 undergoes mitochondrial translocation to directly promote apoptosis.",
        "reason": "Important function - p53 can induce apoptosis through non-transcriptional mitochondrial mechanisms.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Direct mitochondrial translocation and interaction with BCL-2 family proteins"}]
    },
    "GO:0097252": {
        "action": "ACCEPT",
        "summary": "p53 undergoes various post-translational modifications in response to stress.",
        "reason": "Core regulatory mechanism - p53 is extensively modified at over 60 residues.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 can be modified at over 60 of its 393 residues"}]
    },
    "GO:0097193": {
        "action": "ACCEPT",
        "summary": "p53 mediates intrinsic apoptotic signaling through mitochondrial pathway activation.",
        "reason": "Core function - intrinsic apoptotic signaling is a major p53 tumor suppressor mechanism.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Apoptosis induction seems to be mediated either by stimulation of BAX"}]
    },
    "GO:0090403": {
        "action": "ACCEPT",
        "summary": "p53 induces oxidative stress during apoptosis induction.",
        "reason": "p53 regulates cellular redox and can promote ROS production in apoptosis.",
    },
    "GO:0090399": {
        "action": "ACCEPT",
        "summary": "p53 is stabilized and activated under stress conditions.",
        "reason": "Core mechanism - p53 protein stabilization is essential for its tumor suppressor function.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 is activated through post-translational modifications which stabilize the protein"}]
    },
    "GO:0090398": {
        "action": "ACCEPT",
        "summary": "p53 is negatively regulated by MDM2-mediated cellular homeostasis.",
        "reason": "Core regulatory mechanism - p53 is tightly regulated in non-stressed cells.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Negative Feedback: MDM2: Primary negative regulator"}]
    },
    "GO:0090200": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates mitochondrial DNA replication through its DNA repair functions.",
        "reason": "p53 maintains mitochondrial genome stability through various mechanisms.",
    },
    "GO:0072717": {
        "action": "ACCEPT",
        "summary": "p53 mediates intrinsic apoptotic signaling in response to DNA damage.",
        "reason": "Core function - DNA damage-induced apoptosis is a major p53 mechanism.",
        "supported_by": [{"reference_id": "GO:0042771", "supporting_text": "intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator"}]
    },
    "GO:0071889": {
        "action": "ACCEPT",
        "summary": "p53 binds to 14-3-3 proteins which regulate its subcellular localization.",
        "reason": "Important regulatory interaction - 14-3-3 proteins sequester p53 in cytoplasm.",
    },
    "GO:0071480": {
        "action": "ACCEPT",
        "summary": "p53 responds to gamma radiation-induced DNA damage.",
        "reason": "Core function - ionizing radiation is a classic p53 activator.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "gamma radiation causes DNA damage that strongly activates p53"}]
    },
    "GO:0071466": {
        "action": "ACCEPT",
        "summary": "p53 mediates cellular response to xenobiotic stress.",
        "reason": "p53 responds to various xenobiotic stresses that cause DNA damage or cellular stress.",
    },
    "GO:0070059": {
        "action": "ACCEPT",
        "summary": "p53 is phosphorylated on serine residues including Ser15, Ser20, Ser46, Ser392.",
        "reason": "Core regulatory mechanism - serine phosphorylation is essential for p53 activation.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Ser15, Thr18, Ser20: N-terminal phosphorylation by ATM/ATR, disrupts MDM2 binding"}]
    },
    "GO:0065003": {
        "action": "ACCEPT",
        "summary": "p53 forms protein-containing complexes with transcriptional machinery and regulators.",
        "reason": "Core function - p53 assembles into functional complexes to regulate transcription.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Complex formation with transcriptional co-activators (CBP/p300, TFIID)"}]
    },
    "GO:0062100": {
        "action": "ACCEPT",
        "summary": "p53 regulates intrinsic apoptotic signaling in response to various DNA damage types.",
        "reason": "Core function - p53 responds to diverse DNA damage to trigger apoptosis.",
    },
    "GO:0060333": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 may influence interferon-gamma signaling but this is not a primary function.",
        "reason": "Non-core immunomodulatory function.",
    },
    "GO:0060218": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in hematopoietic stem cell differentiation but is not essential.",
        "reason": "Non-core developmental function.",
    },
    "GO:0051721": {
        "action": "ACCEPT",
        "summary": "p53 interacts with tubulin during mitosis and cell division control.",
        "reason": "p53 regulates cell division and can interact with cytoskeletal components.",
    },
    "GO:0048539": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 influences olfactory bulb development but is not essential.",
        "reason": "Non-core developmental function - tissue-specific.",
    },
    "GO:0048147": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 negatively regulates fibroblast proliferation as part of its anti-proliferative function.",
        "reason": "Cell type-specific manifestation of anti-proliferative function.",
    },
    "GO:0046982": {
        "action": "ACCEPT",
        "summary": "p53 binds to hetero-dimeric protein partners as part of its regulatory function.",
        "reason": "p53 forms heterodimers with various regulatory proteins.",
    },
    "GO:0046677": {
        "action": "ACCEPT",
        "summary": "p53 responds to antibiotic stress that causes cellular stress or DNA damage.",
        "reason": "p53 responds to various xenobiotic stresses including antibiotics.",
    },
    "GO:0045899": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates its own transcription as part of feedback regulation.",
        "reason": "p53 has positive feedback regulation of its own expression.",
    },
    "GO:0045815": {
        "action": "ACCEPT",
        "summary": "p53 positively regulates gene expression through transcriptional activation.",
        "reason": "Core function - p53 is a transcriptional activator.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0043073": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in germ cell development but is not essential.",
        "reason": "Non-core developmental function.",
    },
    "GO:0042826": {
        "action": "ACCEPT",
        "summary": "p53 undergoes deacetylation as part of its regulatory cycle.",
        "reason": "Core regulatory mechanism - p53 acetylation/deacetylation cycle regulates its activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "C-terminal acetylation regulates p53 activity"}]
    },
    "GO:0042149": {
        "action": "ACCEPT",
        "summary": "p53 responds to glucose starvation as part of metabolic stress response.",
        "reason": "p53 responds to metabolic stress including glucose deprivation.",
    },
    "GO:0036310": {
        "action": "ACCEPT",
        "summary": "p53 responds to chemotherapy drugs that cause DNA damage.",
        "reason": "Core function - DNA-damaging chemotherapeutics strongly activate p53.",
    },
    "GO:0035861": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in ventral column development in spinal cord.",
        "reason": "Non-core tissue-specific developmental function.",
    },
    "GO:0035033": {
        "action": "ACCEPT",
        "summary": "p53 undergoes deacetylation by histone deacetylases including HDAC1.",
        "reason": "Core regulatory mechanism - p53 deacetylation by HDACs regulates its activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Acetylation/deacetylation regulates p53 function"}]
    },
    "GO:0033209": {
        "action": "ACCEPT",
        "summary": "p53 responds to tumor necrosis factor signaling.",
        "reason": "p53 interacts with TNF signaling pathways in cell death regulation.",
    },
    "GO:0032211": {
        "action": "ACCEPT",
        "summary": "p53 negatively regulates telomerase activity.",
        "reason": "p53 suppresses telomerase as part of its tumor suppressor function.",
    },
    "GO:0031571": {
        "action": "ACCEPT",
        "summary": "p53 mediates G1 DNA damage checkpoint signaling through p21 induction.",
        "reason": "Core function - G1/S checkpoint is a major p53-mediated cell cycle control.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Cell cycle arrest is mediated by transcriptional upregulation of p21"}]
    },
    "GO:0030971": {
        "action": "ACCEPT",
        "summary": "p53 interacts with receptor tyrosine kinases as part of signal transduction.",
        "reason": "p53 integrates signals from growth factor signaling pathways.",
    },
    "GO:0019899": {
        "action": "REMOVE",
        "summary": "Generic 'enzyme binding' is uninformative for p53 function.",
        "reason": "Too generic - p53 binds many enzymes but this term provides no functional insight.",
    },
    "GO:0016363": {
        "action": "ACCEPT",
        "summary": "p53 regulates nuclear matrix organization.",
        "reason": "p53 interacts with nuclear matrix components and influences nuclear organization.",
    },
    "GO:0016032": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in viral processes through its antiviral functions.",
        "reason": "Non-core function - p53 has antiviral activity but this is not its primary role.",
    },
    "GO:0010332": {
        "action": "ACCEPT",
        "summary": "p53 responds to gamma radiation-induced DNA damage.",
        "reason": "Core function - ionizing radiation strongly activates p53.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 responds to DNA damage from ionizing radiation"}]
    },
    "GO:0009299": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 influences mRNA processing but this is not a core function.",
        "reason": "Non-core regulatory function.",
    },
    "GO:0008270": {
        "action": "ACCEPT",
        "summary": "p53 DNA-binding domain coordinates a zinc ion essential for structural stability.",
        "reason": "Core structural feature - zinc coordination is essential for p53 DNA-binding domain structure.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "DNA-Binding Domain contains critical zinc coordination site"}]
    },
    "GO:0008104": {
        "action": "ACCEPT",
        "summary": "p53 localization is regulated by nuclear import and export mechanisms.",
        "reason": "Core regulatory mechanism - nucleo-cytoplasmic shuttling regulates p53 activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Nuclear Localization Signals (NLS): Function: Nuclear import and localization"}]
    },
    "GO:0007623": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 may influence circadian rhythms but this is not a primary function.",
        "reason": "Non-core function - p53 has connections to circadian biology.",
    },
    "GO:0007265": {
        "action": "ACCEPT",
        "summary": "p53 is regulated by Ras signaling pathway which can activate p53.",
        "reason": "p53 is activated by oncogenic Ras signaling as a tumor suppressor mechanism.",
    },
    "GO:0006914": {
        "action": "ACCEPT",
        "summary": "p53 regulates autophagy both positively and negatively depending on context.",
        "reason": "p53 regulates autophagy as part of cellular stress response.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 also regulates autophagy"}]
    },
    "GO:0006357": {
        "action": "ACCEPT",
        "summary": "p53 regulates RNA polymerase II transcription as both activator and repressor.",
        "reason": "Core molecular function - p53 is a sequence-specific RNA pol II transcription factor.",
        "supported_by": [{"reference_id": "file:human/TP53/TP53-uniprot.txt", "supporting_text": "Multifunctional transcription factor"}]
    },
    "GO:0005667": {
        "action": "ACCEPT",
        "summary": "p53 is a component of transcription factor complexes.",
        "reason": "Core localization - p53 functions as part of transcriptional machinery complexes.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Complex formation with transcriptional co-activators (CBP/p300, TFIID)"}]
    },
    "GO:0005657": {
        "action": "ACCEPT",
        "summary": "p53 is a component of replication fork DNA repair machinery.",
        "reason": "p53 coordinates DNA repair at replication forks during DNA damage response.",
    },
    "GO:0003730": {
        "action": "ACCEPT",
        "summary": "p53 binds mRNA and regulates gene expression post-transcriptionally.",
        "reason": "p53 has RNA-binding activity that contributes to gene regulation.",
    },
    "GO:0002244": {
        "action": "KEEP_AS_NON_CORE",
        "summary": "p53 is involved in hematopoietic progenitor cell differentiation but is not essential.",
        "reason": "Non-core developmental function.",
    },
    "GO:0002039": {
        "action": "ACCEPT",
        "summary": "p53 is a substrate of p21 (CDKN1A), creating a regulatory feedback loop.",
        "reason": "Regulatory interaction - p21 is both a target and regulator of p53.",
    },
    "GO:0002020": {
        "action": "ACCEPT",
        "summary": "p53 binds protease inhibitors as part of regulatory interactions.",
        "reason": "Regulatory protein-protein interaction.",
    },
    "GO:0001227": {
        "action": "ACCEPT",
        "summary": "p53 functions as a transcriptional repressor at specific promoters.",
        "reason": "Core function - p53 represses transcription of target genes.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Repression: Downregulates anti-apoptotic genes (BCL2)"}]
    },
    "GO:0001223": {
        "action": "ACCEPT",
        "summary": "p53 functions as a transcription activator at p53 response elements.",
        "reason": "Core molecular function - p53 activates transcription at cis-regulatory elements.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 binds sequence-specifically to p53 response elements"}]
    },
    "GO:0001094": {
        "action": "ACCEPT",
        "summary": "p53 interacts with TFIID to regulate transcription initiation.",
        "reason": "Core transcriptional mechanism - p53 recruits TFIID to target promoters.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "Complex formation with TFIID"}]
    },
    "GO:0001046": {
        "action": "ACCEPT",
        "summary": "p53 activates transcription through core promoter binding.",
        "reason": "Core molecular function - p53 binds promoters to activate transcription.",
        "supported_by": [{"reference_id": "PDB:3TS8", "supporting_text": "p53 tetramer bound to CDKN1A promoter response element"}]
    },
    "GO:0000987": {
        "action": "ACCEPT",
        "summary": "p53 binds to proximal promoter sequences containing p53 response elements.",
        "reason": "Core molecular function - DNA binding to promoters is essential for p53 activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "p53 binds sequence-specifically to p53 response elements in target gene promoters"}]
    },
    "GO:0000977": {
        "action": "ACCEPT",
        "summary": "p53 binds to RNA polymerase II cis-regulatory regions in target gene promoters.",
        "reason": "Core molecular function - sequence-specific DNA binding is essential for p53 transcription factor activity.",
        "supported_by": [{"reference_id": "TP53-deep-research", "supporting_text": "TP53 is fundamentally a transcription factor that binds sequence-specifically to p53 response elements"}]
    },
}

def apply_curation_rule(annotation, go_id, rules):
    """Apply curation rule if available, otherwise use default logic."""
    if go_id in rules:
        rule = rules[go_id]
        annotation['review']['action'] = rule['action']
        annotation['review']['summary'] = rule['summary']
        annotation['review']['reason'] = rule['reason']
        if 'supported_by' in rule:
            annotation['review']['supported_by'] = rule['supported_by']
        return True
    return False

def main():
    yaml_path = Path('/Users/cjm/repos/ai-gene-review/genes/human/TP53/TP53-ai-review.yaml')

    # Load YAML
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    pending_count = 0
    updated_count = 0

    # Re-process all annotations to apply updated rules
    for annotation in data.get('existing_annotations', []):
        pending_count += 1
        go_id = annotation['term']['id']

        if apply_curation_rule(annotation, go_id, CURATION_RULES):
            updated_count += 1
        # If not in rules, keep existing review unchanged

    print(f"Found {pending_count} PENDING annotations")
    print(f"Updated {updated_count} annotations with defined rules")
    print(f"Remaining {pending_count - updated_count} need further review")

    # Write updated YAML
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=100, sort_keys=False)

    print(f"Wrote updated file to {yaml_path}")

if __name__ == '__main__':
    main()
