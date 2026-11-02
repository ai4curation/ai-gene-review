# CG8353 (Q9VLR2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted. Sources: UniProt Q9VLR2, the falcon deep-research report, PANTHER 19.0 classification,
the PTHR11644 PAINT file and family review, the human CDA review, PMID:30476102 (cached full text), and a new
pairwise analysis in `CG8353-bioinformatics/RESULTS.md`.

### Identity

- Q9VLR2 is the complete canonical product of CG8353 (FBgn0032002). Both RefSeq proteins (NP_609196.1,
  NP_001260233.1) are 170 aa and identical to Q9VLR2; it is not a fragment, isoform or alternative gene model.
- UniProt entry is unreviewed (PE 3); all functional text there (FUNCTION, CATALYTIC ACTIVITY) is ARBA/RuleBase
  and is not used as support.

### Evolutionary placement

- PANTHER PTHR11644:SF2 (CYTIDINE DEAMINASE), together with human CDA P32320, mouse Cda P56389, yeast CDD1 Q06549,
  E. coli cdd P0ABF6, and two adjacent fly paralogs CG8360 (Q9VLR3) and CG8349 (Q7KTJ2).
- PAINT node PTN000182087 propagates cytidine deaminase activity (GO:0004126), cytosol (GO:0005829), deoxycytidine
  catabolic process (GO:0006217) and uridine biosynthetic process (GO:0046109). Human CDA's
  pyrimidine-containing compound salvage (GO:0008655) term was not propagated; treated as a deliberate PAINT decision,
  so no NEW salvage term is proposed.
- Family review `interpro/panther/PTHR11644/PTHR11644-review.yaml` (HETEROGENEOUS family; SF2 contains a
  blasticidin-S deaminase) scopes GO:0004126 to SF2 and lists CG8353 as representative. No disagreement with the
  subfamily placement.

### Catalytic residues (RESULTS.md)

- Aligned to human CDA: Zn ligands C78/C112/C115 and proton donor E80 retained (human C65/C99/C102, E67); 45% identity
  over 141 columns. Cys3 zinc set of the small-chain tetrameric CDA class (TIGR01354), not the His-Cys-Cys set of
  dimeric E. coli cdd.
- The three fly paralogs are 49-54% identical to each other: lineage-specific triplication of a CDA ortholog.

### Literature

- No biochemical, localisation or mutant study of CG8353 itself.
- PMID:30476102 (Kong et al. 2019, FXTAS fly model): eye-specific RNAi of CG8353 enhanced r(CGG)90 rough-eye toxicity;
  CG8353 was chosen as the fly ortholog of mouse Cda. This is a genetic-modifier phenotype in a disease model; not
  annotated as process participation.
- Deep research also cites a bioRxiv preprint (Crane et al., doi:10.1101/2024.05.17.594696) listing CG8353 as one of
  three predicted fly cytosine deaminases in a C-to-U editing discussion; no editing activity was tested. Not used.

### Decisions

- GO:0004126 (IBA, IEA): ACCEPT, core.
- GO:0005829 cytosol (IBA): ACCEPT; GO:0005737 cytoplasm (ARBA): TOO_GENERAL beside cytosol.
- GO:0006217 deoxycytidine catabolic process, GO:0046109 uridine biosynthetic process (IBA): ACCEPT; these are the
  two products of the deamination reaction on 2'-deoxycytidine and cytidine.
- GO:0008270 zinc ion binding: KEEP_AS_NON_CORE (catalytic cofactor).
- GO:0016787 hydrolase activity; GO:0055086, GO:0072527, GO:1901135 broad metabolic parents (ancestry verified via
  OLS4 hierarchicalAncestors of GO:0006217 and GO:0046109): TOO_GENERAL.
- GO:0042802 identical protein binding (ARBA): changed from UNDECIDED to KEEP_AS_NON_CORE. The tetrameric CDA
  architecture (TIGR01354) and the curated homotetramer of human CDA (PMID:15689149) support self-association,
  but it is not measured for CG8353.

### Relative to review next

- Human CDA (P32320), same PANTHER subfamily SF2 and PAINT node; reviewed at `genes/human/CDA/CDA-ai-review.yaml`
  (all 40 annotations have actions, core functions present).
