# CD8B notes

## 2026-10-03 initial review (ADAPTIVE_IMMUNITY, TCR trunk)

CD8 beta (P10966) is the partner of CD8 alpha in the CD8 alpha-beta coreceptor of conventional
MHC class I-restricted T cells.

Key primary evidence:

- Human CD8B cloned; ~90% of CD8A+ thymocytes and blood lymphocytes carry surface CD8 beta;
  splice variants differ in the tail and one lacks the TM exon
  [PMID:3145195 "About 90% of human CD8 alpha positive thymocytes and peripheral blood lymphocytes express CD8 beta at the cell surface."].
- Needs CD8A for surface expression
  [PMID:3145196 "the human Lyt-3 molecule cannot be expressed alone, but requires the human Lyt-2 homologue for efficient cell surface expression"].
- CD8 beta tail palmitoylation partitions CD8ab into rafts, where LCK associates and is activated (mouse T1.4 hybridomas)
  [PMID:10925291 "We demonstrate that CD8 is palmitoylated at the cytoplasmic tail of CD8beta and that this allows partitioning of CD8alphabeta, but not of CD8alphaalpha, in lipid rafts."].
- CD8 beta tail couples CD8 to TCR/CD3 and raises TCR-pMHC avidity
  [PMID:11714755 "the cytoplasmic portion of CD8beta mediates constitutive association of CD8 with TCR/CD3"];
  Cys179 mutation abolishes raft association
  [PMID:11714755 "Thus, mutation of Cys179 of CD8β impaired CD8 association with rafts as dramatically as deletion of the CD8β tail."].
  The human tail has a membrane-proximal Cys pair (sequence ...IHLCCRRRRARLRFMKQFYK).
- Mouse CD8ab/H-2Dd structure: CD8 beta contributes ~half the interface and sits T cell-membrane proximal
  [PMID:19625641 "The CD8β subunit of CD8αβ contributes almost equally (49%) to the buried surface of the interface."].
- Mouse CD8b-/- and tailless CD8b: lower CD8a-associated LCK activity, impaired CD8 SP development
  [PMID:9647223 "Lack of CD8 beta expression or expression of a cytoplasmic domain-deleted CD8 beta resulted in a severalfold reduction in CD8 alpha-associated Lck kinase activity"].
  Necessity evidence only; no thymocyte-development process term proposed (project rule 3).
- LCK binds the CD8 alpha tail (CxC zinc clasp), not CD8 beta
  [PMID:9830036 "Binding of the protein tyrosine kinase p56(lck) to T-cell co-receptors CD4 and CD8alpha is necessary for T-lymphocyte development and activation."].
  So no LCK-binding MF for CD8B; GO:0042610 CD8 receptor binding sits on LCK.

## Annotation decisions

- protein binding (IPI, PMID:2493728, with CD8A): REMOVE, matching CD8A review.
- GO:0007169 RTK signaling (NAS): MODIFY -> GO:0050852. TCR signaling is not under GO:0007169
  in GO (checked ancestors via OLS); receptor has no kinase activity.
- GO:0042101 T cell receptor complex (NAS): MARK_AS_OVER_ANNOTATED. Definition = TCR heterodimer + CD3.
  Differs from CD8A review (ACCEPT); raised as a suggested question.
- Early endosome membrane (Reactome, Nef pathway): non-core.
- NEW: plasma membrane raft (GO:0044853), ISS from mouse palmitoylation data; CD8A has IDA raft.
- Curation gap (not a knowledge gap): no GO CC for the CD8 alpha-beta heterodimer.

## Deep research integration (falcon)

Report: `CD8B-deep-research-falcon.md` (Edison/falcon, finished 2026-10-03, ~23 min). Used as leads only.

Adopted (each traced to a cached primary paper):
- Human primary-T-cell evidence that CD8 alpha-beta (not alpha-alpha) is needed for optimal HLA class I
  coreceptor function, and that the extracellular domains suffice
  [PMID:23738014 "for optimal antigen-specific HLA class I restricted CD4(+) T-cell reactivity the extracellular domains of the CD8α and ß subunits are sufficient"].
  Added as support for coreceptor activity and core function 1.
- Human CD8B membrane isoforms M-1 to M-4; M-1 naive, M-4 effector memory; M-4 tail internalization motif
  [PMID:23533620 "The M-1 isoform which is the equivalent of murine CD8β, is predominantly expressed in naïve T cells, whereas, the M-4 isoform is predominantly expressed in effector memory T cells."].
  Added to description only (no GO change).
- Mouse CD8 beta CDR2/CDR3 loops required for coreceptor activity
  [PMID:16356863 "mutations in CD8beta CDR2 and CDR3 loops abolish CD8alphabeta coreceptor activity"].
  Added as support for MHC class I protein binding.
- Confirms CxC LCK-binding motif is on CD8 alpha, not CD8 beta (agrees with my reading; cited on the GO:0007169 MODIFY row).

Not adopted:
- Nanobody radiotracer imaging (De Groof 2024), transcriptomics (Akula 2024), CD8ab gamma-delta T cells in T-ALL
  (Sumaria 2024): applications/expression context, no bearing on GO terms.
- Stalk sialylation tuning MHC affinity: from the Srinivasan 2024 review, mostly mouse; not traced to a primary
  human paper, so not used.
- Kd range 10-500 uM: review-level range across CD8 complexes, not a CD8B measurement.

Report errors/caveats:
- Table says the membrane-proximal cysteine of the TM "contributes to disulfide stabilization"; the
  primary literature (Arcaro 2000/2001) assigns the membrane-proximal tail cysteine to palmitoylation, and the
  interchain disulfide is in the stalk region. Not used.
- No other factual errors found; the report correctly flags that the bound structures are mouse and that
  familial CD8 deficiency is a CD8A, not CD8B, defect.
