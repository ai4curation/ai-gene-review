# GDI1 notes

## Deep research

- The Falcon and Perplexity providers were unavailable in the retained environment during this GO-CAM batch on 2026-11-24, so this review does not retry those unavailable providers.
- The GDI1 review uses a manual synthesis from the cached UniProt record, the GO-CAM context, and primary literature instead of a generated `GDI1-deep-research-*.md` provider file.

## Functional synthesis

GDI1/Rab GDI alpha is a soluble Rab GDP-dissociation inhibitor. It binds prenylated GDP-bound Rabs, suppresses nucleotide exchange while the Rab is in the soluble complex, extracts inactive Rabs from membranes, and thereby maintains a cytosolic Rab:GDI pool for repeated membrane-delivery cycles [PMID:19570034; PMID:23815289].

- GDI1 preferentially interacts with RAB10, while the paralog GDI2 favors RAB4A, in the insulin-stimulated GLUT4-trafficking system; both GDIs localize with RAB10 and GLUT4 at the trans-Golgi network and peripheral cytoplasm [PMID:19570034].
- The Legionella SidM/DrrA structural paper captures the same core mammalian mechanism from the pathogen side: host prenylated Rab1:GDP is sequestered by GDI1 in the cytosol, and Rab1 activation requires GDI displacement [PMID:19942850].
- In the RNF115/TLR GO-CAM pathway, GDI1 is recruited to RAB1A and RAB13; RNF115-catalyzed K11-linked ubiquitination of RAB1A and RAB13 blocks this recruitment and inhibits Rab recycling, thereby limiting TLR post-ER and post-Golgi trafficking [PMID:35343654].
- Several large human interactome papers report GDI1 interactions with RAB1A, RAB4A, LNX1, and USP25. Rows to RAB1A and RAB4A support `small GTPase binding`; rows to LNX1 and USP25 remain bare `protein binding` and are not mechanistically informative enough for GO [PMID:25416956; PMID:25910212; PMID:26496610; PMID:28514442; PMID:33961781; PMID:35271311; PMID:35914814].

## GO-CAM 65692e7e00001822 consistency

- Activity `gomodel:65692e7e00001822/657ba49f00000094` models UniProtKB:P31150/GDI1 as `GO:0005092 GDP-dissociation inhibitor activity`, `part_of GO:0034123 positive regulation of toll-like receptor signaling pathway`, and `occurs_in GO:0005783 endoplasmic reticulum`.
- The molecular function and pathway role are consistent with the GDI1 gene review. The review refines the molecular function to `GO:0005093 Rab GDP-dissociation inhibitor activity`, which is a Rab-specific child of the model's term and is supported by the RAB1A/RAB13 mechanism in PMID:35343654.
- The ER location remains a GO-CAM consistency issue. PMID:35343654 shows GDI1 recruitment to RAB1A and RAB13 but does not localize GDI1 to the ER, and GDI1 is better represented as a cytosolic Rab chaperone that extracts membrane-associated Rabs.
