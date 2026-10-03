---
title: "CO2-Concentrating Mechanisms"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [CHLRE, ARATH]
genes: [EPYC1, LCI5, RBCS1, SAGA1, MITH1, RBMP1, RBMP2, BST1, BST2, BST3, BST4, CAH3, LCIB, LCIC, HLA3, LCIA, CIA5]
---

# CO2-Concentrating Mechanisms (CCMs)

**Bottom line:** Rubisco is slow and also reacts with O2. Many photosynthetic
organisms get around this with a CO2-concentrating mechanism (CCM) that raises
CO2 around Rubisco. This project curates CCMs as modules and gene reviews,
starting with the pyrenoid-based CCM of the green alga *Chlamydomonas
reinhardtii*. It is the best-characterized eukaryotic CCM and the main
candidate for engineering into C3 crops. The first deliverable is the
[pyrenoid CCM module](../modules/pyrenoid_ccm.html) (`modules/pyrenoid_ccm.yaml`,
status DRAFT). It follows the six-step minimal-pyrenoid plan of Fei et al.
(2022) and Adler et al. (2022), and grounds each step on Chlamydomonas proteins
with UniProt ids. One finding already affects existing curation: **LCI5 (Q94ET8)
is EPYC1**, the Rubisco linker that forms the pyrenoid matrix. The existing
LCI5 gene review describes it as a protein of unknown function and needs
redoing.

## Scope

CCMs arose many times. This project will cover them as separate modules:

| CCM type | Where | Status |
|---|---|---|
| Pyrenoid-based (biophysical, eukaryotic algae and hornworts) | chloroplast stroma | **[module started](../modules/pyrenoid_ccm.html)** (Chlamydomonas) |
| Carboxysome-based (cyanobacteria, some chemoautotrophs) | bacterial microcompartment | not started; stub variant in [photosynthesis module](../modules/photosynthesis.html) |
| C4 (biochemical, two-cell) | mesophyll + bundle sheath | not started |
| CAM (biochemical, temporal) | single cell, day/night | not started |

The [oxygenic photosynthesis module](../modules/photosynthesis.html) already has
an optional CCM part with carboxysome and pyrenoid variants. Its pyrenoid
variant is a one-line stub; it should point to the new module once this matures
(see [PHOTOSYNTHESIS](PHOTOSYNTHESIS.md)).

The pyrenoid module is deliberately **concrete** (Chlamydomonas). Pyrenoids in
diatoms, hornworts, and other lineages evolved independently and use unrelated
linker proteins, so a lineage-neutral module should come later, once more than
one instance is curated.

## The pyrenoid module: six steps

The steps follow Adler et al. 2022
[PMID:35961043](https://pubmed.ncbi.nlm.nih.gov/35961043/), Fig. 5. That figure
is built on the reaction-diffusion model of Fei et al. 2022
[PMID:35596080](https://pubmed.ncbi.nlm.nih.gov/35596080/). The model predicts
that the full minimal PCCM (step 6) raises CO2 assimilation about three-fold,
at an extra cost of about 1.3 ATP per CO2 fixed. That prediction assumes native
plant carbonic anhydrase is kept out of the Rubisco matrix from step 1 on.

| Step | Module part | Chlamydomonas participants (UniProt) | GO grounding | Evidence state |
|---|---|---|---|---|
| 1. Rubisco condensation | `rubisco_condensate` | Rubisco large subunit (P00877) + RBCS1 (P00873); EPYC1/LCI5 (Q94ET8) | pyrenoid GO:1990732; molecular condensate scaffold activity GO:0140693 | Strong. Reconstituted in vitro and in Arabidopsis chloroplasts with a hybrid Rubisco ([PMID:33298923](https://pubmed.ncbi.nlm.nih.gov/33298923/)) |
| 2. Thylakoid tubules in the condensate | `tubule_matrix_tethering` | SAGA1 (A0A2K3D7T6), RBMP1 (A0A2K3DMS8); MITH1, RBMP2, BST4 not yet grounded | pyrenoid tubule GO:0160223 | Rubisco-binding motif ([PMID:33177094](https://pubmed.ncbi.nlm.nih.gov/33177094/)); SAGA1/MITH1 tubules reconstituted in Arabidopsis ([PMID:39211136](https://pubmed.ncbi.nlm.nih.gov/39211136/)) |
| 3. Lumenal carbonic anhydrase | `lumenal_co2_release` | CAH3 (Q39588) | carbonate dehydratase activity GO:0004089; thylakoid lumen | Strong genetics; moves to tubules under low CO2 by an unknown route |
| 4. Thylakoid bicarbonate channels | `thylakoid_bicarbonate_entry` | `BST1`-3 (`BST1` = A0A2K3CTN0) | bicarbonate transmembrane transporter activity GO:0015106 (inferred) | Location and genetics only; no direct transport measurement |
| 5. Starch sheath diffusion barrier | `starch_sheath_barrier` | SAGA1 (A0A2K3D7T6) | starch binding GO:2001070 (inferred from the CBM20 domain) | Modeling says a barrier is needed; whether starch is that barrier is unclear |
| 6. Stromal CO2 recapture | `stromal_co2_recapture` | LCIB (Q75NZ2) / LCIC (Q75NZ1) | carbonate dehydratase activity GO:0004089 | Beta-CA structures ([PMID:27911826](https://pubmed.ncbi.nlm.nih.gov/27911826/)); strong genetics |
| Optional: Ci uptake | `ci_uptake` | HLA3 (A0A2K3E226), LCIA (Q75NZ3) | GO:0015106 | Knockdown phenotypes |
| Optional: regulation | `ccm_induction` | CIA5/CCM1 (Q9FED4) | cellular response to carbon dioxide GO:0071244 | Mutant rescue; DNA binding not shown |

Ontology gap: GO has **no biological-process term for a carbon-concentrating
mechanism** of any kind. The module records this as an ONTOLOGY knowledge gap,
and it is a candidate new-term request.

## Gene review backlog

All participants are Chlamydomonas proteins, and most are unreviewed TrEMBL
entries named only by locus (e.g. `CHLRE_11g467712v5`). None has a gene review
yet, except LCI5.

- [ ] **CHLRE/LCI5 → re-review as EPYC1 (high priority).** The sequences are
  identical, and Freeman Rosenzweig et al. 2017
  ([PMID:28938114](https://pubmed.ncbi.nlm.nih.gov/28938114/)) state "EPYC1;
  also known as LCI5". The current review has no condensate/linker function, so
  the module validator warns `FUNCTION_UNREVIEWED` on `epyc1_linker`. Decide
  whether to keep the folder name `LCI5` (UniProt gene name) or move it to
  `EPYC1`, and use `target.superseded_by` in history if it is moved.
- [ ] CAH3 (Q39588), LCIB (Q75NZ2), LCIC (Q75NZ1): best-evidenced enzymes; review next.
- [ ] SAGA1, RBMP1, `BST1`-3: `just fetch-gene CHLRE <symbol>` will need the
  accessions above, because UniProt has no gene symbol for these entries.
- [ ] Ground MITH1, RBMP2, SAGA2, BST4 accessions from the cached papers'
  `Cre` loci before adding them to the module.
- [ ] Rubisco (large subunit P00877, RBCS1 P00873): check whether GOA records the
  pyrenoid location.

## Where AI, bioinformatics, and data integration could help

These come from scoping discussions (December 2024) about what the LBNL work
needs. That work is building a synthetic pyrenoid in a green alga, as a faster
and more tractable system for basic understanding, and then using what it
learns to design for land plants.

**Step 1, Rubisco condensation**
- Is condensation a solved problem for engineered pyrenoids? It works for a
  hybrid Rubisco carrying algal small-subunit helices
  ([PMID:23112177](https://pubmed.ncbi.nlm.nih.gov/23112177/),
  [PMID:33298923](https://pubmed.ncbi.nlm.nih.gov/33298923/)). It is unknown
  for native crop Rubisco.
- Do protein properties and levels need tuning for different environmental
  conditions?
- Bioinformatics of linker repeat domains and of Rubisco small-subunit helices
  across algae, i.e. mining orthologs and analogs from other pyrenoid-bearing
  lineages.
- Reaction-diffusion modeling (extending Fei et al.
  [PMID:35596080](https://pubmed.ncbi.nlm.nih.gov/35596080/), and the update
  on CO2 permeability [PMID:40794800](https://pubmed.ncbi.nlm.nih.gov/40794800/)).
- Structural modeling and docking of linker-Rubisco interfaces (template: He
  et al. [PMID:33230314](https://pubmed.ncbi.nlm.nih.gov/33230314/)).

**Steps 2-6**: thylakoid association, lumenal CA, bicarbonate channels, starch
sheath, stromal CA. Each is a module part with the same questions about
grounding and homologs.

**Broader informatics goals**
- A "virtual Chlamydomonas": integrated models of the cell.
- Chlamydomonas in KBase.
- Functional characterization of all Chlamydomonas genes. Most CCM proteins
  are unreviewed TrEMBL entries with no GO annotation, which this project can
  address one module at a time.
- A GO pathway (GO-CAM) for the pyrenoid CCM. The module's `connections` are
  the draft causal graph.

## Open questions

These are recorded as `knowledge_gaps` on the module where they map to a step.

- Can an interaction interface between native crop Rubiscos and an EPYC1-like
  linker protein be engineered?
- Is the native level of stromal carbonic anhydrase activity in plant
  chloroplasts sufficient to drive a pyrenoid-based CCM?
- How are thylakoid membranes that traverse pyrenoids formed, and what do the
  traversing thylakoids do?
- What regulates the formation and turnover of starch around pyrenoids? Will a
  starch sheath interfere with plant starch metabolism or fit into it?
- How is the lumenal carbonic anhydrase CAH3 relocalized to the pyrenoid
  thylakoid tubules in Chlamydomonas?
- How is a pyrenoid-based CCM energized? Will normal levels of ATP production
  and proton-motive force in C3 thylakoids be enough to power a CCM?
- What are the minimal components required for a functional pyrenoid-based CCM?

## Key references

- Mackinder et al. 2016, EPYC1 links Rubisco: [PMID:27166422](https://pubmed.ncbi.nlm.nih.gov/27166422/)
- Freeman Rosenzweig et al. 2017, pyrenoid is liquid-like: [PMID:28938114](https://pubmed.ncbi.nlm.nih.gov/28938114/)
- Mackinder et al. 2017, CCM spatial interactome: [PMID:28938113](https://pubmed.ncbi.nlm.nih.gov/28938113/)
- Wunder et al. 2018, Rubisco + EPYC1 phase separation in vitro: [PMID:30498228](https://pubmed.ncbi.nlm.nih.gov/30498228/)
- Meyer et al. 2020, Rubisco-binding motif: [PMID:33177094](https://pubmed.ncbi.nlm.nih.gov/33177094/)
- Fei et al. 2022, PCCM model and engineering roadmap: [PMID:35596080](https://pubmed.ncbi.nlm.nih.gov/35596080/)
- Adler et al. 2022, new horizons for building PCCMs in plants: [PMID:35961043](https://pubmed.ncbi.nlm.nih.gov/35961043/)
- Hennacy et al. 2024, SAGA1/MITH1 tubule biogenesis: [PMID:39211136](https://pubmed.ncbi.nlm.nih.gov/39211136/)
- Barrett et al. 2021, pyrenoid review: [PMID:33421532](https://pubmed.ncbi.nlm.nih.gov/33421532/)
