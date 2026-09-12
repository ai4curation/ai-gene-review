---
title: "Proteostasis Review Batch 5 — Gene Selection"
---

# Proteostasis Review Batch 5 — Gene Selection

Date: 2026-06-07
Branch: `claude/proteostasis-50-genes-xFOZK`

## Context

The four prior batches are complete:
- `proteostasis-pr-1217` (50 human genes, merged 2026-06-02)
- `proteostasis-batch-2026-06-03` (50 human genes, alphabetical sweep AAAS..ATP6V0D1)
- `proteostasis-batch-2026-06-06` (20 human genes; V-ATPase core, ER folding/QC,
  autophagy/mitophagy receptors, co-chaperone/UPS regulation)
- `proteostasis-batch-2026-06-07` (30 human genes; V-ATPase tissue isoforms + ClC-7,
  mito/ER chaperones, collagen biogenesis, histone chaperones, CRL/UPS adaptors)

This batch selects **50 more genes** from the PN projected candidate-additions
report (`reports/pn_projection/pn_projected_candidate_additions.tsv`), all PN
candidates with `ok_for_propagation_to_go` scope that had no local
`*-ai-review.yaml` before this batch.

## Theme: the protein-folding chaperone & co-chaperone network

Rather than continue the alphabetical sweep into low-value family/domain UPS
inclusions, batch 5 takes a **biologically coherent slice through the cytosolic
and ER protein-folding machinery** — the mechanistic heart of proteostasis. It
is dominated by the J-domain (HSP40) co-chaperone family, which had a large run
of unreviewed PN candidates, plus their HSP70/HSP90 partners, the small heat
shock proteins, the FKBP immunophilin co-chaperones, and the ER oxidative-folding
and peptidyl-prolyl isomerase enzymes.

### Deliberate exclusion of the mega-genes

`HSPA5` (BiP), `HSP90AA1`, and `HSP90AB1` were considered but **deferred**.
Each carries 50+ unique GOA GO terms (HSPA5 alone has 58 terms / 214 annotation
rows) and a very large literature; folding them into a 50-gene batch would force
shallow review. They are flagged for dedicated single-gene PRs and replaced here
by lighter but high-value hub co-chaperones (`STIP1`/Hop, `SGTA`, `SERPINH1`/HSP47).

## Selected genes (50)

### J-domain (HSP40 / DNAJ) co-chaperones — 29
Cytosolic, ER, and mitochondrial HSP70 J-domain co-chaperones that set HSP70
substrate specificity and stimulate its ATPase.

1. `DNAJB4` — cytosolic HSP40 (DNAJB1 paralog)
2. `DNAJB5` — cytosolic HSP40
3. `DNAJB11` (ERdj3) — ER-lumenal BiP J-protein co-chaperone
4. `DNAJB13` — flagellar/axonemal HSP40
5. `DNAJC1` (ERdj1/MTJ1) — ER membrane J-protein
6. `DNAJC3` (p58IPK/ERdj6) — ER J-protein, PERK/eIF2α regulation
7. `DNAJC4` — J-domain protein
8. `DNAJC5` (CSPα) — synaptic vesicle co-chaperone (ANCL/DNAJC5)
9. `DNAJC5B` — CSP paralog
10. `DNAJC5G` — CSP paralog
11. `DNAJC6` (auxilin/PARK19) — clathrin-uncoating HSC70 co-chaperone
12. `DNAJC7` (Tpr2) — TPR-containing HSP70/HSP90 shuttling co-chaperone
13. `DNAJC9` — histone H3-H4 co-chaperone / HSP70 J-protein
14. `DNAJC10` (ERdj5) — ER reductase / PDI-family J-protein, ERAD
15. `DNAJC11` — mitochondrial MIB/MICOS-associated J-protein
16. `DNAJC12` (JDP1) — cytosolic HSP70 co-chaperone (phenylalanine metabolism)
17. `DNAJC13` (RME-8/PARK21) — endosomal HSC70 co-chaperone
18. `DNAJC14` (DRIP78) — ER J-protein, receptor trafficking
19. `DNAJC15` (MCJ) — mitochondrial inner-membrane J-protein
20. `DNAJC16` — J-domain protein
21. `DNAJC17` — J-domain protein
22. `DNAJC19` (TIM14/TIMM14) — mitochondrial import motor J-protein
23. `DNAJC21` (DNAJA5) — ribosome biogenesis HSP70 co-chaperone
24. `DNAJC22` — J-domain protein
25. `DNAJC24` (DPH4) — diphthamide biosynthesis / J-domain
26. `DNAJC25` — J-domain protein
27. `DNAJC27` (RBJ) — Rab-domain J-protein
28. `DNAJC28` — J-domain protein
29. `DNAJC30` — mitochondrial J-protein (LHON-related)

### Small heat shock proteins (sHSP / HSPB) — 5
ATP-independent holdase chaperones.

30. `HSPB2` (MKBP) — small HSP, muscle
31. `HSPB3` — small HSP, muscle
32. `HSPB7` (cvHSP) — cardiovascular small HSP, aggregate handling
33. `HSPB8` (HSP22) — CASA-pathway holdase (BAG3 partner)
34. `HSPB9` — testis small HSP

### HSP70 / HSP90 hub co-chaperones — 6
35. `HSPA13` (STCH) — microsomal/ER atypical HSP70
36. `HSPA14` (HSP70L1) — ribosome-associated complex (RAC) HSP70
37. `STUB1` (CHIP) — HSP70/HSP90 co-chaperone & U-box E3 (triage/degradation)
38. `STIP1` (HOP) — HSP70-HSP90 organizing protein / adaptor
39. `SGTA` — small glutamine-rich TPR co-chaperone (BAG6/GET tail-anchor QC)
40. `SERPINH1` (HSP47) — ER collagen-specific molecular chaperone

### FKBP immunophilin co-chaperones — 4
PPIase-domain HSP90 co-chaperones.

41. `FKBP4` (FKBP52) — HSP90 co-chaperone, steroid receptor maturation
42. `FKBP5` (FKBP51) — HSP90 co-chaperone, stress/GR signaling
43. `FKBP8` (FKBP38) — membrane FKBP, Bcl-2/mTOR, BNIP3 mitophagy adapter
44. `FKBPL` (WISP39) — FKBP-like HSP90 co-chaperone

### ER oxidative folding & peptidyl-prolyl isomerization — 6
45. `P4HB` (PDI / PDIA1) — protein disulfide isomerase, prototypical ER folding enzyme
46. `ERO1A` (ERO1L) — ER oxidoreductin 1 alpha (reoxidizes PDI)
47. `ERO1B` (ERO1LB) — ER oxidoreductin 1 beta
48. `ERP27` — PDI-family non-catalytic chaperone (ERp27)
49. `ERP29` — PDI-family ER chaperone (ERp29)
50. `PPIB` (cyclophilin B) — ER peptidyl-prolyl isomerase, collagen folding

## Method

For each gene:
- `uv run ai-gene-review fetch-gene human <GENE>` (UniProt, GOA, cached
  publications, seeded `-ai-review.yaml`).
- Research from cached publications + UniProt + literature; notes recorded in
  `<GENE>-notes.md` with provenance.
- Each seeded GOA annotation reviewed per GO guidelines (ACCEPT /
  KEEP_AS_NON_CORE / MODIFY / MARK_AS_OVER_ANNOTATED / REMOVE / UNDECIDED) with
  `supported_by` evidence.
- `description`, `core_functions`, `suggested_questions`, `suggested_experiments`
  populated.
- Validated with `uv run ai-gene-review validate human <GENE>`.

## Curation watch-points for this batch

- **Avoid `protein binding` (GO:0005515)** as a core function; for J-proteins
  prefer `GO:0001671 ATPase activator activity` / `GO:0030544 Hsp70 protein
  binding` / `GO:0051087 protein-folding chaperone binding` as appropriate.
- **Holdase vs foldase:** small HSPs and many J-proteins are holdases/co-chaperones,
  not autonomous foldases — keep `protein folding` (GO:0006457) as non-core where
  the gene only assists HSP70/HSP90.
- **Family/paralog over-annotation:** poorly characterized J-proteins (e.g.
  DNAJC4, DNAJC16, DNAJC22, DNAJC25, DNAJC28, DNAJC5B/G, HSPB9) may carry IBA
  terms transferred from better-studied paralogs; mark over-annotations.
- **Compartment specificity:** assign ER vs mitochondrial vs cytosolic
  localization carefully (e.g. DNAJC11/15/19/30 mitochondrial; DNAJB11/C1/C3/C10
  ER-lumenal/membrane).

## Feedback into the PN mapping sets (2026-06-07)

The batch-5 gene reviews were fed back into the curated PN source-code -> GO
mapping YAMLs (`projects/PROTEOSTASIS/mappings/`). Changes:

- **Correction (er_proteostasis):** the `Protein disulfide isomerase reoxidation`
  type node was retargeted from `GO:0003756` (PDI activity) to `GO:0016971`
  (flavin-dependent sulfhydryl oxidase activity); ERO1A/ERO1B are PDI-reoxidizing
  oxidases, not isomerases. ERO1A/ERO1B were ALSO added to the parent
  `Protein disulfide isomerases` group `excluded_subjects` so the parent
  PDI-activity term no longer double-propagates to them.
- **Exclusions:** ERP27, ERP29 (non-catalytic, no CXXC) from the PDI group;
  DNAJC27 (Rab/J MEK-ERK scaffold) from the cytonuclear J-domain cochaperone
  node; DNAJC11 (structural MIB/MICOS subunit) from the mitochondrial J-domain
  node; HSPA13/STCH (atypical, truncated SBD) from the ER HSP70 node; STIP1
  from the CMA `Substrate selection` node (no CMA evidence).
- **Confirmations + provenance:** added `file:` gene-review references to the
  HSP90-cochaperone (FKBP4/5/8/FKBPL), small-HSP (HSPB2/3/7/8/9), cytonuclear
  HSP70 (HSPA14), GET-pathway (SGTA), collagen processing (SERPINH1/PPIB/P4HB),
  CASA/aggrephagy (HSPB8/STUB1), and mitophagy (FKBP8) nodes, with curation
  notes (incl. that GO:0001671 / GO:0051082 are the more-specific J-protein /
  small-HSP MFs supported at the gene level).

Verified by re-running the PN projection against the affected genes: the
excluded gene-GO pairs are gone and ERO1A/B project only to GO:0016971.

**Caveat:** the canonical candidate-additions report
(`reports/pn_projection/pn_projected_candidate_additions.tsv`) was NOT
regenerated in this session because the DuckDB GOA source
(`~/repos/go-db/db/goa_human.ddb`) is unavailable here; regenerating against
only the local `genes/human` GOA folders would mark ~3000 workbook genes as
`no_local_goa` and degrade the committed report. The projection should be
regenerated against the DuckDB GOA source to propagate these mapping edits into
the candidate queue.
