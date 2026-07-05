# lys-1 (Caenorhabditis elegans) — research notes

UniProt: O62415 (LYS1_CAEEL) · WormBase: WBGene00003090 / Y22F5A.4 · Chromosome V
Gene product: Lysozyme-like protein 1 (LYS-1). Precursor with N-terminal signal peptide.

## Summary of what is KNOWN vs NOT KNOWN

### KNOWN
- lys-1 is a member of the C. elegans **protist-type (Entamoeba-type)** lysozyme family
  (`lys` genes), one of two lysozyme classes in the worm (the other being the
  invertebrate-type `ilys` genes). C. elegans has an unusually large, divergent lysozyme
  family: [PMID:21931778 "the nematode Caenorhabditis elegans harbours 15 phylogenetically
  diverse lysozyme genes, belonging to two distinct types, the protist- or Entamoeba-type
  (lys genes) and the invertebrate-type (ilys genes) lysozymes."]. lys-1 is one of the
  chromosome V protist-type lysozymes: [PMID:21931778 "Reddish/yellowish bar colours refer
  to the lysozymes from chromosome V (lys-1, lys-2, lys-3, and lys-7)"].
- Structurally it belongs to the **glycosyl hydrolase family 25 (GH25)** (UniProt SIMILARITY:
  "Belongs to the glycosyl hydrolase 25 family."; InterPro Glyco_hydro_25 IPR002053; PROSITE
  Ch-type lysozyme domain PS51904; CDD cd06416 GH25_Lys1-like; PANTHER PTHR23208:SF41).
- lys-1 is an **infection-inducible antibacterial effector**. It is among the most strongly
  induced genes upon infection with the Gram-negative bacterium *Serratia marcescens*:
  [PMID:12176330 "Among the most robustly induced are genes encoding lectins and lysozymes,
  known to be involved in immune responses in other organisms."]. Overexpression is
  protective: [PMID:12176330 "overexpression of the lysozyme gene lys-1 augments the
  resistance of C. elegans to S. marcescens."].
- lys-1 is required for normal resistance to the Gram-positive bacterium *Staphylococcus
  aureus*. RNAi knockdown reduces survival on S. aureus:
  [PMID:21209831 "we show that two of these genes, lys-1 and clc-1, are required for normal
  resistance to Staphylococcus aureus."]; [PMID:21209831 "The TD50 (time required for 50% of
  the nematodes to die) for lys-1 was 4.7 days (p<0.0001) ... compared to 6.8 days for the
  GFP RNAi control."].
- lys-1 is a **DAF-16/FOXO transcriptional target** and behaves as a synthetic dauer-formation
  (SynDaf) gene, linking innate immunity to the insulin/IGF-1 signalling (dauer) axis:
  [PMID:21209831 "Two of the latter genes, lys-1 and cpr-1, are known to participate in innate
  immunity"] (the whole screen was of DAF-16 targets; lys-1 gave a SynDaf phenotype, Table 1,
  19.1% dauer).
- lys-1 is induced by additional pathogens. It is transcriptionally upregulated by
  *Bacillus thuringiensis* in all three tested C. elegans strains:
  [PMID:21931778 "significant upregulation was found for lys-1 and lys-2 in all three C.
  elegans strains"]. It is also part of the intestinal ELT-2/GATA-regulated infection response
  program (HEP annotation, PMID:16968778 genome-wide study of intestinal innate immune genes).
- Expression / localization (from the UniProt curated summary of PMID:12176330 full text; the
  cached publication is abstract-only, so these come from the curator who read the full paper):
  expressed in intestine and in a subset of head neurons (IL2, IL6 and other head ganglia
  neurons); the protein localizes to vesicles in the apical region of intestinal cells
  (cytoplasmic vesicle / cytoplasmic vesicle lumen; apical part of cell).
- Direct genetic/overexpression evidence links lys-1 to defence against two pathogens:
  [PMID:21931778 "four lysozyme genes were directly shown by overexpression and mutant or
  RNAi-knock down analysis to contribute to the nematode's defence against pathogens: lys-1
  against Serratia marcescens and Staphylococcus aureus"].

### NOT KNOWN (knowledge gaps)
- **Whether LYS-1 actually has muramidase / lysozyme enzymatic (peptidoglycan-hydrolysing)
  activity is NOT demonstrated.** All functional data are genetic (expression, RNAi,
  overexpression); the protein has never been purified or assayed biochemically:
  [PMID:21931778 "All available data is based on genetic analysis, whereas none of the
  lysozymes have been characterized at the protein level."];
  [PMID:21931778 "our study (and most previous studies) only indicates, but does not strictly
  prove a defence function of these enzymes. Unequivocal evidence would require analysis of
  the purified protein, especially its ability to interact with the pathogen at the molecular
  level."].
  Critically, UniProt flags a **CAUTION** on the sequence itself:
  "Lacks conserved active site residues, suggesting it has no catalytic activity."
  (UniProt O62415, CC CAUTION line, ECO:0000305). So the `lysozyme activity` and
  `peptidoglycan catabolic process` / `cell wall macromolecule catabolic process` annotations
  are family-level IEA (InterPro) inferences that may not hold for this specific paralog.
- The **molecular substrate / target microbe surface molecule** of LYS-1 (if any) is unknown;
  no biochemical demonstration of peptidoglycan cleavage or bacteriolysis by LYS-1 exists.
- Whether lys-1 is **individually necessary** in vivo, or **redundant** within the 15-member
  lysozyme family, is not resolved. The evidence for a defence role is RNAi/overexpression, not
  a clean single-gene loss-of-function null; the large paralog family and overlapping infection
  induction profiles suggest possible redundancy [PMID:21931778 "the encountered genetic
  diversity may reflect functional diversity"].
- Whether lys-1 has a **digestive / nutritional (non-immune)** role, as lysozymes do in some
  organisms [PMID:21931778 "They ... play important roles in both immunity and digestion"], is
  untested in C. elegans.

## Per-annotation reasoning (GOA)

1. GO:0007165 signal transduction (IBA, GO_REF:0000033) — This IBA is propagated from a
   PANTHER subfamily (PTN000574946, seeded from *Dictyostelium*). Lysozymes are secreted
   antibacterial hydrolases / effectors, not signalling proteins; there is no evidence LYS-1
   transduces a signal. This is a spurious/over-broad phylogenetic propagation. → REMOVE.
2. GO:0045087 innate immune response (IBA, GO_REF:0000033) — supported by whole picture and by
   the experimental IMP/HEP annotations below; but IBA here is redundant with the stronger
   experimental annotations. Keep as non-core (BP context). → KEEP_AS_NON_CORE.
3. GO:0003796 lysozyme activity (IEA, InterPro IPR002053) — family/domain-based MF inference.
   NOT experimentally demonstrated for LYS-1, and UniProt CAUTION says it lacks conserved
   active-site residues. This is the central MF uncertainty. → UNDECIDED / MARK_AS_OVER_ANNOTATED
   (I will use UNDECIDED: cannot verify demonstrated activity, and cannot definitively rule out
   family activity without biochemistry; the CAUTION suggests possible pseudo-muramidase).
4. GO:0006950 response to stress (IEA, ARBA GO_REF:0000117) — extremely generic; ARBA
   machine-learned. The specific defense-response terms below capture the biology far better.
   → MARK_AS_OVER_ANNOTATED (too generic to be informative).
5. GO:0009253 peptidoglycan catabolic process (IEA, InterPro) — the BP counterpart of the
   unverified lysozyme MF; same caveat. → UNDECIDED.
6. GO:0016998 cell wall macromolecule catabolic process (IEA, InterPro) — same family-inference
   caveat, and it is a more general parent of peptidoglycan catabolism. → UNDECIDED.
7. GO:0060205 cytoplasmic vesicle lumen (IEA, UniProtKB-SubCell GO_REF:0000044) — SubCell
   propagation matching the curated location. Redundant with the EXP annotation; keep non-core.
   → KEEP_AS_NON_CORE.
8. GO:0060205 cytoplasmic vesicle lumen (EXP, PMID:12176330) — curated location from the
   primary paper (apical intestinal vesicles). → ACCEPT (CC location).
9. GO:0045087 innate immune response (HEP, PMID:16968778) — expression-based (ELT-2/GATA
   intestinal infection-response program). Consistent. → KEEP_AS_NON_CORE.
10. GO:0045087 innate immune response (IMP, PMID:21209831) — RNAi reduces S. aureus survival;
    solid experimental BP. → ACCEPT.
11. GO:0050830 defense response to Gram-positive bacterium (IMP, PMID:21209831) — S. aureus is
    Gram-positive; RNAi reduces survival on it. Directly supported and specific. → ACCEPT (core).
12. GO:0031410 cytoplasmic vesicle (IDA, PMID:12176330) — curated location. → ACCEPT (CC).
13. GO:0045177 apical part of cell (IDA, PMID:12176330) — apical intestinal localization.
    → ACCEPT (CC).
14. GO:0050829 defense response to Gram-negative bacterium (IEP, PMID:12176330) — induced by
    S. marcescens (Gram-negative) and overexpression protects. IEP = expression-based; the
    overexpression protection strengthens it. → ACCEPT (core BP).

## Family / paralog context (do not confuse lys-1 with paralogs)
- lys-1, lys-2, lys-3, lys-7 are chromosome V protist-type lysozymes; lys-4/5/6/10 chr IV;
  lys-8 chr II [PMID:21931778 Figure 1 legend].
- Functionally characterized paralogs by genetics: lys-2 (P. aeruginosa, B. thuringiensis),
  lys-5 & lys-7 (B. thuringiensis and others), ilys-3 (M. nematophilum) [PMID:21931778].
  These are DIFFERENT genes; lys-1's own direct evidence is S. marcescens + S. aureus.

## Provenance notes
- PMID:12176330 (Mallo et al., Curr Biol 2002) — cached copy is ABSTRACT-ONLY
  (full_text_available: false). Localization/tissue-specificity claims (apical intestinal
  vesicles; IL2/IL6 neurons) are in the UniProt curated record from the full text, not in the
  cached abstract. Do not quote those as verbatim supporting_text from the cache.
- PMID:21209831 (Jensen et al., PLoS ONE 2010) — FULL TEXT cached. Strong source for S. aureus
  RNAi phenotype and DAF-16/dauer link.
- PMID:21931778 (Boehnisch et al., PLoS ONE 2011) — FULL TEXT cached. Best source for
  protist-type classification, B. thuringiensis induction of lys-1, and the explicit "no
  protein-level characterization" statements underpinning the knowledge gaps.
- PMID:16968778 (Shapira et al., PNAS 2006) — ABSTRACT-ONLY. ELT-2/GATA intestinal
  infection-response program; source of the HEP innate-immune-response annotation.
