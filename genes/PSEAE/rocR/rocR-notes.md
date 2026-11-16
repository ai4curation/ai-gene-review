# rocR (PA3947, Q9HX69) review notes

## Summary of the literature

RocR is a 392-aa response regulator with an N-terminal receiver (REC) domain
(phosphorylatable Asp56) and a C-terminal EAL domain. It is part of the
RocS1-RocR-RocA1 (SadARS) system.

- Purified RocR hydrolyses c-di-GMP by a Mg2+-assisted general-base mechanism
  [PMID:18344366 "RocR, an EAL domain protein that regulates the expression of
  virulence genes and biofilm formation in Pseudomonas aeruginosa PAO-1, catalyzes
  the hydrolysis of cyclic di-GMP by using a general base-catalyzed mechanism with
  the assistance of Mg(2+) ion"]. UniProt records Km 3.2 uM and kcat 0.67/s, and
  no activity on cAMP or cGMP.
- Loop 6 of the EAL domain and the D56 phosphorylation site modulate activity
  [PMID:19376848 "the catalytic activity of RocR was affected by mutating the
  putative phosphorylation site (D56N) in the phosphoreceiver domain"].
- The crystal structure (R286W mutant) is an unusual tetramer, and RocR is
  tetrameric in solution [PMID:22753070 "a finding consistent with the observation
  that RocR forms tetramers in solution"]. RocR has no predicted transmembrane
  segment in UniProt; it is a soluble cytoplasmic response regulator.
- Genetics: RocR antagonises RocA1, the DNA-binding activator of cupB/cupC
  [PMID:15659157 "RocA1 is a DNA binding response regulator that activates cup
  genes, and RocR is an antagonist of RocA1 activity"]. The SadARS system is needed
  for late biofilm maturation and type III secretion gene expression
  [PMID:15687209].
- Kulesekara et al. 2006 (PMID:16477007). I read the full text on the PMC web page
  (PMC1413825); the cached copy is abstract-only. The PDE assay was a lysate assay:
  "The ability of the PDE-containing proteins to hydrolyze c-di-GMP was tested by
  adding synthetic c-di-GMP to lysates of strains overexpressing these proteins and
  measuring the disappearance of the dinucleotide from the reaction mixture". In
  Table 1 PDE activity is "measured as percent of the added synthetic c-diGMP
  degraded". The rows for genes in this batch and its neighbours read: "PA2133 ETL
  — +(71) PA2200 EAL +(61)", "PA3311 AGDEF EAL — —", "PA2818 EAL —", "PA3825 EVL
  +(27) PA3947 EVL +(100)", and "PA4367 GGDQF EAL — —". A rocR insertion abolished
  TTSS cytotoxicity and virulence in mice.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002105365 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 18 | 162 (24 taxa) | GO:0071111, IDA, PMID:16477007 (PseudoCAP); also EXP PMID:18344366, PMID:19376848 (UniProt) | SOUND | Lysate of a RocR-overexpressing strain degraded 100% of added c-di-GMP (full text read). Purified-enzyme kinetics (UniProt EXP rows) confirm the activity directly. | E. coli PdeA, PdeB, PdeC, PdeF, PdeH, PdeI, PdeK, PdeL, PdeN, DosP; M. tuberculosis P9WM13; P. aeruginosa bifA, PA2133, PA2200, nbdA, PA2567, PA3825 | Yes. Many seeds have purified-enzyme evidence (e.g. PdeH, PdeL, PdeF, RocR's own EXP rows). |

### Node-level GO_CENTRAL defects for PTN002105365 (recorded here, once)

RocR has the most direct biochemical evidence among the P. aeruginosa seeds, so the
node-level defects for the shared node PTN002105365 are recorded in this review and
cross-referenced from bifA, PA2133, PA2200 and nbdA.

1. **GO:0071111 reaches degenerate EAL proteins.** The leaf GAF
   (`.cache/paint/leaf.gaf.gz`, queried 2026-11-05) shows IBA GO:0071111 from this
   node on E. coli CsrD (P13518), YdiV (P76204), Salmonella YdiV (Q8ZPS6) and BluF
   (P75990), with no NOT annotation. CsrD is experimentally not a c-di-GMP PDE
   [PMID:16980588 "These results suggested that the EAL domain of CsrD activity does
   not hydrolyze c-di-GMP."]. UniProt describes YdiV as an anti-FlhD4C2 factor and
   BluF as a blue-light BluR antirepressor. The node term is right for the clade as a
   whole, and the IBD does not depend on any one P. aeruginosa seed; what is missing
   is NOT/loss annotations on the degenerate branches. Confidence PROBABLE.
2. **GO:0005886 plasma membrane (is_active_in) on the same node.** The PM IBD is
   seeded by membrane-anchored E. coli proteins, but the clade includes soluble EAL
   proteins: RocR (REC-EAL, tetramer in solution, no TM) and PA2133 (285 aa, a lone
   EAL domain, no TM). The PM term does not suit the whole clade. Confidence
   PROBABLE.

## Annotation decisions

- GO:0071111 rows (IBA, IEA, EXP x2, IDA): ACCEPT; core function.
- GO:0005886 IBA: MARK_AS_OVER_ANNOTATED; RocR is soluble.
- GO:0000160 phosphorelay signal transduction system (IEA, REC domain): ACCEPT; RocR
  is the receiver of the RocS1 phosphorelay.
- GO:0045892 negative regulation of DNA-templated transcription (IMP,
  PMID:15659157): KEEP_AS_NON_CORE. RocR is not a DNA-binding protein; it acts by
  antagonising RocA1, the transcription factor. The full text was not read.
