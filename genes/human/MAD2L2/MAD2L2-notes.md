# MAD2L2 (REV7 / MAD2B / FANCV) — curation notes

## 2026-07-22 — QA re-review of MAD2L2-ai-review.yaml

Performed a conservative quality-assurance pass on the existing, complete review
(79 existing_annotations, 3 core_functions). **No substantive changes were made** —
the review was found to be biologically and curatorially sound.

### Validation
- `uv run ai-gene-review validate --verbose --terms genes/human/MAD2L2/MAD2L2-ai-review.yaml` → ✓ Valid.
- Reference validator (`scripts/run_reference_validator.sh`) → all validations passed.
- Manually confirmed several `supporting_text` quotes are verbatim substrings of the
  cached publications (whitespace-normalized), including PMID:11459825, PMID:11485998,
  PMID:17541814, PMID:20164194, PMID:11459826, PMID:17296730.

### Checks performed (all clean)
- **Action consistency:** no GO term carries more than one distinct action across
  evidence types (programmatic check). Action distribution: 42 ACCEPT / 15
  KEEP_AS_NON_CORE / 22 MARK_AS_OVER_ANNOTATED; no PENDING/UNDECIDED.
- **`protein binding` (GO:0005515):** all 22 instances are `MARK_AS_OVER_ANNOTATED`
  (none ACCEPT), consistent with the "avoid protein binding" guideline. The specific
  functional interactions (REV3L/REV1 adapter role, shieldin, APC/CDH1) are captured by
  dedicated MF/BP/CC annotations and by `core_functions`, so downgrading the generic
  term rather than MODIFY-ing each is a defensible, non-duplicative choice.
- **Dual biology captured correctly in `core_functions`:**
  (1) Pol zeta accessory subunit / translesion synthesis — MF GO:0030674 adaptor
  activity, involved_in TLS (GO:0019985), in_complex GO:0016035 (zeta DNA pol complex);
  (2) shieldin (SHLD1/2/3–REV7) downstream of 53BP1–RIF1 — involved_in +NHEJ
  (GO:2001034) / −HR (GO:2000042), located at GO:0035861 (site of DSB);
  (3) APC/C inhibition via CDH1/CDC20 — involved_in −ubiquitin ligase activity
  (GO:1904667) / cell division (GO:0051301), in_complex GO:0005680 (APC/C).
  All MF/BP/CC branch placements are correct (confirmed by `--terms` validation).
- **Core vs non-core:** TLS, shieldin/NHEJ, and APC/C roles are core; transcription
  (TCF4/Wnt/ELK1-JNK), EMT, actin, cell-growth, and telomere/immune roles are
  appropriately `KEEP_AS_NON_CORE` or accepted as secondary.
- **`description` field:** clean standalone biology, no project/curation framing.

### Non-blocking observations (deliberately left unchanged)
- **GO:0005634 nucleus (IBA):** one of two `supported_by` quotes (PMID:11717438
  "…MAD2B interacts with PRCC") speaks to a protein interaction rather than to nuclear
  localization; the second quote (PMID:17541814 nuclear colocalization) does support the
  term, so the annotation remains validly supported. Not changed (retains valid support;
  editing would be churn).
- **GO:0005737 cytoplasm (IEA):** the `supporting_text` (PMID:17719540 IpaB → cell-cycle
  arrest) does not directly evidence cytoplasmic localization, and no better quote is
  available in the cache. Left as-is (ACCEPT, IEA); flagged here rather than removing the
  only supporting quote.
- **GO:0007094 mitotic spindle assembly checkpoint signaling (TAS):** reviewer reason
  argues REV7 does not act in the SAC like MAD2 (name-based homology only). The chosen
  `MARK_AS_OVER_ANNOTATED` is the conservative call; a case could be made for stronger
  action but REMOVE is not warranted for a TAS annotation without fuller evidence.
- Several `protein binding` interactions of clear functional import (REV3L/REV1:
  PMID:20164194, PMID:22828282, PMID:23143872, PMID:11485998) could alternatively be
  `MODIFY` → GO:0030674; left as `MARK_AS_OVER_ANNOTATED` to avoid duplicating the
  existing dedicated adaptor-activity annotation.

**Conclusion:** review passes QA; no edits required.

## 2026-07-24 — Affinage reconciliation (conservative additions)

Reconciled the Affinage deep-research record (run 2026-06-10, 47 PMIDs, self-eval win)
against the QA'd review. Most Affinage PMIDs were already cited/adjudicated. Two genuine
gaps were filled conservatively; no existing decision was weakened.

- **PMID:27500492** (Bluteau et al. 2016, J Clin Invest; abstract-only) — canonical FANCV /
  Fanconi anemia paper. The `description` asserted the FANCV identity but had **no citation**
  anywhere in the review. Added to `references` (reference_review HIGH / VERIFIED) and attached
  as a verbatim `supported_by` on the existing GO:0006281 DNA repair (IBA) annotation.
- **PMID:36075897** (Paniagua et al. 2022, Nat Commun; full text) — MAD2L2 protects/restarts
  stalled replication forks by limiting MRE11-dependent resection, **shieldin-independently** and
  **REV3L/REV1-dependently**. A well-evidenced function absent from GOA and the review. Added to
  `references` (HIGH / VERIFIED) and captured as **one NEW annotation**: GO:0110027 "negative
  regulation of DNA strand resection involved in replication fork processing" (evidence IMP),
  verified via OLS as a real, non-obsolete biological_process term, correctly branched. Two verbatim
  `supported_by` quotes attached.

Validation after edits: `uv run ai-gene-review validate genes/human/MAD2L2/MAD2L2-ai-review.yaml`
→ ✓ Valid. Evaluation write-up: `projects/AFFINAGE_EVALUATION/results/fa-cohort/MAD2L2.md`.

Deliberately NOT imported (conservative): Affinage's coarse `mechanism_profile` GO layer
(including an unsupported GO:0003677 DNA binding), and mouse-PGC / regulation-of-MAD2L2 /
single-group recent human findings (e.g. TRIP13-p31comet disassembly, CHAMP1 competition,
p53 signaling) — real but peripheral to the human core functions.
