# G6pc3 notes

Deep-research status: the Falcon and Perplexity providers were unavailable on 2026-11-24, so this review used the seeded GOA rows, UniProt, cached publications, PTHR12591 PAINT data, the human G6PC3 review, the mouse G6pc2 review and GO-CAMs 61e0e55600001225 / 62d0afa500000298.

## Core role and substrate scope

- G6pc3 / UGRP / G6Pase-beta is a broadly expressed G6PC paralog, not the liver/kidney/intestine G6pc1 isoform. The mouse cloning paper found a 346-aa G6pc3 protein with G6pc1-like topology and broad mRNA expression, but its early assay did not detect G6P hydrolysis [PMID:14765991].
- The G6Pase activity is nevertheless real. Mouse astrocytes express G6pc3 and Slc37a4 activities that couple into an active G6Pase complex [PMID:15661744, "these activities can couple to form an active Glc-6-Pase complex"], and G6pc3-null mouse brain homogenates lose about half their G6P hydrolytic activity [PMID:17023421].
- G6pc3 is not the systemic fasting-glucose enzyme: G6pc3-null mice have normal blood glucose, hepatic glycogen and triglycerides, contrasting with G6pc1 deficiency [PMID:17023421, "G6Pase is the major glucose-6-phosphatase of physiological importance for glucose homeostasis in vivo"]. For that reason the gluconeogenesis rows are kept as non-core local glucose-production context rather than treated as the central physiological role.
- The best supported conserved role is clearing 1,5-anhydroglucitol 6-phosphate. Human G6PC3 hydrolyzes 1,5AG6P, deficient human cells accumulate it, and G6PC3-deficient mouse neutrophils die when exposed to physiological 1,5AG; lowering 1,5AG with an SGLT2 inhibitor rescues neutrophils in vivo [PMID:30626647, "G6PC3 and G6PT collaborate to dephosphorylate 1,5AG6P"]. That supports adding GO:1990748 cellular detoxification and a proposed 1,5AG6P phosphatase term.

## Propagation and transport rows

- The PTHR12591 activity and ER-location IBAs are sound for all three mammalian paralogs. `just paint-losses mouse G6pc3` reports no PAINT loss on the G6pc3 lineage.
- The PTHR12591 gluconeogenesis IBD is seeded by G6pc1 orthologs and by mouse/rat G6pc3. G6pc3 is therefore not a simple unsupported passenger, but the process is secondary and local for G6pc3 and should not make it a second terminal hepatic gluconeogenesis enzyme beside G6pc1.
- The GO:0015760 glucose-6-phosphate transport IGI row overstates G6pc3's role. G6pc3 hydrolyzes imported substrates in the ER lumen; Slc37a4/G6PT performs the transport.

## GO-CAM context

The two gluconeogenesis GO-CAMs place G6pc3 in the same terminal reaction position as G6pc1. The glucose-6-phosphatase activity and ER location are real, but the review keeps GO:0006094 as non-core for G6pc3. The activity therefore remains biologically related rather than fully consistent with G6pc3's core function.
