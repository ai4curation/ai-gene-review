# DDP1 (YOR163W, Q99321) notes

- Nudix (MutT) hydrolase; (di)adenosine polyphosphate hydrolase, Ap6A preferred [PMID:10085096 "we have shown the product to be a (di)adenosine polyphosphate hydrolase with a previously undescribed substrate specificity"].
- Also hydrolyses inositol pyrophosphates (DIPP activity) [PMID:10419486 "the efficient hydrolysis of diphosphorylated inositol polyphosphates"]; [UniProt:Q99321 "cleaves a beta-phosphate from the diphosphate groups in PP-InsP5"].
- Endopolyphosphatase [PMID:21775424 "possesses a robust poly-P endopolyphosphohydrolase activity"]; [PMID:31175919 "Ppn2, Ppn1, and Ddp1 had endopolyphosphatase activities, whereas Ppx1 did not."].
- In vitro mRNA decapping [PMID:23353937 "Ddp1p, also possesses decapping activity in vitro"] - non-core.
- Localization cytoplasm + nucleus (GFP) [UniProt:Q99321 "SUBCELLULAR LOCATION: Cytoplasm ... Nucleus"].

## Curation decisions
- YeastPathways RCA "inositol phosphate biosynthetic process" is superpathway inheritance for a catabolic (PP-InsP -> InsP) enzyme: MODIFY to GO:0071544 diphosphoinositol polyphosphate catabolic process.
- Core MF: GO:0008486 (PP-InsP phosphatase) + GO:0034431 (Ap6A hydrolase). PolyP catabolism kept non-core (Ppn1/Ppn2/Ppx1 dominant).
