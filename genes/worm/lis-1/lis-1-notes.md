# lis-1 (Caenorhabditis elegans, Q9NDC9) — review notes

## 2026-09-27 — initial review (claude-code)

Sources: UniProt Q9NDC9, cached GOA-cited publications (full text for PMID:17376425, 20005871, 20599902;
abstract-only for 11685578, 15331665, 16996038, 17922003). Deep research (falcon) not yet available when written.

### Core biology
- lis-1 null alleles phenocopy dhc-1 [PMID:15331665 "We identified apparent null alleles of lis-1, which result in defects identical to those observed after inactivation of the dynein heavy chain dhc-1, including defects in centrosome separation and spindle assembly."].
- Localization: cytoplasm, cortex, asters, nuclear periphery, kinetochores; perinuclear targeting requires dhc-1/dnc-1/dnc-2 [PMID:15331665].
- NUD-2/LIS-1 complex recruited to the nuclear envelope by the KASH protein UNC-83; hyp7 nuclear migration defects after lis-1(RNAi) [PMID:20005871 "One consists of the NudE homolog NUD-2 and the NudF/Lis1/Pac1 homolog LIS-1"].
- Centrosome movement from the posterior cortex requires DHC-1 and LIS-1 [PMID:20599902 "When either dynein heavy chain (n=12) or lis-1 (n=4) was inactivated by RNAi, these movements failed and the centrosomes remained in the posterior"].
- Germline: bipolar spindle defects, checkpoint-dependent arrest and apoptosis, slowed corpse engulfment, univalents [PMID:17376425].
- Neurons: GABA synaptic vesicle trafficking defects and convulsion susceptibility [PMID:16996038].

### Decisions
- NEW GO:0140659 cytoskeletal motor regulator activity (consistent with human/fly/module).
- GO:0031022 nuclear migration along microfilament -> MODIFY to GO:0030473 (hyp7 nuclear migration is kinesin-1/dynein, microtubule-based).
- GO:0051661 maintenance of centrosome location IMP -> MODIFY to GO:0051660 establishment of centrosome localization (phenotype is failure of centrosome movement); IBA of same term accepted as PAINT judgment (validator warns about inconsistent actions; intentional).
- cytoplasmic dynein complex / dynein complex -> MODIFY to GO:0005875.
- protein binding (NUD-2) -> REMOVE (no informative MF term; interaction not disputed).
- ARBA signaling / cell communication -> REMOVE; ARBA phagocytosis and IEA synapse, IMP locomotion -> MARK_AS_OVER_ANNOTATED.
