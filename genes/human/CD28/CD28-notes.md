# CD28 curation notes

## 2026-09-04 (PAINT no-IBA project finishing pass)

Reviewed the full `CD28-ai-review.yaml` draft (all actions were pre-assigned). CD28
is the prototypic T-cell costimulatory receptor; the annotation set is large but
internally consistent and well-supported.

Findings and decisions confirmed:
- Core MF is `coreceptor activity` (GO:0015026); the numerous IPI `protein binding`
  (GO:0005515) rows are correctly marked MODIFY, split between `coreceptor activity`
  for the CD80/CD86 ligand interactions and `protein kinase binding` (GO:0019901) for
  the cytoplasmic signaling recruits (PI3K p85/PIK3R1, GRB2, Lck, ITK via the
  YMNM/PRRP/PYAP motifs) [PMID:7568038 "p56Lck and p59Fyn regulate CD28 binding to
  phosphatidylinositol 3-kinase, growth factor receptor-bound protein GRB-2, and T
  cell-specific protein-tyrosine kinase ITK"].
- `positive regulation of mitotic nuclear division` (GO:0045840, IDA, PMID:3159820)
  is correctly MARK_AS_OVER_ANNOTATED — CD28 is a signaling receptor, not a direct
  regulator of mitotic machinery; the proliferative effect is downstream of
  transcriptional/metabolic reprogramming.
- Isoform-3 (CD28i)-specific CD40LG interaction (PMID:15067037) and the viral-context
  entries (PMID:15554700 Lck/Tip; PMID:11285224 Nef) kept as UNDECIDED — reasonable
  given they are isoform- or context-specific and full text was not readable.
- Cytokine/gene-expression/survival outputs (IL-2/IL-4/IL-10, GO:0010628/0010629,
  GO:0043066) kept as KEEP_AS_NON_CORE (downstream of costimulation, not the core MF).

No changes were required to the CD28 review content: it validates clean with zero
warnings and no PENDING actions. Status advanced IN_PROGRESS -> COMPLETE.

Action tally: 54 ACCEPT, 15 MODIFY, 11 KEEP_AS_NON_CORE, 3 UNDECIDED,
1 MARK_AS_OVER_ANNOTATED.
