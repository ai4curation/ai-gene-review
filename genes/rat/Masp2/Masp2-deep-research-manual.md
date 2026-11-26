# Masp2 (rat, Q9JJS8) - manual literature synthesis

No deep-research API was available; this synthesis was assembled by hand from cached
publications in `publications/` and the UniProt record.

## Identity and gene structure
- Rat MASP-2 (mannan-binding lectin serine protease 2), 685 aa precursor; single gene also
  encodes MAp19 (isoform 2) by alternative polyadenylation/splicing
  [PMID:10586086 "Southern blot and PCR analyses of rat genomic DNA indicate that as in humans, rat MASP-2 and MAp19 are encoded by a single structural gene."].
- Domain order CUB1-EGF-CUB2-CCP1-CCP2-SP [PMID:22167201 "MASP-2 is constructed from six domains in the order CUB1-EGF-CUB2-SCR-1-SCR-2-SP"].
- Hepatic biosynthesis, plasma protein [PMID:10586086 "demonstrate their exclusively hepatic biosynthesis"].

## Molecular function
- Serine protease that cleaves C4 and C2 [PMID:15060079 "MASP-2 subsequently cleaves complement components C2 and C4 to activate the complement cascade."];
  rat zymogen and activated forms produced recombinantly; MBP stimulates autoactivation
  [PMID:15060079 "MBP stimulates MASP-2 autoactivation by increasing the rate of autocatalysis when MBP.MASP-2 complexes bind to a glycan-coated surface"].
- Active-site Ser613 (mature numbering; Ser632 in the precursor) and activation-cleavage
  Arg424 (mature; Arg443 precursor) [PMID:20118239 "MASP-2A is a catalytically inactive form in which the active site serine at position 613 has been replaced by an alanine."].
- Wild-type rat MASP-2 autoactivates [PMID:20118239 "Recombinant wild-type rat MASP-2 is toxic to producing Chinese hamster ovary cells and autoactivates during biosynthesis."].
- Accessory (exosite) binding of C4, and of C4b after cleavage [PMID:15060079 "MASP-2 binds to C4 while separate structural changes create a functional catalytic site able to cleave C4"];
  [PMID:17204478 "Following cleavage of C4, C4b still binds to MASP-2"].

## Assembly
- Ca2+-independent homodimer via CUB1-EGF; Ca2+-dependent binding to MBL collagenous region
  [PMID:10913141 "each truncated MASP is a Ca(2+)-independent homodimer in solution"];
  [PMID:10913141 "both MASPs associate independently with rat MBP in a Ca(2+)-dependent manner"].
- MBL binding site in collagen-like domain [PMID:14724269 "MASPs bind on the C-terminal side of the hinge region"].
- Crystal structure of rat CUB1-EGF-CUB2 dimer [PMID:12743029 "The CUB1-EGF-CUB2 region mediates homodimerization and binding to MBP."].
- Part of rat MBL activation complex [PMID:10586086 "We show that both MASP-2 and MAp19 are part of the rat MBL pathway activation complex"].

## Process
- Lectin-pathway initiation: MBL/ficolins bind pathogen carbohydrates, activating MASP-2
  [PMID:20118239 "MBLs and ficolins with MBL-associated serine protease-2 (MASP-2)"];
  activation only on carbohydrate target [PMID:20118239 "indicating that all MBLs activate only on a carbohydrate target"].
- C4b covalently deposits on pathogen surface [PMID:17204478 "generating C4b, which attaches covalently to the pathogen surface upon exposure of its reactive thioester"].

## Not supported for rat / likely over-annotation
- Golgi apparatus (secretory transit only), cell-surface PRR signaling (MBL/MASP is a soluble
  pattern-recognition complex, not a cell-surface receptor).
