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
- [PMID:34133218 "Although the Polo kinase Plo1 is not necessary for Sad1 redistribution, it localizes to the SPB region connected to the centromere, and its activity is vital for redistribution of other SPB ring proteins and for complete NEBD at the SPB to allow for SPB insertion."] — direct SIM and chemical-genetic support for Plo1 at the nuclear-facing SPB and for its role in localized NE breakdown/SPB insertion. The authors explicitly state that direct phosphorylation of Sad1 has not been detected, so the substrate remains unresolved.
- [PMID:21131906 "Sid4 ubiquitination delays recruitment of the Polo-like kinase and SIN activator, Plo1, to spindle pole bodies (SPBs)"] — Dma1-dependent Sid4 ubiquitination controls the timing of Plo1 recruitment during checkpoint arrest; this paper supports regulated SPB recruitment, while Plo1 kinase activity is established more directly by the assays cited above.

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
- The 2026 GOA refresh added PMID:34133218 annotations to the half bridge, inner plaque, and mitotic SPB insertion. Accept all three: the full text directly places the bulk Plo1 signal at the INM/nuclear face and shows that acute Plo1 inhibition disrupts ring remodeling and insertion. Do not infer a direct Sad1 substrate relationship; the paper says this has not been detected.

## 2026-09-01 research refresh

- The project wrapper refreshed 76 GOA rows and added four new annotations: an IDA kinase annotation from PMID:21131906 and three PMID:34133218 annotations covering the half bridge, inner plaque, and mitotic SPB insertion. All were manually reviewed; no PENDING actions remain.
- OpenScientist tested the focused hypothesis that Plo1 directly phosphorylates an SPB-ring component. It judged the process claim supported but the direct-substrate clause unresolved, agreeing with the full-text statement that direct Sad1 phosphorylation has not been detected. This constrained the core-function wording and generated a substrate-identification experiment rather than a new MF assertion.
- Falcon's broader synthesis corroborated the existing core modules and highlighted the unusually direct meiotic Rec8/Psm3 substrate evidence. It is retained as research provenance, while annotation decisions cite the cached primary literature.
- Meiosis is kept outside `core_functions` despite the unusually direct Rec8/Psm3 substrate evidence because it is a stage-specific deployment of the same Plo1 kinase rather than the constitutive organizing role that makes Plo1 essential in vegetative M phase. The individual meiotic annotations remain retained as non-core, not discounted or removed.

## 2026-11-01 PMID:23222840 integration (Grallert et al. 2013, Nat Cell Biol)

Cached text: abstract plus PMC author-manuscript main text (results and discussion). Figure legends, methods and supplementary figures are NOT in the cache; claims below rest on the main-text narrative.

- Late-G2 SPB recruitment and activity: [PMID:23222840 "Time lapse imaging revealed that Plo1 was initially recruited around 30 minutes before mitosis (Figure 1a-c). This initial recruitment was advanced by a further 30 minutes in cut12.s11 cells"]; FRAP half-life 21-22 s; MPM2 SPB staining is Plo1-dependent and reports local Plo1 activity.
- MPF dependency: [PMID:23222840 "indicating that MPF activity is continuously required for Plo1 association with the late G2 SPB"] (cdc2.as + 1NA-PP1; washout restores Plo1 at the SPB).
- Mitotic-commitment timing (loss of function): [PMID:23222840 "Addition of 20 μM 3-BrB-PP1 to G2 plo1.as8 cells delayed the phosphorylation of histone H3 serine 10 that accompanies mitotic commitment by 40 minutes"]. plo1.as8 = M→F gatekeeper-region change in a plo1.as3 backbone; strong inhibition gives monopolar spindles.
- SPB-tethered active Plo1 (GBP chimera Plo1.RL): [PMID:23222840 "Plo1.RL activation at SPBs via recruitment to Cut12.NEGFP promoted mitotic commitment (Figure 2a). A lower level of mitotic induction arose from recruitment to the SPB components Pcp1.GFP and Sid4.GFP while none followed targeting to any other location"]; requires functional endogenous Plo1 (fails in plo1.ts41).
- SPB-tethered Cdc2.RL acts through Plo1: [PMID:23222840 "Consistently, this ability of Cut12.NEGFP anchored Cdc2.RL to induce mitosis relied upon Plo1 activity (Figure 2e)."]
- NETO: coincident with Plo1 SPB recruitment ("every post-NETO G2 cell displayed a Plo1.GFP signal at its SPB while neighbouring pre-NETO cells had none"); [PMID:23222840 "NETO execution was severely compromised by Plo1 inactivation (Figure 3c, Supplementary Figure 1g)."]; [PMID:23222840 "NETO was triggered when Plo1.RL was activated at the SPBs of cdc10.v50 cells but nowhere else, including recruitment to the cell end itself through either Tea1.v5GFP or For3.GFP fusion proteins"]; [PMID:23222840 "Critically, this ability of Cut12.NEGFP anchored Cdc2.RL to induce NETO was reliant on Plo1 activity (Figure 4d)."] MPF-induced NETO also needs Tea1, Bud6 and Sla2.

Curation decisions:
- Added the reference with findings and reference_review (HIGH/VERIFIED).
- GO:0010971 (positive regulation of G2/M transition, IMP PMID:21965528 row) gains PMID:23222840 supporting quotes; no new G2/M row (term already carried twice by IMP).
- SPB localization: no new CC row; GO:0044732 mitotic SPB / GO:0005816 SPB already carried, and the late-G2 SPB is part of the vegetative (mitotic-cycle) SPB.
- NEW GO:0051523 "cell growth mode switching, monopolar to bipolar" (IMP, PMID:23222840). Term choice: GO:0051519 activation of bipolar cell growth is obsolete; GO:0051518 positive regulation of bipolar cell growth is the alternative, but GO:0051523 names the NETO switch itself and sits under regulation of direction of cell growth. Comparator check (QuickGO, S. pombe): GO:0051523 is carried by IMP for signalling regulators of NETO such as ssp1, kin1, rgf1, tea3, so a regulatory kinase is the conventional bearer. Kept out of core_functions (single paper; downstream targets unknown), but mentioned in description.
- Core function 2 (mitotic commitment) description extended with MPF-dependent late-G2 SPB activation, with two PMID:23222840 quotes.
- cdc2 review: NEW GO:0051523 for cdc2 too (IMP: strong cdc2.as inhibition blocks NETO; SPB-tethered Cdc2.RL triggers NETO, Plo1-dependent).
