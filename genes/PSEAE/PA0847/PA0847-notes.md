# PA0847 (Q9I594) review notes

No deep-research provider was available. Literature checked by hand on 2026-11-05: cached
publications, the PMC web page for PMID:16477007, and Europe PMC search "PA0847 AND aeruginosa"
(hits include PMID:31114257, PMID:32012489, PMID:35935233; the last is a mutant-library
survey not cached here).

## Domain architecture

UniProt (unreviewed) gives two TM helices (91-110, 369-392) and four domains; the 2019
paper describes a periplasmic CHASE domain between two TM helices, then HAMP, PAS and a
C-terminal GGDEF [PMID:31114257 "Domain analysis of PA0847 shows a unique molecular
architecture with an N-terminal periplasmic sensory domain"].

## Function

- Purified PAS-GGDEF makes c-di-GMP; GGDEF alone is nearly inactive [PMID:31114257 "Although
  isolated GGDEF domain showed only residual DGC activity (data not shown), PAS-GGDEF duel
  domain efficiently catalyzed the formation of c-di-GMP in vitro."]. Mg2+-dependent; no
  product inhibition despite conserved I-site residues (abstract).
- Deletion increases swimming and swarming [PMID:31114257 "Compared with wild type strain,
  PA0847 mutant bacteria displayed significantly increased swimming and swarming motilities
  (Figure 1A and B)."].
- A deletion lowers cellular c-di-GMP [PMID:32012489 "Among DGC mutants, ∆PA0169, ∆PA0847,
  ∆PA1120 (yfiN), ∆PA3702 (wspR), and ∆PA4332 produced significantly less c‐di‐GMP compared to
  wild type."].

## Verbatim excerpts from PMID:16477007 full text (PMC1413825, PMC web page, read 2026-11-05)

- PA0847 GGDEF +(16)
- DGC activity is measured as pmol of c-diGMP produced per mg wet cell weight.
- Given the limits of sensitivity of the HPLC assay (12 pmol/mg cell wet weight), we cannot conclude that any particular DGC or PDE domain does not have the corresponding enzymatic activity in vivo .
- Specifically, P. aeruginosa PA14 overexpressing PA0338, PA0847, PA1107, PA1120, PA3702, PA4332, and PA5487 formed pronounced pellicles

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; other seeds' experimental rows from QuickGO, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN005315326 | GO:0052621 diguanylate cyclase activity | 5 | 35 (16 taxa) | GO:0052621, IDA, PMID:16477007 (PseudoCAP) | SOUND | Overexpressing cells held 16 pmol c-di-GMP/mg (Table 1, full text read), just above the 12 pmol/mg limit: weak but positive and direct. Later confirmed with purified PAS-GGDEF (PMID:31114257). | tpbB Q9I4L5 (EXP PMID:20300602, PMID:24278422); VCA0965 Q9KKY5 (IDA PMID:24490592); E. coli DgcT P75908 (IMP, EcoCyc); Dictyostelium DgcA DDB_G0283453 | Yes |

Worklist says pseudocap_only_support: true for this seed; the 2019 in vitro assay now gives
independent support. Same node as tpbB (see tpbB-notes.md); both seeds SOUND, no node-level
defect, so nothing to cross-reference.

Other rows:
- GO:0006355 regulation of DNA-templated transcription IEA (InterPro IPR013767 PAS fold):
  REMOVE. PA0847 has no DNA-binding domain; the PAS domain here regulates the DGC
  (PMID:31114257). This is the generic PAS2GO over-mapping, not a PseudoCAP row.
