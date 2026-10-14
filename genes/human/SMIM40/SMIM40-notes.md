# SMIM40 notes

## 2026-10-03 - initial review (MICROPROTEINS Tier 2)

### Identity
- UniProt Q5STR5 (SIM40_HUMAN), 79 aa, PE1. HGNC:54073, chr 6p21.32. NCBI GeneID 113523636, no aliases.
- Single predicted helical TM segment, residues 35-55 [file:human/SMIM40/SMIM40-uniprot.txt "FT   TRANSMEM        35..55"];
  membrane location by sequence prediction only (ECO:0000255).
- Own sequence inspection: acidic N-terminus (MAEEGDVDEADVF...), Pro/Arg segment before the TM, Trp/Leu-rich
  juxtamembrane region after it (YKLLWLLLWAKLGDWLL), acidic C-terminal tail (...EEELEL). Not tested experimentally.
- Protein-level evidence: UniProt cites a large-scale human liver phosphoproteome MS study (PMID:24275569)
  [file:human/SMIM40/SMIM40-uniprot.txt "RP   IDENTIFICATION BY MASS SPECTROMETRY [LARGE SCALE ANALYSIS]."]. No modified residue is annotated in the entry.
- Locus (Ensembl REST overlap 6:33300000-33350000): SMIM40 (ENSG00000286920, - strand, 33323628-33329279)
  sits immediately upstream of DAXX (same strand, ends 33323259), with ZBTB22 and TAPBP further downstream,
  i.e. in the class II/extended MHC region. A second Ensembl gene (ENSG00000285064, "novel protein") spans
  the same region and encodes the same 79-aa product only via a nonsense_mediated_decay transcript
  (ENST00000453407); UniProt lists both Ensembl genes.

### Family / conservation
- Own family: InterPro IPR062398 SMIM40, Pfam PF29122 [file:human/SMIM40/SMIM40-uniprot.txt "DR   InterPro; IPR062398; SMIM40."].
  No PANTHER family; PAN-GO 0 IBA.
- Ensembl Compara (orthologues): 41 species, all mammals, including marsupials (monodelphis, phascolarctos, vombatus)
  and mouse/rat; none in platypus, birds or fish -> therian-mammal gene.

### Expression
- HPA "Tissue enriched (retina)" [file:human/SMIM40/SMIM40-uniprot.txt "DR   HPA; ENSG00000286920; Tissue enriched (retina)."];
  Bgee lists granulocytes as top (11 cell types/tissues only) - expression is narrow and low.

### Literature
- PubMed esearch "SMIM40" (2026-10-03): 0 hits. NCBI Gene has no linked PubMed records.
- Only references in UniProt: chr6 genome sequence (14574404) and the liver phosphoproteome (24275569); neither functional.

### Conclusion
- No functional literature. IEA membrane: ACCEPT. core_functions empty. No NEW terms. Not in gocams/index.tsv.
- Mouse orthologue exists, so a mouse knockout is feasible.
