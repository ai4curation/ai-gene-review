---
title: "Ligands in signaling pathways"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, DANRE, DROME, SCHPO]
genes:
  - NTN1
  - NTN3
  - DCC
  - VEGFA
  - KITLG
  - kitlga
  - EFNB1
  - MIF
manifest:
  artifacts:
    - href: https://claude.ai/artifact/J3MezLgjhawKdowHbNDKRJ
      title: Ligand gap report
      description: AI generated
---

# Ligands in signaling pathways

**Status: incomplete, handed off mid-way.** See [Handoff](#handoff) for what is done, what is
next, and how to rerun everything.

**Bottom line:** GO treats a protein ligand as part of the signaling pathway it starts, and
human and fly curators annotate it that way. That gives a simple completeness test: every
receptor-initiated pathway an organism annotates should contain at least one gene with
receptor ligand activity. Run on seven GO Consortium GAFs, the test fails for a third or more
of the pathway terms in every organism. Most failures have no protein ligand to find (small
molecules, light, microbial products, antigens). The rest are real gaps: ligands missing from
their pathway, ligands placed only on a neighbouring term, and ligands that carry a
receptor-specific binding term (such as "Roundabout binding") instead of a ligand-activity term.

Knowing that *some* ligand is missing needs only GOA. Knowing *which* ligand is missing is
curated knowledge, and the curated module is the place to keep it with its evidence. We
therefore started curating pan-species signaling modules whose first step is the ligand, so
that generic pathway hole-filling can report the gaps. Three new two-step modules are done
(netrin, Slit-Robo, and MIF-CD74) and two existing modules with open ligand gaps were upgraded
to family-level ligand steps (Kit signaling and Ephrin-Eph signaling).

## 1. Are ligands part of the pathway in GO?

Yes, in standard annotation and in the ontology.

- **Annotations.** A hand-picked sample of textbook ligands was checked against QuickGO
  ([results/ligand_survey.json](LIGANDS_IN_SIGNALING/results/ligand_survey.json),
  [script](LIGANDS_IN_SIGNALING/scripts/survey/ligand_pathway_survey.py)). 21 of 22 human
  ligands (plus 4 of 5 receptor comparators) and all 14 fly ligands are annotated `involved_in`
  the pathway they activate, mostly
  with experimental evidence (FlyBase almost entirely so). Human KITLG is the exception: it has
  no Kit signaling pathway annotation. Receptors are annotated the same way, except the
  inhibitory receptors PTCH1 and ptc, which carry only regulation terms.
- **Fission yeast is different.** PomBase annotates the pheromones map2 and mfm1-3, the
  receptors mam2 and map3, and the G-alpha gpa1 alike to *positive regulation of pheromone
  response MAPK cascade*; only the kinases are `involved_in` the cascade. The old pathway term
  (pheromone-dependent signal transduction involved in conjugation with cellular fusion) is
  obsolete. We want one convention across GO, so this is a convention to raise, not to model
  around.
- **Ontology.** *Receptor ligand activity* (GO:0048018) is `part_of` *signal transduction*
  (GO:0007165), whose definition says it "begins with reception of a signal (e.g. a ligand
  binding to a receptor…)". The GO-CAM signaling receptor guideline (reviewed 2023-07-20) says
  a ligand "'enables' receptor ligand activity (GO:0048018) or a child" and is "'part of' the
  process in which the ligand participates".
- **The "cellular response to X" question is open.** Since 2014 pathway terms are `part_of`
  the matching *cellular response to X stimulus* term, so a ligand in the pathway is, by
  inference, in the response. Whether ligands should carry the response term is unresolved in
  [go-ontology#15477](https://github.com/geneontology/go-ontology/issues/15477) (2018); R.
  Lovering and P. Gaudet said there that the ligand belongs in the pathway. The link is applied
  unevenly: for example *vascular endothelial growth factor signaling pathway* is part of the
  VEGF response, but *vascular endothelial growth factor receptor signaling pathway* is not.
  Earlier history: [#5890](https://github.com/geneontology/go-ontology/issues/5890) (2009),
  [#10067](https://github.com/geneontology/go-ontology/issues/10067) (2012, is_a), then a
  2014-12-20 move to part_of.

## 2. Ligand activity versus receptor binding terms

A background research pass (go-ontology issues, GO docs, QuickGO term history) found that
annotating ligands only with "X receptor binding" terms is history, not policy:

- GO's written guidance is to annotate a ligand to *receptor ligand activity* or a child. No
  guideline gives the receptor-specific binding terms a role for ligands.
- In January 2026
  ([go-ontology#31015](https://github.com/geneontology/go-ontology/issues/31015), PR #31370)
  *receptor ligand activity* changed from "a kind of *signaling receptor binding*" to "has
  *signaling receptor binding* as a part", so that ligand activity is "classed as an activity
  rather than binding only" (V. Wood). Since then a ligand annotated only to, say, *Roundabout
  binding* no longer counts as a ligand. That is why these gaps are now visible.
- The receptor-specific terms (*Notch binding*, *frizzled binding*, *patched binding* date from
  2001) are old and not scheduled for replacement; a 2022 request for a ligand-binding branch
  ([#23891](https://github.com/geneontology/go-ontology/issues/23891)) was closed as not planned.
- They are noisy: *netrin receptor binding* is annotated only to receptor-side proteins (DSCAM,
  tubulins) and to no netrin; *Notch binding* sits on ADAM17, DTX1 and numb; *patched binding*
  on SMO.
- The comment on *signaling receptor binding* (GO:0005102) still points to "receptor agonist
  activity", a name retired in 2017. No open issue covers this.
- Hedgehog is an awkward case: Hh binding inhibits Patched, while *receptor ligand activity* is
  now classed as an activator. [#14275](https://github.com/geneontology/go-ontology/issues/14275)
  (open since 2017, agonist vs antagonist ligand terms) is the natural place to raise it.
  **Undecided; parked.**

**Decisions taken (C. Mungall, this session):**

1. A module's ligand step uses *receptor ligand activity* or a fitting child (for example
   *chemorepellent activity*), not the receptor-specific binding term.
2. Keep the PANTHER family and PAINT ancestral node on the ligand step with the correct term,
   and record in the family review that the PAINT node's binding term should be the
   ligand-activity term.
3. Modules are pan-species; species proteins are representative examples only.
4. Receptor-specific binding terms in gene reviews should generally be MODIFY. The replacement
   depends on the protein: ligands go to receptor ligand activity or a child; non-ligands that
   bind a receptor need their real activity (adaptor, enzyme, and so on). Adaptor terms that GO
   places under signaling receptor binding (such as *transmembrane receptor protein tyrosine
   kinase adaptor activity*) are already activities and are excluded.

## 3. The ligand gap check

**Rule.** For each organism, every pathway term P under *cell surface receptor signaling
pathway* (GO:0007166) or *G protein-coupled receptor signaling pathway* (GO:0007186) that the
organism's GAF uses directly must contain a gene that is `involved_in` P (or a subterm) and
`enables` *receptor ligand activity* (or a subterm). GPCR pathways are added separately because
they are not under cell surface receptor signaling. The check uses only GOA and the ontology:
no modules, no hand-picked lists.

Full output: [results/RESULTS.md](LIGANDS_IN_SIGNALING/results/RESULTS.md) (generated). Summary
for the GAFs dated 2026-05-21 and GO release 2026-07-26:

| Organism | Pathway terms used | No ligand gene |
|---|---|---|
| human | 237 | 78 |
| mouse | 234 | 86 |
| rat | 231 | 79 |
| zebrafish | 145 | 91 |
| fly | 74 | 39 |
| budding yeast | 6 | 6 |
| fission yeast | 4 | 4 |

**Triage.** [scripts/triage.py](LIGANDS_IN_SIGNALING/scripts/triage.py) sorts each failure.
Where a term passes in another species of the same lineage, that species' ligands are looked up
by gene symbol in the failing species. Where no species passes, an expected-ligand list is used.
Both curated inputs are explicit files, so the prior knowledge is visible and reviewable:

- [curated/term_labels.yaml](LIGANDS_IN_SIGNALING/curated/term_labels.yaml): terms with no host
  protein ligand (X: small molecule, light, microbial; Y: antigen, contact, ligand-independent).
- [curated/expected_ligands.yaml](LIGANDS_IN_SIGNALING/curated/expected_ligands.yaml): expected
  ligands per term. Each entry is a candidate ligand step for a module.
- [curated/organism_flags.yaml](LIGANDS_IN_SIGNALING/curated/organism_flags.yaml): suspect
  over-annotations (O) and misapplied or generic terms (G).

| Category | human | mouse | rat | zebrafish | fly |
|---|---|---|---|---|---|
| A: ligand counterpart not on the pathway | 11 | 10 | 13 | 29 | 5 |
| B: ligand only on a related pathway term | 8 | 9 | 9 | 7 | 1 |
| C: ligand on the pathway but no ligand-activity MF | 4 | 4 | 4 | 8 | 2 |
| X/Y: no host protein ligand expected | 48 | 51 | 45 | 39 | 21 |
| O: suspect over-annotation | 0 | 0 | 0 | 0 | 6 |
| Other (N, U, G) | 7 | 12 | 8 | 8 | 4 |

Examples (human unless noted). A: KITLG, IL21, IL22, CXCL8, C5, MIF, FASLG and the netrins are
not on their pathways. B: VEGFA/VEGFB/PGF are on VEGF receptor signaling but not the VEGFR-1
subterm; the FGFs are on FGF receptor signaling but not its "involved in X" subterms; fly spz5
and NT1 are only on Toll signaling, not neurotrophin signaling. C: IL34 and the collagens are in
their pathways without a ligand MF; fly Ephrin and sli likewise. O (fly; from background
knowledge, not checked): NGF, neurotrophin TRK, G-CSF, adiponectin, TLR4 and LPS-mediated
signaling terms in a genome without those ligands or receptors.

Before the triage was automated, 28 human and fly failures were sorted by hand into A, B or C.
The automatic lookup agrees on 21. The differences: three FGF "involved in X" subterms have no
donor (U); the FGF receptor apoptotic signaling term comes out C because FGFR3 itself carries a
ligand-activity MF in another species; and three fly cases that are really B (egr, Ilps,
spz5/NT1 sit on a sibling pathway) come out A because the sibling shares only generic ancestors.
(X, Y, O and G agree by construction, since the hand labels are the curated inputs.)

**Reverse check.** Ligand-activity genes in no signaling pathway: 22 of 571 in human (mostly
chemokines such as CCL17, CCL27, CCL28, CXCL2, CXCL3, CXCL16, PPBP, PF4V1, and beta-defensins;
ALKBH1 and DPP4 look like MF over-annotation), 1 in fly (orion), none in either yeast. In
budding yeast the receptors STE2/STE3 are in the pheromone pathway but the pheromones are not.

**Relaxing the rule does not work.** Counting genes with a *signaling receptor binding* MF plus
an extracellular CC annotation as ligands makes 31 more human terms and 3 more fly terms pass,
almost all falsely: G-protein alphas, LYN and IRAK4 qualify through exosome or extracellular
annotations, and netrin signaling "passes" on DSCAM and tubulin. Only IL34 (human) and sli
(fly) are real. The ligand step has to come from curated modules.

Caveats: symbol matching stands in for orthology; budding yeast and fission yeast have no
same-lineage donor in the seven-species panel (so unflagged yeast terms fall into U);
go-basic omits MF-to-BP part_of links, which is harmless here because only BP annotations
place genes in pathways.

## 4. Curated modules

All five modules have family-grounded pan-species ligand steps and pass the schema and module
validators.

- **[Netrin signaling](../modules/netrin_signaling.yaml)** (*netrin-activated signaling
  pathway*). Ligand: netrin family (PANTHER netrin/laminin family `PTHR10574`, restricted to
  canonical secreted netrins under PAINT node PTN008501429 and excluding netrin-G1/G2,
  netrin-4, and netrin-5), *receptor ligand activity* (netrins both attract and repel, so neither
  child fits). Receptor: attraction through the DCC family (no PANTHER id; DCC and Frazzled sit
  in different subfamilies of a broad family) or repulsion through the UNC5 family. GOA gaps
  recorded in the notes: no netrin and not DCC is on the netrin pathway in human; fly NetA/NetB
  are only on axon guidance terms and have no MF.
- **[Slit-Robo signaling](../modules/slit_robo_signaling.yaml)** (*Roundabout signaling
  pathway*). Ligand: Slit subfamilies of PTHR45836, *chemorepellent activity*, with PAINT node
  PTN002911633 kept. The validator warns that the node's own term is *Roundabout binding*; that
  warning is intentional and documented. Receptor: Robo receptors (no PANTHER id; they span three
  families). GOA gaps in the notes: human SLIT1 and ROBO2, fly robo2 and robo3 are not on the
  pathway.
- **[Kit signaling](../modules/kit_signaling.yaml)** (*Kit signaling pathway*, `GO:0038109`).
  Upgraded the ligand step (`kitlg_scf_ligand`) from a single-gene `ENTITY` to `FAMILY`
  (`PANTHER:PTHR11574` `KIT LIGAND`, PAINT node `PTN002611905`, *stem cell factor receptor
   ligand activity* `GO:0038111`) with representative members across human (`KITLG`), mouse
  (`Kitl`), rat (`Kitlg`), and zebrafish (`kitlga`, `kitlgb`). GOA gaps resolved in gene reviews:
  human `KITLG` and zebrafish `kitlga` lacked `GO:0038109` *Kit signaling pathway* (added as
  `NEW` in both reviews).
- **[Ephrin-Eph signaling](../modules/ephrin_receptor_signaling.yaml)** (*ephrin receptor
  signaling pathway*, `GO:0048013`). Upgraded the ligand step (`efnb2_efnb2_ligand`) from a
  single-gene `ENTITY` using *ephrin receptor binding* (`GO:0046875`) to `FAMILY`
  (`PANTHER:PTHR11304` `EPHRIN`, PAINT node `PTN000885159`, *receptor ligand activity*
  `GO:0048018`) with representative members spanning GPI-anchored ephrin-A (`EFNA1`),
  transmembrane ephrin-B (`EFNB1`, `EFNB2`, `Efnb2`), *C. elegans* (`vab-2`), and *Drosophila*
  (`Ephrin`). The validator's `PAINT_TERM_NOT_ASSERTED` warning on `PTN000885159` (`GO:0048018`
  vs PAINT's `GO:0046875`) is intentional per Decision 2 and documented in
  `interpro/panther/PTHR11304/PTHR11304-review.yaml`.
- **[MIF-CD74 signaling](../modules/mif_signaling.yaml)** (*macrophage migration inhibitory
  factor signaling pathway*, `GO:0035691`). Two-step pan-species module. Ligand: MIF /
  D-dopachrome tautomerase family (`PANTHER:PTHR11954`, PAINT nodes `PTN000237513` and
  `PTN000237510`), *cytokine activity* (`GO:0005125`, a child of *receptor ligand activity*
  `GO:0048018`). Receptor: CD74 subfamily (`PANTHER:PTHR14093:SF17`, PAINT node `PTN002679661`),
  *cytokine receptor activity* (`GO:0004896`). GOA gap resolved in the new human `MIF` gene
  review: human `MIF` carried `GO:0005125` *cytokine activity* and `GO:0048018` *receptor ligand
  activity* (IBA) but lacked `GO:0035691` *macrophage migration inhibitory factor signaling
  pathway* (`NEW` added).

## 5. Other curator work in this branch

- **NTN1 and NTN3 gene reviews:** core function and MODIFY replacements changed from *netrin
  receptor binding* to *receptor ligand activity*, and `NEW` annotations for *netrin-activated
  signaling pathway* (`GO:0038007`) added to both reviews and their `core_functions`. NTN1's
  four non-verbatim deep-research quotes (listed in `conf/local_quote_baseline.yaml`) replaced
  with row-specific verbatim publication quotes and their baseline entries removed. The repo-wide
  prune would also remove 233 now-passing entries for other genes; that was left out to keep this
  change focused.
- **KITLG, kitlga, EFNB1, and MIF gene reviews:** added `NEW` `GO:0038109` (*Kit signaling
  pathway*) to human `KITLG` and zebrafish `kitlga`; updated `GO:0046875` (*ephrin receptor
  binding*) to `MODIFY` → `GO:0048018` (*receptor ligand activity*) on human `EFNB1`; and
  created the full human `MIF` review (`genes/human/MIF/MIF-ai-review.yaml`) with `NEW`
  `GO:0035691` (*macrophage migration inhibitory factor signaling pathway*) and `MODIFY` on
  `GO:0005102` (*signaling receptor binding*) → `GO:0005125` (*cytokine activity*).
- **PANTHER family reviews** (`PTHR45836`, `PTHR11574`, `PTHR11304`, `PTHR11954`):
  - `interpro/panther/PTHR45836/PTHR45836-review.yaml`: the `PTN002911633` assessment notes that
    its IBD should use the ligand-activity term; a new `SUBFAMILY_ONLY` assessment of
    *chemorepellent activity* covers the four Slit subfamilies.
  - `interpro/panther/PTHR11574/PTHR11574-review.yaml`: `APPROVE` assessment for `PTN002611905`
    (`GO:0038111` *stem cell factor receptor ligand activity*, `GO:0038109` *Kit signaling
    pathway*).
  - `interpro/panther/PTHR11304/PTHR11304-review.yaml`: `MODIFY_TERM` assessment on
    `PTN000885159` replacing `GO:0046875` (*ephrin receptor binding*) with `GO:0048018`
    (*receptor ligand activity*) while retaining `GO:0048013` (*ephrin receptor signaling
    pathway*).
  - `interpro/panther/PTHR11954/PTHR11954-review.yaml`: `APPROVE` on `PTN000237513` (`GO:0005125`
    *cytokine activity*, `GO:0048018` *receptor ligand activity*) with a `MISSING_ANNOTATION`
    assessment proposing `GO:0035691` (*macrophage migration inhibitory factor signaling
    pathway*) at the vertebrate MIF/DDT node.
- **Corpus count of receptor-specific binding terms** in gene reviews: 820 annotation rows in
  353 reviews (489 ACCEPT, 221 KEEP_AS_NON_CORE, 13 MODIFY), plus 162 core functions. Most common:
  Notch binding (73), integrin binding (67), EGF receptor binding (36), ephrin receptor binding
  (30), FGF receptor binding (29). Not yet acted on.
- History records for every edit are under `history/`.

## Handoff

### Done

- Ligand survey, gap check, triage and the relaxed-rule experiment, all rerunnable (below).
- Research on GO policy (sections 1 and 2) and the decisions in section 2.
- Modules: `netrin_signaling`, `slit_robo_signaling`, `kit_signaling` (upgraded),
  `ephrin_receptor_signaling` (upgraded), `mif_signaling`.
- Gene reviews: NTN1, NTN3, KITLG, kitlga, EFNB1, MIF.
- Family reviews: PTHR45836, PTHR11574, PTHR11304, PTHR11954.
- Report page: [report/ligand-gap-report.html](LIGANDS_IN_SIGNALING/report/ligand-gap-report.html)
  (human, fly and fission yeast snapshot; also published as the Ligand gap report artifact).
  It predates the GPCR scope and the other species, so its counts are lower than section 3.

### Next steps

1. **More modules**, pan-species, ligand step first, using the decisions in section 2. Queue from
   the gap check: collagen-DDR, fly Toll-6/7 neurotrophin (spz5, NT1), IL-21, IL-22.
   Several human gaps (VEGFR-1/3, FGFR, Fas, CXCL8) already have modules with the
   ligand; they need the hole-filling run, not new modules.
2. **Module-driven hole filling.** Replace `curated/expected_ligands.yaml` with the modules: an
   annotation oracle for `src/ai_gene_review/module_logic.py` that resolves each ligand annoton's
   family to members per species (PANTHER membership, as in
   `projects/PATHWAY_SATISFIABILITY/taxon_absent_component/`) and asks GOA whether they carry the
   module's pathway term. Unfilled ligand steps are the gaps.
3. **Binding-term MODIFY batch** over the 820 rows and 162 core functions: propose a replacement
   per row (ligand → receptor ligand activity or child; non-ligand → its actual activity; skip
   adaptor terms), for curator review. Consider adding the rule to CLAUDE.md.
4. **GO issues to draft for C. Mungall:** the outdated comment on *signaling receptor binding*;
   ligands annotated only with receptor-specific binding terms; PomBase's pheromone convention
   (ligand and receptor as regulators of the MAPK cascade) and budding yeast pheromones missing
   from the pathway; optionally Hedgehog/Patched on #14275.
5. **VEGFA review inconsistency, unresolved:** it REMOVEs *cellular response to vascular
   endothelial growth factor stimulus* ("VEGFA is the ligand, not the responder") while ACCEPTing
   *vascular endothelial growth factor signaling pathway*, which is part_of that response.
   Decide alongside #15477; no edit was made.
6. Check the fly over-annotation (O) calls against data before acting on them.

### How to rerun

```bash
# data (GAFs + go-basic.obo) into the git-ignored .cache/ligands_in_signaling
projects/LIGANDS_IN_SIGNALING/scripts/fetch_data.sh
# gap check for all seven organisms, then the relaxed-rule variant for human and fly
uv run python projects/LIGANDS_IN_SIGNALING/scripts/ligand_gap_check.py --out projects/LIGANDS_IN_SIGNALING/results
uv run python projects/LIGANDS_IN_SIGNALING/scripts/ligand_gap_check.py --out projects/LIGANDS_IN_SIGNALING/results --orgs human fly --or-receptor-binding
# triage; writes results/triage.json and results/RESULTS.md
uv run python projects/LIGANDS_IN_SIGNALING/scripts/triage.py --results projects/LIGANDS_IN_SIGNALING/results
# QuickGO survey of textbook ligands (network; a few minutes)
uv run python projects/LIGANDS_IN_SIGNALING/scripts/survey/ligand_pathway_survey.py --out projects/LIGANDS_IN_SIGNALING/results/ligand_survey.json
```

### Known issues

- Module validator warnings: PANTHER family-membership checks pass against `.cache/panther/panther-members-19.0.tsv`;
  the remaining advisory warnings are `PTN008501429` MOD-ID seed comparison (no UniProtKB accessions in `PTHR10574-paint.tsv`)
  and the intentional `PAINT_TERM_NOT_ASSERTED` / `SUBFAMILY_ONLY` warnings on `slit_robo_signaling.yaml` (`GO:0045499` vs PAINT's `GO:0048495`)
  and `ephrin_receptor_signaling.yaml` (`GO:0048018` vs PAINT's `GO:0046875`).
- `tests/test_bioreason_benchmark_policy.py::test_argo95_exact_goa_reads_the_declared_baseline_commit`
  fails on main as well; unrelated to this work.
