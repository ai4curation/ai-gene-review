# Apoptosis phase 2 scope: ontology, cross-species completeness, GO-CAMs

Drafted 2026-11-23. This is a proposal to agree on, not a record of work done.

**Bottom line:** phase 1 of this project was a mammal-first review campaign
and it is finished: 58 genes reviewed and seven apoptosis modules drafted. Phase 2 changes the unit of work from the gene to the **step**. We
fix one spine of about a dozen apoptosis steps, give each step a GO term with a
logical definition, and then measure three things per step and species: is the
term sound, do the genes that carry out the step have it, and is there a
GO-CAM. The baseline below shows where the gaps are: none of the 44 step-level
terms has a logical definition, human has zero annotations to `apoptosome
assembly`, and no production GO-CAM contains APAF1, CYCS, or any fly or worm
apoptosis gene.

## What phase 1 left us

| Asset | State on 2026-11-23 |
|---|---|
| Gene reviews | Human core machinery (32 genes), a mouse slice (7), worm `ced-3`/`ced-4`/`ced-9`/`egl-1`/`cep-1`, ten fly genes, yeast MCA1/NUC1/IRE1 and a Trichoderma IRE1. No zebrafish or frog reviews. |
| Modules | `intrinsic_apoptotic_signaling`, `death_receptor_apoptotic_signaling`, `trail_apoptotic_signaling`, `bcl2_family_momp_control`, `apoptotic_execution_phase`, `c_elegans_core_apoptosis`, `dmel_rhg_apoptosome_caspase_activation`, all `DRAFT`. Neighbours: `necroptosis`, `ferroptosis`, `phagocytic_engulfment`, three efferocytosis modules. |
| Broad-term audit | Exact `GO:0006915` snapshot for human, mouse and zebrafish ([GO0006915](GO0006915.md)) and the [assay-readout over-annotation](ASSAY_READOUT_OVERANNOTATION.md) notes. |

The modules are organized by pathway and by species. They do not share step
identifiers, so nothing currently says that the worm CED-4 octamer and the
human APAF1 heptamer are the same step with different carriers.

## Baseline measurements

### Ontology (go.obo release 2026-07-26)

- `GO:0006915` apoptotic process has 115 `is_a`/`part_of` descendants and a
  further 232 terms that regulate them.
- All 232 regulation terms have logical definitions. Of the 115 process terms
  they are built on, 19 do in go.obo. The 24 signaling-pathway terms have none,
  and 7 of 13 execution and step terms have one.
- 63 of the 115 are cell-type or context terms (`neuron apoptotic process` and
  similar). Their logical definitions use the Cell Ontology and sit in go-plus,
  which was not checked here, so the count of 11 defined is a lower bound.
- 16 of the 24 signaling terms precompose a pathway with a stimulus, mediator
  or receptor class (`in response to DNA damage`, `hypoxia`, `nitrosative
  stress`, `by p53 class mediator`, `via death domain receptors`), and some
  stack two, such as `neuron intrinsic apoptotic signaling pathway in response
  to hydrogen peroxide`. They have 24 regulation terms of their own.
- Four molecular-function terms precompose an activity with the process:
  `GO:0016505`, `GO:0008656`, `GO:0043027`, `GO:0043028`. The three sibling
  caspase-activity terms of this kind have already been obsoleted, as have the
  `activation of cysteine-type endopeptidase activity involved in ...` process
  terms.
- 13 cellular-component terms name pairwise BCL2-family complexes
  (`GO:0097137` BAD-BCL-xl complex through `GO:0097148`, and `GO:1990346`).
- `GO:0097345` mitochondrial outer membrane permeabilization is classified as
  a `positive regulation of mitochondrial membrane permeability involved in
  apoptotic process`, so the event itself is typed as a regulation term.
- `GO:0097194` execution phase of apoptosis has two `part_of` children and one
  `has_part`. Effector-caspase activation has no process term since the
  obsoletions above.

### Annotation rows per step and species

QuickGO, 2026-11-23, from [step_coverage.py](step_coverage.py). Each cell is
experimental rows / all rows, counting the term and its descendants. These are
annotation rows, not genes, and one gene can contribute many. The last row is
the positive control: its human, mouse and zebrafish totals match the September
snapshot exactly.

| Step term | human | mouse | rat | zebrafish | frog | fly | worm | budding yeast | fission yeast | Dictyostelium | Arabidopsis |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GO:0006915` apoptotic process | 414/1975 | 850/2461 | 116/1922 | 128/545 | 0/267 | 171/330 | 149/199 | 32/34 | 0/0 | 1/14 | 0/0 |
| `GO:0097193` intrinsic signaling | 100/350 | 169/513 | 7/405 | 61/124 | 0/46 | 37/48 | 26/30 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0097191` extrinsic signaling | 76/218 | 119/374 | 8/247 | 0/27 | 0/19 | 0/1 | 0/1 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0071550` DISC assembly | 1/5 | 1/3 | 0/4 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0097345` MOMP | 6/39 | 2/18 | 0/13 | 0/5 | 0/3 | 0/1 | 0/1 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0001836` cytochrome c release | 15/54 | 20/77 | 7/55 | 0/14 | 0/11 | 0/0 | 0/1 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0097314` apoptosome assembly | 0/0 | 2/2 | 0/2 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0097194` execution phase | 36/109 | 35/148 | 6/119 | 0/28 | 0/17 | 4/36 | 49/57 | 2/3 | 0/0 | 0/13 | 0/0 |
| `GO:0006309` apoptotic DNA fragmentation | 6/38 | 5/37 | 2/30 | 0/10 | 0/8 | 1/26 | 35/40 | 2/3 | 0/0 | 0/13 | 0/0 |
| `GO:0070782` phosphatidylserine exposure | 2/11 | 10/22 | 0/19 | 0/10 | 0/4 | 0/2 | 5/6 | 0/0 | 0/0 | 0/0 | 0/0 |
| `GO:0043277` apoptotic cell clearance | 22/86 | 54/122 | 1/87 | 24/38 | 0/11 | 20/29 | 95/99 | 0/0 | 0/0 | 0/4 | 0/0 |
| `GO:0006915` exact term only | 87/825 | 130/557 | 7/425 | 22/253 | 0/124 | 90/181 | 34/62 | 30/30 | 0/0 | 0/0 | 0/0 |

What this says:

- **Step terms are almost unused.** `apoptosome assembly` has no human row
  although APAF1, CYCS and CASP9 are reviewed and the mechanism is textbook.
  DISC assembly has five human rows. Most of the mechanism is annotated to the
  pathway terms or to the root.
- **The assembly steps are empty outside mammals.** Fly Dark/Dronc and worm
  CED-4/CED-3 form apoptosomes and carry no assembly annotation.
- **Single rows in the wrong lineage are leads, not findings.** One MOMP row and
  one extrinsic-signaling row in each of fly and worm, and one cytochrome c
  release row in worm, are probably propagation from vertebrate wiring. Phase 1
  already removed such a row from `ced-9`.
- **Frog has no experimental row at all** and rat is nearly all transferred, so
  for those two the question is propagation quality, not literature curation.
- **Budding yeast has 30 experimental rows on the root term** and none on any
  step. That is the fungal programmed-cell-death boundary question.

### GO-CAMs (`gocams/index.tsv`, 2,037 cached models)

- 27 models have an activity whose process is an apoptosis term: 24 human, 3
  mouse, none in any other species. The cache holds 116 fly and 4 worm models,
  and none of them contains a core apoptosis gene.
- Gene coverage is uneven. CASP3 is in 11 models, CASP8 in 10, TP53 in 10.
  BAX, BAK1, BID, FAS, FASLG, CASP6 and CASP10 are in one each. APAF1, CYCS,
  BCL2L1, MCL1, BCL2L11, BBC3, PMAIP1, BAD, DIABLO, DFFA, DFFB, ENDOG, AIFM1
  and HTRA2 are in none. Phosphatidylserine exposure is covered by three
  models, for XKR4, XKR8 and XKR9.
- So the extrinsic arm is modelled (FASL-FAS, TRAIL-R1, TRAIL-R2, mouse TNFR1)
  and the intrinsic core, from BH3-only proteins through the apoptosome, is not
  modelled in any species.
- The repository can read a module as logic (`module_logic.py`) and align
  modules to models (`gocam_module_bridges.py`). It has no code that writes a
  GO-CAM from a module.

## The step spine

One abstract list of steps, each with a GO anchor and a set of carriers per
lineage. Lineage entries marked "none" are claims to verify in the audit, and
where they hold they become proposed taxon constraints.

| # | Step | GO anchor | Vertebrate carriers | Fly | Worm |
|---|---|---|---|---|---|
| 1 | Death ligand binds death receptor | `GO:0008625`; `GO:0005035` death receptor activity | FASLG-FAS, TNFSF10-TNFRSF10A/B, TNF-TNFRSF1A | none expected for a DISC route | none |
| 2 | DISC assembly | `GO:0071550`; complex `GO:0031264` | FADD, CASP8, CASP10, CFLAR | none expected | none |
| 3 | Initiator caspase-8 activation and BID cleavage | no process term | CASP8, CASP10, BID | none expected | none |
| 4 | BH3-only sensing and release of BCL2 restraint | no process or function term | BCL2L11, BBC3, PMAIP1, BID on BCL2, BCL2L1, MCL1 | Debcl and Buffy, role limited | EGL-1 on CED-9 |
| 5 | MOMP | `GO:0097345` | BAX, BAK1 | not required | none: CED-9 releases CED-4 directly |
| 6 | Cytochrome c and SMAC release | `GO:0001836` | CYCS, DIABLO, HTRA2 | to verify | none |
| 7 | Apoptosome assembly and initiator caspase activation | `GO:0097314`; complex `GO:0043293` | APAF1, CYCS, CASP9 | Dark, Dronc | CED-4, CED-3 |
| 8 | IAP restraint and its antagonism | no function term for the antagonist | XIAP against DIABLO and HTRA2 | Diap1 against Rpr, Hid, Grim, Skl | none known |
| 9 | Effector caspase activation and substrate cleavage | `GO:0097194` | CASP3, CASP7, CASP6 | DrICE, Dcp-1 | CED-3, which is initiator and effector |
| 10 | Apoptotic DNA fragmentation | `GO:0006309` | DFFB released from DFFA; ENDOG | to assign | to assign |
| 11 | Phosphatidylserine exposure | `GO:0070782` | XKR8 family | to assign | to assign |
| 12 | Handoff to clearance | `GO:0043277` | out of scope: existing engulfment and efferocytosis modules | | |

Steps 1 to 3 are a vertebrate route into the shared core at step 4 or step 9.
Steps 4 to 6 are a route that worms skip. That is the structure the module
schema already has words for: a `ROUTE` variant set for how initiator caspase
activation is reached, and `REALIZER` variant sets on a taxon axis for who
carries each step.

## Workstreams

### A. Ontology refactoring

Output: `projects/APOPTOSIS/ontology_changes.yaml`, one entry per requested
change with the evidence and the annotation count it affects, exported through
`export-ontology-changes`. Obsoletion requests that need their own annotation
review get a sub-page here and the `OBSOLETION` tag.

1. **Logical definitions for the step terms.** The two assembly terms are
   mechanical (`results in assembly of` the apoptosome or the DISC). MOMP,
   cytochrome c release, DNA fragmentation and phosphatidylserine exposure need
   a genus and a participant or location. The definitions are what the GO-CAM
   projection in workstream D reads, so they are written first.
2. **MOMP placement.** Decide whether the event should stay under a regulation
   term or become a membrane permeabilization process that is `part_of`
   intrinsic signaling.
3. **Stimulus precompositions.** For the 16 precomposed signaling terms and
   their 24 regulation terms: count
   annotations per term, then propose either a logical definition (pathway
   `part_of` the response) or a merge into the parent with the stimulus carried
   by the response term. This follows `projects/INVOLVED_IN_PRECOMPOSITION.md`.
4. **Cell-type terms.** Check the go-plus definitions for the 63 process terms
   and 133 regulation terms, and count annotations. Phase 1 found these mostly
   record where a phenotype was scored. Propose retirement only where a count
   and a sample of reviewed rows support it.
5. **Function terms precomposed with the process.** Review the four listed
   above against their unqualified parents, as GO already did for the caspase
   activity terms.
6. **Pairwise BCL2-family complex terms.** Count usage of the 13 terms and ask
   whether `GO:0097136` Bcl-2 family protein complex is enough.
7. **Missing terms.** Phase 1 reviews already propose a BH3-only activator and
   sensitizer function, an IAP antagonist function, a CASP8 inhibitor term and
   an apoptosome-related assertion. Collect them with `export-proposed-terms`
   and deduplicate into one request set, plus a process term for step 3 if the
   audit shows it is needed.
8. **Taxon constraints.** Where the audit confirms a "none" cell in the spine,
   add an entry to `TAXON_PATHWAY_VARIANCE/proposed_taxon_constraints.yaml`.
9. **The fungal boundary.** Decide, from the 30 yeast rows and the MCA1 and
   NUC1 reviews, whether yeast programmed cell death belongs under `GO:0006915`
   as defined. This is a question for GO editors, recorded as such.

### B. Standard annotation completeness

Output: a gene-level step-by-species matrix in YAML, regenerated by script,
with every gap classified.

1. Replace the row counts above with a gene-level table: for each step and
   species, the carrier genes from the spine and whether each has the step term,
   by what evidence, or only an ancestor.
2. Classify each gap as one of four things. **Curation gap**: literature exists,
   so propose the row in the gene review as `NEW`, after the participation test
   and comparator check in `CLAUDE.md`. **Propagation gap**: the family review
   requests a PAINT change at a named node. **Granularity gap**: the gene has
   the pathway term and the review already says `MODIFY` to the step term.
   **True absence**: the lineage lacks the step, which feeds A8.
3. Species tiers. Tier 1 is human, mouse, fly and worm, where machinery is
   reviewed and gaps can be closed from existing reviews. Tier 2 is zebrafish,
   rat and frog, where there are no reviews and the work is about 35 orthologs
   per species plus a propagation audit. Tier 3 is budding and fission yeast,
   Dictyostelium and Arabidopsis, where the expected result is near-empty and
   each existing row is audited.
4. Family reviews for the families that carry the propagation: caspases, the
   BCL2 family, APAF1/CED-4, IAPs and death-domain adaptors. Phase 1 flagged
   several PAINT transfers gene by gene; the node-level fix belongs here.

### C. GO-CAMs across species

Output: `GoCamReview` files for existing models, and reviewed model drafts for
the steps and species that have none.

1. Review the existing models that touch the spine, about a dozen of the 27,
   and record `gocam_associations` on the modules.
2. Draft the missing models, in this order: human intrinsic core (steps 4 to
   7 and 9), human execution and DNA fragmentation (9 to 11), worm core, fly
   RHG-Diap1-Dark-Dronc, then mouse and zebrafish by projection.
3. Drafts stay in this repository as candidates. Whether and how they go to
   Noctua is an open decision below.

### D. Projection from axiomatized steps

Output: one abstract `apoptosis_core` module that the per-pathway and
per-species modules realize, and an exporter that turns a realization into a
GO-CAM draft.

1. Restructure the modules around the spine. The seven existing modules keep
   their content and become realizations of shared step identifiers.
2. Write the exporter. For a chosen taxon it resolves each variant set, emits
   one activity per carrier with the step's function, process and location, and
   takes causal edges from module connections. Every activity carries the
   review or publication it rests on.
3. Projection rule: emit an activity only when the carrier in that species has
   a reviewed core function for it, or an IBA whose node passed family review.
   Anything else is a reported gap, which is the same gap list as workstream B.
4. Pilot on step 7. It has one clean logical definition and three lineage
   realizations, and no existing GO-CAM in any species to disagree with. Then
   test the exporter against the FASL-FAS and TRAIL models, where a production
   model exists to compare with.

## Order of work

1. **Spine and definitions**: agree the step list, draft the logical
   definitions (A1, A2), build the gene-level matrix (B1). No gene edits.
2. **Pilot**: step 7 end to end: definition, annotation gaps closed in human,
   mouse, fly and worm, module restructured, exporter, three GO-CAM drafts.
3. **Widen**: remaining steps for tier 1, family reviews, the term-request
   set, GoCamReviews of existing models.
4. **Tier 2 and 3 species**, and the stimulus and cell-type term proposals.

Each stage is a small number of PRs that touch disjoint files, which keeps
within the six-workstream limit.

## Out of scope

- Necroptosis, pyroptosis and ferroptosis, which have their own modules. The
  CASP8-RIPK1 switch is recorded as an interface only.
- Engulfment and efferocytosis downstream of step 11.
- The long tail of `regulation of apoptotic process` on survival kinases and
  transcription factors. Phase 1's assay-readout rubric covers it and it has no
  step in the spine.
- Non-apoptotic caspase functions.

## Decisions needed

1. **Spine granularity.** Twelve steps as listed, or fewer and coarser?
2. **How bold on the ontology.** Add definitions and request missing terms
   only, or also propose merging the stimulus and cell-type precompositions?
3. **GO-CAM destination.** Keep drafts here as review material, or aim for
   import into Noctua, which sets a higher bar for evidence on each activity?
4. **Tier 2 species.** Is zebrafish the priority after tier 1, and are rat and
   frog worth more than a propagation audit?
5. **The fungal boundary.** In scope as an ontology question, or left alone?
