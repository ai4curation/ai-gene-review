---
title: "CO2-Concentrating Mechanisms"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [CHLRE, ARATH]
genes: [LCI5, RBCS1, SAGA1, MITH1, RBMP1, RBMP2, BST1, BST2, BST3, CAH3, LCIB, LCIC, HLA3, LCIA, CIA5]
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
with UniProt ids. All 12 Chlamydomonas proteins in the module now have gene
reviews. The reviews changed the module in four places:

- **LCI5 is EPYC1**, the Rubisco linker that forms the pyrenoid matrix. The
  old LCI5 review called it a protein of unknown function; it has been redone.
- **RBMP1 is BST4**, and it is not the tubule-matrix tether the module first
  assumed: bst4 mutants keep normal tubule-matrix contact. It is a
  tubule-resident bestrophin-family channel.
- **No transport has been measured for BST1-3.** They are annotated as anion
  channels, and bicarbonate as the permeant ion is still a proposal.
- **Purified Chlamydomonas LCIB, LCIC and LCIB/LCIC were inactive as carbonic
  anhydrases.** LCIB's activity rests on rescue of CA-deficient mutants, so the
  module now gives the activity to LCIB only.

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
| 2. Thylakoid tubules in the condensate | `tubule_matrix_tethering` | SAGA1 (A0A2K3D7T6); BST4/RBMP1 (A0A2K3DMS8); MITH1, RBMP2 not yet grounded | pyrenoid tubule GO:0160223; SAGA1 protein-membrane adaptor activity GO:0043495 (tentative) | SAGA1/MITH1 tubules reconstituted in Arabidopsis ([PMID:39548241](https://pubmed.ncbi.nlm.nih.gov/39548241/)); BST4 is not a tether ([PMID:39240724](https://pubmed.ncbi.nlm.nih.gov/39240724/)); the actual tether is unknown |
| 3. Lumenal carbonic anhydrase | `lumenal_co2_release` | CAH3 (Q39588) | carbonate dehydratase activity GO:0004089; thylakoid lumen and pyrenoid tubule | Strong genetics; the low-CO2 shift into the tubules is modest (19% to 37%) and contested |
| 4. Thylakoid bicarbonate channels | `thylakoid_bicarbonate_entry` | `BST1`-3 (`BST1` = A0A2K3CTN0, BST2 = A0A2K3CTQ2, BST3 = A0A2K3CTP3) | monoatomic anion channel activity GO:0005253 | Location and knockdown genetics only; no transport measured |
| 5. Starch sheath diffusion barrier | `starch_sheath_barrier` | SAGA1 (A0A2K3D7T6) | starch binding GO:2001070 | The SAGA1 CBM20 domain binds starch in vitro ([PMID:42090253](https://pubmed.ncbi.nlm.nih.gov/42090253/)); whether starch is the main barrier is unclear |
| 6. Stromal CO2 recapture | `stromal_co2_recapture` | LCIB (Q75NZ2) / LCIC (Q75NZ1) | carbonate dehydratase activity GO:0004089 (LCIB) | LCIB rescues CA-deficient yeast and Arabidopsis ([PMID:36856938](https://pubmed.ncbi.nlm.nih.gov/36856938/)); purified Chlamydomonas proteins inactive ([PMID:27911826](https://pubmed.ncbi.nlm.nih.gov/27911826/)) |
| Optional: Ci uptake | `ci_uptake` | HLA3 (A0A2K3E226), LCIA (Q75NZ3) | bicarbonate transmembrane transporter activity GO:0015106 | Oocyte uptake assays for both; LCIA structure with a bicarbonate selectivity filter ([PMID:41507353](https://pubmed.ncbi.nlm.nih.gov/41507353/)) |
| Optional: regulation | `ccm_induction` | CIA5/CCM1 (Q9FED4) | cellular response to carbon dioxide GO:0071244 | Mutant rescue; DNA binding not shown |

Ontology gap: GO has **no biological-process term for a carbon-concentrating
mechanism** of any kind. The module records this as an ONTOLOGY knowledge gap,
and it is a candidate new-term request.

## Gene reviews

All reviews are under `genes/CHLRE/`. Most participants are unreviewed TrEMBL
entries named only by locus, so the folders use the literature symbol and the
UniProt accession is passed explicitly. Falcon deep research was unavailable
for this batch (HTTP 402), so each review was built directly from PubMed and
says so in its notes file.

| Gene (UniProt) | GOA rows | Core function in the review | Matches module? |
|---|---|---|---|
| LCI5 = EPYC1 (Q94ET8) | 0 | molecular condensate scaffold activity; membraneless organelle assembly; pyrenoid | yes |
| rbcL (P00877) | 5 | ribulose-bisphosphate carboxylase activity; CBB cycle; pyrenoid and stroma | yes |
| RBCS1 (P00873) | 4 | contributes to the carboxylase activity; Rubisco complex; pyrenoid | yes |
| SAGA1 (A0A2K3D7T6) | 2 | starch binding; protein-membrane adaptor activity (tentative); pyrenoid tubule | yes, after update |
| RBMP1 = BST4 (A0A2K3DMS8) | 5 | monoatomic ion channel activity; pyrenoid tubule | yes, after update (not a tether) |
| CAH3 (Q39588) | 2 | carbonate dehydratase activity; thylakoid lumen and pyrenoid tubule | yes, after update |
| `BST1` (A0A2K3CTN0) | 5 | monoatomic anion channel activity; thylakoid membrane | yes, after update |
| LCIB (Q75NZ2) | 0 | carbonate dehydratase activity; chloroplast stroma | yes |
| LCIC (Q75NZ1) | 0 | no molecular function; zinc binding, LCIB/LCIC complex, stroma | yes, after update (no CA activity) |
| HLA3 (A0A2K3E226) | 9 | bicarbonate transmembrane transporter activity; plasma membrane | yes |
| LCIA (Q75NZ3) | 6 | bicarbonate transmembrane transporter activity; chloroplast envelope | yes |
| CIA5 / CCM1 (Q9FED4) | 0 | positive regulation of transcription; cellular response to CO2; nucleus | yes (no MF asserted) |

Patterns worth noting for GO curation:

- Four of the twelve proteins had **no GOA annotations at all** (EPYC1, LCIB,
  LCIC, CIA5), despite decades of genetic and structural work.
- Several electronic annotations were wrong in the same way:
  - **Location:** the UniProt ARBA rule placed HLA3 in the vacuole membrane, and
    BST1 and BST4 in the plasma membrane.
  - **IBA from other family members:** the VCCN1 chloride-channel IBA was
    applied to the thylakoid bestrophins, and the formate-transport IBA from
    bacterial FNT channels to LCIA.
- **Ontology gaps:** there is no GO process term for a CO2-concentrating
  mechanism or for pyrenoid assembly, and no complex term for LCIB/LCIC.
  These are raised in the reviews as new-term requests.

Still to do:

- [ ] BST2 (A0A2K3CTQ2) and BST3 (A0A2K3CTP3), the other two module BST
  family members.
- [ ] Ground MITH1, RBMP2 and SAGA2 accessions from the cached papers' `Cre`
  loci, then review them.
- [ ] Regenerate `genes/CHLRE/LCI5/LCI5-pathway.md`, which predates the EPYC1
  re-review.

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
  thylakoid tubules in Chlamydomonas? (The reviews found that the shift is
  modest and now contested.)
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
- Hennacy et al. 2024, SAGA1/MITH1 tubule biogenesis: [PMID:39548241](https://pubmed.ncbi.nlm.nih.gov/39548241/)
- Adler et al. 2024, BST4 (RBMP1) is a tubule channel, not a tether: [PMID:39240724](https://pubmed.ncbi.nlm.nih.gov/39240724/)
- Barrett et al. 2021, pyrenoid review: [PMID:33421532](https://pubmed.ncbi.nlm.nih.gov/33421532/)
