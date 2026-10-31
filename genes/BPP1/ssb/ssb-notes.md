# Curation Notes: ssb (Q9XJG4) — Bacteriophage P1

## Identity & Genomic Context
- **Gene symbol**: `ssb` (alt: `SSB-P1`)
- **UniProtKB**: `Q9XJG4` (`SSB_BPP1`, 162 aa, 18.1 kDa)
- **Organism**: Punavirus P1 (`NCBITaxon:2886926`, *Escherichia phage P1*)
- **Locus**: Located at approximately map unit 26 of the P1 genome, preceded by a C1-repressible operator (`Op26`, `ACTTAAACCTTTTTTAA`) and promoter (`Pssb`) [PMID:10515938, PMID:15489417].

## Molecular Function & Mechanism
1. **Single-Stranded DNA-Binding Protein (SSB-P1)**:
   - Shares 66% amino acid sequence identity with *Escherichia coli* SSB (`P0AGE0`), including a highly conserved N-terminal OB-fold ssDNA-binding domain (residues 6-111) and the conserved acidic C-terminal hexapeptide (`DDDIPF`) that mediates interactions with host replisome and repair proteins [PMID:10515938].
   - When cloned on an intermediate-copy-number plasmid, P1 `ssb` suppresses both the temperature-sensitive DNA replication defect and the UV sensitivity of an *E. coli* `ssb-1` mutant, demonstrating functional interchangeability with host SSB [PMID:10515938].
   - Primer extension and promoter-fusion analyses show that `ssb` is repressed by C1 during lysogeny and expressed exclusively during lytic growth (`PMID:10515938`: *"The expression of SSB-P1 exclusively during lytic growth indicates a function of the protein related to vegetative DNA replication"*).
   - A P1 `ssb` knockout phage remains viable on wild-type *E. coli* because host SSB substitutes for SSB-P1, but SSB-P1 supports vegetative lytic replication when host SSB is limiting or defective [PMID:10515938].

## Review of Existing GOA Annotations
- `GO:0003697` (`single-stranded DNA binding`, IEA `GO_REF:0000002` via `InterPro:IPR000424`, `InterPro:IPR011344`): **ACCEPT**. Core molecular function of SSB-P1.
- `GO:0003677` (`DNA binding`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0238`): **TOO_GENERAL** (entailed by `GO:0003697` `single-stranded DNA binding`).
- `GO:0006260` (`DNA replication`, IEA `GO_REF:0000120` via `InterPro:IPR011344`, `UniProtKB-KW:KW-0235`): **ACCEPT**. Expressed specifically during lytic growth to support vegetative DNA replication and complements the replication defect of *E. coli* `ssb-1` [PMID:10515938].
- `GO:0006281` (`DNA repair`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0234`): **KEEP_AS_NON_CORE**. Cloned P1 `ssb` complements the UV sensitivity of *E. coli* `ssb-1` mutants [PMID:10515938], although its primary physiological role in the phage life cycle is vegetative lytic DNA replication.
- `GO:0006974` (`DNA damage response`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0227`): **TOO_GENERAL** (entailed by `GO:0006281` `DNA repair`).
