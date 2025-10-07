# Notes for dorR (CERSP)

## Selection Rationale

This gene was selected as it was featured in Nigel's talk as an example of a bacterial gene involved in photosynthetic regulation. It represents an interesting case study for GO annotation curation in prokaryotes.

## Key Research Findings

From the Falcon research report:

### Gene Function
- Central transcriptional regulator controlling photosynthetic gene expression
- Acts as repressor under aerobic conditions
- Binds to promoter regions of bacteriochlorophyll and carotenoid biosynthesis genes
- Integrates environmental signals (oxygen tension, light intensity)

### Molecular Mechanism
- Redox-sensitive conformational changes via cysteine disulfide bonds
- Interacts with anti-repressor protein AppA under low oxygen conditions
- AppA is a blue-light photoreceptor with BLUF domain
- DNA binding through helix-turn-helix (HTH) motif

### Protein Domains
- C-terminal helix-turn-helix (HTH) DNA-binding motif
- N-terminal PAS domain for redox sensing
- Glutamine-rich coiled-coil "Q-linker" domain for dimerization
- Critical cysteine residues for disulfide bond formation

### Biological Processes
- Negative regulation of photosynthetic gene expression
- Prevention of photooxidative damage under aerobic conditions
- Integration of photosynthetic and respiratory functions
- Orchestration of aerobic/anaerobic metabolism transition

### Conservation
- Conserved across purple non-sulfur bacteria (Rhodobacter, Rubrivivax, Bradyrhizobium)
- Similar to PpsR homologs in related species
- Essential for environmental adaptation

## GO Annotation Implications

Based on the research, key GO terms to consider:
- Transcriptional regulation
- Response to oxidative stress
- Photosystem organization/development
- DNA binding (sequence-specific)
- Protein dimerization activity
- Response to oxygen levels
- Response to light intensity

## Experimental Evidence

Strong experimental support from:
- Mutagenesis studies showing deregulated photosynthetic genes in knockouts
- In vitro DNA-binding assays confirming promoter interaction
- Transcriptome analyses revealing differential expression profiles
- Protein-protein interaction studies with AppA

## Next Steps

1. Review existing GO annotations in the GOA file
2. Compare with research findings
3. Propose appropriate curation actions (ACCEPT/MODIFY/REMOVE)
4. Consider new term proposals if needed