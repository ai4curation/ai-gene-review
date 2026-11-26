# MICU3 (Q86XE3) review notes

Journal for the AI review of human MICU3, mitochondrial calcium uptake 3, for the
MICU3 GO-CAM model.

## Research inputs

The seed was created with `just fetch-gene human MICU3`, which downloaded the
UniProt and GOA files and produced 27 existing GOA rows.

Automated deep research could not be generated in this runtime. Falcon was not
available in the current provider set, and the requested Perplexity fallback was
also unavailable. This review therefore uses the local MICU3 publications cached
under `publications/`, the UniProt record, Reactome records, PANTHER family
membership, the local sibling MICU1/MICU2 reviews, and the GO-CAM review for
`65d7e4ac00002435`.

`just paint-losses human MICU3` reported no IRD or IKR loss on the human MICU3
lineage, so the PAINT rows were judged on source granularity rather than on a
lineage-specific loss.

## Core biology

- PMID:29725115 is the central human MICU3 paper. It shows that MICU3 is a
  brain-enriched EF-hand protein, forms a disulfide-mediated dimer with MICU1
  but not MICU2, enhances MCU-dependent mitochondrial Ca2+ uptake, and is needed
  for synaptic-activity-evoked mitochondrial Ca2+ transients in primary cortical
  neurons [PMID:29725115 "We show that MICU3 forms a disulfide bond-mediated
  dimer with MICU1, but not with MICU2, and it acts as enhancer of
  MCU-dependent mitochondrial Ca2+ uptake."].
- PMID:30699349 is cached as abstract only. The abstract is still enough to
  confirm that human MICU3 was structurally analysed as a Ca2+-responsive MICU
  EF-hand protein [PMID:30699349 "Here, we determined multiple crystal
  structures of MICU2 and MICU3 from Homo sapiens."].
- PMID:31862210 is a rat neuronal study showing that MICU3 is the factor that
  gives axonal mitochondria a lower threshold for activity-driven Ca2+ uptake,
  allowing local ATP synthesis to accelerate under oxidative fuel conditions
  [PMID:31862210 "Ablation of MICU3 renders axonal mitochondria similar to
  non-neuronal mitochondria, prevents acceleration of local ATP synthesis, and
  impairs presynaptic function under oxidative conditions."].

MICU3's two core molecular functions in GO terms are `GO:0061891` calcium ion
sensor activity and `GO:0046982` protein heterodimerization activity. They are
coupled in the biology: the functional sensor is the MICU1-MICU3 heterodimer on
the IMS side of the MCU/EMRE pore, and Ca2+ binding changes how that regulatory
dimer gates MCU-dependent import into the matrix.

UniProt records MICU3 as expressed in the central nervous system and skeletal
muscle, and infers a skeletal-muscle uptake role by similarity from mouse Micu3
[file:human/MICU3/MICU3-uniprot.txt "CC       also required to increase
mitochondrial calcium uptake in skeletal"].

The cellular component rows are complementary rather than conflicting. MICU3 is
a soluble intermembrane-space regulator, but it acts while associated with the
mitochondrial inner membrane through the uniplex complex.

## Annotation decisions

- `GO:0005509`, `GO:0061891`, `GO:0046982`, `GO:0036444`, `GO:0051560` and
  `GO:1990246` are all core MICU3/uniplex terms and were accepted for every
  evidence source.
- `GO:0005739` was accepted under the root-organelle policy. The more precise
  `GO:0005758` and `GO:0005743` rows were also accepted because MICU3 senses
  Ca2+ from the IMS side of the inner-membrane uniporter.
- `GO:0006851` mitochondrial calcium ion transmembrane transport was accepted
  at its own source granularity, as in the MICU1 and MICU2 reviews. MICU3
  regulates Ca2+ transport across the inner membrane even though MCU, not
  MICU3, is the conducting pore.
- `GO:0071277` cellular response to calcium ion was kept as non-core. MICU3 is
  a Ca2+-responsive protein, but the sharper mechanism is already captured by
  calcium ion sensor activity plus calcium import into the mitochondrion.
- `GO:0001956` positive regulation of neurotransmitter secretion was marked as
  over-annotated. Rat MICU3 loss impairs presynaptic function under oxidative
  fuel conditions by disrupting mitochondrial Ca2+ uptake and local ATP
  flexibility, but the clearest vesicle-cycle phenotype is slowed recycling
  rather than direct regulation of neurotransmitter exocytosis.

## Upstream source defects

The UniProt MICU3 `CC:DOMAIN` note says EF-hand domains 1 and 3 "act as sensors
of mitochondrial matrix calcium levels". That appears to name the wrong side of
the inner membrane: MICU3 is an intermembrane-space regulator associated with
MCU/EMRE, and it senses the extramitochondrial Ca2+ that will enter the matrix.
The review records this as a `PROBABLE` `UNIPROT` `WRONG_STATEMENT` defect.

## GO-CAM consistency

The GO-CAM model activity for MICU3 is directionally consistent with this gene
review: both put MICU3 at `GO:0061891` calcium ion sensor activity in the
mitochondrial inner membrane with `GO:0036444` calcium import into the
mitochondrion as the nested process context.

The model uses `GO:0071277` cellular response to calcium ion as the outer
process while this gene review treats that term as a correct but broad
contextual annotation. The more specific nested import process is the direct
mechanism and matches the core functions here.

The model's MICU3-to-MCU positive causal edge still cites PMID:32494073, a
MICU1-MICU2 holocomplex structure paper, rather than PMID:29725115, the primary
MICU3 enhancer paper. That wrong-reference defect is already recorded in the
GO-CAM review and should be carried into the final GO-CAM consistency-notes PR
after the gene PR has merged.
