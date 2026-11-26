# cro (P03040) - Curation Notes

## Overview
- **Gene symbol**: `cro`
- **UniProt ID**: `P03040` (`RCRO_LAMBD`)
- **Protein name**: Regulatory protein cro (Antirepressor, 66 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Lytic genetic switch regulator**: Cro (Control of Repressor and Other things) is a 66-residue helix-turn-helix transcriptional repressor that promotes the lytic cycle and antagonizes the lysogenic repressor CI [PMID:17908932, "In the anti-immune (Cro-dominant) state, Cro is expressed from P R and prevents CI expression, presumably by virtue of its high affinity for O R 3, where it can bind to repress P RM"].
- **Homodimerization and operator binding**: Cro folds into an alpha+beta structure (three alpha-helices and a three-stranded antiparallel beta-sheet) and forms a homodimer in solution that binds consensus operator DNA [PMID:7500341, "Based on the distance and dihedral angle constraints derived from the NMR data, the three-dimensional solution structure of the lambda-Cro repressor in the dimeric form has been calculated by the simulated annealing method."; PMID:9653037, "The structure of the Cro protein from bacteriophage lambda in complex with a 19 base-pair DNA duplex that includes the 17 base-pair consensus operator has been determined at 3.0 A resolution."].
- **Reverse operator affinity relative to CI**: Whereas CI binds with highest affinity to `OR1` > `OR2` > `OR3`, Cro binds with highest affinity to `OR3` > `OR2` ~ `OR1`. By occupying `OR3` first, Cro directly represses the `PRM` promoter, shutting off `cI` synthesis during prophage induction and committing the phage to lytic development [PMID:17908932, "We demonstrate that following inactivation of CI by ultraviolet treatment of lysogens, repression of P(RM) by Cro is needed to prevent synthesis of new CI that would otherwise significantly impede lytic development."; PMID:29158090, "After inactivation of CI by SOS-induced cleavage, pR and pL are de-repressed; Cro produced from pR binds to its strongest site oR3 and turns off further CI synthesis, thus ensuring a lysogenic-to-lytic transition"].
- **Negative regulation of early lytic transcription**: At higher concentrations later in early lytic infection, Cro also occupies `OR1`/`OR2` and `OL1`/`OL2`/`OL3`, turning down early rightward (`PR`) and leftward (`PL`) transcription (including `cII`, `cIII`, `N`, and its own gene `cro`) so that the phage can transition to late lytic gene expression [PMID:1065873, "The Cro protein specified by bacteriophage lambda is a repressor essential for normal lytic growth of the virus, thus having a physiological role distinct from that of cI, the repressor that maintains lysogeny."].

## Review of Existing GO Annotations
- `GO:0001046` (core promoter sequence-specific DNA binding, IDA, `PMID:17908932`): **ACCEPT**. Cro binds specifically to the `OR3` (and `OR1`/`OR2`, `OL1`-`OL3`) operators overlapping the `PRM`, `PR`, and `PL` core promoters.
- `GO:0003677` (DNA binding, IDA `PMID:9653037` and IEA `GO_REF:0000120`): **MODIFY** both rows to `GO:0001046` (core promoter sequence-specific DNA binding), which is already experimentally annotated and more specific.
- `GO:0006355` (regulation of DNA-templated transcription, IEA, `GO_REF:0000002`): **MODIFY** to `GO:0032897` (negative regulation of viral transcription).
- `GO:0009411` (response to UV, IMP, `PMID:17908932`): **KEEP_AS_NON_CORE**. UV irradiation activates the host RecA* SOS pathway that cleaves CI; Cro does not sense UV directly, but its binding to `OR3` to repress `PRM` and autoregulate `PR` is required for efficient UV-induced prophage induction once CI cleavage begins.
- `GO:0019042` (viral latency, IEA, `GO_REF:0000043`): **MODIFY** to `GO:0019046` (release from viral latency), as Cro antagonizes latency and promotes the switch from lysogeny to lytic growth.
- `GO:0019046` (release from viral latency, IMP, `PMID:17908932`): **ACCEPT**. Core biological role of Cro during prophage induction.
- `GO:0032897` (negative regulation of viral transcription, IDA `PMID:1065873` and IMP `PMID:17908932`): **ACCEPT** (both rows). Cro represses `PRM`, `PR`, and `PL`.
- `GO:0042803` (protein homodimerization activity, IDA, `PMID:7500341` and `PMID:9653037`): **ACCEPT** (both rows). Cro functions as an obligate homodimer for sequence-specific DNA binding.
- `GO:0045892` (negative regulation of DNA-templated transcription, IMP, `PMID:17908932`): **MODIFY** to `GO:0032897` (negative regulation of viral transcription), which is more specific and already annotated on the gene.
- `GO:0098689` (latency-replication decision, IDA `PMID:29158090` and IEA `GO_REF:0000043`): **ACCEPT** (both rows). Cro is the key pro-lytic factor in the lysis-lysogeny decision.
