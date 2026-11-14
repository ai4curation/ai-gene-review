# DRL (BAB2_0264, Q2YIM3) review notes

Brucella abortus 2308 DXR-like (DRL) enzyme. The UniProt entry is unreviewed and is
still named "Oxidoreductase, putative" (an ECO:0000313 submitter name, not evidence).

## Sources

- PMID:20660776 (full text cached): identification by complementation, in vitro
  activity, kinetics and phylogeny of the DRL family.
- PMID:22442144 (abstract only in cache; PMC3346137): crystal structures (PDB 3UPL apo,
  3UPY with fosmidomycin).

## Activity

- B. abortus lacks DXR but has the other MEP pathway genes
  [PMID:20660776 "The completely sequenced genome of B. abortus lacks a DXR-encoding gene but it contains homologues of the rest of MEP pathway enzymes"].
- BAB2_0264 alone fully complements the MVA auxotrophy of a dxr-deleted E. coli strain
  but not dxs or ispD (MCT) mutants
  [PMID:20660776 "Transformation of EcAB4-10 cells with a vector harbouring only BAB2_0264 led to full complementation of MVA auxotrophy"].
- Purified His-tagged DRL converts DXP to MEP in an NADPH-dependent reaction, product
  confirmed by MS/MS, inhibited by fosmidomycin
  [PMID:20660776 "Samples containing either DRL or DXR were found to produce MEP from DXP in a similar fashion"];
  no product without NADPH.
- Kinetics: kcat 0.065 s-1, Km(DXP) 109 uM; kcat two to three orders of magnitude below
  DXR. Because B. abortus has no DXR and relies on the MEP pathway, DRL is its only
  route from DXP to MEP; the low in vitro rate is not a reason to treat the activity as
  secondary (it may reflect assay conditions with a C-terminally tagged protein).
- Homodimer by size-exclusion (PMID:20660776) and in the crystal (PMID:22442144).

## Binding properties

- N-terminal NAD(P)-binding Rossmann domain (InterPro IPR005106 / Pfam PF03447) and
  "NADPH-binding domain" in the structure abstract. No nucleotide-bound structure was
  checked here, so NADP binding stays at the generic term.
- UniProt records Mg2+ binding at residues 167, 168 and 232 from the PDB structures;
  the assay contains MgCl2. Whether the metal is catalytic (as in DXR) was not checked,
  so no magnesium ion binding row was added.

## Process

DRL performs the DXP -> MEP step itself (reductoisomerization with NADPH), so it
does work in GO:0019288; E. coli and other DXR enzymes carry this term for the same
step. A NEW involved_in row is therefore justified.

## Location

No localization experiment exists; no signal peptide or TM segment is annotated.
No location is asserted in core_functions.
