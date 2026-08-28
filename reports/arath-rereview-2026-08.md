# Arabidopsis (ARATH) Rereview — August 2026

Systematic rereview of the 129 completed Arabidopsis thaliana gene reviews under
`genes/ARATH/`. The pass combined a fresh full-organism validation run
(`reports/validation-ARATH.tsv`) with pattern scans for the failure modes called out
in the project guidelines: curation commentary in `description` fields, REMOVE
actions that overrule experimental annotations from abstract-only caches,
`CIRCULAR_OR_REDUNDANT` misuse on IBA self-donors, and protein-binding terms used
as core functions.

## Scan results (no action needed)

- No `CIRCULAR_OR_REDUNDANT` misuse found.
- No `GO:0005515` (protein binding) used as a core-function molecular function.
- No validation errors anywhere; all findings were warning-level.
- The large family of REMOVE-on-`GO:0005515` rows follows the project convention of
  deprecating uninformative protein-binding annotations and was left as-is.
- REMOVE actions grounded in explicit contradicting evidence were verified and kept,
  e.g. RGA/SCR direct DNA-binding removals (structural evidence that DELLA/SHR-SCR
  lack DNA-binding surfaces), PAL1 catabolic-process terms (directionally wrong),
  NPR1/ICS1 rows citing PMID:16732289 (the paper explicitly states mlo resistance is
  SA/JA/ET-independent), and EDS1 chloroplast (the cached full text of PMID:33751092
  attributes chloroplast localization to EIJ1, not EDS1).

## Substantive corrections

### Reviews that overruled curators from incomplete evidence (fixed)

Per the "Do not overrule curators from incomplete evidence" guideline, experimental
annotations for clearly correct functions must not be removed because an
abstract-only cache foregrounds a different gene or paralog:

- **AGO1** `GO:0035198` miRNA binding (IPI PMID:35137215, IDA PMID:16998468):
  REMOVE → ACCEPT. Both caches are abstract-only; miRNA binding is a textbook core
  AGO1 function independently supported by PMID:16081530 and PMID:30181559.
- **RPS2** `GO:0042742` (IMP) and `GO:0005886` (EXP), both PMID:22331412:
  REMOVE → ACCEPT. The "RPS5-focused" paper in fact assayed RPS2 domains directly
  (RPS2 CC and LRR chimeras are described in its abstract), so it is not a citation
  mismatch, and both functions are unambiguously correct for RPS2.
- **RPS2** `GO:0002220` (EXP): REMOVE → MODIFY with proposed replacement
  `GO:0002753` cytoplasmic pattern recognition receptor signaling pathway. The
  immune-activation claim is sound; only the receptor class (cell surface vs.
  cytoplasmic) is wrong.
- **COP1** `GO:0006281` DNA repair (IMP PMID:18434413): REMOVE →
  MARK_AS_OVER_ANNOTATED. The abstract explicitly reports DNA damage in cop1
  mutants, so the IMP is not a CSN mis-attribution; but the phenotype is plausibly
  an indirect CRL-pathway consequence, hence over-annotation rather than removal.
- **DCL1** `GO:0003677` DNA binding (EXP/IDA PMID:26101256, plus the IEA row):
  REMOVE → KEEP_AS_NON_CORE. The cached full text directly measures dsDNA binding by
  the DCL1 dsRBDs ("We found that both constructs do bind dsDNA", Kd ≈ 600–860 nM),
  contradicting the removal reason; the activity is real but peripheral.
- **PHYA** `GO:0009630` gravitropism (IMP PMID:15695459): REMOVE →
  KEEP_AS_NON_CORE. The paper directly assayed phyA-containing mutants for root
  gravitropism; the phyAB double-mutant defect supports a redundant, non-core PHYA
  contribution.
- **PIN1** `GO:0005886` plasma membrane (IDA ×3, PMIDs 18337510/19825598/18539115):
  UNDECIDED → ACCEPT, deferring to curators for a textbook-correct localization
  attested by accepted sibling rows.
- **RDR6** `GO:0030422` and `GO:0070549` (IMP PMID:32376953): UNDECIDED → ACCEPT.
  The 22-nt siRNAs the paper characterizes derive from RDR6-synthesized dsRNA; an
  abstract foregrounding DCL2 is not grounds to withhold acceptance.
- **AGO1** `GO:0005634`/`GO:0005737` (IDA PMID:17442570): UNDECIDED → ACCEPT
  (textbook nucleocytoplasmic localization, accepted on sibling rows).

### Wrong-identifier rows (explicit mismatches, REMOVE retained/strengthened)

- **GL1** `GO:0010154` fruit development (IMP PMID:3793867): the cached record is
  explicitly a 1986 Campylobacter jejuni toxin paper; reason strengthened to state
  the explicit mismatch.
- **CER1** `GO:0010025` (IMP PMID:1847001): UNDECIDED → REMOVE; the cached record is
  explicitly an asbestos epidemiology paper, and the term remains accepted via the
  properly referenced PMID:8718622 row.
- **STM** `GO:0003723` RNA binding (IDA PMID:17965274): REMOVE retained; reason
  strengthened with the full-text finding that MPB2C, not STM, is the RNA-binding
  protein.

### Description-field cleanup (14 genes)

Removed or rewrote curation/annotation commentary (banned from `description` by the
project guidelines) in: ABI1, AP1, AT1G32330, AT3G02990, AT5G02500, CRY1, EIN3,
GL1, JAZ1, RPS2, SVP, TT8, TTG1, WRKY70. Biological content was preserved;
sentences about what "annotations should be interpreted as" or what is "not
proposed as new GO annotations" were recast as plain statements about the biology
or dropped.

### Validation-driven fixes

- **AT1G06680 (PSBP1)**: added the missing `core_functions` block (extrinsic PSII
  OEC subunit; contributes to oxygen evolving activity; thylakoid-lumen location;
  PSII OEC complex membership).
- **EDS1 / PAD4**: added verbatim, cache-verified `supported_by` quotes to all 32
  ACCEPT rows that lacked them (PMIDs 10557364, 11574472, 11826312, 16040633,
  22072959, 29253890, 33751092); both files now validate with zero warnings.

## Known remaining warnings (deliberately not addressed)

- `missing_propagation_review` on ~25 IBA rows: adding structured
  `propagation_review` metadata requires inspecting the PAINT family trees; per the
  guidelines, asserting phylogenetic claims without that inspection is worse than
  leaving the warning.
- `core_function_*_not_in_annotations` and `missing_aliases`/`no_deep_research_results`
  informational warnings: pre-existing and benign.
