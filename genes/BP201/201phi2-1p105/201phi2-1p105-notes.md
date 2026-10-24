# Curation Notes: Pseudomonas phage 201phi2-1 `201phi2-1p105` (`ChmA` / `PhuN`, UniProt `B3FIW8`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `201phi2-1p105` (`ChmA`, `PhuN`, `gp105`)
- **Organism**: *Pseudomonas phage 201phi2-1* (`NCBITaxon:198110`), a jumbo myovirus infecting *Pseudomonas chlororaphis*.
- **UniProt Accession**: `B3FIW8` (631 AA, ~68.6 kDa).
- **Structural Data**: Subtomogram averaging of native phage nuclear shells in situ and high-resolution cryo-EM of recombinant cubic (`O` symmetry, 24-mer, `PDB:7SQQ`) and flat-sheet (`C4` homotetramer, `PDB:7SQR`, `PDB:7SQS`, `PDB:8IGG`) assemblies.

## Molecular Function & Self-Assembly Architecture
- **Chimallin (`ChmA`) Phage Nuclear Shell Protein**: `gp105` (`201phi2-1p105`) is the earliest and most abundantly expressed phage protein upon infection [PMID:28082593]. Monomers adopt a four-domain fold (N-terminal extension, core domain, C-terminal domain, and flexible C-terminal tail `residues 580–631`) and self-assemble into four-fold symmetric (`C4`) homotetramers measuring `~11.5 x 11.5 nm` with a central ~2 nm pore [PMID:35922510].
- **Higher-Order Square Lattice Polymerization**: `ChmA` protomers interlock within the tetramer via their N-terminal extensions, while flexible C-terminal tail segments (`ChmA_C1`, `residues 590–611`, and `ChmA_C2`, `residues 622–631`) reach across to adjacent tetramers to assemble a flexible single-layered square-lattice sheet (~6 nm thick) that closes into a micrometer-scale spherical compartment in the host cell cytoplasm [PMID:35922510].

## Biological Role in Viral Replication Compartmentalization
- **Selective Subcellular Compartmentalization ("Phage Nucleus")**: The `ChmA` shell encloses replicating phage 201phi2-1 genomic DNA at midcell (positioned by the bipolar `PhuZ` / `gp59` spindle) and segregates proteins by function: phage DNA replication and transcription proteins (e.g., thymidylate kinase `gp224`, DNA ligase `gp242`, RNA polymerase subunit `gp273/274`, `gp197`, topoisomerase `gp355`, RecA-like `gp237`) localize inside the phage nucleus, whereas ribosomes (`L28`, `S17`), translation elongation factors (`EF-Tu`), metabolic enzymes (thymidylate synthase `gp245`), and the `PhuZ` cytoskeleton remain strictly in the surrounding host cytoplasm [PMID:28082593, PMID:28813669, PMID:35922510].
- **Capsid Docking and DNA Packaging**: Late in infection, membrane-assembled procapsids (`gp200`) traffic along `PhuZ` filaments and dock directly onto the exterior of the `ChmA` shell to package replicated viral DNA before detaching and assembling with tails in the cytoplasm [PMID:28082593, PMID:31199917].

## Curation Decisions
- **ACCEPT**: All four existing annotations to `GO:0030430` (`host cell cytoplasm`, EXP from `PMID:28082593`, `PMID:28813669`, `PMID:35922510`, and IEA from `GO_REF:0000044`).
- **Core Function**: Capture its structural self-assembly (`GO:0005198` `structural molecule activity` / `GO:0042802` `identical protein binding`) and localization in `GO:0030430` (`host cell cytoplasm`) during `GO:0019058` (`viral life cycle`).
