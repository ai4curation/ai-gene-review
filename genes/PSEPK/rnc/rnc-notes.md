# rnc (Ribonuclease 3 / RNase III) — Pseudomonas putida KT2440

UniProt: Q88MY5 (RNC_PSEPK), OrderedLocusName PP_1433, 229 aa.
Evidence level: PE 3 (Inferred from homology). All UniProt functional annotation is via
HAMAP-Rule MF_00104; no gene-specific experimental publications are present for this
ortholog. The genome sequence reference is the KT2440 genome paper [PMID:12534463].

## FUNCTION
- "Digests double-stranded RNA. Involved in the processing of primary rRNA transcript to
  yield the immediate precursors to the large and small rRNAs (23S and 16S). Processes
  some mRNAs, and tRNAs when they are encoded in the rRNA operon. Processes pre-crRNA and
  tracrRNA of type II CRISPR loci if present in the organism."
  [UniProt "Digests double-stranded RNA. Involved in the processing of primary rRNA transcript to yield the immediate precursors to the large and small rRNAs (23S and 16S). Processes some mRNAs, and tRNAs when they are encoded in the rRNA operon."]

RNase III is a Mg2+-dependent, double-stranded-RNA-specific endoribonuclease. Its principal
cellular role is the maturation of ribosomal RNA: it makes the initial endonucleolytic
cleavages in the long polycistronic pre-rRNA transcript to excise the immediate precursors
of 16S and 23S rRNA. Beyond rRNA processing, RNase III cleaves and thereby regulates the
abundance/translation of specific cellular mRNAs and participates in small-RNA-mediated
regulation, contributing to post-transcriptional control of gene expression.

## CATALYTIC ACTIVITY
- EC 3.1.26.3.
  [UniProt "Reaction=Endonucleolytic cleavage to 5'-phosphomonoester.; EC=3.1.26.3;"]
- The reaction is an endonucleolytic cleavage of double-stranded RNA producing products
  with 5'-phosphomonoester (and 3'-hydroxyl) termini.

## COFACTOR
- Mg(2+) (CHEBI:18420) is required.
  [UniProt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420;"]
- Active-site/metal-binding residues annotated by homology: ACT_SITE 44 and 116;
  Mg2+-binding residues 40, 113, 116.
  [UniProt "ACT_SITE        44" / "BINDING         40" "/ligand=\"Mg(2+)\""]

## DOMAIN ARCHITECTURE
- N-terminal RNase III catalytic domain (residues 5..127) and a C-terminal
  double-stranded-RNA-binding domain (DRBM, residues 154..224).
  [UniProt "DOMAIN          5..127" "/note=\"RNase III\"" ; "DOMAIN          154..224" "/note=\"DRBM\""]
- Pfam: PF00035 (dsrm) + PF14622; InterPro IPR011907 (RNase_III), IPR000999
  (RNase_III_dom), IPR014720 (dsRBD_dom). This dual-domain architecture (catalytic +
  dsRNA-binding) is the hallmark of the bacterial RNase III family.

## SUBUNIT / LOCALIZATION
- Homodimer. [UniProt "SUBUNIT: Homodimer."]
  The functional enzyme is a homodimer; each catalytic domain contributes to forming the
  two composite processing centers that cleave the two strands of the dsRNA substrate.
  This is the structural basis for the "identical protein binding" (GO:0042802) ARBA
  annotation.
- Cytoplasm. [UniProt "SUBCELLULAR LOCATION: Cytoplasm"]

## SIMILARITY
- "Belongs to the ribonuclease III family."
  [UniProt "Belongs to the ribonuclease III family."]

## GO REVIEW RATIONALE
Core functions (accept):
- GO:0004525 ribonuclease III activity (MF) — defining catalytic activity, EC 3.1.26.3.
- GO:0003725 double-stranded RNA binding (MF) — substrate-recognition activity via the
  DRBM domain; more specific than generic RNA binding.
- GO:0006364 rRNA processing (BP) — principal biological role (16S/23S excision from
  pre-rRNA).

Broad / less-specific terms (mark as over-annotated or modify when a specific sibling is
co-annotated):
- GO:0003723 RNA binding — generic parent of double-stranded RNA binding; over-annotated.
- GO:0006396 RNA processing — generic parent of rRNA/mRNA processing; over-annotated.
- GO:0019843 rRNA binding (UniProt keyword-derived; not in GOA list) — substrate is dsRNA;
  rRNA binding captured by the dsRNA-binding activity and rRNA processing.

Plausible secondary roles (keep as non-core / accept as supported by homology):
- GO:0006397 mRNA processing — RNase III processes specific mRNAs.
- GO:0010468 regulation of gene expression — post-transcriptional regulation via mRNA/sRNA
  cleavage; somewhat generic but biologically supported.
- GO:0042802 identical protein binding — homodimerization; supported by SUBUNIT.

Cellular component:
- GO:0005737 cytoplasm — accepted, consistent with subcellular location.

Note: there is no experimental evidence specific to the P. putida ortholog; all calls rest
on strong family-level homology (HAMAP MF_00104) plus the well-characterized biology of
bacterial RNase III (e.g., E. coli Rnc). Calls flagged accordingly.
