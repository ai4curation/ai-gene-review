# dnaB research and annotation review

## 2026-11-06

Identity: P07908, BACSU, B. subtilis strain 168, taxon 224308. Current UniProt response and untouched fetch-gene seed are archived in `.cache/module-audit-logs/chromosomal-replication-20261106/bacillus-baseline.json`. Original 8 annotation payloads and raw files remain unchanged.

DnaB is a DNA-binding, DNA-remodeling helicase-loading accessory protein in Bacillus subtilis. It cooperates with DnaD and DnaI to place the DnaC replicative helicase on DNA during chromosome initiation and replication restart. DnaB binds single- and double-stranded DNA, oligomerizes and occurs in cytosolic and membrane-associated pools. It is distinct from the unrelated helicase named DnaB in Escherichia coli.

The genuine default Falcon attempt failed with HTTP403 authentication/access failure; no provider report was authored or substituted. This document and the review are manual research. PAINT lineage check: no PANTHER family in the record, so no lineage-loss check was possible. No donor-count argument was used.

PMID20122408 was fetched normally (abstract-only cache); the full author-hosted PDF including supplement was inspected at https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/2010_23702_mc_37_273.pdf . Its Methods explicitly specify native strain168 sequences without appended tags. The reconstitution is a PriA-dependent flapped-minicircle replication-fork assay, not oriC initiation or complete Okazaki-fragment maturation. Source-download checksum and provenance are in the shared audit cache; the publisher PDF is not redistributed in this gene directory.

Current GO was checked directly through QuickGO. GO0003896 is obsolete as equivalent to DNA-directed RNA polymerase activity; primase context therefore belongs with GO0003899 and primer synthesis. GO0003689 describes clamp loading, GO0030337 polymerase processivity. GO1990100/1990156 use E. coli protein names; in Bacillus the helicase is DnaC and the AAA+ loader is DnaI. Bacillus DnaB is an accessory loader. GO7770122 is MCM-specific and is not assigned to bacterial loaders.

## Row decisions

- 0: GO:0005515 (IPI, PMID:35576203): REMOVE. The cited interaction evidence can be biologically valid, but bare protein binding is removed under the repository policy. The interaction is retained in the biological account and does not establish an additional catalytic activity.
- 1: GO:0005737 (EXP, PMID:10844689): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Cytosolic and membrane-associated DnaB pools are experimentally distinguished; cytosolic proteolysis and origin association vary with growth phase.
- 2: GO:0005737 (EXP, PMID:20071750): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Cytosolic and membrane-associated DnaB pools are experimentally distinguished; cytosolic proteolysis and origin association vary with growth phase.
- 3: GO:0005737 (IEA, GO_REF:0000044): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Cytosolic and membrane-associated DnaB pools are experimentally distinguished; cytosolic proteolysis and origin association vary with growth phase.
- 4: GO:0005886 (EXP, PMID:15186423): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Cytosolic and membrane-associated DnaB pools are experimentally distinguished; cytosolic proteolysis and origin association vary with growth phase.
- 5: GO:0005886 (EXP, PMID:20071750): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Cytosolic and membrane-associated DnaB pools are experimentally distinguished; cytosolic proteolysis and origin association vary with growth phase.
- 6: GO:0005886 (IEA, GO_REF:0000044): ACCEPT. This location is consistent with the protein’s chromosome-associated work. Cytosolic and membrane-associated DnaB pools are experimentally distinguished; cytosolic proteolysis and origin association vary with growth phase.
- 7: GO:0006260 (IMP, PMID:3027697): ACCEPT. DnaB is a DNA-binding, DNA-remodeling helicase-loading accessory protein in Bacillus subtilis. It cooperates with DnaD and DnaI to place the DnaC replicative helicase on DNA during chromosome initiation and replication restart. DnaB binds single- and double-stranded DNA, oligomerizes and occurs in cytosolic and membrane-associated pools. It is distinct from the unrelated helicase named DnaB in Escherichia coli. Purified-component experiments or direct DNA engagement establish a molecular role; process participation is not inferred solely from essentiality. The specific division of labor is retained in the core function.
- 8: GO:0003677 (IDA, PMID:20071750): NEW. The protein itself binds the DNA substrate and organizes initiation machinery. This is direct molecular participation, not a process assertion based only on essentiality. The original seed lacks this claim.

## Evidence boundaries

- [PMID:20071750] DnaB proteolysis in vivo regulates oligomerization and its localization at oriC in Bacillus subtilis. Full cached text was consulted for the relevant target-specific claims.
- [PMID:35576203] Structure and kinase activity of bacterial cell cycle regulator CcrZ. Supports CcrZ interactions with B. subtilis DnaA/DnaB and replication control. It is not relied upon as the sole direct source for a DnaA–oriC complex; the origin complex is independently supported by DnaA-trio studies.
- [PMID:12718886] A two-protein strategy for the functional loading of a cellular replicative DNA helicase. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.

PMID20071750 full Methods explicitly uses B. subtilis strain168 for growth-phase protein studies and ChIP, supporting the target identity without strain transfer.

## Ontology-gap placement follow-up

Moved the ontology-only helicase-loading term question from knowledge_gaps to suggested_questions. The supported DnaI ATPase/loading and DnaD/DnaB DNA-binding contributions are unchanged. MCM2–7-specific loader terminology remains inappropriate. Biological mechanism uncertainties and existing evidence boundaries are preserved.


## PR #6117 round-1 follow-up (2026-11-06)

- Refine remaining broad machine replication row consistently to the supported process, preserving original payload.
- Retain inherited NEW GO:0003677; specify both ssDNA and dsDNA binding in core activities from direct domain/gel-shift evidence.
- Replace generic location rationales with fractionation evidence distinguishing cytoplasmic and membrane-associated pools.

All historical annotation payloads, inherited NEW proposals, and frozen raw/provider files are preserved. Source confidence distinguishes direct target assays from comparative Pseudomonas evidence. No publication cache was refreshed.
