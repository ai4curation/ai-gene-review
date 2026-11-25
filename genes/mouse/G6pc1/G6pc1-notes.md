# G6pc1 notes

Deep-research status: the Falcon and Perplexity providers were unavailable on 2026-11-24, so this review used the seeded GOA rows, UniProt, cached publications, PTHR12591 PAINT data, the human G6PC1 review, the mouse G6pc2 review and GO-CAMs 61e0e55600001225 / 62d0afa500000298.

## Core role

- G6pc1 is the mouse liver/kidney/intestine glucose-6-phosphatase catalytic subunit. The cloned murine cDNA encodes a membrane-bound enzyme whose in-vitro expression matched liver microsomal G6Pase [PMID:8407995, "the in vitro expressed enzyme is indistinguishable from mouse liver microsomal glucose-6-phosphatase"].
- It couples to Slc37a4/G6PT in the ER glucose-6-phosphatase system: Slc37a4 transports G6P into the ER lumen and G6pc1 hydrolyzes it to glucose plus phosphate [PMID:11121425, "G6PT translocates G6P from the cytoplasm to the lumen of the endoplasmic reticulum where it is metabolized by G6Pase to glucose and phosphate."].
- G6pc1 loss blocks the terminal glucose-production step shared by gluconeogenesis and glycogenolysis. G6pc1-null mice model GSD1a, and adenoviral G6pc1 replacement restores hepatic G6Pase activity, normalizes plasma glucose/lipid/urate values and reduces liver/kidney glycogen accumulation [PMID:10625614, "Hepatic G6Pase activity in Ad-mG6Pase-infused mice was restored to 19% of that in G6Pase(+/+) mice at 7-14 days post-infusion"].
- Later liver-specific mRNA and CRISPR repair models support the same assignment in adult liver: liver-specific G6PC-null mice lose hepatic G6Pase and cannot maintain fasting glucose, and corrected G6Pase activity restores fasting tolerance [PMID:29428299; PMID:33359667].

## Peripheral rows

- Triglyceride, cholesterol and urate homeostasis are retained as non-core metabolic consequences of GSD1a physiology: loss of the terminal G6Pase step redirects substrate into glycogen and lipid pools and perturbs plasma metabolites, but G6pc1 is not a lipid or urate enzyme.
- The steroid-metabolism row from PMID:17588937 is ER substrate-pool crosstalk. G6pc1 and H6pd both consume luminal G6P, and G6P trafficking regulates H6pd-dependent 11beta-HSD1 reductase activity; the direct G6pc1 activity remains G6P hydrolysis.
- The GO:0015760 glucose-6-phosphate transport rows were marked over-annotated. PMID:8640227 shows the separate transport and hydrolysis proteins are tightly coupled, which explains why G6pc1 perturbation alters apparent transport, but Slc37a4 is the transporter and G6pc1 is the downstream phosphatase.
- The GO:0016773 phosphotransferase row is a measured disrupted-microsome side activity from PMID:8407995 rather than an established physiological reaction, so it is over-annotated under the measured-activity policy.

## GO-CAM context

Both gluconeogenesis GO-CAMs put G6pc1 at the terminal ER glucose-6-phosphate hydrolysis step downstream of Slc37a4. The activity uses GO:0004346, GO:0006094 and GO:0005783; that is consistent with the review. The ER root is coarser than the active ER-membrane location but is informative and correct under the root-organelle policy.
