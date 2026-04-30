# EIF2AK3 notes

## Core literature picture

PERK is an ER-resident transmembrane stress-sensor kinase whose defining activity is phosphorylation of EIF2S1/eIF2alpha to attenuate translation during ER stress [PMID:9930704 Protein translation and folding are coupled by an endoplasmic-reticulum-resident kinase., "ER stress increases PERK's protein-kinase activity and PERK phosphorylates eIF2alpha on serine residue 51, inhibiting translation of messenger RNA into protein."].

The membrane placement is also explicit in the foundational paper and supports preferring ER membrane over generic ER/cytoplasm terms [PMID:9930704 Protein translation and folding are coupled by an endoplasmic-reticulum-resident kinase., "Here we describe the cloning of perk, a gene encoding a type I transmembrane ER-resident protein."].

BiP release and oligomerization-dependent activation support the core PERK-mediated UPR picture rather than a generic signaling or ER-overload label [PMID:11907036 Dimerization and release of molecular chaperone inhibition facilitate activation of eukaryotic initiation factor-2 kinase in response to endoplasmic reticulum stress., "In the absence of stress, PEK associates with ER chaperones GRP78 (BiP) and GRP94, and this binding is released in response to ER stress."].

PERK luminal-domain tetramerization and eIF2alpha phosphorylation further support a direct PERK-branch UPR annotation [PMID:25925385 Crystal structures reveal transient PERK luminal domain tetramerization in endoplasmic reticulum stress signaling., "interface mutations that disrupt tetramer formation in vitro reduce phosphorylation of PERK and its target eIF2α in cells. These results suggest that transient conversion from dimeric to tetrameric state may be a key regulatory step in UPR activation."].

Direct misfolded-protein recognition is experimentally supported and justifies retaining `misfolded protein binding` as a core sensing function [PMID:27917829 The ER stress sensor PERK luminal domain functions as a molecular chaperone to interact with misfolded proteins., "the PERK luminal domain can recognize and selectively interact with misfolded proteins but not native proteins."].

## PN framing used here

The PN prompt was useful for prioritization, but only the literature-backed pieces were kept as core: regulation of translation, negative regulation of translation in response to stress, integrated stress response signaling, and PERK-mediated ER-stress/UPR biology [PMID:9930704 Protein translation and folding are coupled by an endoplasmic-reticulum-resident kinase., "ER stress increases PERK's protein-kinase activity and PERK phosphorylates eIF2alpha on serine residue 51, inhibiting translation of messenger RNA into protein."].

I added `integrated stress response signaling` as a `NEW` annotation because PERK is one of the named ISR sensor kinases and the EIF2S1 phosphorylation/translation attenuation mechanism is explicit in the PERK literature [PMID:9930704 Protein translation and folding are coupled by an endoplasmic-reticulum-resident kinase., "ER stress increases PERK's protein-kinase activity and PERK phosphorylates eIF2alpha on serine residue 51, inhibiting translation of messenger RNA into protein."].

I added `regulation of IRE1-mediated unfolded protein response` as a contextual `NEW` annotation, but not as a core function, because the literature supports cross-talk rather than a primary defining role [PMID:30118681 Coordination between Two Branches of the Unfolded Protein Response Determines Apoptotic Cell Fate., "Here, we report that PERK governs IRE1's attenuation through a phosphatase known as RPAP2 (RNA polymerase II-associated protein 2)."].

## Contextual roles retained as non-core

Wolcott-Rallison syndrome phenotypes support keeping pancreas and skeletal-development terms as contextual outcomes rather than core functions [PMID:12086964 Loss of kinase activity in a patient with Wolcott-Rallison syndrome caused by a novel mutation in the EIF2AK3 gene., "Our data demonstrate that EIF2AK3 kinase activity is essential for pancreas islet function and bone development in humans"].

Tumor stress biology such as glucose starvation, VEGF induction, and angiogenesis is literature-supported but context-dependent and should stay separate from the core PERK proteostasis role [PMID:22915762 The unfolded protein response induces the angiogenic switch in human tumor cells through the PERK/ATF4 pathway., "Collectively, these results show that the PERK/ATF4 arm of UPR mediates the angiogenic switch and is a potential target for antiangiogenic cancer therapy."].

ER-stress-induced apoptosis is also a downstream context, not a defining homeostatic function [PMID:23000344 Ursolic acid induces ER stress response to activate ASK1-JNK signaling and induce apoptosis in human bladder cancer T24 cells., "Salubrinal inhibits ursolic acid-induced CHOP expression, Bim ER accumulation and caspase-3 activation in T24 cells."].

Stress-induced recruitment to mitochondria-associated ER contact sites looks real but contextual [PMID:39116259 PERK-ATAD3A interaction provides a subcellular safe haven for protein synthesis during ER stress., "PERK-ATAD3A interactions increased during ER stress, forming mitochondria-ER contact sites."].

## Cautionary removals

I removed tyrosine kinase terms because the literature supports PERK as an eIF2alpha serine kinase; Tyr619 is discussed as a regulatory phosphorylation site rather than evidence that PERK is a bona fide protein tyrosine kinase [PMID:22169477 H2S-Induced sulfhydration of the phosphatase PTP1B and its role in the endoplasmic reticulum stress response., "PERK, which phosphorylates the eukaryotic translational initiation factor 2, leading to attenuation of protein translation, was a direct substrate of PTP1B."].

I removed the `cytosol` Reactome-based annotation because the local Reactome entry is clearly about an `EIF2AK3-ALK` fusion and not native PERK [Reactome:R-HSA-9700131 ALK mutants bind type I TKIs, "EIF2AK3(30-144)-ALK(1058-1620)"].

I treated broad binding and very generic signaling terms conservatively when they did not sharpen the PERK story beyond the ISR/ER-stress framework.
