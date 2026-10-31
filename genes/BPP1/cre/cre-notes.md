# cre (P06956) — Curation Notes

## Summary
- **Gene symbol**: `cre`
- **UniProtKB**: `P06956` (`CRE_BPP1`, 343 aa, 38.5 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Tyrosine site-specific recombinase Cre ("cyclization of DNA"), prototypical member of the tyrosine recombinase/integrase superfamily. Catalyzes cofactor-independent site-specific recombination between two 34-bp `loxP` sites (comprising two 13-bp inverted repeats flanking an 8-bp asymmetric spacer) as a homotetramer via a covalent 3'-phosphotyrosine (Tyr-324) DNA intermediate and Holliday junction synapse (`PDB:1CRX`, `PDB:2CRX`, `PDB:3CRX`). In the P1 life cycle, Cre cyclizes terminally redundant linear phage DNA following injection into the host and resolves dimeric Prophage plasmids into monomers to ensure faithful plasmid partitioning and maintenance.

## Literature Evidence
- **Sternberg et al. 1986 (`PMID:3486297`)**:
  - Sequenced the P1 `cre` gene (`X03453`), showed that it encodes a 343-aa protein expressed from three upstream promoters, and demonstrated its role in `loxP`-specific recombination.
  - Quote: `"The bacteriophage P1 site-specific recombination system consists of two components, a site, loxP, at which recombination occurs, and a recombinase protein, Cre. In this paper, we present the DNA sequence of the cre structural gene and its upstream regulatory region."`
- **Guo, Gopaul & Van Duyne 1997 (`PMID:9288963`) & Gopaul, Guo & Van Duyne 1998 (`PMID:9670032`)**:
  - Solved the 2.4 Å crystal structure of the tetrameric Cre recombinase covalently bound to a `loxP` suicide DNA substrate via Tyr-324 (`PMID:9288963`, `PDB:1CRX`) and the 2.2 Å crystal structure of the Cre-`loxA` Holliday junction reaction intermediate (`PMID:9670032`, `PDB:2CRX`, `PDB:3CRX`), defining how the N-terminal (`residues 20-129`) and C-terminal (`residues 132-341`) domains clamp around the `loxP` inverted repeats and catalyze strand cleavage, exchange, and religation.
  - Quote (`PMID:9288963`): `"The bacteriophage recombinase Cre catalyses site-specific recombination between two 34-base-pair loxP sites. The crystal structure at 2.4 A resolution of Cre bound to a loxP substrate reveals an intermediate in the recombination reaction, in which a Cre molecule has cleaved the substrate to form a covalent 3'-phosphotyrosine linkage with the DNA."`
  - Quote (`PMID:9670032`): `"We have determined the X-ray crystal structures of two DNA Holliday junctions (HJs) bound by Cre recombinase. ... Cre recombinase is an integrase family member that recombines 34 bp loxP sites in the absence of accessory proteins or auxiliary DNA sequences."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Reviewed the biological roles of Cre in the P1 life cycle: (1) cyclization of newly injected terminally redundant linear phage DNA carrying `loxP` sites at both ends, and (2) resolution of dimeric/multimeric prophage plasmids into monomers so they can be partitioned prior to cell division. Emphasized that P1 prophage exists as an autonomous extrachromosomal plasmid rather than integrating into the host chromosome during its normal life cycle.
  - Quote: `"A site-specific recombinase, Cre, which appears promptly after infection, is involved in phage DNA cyclization ( 137 ), assists plasmid maintenance by resolving plasmid multimers ( 21 ), and perhaps, by a separate mechanism, may stabilize plasmid copy number"`
  - Quote: `"Whereas λ prophage leads an essentially passive existence within the chromosome of its host, P1 prophage exists as an autonomous plasmid that is maintained at low copy number."`
- **UniProtKB `P06956` (`file:genes/BPP1/cre/cre-uniprot.txt`)**:
  - Quote: `"CC   -!- FUNCTION: Catalyzes site-specific recombination between two 34-base- ... pair LOXP sites. Its role is to maintain the phage genome as a ... monomeric unit-copy plasmid in the lysogenic state."`

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000120`): **MODIFY** to `GO:0043565` (`sequence-specific DNA binding`) and `GO:0000150` (`DNA strand exchange activity`). Cre binds specifically to the 13-bp inverted repeats of 34-bp `loxP` sites and catalyzes site-specific DNA strand exchange via a 3'-phosphotyrosine covalent intermediate (`PMID:9288963`, `PMID:9670032`).
- `GO:0006310` (`DNA recombination`, IEA: `GO_REF:0000120`): **ACCEPT**. Cre catalyzes conservative site-specific DNA recombination at `loxP` sites to circularize linear viral DNA and resolve plasmid dimers (`PMID:9288963`, `PMID:15489417`).
- `GO:0015074` (`DNA integration`, IEA: `GO_REF:0000120`): **REMOVE**. Over-propagated from `InterPro:IPR002104` (`Integrase catalytic domain`) and `UniProtKB-KW:KW-0229` (`DNA integration`). Unlike lambda Int, P1 does not integrate into the bacterial chromosome during normal lysogeny; instead, P1 is maintained as an autonomous extrachromosomal plasmid (`PMID:15489417`), and Cre's physiological role is intramolecular cyclization of linear phage DNA and resolution of plasmid dimers into monomers (`PMID:15489417`, `file:genes/BPP1/cre/cre-uniprot.txt`).
