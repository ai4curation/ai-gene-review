# Curatorial Notes for Zebrafish abhd10a (UniProtKB:A0A0R4ILM1)

## Summary of Gene Product & Orthology

- **Protein**: Palmitoyl-protein thioesterase ABHD10, mitochondrial (`UniProtKB:A0A0R4ILM1`, sequence version 1; 284 aa; `ZFIN:ZDB-GENE-060526-144`, `GeneID:568517`, chromosome 5; secondary accession `A0A8M1P930`, PANTHER 19.0 leaf `A0A8M2BCX5` in `PANTHER:PTHR16138:SF7`).
- **Teleost Genome Duplication (TGD) Co-Orthology**:
  - Teleost whole-genome duplication (`PMID:27189481`) produced two retained zebrafish co-orthologs of tetrapod `ABHD10`: `abhd10a` (`A0A0R4ILM1`, Chr 5) and `abhd10b` (`E7F9Y7`, Chr 24, syntenic with `tagln3b`).
  - `abhd10a` contains the full `PF00561` (`Abhydrolase_1`, residues 57-163) and `IPR052382` (`ABHD10_acyl-thioesterase`) architecture and strictly conserves the charge-relay catalytic triad at **Ser131** (within the `GSSMG` nucleophilic elbow), **Asp228**, and **His258**, homologous to human `Q9NUJ1` Ser152-Asp249-His279 (`PMID:22294686`, `PMID:31740833`).
- **Literature Search**:
  - PubMed queries for `"abhd10a"`, `("abhd10" AND ("zebrafish" OR "Danio rerio"))`, `"ZDB-GENE-060526-144"`, and `"A0A0R4ILM1"` returned 0 gene-specific experimental functional studies in *Danio rerio*; `PMID:27189481` (PhyloFish transcriptome database) provides multi-tissue ray-finned fish RNA-seq assemblies.

## Key Curation Decisions

- **`GO:0008474` (`palmitoyl-(protein) hydrolase activity`, `IEA` `GO_REF:0000120` via `ARBA:ARBA00085285` / `EC:3.1.2.22`)**: `ACCEPT` — core conserved family activity supported by `PTHR16138:SF7` orthology and intact Ser131-Asp228-His258 catalytic triad (`PMID:31740833`).
- **`GO:0098734` (`obsolete macromolecule depalmitoylation`, `IEA` `GO_REF:0000108` from `GO:0008474`)**: `MODIFY` -> `GO:0008474` (`palmitoyl-(protein) hydrolase activity`), replacing the obsoleted inter-ontology biological process projection with the active molecular function term already present on `abhd10a`.
- **`GO:0005739` (`mitochondrion`, `IEA` `GO_REF:0000044` `SL-0173`)**: `ACCEPT` per the Root Organelle Policy; we stay at root `GO:0005739` and do not add a `NEW` `GO:0005759` (`mitochondrial matrix`) row because `A0A0R4ILM1` is an unreviewed TrEMBL record lacking an annotated transit-peptide cleavage feature or fish sub-organellar experimental assay.
- **`GO:0102390` (`mycophenolic acid acyl-glucuronide esterase activity`, `IEA` `GO_REF:0000003` via `EC:3.1.1.93`)**: `MARK_AS_OVER_ANNOTATED` — automated `EC:3.1.1.93` propagation transfers a human hepatic drug-metabolite carboxylic-esterase activity (`PMID:22294686`) across 400+ Myr to a teleost paralog without biochemical evidence in fish.
