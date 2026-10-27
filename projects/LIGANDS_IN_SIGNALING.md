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
  - IL34
  - IL21
  - IL22
  - FASLG
  - CXCL8
  - C5
  - C3
  - TSHB
  - CGA
  - GRP
  - NMB
  - COL1A1
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
  [script](LIGANDS_IN_SIGNALING/scripts/survey/ligand_pathway_survey.py)). 23 of 24 human
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

All fourteen modules have family-grounded pan-species ligand steps and pass the schema and module
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
  (`PANTHER:PTHR11574` `KIT LIGAND`, PAINT node `PTN002611905`, *cytokine activity*
  `GO:0005125`) with representative members in human (`KITLG`) and zebrafish (`kitlga`; the
  `PTHR11574` family review also covers mouse `Kitlg` and zebrafish `kitlgb`). GOA gaps resolved
  in gene reviews: human `KITLG` and zebrafish `kitlga` lacked `GO:0038109` *Kit signaling
  pathway* (added as `NEW` in both reviews).
- **[Ephrin-Eph signaling](../modules/ephrin_receptor_signaling.yaml)** (*ephrin receptor
  signaling pathway*, `GO:0048013`). Upgraded the ligand step (`efnb2_efnb2_ligand`) from a
  single-gene `ENTITY` using *ephrin receptor binding* (`GO:0046875`) to `FAMILY`
  (`PANTHER:PTHR11304` `EPHRIN`, PAINT node `PTN000885159`, *receptor ligand activity*
  `GO:0048018`) with representative members on the module step for human (`EFNB2`, `EFNB1`) and
  zebrafish (`efnb2a`), while the `PTHR11304` family review spans GPI-anchored ephrin-A
  (`EFNA1`–`EFNA5`), transmembrane ephrin-B (`EFNB1`–`EFNB3`), *C. elegans* (`efn-4`), and
  *Drosophila* (`Ephrin`). The validator's `PAINT_TERM_NOT_ASSERTED` warning on `PTN000885159`
  (`GO:0048018` vs PAINT's `GO:0046875`) is intentional per Decision 2 and documented in
  `interpro/panther/PTHR11304/PTHR11304-review.yaml`.
- **[MIF-CD74 signaling](../modules/mif_signaling.yaml)** (*macrophage migration inhibitory
  factor signaling pathway*, `GO:0035691`). Two-step pan-species module. Ligand: MIF /
  D-dopachrome tautomerase family (`PANTHER:PTHR11954`, PAINT nodes `PTN000237513` and
  `PTN000237510`), *cytokine activity* (`GO:0005125`, a child of *receptor ligand activity*
  `GO:0048018`). Receptor: CD74 subfamily (`PANTHER:PTHR14093:SF17`, PAINT node `PTN002679661`),
  *cytokine receptor activity* (`GO:0004896`). GOA gap resolved in the new human `MIF` gene
  review: in GOA only the receptor `CD74` carried `GO:0035691`, while human `MIF` carried
  `GO:0005125` *cytokine activity* and the parent term `GO:0007166` *cell surface receptor
  signaling pathway* (`IDA`, `PMID:12782713`), which is refined via `MODIFY` to `GO:0035691`
  *macrophage migration inhibitory factor signaling pathway*.
- **[IL-34-CSF1R signaling](../modules/il34_signaling.yaml)** (*interleukin-34-mediated signaling
  pathway*, `GO:0061514`, and sibling *macrophage colony-stimulating factor signaling pathway*,
  `GO:0038145`). Three-step pan-species module. Ligand: IL-34 family (`PANTHER:PTHR28606`, PAINT
  node `PTN002823014`), *cytokine activity* (`GO:0005125`). Receptor: CSF1R subfamily
  (`PANTHER:PTHR24416:SF47`, PAINT nodes `PTN001230349` and `PTN002814394`), *macrophage
  colony-stimulating factor receptor activity* (`GO:0005011`). GOA Category C gap resolved in the
  new human `IL34` gene review: in GOA `IL34` was annotated to `GO:0038145` (`IBA`, modified to
  `GO:0061514`) and `GO:0061514` (`IDA`), while its only MF terms were `GO:0005157` (*macrophage
  colony-stimulating factor receptor binding*, `IBA`/`IDA`/`IMP`) and `GO:0005515` (*protein
  binding*, `IPI`); `GO:0005157` is modified to `GO:0005125` (*cytokine activity*) per Decision 2.
- **[IL-21 signaling](../modules/il21_signaling.yaml)** (*interleukin-21-mediated signaling
  pathway*, `GO:0038114`). Three-step pan-species module. Ligand: IL-21 subfamily
  (`PANTHER:PTHR14356:SF2`, within `PANTHER:PTHR14356` `INTERLEUKIN-15-RELATED`, PAINT nodes
  `PTN002682898` and `PTN007637558`), *cytokine activity* (`GO:0005125`). Receptor: IL21R
  subfamily (`PANTHER:PTHR23037:SF7`, PAINT node `PTN000547990`) paired with the common gamma
  chain (`IL2RG`, `PANTHER:PTHR23037:SF47`, PAINT nodes `PTN002745476` and `PTN008588077`),
  *cytokine receptor activity* (`GO:0004896`). GOA Category A gap resolved in the human `IL21`
  gene review: `IL21` lacked `GO:0038114` and carried `GO:0007165` (*signal transduction*, `NAS`,
  refined via `MODIFY` to `GO:0038114`) alongside `GO:0007259` (*cell surface receptor signaling
  pathway via JAK-STAT*, `NAS`, `ACCEPT`), and its receptor-binding annotations (`GO:0005126`,
  `GO:0005134`) are modified to `GO:0005125` (*cytokine activity*).
- **[IL-22 signaling](../modules/il22_signaling.yaml)** (*interleukin-22-mediated signaling
  pathway*, `GO:0140865`). Three-step pan-species module. Ligand: IL-22 family (`PANTHER:PTHR48488`,
  PAINT node `PTN009232695`), *cytokine activity* (`GO:0005125`). Receptor: IL22RA1 subfamily
  (`PANTHER:PTHR20859:SF53`, PAINT node `PTN000466212`) paired with the shared `IL10RB` beta
  chain (`PANTHER:PTHR20859:SF50`), *cytokine receptor activity* (`GO:0004896`), alongside
  extracellular decoy antagonism by soluble `IL22RA2` (`PANTHER:PTHR20859:SF51`). GOA Category A
  gap resolved in the human `IL22` gene review: `IL22` lacked `GO:0140865` and carried only
  `GO:0007165` (*signal transduction*, `IEA`), refined via `MODIFY` to `GO:0140865` (with `NEW`
  `GO:0007259` *cell surface receptor signaling pathway via JAK-STAT* retained alongside it), and
  `GO:0045518` (*interleukin-22 receptor binding*, `NAS`) is modified to `GO:0005125` (*cytokine
  activity*).
- **[Death receptor / Fas signaling](../modules/death_receptor_apoptotic_signaling.yaml)** (*Fas
  signaling pathway*, `GO:0036337`, and *extrinsic apoptotic signaling pathway via death domain
  receptors*, `GO:0008625`). Upgraded all steps from single-gene `ENTITY` selectors to `FAMILY`
  selectors. Ligand: Fas ligand subfamily (`PANTHER:PTHR11471:SF33`, within `PANTHER:PTHR11471`
  `TUMOR NECROSIS FACTOR FAMILY MEMBER`, PAINT node `PTN000895255`), *cytokine activity*
  (`GO:0005125`). Receptor: FAS (`PANTHER:PTHR46874:SF1`) and DISC adaptor FADD (`PANTHER:PTHR15077:SF10`).
  GOA Category A gap resolved in the human `FASLG` gene review: `FASLG` carried `GO:0008625`
  (*extrinsic apoptotic signaling pathway via death domain receptors*) and `GO:0005125` (*cytokine
  activity*) but lacked `GO:0036337` (*Fas signaling pathway*), added as `NEW` (`PMID:7826947`).
- **[Chemokine / Interleukin-8 signaling](../modules/chemokine_signaling.yaml)**
  (*chemokine-mediated signaling pathway*, `GO:0070098`, and *interleukin-8-mediated signaling
  pathway*, `GO:0038112`). Upgraded all steps from single-gene `ENTITY` selectors to `FAMILY`
  selectors. Ligand: Interleukin-8 subfamily (`PANTHER:PTHR12015:SF200`, within `PANTHER:PTHR12015`
  `SMALL INDUCIBLE CYTOKINE A`, PAINT node `PTN002564680`), *chemokine activity* (`GO:0008009`).
  Receptor: CXCR2 (`PANTHER:PTHR10489:SF689`, PAINT nodes `PTN001628461` and `PTN002573743`) and
  CCR5 (`PANTHER:PTHR10489:SF686`, PAINT node `PTN001628461`). In the new human `CXCL8` gene
  review, `CXCL8` already carries `GO:0038112` (*interleukin-8-mediated signaling pathway*, `IDA`,
  `PMID:8399143`) and `GO:0008009` (*chemokine activity*) in GOA, both of which are `ACCEPT`ed;
  broader or sibling signaling rows (`GO:0007165`, `GO:0007186`, `GO:0035556`, `GO:0019722`) are
  refined via `MODIFY` to `GO:0038112`, `GO:0005125` (*cytokine activity*) is modified to
  `GO:0008009` (*chemokine activity*), and `GO:0005153` (*interleukin-8 receptor binding*) is
  `ACCEPT`ed (with `GO:0045236` *CXCR chemokine receptor binding* modified to `GO:0005153`).
- **[Complement component C5a signaling](../modules/c5a_signaling.yaml)** (*complement component
  C5a signaling pathway*, `GO:0038178`). Three-step pan-species module. Ligand: Complement C5
  subfamily (`PANTHER:PTHR11412:SF83`, within `PANTHER:PTHR11412` `MACROGLOBULIN / COMPLEMENT`,
  PAINT node `PTN002605305`), *signaling receptor binding* (`GO:0005102`). Receptors: C5AR1
  (`PANTHER:PTHR24225:SF29`) and C5AR2 (`PANTHER:PTHR24225:SF1`), *complement receptor activity*
  (`GO:0004875`). GOA Category A gap resolved in the new human `C5` gene review: `C5` lacked
  `GO:0038178` in GOA (added via `NEW` with `PMID:36806352` and `MODIFY` on `GO:0007166`
  `PMID:10820279` and `GO:0007186` `PMID:8898085`), `GO:0001664` (*G protein-coupled receptor
  binding*) is `ACCEPT`ed as the core MF (with `GO:0005102` modified to `GO:0001664`), while the
  mis-curated `PINC` `TAS` `GO:0008009` (*chemokine activity*, `PMID:10820279`) and InterPro2GO
  `IEA` `GO:0004866` (*endopeptidase inhibitor activity*, also over-propagated at PAINT node
  `PTN000892454`) are removed (`REMOVE`, with `source_defects` on `GO:0008009`).
- **[Thyroid-stimulating hormone (TSH) signaling](../modules/tsh_signaling.yaml)** (*thyroid-stimulating
  hormone signaling pathway*, `GO:0038194`). Two-step pan-species module. Ligand: TSH
  heterodimer composed of TSHB (`PANTHER:PTHR11515:SF5`, within `PANTHER:PTHR11515` `GLYCOPROTEIN
  HORMONE BETA CHAIN`, PAINT node `PTN000162063`) and CGA (`PANTHER:PTHR11509:SF0`, within
  `PANTHER:PTHR11509` `GLYCOPROTEIN HORMONES ALPHA CHAIN`, PAINT node `PTN002608947`), *hormone
  activity* (`GO:0005179`) and *signaling receptor binding* (`GO:0005102`). Receptor: TSHR
  (`PANTHER:PTHR24372:SF0`), *thyroid-stimulating hormone receptor activity* (`GO:0004996`). GOA
  Category A gap resolved in the new human `TSHB` and `CGA` gene reviews (`NEW` `GO:0038194` on
  both subunits and `MODIFY` on `GO:0007186` → `GO:0038194` on `TSHB`).
- **[Bombesin receptor signaling](../modules/bombesin_receptor_signaling.yaml)** (*bombesin receptor
  signaling pathway*, `GO:0031989`). Two-step pan-species module. Ligands: GRP
  (`PANTHER:PTHR16866:SF2`) and NMB (`PANTHER:PTHR16866:SF3`, within `PANTHER:PTHR16866`
  `GASTRIN-RELEASING PEPTIDE`, PAINT node `PTN008565241`), *bombesin receptor binding*
  (`GO:0031853`), *neuromedin B receptor binding* (`GO:0031710`), and *neuropeptide hormone
  activity* (`GO:0005184`). Receptors: GRPR (`PANTHER:PTHR45695:SF7`), NMBR
  (`PANTHER:PTHR45695:SF8`), and BRS3 (`PANTHER:PTHR45695:SF6`), *bombesin receptor activity*
  (`GO:0004946`). GOA Category A gap resolved in the new human `GRP` and `NMB` gene reviews (`NEW`
  `GO:0031989` on both genes, plus `MODIFY` on `GO:0007218` → `GO:0031989`).
- **[Collagen-DDR receptor tyrosine kinase signaling](../modules/collagen_ddr_signaling.yaml)**
  (*collagen-activated tyrosine kinase receptor signaling pathway*, `GO:0038063`). Two-step
  pan-species module. Ligands: fibrillar and basement-membrane collagen triple-helical chains
  including COL1A1 (`PANTHER:PTHR24023:SF1082`), COL1A2 (`PANTHER:PTHR24023:SF568`), COL2A1
  (`PANTHER:PTHR24023:SF58`), COL3A1 (`PANTHER:PTHR24023:SF604`), and COL4A1
  (`PANTHER:PTHR24023:SF854`, within `PANTHER:PTHR24023` `COLLAGEN ALPHA`), *receptor ligand
  activity* (`GO:0048018`). Receptors: DDR1 (`PANTHER:PTHR24416:SF333`) and DDR2
  (`PANTHER:PTHR24416:SF295`), *protein tyrosine kinase collagen receptor activity* (`GO:0038062`)
  and *collagen binding* (`GO:0005518`). GOA Category C gap resolved in the updated human `COL1A1`
  gene review (`NEW` `IC` annotations for `GO:0048018` and `GO:0038063` backed by
  `Reactome:R-HSA-2327738` and `Reactome:R-HSA-2465890`).

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
  created the full human `MIF` review (`genes/human/MIF/MIF-ai-review.yaml`) with `MODIFY` on
  `GO:0007166` (*cell surface receptor signaling pathway*) → `GO:0035691` (*macrophage migration
  inhibitory factor signaling pathway*) and `MODIFY` on `GO:0005126` (*cytokine receptor
  binding*) → `GO:0005125` (*cytokine activity*).
- **IL34, IL21, and IL22 gene reviews:** created the human `IL34` review
  (`genes/human/IL34/IL34-ai-review.yaml`), modifying `GO:0005157` (*macrophage colony-stimulating
  factor receptor binding*) to `GO:0005125` (*cytokine activity*) and `GO:0038145` (*macrophage
  colony-stimulating factor signaling pathway*) to `GO:0061514` (*interleukin-34-mediated signaling
  pathway*), and accepting `GO:0061514`; updated `genes/human/IL21/IL21-ai-review.yaml` to modify
  `GO:0007165` (*signal transduction*) to `GO:0038114` (*interleukin-21-mediated signaling
  pathway*), retain `GO:0007259` (*cell surface receptor signaling pathway via JAK-STAT*) as
  `ACCEPT`, and modify receptor-binding rows (`GO:0005126`, `GO:0005134`) to `GO:0005125`
  (*cytokine activity*); and updated `genes/human/IL22/IL22-ai-review.yaml` to modify `GO:0007165`
  (*signal transduction*) to `GO:0140865` (*interleukin-22-mediated signaling pathway*), retain
  `NEW` `GO:0007259` (*cell surface receptor signaling pathway via JAK-STAT*), and modify
  `GO:0045518` (*interleukin-22 receptor binding*) to `GO:0005125` (*cytokine activity*).
- **FASLG, CXCL8, and C5 gene reviews:** updated `genes/human/FASLG/FASLG-ai-review.yaml` to add
  `NEW` `GO:0036337` (*Fas signaling pathway*, `PMID:7826947`) alongside existing `GO:0008625`
  (*extrinsic apoptotic signaling pathway via death domain receptors*), `GO:0005125` (*cytokine
  activity*), and `GO:0005123` (*death receptor binding*); created the full human `CXCL8` review
  (`genes/human/CXCL8/CXCL8-ai-review.yaml`), accepting `GO:0038112` (*interleukin-8-mediated
  signaling pathway*, `IDA`, `PMID:8399143`), `GO:0008009` (*chemokine activity*), and `GO:0005153`
  (*interleukin-8 receptor binding*), modifying broader/sibling signaling terms (`GO:0007165`,
  `GO:0007186`, `GO:0035556`, `GO:0019722`) to `GO:0038112`, modifying `GO:0005125` (*cytokine
  activity*) to `GO:0008009`, modifying `GO:0045236` (*CXCR chemokine receptor binding*) to
  `GO:0005153`, and removing mis-keyed `GO:0016020` (*membrane*, `PMID:25411203`, with
  `source_defects`); and created the full human `C5` review (`genes/human/C5/C5-ai-review.yaml`),
  adding `NEW` `GO:0038178` (*complement component C5a signaling pathway*, `PMID:36806352`),
  modifying `GO:0007166` (`PMID:10820279`) and `GO:0007186` (`PMID:8898085`) to `GO:0038178`,
  accepting `GO:0001664` (*G protein-coupled receptor binding*) as core MF (and modifying
  `GO:0005102` to `GO:0001664`), and removing (`REMOVE`) both the mis-curated `PINC` `TAS`
  `GO:0008009` (*chemokine activity*, `PMID:10820279`, with `source_defects`) and the InterPro2GO
  `IEA` `GO:0004866` (*endopeptidase inhibitor activity*).
- **C3, TSHB, CGA, GRP, NMB, and COL1A1 gene reviews (Tranche 4B):** updated human `C3`
  (`genes/human/C3/C3-ai-review.yaml`) to change all four UniProt `IDA` `GO:0008009` (*chemokine
  activity*) rows (`PMID:342601`, `PMID:5778786`, `PMID:37169960`, `PMID:37852260`) from `ACCEPT`
  to `REMOVE` with `source_defects` (`WRONG_TERM` → `GO:0001664`), matching `C5` and
  `PTHR11412-review.yaml`; created the full human `TSHB` (`genes/human/TSHB/TSHB-ai-review.yaml`)
  and `CGA` (`genes/human/CGA/CGA-ai-review.yaml`) reviews for `GO:0038194` (*thyroid-stimulating
  hormone signaling pathway*); created the full human `GRP` (`genes/human/GRP/GRP-ai-review.yaml`)
  and `NMB` (`genes/human/NMB/NMB-ai-review.yaml`) reviews for `GO:0031989` (*bombesin receptor
  signaling pathway*); and updated human `COL1A1` (`genes/human/COL1A1/COL1A1-ai-review.yaml`) to
  add `NEW` `IC` annotations and a second `core_functions` entry for `GO:0048018` (*receptor
  ligand activity*) and `GO:0038063` (*collagen-activated tyrosine kinase receptor signaling
  pathway*).
- **PANTHER family reviews** (`PTHR45836`, `PTHR11574`, `PTHR11304`, `PTHR11954`, `PTHR28606`,
  `PTHR14356`, `PTHR48488`, `PTHR11471`, `PTHR12015`, `PTHR11412`, `PTHR11515`, `PTHR11509`,
  `PTHR16866`, `PTHR24023`):
  - `interpro/panther/PTHR45836/PTHR45836-review.yaml`: the `PTN002911633` assessment notes that
    its IBD should use the ligand-activity term; a new `SUBFAMILY_ONLY` assessment of
    *chemorepellent activity* covers the four Slit subfamilies.
  - `interpro/panther/PTHR11574/PTHR11574-review.yaml`: `SOUND` node assessments for
    `PTN002611905` (`GO:0005125` *cytokine activity*, `GO:0005576` *extracellular region*,
    `GO:0005886` *plasma membrane*, `GO:0008284` *positive regulation of cell population
    proliferation*) and `FAMILY_WIDE` term assessments including `GO:0005125` (*cytokine
    activity*) and `GO:0038109` (*Kit signaling pathway*).
  - `interpro/panther/PTHR11304/PTHR11304-review.yaml`: `SOUND` node assessments on
    `PTN000885159` (`GO:0046875` *ephrin receptor binding*, `GO:0048013` *ephrin receptor
    signaling pathway*, `GO:0005886` *plasma membrane*, `GO:0007411` *axon guidance*), noting
    in `assessment_reason` that PAINT should also assert `GO:0048018` (*receptor ligand
    activity*) at `PTN000885159`, together with `FAMILY_WIDE` term assessments for `GO:0048018`
    and `GO:0048013`.
  - `interpro/panther/PTHR11954/PTHR11954-review.yaml`: `SOUND` node assessments on
    `PTN000237510` (`GO:0005576` *extracellular region*, `GO:0050178` *phenylpyruvate
    tautomerase activity*) and `PTN000237513` (`GO:0005125` *cytokine activity*), noting in
    `assessment_reason` and the `FAMILY_WIDE` term assessment for `GO:0035691` (*macrophage
    migration inhibitory factor signaling pathway*) that PAINT should also place `GO:0035691` at
    `PTN000237513`.
  - `interpro/panther/PTHR28606/PTHR28606-review.yaml`: `SOUND` node assessments on
    `PTN002823014` (`GO:0005576` *extracellular region*, `GO:0005157` *macrophage
    colony-stimulating factor receptor binding*, `GO:0008284` *positive regulation of cell
    population proliferation*, `GO:0045651` *positive regulation of macrophage differentiation*,
    `GO:0045657` *positive regulation of monocyte differentiation*), noting in `assessment_reason`
    and the `FAMILY_WIDE` term assessments for `GO:0005125` (*cytokine activity*) and `GO:0061514`
    (*interleukin-34-mediated signaling pathway*) that PAINT should also place `GO:0005125` and
    `GO:0061514` at `PTN002823014`.
  - `interpro/panther/PTHR14356/PTHR14356-review.yaml`: `SOUND` node assessments on
    `PTN002682898` (`GO:0001819` *positive regulation of cytokine production*, `GO:0050778`
    *positive regulation of immune response*) and `PTN007637558` (`GO:0045954` *positive
    regulation of natural killer cell mediated cytotoxicity*), `FAMILY_WIDE` term assessment for
    `GO:0005125` (*cytokine activity*) across IL-21 (`PTHR14356:SF2`) and IL-15 (`PTHR14356:SF3`)
    subfamilies, and `SUBFAMILY_ONLY` term assessments for `GO:0038114` (*interleukin-21-mediated
    signaling pathway* on `PANTHER:PTHR14356:SF2`) and `GO:0035723` (*interleukin-15-mediated
    signaling pathway* on `PANTHER:PTHR14356:SF3`).
  - `interpro/panther/PTHR48488/PTHR48488-review.yaml`: `SOUND` node assessments on
    `PTN009232695` (`GO:0005125` *cytokine activity*, `GO:0005576` *extracellular region*) and
    `SCOPE_MISMATCH` on `GO:0050728` (*negative regulation of inflammatory response*), plus a
    `FAMILY_WIDE` term assessment recommending `GO:0140865` (*interleukin-22-mediated signaling
    pathway*) at `PTN009232695`.
  - `interpro/panther/PTHR11471/PTHR11471-review.yaml`: `SOUND` node assessments on
    `PTN000895255` (`GO:0005125` *cytokine activity*, `GO:0005615` *extracellular space*,
    `GO:0005886` *plasma membrane*, `GO:0043123` *positive regulation of canonical NF-kappaB
    signal transduction*), `SCOPE_MISMATCH` on `PTN000895255` `GO:2001238` (*positive regulation
    of extrinsic apoptotic signaling pathway*) and `PTN007549844` `GO:0010811` (*positive
    regulation of cell-substrate adhesion*), and `SUBFAMILY_ONLY` term assessments for
    `GO:0036337` (*Fas signaling pathway* on `PANTHER:PTHR11471:SF33`) and `GO:0008625`
    (*extrinsic apoptotic signaling pathway via death domain receptors* on `SF33`, `SF35`,
    `SF36`, `SF41`).
  - `interpro/panther/PTHR12015/PTHR12015-review.yaml`: `SOUND` node assessments on
    `PTN002564680` (ELR+ CXC chemokines including CXCL8), `PTN000245709` (CC/XC chemokines),
    `PTN000428508` (CXCL12), and `PTN008302571` (CXCL9/10/11), `NEEDS_PRUNING` on `PTN008532501`
    `GO:0048245` (*eosinophil chemotaxis* for `SF103` CCL4), `FAMILY_WIDE` term assessments for
    `GO:0008009` (*chemokine activity*) and `GO:0070098` (*chemokine-mediated signaling pathway*),
    and a `SUBFAMILY_ONLY` term assessment for `GO:0038112` (*interleukin-8-mediated signaling
    pathway* on `PANTHER:PTHR12015:SF200`).
  - `interpro/panther/PTHR11412/PTHR11412-review.yaml`: `TOO_DEEP` assessment on `PTN000892454`
    `GO:0004866` (*endopeptidase inhibitor activity*, over-propagated into complement C3/C4/C5),
    `WRONG_NODE` assessment on `PTN008967461` `GO:0008009` (*chemokine activity*, conflating
    anaphylatoxins C3a/C5a with chemokines), `SOUND` assessments on `PTN002605305` (C5) and
    `PTN002605320` (C3), and `SUBFAMILY_ONLY` term assessments for `GO:0038178` (*complement
    component C5a signaling pathway* on `PANTHER:PTHR11412:SF83`) and `GO:0004866` (*endopeptidase
    inhibitor activity* on `SF165`, `SF182`, `SF92`, `SF116`, `SF133`, `SF170`, `SF174`).
  - `interpro/panther/PTHR11515/PTHR11515-review.yaml` and
    `interpro/panther/PTHR11509/PTHR11509-review.yaml`: `SOUND` node assessments on `PTN000162063`
    (beta chains) and `PTN002608947` (alpha chain `CGA`), `SCOPE_MISMATCH` on `PTN002608947`
    `GO:0016914` (*follicle-stimulating hormone complex*), and `SUBFAMILY_ONLY` / `FAMILY_WIDE`
    term assessments scoping `GO:0038194` (*thyroid-stimulating hormone signaling pathway*) to
    `TSHB` (`PTHR11515:SF5`), `GPHB5` (`PTHR11515:SF14`), `CGA` (`PTHR11509:SF0`), and `GPHA2`
    (`PTHR11509:SF5`).
  - `interpro/panther/PTHR16866/PTHR16866-review.yaml`: `SOUND` node assessments on `PTN008565241`
    (`GO:0005576`, `GO:0005184` *neuropeptide hormone activity*, `GO:0007218` *neuropeptide
    signaling pathway*), `PTN002704034` (`NMB`), and `PTN002704045` (`GRP`), and a `SUBFAMILY_ONLY`
    term assessment scoping `GO:0031989` (*bombesin receptor signaling pathway*) to `GRP`
    (`PTHR16866:SF2`) and `NMB` (`PTHR16866:SF3`).
  - `interpro/panther/PTHR24023/PTHR24023-review.yaml`: `SOUND` node assessments on `PTN001166351`
    (`GO:0030020`), `PTN008390299` (`GO:0031012`), `PTN009074843` (`GO:0030199` on the major
    fibrillar collagen clade), `PTN000615596` (`COL4A3`), and `PTN000615545` (`COL4A6`), plus
    `SUBFAMILY_ONLY` term assessments for `GO:0048018` (*receptor ligand activity*) and
    `GO:0038063` (*collagen-activated tyrosine kinase receptor signaling pathway*) across `COL1A1`
    (`SF1082`), `COL1A2` (`SF568`), `COL2A1` (`SF58`), and `COL3A1` (`SF604`).
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
  `ephrin_receptor_signaling` (upgraded), `mif_signaling`, `il34_signaling`, `il21_signaling`,
  `il22_signaling`, `death_receptor_apoptotic_signaling` (upgraded), `chemokine_signaling`
  (upgraded), `c5a_signaling`, `tsh_signaling`, `bombesin_receptor_signaling`,
  `collagen_ddr_signaling`.
- Gene reviews: NTN1, NTN3, KITLG, kitlga, EFNB1, MIF, IL34, IL21, IL22, FASLG, CXCL8, C5, C3,
  TSHB, CGA, GRP, NMB, COL1A1.
- Family reviews: PTHR45836, PTHR11574, PTHR11304, PTHR11954, PTHR28606, PTHR14356, PTHR48488,
  PTHR11471, PTHR12015, PTHR11412, PTHR11515, PTHR11509, PTHR16866, PTHR24023.
- Report page: [report/ligand-gap-report.html](LIGANDS_IN_SIGNALING/report/ligand-gap-report.html)
  (human, fly and fission yeast snapshot; also published as the Ligand gap report artifact).
  It predates the GPCR scope and the other species, so its counts are lower than section 3.

### Next steps

1. **More modules**, pan-species, ligand step first, using the decisions in section 2. Queue from
   the gap check: fly Toll-6/7 neurotrophin (spz5, NT1), opioid receptor signaling (PENK, PDYN,
   POMC), endothelin receptor signaling (EDN1, EDN2, EDN3), galanin signaling (GAL, GALP),
   angiotensin signaling (AGT), CCL19 signaling, APOA1 signaling.
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
