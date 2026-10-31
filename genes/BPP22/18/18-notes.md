# Gene Review Notes: Salmonella phage P22 `18` (`P03687`, DNA replication protein gp18)

## Overview
- **Gene symbol**: `18`
- **UniProt ID**: `P03687` (`VG18_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 271 amino acids (30.7 kDa)
- **Operon / genomic context**: Encoded in the early right ($P_R$) replication operon immediately upstream of the replicative helicase gene `12` (`c1`-`18`-`12` region), analogous to the $cII$-$O$-$P$ replication region of Escherichia phage lambda ([PMID:6241581](https://pubmed.ncbi.nlm.nih.gov/6241581/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Structural Architecture
- **Origin-binding replication initiator (gp18)**:
  - Bacteriophage P22 gp18 is the phage-encoded replication initiator protein, homologous in its N-terminal domain to the phage lambda replication initiator protein O (`InterPro:IPR006497` / `Pfam:PF04492` `Phage_rep_O` / `NCBIfam:TIGR01610` `phage_O_Nterm`) and containing a winged helix-like DNA-binding domain (`Gene3D:1.10.10.10` / `InterPro:IPR036388` `WH-like_DNA-bd_sf`).
  - As shown by Backhaus & Petri (1984) [PMID:6241581, "A comparison of a 3000-bp sequence of Salmonella phage P22, coding for gene c1 and the replication genes 18 and 12, with the analogous cII-O-P region of coliphage lambda permits the localization of transcriptional signals, an oop RNA species, and the origin of replication (ori) within gene 18."], the P22 replication origin (`ori`) is embedded directly within the coding sequence of gene `18`, and the N-terminal DNA-binding domain of gp18 recognizes and binds the `ori` iteron sequences, with strongest sequence conservation in the `ori`-binding region to lambdoid phage $\phi 82$ [PMID:6241581].
  - Note on terminology in Vander Byl & Kropinski (2000) [PMID:11053393]: the genome paper refers to gp18 in passing as a "primase (gp18)" when contrasting P22 with lambda ("with the exception that P22 contains a primase (gp18) and a helicase (gp12)"), citing Wickner (1984). Biochemical studies by Wickner (1984, J. Biol. Chem. 259:14038-14043) actually showed that gp18 is the origin-binding initiator (lambda O analog) that recruits the phage DnaB-like replicative helicase gp12 to the P22 replication origin in a host DnaK/DnaJ-dependent prepriming reaction, whereas RNA primer synthesis is carried out by host primase (DnaG).

## Review of Existing GO Annotations
- **`GO:0006260` (`DNA replication`, `IEA`, `GO_REF:0000120`)**:
  - **Action**: `MODIFY` -> `GO:0039693` (`viral DNA genome replication`).
  - **Reasoning**: gp18 specifically initiates lytic replication of the bacteriophage P22 dsDNA genome from the internal replication origin (`ori`) located within gene `18` ([PMID:6241581](https://pubmed.ncbi.nlm.nih.gov/6241581/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)). Replacing the broad `GO:0006260` (`DNA replication`) with `GO:0039693` (`viral DNA genome replication`) captures the phage-specific biological process and maintains consistency with the partner replication gene `12` (`P03006`).
- **Proposed `NEW` annotations**:
  - `GO:0003688` (`DNA replication origin binding`, `enables`): Captures the core molecular function of gp18 as the phage O-family origin-binding initiator protein (`InterPro:IPR006497`, `Pfam:PF04492`, [PMID:6241581](https://pubmed.ncbi.nlm.nih.gov/6241581/)).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`): P22 viral DNA replication takes place in the cytoplasm of the infected *Salmonella* host cell ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).
