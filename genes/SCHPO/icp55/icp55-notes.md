# icp55 review notes

## Manual deep research

Perplexity deep research failed in this runtime because the wrapper reported `Provider 'perplexity' not available`; I kept the review serial and used this manual note together with the seeded GOA, UniProt, cached publication abstracts, and the GO-CAM source.

## Function synthesis

S. pombe icp55 is the fission-yeast ortholog of S. cerevisiae ICP55 and falls in the M24B metallopeptidase family. The fission-yeast protein has a predicted N-terminal mitochondrial transit peptide, Peptidase M24 catalytic signatures, and predicted manganese-binding residues in the C-terminal peptidase domain.

The direct mechanistic evidence is from S. cerevisiae. Vögtle et al. used mitochondrial N-proteomics and icp55 deletion mitochondria to identify Icp55 as the intermediate cleaving peptidase that removes one residue from a characteristic set of mitochondrial processing peptidase products, converting destabilizing N-termini into stabilizing N-termini and protecting the mitochondrial proteome [PMID:19837041].

The direct S. pombe evidence is subcellular rather than biochemical. The Matsuyama ORFeome YFP screen localized the fission-yeast ORF product to mitochondria at proteome scale [PMID:16823372]. Teixeira and Glaser summarize Icp55 as one of the matrix mitochondrial precursor-processing peptidases, acting after the mitochondrial processing peptidase [PMID:22495024].

The ARBA cytoplasm row is not evidence for a cytosolic icp55 isoform. It is an over-broad cellular-component placement relative to the supported mitochondrial and matrix-side inner-membrane annotations.

## GO-CAM context

GO-CAM 69729a3800007453 uses icp55 as a metalloaminopeptidase activity that occurs in the mitochondrial matrix and is part of mitochondrial protein processing in the matrix-import model. The GO term choices agree with this review.
