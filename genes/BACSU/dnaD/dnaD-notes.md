# dnaD research and annotation review

## 2026-11-06

Identity: P39787, BACSU, B. subtilis strain 168, taxon 224308. Current UniProt response and untouched fetch-gene seed are archived in `.cache/module-audit-logs/chromosomal-replication-20261106/bacillus-baseline.json`. Original 2 annotation payloads and raw files remain unchanged.

DnaD is a DNA-binding and DNA-remodeling protein that helps assemble the Bacillus subtilis replication-initiation machinery. It recognizes a single-stranded DnaD recognition element at oriC and links DnaA-dependent origin assembly to DnaB and subsequent DnaI-mediated loading of DnaC helicase. DnaD also participates in replication restart and can form DNA-remodeling scaffolds without nicking DNA.

The genuine default Falcon attempt failed with HTTP403 authentication/access failure; no provider report was authored or substituted. This document and the review are manual research. PAINT lineage check: no IRD or IKR on the resolved lineage. No donor-count argument was used.

PMID20122408 was fetched normally (abstract-only cache); the full author-hosted PDF including supplement was inspected at https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/2010_23702_mc_37_273.pdf . Its Methods explicitly specify native strain168 sequences without appended tags. The reconstitution is a PriA-dependent flapped-minicircle replication-fork assay, not oriC initiation or complete Okazaki-fragment maturation. Source-download checksum and provenance are in the shared audit cache; the publisher PDF is not redistributed in this gene directory.

Current GO was checked directly through QuickGO. GO0003896 is obsolete as equivalent to DNA-directed RNA polymerase activity; primase context therefore belongs with GO0003899 and primer synthesis. GO0003689 describes clamp loading, GO0030337 polymerase processivity. GO1990100/1990156 use E. coli protein names; in Bacillus the helicase is DnaC and the AAA+ loader is DnaI. Bacillus DnaB is an accessory loader. GO7770122 is MCM-specific and is not assigned to bacterial loaders.

## Row decisions

- 0: GO:0005737 (EXP, PMID:15186423): ACCEPT. This location is consistent with the protein’s chromosome-associated work. DnaD is predominantly cytoplasmic. Membrane recruitment observed with the dnaB S371P mutant is a distinct experimental condition and is not added as a wild-type location.
- 1: GO:0005737 (IEA, GO_REF:0000044): ACCEPT. This location is consistent with the protein’s chromosome-associated work. DnaD is predominantly cytoplasmic. Membrane recruitment observed with the dnaB S371P mutant is a distinct experimental condition and is not added as a wild-type location.
- 2: GO:0003688 (IDA, PMID:37093985): NEW. The protein itself binds the DNA substrate and organizes initiation machinery. This is direct molecular participation, not a process assertion based only on essentiality. The original seed lacks this claim.
- 3: GO:0006270 (IC, PMID:37093985): NEW. The protein itself binds the DNA substrate and organizes initiation machinery. This is direct molecular participation, not a process assertion based only on essentiality. The original seed lacks this claim.

## Evidence boundaries

- [PMID:15186423] Control of DNA replication initiation by recruitment of an essential initiation protein to the membrane of Bacillus subtilis. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.
- [PMID:37093985] The DNA replication initiation protein DnaD recognises a specific strand of the Bacillus subtilis chromosome origin. Direct DnaD ssDNA/DRE binding and origin-initiation mechanism. Purification Methods specify genomic templates from B. subtilis 168CA and removable His14-SUMO constructs; this is a 168-derived background, not an unqualified assay of every Bacillus strain.

## Ontology-gap placement follow-up

Moved the ontology-only helicase-loading term question from knowledge_gaps to suggested_questions. The supported DnaI ATPase/loading and DnaD/DnaB DNA-binding contributions are unchanged. MCM2–7-specific loader terminology remains inappropriate. Biological mechanism uncertainties and existing evidence boundaries are preserved.
