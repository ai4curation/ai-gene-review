# epmB (P39280, E. coli K-12) notes

Deep research was not available for this gene (falcon returns 403; asta gave
nothing useful in Phase 1 of the RADICAL_SAM project). These notes are built
from cached primary papers, UniProt, PubMed and QuickGO.

## Activity and stereochemistry

- EpmB (YjeK, b4146) is a radical SAM, PLP-dependent L-lysine 2,3-aminomutase
  of the KamA family. Its product is (R)-beta-lysine, the opposite enantiomer
  to the clostridial enzyme [PMID:17042480 "The product of the E. coli enzyme is (R)-beta-lysine, the enantiomer of the clostridial product."].
  kcat is about 0.1% of clostridial LAM [PMID:17042480].
- Radical mechanism with the 5'-deoxyadenosyl radical [PMID:17042480 "hydrogen transfer from C2 of (S)-beta-lysine to the 5'-deoxyadenosyl radical"].
- Rhea: RHEA:44148 "L-lysine = D-beta-lysine" (UniProt CATALYTIC ACTIVITY,
  ECO:0000269 PubMed:17042480). Rhea lists no EC and no GO term for it
  (checked 2026-10-19).
- GO:0050066 "L-lysine 2,3-aminomutase activity" is defined as
  "L-lysine = (3S)-3,6-diaminohexanoate" (QuickGO, checked 2026-10-19). That
  is the clostridial (S) product. **It does not fit EpmB**, so it should not be
  used; a new (3R)-forming term is proposed instead, with parent GO:0016869
  intramolecular aminotransferase activity.

## Role in EF-P modification

- Genomic context predicted that yjeK and yjeA act on EF-P [PMID:20070887].
- EpmA (PoxA/YjeA) ligates (R)-beta-lysine to EF-P Lys34; (R)-beta-lysine is
  about 100-fold better than alpha-lysine or (S)-beta-lysine [PMID:21841797].
- Both YjeA and YjeK are needed for beta-lysyl-EF-P in vivo [PMID:22128152].
  EpmC (YfcM) then hydroxylates the modified Lys34 [PMID:22706199].
- Salmonella yjeK and poxA mutants share virulence and stress phenotypes
  [PMID:20670890].

## Participation test for GO:0043687 post-translational protein modification

- Which entity performs the covalent step? EpmA (ligation onto EF-P) and EpmC
  (hydroxylation). EpmB makes the free amino acid donor and never touches
  EF-P.
- Comparator: QuickGO, E. coli BioB (P12996) has biotin biosynthetic process
  but not protein biotinylation; EpmA (P0A8N7) and EpmC (P76938) both carry
  GO:0043687. The donor-synthesis enzyme does not take the protein
  modification term.
- Decision: MARK_AS_OVER_ANNOTATED. EpmB is dedicated to and required for the
  pathway, so the term is not wrong in spirit, but EpmB does no work on the
  protein. GO has no beta-lysine biosynthetic process term; raised as a
  suggested question rather than proposed.

## Curation decisions

- GO:0003824, GO:0016869 (IBA, IDA): MODIFY to the proposed (R)-beta-lysine
  forming term (NTR).
- GO:0051536 MODIFY to GO:0051539; GO:0051539 (IBA, IDA) ACCEPT.
- NEW: GO:1904047 SAM binding (IC: radical mechanism shown) and GO:0030170
  pyridoxal phosphate binding (UniProt cofactor, ECO:0000269 PubMed:17042480).
- The cached Behshad paper is abstract-only, so cofactor quotes come from the
  curated UniProt COFACTOR lines.
