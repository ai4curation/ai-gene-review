# Curation Notes: Pseudomonas phage phiKZ `PHIKZ054` (`ChmA` / `PhuN`, UniProt `Q8SDA8`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `PHIKZ054` (`ChmA`, `PhuN`, `gp54`)
- **Organism**: *Pseudomonas phage phiKZ* (`NCBITaxon:2905945`), giant myovirus infecting *Pseudomonas aeruginosa*.
- **UniProt Accession**: `Q8SDA8` (626 AA, ~69.3 kDa).
- **Orthology**: PhiKZ ortholog of *Pseudomonas phage 201phi2-1* `gp105` (`201phi2-1p105`, `B3FIW8`) and *Pseudomonas phage phiPA3* `gp53` [PMID:28813669].

## Molecular Function & Role in Viral Replication Compartmentalization
- **Chimallin (`ChmA`) Phage Nuclear Shell Protein**: Upon phiKZ infection of *Pseudomonas aeruginosa*, `gp54` (`PHIKZ054`) self-assembles into a spherical, micrometer-scale proteinaceous shell in the host cytoplasm that encloses replicating phage DNA [PMID:28813669]. When expressed alone in uninfected cells, GFP- or mCherry-tagged `gp54` forms small non-localized foci, whereas phage infection triggers assembly of a closed spherical compartment surrounding the viral nucleoid that is positioned at midcell by the bipolar `PhuZ` (`PHIKZ039` / `gp39`) tubulin spindle [PMID:28813669].
- **Selective Compartmentalization and Capsid Docking**: The `gp54` shell partitions cellular and viral proteins according to function: phage DNA-processing enzymes such as the RecA-like recombinase `gp152` accumulate inside the phage nucleus alongside viral DNA, whereas host ribosomes (`L28`, `S21`), Peptide deformylase, and soluble cytoplasmic GFP are excluded and remain in the cytoplasm [PMID:28813669]. Late in infection (~40–60 min post-infection), newly assembled `gp120` (`CAPSD`) procapsids move from the cell periphery to dock onto the exterior of the `gp54` shell for viral DNA packaging [PMID:28813669].

## Curation Decisions
- **ACCEPT**: Both existing annotations to `GO:0030430` (`host cell cytoplasm`, EXP from `PMID:28813669` and IEA from `GO_REF:0000044`).
- **Core Function**: Capture its structural self-assembly (`GO:0005198` `structural molecule activity`) in `GO:0030430` (`host cell cytoplasm`) during `GO:0019058` (`viral life cycle`).
