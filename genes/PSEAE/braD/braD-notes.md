# braD (PA1073, P21627) notes

## Identity

- UniProt P21627 (Swiss-Prot, PE 3), 307 aa, gene braD, locus PA1073,
  P. aeruginosa PAO1. Fetched accession matches the worklist entry (rank 30).
- Polytopic inner-membrane permease, with ten predicted TM helices
  (UniProt FT TRANSMEM). Pfam PF02653 BPD_transp_2; CDD cd06582
  TM_PBP1_LivH_like; PANTHER PTHR11795:SF371 (LIVH). UniProt places it in the
  LivHM subfamily. TCDB 3.A.1.4.8.
- One of the two permease subunits (BraD, BraE) of LIV-I, the
  braC-braD-braE-braF-braG ABC importer (PA1074-PA1070).

## Literature

- Cloning: BraD is 67% identical to E. coli LivH and is a very hydrophobic
  membrane protein
  [PMID:2120183 "The braD gene product showed extensive homology (67% identical) to the livH gene product, a component required for the Escherichia coli high-affinity branched-chain amino acid transport systems."].
- Complementation shows braD is required for LIV-I
  [PMID:2120184 "confirming that the braD, braE, braF, and braG genes are required for the LIV-I transport system"].
- Reconstitution: BraDEFG form a membrane complex. With BraC, the complex
  transports Leu, the branched-chain amino acids, Ala and Thr in an
  ATP-dependent way
  [PMID:1400443 "In this reconstituted system, leucine transport was completely dependent on the presence of all five Bra components and on ATP loaded internally to the proteoliposomes."]
  [PMID:1400443 "Alanine and threonine in addition to branched-chain amino acids were transported by the proteoliposomes, reflecting the substrate specificity of the BraC protein."].
- LIV-I substrate range in cells
  [PMID:113383 "The former system seemed to serve not only for the entry of leucine, isoleucine, and valine, but also for that of alanine and threonine, although less effectively."].
- Johnson et al. 2008 Biolog screen (PMID:18833300, full text; PathoGenesis
  Mini-Tn5 mutant, strain PAK). PA1073 grows less well (+/-) on D-Ala (C) and
  L-Ile (C), and does not grow on L-Ala (C) (Table 2). No valine phenotype was
  recorded for PA1073
  [PMID:18833300 "In this work, mutants for each of these genes were found to be defective in Alanine metabolism, while utilization of L-Valine and L-Isoleucine was also altered in some cases"].
  The insertion in braD is in the middle of the operon and is likely polar on
  braE-braG. The phenotype is therefore an operon phenotype, which is harmless
  here because every bra gene is needed.

## Interpretation

Same as for braF (see genes/PSEAE/braF/braF-notes.md). L-Leu, L-Ile, L-Val,
L-Ala (and L-Thr) import by BraCDEFG is directly established. D-Ala import is
plausible but rests only on growth phenotypes. Phenylalanine comes from E. coli
LivH and has no P. aeruginosa support.

## PseudoCAP IBA-seed assessment

PTN000765102 is the LivH permease node: 18 leaves in 16 taxa (E. coli,
Salmonella and Yersinia LivH, Synechocystis LivH, BraD, PA4912, Geobacter,
Deinococcus (two), Thermotoga, Chloroflexus, Dictyoglomus, Clostridium,
Fusobacterium, Streptococcus, Streptomyces, Gloeobacter, Bradyrhizobium). It
carries E. coli LivH (P0AEX7)-seeded IBDs for L-leucine import, L-valine
transport, and L-Leu/Ile/Val/Phe transporter activity. PTN000209860 is a much
broader permease node (24+ leaves, including archaea (Sulfolobus, Pyrobaculum),
plants (Ricinus, tomato) and the urea permease UrtB), seeded by E. coli LivH
plus the two PseudoCAP rows.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000209860 | GO:0055085 transmembrane transport | 3 (P0AEX7, P21627, Q9HUQ1) | 50 (15 taxa) | GO:0042941 and GO:1903806, IMP, PMID:18833300 (PseudoCAP) | SOUND | The generic term suits a broad permease clade that includes urea and other HAAT substrates. It is independently supported by the E. coli LivH seed and by BraDEFG reconstitution. |
| PTN000765102 | GO:1903806 L-isoleucine import across plasma membrane | 1 (sole) | 18 (16 taxa) | GO:1903806, IMP, PMID:18833300 (PseudoCAP) | SOUND | The growth phenotype is corroborated by LIV-I uptake and BraC binding of Ile (PMID:113383, PMID:6767701). It matches the E. coli-seeded L-isoleucine transporter activity and L-leucine import IBDs at the same node. |
| PTN000765102 | GO:0015808 L-alanine transport | 1 (sole) | 18 (16 taxa) | GO:0015808, IMP, PMID:18833300 (PseudoCAP) | SOUND | The PA1073 mutant fails to grow on L-Ala, and BraCDEFG transports Ala in proteoliposomes. Correct for P. aeruginosa, but Ala is a secondary substrate set by BraC, and no non-P. aeruginosa seed supports it clade-wide. GO:1904273 L-alanine import across plasma membrane would be more precise. |
| PTN000765102 | GO:0042941 D-alanine transmembrane transport | 2 (P21627, Q9HUQ1) | 18 (16 taxa) | GO:0042941, IMP, PMID:18833300 (PseudoCAP) | INDIRECT-PHENOTYPE | Both seeds are partial D-Ala growth defects from one Biolog screen. No D-Ala uptake or binding has been shown for LIV-I. Plausible but not established. |

No source defects were filed. The L-Ile and L-Ala PseudoCAP rows are true of
LIV-I, and the D-Ala rows are left UNDECIDED, with a suggested question.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA); L-valine, L-isoleucine and L-leucine
  transporter activity (IBA); L-leucine import (IBA); L-isoleucine import
  (IBA, IMP).
- MODIFY: L-alanine transport (IBA, IMP) -> L-alanine import across plasma
  membrane; L-valine transmembrane transport (IBA) -> L-valine import across
  plasma membrane; membrane (IEA) -> plasma membrane; transmembrane
  transporter activity (IEA) -> ABC-type amino acid transporter activity;
  transmembrane transport (IEA) -> the four import terms.
- MARK_AS_OVER_ANNOTATED: L-phenylalanine transmembrane transporter activity
  (IBA), phenylalanine transport (IBA).
- UNDECIDED: D-alanine transmembrane transport (IBA, IMP).
- NEW: part_of the substrate-binding-subunit-containing ABC transporter
  complex (IDA, PMID:1400443).
