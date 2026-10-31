# Klf4 (rat) review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene rat Klf4`; UniProt Q923V7 (unreviewed TrEMBL, 482 aa),
  151 GOA rows (75 ISO from RGD, 52 IEA, 24 experimental/ISS).
- No deep-research API keys; manual literature work is in `Klf4-deep-research-manual.md`.
- Rat experimental literature is almost entirely vascular smooth muscle (Wen JK group,
  Hebei; Wassmann/Nickenig, Bonn), kidney (B2R promoter), mesangial cells (LAMC1) and
  cardiac myocytes (expression only).

### Key decisions

- Core MF: sequence-specific Pol II cis-regulatory DNA binding (GO:0000978) and
  DNA-binding TF activity, both activator (GO:0001228) and repressor (GO:0001227).
  General DNA-binding / TF rows are MODIFY to these terms.
- `GO:0035014 phosphatidylinositol 3-kinase regulator activity` (IMP, PMID:19531492):
  REMOVE. The paper's own abstract attributes the PI3K effect to transcriptional
  repression of RARalpha and PDGFRbeta [PMID:19531492 "Klf4 inhibits RAR alpha and PDGFR
  beta expression while blocking PI3K and ERK signaling"], so KLF4 has no regulator
  activity on PI3K itself; the BP row (negative regulation of PI3K/PKB signalling) is kept
  as non-core. Flagged for expert check (full text not cached).
- `GO:0060070 canonical Wnt signaling pathway`: MODIFY to negative regulation
  (GO:0090090); KLF4 is a beta-catenin antagonist, not a pathway participant.
- `GO:0006351 DNA-templated transcription`, `gene expression`: TF regulates rather than
  executes transcription; MODIFY/over-annotated.
- IEP rows (H2O2, endothelin, retinoic acid) are expression responses: KEEP_AS_NON_CORE.
- No NEW terms proposed: all candidate processes are either already present or rest only
  on phenotype/expression evidence.
- Unverifiable ISO rows (lncRNA binding, hemoglobin biosynthesis) left UNDECIDED.

## 2026-10-28: propagation_review metadata

- Added structured `propagation_review` to the 24 ISO rows with MODIFY, MARK_AS_OVER_ANNOTATED
  or UNDECIDED, derived only from each row's existing reason text (no new analysis). Sources are
  mouse Klf4 (MGI:MGI:1342287) or human KLF4 (UniProtKB:O43474) per With/From; the source
  annotations themselves were not inspected, and each comment says so.
- "Correct but general" MODIFY rows: TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH. DNA-templated
  transcription and canonical Wnt signaling: TERM_SCOPING_PROBLEM / ROLE_CONFLATION. Gene
  expression (phenotype-based source): SOURCE_WEAK_OR_INFERRED. lncRNA binding and hemoglobin
  biosynthesis (UNDECIDED): UNRESOLVED.
- Validation now clean of propagation warnings; status set to COMPLETE per update-status.
