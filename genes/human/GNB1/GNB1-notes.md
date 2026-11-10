# GNB1 (human, P62873) review notes

## Process log

- 2026-10-23: `just fetch-gene human GNB1` had already been run (uniprot, goa, stub
  review with 150 PENDING rows).
- Deep research: `just deep-research-falcon human GNB1 --fallback perplexity-lite` was run
  twice and FAILED both times (falcon: "Exception: Failed to authenticate" from the Edison
  API; fallback perplexity-lite: "Provider 'perplexity' not available"). No
  `-deep-research-*.md` file exists; this review is based on UniProt, the cached
  publications and the notes below.
- `just fetch-gene-pmids human GNB1`: 31/31 publications cached. Additional papers fetched
  with `just fetch-pmid`: 18403039, 1606965, 31300275, 27108799, 25485910, 8521505
  (8538741 was fetched by mistake; it is an unrelated plant paper and is not cited).

## Identity and structure

- GNB1 encodes Gbeta1, the WD40 beta subunit shared by heterotrimeric G proteins. Human
  liver Gs/Gi beta is identical to the rod transducin beta subunit
  [PMID:3095147 "This work proves for the first time that the beta-subunits of all
  signal-transducing G-proteins, including transducin, are the same."].
- Seven-bladed WD40 propeller, obligate dimer with Ggamma, two contact regions with
  Galpha [PMID:8521505 "Repeated WD motifs in beta form a circularized sevenfold beta
  propeller."; "an extended interface between beta and nearly all of gamma"].
- Gbeta has no nucleotide-binding domain. Nucleotide exchange and GTP hydrolysis take place
  on Galpha [PMID:31300275 "activates the G-protein transducin (GT) by catalyzing GDP-GTP
  exchange on its α subunit (GαT)"]. The GOA "GTPase activity" rows on GNB1 (IDA
  PMID:1543505, TAS PMID:3095147) attribute a Galpha activity to Gbeta. The cached abstract
  of PMID:1543505 is a cDNA cloning study of mouse Gbeta4 and says only that
  "The beta and gamma subunits are thought to have a more passive role in G protein function".

## Molecular functions

- **Heterotrimer assembly / receptor coupling.** Gbeta1gamma2 is the standard Gbetagamma
  used in reconstituted and cryo-EM GPCR-G protein complexes (5-HT1B-mini-Go
  PMID:29925951; D2-Gi PMID:32528175; CTR-Gs PMID:28437792; GPR88-Gi1 PMID:35501348;
  muOR-Gi PMID:42870023). Gbeta contacts receptor ICL1/helix 8 in the GCGR-Gs structure
  [PMID:32371397 "There were also limited interactions between the Gβ subunit"]. In a
  coIP screen, Gbeta1 formed heterotrimers with Galphai1/Galphas and essentially every
  Ggamma [PMID:25733868 "G-protein combinations consisting of αi1 or αsL and all possible
  βγ-dimers to form a heterotrimeric complex"]. PAINT represents this with
  "signaling receptor complex adaptor activity" (GO:0030159, IBA).
- **Effector activation by free Gbetagamma.**
  - GIRK channels: purified Gbeta1gamma2 activates reconstituted GIRK2
    [PMID:23739333 "Gβγ by itself is sufficient to activate the GIRK channel"].
    Supports GO:0099104 potassium channel activator activity (IDA).
  - Phospholipase C-beta: [PMID:1606965 "beta gamma subunits, purified from bovine retinal
    transducin (beta gamma t), markedly stimulated the hydrolysis of phosphatidylinositol
    4,5-bisphosphate by this phospholipase C preparation"]. Transducin betagamma is
    Gbeta1gamma1, so this is direct evidence for Gbeta1 (GO:0016004 phospholipase activator
    activity).
  - Ras-GRF: [PMID:8717044 "cotransfection with G-protein beta gamma subunits caused a
    constitutive activation that was sensitive to PP1"]. This is indirect (phosphorylation
    dependent), so it supports GPCR signaling and not a direct Ras pathway role.
- **Other interactors.** p67phox binding is indirect, through Galphai2
  [PMID:16782902 "Based on these data, we concluded that the association between Gβγ and p67
  phox is indirect and mediated through the inactive, GDP-bound Gαi."]. Rhes (RASD2) binds
  Gbeta1 by Y2H [PMID:19255495]. Radil/Rap1 complexes co-purify Gbetagamma [PMID:23209302].
  Chaperone (PFDN5) and huntingtin/neurodegeneration screen interactions are
  high-throughput and functionally uninformative.

## Localization

- Gbetagamma is anchored to the cytoplasmic face of the plasma membrane through Ggamma
  prenylation (the muOR study purified "prenylated Gβγ" from membranes, PMID:42870023).
  Reactome places Gbetagamma in the "cytosol" compartment for 79 reactions; this captures
  the cytoplasmic side but not the membrane anchoring. Kept as non-core.
- In rods GNB1 is the transducin beta subunit (photoreceptor outer segment / disc membrane).
- Exosome, extracellular vesicle and lysosomal-membrane rows come from proteomics (HDA).

## Background paper: Deutsch et al. 2026 (PMID:42870023)

- smFRET of the Galphai alpha-helical domain (AHD) in muOR-Gi complexes. The Gbetagamma
  was human Gbeta1 with Ggamma2 [PMID:42870023 "we used a single virus containing the genes
  for both the human Gβ1 and Gγ2 subunits"], and the WT heterotrimer was Galphai1 beta1
  gamma2 [PMID:42870023 "WT Gi heterotrimer (Gαi1β1γ2) from Hi-5 cells was prepared
  similarly"].
- The paper explains why the dwell times in the open AHD state do not depend on the ligand:
  [PMID:42870023 "possibly because the AHD is affixed against Gβ, as seen in a recent cryo-EM
  structure14"]. This agrees with rhodopsin-transducin structures in which the
  GalphaT helical domain contacts Gbetagamma [PMID:31300275 "capture three distinct
  conformers showing the GαT helical domain (αHD) contacting the Gβγ subunits"].
  This suggests Gbeta1 may do more than anchor Galpha during receptor-catalysed exchange:
  it may also hold the open AHD in place. The paper does not test this directly, so it is
  kept as a suggested question and not added as an annotation.

## Disease

- De novo GNB1 missense variants cause neurodevelopmental disorder with hypotonia and
  seizures (MRD42) [PMID:27108799 "The majority of these 13 mutations affect known Gβ binding
  sites, which suggests that a likely disease mechanism is through the disruption of the
  protein interface required for Gα-Gβγ interaction"].
- Somatic GNB1 mutations (K57, I80) in myeloid/B-cell neoplasms
  [PMID:25485910 "Multiple mutations in GNB1 affect the protein interface that binds Gα
  subunits as well as downstream effectors and disrupt Gα interactions with the Gβγ dimer."].

## Curation decisions (summary)

- GTPase activity: REMOVE. Gbeta has no catalytic site, and the activity belongs to Galpha.
- protein binding: MODIFY to G-protein alpha-subunit binding (GO:0001965) where the partner
  is GNAI1/GNAI2, and to G-protein gamma-subunit binding (GO:0031682) where the partner is
  GNG2/GNG5. REMOVE the other partners (indirect or uninformative).
- signal transduction: MODIFY to GPCR signaling pathway (GO:0007186).
- membrane (ISS): MODIFY to plasma membrane.
- Ras protein signal transduction: MARK_AS_OVER_ANNOTATED, because Gbetagamma acts upstream
  of Ras-GRF and not within the Ras cascade.
- Reactome cytosol (79 rows): KEEP_AS_NON_CORE.
