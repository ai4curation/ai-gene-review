# Curation Notes: Pseudomonas phage phiKZ `PHIKZ039` (`PhuZ` / `TubZ`, UniProt `Q8SDC3`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `PHIKZ039` (`PhuZ`, `TubZ`, `gp39`)
- **Organism**: *Pseudomonas phage phiKZ* (`NCBITaxon:2905945`), giant myovirus infecting *Pseudomonas aeruginosa*.
- **UniProt Accession**: `Q8SDC3` (327 AA, ~36.8 kDa, EC `3.6.5.-`).
- **Structural Data**: Crystal structures in monomeric (`PDB:3ZBP`, 1.73 A) and protofilament (`PDB:3ZBQ`, 3.10 A) states [PMID:23528827].

## Molecular Function & Spindle Assembly
- **Tubulin/FtsZ-Like Cytoskeletal GTPase**: `PHIKZ039` (`PhuZ` / `TubZ`) is the phiKZ ortholog of phage 201phi2-1 `PhuZ` (`B3FK34`) [PMID:23528827, PMID:28813669]. Crystal structures in monomeric (`PDB:3ZBP`) and protofilament (`PDB:3ZBQ`) conformations show a two-domain tubulin/FtsZ fold lacking helix H6, where polymerization induces an ~11-degree rotation between the N-terminal nucleotide-binding domain and C-terminal activation domain that inserts the catalytic T7 loop (`Asp201`, `Asp204`) of one subunit into the nucleotide-binding pocket of the adjacent subunit [PMID:23528827].
- **Dynamic Instability & Phage Nucleus Centering**: Above a threshold concentration, `PHIKZ039` polymerizes in a GTP-dependent manner into twisted, three-stranded filament bundles in the *Pseudomonas aeruginosa* cytoplasm [PMID:23528827, PMID:28813669]. During infection, `PHIKZ039` assembles a bipolar spindle with dynamically unstable filaments extending from the cell poles to position the `ChmA` (`PHIKZ054` / `gp54`)-bounded phage nucleus at midcell [PMID:28813669]. Mutation of the catalytic T7-loop aspartate (`D204A`) abolishes filament length fluctuations (dynamic instability) and blocks midcell centering of the phiKZ phage nucleus [PMID:28813669].

## Curation Decisions
- **ACCEPT**: `GO:0003924` (`GTPase activity`, IEA and ISS), `GO:0005525` (`GTP binding`, IEA), and `GO:0030430` (`host cell cytoplasm`, IEA and ISS), all directly supported by experimental characterization in `PMID:23528827` and `PMID:28813669`.
- **TOO_GENERAL**: `GO:0000166` (`nucleotide binding`, entailed by `GO:0005525`) and `GO:0016787` (`hydrolase activity`, entailed by `GO:0003924`).
