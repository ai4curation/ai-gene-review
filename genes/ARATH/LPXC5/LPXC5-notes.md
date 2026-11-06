# LPXC5 (At1g25210, F4IAW1) notes

Deep research (falcon) fails in this environment (authentication), so no
`-deep-research-*.md` file exists. The shared literature summary for the five-gene
AtLpxC tandem cluster is in `genes/ARATH/LPXC1/LPXC1-notes.md`, and the paralog/active-site
analysis is in `genes/ARATH/LPXC1/LPXC1-bioinformatics/RESULTS.md`.

## Locus-specific points

- Li et al. 2011 Table 1 (PMC3136250) lists At1g25210 as AtLpxC5.
- The canonical UniProt product (F4IAW1, 326 aa) is 100% identical to LPXC1/AtLpxC1.1 and to
  the other three copies, and keeps all E. coli LpxC Zn(2+) ligands and catalytic residues
  (file:ARATH/LPXC1/LPXC1-bioinformatics/RESULTS.md).
- No experiment has targeted this locus alone. The RNAi in Li et al. 2011 hit all five
  genes [PMID:21709257 "To suppress transcription of the five closely linked AtLpxC genes"],
  and the authors could not say which copy is active
  [PMID:21709257 "However, it remains unclear which of the closely related AtLpxC enzymes is functional in vivo"].
- The mitochondrial IDA in GOA comes from the AtLpxC1.1 (LPXC1) GFP fusion
  [PMID:21709257 "The GFP fluorescence from the full-length GFP fusions of AtLpxA and AtLpxC1.1 localized in mitochondria"];
  accepted here because the protein is identical.
- Li et al. list a truncated variant, AtLpxC5.2, that lacks the C-terminal catalytic residues [PMID:21709257 "These residues are truncated in two of the eight AtLpxC proteins, specifically in AtLpxC1.2 and AtLpxC5.2"]. UniProt F4IAW1 records only isoform 1, so the variant is not modelled.
