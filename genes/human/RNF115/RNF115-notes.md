# RNF115 notes

## Deep research

- `just deep-research human RNF115 --provider falcon --fallback perplexity-lite --timeout 900` was attempted on 2026-11-24 with the shared retained runtime at `/srv/home/cmungall/orca/workspaces/ai-gene-review/aigr-ros/.venv`.
- The Falcon and Perplexity providers were unavailable in that environment, so this review uses a manual synthesis from the cached UniProt record and primary literature instead of a generated `RNF115-deep-research-*.md` provider file.

## Functional synthesis

RNF115/BCA2/Rabring7 is an intracellular RING E3 ligase. Early work showed intrinsic RING-dependent E3/autoubiquitination activity and an N-terminal BZF domain that binds ubiquitin and contributes autoubiquitination sites [PMID:18819927]. Later work expanded the substrate range:

- RNF115 promotes post-ER restraint of Toll-like receptor delivery by catalyzing K11-linked ubiquitination of RAB1A on Lys49/Lys61 and RAB13 on Lys46/Lys58, reducing GDI1 recruitment and RAB recycling [PMID:35343654].
- RNF115 has antiviral roles through K48-linked MAVS degradation in the resting state and K63-linked STING/MITA ubiquitination after HSV-1 infection [PMID:33139700].
- RNF115 contributes to ubiquitin-dependent sorting of EGFR, MET, and CXCR4 from the early endocytic compartment [PMID:23418353].
- RNF115 promotes autophagosome maturation by stabilizing the autophagosomal SNARE STX17, though that STX17 effect was reported not to be a direct K48/K63-ubiquitination effect [PMID:32980859].
- Multiple large binary interactome papers report RNF115 interactions, including with UBE2D/UBE2E family E2 enzymes. Those E2 rows support `ubiquitin conjugating enzyme binding`, while the rows to DAZAP2, MDM4, VCP, and MDM2 remain bare `protein binding` and are not mechanistically informative enough for GO [PMID:25416956; PMID:31515488; PMID:32296183; PMID:32814053; PMID:35044719].

## GO-CAM 65692e7e00001822 consistency

- Activity `gomodel:65692e7e00001822/657ba49f00000074` models UniProtKB:Q9Y4L5/RNF115 as `GO:0061630 ubiquitin protein ligase activity`, `part_of GO:0070979 protein K11-linked ubiquitination`, and `occurs_in GO:0005783 endoplasmic reticulum`. This is consistent with PMID:35343654 and with the gene review: RNF115 is recruited to the ER/Golgi by AKT1/14-3-3 signaling and directly catalyzes K11-linked ubiquitination of RAB1A and RAB13.
- No RNF115-specific GO-CAM discrepancy was found. The GO-CAM review can be updated after this gene PR merges to change RNF115 consistency from `NO_GENE_REVIEW` to `CONSISTENT`.
