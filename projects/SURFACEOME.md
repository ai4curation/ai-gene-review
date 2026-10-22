---
title: "Accessible Surfaceome (SurfaceBench) Comparison"
maturity: IN_PROGRESS
tags: [EVALUATION, BIOLOGY_DOMAIN]
species: [human]
sidecars:
  scripts: SURFACEOME/scripts/
  gaf_rule_scores: SURFACEOME/results/gaf_rule_scores.tsv
  gaf_per_gene: SURFACEOME/results/gaf_per_gene.tsv
  review_per_gene: SURFACEOME/results/review_per_gene.tsv
  catalog_overlap: SURFACEOME/results/catalog_overlap.tsv
manifest:
  artifacts:
    - href: https://claude.ai/artifact/WCjRqayPU7HqmNMi6YwR78
      title: Project brief
---

# Accessible Surfaceome (SurfaceBench) Comparison

> **Status: INCOMPLETE — handed off mid-analysis (2026-10-21).** See
> [Handoff](#handoff-next-steps) at the bottom before continuing.

## Background

The Deliverome Project preprint *The accessible human surfaceome*
(<https://deliverome.org/paper/accessible-surfaceome/>; viewer
<https://surfaceome.deliverome.org/>; code
<https://github.com/Deliverome-Project/accessible-surfaceome>; data Zenodo record
23445521, v1.3.0) uses an LLM pipeline to call which human proteins are
**accessible on the extracellular face of an intact cell**. It releases:

- a catalog of 1,783 `canonical` + 1,252 `likely` surface proteins (5,332 genes
  given a "deep dive" in total), and
- **SurfaceBench**: 147 proteins on which five public databases (UniProt, GO,
  SURFY, CSPA, HPA) disagree, curated as `yes` (68) / `contextual` (31) / `no` (48)
  (<https://surfaceome.deliverome.org/benchmark/>).

The paper reports GO as a weak baseline (42.2% on SurfaceBench). This project
(a) makes sure every SurfaceBench protein has an ai-gene-review human review,
(b) checks our localization calls against the benchmark, and (c) asks how well
**public GO annotations** can answer the "accessible surface" question, and why
the paper's GO baseline scored so low.

## 1. Coverage

From `scripts/overlap.py` (`results/catalog_overlap.tsv`):

| Catalog tier | Catalog genes | With a human review |
|---|---|---|
| canonical | 1,783 | 286 |
| likely | 1,252 | 164 |
| low / uncertain / no | 2,297 | 318 |

**SurfaceBench: 147/147 reviewed.** 43 already existed; the other 104 were
created in this project (branch `surfacebench-reviews`, one commit per batch).
The new reviews were written by parallel agents; no automated deep-research
provider was available (no API keys), so each gene's research and provenance is in
`genes/human/GENE/GENE-notes.md`. All pass `just validate`, and each has a history record.

Edits to existing reviews prompted by the benchmark: **HSPA1A** and **HMGB1**
plasma-membrane/cell-surface rows changed ACCEPT → KEEP_AS_NON_CORE, because their
surface pool is stress- or activation-induced and core locations are
nucleus/cytosol.

## 2. How the paper scored GO

From `src/accessible_surfaceome/sources/go.py` in the authors' code:

- Surface if any **non-IEA**, non-NOT annotation to `GO:0009986` cell surface,
  `GO:0009897` external side of plasma membrane, or `GO:0005887` integral
  component of plasma membrane (each with is_a/part_of descendants).
- `GO:0005886` plasma membrane was deliberately excluded ("too broad, includes
  cytoplasmic-face"), as was `GO:0098552` side of membrane.
- Scored as binary accuracy with `yes` + `contextual` collapsed to surface.

Two problems found:

1. **`GO:0005887` is obsolete** (replaced by `GO:0005886`) in the current GO
   (local build 2026-07-26). No benchmark protein carries it in the current GAF, so
   the rule effectively reduces to "cell surface or external side of PM". The
   anchored and intrinsic component terms (`GO:0031225`, `GO:0046658`,
   `GO:0031362`, `GO:0031226`) are also obsolete, so **GO no longer has a live term
   for GPI-anchored or integral PM proteins**.
2. **The benchmark's own `db_go` column does not follow that rule.** It flags
   KRAS, LYN, the JAKs, SYK, RAC1, RHOA, SYNE1/2 and IL6 as GO-surface (their only PM-type
   terms are *cytoplasmic side of plasma membrane*), and flags GCGR, SSTR2 etc. as
   not surface (they carry only `plasma membrane`). The term set that best
   reproduces `db_go` is **outward CC + side of membrane (`GO:0098552`) + plasma
   membrane protein complex (`GO:0098797`): 131/147 agreement**. That is the
   "Tier C" set the authors' code comments say was dropped on 2026-04-17. So the
   published 42.2% appears to count inner-leaflet proteins as GO surface calls.
   *This is an inference from matching the column against the annotations, not a
   statement in the paper or code — confirm with the authors.*

## 3. Public GO annotations vs SurfaceBench

`scripts/score_gaf.py` on `goa_human.gaf` (downloaded 2026-10-21; header
`!date-generated: 2026-05-21T08:10`). Accuracy uses the paper's convention
(yes+contextual = surface, n=147), and separately yes vs no only (n=116).

| Rule (public annotations) | yes | ctx | no called surface | Acc (147) | Acc yes/no (116) |
|---|---|---|---|---|---|
| R1 outward CC (cell surface or external side of PM), no IEA | 22/68 | 10/31 | 3/48 | 52.4% | 57.8% |
| R1, IEA included | 23/68 | 11/31 | 3/48 | 53.7% | 58.6% |
| **R2 = R1 OR (PM AND TM function)**, no IEA | 46/68 | 13/31 | 5/48 | **69.4%** | **76.7%** |
| R2, IEA included | 48/68 | 14/31 | 5/48 | 71.4% | 78.4% |
| R0 plain plasma membrane, no IEA | 66/68 | 26/31 | 32/48 | 73.5% | 70.7% |

The TM functions in R2 are transmembrane signaling receptor activity
(`GO:0004888`), transmembrane transporter activity (`GO:0022857`) and channel
activity (`GO:0015267`), each with descendants. An extra inner-side exclusion rule
(R3: drop proteins whose only PM evidence is cytoplasmic-side terms) changes
nothing, because those proteins already fail R2. Plain PM looks competitive on
the 147-set only because it lets through 32/48 `no` proteins; the contextual-heavy
benchmark rewards that.

**R2 errors (no IEA):**

- `yes` missed (22) — fall into GO gaps:
  - GPI-anchored (no live GO term): LYPD1, LYPD3, PSCA, DPEP1.
  - Adhesion/junction (no receptor/transporter/channel MF): CLDN6, CLDN18, DSG3, DSG4, EPCAM, NECTIN4, MUC1, TACSTD2.
  - Ectoenzymes: CA9, STEAP1, STEAP2, GUCY2C.
  - Orphan or unknown MF: GPRC5D, GPNMB, SEZ6, DLK1, GYPA, TM4SF1.
- `no` called surface (5): ITPR1, ITPR3 (ER channels with a PM annotation),
  F2, TF, VEGFA (secreted ligands with cell-surface annotations).
- `contextual` (18 not called surface): mostly lysosomal/secretory-pathway
  proteins with a minor surface pool (LAMP1/2, CD68, PMEL, TYRP1, TGOLN2, STIM1).

Per-gene calls: `results/gaf_per_gene.tsv`.

## 4. Our review calls vs SurfaceBench (secondary)

`scripts/score_reviews.py`, using accepted, kept, modified (replacement term) and
new rows plus `core_functions` locations:

| Rule (our reviews) | yes | ctx | no called surface | Acc (147) | Acc yes/no (116) |
|---|---|---|---|---|---|
| R1 outward CC | 25/68 | 14/31 | 3/48 | 57.1% | 60.3% |
| R2 | 48/68 | 16/31 | 5/48 | 72.8% | 78.4% |
| R0 plain PM | 68/68 | 27/31 | 30/48 | 76.9% | 74.1% |

Reviews add a little (a few NEW cell-surface rows, refinements to
cytoplasmic-side terms), but they follow GO convention and do not add cell
surface to every TM receptor. A blanket addition would conflict with the repo rule
against manufacturing annotations (see CLAUDE.md "Do not add what curators
deliberately declined to add").

Review-level calls worth expert eyes:

- **DLL3**: two experimental PM rows were MODIFYed to Golgi/late endosome, with a NEW non-core cell-surface row for the tumour pool.
- **LGR5**: called mostly internalized at steady state.
- **IZUMO4**: called soluble; its IEA membrane row was removed.
- **F2**: core location is external side of PM.
- **TMED10 / KLK2**: neither has a surface location.
- **Source defects recorded**:
  - F2 thrombospondin receptor activity: the paper's receptor is CD36.
  - FLT3 VEGF receptor rows: from FLT name confusion.
  - FZD10 ISS rows: the WITH donor is the ligand WNT7B.
  - CD24 interaction row: FGFR1 where the paper studies FGR.
  - ABCB9 ER row: cites mis-keyed PMID 1101155 (should be 11011155).

## 5. Why "plasma membrane" is ambiguous for accessibility

1. **Inner-leaflet / peripheral cytoplasmic** proteins (KRAS, LYN, BTK, JAKs):
   cytoplasmic-side terms exist but are rarely used.
2. **Outer-leaflet GPI-anchored** proteins: now plain PM, since the anchored-component terms are obsolete.
3. **Secreted ligands bound at the surface** (F2, TF, VEGFA, latent TGFB1,
   LDL/APOB, C3b). `GO:0009986` is defined as "The external part of the cell wall
   and/or plasma membrane", so these legitimately carry it. Note that cell surface
   is *not* an is_a/part_of descendant of PM.
4. **TM proteins with minimal exposure**: claudins and tetraspanins expose only
   small loops, and tight junctions hide them.
5. **PM subdomains** with tissue-dependent accessibility: apical vs basolateral,
   T-tubule, sarcolemma, cilium, postsynaptic membrane, acrosome.
6. **Between membranes**:
   - ER–PM contact site (`GO:0140268`; STIM1): not under PM.
   - Intercellular junctions spanning two PMs: desmosome (`GO:0030057`) and gap junction (`GO:0005921`) are not under PM either, so PM-descendant rules miss DSG3 and the connexins.
   - Synaptic cleft.
7. **Transient or vesicle-derived** surface presence: lysosomal exocytosis (LAMP1, CD63), the phagocytic cup, exosomes.
8. **Evidence artifacts**: PM from membrane-fraction proteomics (HDA), and
   Reactome TAS assigning PM to a whole complex (the APOB/LDL case).

## Reproducing

```bash
projects/SURFACEOME/scripts/fetch_inputs.sh   # Zenodo v1.3.0 files + current goa_human.gaf.gz -> data/ (git-ignored)
projects/SURFACEOME/scripts/run_all.sh        # writes results/*.tsv and *.txt
```

`run_all.sh` needs the oaklib GO sqlite at `~/.data/oaklib/go.db` (created by any
`runoak -i sqlite:obo:go` call). Results drift as GO and the GAF are updated; the
numbers above are from the run on 2026-10-21.

## Handoff: next steps

The work is incomplete. In priority order:

1. **Extend the public-GO rule (R2)** in `scripts/score_gaf.py`, then re-run:
   - count cell-adhesion MF as TM evidence (e.g. `GO:0098631` cell adhesion
     mediator activity), and possibly ectoenzyme evidence. Check FP risk against the `no` set.
   - count junction CC terms that sit outside PM (desmosome `GO:0030057`,
     tight junction / bicellular tight junction, gap junction `GO:0005921`)
     as surface evidence.
   - drop ITPR-type false positives: require the TM function and the PM annotation to be non-IBA, or
     require that PM is not outweighed by ER-membrane experimental annotations.
   - Report every change in a new row in §3; never tune on per-gene names.
2. **Confirm the `db_go` finding** (§2, point 2) with the authors before
   publicizing it. Their code is pinned at commit `80930d0` (cloned 2026-10-21).
3. **Score our reviews** with the final rule (§4), and decide whether to make inner-face proteins consistently
   use `GO:0009898` / `GO:0031234` instead of bare `GO:0005886`. Candidates:
   JAK1, MAP2K1, LRRK2, IKBKB, AKT2, BTK, KRAS, NRAS, LYN, BRAF, SYK, RAC1, RHOA, HCK.
   That is a refinement (MODIFY), allowed where the evidence supports it.
4. **Expert-review the flagged review calls** in §4 (DLL3, LGR5, IZUMO4, F2,
   the source defects).
5. **Optional:** compare against UniProt topology (`TOPO_DOM Extracellular`,
   `LIPID GPI-anchor`) as a non-GO reference. The paper's best single database was
   UniProt's expanded rule (89.8%). The user asked to focus on GO first.
6. Branch `surfacebench-reviews` is PR
   [#5312](https://github.com/ai4curation/ai-gene-review/pull/5312); push follow-up
   commits there, and get it green and merged. The project card in
   `pages/projects/index.html` is already added.

Work log: the session that started this project ran 10 parallel review agents
(10–11 genes each) over the 104 missing SurfaceBench genes, then committed each batch after
`just validate` passed. The scratch versions of these scripts were moved here.
