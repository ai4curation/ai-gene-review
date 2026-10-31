# Curation Notes: Pseudomonas phage 201phi2-1 `201phi2-1p059` (`PhuZ`, UniProt `B3FK34`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `201phi2-1p059` (`PhuZ`, `gp59`)
- **Organism**: *Pseudomonas phage 201phi2-1* (`NCBITaxon:198110`), a jumbo myovirus infecting *Pseudomonas chlororaphis*.
- **UniProt Accession**: `B3FK34` (315 AA, ~34.9 kDa, EC `3.6.5.-`).
- **Structural Data**: Crystal structures of GDP-bound monomer (`PDB:3R4V`, `PDB:3RB8`) and 3.5-A cryo-EM reconstruction of the polymerized three-stranded filament (`PDB:3J5V`).

## Molecular Function & Filament Assembly Mechanism
- **Divergent Tubulin/FtsZ-Family GTPase**: `PhuZ` (`201phi2-1p059`) possesses a canonical two-domain tubulin fold (N-terminal nucleotide-binding domain and C-terminal activation domain bridged by helix H7) but lacks helix H6, creating a cavity occupied by the side chain of `Tyr161` from helix H7 [PMID:22726436]. Its T7 loop contains two conserved catalytic aspartates (`Asp187` and `Asp190`); mutating either (`D187A` or `D190A`) reduces GTP hydrolysis by >95% without preventing GTP binding or static polymerization [PMID:22726436].
- **Extended Acidic C-Terminal Tail**: The C-terminal 21 amino acids (`residues 295–315`) form an extended acidic tail (knuckle + last 13 acidic residues) containing critical residues (`Arg217`, `Asp303`, `Asp305`, `Asp306`, `Asp311`) that reach across to adjacent subunits to simultaneously stabilize longitudinal (`1800 A^2` buried surface area per dimer interface) and lateral contacts across three intertwined protofilaments [PMID:22726436, PMID:24631461].
- **Three-Stranded Filament with Dynamic Instability and Treadmilling**: In the presence of GTP (above a 2.5 uM critical concentration), `PhuZ` polymerizes into a right-handed, three-stranded helical filament (`43.4 A` axial rise, `-113.5 deg` twist) where longitudinal kinetic interfaces stay relaxed prior to hydrolysis and compact upon Pi release, storing elastic energy in the lattice that drives microtubule-like dynamic instability at the plus end and treadmilling [PMID:22726436, PMID:24631461, PMID:25429514].

## Biological Role in Phage Nucleus Positioning and Capsid Trafficking
- **Bipolar Spindle Centering of the Phage Nucleus**: During infection of *P. chlororaphis*, `PhuZ` filaments have their minus ends stably anchored at both cell poles and extend dynamically unstable plus ends toward midcell, pushing the `ChmA` (`201phi2-1p105` / `gp105`)-enclosed phage nucleus to the cell center and maintaining it there via balanced pushing forces [PMID:22726436, PMID:25429514, PMID:28082593]. Catalytic `D190A` mutants form static filaments that misposition the phage nucleus to the cell pole and reduce phage burst size by ~50% [PMID:22726436, PMID:25429514].
- **Capsid Trafficking and Nuclear Rotation**: Empty procapsids assemble on the host plasma membrane, attach to `PhuZ` spindles, and are transported rapidly along treadmilling `PhuZ` filaments to dock onto the surface of the `ChmA` phage nucleus for DNA packaging; transverse pushing forces from the spindle also rotate the phage nucleus at midcell so capsids are distributed evenly across its surface [PMID:31199917].

## Curation Decisions
- **ACCEPT**: `GO:0003924` (`GTPase activity`), `GO:0005525` (`GTP binding`), `GO:0042802` (`identical protein binding`), and `GO:0030430` (`host cell cytoplasm`).
- **KEEP_AS_NON_CORE**: `GO:1903902` (`positive regulation of viral life cycle`, IMP from `PMID:22726436`), as reduced burst size in catalytic `D190A` mutants is a downstream consequence of defective spindle dynamics, nuclear centering, and capsid trafficking.
- **TOO_GENERAL**: `GO:0000166` (`nucleotide binding`, entailed by `GO:0005525`) and `GO:0016787` (`hydrolase activity`, entailed by `GO:0003924`).
