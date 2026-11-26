# ABCB9 (TAPL) review notes

Deep research (`just deep-research-falcon ... --fallback perplexity-lite`) failed in this environment (no provider API keys); research done directly from cached publications and the UniProt record.

## Function
- Homodimeric half-size ABC transporter; ATP-dependent peptide translocation [PMID:15863492 "TAPL forms a homodimeric complex, which translocates peptides across the membrane. Peptide transport strictly requires ATP hydrolysis."]
- Broad length specificity 6->59-mer [PMID:15863492 "ranging from 6-mer up to at least 59-mer peptides with a preference for 23-mers"]
- Terminal-residue preferences [PMID:18434309 "At both ends, TAPL favors positively charged, aromatic, or hydrophobic residues"]
- Basal ATPase, uncoupling grows with peptide length [PMID:31417173 "TAPL shows a basal ATPase activity, which is inhibited in the presence of longer peptides."]
- Not a substitute for TAP in MHC-I loading [PMID:17977821 "TAPL does not, however, restore MHC class I surface expression in TAP-deficient cells"]

## Localization (key for surface benchmark)
- Steady state: lysosomal limiting membrane; NOT plasma membrane [PMID:17977821 "TAPL was detected in the lysosomal compartment co-localizing with the lysosome-associated membrane protein LAMP-2"; PMID:10748049 "ABCB9 protein colocalized with the lysosomal markers, LAMP1 and LAMP2"]
- TMD0 encodes lysosomal targeting; coreTAPL lacking TMD0 mis-targets to the plasma membrane [PMID:20377823 "in contrast to the full-length transporter, the core translocation complex is targeted preferentially to the plasma membrane"]
- Early ER calls (TAPL-GFP transient overexpression; PMID:11011155, PMID:15577206) are superseded; ER is biosynthetic transit [PMID:30877195 "we demonstrate that TAPL takes the direct route to lysosomes"]
- LAMP-1/2 retain TAPL on limiting membrane [PMID:22641697 "LAMP proteins retain TAPL on the limiting membrane of endosomes and prevent its sorting to intraluminal vesicles"]
- Lipid-raft microdomains of lysosomal membrane [PMID:21212514]

## Curation issues
- GOA row ER membrane IDA cites PMID:1101155 (1975 alpha-1-antitrypsin/COPD paper); likely typo for PMID:11011155. Recorded as source defect (MGI).
