# CD74 notes

Deep research providers unavailable in this environment (`just deep-research-falcon human CD74
--fallback perplexity-lite` failed). Research from the 23 cached publications and UniProt P04233.

## Topology and localization
- Type II single-pass membrane protein: cytoplasmic N-terminal tail with dileucine endosomal sorting
  motifs, TM segment, large lumenal C-terminal region containing CLIP and the trimerization domain.
- Main pools: ER (assembly with MHC class II), Golgi/TGN, transport and endocytic vesicles, endosomal
  MHC class II loading compartments, lysosome membrane (where Ii is degraded).
  [PMID:1448172 "it contains a cytoplasmic signal that targets the class II-invariant chain complex to an
  acidic endosomal compartment"]
- A minor plasma-membrane / cell-surface pool exists, with the lumenal domain exposed extracellularly;
  this pool is the MIF receptor [PMID:17045821 "CD74 alone mediated MIF binding"] and
  [PMID:19665027 "Expression of CD74-variants lacking an ER-retention signal showed CD74/CXCR4 complexes at the cell surface"].
- Also detected extracellularly as a chondroitin-sulfate-modified glycopeptide and in B-cell exosomes.

## Functions
1. MHC class II chaperone: trimer binds class II dimers in the ER, CLIP blocks the groove
   [PMID:7477400 "The structure shows that the CLIP fragment binds to DR3 in a way almost identical to that
   in which antigenic peptides bind class II histocompatibility glycoproteins"], and the tail routes the
   complex to endosomes for peptide exchange by HLA-DM.
2. Cell-surface MIF receptor: binds MIF; signalling requires CD44 [PMID:17045821] and can involve
   CXCR2/CXCR4 [PMID:19665027, PMID:17435771]; outputs are ERK1/2, AKT, NF-kB, cytokine/prostaglandin
   production, survival and p53 suppression.

## Curation decisions
- Protein-binding rows: CXCR2, CXCR4 and CD44 rows modified to signaling receptor binding; the DnaK/HLA-DR
  paper and the two ISG-network rows removed as uninformative.
- `prostaglandin biosynthetic process` (IDA) modified to positive regulation of prostaglandin biosynthetic
  process: CD74 signals, it does not synthesize.
- CD4 receptor binding (PMID:24942581) and the mouse-transferred NOS2-CD74 complex / NOS binding rows set
  UNDECIDED; the cached evidence does not establish them in human.
- Broad locations (lysosome, membrane, cytoplasm) modified or kept non-core in favour of the specific
  compartments already annotated.
