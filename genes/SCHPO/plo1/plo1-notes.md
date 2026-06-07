# plo1 (Polo-like kinase, S. pombe) — review notes

UniProt: P50528. PomBase: SPAC23C11.16. Sole Polo-like kinase (PLK) of fission yeast.
Architecture: N-terminal Ser/Thr protein kinase domain (aa 41-296; ATP binding 47-55, K69; catalytic Asp/proton acceptor 163) and C-terminal Polo-box domain composed of POLO box 1 (493-575) and POLO box 2 (596-678). The polo boxes form a single functional substrate-targeting module.

## Core function summary
Master mitotic regulator. Ser/Thr kinase activity is biochemically demonstrated. Localizes to SPB (mitotic only), mitotic spindle, spindle midzone, kinetochore, division-site/contractile ring, and (in meiosis) meiotic SPB/spindle/poles and kinetochore. Drives mitotic commitment (positive feedback on Cdc25/MPF via Cut12 at the SPB), bipolar spindle formation, contractile-ring/medial-ring assembly (via Mid1), and septation (initiates SIN). In meiosis (via Moa1/meikin) directs mono-orientation and cohesion protection (Rec8 phosphorylation).

## Key findings with provenance

### Catalytic / kinase activity
- [PMID:11250892 "Plo1-associated casein kinase activity peaked during mitosis before septation. Phosphatase treatment abolished this activity."] — kinase activity, mitotic peak.
- [PMID:22375062 "Dam1 is instead phosphorylated on serine 143 by the Polo kinase homologue, Plo1, during prometaphase and metaphase"] — Ser/Thr kinase activity (direct substrate Dam1).
- [PMID:33888556 "Plo1, purified from bacteria, was shown to phosphorylate the full length of recombinant Rec8 protein"] — direct in vitro Ser/Thr kinase activity.
- Kinase-dead K69R/K69Q loss of function [UniProt MUTAGEN 69].

### Mitotic commitment / G2-M / SPB recruitment
- [PMID:12815070 title "Physical and functional interactions between polo kinase and the spindle pole component Cut12 regulate mitotic commitment in S. pombe."] — Cut12 interaction; mitotic commitment.
- [PMID:15917811 "SRP-mediated phosphorylation of Ser 402 promotes Plo1 recruitment to SPBs and thus commitment to mitosis. Ser 402 phosphorylation also ensures efficient reinitiation of cell tip growth and cell division during recovery from particular stresses."] — links stress pathway to G2-M and cell size/tip growth; intracellular signal transduction.
- [PMID:21965528 "Ark1 phosphorylation of polo kinase Plo1 within the linker region between the kinase domain and polo boxes drives Plo1 onto the spindle poles where it promotes mitosis."] — Aurora drives Plo1 to SPB promoting G2-M; mitotic SPB localization.
- [PMID:23333317 "promoting recruitment of Polo to Cut12 and the SPB and elevating global Polo kinase activity throughout the cell"] — Plo1-Cut12 binding (SPBC649.05 = cut12).
- [PMID:10436027 "Plo1 associates with the mitotic but not interphase spindle pole body (SPB). SPB association of Plo1 is the earliest fission yeast mitotic event recorded to date."] — mitotic SPB localization.

### Spindle / spindle organization
- [PMID:7744248 "Loss of plo1+ function leads to a mitotic arrest in which condensed chromosomes are associated with a monopolar spindle"] — required for bipolar spindle formation.
- [PMID:11250892] Plo1 localizes to mitotic spindle (IDA). PMID:9852154 "Plo1p localizes to the spindle pole bodies and spindles of mitotic cells and also to the medial ring".

### Contractile ring / cytokinesis / septation
- [PMID:7744248 "cells show a failure both in the formation of an F-actin ring and in the deposition of septal material, suggesting that plo1+ function is required high in the regulatory cascade that controls septation"] — actin ring + septum.
- [PMID:21376600 "Plo1 also triggers the recruitment of contractile ring components into medial cortical nodes. Plo1 binds at least two independent sites on Mid1... Plo1 thereby facilitates contractile ring assembly at mitotic onset."] — contractile ring assembly via Mid1/anillin; EXP for regulation of actomyosin ring assembly.
- [PMID:11250892 "We propose that Plo1 acts before the SIN to control septation."] — SIN; positive regulation of septation initiation signaling.
- [PMID:24920823 "Polo-like kinase, which promotes SIN activation, is partially responsible for Byr4 phosphorylation"] and "Cdk1-mediated phosphoregulation of Byr4 facilitates complete removal of Byr4 from metaphase SPBs in concert with Plo1" — SIN activation.
- [PMID:9852154 "Plo1p is thus implicated as a key molecule in the spatial and temporal coordination of cytokinesis with mitosis." / "Plo1p is required for Mid1p to exit the nucleus and form a ring"] — division-site selection; Mid1 nuclear export; nucleus/spindle midzone localization; cytokinesis.
- [PMID:25356547 "two-hybrid in vivo interactions are reported between Plo1p and Sst4p, Vps28p, Vps25p, Vps20p and Vps32p"] — ESCRT interactions (SPAC1142.07c, SPAC1B3.07c, SPBC215.14c are ESCRT genes); septation/membrane trafficking.

### APC / metaphase-anaphase
- [PMID:11777938 "Plo1 kinase physically interacts with the anaphase-promoting complex (APC)/cyclosome through the noncatalytic domain of Plo1 and the tetratricopeptide repeat domain of the subunit, Cut23. A new cut23 mutation, which specifically disrupts the interaction with Plo1, results in a metaphase arrest."] — Cut23(Apc8) interaction (SPAC6F12.14 = cut23); metaphase/anaphase transition.

### Transcription
- [PMID:12411492 "we show that PBF binding activity and consequent gene transcription are regulated by the Plo1p protein kinase, thus invoking a potential auto-feedback loop mechanism that regulates mitotic gene transcription"] — positive regulation of M-G1 transcription (PolII).

### Meiosis
- [PMID:25533956 "These functions are mediated mainly by the activity of Polo-like kinase PLK1, which is enriched to kinetochores in a MEIKIN-dependent manner."] — Plo1/Moa1 mono-orientation + cohesion protection; kinetochore.
- [PMID:28497540 "Moa1 (meikin)... recruits Plo1 (polo-like kinase) to the kinetochores and phosphorylates Spc7 (KNL1) to accumulate Bub1"] — meiotic Bub1 distribution/cohesion protection.
- [PMID:33888556 "The phosphorylation of Rec8 by Moa1-Plo1 potentiates the activity of PP2A associated with Sgo1... prevents cleavage of Rec8 by separase."] — cohesion protection in anaphase I via Rec8-S450.
- [PMID:38448160 "we identify Plo1 phosphorylation sites in the cohesin subunits, Rec8 and Psm3. The non-phosphorylatable mutations at these sites showed specific defects in mono-orientation."] — mono-orientation (homologous chromosome orientation in metaphase I).
- [PMID:22438582 "the polo kinase Plo1, which normally localizes to the SPB during mitosis, is excluded from them in meiotic prophase... artificial targeting of Plo1 to SPBs resulted in an overduplication of SPBs"] — meiotic SPB organization/remodeling; meiotic SPB localization.
- [PMID:23770679 "the microtubule-associated protein complex Alp7-Alp14... is phosphorylated by Polo kinase, which promotes its meiosis-specific association to the outer kinetochore complex Nuf2-Ndc80 of scattered kinetochores"] — meiotic centromere clustering / kinetochore retrieval; kinetochore localization; kinase activity.
- [PMID:20826461] dma1 in spore formation; Plo1 listed as IDA for meiotic spindle/meiotic spindle pole. Abstract is about dma1 but PomBase curated Plo1 meiotic spindle/pole localization from full text (defer to curator).

### Localization (large-scale / phosphoproteomics)
- [PMID:16823372] ORFeome global localization — cytoplasm/cytosol/SPB (HDA).
- [PMID:33176152 "acute HS results in the segregation and aggregation of multiple nuclear and nucleolar proteins into ring-like structures located at the nucleolar periphery (nucleolar rings [NuRs])"] — Plo1 sequestered into nucleolar inclusion bodies under heat stress; reversible aggregation, NOT a normal functional location.
- [PMID:25487150 "A PP1-PP2A phosphatase relay controls mitotic progression"] — Plo1 IDA kinase activity in mitotic-progression context.

## Curation considerations
- "protein binding" (GO:0005515) IPI annotations: not informative MF; mark over-annotated (the interactions themselves — Cut12, Cut23, Mid1, ESCRT, Moa1 — are real and underpin BP terms).
- nucleolar peripheral inclusion body (PMID:33176152): real IDA localization but it is a stress-induced aggregation site, not a site of normal function — keep as non-core.
- IEA terms (protein kinase activity, ATP binding, Ser kinase activity, nucleus, SPB) are supported by experimental data; generally ACCEPT (ATP binding, Ser kinase) or note redundancy.
- Defer to PomBase curators on all IDA/IMP/IPI/IGI experimental annotations per project rules.
