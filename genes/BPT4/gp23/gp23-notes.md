# Curation Notes: Bacteriophage T4 gene gp23 (23; UniProt P04535)

## Identity and Nomenclature
- **Gene symbol**: `gp23` (standard T4 gene name: `23`)
- **Protein**: Major capsid protein gp23 (521 aa precursor, ~56 kDa; proteolytically processed to mature gp23*, residues 66-521, 456 aa, ~48.7 kDa)
- **UniProt**: `P04535` (`CAPSD_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Major structural subunit of the T4 prolate icosahedral capsid**:
   - Mature gp23* forms the hexagonal surface lattice of the T4 head, assembling into 155 hexameric capsomers (930 copies per virion) in a prolate icosahedral shell characterized by `Tend = 13 laevo` at the icosahedral end caps and `Tmid = 20` in the elongated cylindrical midsection (~1200 Å long by ~860 Å wide) (Fokine et al. 2004, PubMed 15181154; Chen et al. 2017, PubMed 28893988). The 11 non-portal fivefold vertices are occupied by pentamers of the homologous vertex protein gp24*, while the 12th vertex is occupied by the gp20 portal dodecamer.
   - Structurally, gp23* adopts the canonical HK97-like fold (P-domain, A-domain, and N-arm) augmented by a characteristic 66-residue insertion domain (I-domain, residues 201-266) connected by long linkers (topologically equivalent to the HK97 E-loop) that form noncovalent intra- and inter-capsomer contacts stabilizing the shell without covalent isopeptide crosslinking (Chen et al. 2017, PubMed 28893988).
2. **Chaperone-assisted folding and proteolytic capsid maturation**:
   - Nascent gp23 (521 aa) requires the *E. coli* GroEL chaperonin paired specifically with the phage-encoded co-chaperonin gp31 (which replaces host GroES to create a larger folding chamber) to fold into assembly-competent monomers and prevent aggregation (Bakkes et al. 2005).
   - Full-length gp23 copolymerizes around the gp22-containing scaffolding core (initiated at the membrane-bound gp20 portal) to form the unexpanded prohead.
   - The T4 prohead protease gp21 then cleaves the N-terminal 65-residue delta-peptide from gp23 (between Glu65 and Ala66) to yield mature gp23* (Hosoda & Cone 1970, PubMed 4920094; Isobe et al. 1976, PubMed 775029). Subsequent DNA packaging triggers dramatic conformational expansion of the gp23* lattice (increasing capsid volume by ~50%), exposing external binding sites for the decoration proteins Soc (clamping adjacent gp23* hexamers) and Hoc (binding at the center of each gp23* hexamer).
   - Point mutations in gp23 (such as `pt21-34`, `A275T`, or `G292S`) alter inter-capsomer angles and produce isometric (`T=13`), giant ("monster"), or petite heads (Parker et al. 1984, PubMed 6389886; Doermann et al. 1973, PubMed 4584811; Chen et al. 2017, PubMed 28893988).

## Review of Existing GOA Annotations
- `GO:0039621` (`T=13 icosahedral viral capsid`, IEA `GO_REF:0000043`): **ACCEPT**. Wild-type T4 capsids have `Tend = 13 laevo` icosahedral end caps (and `T=13` isometric capsids in point mutants), and `GO:0039621` is the most specific capsid structural term available in GO.
- `GO:0019028` (`viral capsid`, IEA `GO_REF:0000120` and IDA `PMID:4920094`): **MODIFY** -> `GO:0039621` (`T=13 icosahedral viral capsid`) on both rows. `GO:0019028` is correct but less specific than `GO:0039621`, which is already present on the record.
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): gp23* is the major structural protein of the T4 virion capsid (930 copies per capsid).
  - `GO:0019069` (`viral capsid assembly`): gp23 polymerization around the scaffolding core and subsequent proteolytic maturation/expansion drive viral capsid morphogenesis.
