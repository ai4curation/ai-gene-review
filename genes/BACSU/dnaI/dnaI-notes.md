# dnaI research and annotation review

## 2026-11-06

Identity: P06567, BACSU, B. subtilis strain 168, taxon 224308. Current UniProt response and untouched fetch-gene seed are archived in `.cache/module-audit-logs/chromosomal-replication-20261106/bacillus-baseline.json`. Original 8 annotation payloads and raw files remain unchanged.

DnaI is the AAA+ helicase-loading protein of Bacillus subtilis. Its N-terminal zinc-binding region interacts with the replicative helicase DnaC, while its C-terminal region binds nucleotide and contains a regulated DNA-binding site. DnaI supports helicase assembly on DNA, assisted by DnaB in the native loading pathway. It is distinct from the DnaA origin-recognition initiator.

The genuine default Falcon attempt failed with HTTP403 authentication/access failure; no provider report was authored or substituted. This document and the review are manual research. PAINT lineage check: no IRD or IKR on the resolved lineage. No donor-count argument was used.

PMID20122408 was fetched normally (abstract-only cache); the full author-hosted PDF including supplement was inspected at https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/2010_23702_mc_37_273.pdf . Its Methods explicitly specify native strain168 sequences without appended tags. The reconstitution is a PriA-dependent flapped-minicircle replication-fork assay, not oriC initiation or complete Okazaki-fragment maturation. Source-download checksum and provenance are in the shared audit cache; the publisher PDF is not redistributed in this gene directory.

Current GO was checked directly through QuickGO. GO0003896 is obsolete as equivalent to DNA-directed RNA polymerase activity; primase context therefore belongs with GO0003899 and primer synthesis. GO0003689 describes clamp loading, GO0030337 polymerase processivity. GO1990100/1990156 use E. coli protein names; in Bacillus the helicase is DnaC and the AAA+ loader is DnaI. Bacillus DnaB is an accessory loader. GO7770122 is MCM-specific and is not assigned to bacterial loaders.

## Row decisions

- 0: GO:0003688 (IBA, GO_REF:0000033): UNDECIDED. The frozen PTHR30050 tree places both DnaA SF2 and DnaI SF8 below PTN001574578. Direct DnaI data show helicase binding and a regulated DNA-binding site, whereas DnaA recognizes oriC sequences. Recruitment to oriC does not itself prove direct origin binding, but the absence of a specificity assay is not evidence of loss. Retain this ancestral assignment as unresolved.
- 1: GO:0005515 (IPI, PMID:16796675): UNDECIDED. The cached abstract emphasizes cell-division or cell-wall proteins and does not resolve the DnaC–DnaI interaction experiment. This is not evidence of mis-attribution. Full-text or supplementary interaction data are needed; neither a false-interaction claim nor a new specific function is inferred.
- 2: GO:0005515 (IPI, PMID:19192185): UNDECIDED. The cached abstract emphasizes cell-division or cell-wall proteins and does not resolve the DnaC–DnaI interaction experiment. This is not evidence of mis-attribution. Full-text or supplementary interaction data are needed; neither a false-interaction claim nor a new specific function is inferred.
- 3: GO:0005515 (IPI, PMID:21630458): REMOVE. The cited interaction evidence can be biologically valid, but bare protein binding is removed under the repository policy. The interaction is retained in the biological account and does not establish an additional catalytic activity.
- 4: GO:0005737 (EXP, PMID:10844689): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Target-specific immunofluorescence detects DnaI foci within the cytoplasm near nucleoid edges.
- 5: GO:0005737 (IEA, GO_REF:0000044): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Target-specific immunofluorescence detects DnaI foci within the cytoplasm near nucleoid edges.
- 6: GO:0006270 (IBA, GO_REF:0000033): ACCEPT. DnaI is the AAA+ helicase-loading protein of Bacillus subtilis. Its N-terminal zinc-binding region interacts with the replicative helicase DnaC, while its C-terminal region binds nucleotide and contains a regulated DNA-binding site. DnaI supports helicase assembly on DNA, assisted by DnaB in the native loading pathway. It is distinct from the DnaA origin-recognition initiator. Purified-component experiments or direct DNA engagement establish a molecular role; process participation is not inferred solely from essentiality. The specific division of labor is retained in the core function.
- 7: GO:0016887 (EXP, PMID:17003052): ACCEPT. The target-specific study detects weak intrinsic DnaI ATPase activity and stronger ssDNA-responsive activity of the isolated C-terminal domain. Earlier failure to detect turnover under other conditions does not negate the positive assay; activity is not assumed to be strongly DNA-stimulated in the intact protein.

## Evidence boundaries

- [PMID:10844689] Subcellular localization of Dna-initiation proteins of Bacillus subtilis: evidence that chromosome replication begins at either edge of the nucleoids. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.
- [PMID:16796675] A new FtsZ-interacting protein, YlmF, complements the activity of FtsA during progression of cell division in Bacillus subtilis. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.
- [PMID:17003052] Helicase binding to DnaI exposes a cryptic DNA-binding site during helicase loading in Bacillus subtilis. Target DnaI ATPase and regulated DNA-binding domains are described in the cached abstract. The study uses a heterologous helicase complex; its sufficiency statement does not remove the native Bacillus DnaB requirement established in other loading contexts.
- [PMID:19192185] Regulation of cell wall morphogenesis in Bacillus subtilis by recruitment of PBP1 to the MreB helix. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.
- [PMID:21630458] An expanded protein-protein interaction network in Bacillus subtilis reveals a group of hubs: Exploration by an integrative approach. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.
- [PMID:12718886] A two-protein strategy for the functional loading of a cellular replicative DNA helicase. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.
- [PMID:19968790] Ordered association of helicase loader proteins with the Bacillus subtilis origin of replication in vivo. Full cached text was consulted for the relevant target-specific claims.

## Ontology-gap placement follow-up

Moved the ontology-only helicase-loading term question from knowledge_gaps to suggested_questions. The supported DnaI ATPase/loading and DnaD/DnaB DNA-binding contributions are unchanged. MCM2–7-specific loader terminology remains inappropriate. Biological mechanism uncertainties and existing evidence boundaries are preserved.


## PR #6117 round-1 follow-up (2026-11-06)

- Apply REMOVE consistently to bare GO:0005515 rows without denying interactions or claiming citation misattribution.

All historical annotation payloads, inherited NEW proposals, and frozen raw/provider files are preserved. Source confidence distinguishes direct target assays from comparative Pseudomonas evidence. No publication cache was refreshed.
