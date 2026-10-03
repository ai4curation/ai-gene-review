# EHD1 curation notes

## Deep research status
- `just deep-research-falcon human EHD1` was attempted (unavailable perplexity-lite fallback; then `--timeout 2400`, killed with exit 137; then retried). See the end of this file for the final outcome. The review was written from cached primary literature.

## Key findings (with provenance)
- ATPase, not GTPase [PMID:15710626 "we show that both Caenorhabditis elegans and mouse RME-1 proteins bind and hydrolyze ATP. No significant GTP binding or hydrolysis was detected."]; ATP binding drives oligomerization and endosome association [PMID:15710626 "ATP binding is required for oligomerization of mRme-1/EHD1, which in turn is required for its association with endosomes"]
- Endocytic recycling [PMID:15020713 "Depletion of either EHD1 or Rabenosyn-5 delayed the recycling of transferrin and major histocompatibility complex class I to the plasma membrane."]; [PMID:17233914 "loss of EHD1 and 3 (and to a lesser extent EHD4) but not EHD2 function retarded transferrin exit from the endocytic recycling compartment"]
- MICAL-L1 recruits EHD1 to tubular recycling endosomes and links it to RAB8A [PMID:19864458 "endogenous MICAL-L1 can link both EHD1 and Rab8a to these structures, as its depletion leads to loss of the EHD1-Rab8a interaction"]
- EHD1 vesiculates, EHD3 stabilizes tubular recycling endosomes [PMID:27189942 "EHD1 induces membrane vesiculation, whereas EHD3 supports TRE biogenesis and/or stabilization by an unknown mechanism."]
- Ciliary vesicle assembly [PMID:25686250 "EHD-dependent membrane tubulation is essential for ciliary vesicle formation from smaller distal appendage vesicles (DAVs)."]; required for CP110 loss [PMID:25686250 "In contrast, in EHD1-depleted cells 80% of cells had CP110 localized to both centrioles"]; ciliary pocket [PMID:25686250 "EHD1 and EHD3 localize to preciliary membranes and the ciliary pocket."]
- MICAL-L1 recruits EHD1 to basal bodies [PMID:31615969 "upon MICAL-L1-depletion, EHD1 fails to localize to basal bodies"]
- Acts downstream of myosin-Va delivery [PMID:29335527 "Myosin-Va functions upstream of EHD1- and Rab11-mediated ciliary vesicle formation."]

## Pleiotropy: ciliary vs other roles
- Core non-ciliary role: endocytic recycling ATPase on tubular recycling endosomes (ACCEPT).
- Ciliary role: ciliary vesicle assembly + cilium assembly (ACCEPT existing; NEW GO:1905556).
- Tissue-specific rodent-transferred roles (cholesterol homeostasis/storage, LDL clearance, lipid droplet, neuronal projection/NGF response, synapse, myoblast fusion, platelet DTS): KEEP_AS_NON_CORE.

## Curation decisions (summary)
- GTP binding IEA: MODIFY -> ATP binding; NEW ATP hydrolysis activity (ISS, PMID:15710626).
- Ciliary membrane IEA: MODIFY -> ciliary pocket membrane.
- Small GTPase binding (RAB8A) IPI: MARK_AS_OVER_ANNOTATED (bridged by MICAL-L1).
- Protein binding x20: REMOVE; identical protein binding and homooligomerization: ACCEPT (dimerization/oligomerization is functionally essential).
- NEW ciliary vesicle assembly (GO:1905556, IMP, PMID:25686250): EHD1 performs the tubulation/fusion step. Comparator check: no gene product in GO currently carries GO:1905556 (QuickGO, all taxa), so there is no contrary convention; the term definition (small vesicles dock to transitional fibres and fuse) matches the EHD1 step exactly.

## HPA cilium atlas vs module role
- Module: stage 2_ciliary_vesicle, "ciliary vesicle formation", membrane-shaping ATPase in the EHD1/EHD3 membrane tubulation step; process ciliary vesicle assembly, location ciliary vesicle; MF not asserted.
- HPA v25: Primary cilium (S), Primary cilium transition zone (S); main location plasma membrane. GOA carries HPA rows (GO_REF:0000052) for cilium, ciliary transition zone and plasma membrane (all ACCEPT).
- Assessment: consistent. HPA proximal cilium/transition-zone signal matches the ciliary pocket localization in ciliated cells (the CV-assembly step itself is transient and precedes the cilium). core_functions agree with the module and fill its open MF slot with ATP hydrolysis activity.
