# cup (Q9VMA3) review notes

Module context: dmel_eif4e_cup_complex (Cup with eIF4E1).

Deep research: the first falcon attempt failed (timeout/killed; perplexity unavailable); a retry produced `cup-deep-research-falcon.md` after the review was drafted. It agrees with this review: Cup is described as a cytoplasmic mRNP adaptor and translational repressor, not an enzyme, acting in germline P bodies; it also notes newer roles in cycA/cycB mRNA partitioning and CTLH-mediated clearance at the maternal-to-zygotic transition (not in GOA).

## Molecular function
- Cup is an eIF4E-binding protein (4E-BP) of the 4E-T family. [PMID:14685270 "Cup is an eIF4E-binding protein that blocks the binding of eIF4G to eIF4E"]
- Binding uses a canonical and a non-canonical motif on two faces of eIF4E. [PMID:22832024 "two separate segments of Cup contact two orthogonal faces of eIF4E"]; [PMID:25179781 "the II-AA mutations disrupted the association of eIF4E with CUP, Thor and 4E-T but not with eIF4G"]
- eIF4E-independent effector domain: [PMID:21937713 "CUP maintains mRNA targets in a repressed state by promoting their deadenylation and protects deadenylated mRNAs from further degradation"]; [PMID:21937713 "This domain associates with the deadenylase complex CAF1-CCR4-NOT and decapping activators"]
- Smaug complex reconstitution: [PMID:36951092 "The Smaug-dependent complex represses translation of nanos and induces its deadenylation by the CCR4-NOT deadenylase"]
- No RNA-binding domain; recruited indirectly: [PMID:14685270 "Cup mediates an indirect interaction between Smaug and eIF4E"]; [PMID:37553798 "For osk mRNA, the current model suggests that Bru1 recruits Cup to the transcript, forming a Bru1-Cup-eIF4E translational repression complex"]

## Biological roles
- oskar repression: [PMID:14723848 "Cup is required to repress precocious osk translation"]; mechanism [PMID:16469699 "inhibition of small ribosomal subunit recruitment to oskar mRNA"]
- oskar localization / Barentsz recruitment: [PMID:14691132 "cup is required for oskar mRNA localization and is necessary to recruit the plus end-directed microtubule transport factor Barentsz to the complex"]
- gurken: [PMID:18082158 "We show that cup mutants lay dorsalized eggs"]
- NMJ: [PMID:26102195 "we show that zygotic Cup protein is localized to presynaptic terminals at larval neuromuscular junctions (NMJs)"]

## Localization
- Shuttling: [PMID:15465908 "Cup is a nucleocytoplasmic shuttling protein and that the interaction with eIF4E promotes retention of the Cup protein in the cytoplasm"]
- P bodies: [PMID:37553798 "Cup has also been identified as a processing body (P-body) component due to its association with two core P-body proteins, Me31B and Trailer Hitch (Tral)"]
- The NOT P-body annotation (PMID:24335285) is from GFP-Cup in HeLa cells: [PMID:24335285 "we observed that Drosophila Cup, which lacks these sequences, does not localize to P-bodies in HeLa cells"] -- removed as heterologous and contradicted by native-context data.

## Decisions
- Protein binding rows: eIF4E partners -> MODIFY to GO:0008190; others REMOVE (uninformative).
- RNA binding IDA (PMID:16469699, abstract only) -> UNDECIDED; mRNA binding IBA -> over-annotation.
- protein-RNA adaptor activity -> over-annotation (Cup bridges Bru1/Smaug to eIF4E, protein-protein).
