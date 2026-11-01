# Curation Notes: Pseudomonas phage phiKZ `CAPSD` (`gp120`, UniProt `Q8SD42`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `CAPSD` (`gp120`, `PHIKZ120`)
- **Organism**: *Pseudomonas phage phiKZ* (`NCBITaxon:2905945`), the archetype giant myovirus infecting *Pseudomonas aeruginosa*.
- **UniProt Accession**: `Q8SD42` (747 AA precursor, ~82.7 kDa; cleaved at `Glu163-Ala164` to a 584 AA, ~65 kDa mature major capsid protein).
- **Structural Data**: Cryo-EM reconstruction of the mature phiKZ icosahedral head (`PMID:16081102`; atomic-resolution cryo-EM structure `PDB:8Y6V`).

## Molecular Function & Prohead Maturation
- **T=27 Icosahedral Capsid Lattice**: Mature `gp120` (`CAPSD`) self-assembles into homohexameric capsomers (`~140 A` across) that form a giant `T=27` icosahedral capsid shell (`1455 A` / `145.5 nm` diameter along 5-fold axes, `1240 A` along 2-fold axes, ~45 A average wall thickness) comprising 1,560 `gp120` subunits (`260 hexamers`) and 11 pentameric vertices (with the 12th occupied by the portal vertex attached to the 180 nm contractile tail) [PMID:16081102, file:BPDPK/CAPSD/CAPSD-uniprot.txt]. The capsid encapsulates the ~280-kb circularly permuted, terminally redundant linear dsDNA genome together with a distinctive cylindrical proteinaceous "inner body" (IB) running between opposite 5-fold vertices [PMID:16081102, PMID:22429790].
- **Morphogenetic Proteolytic Processing by `gp175` (`PRO`)**: Synthesized as a 747-residue precursor (`82.7 kDa`), `gp120` undergoes sequential proteolytic maturation by the phage-encoded serine prohead protease `gp175` (`PRO`, `Q8SCY7`) at up to 7 `[S/A/G]-X-E` cleavage motifs within its 163-residue N-terminal propeptide (`residues 24/25, 54/55, 84/85, 97/98, 118/119, 136/137`, and the final maturation site `Glu163-Ala164`), yielding the mature `65 kDa` (`residues 164–747`) capsid subunit during prohead expansion and maturation [PMID:22429790, file:BPDPK/CAPSD/CAPSD-uniprot.txt].

## Curation Decisions
- **ACCEPT**: `GO:0019028` (`viral capsid`, IEA from `GO_REF:0000043`).
- **Core Function**: Annotate `GO:0039660` (`structural constituent of virion capsid`) in `GO:0019028` (`viral capsid`) and `GO:0019069` (`viral capsid assembly`).
