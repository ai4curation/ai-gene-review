# FGF19 (human, O95750) curation notes

## Identity
- 216 aa secreted protein; UniProt annotates a signal peptide (1..24) and mature chain 25..216; "SUBCELLULAR LOCATION: Secreted." Human ortholog of mouse Fgf15.
- Note: the Falcon deep-research file states FGF19 "lacks a conventional signal peptide" (citing a 2026 review). This conflicts with the UniProt SIGNAL feature 1..24 and should not be used.

## Core biology (with provenance)
- Endocrine FGF19 subfamily: reduced heparin-binding affinity confers endocrine mode of action; requires Klotho/betaKlotho
  [PMID:17339340 "This reduces the heparin-binding affinity of these ligands and confers endocrine function."]
- Receptor: high-affinity, heparin-dependent ligand of FGFR4
  [PMID:10525310 "FGF-19 is a high affinity, heparin dependent ligand for FGFR4 and is the first member of the FGF family to show exclusive binding to FGFR4."]
- beta-Klotho (KLB) co-receptor is required for FGF19 binding to FGFR4 and signaling
  [PMID:17627937 "KLB is required for FGF19 binding to FGFR4, intracellular signaling, and downstream modulation of gene expression."]
  [PMID:17623664 "Here we show that, like FGF21, FGF19 also requires betaKlotho."]
- FGF19 can also signal via KLB-FGFR1c/2c/3c (unlike FGF21, it also signals efficiently through FGFR4)
  [PMID:17623664 "Both FGF19 and FGF21 can signal through FGFR1-3 bound by betaKlotho and increase glucose uptake in adipocytes expressing FGFR1."]
  [PMID:18187602 "By contrast, these cells were stimulated fully by FGF19, which induced maximal DNA synthesis at levels comparable to FGF1 in all four transfectants examined."]
- Binds both alpha- and beta-Klotho in vitro; C-terminal tail determines Klotho recognition
  [PMID:18829467 "We previously showed that FGF19 can bind to both alpha and betaKlotho"]
- Bile acid feedback: FXR induces FGF19; FGF19 represses CYP7A1 in human hepatocytes and mouse liver
  [PMID:12815072 "We demonstrate that FXR directly regulates expression of fibroblast growth factor-19 (FGF-19), a secreted growth factor that signals through the FGFR4 cell-surface receptor tyrosine kinase."]
  [PMID:19085950 "FGF19 strongly and rapidly repressed CYP7A1 but not small heterodimer partner (SHP) mRNA levels."]
  Mouse ortholog: [PMID:16213224 "Mice lacking FGF15 have increased hepatic CYP7A1 mRNA and protein levels and corresponding increases in CYP7A1 enzyme activity and fecal bile acid excretion."]
- Downstream kinase: ERK1/2 is well supported; JNK is contested.
  - Holt 2003: JNK activity increased [PMID:12815072 "Thus, FGF-19 treatment of primary human hepatocytes is able to activate the JNK pathway."]
  - Song 2009: [PMID:19085950 "Surprisingly, FGF19 did not activate JNK in this assay."] and [PMID:19085950 "FGF19 (40 ng/ml) time-dependently stimulated phosphorylation of ERK1/2 in primary human hepatocytes"]
- Hepatic glycogen/protein synthesis (insulin-independent, via Ras-ERK-p90RSK)
  [PMID:21436455 "We show that FGF19 stimulates hepatic protein and glycogen synthesis but does not induce lipogenesis."]
  [PMID:21436455 "Because recombinant mouse FGF15 is unstable and has variable bioactivity, we used human FGF19 for these studies."]
- Adipocyte glucose uptake is pharmacological; physiological relevance questioned by the authors
  [PMID:17623664 "contribution of FGF15/19 to the regulation of adipocyte function could be minimal under physiological conditions"]

## Annotation decisions (summary)
- Core MF: GO:0005104 fibroblast growth factor receptor binding (as in FGFR signaling module).
- Core BP: GO:0008543 FGFR signaling pathway; GO:0070858 negative regulation of bile acid biosynthetic process.
- NEW: GO:0045725 positive regulation of glycogen biosynthetic process (Kir 2011). Comparator check: INS carries GO:0045725 (IDA, PMID:17925406), i.e. hormones that trigger the signalling that raises glycogen synthesis carry this regulation term; the hormone does the signalling work (it is the ligand that activates the receptor), unlike a substrate.
- Hormone activity (GO:0005179): not carried by FGF19, FGF21 or FGF23 in QuickGO (checked 2026-09-30), so not proposed; raised as a question.
- REMOVE: cytoplasm IBA (secreted protein; family node includes intracellular FGFs), response to ethanol IEA (rat expression-response transfer).
- MODIFY: protein binding (KLB, KL) -> GO:0005102 signaling receptor binding; negative regulation of gene expression -> GO:0070858.
- GO:0005615 extracellular space is obsolete in the local GO build; used GO:0005576 extracellular region for core location.
