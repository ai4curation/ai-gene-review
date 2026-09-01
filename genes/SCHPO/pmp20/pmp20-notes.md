# pmp20 review notes

## 2026-09-01 — source refresh and annotation review

- Refreshed the UniProt and GOA inputs with `just fetch-gene SCHPO pmp20 --force`.
  Current GOA has 18 rows. Seven stale review rows were removed because their exact
  source/evidence combinations are no longer present; seven newly seeded rows were
  reviewed.
- The decisive target-specific evidence is the recombinant-protein study. It reports
  that “peroxidase activity was not observed for PMP20” and that Pmp20 inhibited
  thermal aggregation of citrate synthase, although more weakly than Tpx
  [PMID:20356456, “However, peroxidase activity was not observed for PMP20
  (peroxisomal membrane protein 20).”; “TPx, PMP20, and GPx inhibited thermal
  aggregation of citrate synthase at 43(o)C, but BCP failed to inhibit the
  aggregation. The chaperone activities of PMP20 and GPx were weaker than that of
  TPx.”]. The cached record is abstract-only, but these statements directly describe
  both assays.
- The existing reproducible analysis independently supports catalytic divergence:
  Pmp20 contains C43 but no candidate resolving cysteine, and the resolving C31 of
  active Prx5 O43099 aligns to Pmp20 V22
  [file:SCHPO/pmp20/pmp20-bioinformatics/RESULTS.md, “Active-control resolving
  positions do **not** map to cysteine in `pmp20`”; “vs `prx5_o43099` resolving C31
  -> `V22`”]. This supports the structured residue claim but is not substituted for
  the direct negative assay.
- PAINT nodes were assessed as ancestral assertions rather than pairwise donor lists.
  PTN001625584 is defensible for cytoplasm and a broad oxidative-stress response, but
  its peroxidase, hydrogen-peroxide-catabolism, and redox-homeostasis transfers fail
  for this target because of the direct negative assay and catalytic-site divergence.
  PTN000046537 peroxisomal and mitochondrial localizations are retained as non-core
  phylogenetic inferences because there is no target-specific contradiction, while
  direct Pmp20 evidence for either organelle was not found.
- The existing OpenScientist focused review was applicable to the catalytic question
  and reached the same evidence-based conclusion: reject thioredoxin-peroxidase
  activity and retain holdase activity
  [file:SCHPO/pmp20/pmp20-hypotheses/function-hypothesis-go-0008379/openscientist.md].
- The core function is limited to GO:0140309, unfolded protein holdase activity. The
  citrate-synthase assay measured prevention of aggregation, not active refolding.
  Cytosol and nucleus are retained as experimentally observed locations; inferred
  peroxisome and mitochondrion are not promoted to core locations.

## 2026-09-01 — PR review follow-up

- Replaced all paraphrased `RESULTS.md` supporting text with exact substrings and
  removed an unused deep-research reference carrying a non-verbatim finding.
- Reclassified the mitochondrial IBA as over-annotated. The supporting mammalian
  PRDX5 protein has a 52-residue N-terminal mitochondrial transit peptide, whereas
  the 156-residue Pmp20 target lacks that extension; its reviewed UniProt record and
  systematic S. pombe localization data instead identify cytoplasmic and nuclear
  pools. This is a compartment-transfer problem, not weak donor biology.
- Clarified that peroxisomal retention is only a non-core family/nomenclature-level
  inference and noted the absence of an obvious canonical C-terminal PTS1 motif.
- Added explicit questions and experiments for endogenous holdase clients and direct
  organelle-localization testing.

## 2026-09-01 — post-merge evidence follow-up

- Accounted explicitly for the fly mitochondrial PAINT donor rather than discussing
  only mammalian PRDX5; the fly localization can support that descendant without
  supplying a targeting mechanism or target-specific evidence for S. pombe Pmp20.
- Added direct file-backed evidence for the P30044 residues 1–52 transit peptide and
  for the reviewed cytoplasmic localization of O14313.
- Replaced the partial homolog-panel quote with the exact contiguous RESULTS.md block
  showing 27 proteins, 23 with resolving-cysteine architecture, and Pmp20 in the
  four-member peroxidatic-only class.
- Clarified the peroxisome/mitochondrion comparison after review: fungal homologs
  independently ground peroxisomal Pmp20 biology, but they too require targeting
  signals. Because S. pombe Pmp20 lacks an obvious canonical PTS1, the peroxisome
  transfer remains unverified and is retained only as non-core rather than accepted.
- Replaced an enzymatic-activity quote attached to the peroxisome annotation with the
  direct CbPmp20 peroxisomal-membrane localization sentence, and accounted for the
  rat mitochondrial donor alongside the human and fly sources.
