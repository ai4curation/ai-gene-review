---
title: "Ferroptosis Project"
maturity: MATURE
last_reviewed: 2026-10-04
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [GPX4, SLC7A11, SLC3A2, ACSL4, LPCAT3, AIFM2, DHODH, GCH1, PTS, SPR, NCOA4, TFRC, FTH1, SLC40A1, GCLC, GSS, NFE2L2, KEAP1, ATF4, TP53, FADS1, ELOVL5]
manifest:
  slides:
    - href: FERROPTOSIS/slides/FERROPTOSIS-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/7nSuCeq7xETTYoc6zrZeoG
      title: Project brief
---

# Ferroptosis Project

**Bottom line:** ferroptosis is iron-dependent regulated cell death driven by
peroxidation of polyunsaturated phospholipids, and GO treats it as an evolved
programmed process ([GO:0097707](http://purl.obolibrary.org/obo/GO_0097707)).
The project reviewed all 22 human genes that supply the oxidizable
PUFA-phospholipid substrate, tune the labile iron pool, suppress the execution
step through four parallel defense systems, or reset those defenses
transcriptionally. Those gene-level reviews are now summarized in a
decomposable [ferroptosis module](../modules/ferroptosis.html) with production
GO-CAM associations for AIFM2, GPX4, NFE2L2, and SLC7A11 switch models.

The 22 COMPLETE reviews cover 2,362 seeded GOA annotations plus 10 proposed new
ones as of 2026-10-04. Across those rows, 1,458 annotations were accepted as
core, 297 were kept as non-core, 113 were marked over-annotated, 97 were
modified, 377 were removed, and 20 were left undecided. TP53 alone contributed
872 seeded rows, 344 of which were removed. The core suppressor term
`GO:0110076` negative regulation of ferroptosis is accepted on GPX4, SLC7A11,
AIFM2, FTH1, and NFE2L2 and proposed as a new annotation for DHODH.

## Mechanistic Scope

Ferroptosis is best modelled as one execution process, not as a linear cascade.
PUFA-containing phospholipids and redox-active iron set up the chemistry; GPX4,
CoQ10, DHODH, and BH4 arms quench the radicals or lipid hydroperoxides in
parallel; NFE2L2, KEAP1, ATF4, and TP53 tune the balance by changing
defense-gene expression.

| Layer | Reviewed genes | Ferroptosis role |
|-------|----------------|------------------|
| PUFA-phospholipid substrate supply | ACSL4, LPCAT3, FADS1, ELOVL5 | ACSL4 activates arachidonate/adrenate-family PUFAs, LPCAT3 remodels them into phospholipids, and FADS1 and ELOVL5 feed the upstream PUFA pool |
| Labile-iron pool | TFRC, NCOA4, FTH1, SLC40A1 | TFRC import and NCOA4 ferritinophagy sensitize cells; FTH1 ferritin storage and SLC40A1/ferroportin export are protective |
| GPX4-glutathione defense | GPX4, SLC7A11, SLC3A2, GCLC, GSS | system xc- supplies cysteine for glutathione, and GPX4 reduces membrane phospholipid hydroperoxides |
| CoQ10 defenses | AIFM2, DHODH | AIFM2/FSP1 regenerates radical-trapping ubiquinol at membranes, while DHODH provides the mitochondrial inner-membrane CoQ arm |
| GCH1-BH4 defense | GCH1, PTS, SPR | de novo BH4 synthesis supplies a radical-trapping antioxidant axis parallel to GPX4 and CoQ |
| Transcriptional set point | NFE2L2, KEAP1, ATF4, TP53 | NRF2 and ATF4 induce defenses; KEAP1 represses NRF2; TP53 is context-dependent but canonically represses SLC7A11 |

This seed deliberately scoped out adjacent or newer partners such as `FTL`,
GCLM, `FADS2`, `MBOAT1/2`, and the GPX4 and SLC7A11 abundance-switch regulators
captured in production GO-CAMs.

## Curation Findings

- **Parallel defenses are first-class biology.** AIFM2 and DHODH were key
  test cases because their 2019-2021 discovery split the field from a
  GPX4-only model into multiple independent suppressor arms. The DHODH review
  proposes `GO:0110076` for the mitochondrial CoQ10 arm, and the module now
  places that process directly on the DHODH quinone oxidoreductase annoton.
- **p53 is not a blanket ferroptosis label.** The TP53 review retained
  well-supported SLC7A11 repression and lipid-peroxidation contexts but removed
  hundreds of indirect DNA-damage, apoptosis, and broad regulation rows from the
  ferroptosis-focused interpretation.
- **The curated module is more precise than the old pathway summary.** The
  maintained artifact is `modules/ferroptosis.yaml`: one GO:0097707 execution
  node fed by PUFA-phospholipid and iron drivers, negatively regulated by
  GPX4-glutathione, AIFM2/FSP1-CoQ10, DHODH-CoQ10, and GCH1-BH4, and optionally
  tuned by NFE2L2/NRF2, KEAP1, ATF4, and p53.
- **GO-CAM switch models extend beyond the 22-gene seed.** The module already
  folds in GPX4 chaperone-mediated autophagy and SLC7A11 CRL3/USP18 abundance
  switches from reviewed production GO-CAMs, but `LAMP2`, `EGLN3`, `USP18`, and
  related ligase/adaptor components remain second-batch review scope.

## Key Discoveries

1. **AIFM2/FSP1-CoQ10 pathway** (2019) - GPX4-independent ferroptosis
   suppression by ubiquinol regeneration.
2. **GCH1-BH4 pathway** (2020) - a tetrahydrobiopterin radical-trapping axis
   parallel to GPX4 and CoQ.
3. **DHODH in mitochondria** (2021) - mitochondrial-inner-membrane CoQ10
   regeneration by the pyrimidine-biosynthesis enzyme DHODH.
4. **MBOAT1/2 resistance** (2023) - sex-hormone-linked lipid remodeling that
   should be considered with other second-batch suppressor and switch genes.

## Module

The ferroptosis mechanism is captured as a recursively decomposable module
grounded to UniProt and GO:

- [Ferroptosis module](../modules/ferroptosis.html) - one execution node
  (GO:0097707) fed by PUFA-phospholipid and labile-iron driver arms,
  redundantly suppressed by four independent defense axes, and tuned by a
  transcriptional regulatory layer. Source: [`modules/ferroptosis.yaml`](https://github.com/ai4curation/ai-gene-review/blob/main/modules/ferroptosis.yaml).

## Key References

- Stockwell BR et al. (2017) Cell - foundational review
- Doll S et al. (2019) Nature - FSP1 discovery
- Mao C et al. (2021) Nature - DHODH
- Kraft VAN et al. (2020) ACS Cent Sci - GCH1
- Jiang X et al. (2021) Nat Rev Mol Cell Biol - comprehensive review
- Chen X et al. (2021) Signal Transduct Target Ther - mechanisms update

## Project Status

- [x] Review the initial 22 human ferroptosis genes
- [x] Validate the 22 seeded gene reviews
- [x] Capture the integrated mechanism as `MODULE:ferroptosis`
- [x] Attach production GO-CAM associations for reviewed GPX4, SLC7A11, AIFM2,
  and NFE2L2 ferroptosis models
- [ ] Complete optional switch and adjacent-gene follow-ups
  ([#4084](https://github.com/ai4curation/ai-gene-review/issues/4084))

---

# STATUS

**Initial 22-gene human ferroptosis seed reviewed and valid; optional switch
scope tracked in [#4084](https://github.com/ai4curation/ai-gene-review/issues/4084)
(2026-10-04).**

# NOTES

## 2026-10-04

- Re-audited the 22 human gene reviews: all validate, ACSL4 was promoted from
  `DRAFT` to `COMPLETE`, and the aggregate seeded/`NEW`/action counts still
  match the project summary.
- Refreshed the project page and slide deck to lead with the mechanism and the
  concrete curation results instead of the original priority-order plan.
- Fixed the main module so FADS2 is treated as adjacent follow-up scope, DHODH's
  annoton carries `GO:0110076`, and the USP18 SLC7A11-stabilization role points
  at the current GO-CAM reference-swap problem.
- Opened [#4084](https://github.com/ai4curation/ai-gene-review/issues/4084) for
  the remaining optional switch genes, `MBOAT1/2` and adjacent-gene scope,
  GO-CAM evidence-reference follow-up, and the stale standalone pathway summary.

## 2026-01-19

- Manual second passes completed for GPX4, SLC7A11, ACSL4, and AIFM2/FSP1; each
  review validated after its pass.
- GPX4 HTP/HDA evidence summaries were updated for mitochondrial, nuclear, and
  exosome entries; nuclear matrix and spermatogenesis primary-evidence follow-up
  remains in #4084.
- SLC7A11 deep-research support was added for the core antiporter activity;
  optional 2025-2026 disease/regulation papers remain in #4084.
- ACSL4 had missing HDA supporting text filled and 2025 context papers folded in.
- AIFM2/FSP1 had missing reference support resolved and newer RNF126 and
  temsirolimus papers integrated.

## 2025-12-28

- Completed the initial 22-gene human ferroptosis review batch across the core
  machinery, regulatory network, and supporting genes.
- Validated all 22 seeded gene reviews and drafted the standalone human pathway
  summary at `genes/human/FERROPTOSIS.md`.
