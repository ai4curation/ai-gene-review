# Gene P57019 (Y55K_BPP22 / ORF485 / GtrC) Research Notes

## Overview
- **Gene symbol**: `P57019` (`ORF485`, `gtrC` / `conC`)
- **UniProt ID**: `P57019` (`Y55K_BPP22`)
- **Protein**: Uncharacterized 55.3 kDa membrane protein in gtrB 5' region (O-antigen conversion glucosyltransferase GtrC; 485 AA, 55.3 kDa)
- **Organism**: *Salmonella* phage P22 (`NCBITaxon:10754`)
- **Genomic context**: Located immediately downstream of `gtrB` (`bgt`) in the three-gene serotype-converting `gtrABC` operon (`gtrA`–`gtrB`–`gtrC`, transcribed from *P*gtr between `int` and `attP`) [PMID:11053393].

## Function & Architecture
- **Serotype-specific O-antigen α-1,6-glucosyltransferase (GtrC)**: Although the UniProt header retains the legacy label `"Uncharacterized 55.3 kDa membrane protein in gtrB 5' region"`, Vander Byl & Kropinski (2000) cloned the P22 `gtrABC` (`conABC`) cassette and demonstrated experimentally that it converts *Salmonella enterica* serovar Typhimurium LT2 from serotype O:4,[5],12 to O:1,4,[5],12 by adding α1→6 glucosyl residues onto the galactose moiety of the O-antigen repeat unit [PMID:11053393]. Within the three-gene cassette (`gtrA` encoding the 120-AA flippase, `gtrB` encoding the 310-AA undecaprenyl-phosphate glucosyltransferase), `ORF485` (`gtrC`, encoding a 485-AA integral membrane protein with 10 transmembrane helices) encodes the serotype-specific glucosyltransferase that transfers glucose from undecaprenyl-phosphate-β-D-glucose onto the O-antigen polysaccharide repeat in the periplasm [PMID:11053393].
- **Domain and topology**: Contains 10 transmembrane helices (`TRANSMEM 9..29`, `66..86`, `98..118`, `131..151`, `159..179`, `194..214`, `259..279`, `293..313`, `322..342`, `350..370`) and the conserved `InterPro:IPR025686` / `Pfam:PF14264` (`Glucos_trans_II`, O-antigen polysaccharide glucosyltransferase GtrC-like) domain (`residues 20..459`) [file:BPP22/P57019/P57019-uniprot.txt].

## Existing GO Annotations Review & Proposed Additions
- `GO:0033644` (`host cell membrane`, IEA via `GO_REF:0000044`, `UniProtKB-SubCell:SL-0380`): **ACCEPT**. Accurately captures localization of this 10-TM integral membrane protein in the host bacterial inner membrane.
- `GO:0016757` (`glycosyltransferase activity`, **NEW**): Supported by cloning and functional characterization of the P22 `gtrABC` serotype-converting cassette (`PMID:11053393`) and the `InterPro:IPR025686` / `Pfam:PF14264` (`Glucos_trans_II`) glucosyltransferase domain (`file:BPP22/P57019/P57019-uniprot.txt`), matching the curation of `gtrB` in this repository.
- `GO:0000271` (`polysaccharide biosynthetic process`, **NEW**): Supported by experimental demonstration that the P22 `gtrABC` operon modifies the *Salmonella* lipopolysaccharide O-antigen polysaccharide repeat by α1→6 glucosylation (`PMID:11053393`), matching the curation of `gtrA` and `gtrB` in this repository.
