---
title: "YeastPathways to Modules"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [yeast, SCHPO]
---

# YeastPathways to Modules

This project turns SGD's YeastPathways (the YeastCyc Pathway Tools database for
*Saccharomyces cerevisiae*) into reusable biological modules. It is a critical
re-curation, not a translation. Each pathway frame was read against the primary
literature, the enzyme assignments were checked, and the pathway was generalised
to the level at which the biology is shared. Fungal exemplars are grounded in
both budding yeast and, where PomBase has a metabolic GO-CAM, fission yeast.
Every exemplar gene, and every PANTHER family used as a role family, is to be
reviewed so that modules, gene reviews and family reviews agree.

## Sources

- **YeastPathways BioPAX.** The original BioPAX Level 3 export for each of the
  220 pathway frames was fetched from
  `https://pathway.yeastgenome.org/YEAST/pathway-biopax?type=3&object=<frame>`
  by [`fetch_yeastpathways_biopax.py`](YEAST_PATHWAYS/scripts/fetch_yeastpathways_biopax.py)
  (BioPAX files are cached locally and git-ignored). Catalysts were resolved to
  UniProt either via the YeastCyc `<ORF>-MONOMER` frame or, for `MONOMER3O-*`
  frames that carry no ORF, by exact sequence match against the reviewed
  *S. cerevisiae* proteome. The distilled reactions, EC numbers, Rhea ids,
  catalysts and citations are in
  [`data/yeastpathways_summary.yaml`](YEAST_PATHWAYS/data/yeastpathways_summary.yaml).
- **GO-CAMs.** The 189 `gomodel:YeastPathways_*` models (SGD's automatic
  conversion, GO_REF:0000123) and the PomBase *S. pombe* metabolic GO-CAMs, all
  cached under `gocams/`. The PomBase models are hand-curated and were used as
  the second exemplar species and as a check on the SGD conversion.

## Method

1. **Crosswalk.** All 220 frames were grouped into 81 module-yielding decisions
   and eight non-module decisions in
   [`crosswalk.yaml`](YEAST_PATHWAYS/crosswalk.yaml): 32 NEW modules, 35 ALIGN
   (an existing module was revised and grounded in yeast), 14 GENERALIZE (an
   existing module was widened beyond its original lineage), 2 FOLD and 6 NOTE.
   Superpathway and variant frames were merged into their component modules
   rather than modelled again. Single-enzyme frames (sucrose hydrolysis,
   periplasmic NAD degradation, serine/threonine deamination) and grab-bag
   frames (phospholipid degradation, which lumps unrelated phospholipases) were
   not made into modules; they are covered in gene reviews or in a neighbouring
   module's notes.
2. **Module curation**, following [`module_agent_brief.md`](YEAST_PATHWAYS/module_agent_brief.md):
   critical assessment of every reaction and catalyst, literature cached under
   `publications/`, generalisation to the chosen scope with `variant_sets` for
   real lineage alternatives, MF terms on leaf annotons only, *S. cerevisiae*
   and *S. pombe* representative members, verified PANTHER ids only, and
   `gocam_associations` to both the SGD and PomBase models. Disagreements with
   either GO-CAM are written into the module notes.
3. **Gene reviews**, following [`gene_review_agent_brief.md`](YEAST_PATHWAYS/gene_review_agent_brief.md),
   for every gene product listed in
   [`module_members/`](YEAST_PATHWAYS/module_members/).
4. **Family reviews**, following [`family_review_agent_brief.md`](YEAST_PATHWAYS/family_review_agent_brief.md),
   for every PANTHER family a module uses as a role family.
5. **Consistency pass.** `module_validator` function-conformance checks compare
   every module annoton with the core functions of its exemplar gene reviews and
   the term scopes of its family reviews.

## Generalisation decisions

The GENERALIZE actions are where the yeast pathway stopped being the right unit:

- The shikimate pathway is modelled across bacteria, fungi, plants and
  apicomplexa (the fungal pentafunctional ARO1 is an architecture variant).
- The proline–P5C cycle, GABA shunt and polyamine biosynthesis are modelled as
  eukaryotic modules, with the yeast enzymes as one instance.
- Ubiquinone biosynthesis covers bacteria and eukaryotes, with the eukaryotic
  COQ route as a variant.
- Cytosolic type I fatty acid synthesis is separated from the mitochondrial
  type II synthase (CEM1, MCT1, OAR1 and HFA1 belong to the latter), which
  YeastCyc mixes into its cytosolic pathways.
- Glycerolipid/TAG synthesis covers both the glycerol-3-phosphate and DHAP
  routes. The ceramide core is modelled for eukaryotes, with fungal
  inositolphosphoceramide head groups as the lineage-specific part.
- The carnitine shuttle covers both mitochondrial long-chain fatty acid import
  in animals and the acetyl-carnitine shuttle in fungi.

## Systemic problems found in YeastPathways and its GO-CAM conversion

These recur across many frames and were corrected in the gene reviews (as
REMOVE or MODIFY with a reason) and noted in the modules. They are the main
findings to feed back to SGD and GO.

- **Default cytosol compartment.** The YeastPathways2GO conversion places every
  activity in the cytosol, including mitochondrial (ARG2, ARG5,6, ARG7, ARG8,
  LEU9, BAT1, ILV1, ILV3, ILV5, SHM1, PGS1, CRD1, PSD1), ER-membrane (the whole
  ergosterol, elongation, sphingolipid and phospholipid sets), peroxisomal (FOX2,
  ECI1, DCI1, FAA2) and nuclear (ARG82, IPK1) enzymes.
- **Superpathway process inflation.** Members of union frames inherit the union's
  process: PRPP-PWY-1 gives "nucleotide biosynthetic process" to histidine
  enzymes; ALL-CHORISMATE-PWY-1 gives "chorismate metabolic process" to
  tryptophan and tyrosine enzymes; PWY3O-285 gives "purine-containing compound
  salvage" to every de novo purine enzyme; GLUCFERMEN-PWY is mapped to
  GO:0019658 (bifid shunt) on every PDC and ADH.
- **Molecular-function mapping errors**, among them:
  - GO:0103045 on ARG2 and ARG7 (an EC 2.3.1.1 name collision);
  - GO:0052656 for every branched-chain and MTOB transamination;
  - GO:0120517 (IP5 to IP6) used for the IP5 to PP-IP4 step on ARG82 and KCS1;
  - (3S)-specific hydratase and dehydrogenase terms on the (3R)-specific MFE-2 FOX2;
  - EC 4.2.1.17 instead of EC 4.2.1.134 on the VLCFA dehydratase PHS1;
  - GO:0102772 (the SUR2 C4-hydroxylase) on SCS7;
  - the animal one-step carboxylase GO:0004638 on fungal ADE2, which is a fused
    N5-CAIR synthetase / N5-CAIR mutase;
  - a bacterial ClsA-type reaction for the CMP-forming cardiolipin synthase CRD1;
  - a phosphatidylcholine phospholipase C reaction for the inositol-sphingolipid
    phospholipase ISC1.
- **Process-direction errors.** Phosphatases (SAC1, YMR1, INP51–54, FIG4) and
  DDP1 inherit "biosynthetic process" terms from the pathways they reverse;
  DPL1 is filed under sphingolipid biosynthesis although it is the exit step.
- **Catalyst-list errors.** Missing enzymes (for example ARO10, LEU2, ILV2,
  ACO2, LYS5, OAC1, the MTA-cycle enzymes), paralogs placed on the wrong step
  (ADK2, a mitochondrial GTP:AMP kinase, on the cytosolic ATP:AMP step; DCI1 on
  ECI1's step; DPP1 and LPP1 on the PAH1 step of TAG synthesis; HIS5 as an
  aromatic aminotransferase) and regulatory subunits presented as catalysts
  (CSG2).
- **PAINT over-propagation** across paralogs, judged node by node in the gene
  and family reviews: for example SPE4 from SPE3, BIO3 from the AtBIO1 fusion
  node, MET6 receiving the B12-dependent MetH activity, KCS1 receiving ARG82's
  IP3/IP4 kinase activities, AUR1 and IPT1 leaking terms through a shared node,
  and the PTHR18968 FAD-binding node reaching the FAD-independent catabolic
  acetolactate synthase.
- **Ontology issues** raised as suggested questions: the GO:0000248 definition
  describes the C-22 rather than the C-5 sterol desaturation; GO:0045140 sits
  under hexosyltransferase activity; GO has no terms for IPT1 (EC 2.7.1.228),
  phytosphingosine-1-phosphate phosphatase or a VLCFA-specific ceramide
  synthase.

The PomBase GO-CAMs agree with the modules far more often than the SGD
conversion does; the differences found so far are noted in each module
(for example, generic "pyruvate fermentation" on three of the four fission-yeast
pyruvate decarboxylases, and the argininosuccinate lyase step resting on IBA
evidence for arg41 while the IMP evidence is on its paralog arg7).

## Status

Counts are per module and include genes and families shared between modules, so
the totals are larger than the number of distinct reviews. Only committed,
fully reviewed files are counted. These counts track the complete
`claude/yeastpathways-01` through `claude/yeastpathways-13` series; links to
NEW module pages become live as those PRs land.

| Module | Action | YeastPathways frames | S. cerevisiae reviewed | S. pombe reviewed | Families reviewed |
|---|---|---|---|---|---|
| [histidine_biosynthesis](../modules/histidine_biosynthesis.html) | ALIGN | 1 | 7/7 | 8/8 | 0/3 |
| [arginine_biosynthesis](../modules/arginine_biosynthesis.html) | ALIGN | 2 | 9/9 | 10/10 | 3/3 |
| [lysine_biosynthesis_aminoadipate](../modules/lysine_biosynthesis_aminoadipate.html) | NEW | 1 | 12/12 | 8/8 | 1/7 |
| [branched_chain_amino_acid_biosynthesis](../modules/branched_chain_amino_acid_biosynthesis.html) | ALIGN | 4 | 12/12 | 10/10 | 12/12 |
| [bacterial_shikimate_chorismate_biosynthesis](../modules/bacterial_shikimate_chorismate_biosynthesis.html) | GENERALIZE | 1 | 4/4 | 4/4 | 8/8 |
| [phenylalanine_tyrosine_biosynthesis](../modules/phenylalanine_tyrosine_biosynthesis.html) | NEW | 3 | 5/5 | 4/4 | 2/5 |
| [tryptophan_biosynthesis](../modules/tryptophan_biosynthesis.html) | ALIGN | 1 | 5/5 | 4/4 | 0/6 |
| [phosphorylated_serine_biosynthesis](../modules/phosphorylated_serine_biosynthesis.html) | ALIGN | 1 | 4/4 | 3/3 | 0/2 |
| [glycine_serine_interconversion](../modules/glycine_serine_interconversion.html) | NEW | 5 | 4/4 | 0/0 | 0/3 |
| [aspartate_family_threonine_biosynthesis](../modules/aspartate_family_threonine_biosynthesis.html) | NEW | 5 | 5/5 | 5/5 | 5/5 |
| [methionine_biosynthesis](../modules/methionine_biosynthesis.html) | ALIGN | 3 | 5/5 | 5/5 | 0/6 |
| [fungal_sulfur_amino_acid_transsulfuration](../modules/fungal_sulfur_amino_acid_transsulfuration.html) | NEW | 4 | 4/4 | 2/2 | 0/2 |
| [aps_dependent_assimilatory_sulfate_reduction](../modules/aps_dependent_assimilatory_sulfate_reduction.html) | ALIGN | 3 | 7/7 | 6/6 | 5/5 |
| [siroheme_biosynthesis](../modules/siroheme_biosynthesis.html) | NEW | 1 | 2/2 | 0/0 | 0/3 |
| [methionine_cycle](../modules/methionine_cycle.html) | ALIGN | 2 | 7/7 | 5/5 | 0/6 |
| [methionine_salvage_mta_cycle](../modules/methionine_salvage_mta_cycle.html) | NEW | 2 | 9/9 | 5/5 | 0/7 |
| [proline_metabolism](../modules/proline_metabolism.html) | GENERALIZE | 2 | 6/6 | 6/6 | 3/6 |
| [arginine_catabolism_arginase_pathway](../modules/arginine_catabolism_arginase_pathway.html) | NEW | 2 | 5/5 | 6/6 | 5/5 |
| [nitrogen_assimilation_glutamate_glutamine](../modules/nitrogen_assimilation_glutamate_glutamine.html) | NEW | 5 | 5/5 | 4/4 | 0/3 |
| [aspartate_asparagine_metabolism](../modules/aspartate_asparagine_metabolism.html) | NEW | 6 | 10/10 | 4/4 | 4/4 |
| [ehrlich_pathway](../modules/ehrlich_pathway.html) | NEW | 6 | 15/15 | 0/0 | 5/5 |
| [gaba_shunt](../modules/gaba_shunt.html) | GENERALIZE | 2 | 3/3 | 3/3 | 1/5 |
| [polyamine_metabolism](../modules/polyamine_metabolism.html) | GENERALIZE | 4 | 7/7 | 7/7 | 0/11 |
| [ureide_urea_catabolism](../modules/ureide_urea_catabolism.html) | NEW | 4 | 4/4 | 5/5 | 0/10 |
| [emp_glycolysis](../modules/emp_glycolysis.html) | ALIGN | 4 | 20/20 | 14/14 | 9/14 |
| [alcoholic_fermentation](../modules/alcoholic_fermentation.html) | NEW | 6 | 6/6 | 6/6 | 7/7 |
| [pdh_bypass_acetyl_coa_synthesis](../modules/pdh_bypass_acetyl_coa_synthesis.html) | NEW | 2 | 9/9 | 0/0 | 3/4 |
| [gluconeogenesis](../modules/gluconeogenesis.html) | ALIGN | 1 | 15/15 | 0/0 | 5/14 |
| [tca_cycle](../modules/tca_cycle.html) | ALIGN | 3 | 17/17 | 16/16 | 0/12 |
| [glyoxylate_cycle](../modules/glyoxylate_cycle.html) | NEW | 1 | 6/6 | 0/0 | 0/3 |
| [pyruvate_metabolism](../modules/pyruvate_metabolism.html) | ALIGN | 1 | 7/7 | 6/6 | 0/5 |
| [pentose_phosphate_pathway](../modules/pentose_phosphate_pathway.html) | ALIGN | 4 | 16/16 | 8/8 | 0/8 |
| [glycerol_metabolism](../modules/glycerol_metabolism.html) | NEW | 2 | 9/9 | 6/6 | 2/6 |
| [galactose_leloir_pathway](../modules/galactose_leloir_pathway.html) | ALIGN | 1 | 5/5 | 4/4 | 1/5 |
| [xylose_oxidoreductase_pathway](../modules/xylose_oxidoreductase_pathway.html) | NEW | 2 | 3/3 | 0/0 | 2/4 |
| [trehalose_metabolism](../modules/trehalose_metabolism.html) | NEW | 2 | 7/7 | 6/6 | 0/9 |
| [glycogen_metabolism_fungal](../modules/glycogen_metabolism_fungal.html) | NEW | 2 | 11/11 | 0/0 | 2/8 |
| [hexosamine_biosynthesis](../modules/hexosamine_biosynthesis.html) | ALIGN | 1 | 4/4 | 5/5 | 2/5 |
| [fungal_chitin_chitosan_synthesis](../modules/fungal_chitin_chitosan_synthesis.html) | NEW | 2 | 7/7 | 0/0 | 0/5 |
| [dolichol_phosphate_sugar_donor_supply](../modules/dolichol_phosphate_sugar_donor_supply.html) | ALIGN | 2 | 11/11 | 11/11 | 12/12 |
| [n_glycan_llo_assembly_cytoplasmic](../modules/n_glycan_llo_assembly_cytoplasmic.html) | ALIGN | 1 | 6/6 | 6/6 | 0/7 |
| [n_glycan_llo_assembly_lumenal](../modules/n_glycan_llo_assembly_lumenal.html) | ALIGN | 1 | 6/6 | 6/6 | 0/4 |
| [methylglyoxal_detoxification](../modules/methylglyoxal_detoxification.html) | ALIGN | 1 | 3/3 | 3/3 | 0/2 |
| [glutathione_dependent_formaldehyde_detoxification](../modules/glutathione_dependent_formaldehyde_detoxification.html) | ALIGN | 1 | 3/3 | 0/0 | 1/3 |
| [glutathione_synthesis_gamma_glutamyl_cycle](../modules/glutathione_synthesis_gamma_glutamyl_cycle.html) | ALIGN | 3 | 9/9 | 10/10 | 0/8 |
| [glutathione_biosynthesis](../modules/glutathione_biosynthesis.html) | ALIGN | 1 | 2/2 | 2/2 | 0/4 |
| [glutathione_thioredoxin_redox_systems](../modules/glutathione_thioredoxin_redox_systems.html) | NEW | 4 | 18/18 | 8/8 | 1/11 |
| [tetrahydrofolate_biosynthesis](../modules/tetrahydrofolate_biosynthesis.html) | NEW | 7 | 7/7 | 7/7 | 2/11 |
| [folate_one_carbon_interconversion](../modules/folate_one_carbon_interconversion.html) | ALIGN | 2 | 6/6 | 0/0 | 0/8 |
| [glycine_cleavage_system](../modules/glycine_cleavage_system.html) | ALIGN | 1 | 4/4 | 4/4 | 0/4 |
| [riboflavin_biosynthesis](../modules/riboflavin_biosynthesis.html) | ALIGN | 1 | 8/8 | 8/8 | 0/8 |
| [eukaryotic_thiamine_biosynthesis](../modules/eukaryotic_thiamine_biosynthesis.html) | NEW | 1 | 9/9 | 7/7 | 0/5 |
| [vitamin_b6_plp_metabolism](../modules/vitamin_b6_plp_metabolism.html) | GENERALIZE | 1 | 4/4 | 5/5 | 1/5 |
| [biotin_biosynthesis](../modules/biotin_biosynthesis.html) | ALIGN | 1 | 5/5 | 1/1 | 6/6 |
| [coenzyme_a_biosynthesis](../modules/coenzyme_a_biosynthesis.html) | ALIGN | 2 | 13/13 | 8/8 | 11/11 |
| [nad_de_novo_and_salvage_fungal](../modules/nad_de_novo_and_salvage_fungal.html) | NEW | 10 | 15/15 | 9/9 | 0/13 |
| [heme_biosynthesis](../modules/heme_biosynthesis.html) | ALIGN | 3 | 8/8 | 8/8 | 0/5 |
| [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) | GENERALIZE | 4 | 14/14 | 11/11 | 0/11 |
| [isoprenoid_diphosphate_biosynthesis](../modules/isoprenoid_diphosphate_biosynthesis.html) | ALIGN | 1 | 3/3 | 3/3 | 0/3 |
| [mevalonate_pathway](../modules/mevalonate_pathway.html) | GENERALIZE | 2 | 7/7 | 6/6 | 0/7 |
| [ergosterol_biosynthesis](../modules/ergosterol_biosynthesis.html) | NEW | 6 | 16/16 | 18/18 | 2/10 |
| [fatty_acid_de_novo_synthesis](../modules/fatty_acid_de_novo_synthesis.html) | GENERALIZE | 9 | 5/5 | 5/5 | 0/6 |
| [type_ii_fatty_acid_synthesis](../modules/type_ii_fatty_acid_synthesis.html) | ALIGN | 1 | 7/7 | 6/6 | 3/14 |
| [fatty_acid_elongation_cycle](../modules/fatty_acid_elongation_cycle.html) | ALIGN | 1 | 6/6 | 5/5 | 0/4 |
| [peroxisomal_beta_oxidation](../modules/peroxisomal_beta_oxidation.html) | ALIGN | 1 | 10/10 | 0/0 | 0/9 |
| [carnitine_shuttle](../modules/carnitine_shuttle.html) | GENERALIZE | 1 | 5/5 | 0/0 | 3/3 |
| [triacylglycerol_biosynthesis](../modules/triacylglycerol_biosynthesis.html) | GENERALIZE | 4 | 9/9 | 8/8 | 1/10 |
| [cdp_dag_phospholipid_synthesis](../modules/cdp_dag_phospholipid_synthesis.html) | NEW | 6 | 11/11 | 11/11 | 11/11 |
| [kennedy_pathway_phospholipid_synthesis](../modules/kennedy_pathway_phospholipid_synthesis.html) | GENERALIZE | 2 | 6/6 | 4/4 | 2/5 |
| [phosphoinositide_biosynthesis](../modules/phosphoinositide_biosynthesis.html) | NEW | 1 | 6/6 | 6/6 | 0/5 |
| [myo_inositol_and_inositol_phosphate_biosynthesis](../modules/myo_inositol_and_inositol_phosphate_biosynthesis.html) | NEW | 2 | 8/8 | 5/5 | 0/6 |
| [sphingolipid_de_novo_synthesis](../modules/sphingolipid_de_novo_synthesis.html) | GENERALIZE | 1 | 15/15 | 14/14 | 3/11 |
| [de_novo_purine_synthesis](../modules/de_novo_purine_synthesis.html) | ALIGN | 5 | 9/9 | 8/8 | 14/14 |
| [purine_nucleotide_interconversion](../modules/purine_nucleotide_interconversion.html) | GENERALIZE | 4 | 10/10 | 0/0 | 4/9 |
| [dntp_de_novo_synthesis](../modules/dntp_de_novo_synthesis.html) | NEW | 3 | 9/9 | 0/0 | 7/7 |
| [de_novo_pyrimidine_synthesis](../modules/de_novo_pyrimidine_synthesis.html) | ALIGN | 4 | 10/10 | 8/8 | 6/6 |
| [purine_salvage_and_catabolism](../modules/purine_salvage_and_catabolism.html) | GENERALIZE | 4 | 7/7 | 5/5 | 0/11 |
| [pyrimidine_salvage](../modules/pyrimidine_salvage.html) | NEW | 2 | 6/6 | 7/7 | 2/7 |
| [oxphos](../modules/oxphos.html) | ALIGN | 1 | 3/3 | 2/2 | 0/2 |
| [diphthamide_biosynthesis](../modules/diphthamide_biosynthesis.html) | NEW | 1 | 7/7 | 0/0 | 5/5 |
| [erythroascorbate_biosynthesis](../modules/erythroascorbate_biosynthesis.html) | NEW | 1 | 3/3 | 0/0 | 1/3 |
| **Total (with overlaps)** | | | 627/627 | 420/420 | 185/547 |

### Remaining work

- All S. cerevisiae and *S. pombe* exemplar genes are reviewed (the later *S. pombe*
  reviews are in `claude/yeastpathways-13`). Some *S. pombe* members are filed under
  their PomBase name or systematic ORF rather than the module-member label (for
  example `ups1` for HEM4, `gpt2` for ALG7); the table matches these by UniProt
  accession.
- 134 of the 443 distinct PANTHER role families have a family review; the other
  309 are not yet reviewed.
- Module-family scope warnings: many modules ground a role on a whole PANTHER
  family where the family review restricts the activity to particular subfamilies.
  `module_validator` reports these as `FAMILY_SCOPE_RESTRICTED` warnings (a
  subfamily outside the reviewed scope is already a blocking `FAMILY_CONFLICT`).
  They are left as warnings rather than re-pointed in bulk, because choosing a
  subfamily or PAINT node is a placement judgement. Examples: the carnitine
  shuttle (PTHR24064, PTHR22589, PTHR45624), PanE/PanC in CoA biosynthesis,
  PDXP in vitamin B6, MPDU1, and the shared BioA / GABA transaminase family
  PTHR42684 used by two modules for two activities.
- GO term migration: several module concept terms (the glycolysis route terms
  GO:0061615 and siblings, GO:0034354) are obsolete in current GO but still live in
  the ontology release this repository validates against. Each affected module
  documents the replacement; migrate when the pinned GO is updated.

## Findings to report upstream

**SGD / YeastPathways and its GO-CAM conversion (GO_REF:0000123)**
- Default cytosol on every activity, including mitochondrial, ER-membrane,
  peroxisomal and nuclear enzymes.
- Wrong catalyst on a reaction: RRT2 on the diphthamide amidation step (DPH6 is
  the ligase); ADK2 (mitochondrial GTP:AMP kinase) on the cytosolic ATP:AMP step;
  ISC1 on a phosphatidylcholine phospholipase C reaction; APT2 (inactive) as an
  adenine phosphoribosyltransferase; DPP1/LPP1 on the PAH1 step; DCI1 on ECI1's step.
- Wrong reaction or term: bacterial ClsA reaction for CRD1; GO:0120517 (IP5 to IP6)
  for the IP5 to PP-IP4 step on ARG82/KCS1; (3S)-specific terms on the (3R)
  MFE-2 FOX2; EC 4.2.1.17 on PHS1; GO:0102772 (Sur2's C4-hydroxylase) on SCS7;
  archaea-only GO:0004164 on DPH5; the obsolete GO:0102480 on FCY1;
  "adenosine" (nucleoside) and "guanosine nucleotide" mappings that pull in ADK1/2
  and GUK1; the outdated comment that the yeast gamma-glutamyl cyclotransferase and
  5-oxoprolinase are unknown.
- Missing genes on reactions, among them TSC3, KEI1, CSH1, PDX1, KGD4, NTH2,
  THI5/11/12, ERG28/NCP1/CYB5, DUG2/DUG3/GCG1/OXP1 and the HMP-P synthase paralogs.

**PomBase**
- cho1 (the OPI3 ortholog) carries a mitochondrial outer membrane ISO transferred
  by gene name from budding-yeast CHO1, an unrelated protein.
- ura1 carries a GMP synthase IGI from a paper about its CPSase/ATCase activities.
- pan5 mitochondrion IBA and GO-CAM placement trace to a PAINT node seeded only by
  CBS2.
- GO-CAM issues: obsolete GO:0061621 in the glycolysis model; a duplicated tpi1
  node; GO:0000248 on erg31/erg32; mitochondrial cut6 and fas1 placeholder nodes
  and an NADH enoyl reductase term on fas1; dephospho-CoA kinase on cab4; a
  missing leu1 step and duplicated edge in the BCAA model; caa1/maa1 roles opposite
  to PMID:39502420.

**GO**
- GO:0000248 "C-5 sterol desaturase activity" has a definition describing the C-22
  reaction.
- GO:0034628 absorbed the tryptophan (kynurenine) route as synonyms, but its
  definition still describes only the L-aspartate route.
- GO:0045140 (inositol phosphoceramide synthase) sits under hexosyltransferase
  activity; GO:0036374 sits under threonine-type peptidase although Dug2/Dug3 use a
  Cys nucleophile.
- Missing terms: IPT1 (EC 2.7.1.228), phytosphingosine-1-phosphate phosphatase, a
  very-long-chain-specific ceramide synthase, an MF for 2-oxoadipate transport.

**PAINT** (each recorded as a `node_assessment` in the family review)
- Paralog over-propagation, for example SPE4 from SPE3, BIO3 from the AtBIO1
  fusion node, KCS1 receiving ARG82 activities, AUR1/IPT1 leakage, ADK2 receiving
  AMP kinase, CPT1C keeping CPT process terms, MocR regulators receiving
  aminotransferase activity, and wrong-node IRDs such as the fungal ornithine
  carrier negation.
- `fetch-panther-paint` misses some IRD rows that are present in the full PAINT GAF.

## Files

- [`crosswalk.yaml`](YEAST_PATHWAYS/crosswalk.yaml): frame-to-module decisions and rationale.
- [`data/yeastpathways_summary.yaml`](YEAST_PATHWAYS/data/yeastpathways_summary.yaml): distilled BioPAX.
- [`module_members/`](YEAST_PATHWAYS/module_members/): exemplar genes and role families per module.
- Agent briefs: [module](YEAST_PATHWAYS/module_agent_brief.md),
  [gene](YEAST_PATHWAYS/gene_review_agent_brief.md),
  [family](YEAST_PATHWAYS/family_review_agent_brief.md).
