# kilA (P19653) — Curation Notes

## Summary
- **Gene symbol**: `kilA`
- **UniProtKB**: `P19653` (`KILA_BPP1`, 266 aa, 29.6 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Protein KilA encoded upstream of `repL` in the C1-controlled `kilA-repL` lytic replication operon. Contains an N-terminal KilA-N domain (aa 21-121, `InterPro:IPR018004`) and a C-terminal ANT domain (aa 171-225, `InterPro:IPR005039`) with a Cro-like helix-turn-helix DNA-binding motif (aa 176-195) homologous to the P1/P7 Ant1/Ant2 antirepressor proteins. Dispensable for lytic DNA replication and phage development, but overexpression or unrepressed expression is lethal to `E. coli` host cells or interferes with plasmid establishment after transformation.

## Literature Evidence
- **Hansen 1989 (`PMID:2661830`)**:
  - Sequenced the P1 L-replicon region (`X14937`) and identified the promoter-proximal 266-codon `kilA` open reading frame upstream of `repL`, controlled by C1 operator `Op53`. Showed that `kilA` is non-essential for L-replicon function, that its expression is lethal to cells or blocks plasmid establishment, and that its C-terminal region shares extensive sequence homology with P1/P7 Ant proteins including a 20-aa Cro-like helix-turn-helix DNA-binding motif.
  - Quote: `"The promoter-proximal reading frame is 266 amino acid residues long and is not essential for replicon function. In fact, expression of that open reading frame either interferes with plasmid establishment after transformation or is lethal to cells."`
  - Quote: `"Near the C terminus is a 20-amino-acid sequence matching the consensus characteristic of the cro-like DNA-binding proteins with an alpha-helix-turn-alpha-helix motif"`
- **Sternberg & Cohen 1989 (`PMID:2661831`)**:
  - Demonstrated by insertional mutagenesis that `kilA` is non-essential for both L-replicon plasmid replication and P1 lytic development, whereas `repL` is essential for lytic replication, and confirmed that derepression of `kilA` from promoter `P53` kills the bacterial host unless suppressed by the Ant1/Ant2 antirepressor complex.
  - Quote: `"The kilA gene was shown to be non-essential for both replication and lytic development whereas the repL gene probably encodes an essential replication protein."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Reviewed the `kilA-repL` operon and noted that the physiological role of KilA in the P1 life cycle remains unclear despite its conserved N-terminal KilA-N domain and C-terminal Ant-like HTH domain.
  - Quote: `"The repL gene is in an operon with the preceding gene, kilA , whose function is unclear ( 112 , 295 ). When expressed, kilA is lethal to E. coli . Its product is dispensable for phage replication."`

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000120`): **ACCEPT**. Supported by the conserved C-terminal Cro-like helix-turn-helix DNA-binding motif (`PMID:2661830`, `InterPro:IPR005039`) and the N-terminal KilA-N putative DNA-binding domain (`InterPro:IPR018004`). Because the specific target DNA sequence and physiological process of KilA during natural P1 infection remain unknown (`PMID:15489417`), `GO:0003677` is as specific as current evidence warrants.
