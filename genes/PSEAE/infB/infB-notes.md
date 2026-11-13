# infB (PA4744, Q9HV55) review notes

Translation initiation factor IF-2, a TRAFAC translational GTPase (HAMAP MF_00100).

## Literature (no deep-research provider available; own reading)

- Steiner-Mosonyi et al. 2004 (abstract only; no PMC full text): P. aeruginosa
  can initiate translation with both fMet-tRNAfMet and unformylated Met-tRNAfMet,
  and its IF2 is required for the formylation-independent route [PMID:15385567
  "Here we show that the Pseudomonas aeruginosa initiation factor IF-2 is
  required for formylation-independent protein initiation in P. aeruginosa"].
  E. coli IF2 could not substitute; changing the charge of the aminoacyl-binding
  cleft swapped the behaviour [PMID:15385567 "the E. coli IF-2 was made to
  function in formylation-independent protein initiation in P. aeruginosa by
  decreasing the positive charge potential of the cleft that binds the amino end
  of the amino acid attached to the tRNA"]. This is genetic and
  structure-function evidence that PA IF2 acts directly in initiation, and
  supports GO:0006413 (and, by the cleft mutagenesis, initiator tRNA
  discrimination as part of the factor's own activity).
- UniProt (HAMAP-Rule MF_00100): IF2 protects fMet-tRNA, promotes its binding to
  the 30S subunit, and hydrolyses GTP during 70S complex formation.
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Seed support queried live in QuickGO on 2026-11-05 (MOD ids mapped to UniProt).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001897651 | GO:0006413 translational initiation | 7 | 326 (141 taxa) | GO:0006413, IMP, PMID:15385567 (PseudoCAP) | SOUND | The abstract positively states that PA IF2 is required for (formylation-independent) initiation and maps the effect to the factor's tRNA-binding cleft; the process term is the factor's own process. | E. coli IF2 P0A705 (IDA PMID:4943554), yeast FUN12/eIF5B P39730 (IDA/IMP, GO:0001732), Candida FUN12 Q5A782 (IGI), S. pombe mti2 O59683 (EXP/IMP, GO:0070124), human MTIF2 P46199 (IDA GO:0001731), bovine MTIF2 P46198 (IDA GO:0070124) | Yes; several IDA/EXP seeds in bacteria, mitochondria and eukaryotic eIF5B |

The node spans bacterial IF2, mitochondrial IF2 and eukaryotic eIF5B; the generic
GO:0006413 suits a clade of that breadth. No PSEUDOCAP or GO_CENTRAL defect.

Cytoplasm IBA at the same node: many seeds are mitochondrial (still part_of
cytoplasm), so the node term is fine; for PA4744 the specific cytosol IBA
(PTN000562019, from E. coli IF2) is accepted, and the cytoplasm rows are
TOO_GENERAL (cytosol part_of cytoplasm).
