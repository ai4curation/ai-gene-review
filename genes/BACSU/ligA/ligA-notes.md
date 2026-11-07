# ligA research and annotation review

## 2026-11-06

Identity: O31498, BACSU, B. subtilis strain 168, taxon 224308. Current UniProt response and untouched fetch-gene seed are archived in `.cache/module-audit-logs/chromosomal-replication-20261106/bacillus-baseline.json`. Original 7 annotation payloads and raw files remain unchanged.

LigA is the NAD-dependent DNA ligase of Bacillus subtilis, formerly called YerG. It seals nicks by joining adjacent 3′-hydroxyl and 5′-phosphate termini in duplex DNA, supporting chromosome replication and DNA repair. NAD supplies the adenylate used during ligation. LigA is distinct from the organism’s ATP-dependent DNA ligases.

The genuine default Falcon attempt failed with HTTP403 authentication/access failure; no provider report was authored or substituted. This document and the review are manual research. PAINT lineage check: no IRD or IKR on the resolved lineage. No donor-count argument was used.

PMID20122408 was fetched normally (abstract-only cache); the full author-hosted PDF including supplement was inspected at https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/2010_23702_mc_37_273.pdf . Its Methods explicitly specify native strain168 sequences without appended tags. The reconstitution is a PriA-dependent flapped-minicircle replication-fork assay, not oriC initiation or complete Okazaki-fragment maturation. Source-download checksum and provenance are in the shared audit cache; the publisher PDF is not redistributed in this gene directory.

Current GO was checked directly through QuickGO. GO0003896 is obsolete as equivalent to DNA-directed RNA polymerase activity; primase context therefore belongs with GO0003899 and primer synthesis. GO0003689 describes clamp loading, GO0030337 polymerase processivity. GO1990100/1990156 use E. coli protein names; in Bacillus the helicase is DnaC and the AAA+ loader is DnaI. Bacillus DnaB is an accessory loader. GO7770122 is MCM-specific and is not assigned to bacterial loaders.

## Row decisions

- 0: GO:0003677 (IEA, GO_REF:0000002): ACCEPT. LigA is the NAD-dependent DNA ligase of Bacillus subtilis, formerly called YerG. It seals nicks by joining adjacent 3′-hydroxyl and 5′-phosphate termini in duplex DNA, supporting chromosome replication and DNA repair. NAD supplies the adenylate used during ligation. LigA is distinct from the organism’s ATP-dependent DNA ligases. This assignment refers to this protein’s molecular action, with biochemical or curated family evidence as cited.
- 1: GO:0003911 (IBA, GO_REF:0000033): ACCEPT. LigA is the NAD-dependent DNA ligase of Bacillus subtilis, formerly called YerG. It seals nicks by joining adjacent 3′-hydroxyl and 5′-phosphate termini in duplex DNA, supporting chromosome replication and DNA repair. NAD supplies the adenylate used during ligation. LigA is distinct from the organism’s ATP-dependent DNA ligases. This assignment refers to this protein’s molecular action, with biochemical or curated family evidence as cited.
- 2: GO:0003911 (IEA, GO_REF:0000120): ACCEPT. LigA is the NAD-dependent DNA ligase of Bacillus subtilis, formerly called YerG. It seals nicks by joining adjacent 3′-hydroxyl and 5′-phosphate termini in duplex DNA, supporting chromosome replication and DNA repair. NAD supplies the adenylate used during ligation. LigA is distinct from the organism’s ATP-dependent DNA ligases. This assignment refers to this protein’s molecular action, with biochemical or curated family evidence as cited.
- 3: GO:0005829 (IBA, GO_REF:0000033): ACCEPT. This location is consistent with the protein’s chromosome-associated work. The soluble NAD-dependent ligase acts on intracellular DNA; cytosolic localization is accepted as an ancestral inference rather than a direct imaging result.
- 4: GO:0006259 (IEA, GO_REF:0000104): MODIFY. Replace the broad metabolic-process term with both specific processes already present. LigA itself catalyzes strand joining; its participation is not inferred only from essentiality.
- 5: GO:0006260 (IEA, GO_REF:0000002): ACCEPT. LigA is the NAD-dependent DNA ligase of Bacillus subtilis, formerly called YerG. It seals nicks by joining adjacent 3′-hydroxyl and 5′-phosphate termini in duplex DNA, supporting chromosome replication and DNA repair. NAD supplies the adenylate used during ligation. LigA is distinct from the organism’s ATP-dependent DNA ligases. Purified-component experiments or direct DNA engagement establish a molecular role; process participation is not inferred solely from essentiality. The specific division of labor is retained in the core function.
- 6: GO:0006281 (IEA, GO_REF:0000002): ACCEPT. SsbA provides the ssDNA-bound platform and stimulates processing partners; LigA seals DNA nicks. These are biochemical contributions rather than merely consequences of a knockout.

## Evidence boundaries

- [PMID:11095673] The NAD-dependent ligase encoded by yerG is an essential gene of Bacillus subtilis. Cached abstract was consulted; detailed assays not visible there are not used to contradict experimental annotations.

Identity limit: ligA is not one of the13 purified components in PMID20122408; no direct assay of this gene is attributed to that reconstitution. Its own cited literature and curated sequence-family evidence ground the review.
