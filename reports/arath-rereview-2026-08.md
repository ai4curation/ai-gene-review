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
  REMOVE → ACCEPT. The "RPS5-focused" paper did assay RPS2 domains in RPS5
  chimeras (the abstract describes swaps of the RPS2 CC and LRR domains), so it is
  not a citation mismatch, and both functions are unambiguously correct for RPS2.
- **RPS2** `GO:0002220` (EXP): REMOVE → MODIFY with proposed replacement
  `GO:0002218` activation of innate immune response. The immune-activation claim
  is sound, but RPS2 is a guard rather than a ligand/PAMP-binding pattern
  recognition receptor, so the replacement is a receptor-class-neutral term rather
  than a different receptor class. This matches the `GO:0016045` row, which rejects
  PRR framing for RPS2 on the same grounds.
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

## IBA family sweep (follow-up pass)

A second pass examined every IBA row flagged `missing_propagation_review` (25 rows
across 19 reviews) against the cached PANTHER PAINT slices
(`interpro/panther/<FAM>/<FAM>-paint.tsv`), inspecting the IBD node placement,
its seeds, and any IRD/IKR prunings before writing structured
`propagation_review` blocks (root cause, failure modes, per-source status).
Findings worth noting:

- **Withdrawn IBDs (SOURCE_STALE_OR_MISSING).** The `GO:0051082` (unfolded
  protein binding) IBDs behind the HSP17.6A, HSP17.7 (PTN000163021 in PTHR11527)
  and HSP90.1/AT5G52640 (PTN000163527 in PTHR11528) IBA rows no longer appear
  anywhere in the current PAINT slices for those families - the upstream IBDs
  appear to have been withdrawn, independently corroborating the reviews' MODIFY
  verdicts.
- **Missing plant-clade IRDs.** For CRY2 (`GO:0003904` photolyase activity,
  PTHR11455) PAINT already carries an IRD pruning the term for the metazoan
  cryptochrome clade (PTN000894457), and for DRB1 (`GO:0004525` RNase III
  activity, PTHR11207) IRDs exist for two other subclades - but in both families
  the plant clade lacks an equivalent IRD, which is exactly why the terms still
  reach CRY2 and DRB1. An IRD for the plant clades would fix these at source.
- **Single-divergent-seed IBDs.** The `GO:0048564` (photosystem I assembly) IBD
  on the PsbP family node (PTN001584458, PTHR31407) is seeded solely by AT4G15510
  (PPD1), a divergent PsbP-domain protein that genuinely is a PSI assembly
  factor; propagating it across the node to true PSII OEC PsbP subunits is a
  wrong-paralog transfer. Similarly, `GO:0038023` (signaling receptor activity)
  reaches RIC7 (an intracellular ROP effector) from a node seeded solely by
  CLV2, and `GO:0031380` (nuclear RdRP complex) reaches cytoplasmic RDR6 from a
  node seeded solely by fission-yeast rdp1.
- **Taxon leakage.** The `GO:0034587` (piRNA processing) IBD (PTN000483941,
  PTHR21404) is seeded exclusively by metazoan HENMT1 orthologs but placed at a
  Eukaryota-wide node, so a metazoan-only pathway term reaches plant HEN1.
- **AAU94417 cleanup.** Two REMOVE rows had empty reasons; both were filled. The
  `GO:0009535` (thylakoid membrane) REMOVE was softened to MODIFY (replacement
  `GO:0009543` thylakoid lumen), since the IBD seed (PPL1) is itself lumenal and
  extrinsic membrane association is real. Note that `genes/ARATH/AAU94417/` and
  `genes/ARATH/AT1G06680/` are duplicate reviews of the same protein
  (UniProt Q42029 / PSBP1) and could be merged.
- **AAU94417 / AT1G06680 verdict split (resolved).** The two duplicate reviews had
  opposite verdicts on the same `GO:0009535` IBA / GO_REF:0000033 row: AAU94417
  MODIFY → `GO:0009543` with a grounded `propagation_review`, AT1G06680 ACCEPT with
  a boilerplate reason. AT1G06680 was aligned to the AAU94417 verdict. The ACCEPT
  also contradicted AT1G06680's own `core_functions`, which already assert
  `GO:0009543` (chloroplast thylakoid lumen) as the location. The two experimental
  `GO:0009535` HDA rows (PMID:15322131, PMID:14729914) were split the same way
  (AAU94417 REMOVE vs AT1G06680 ACCEPT) and were converged on MODIFY →
  `GO:0009543` in both files: the proteomic detection is real, so per the
  "do not overrule curators from incomplete evidence" guideline the imprecise
  compartment term is refined rather than removed. Merging the two
  directories remains outstanding and is deliberately left out of scope here;
  `inconsistent_review_actions` cannot see across directories, so this split would
  not have been caught by validation.

## Known remaining warnings (deliberately not addressed)

- `core_function_*_not_in_annotations` and `missing_aliases`/`no_deep_research_results`
  informational warnings: pre-existing and benign.
- A handful of `inconsistent_review_actions` warnings reflect legitimate
  per-reference judgments (e.g. EIN2 cytoplasm rows) and are intentional.
