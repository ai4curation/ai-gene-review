# Dusp21 (rat) review notes

## 2026-10-28 session

- fetch-gene resolved D3ZAQ8 (RGD:1560427, GeneID 302867) as expected; 26 GOA rows.
- Only one rat experimental row: GO:0005759 mitochondrial matrix IDA from
  PMID:18385140 (Rardin et al. 2008), full text read. Rat testis mitochondria,
  gradient-purified (calreticulin removed), DSP21 peripheral to the IM on the matrix
  side [PMID:18385140 "DSP21 is localized to mitochondria in testis tissue where it peripherally associates with the IM within the matrix compartment"].
- Activity: murine recombinant DSP21 pNPP kinetics and C-to-S loss of activity
  (PMID:18385140); human DUSP21 pTyr > pThr on MAPK peptides (PMID:12408986, abstract);
  STAT3 dephosphorylation in vitro (PMID:39961235, abstract). Core MF chosen as
  GO:0008138 protein tyrosine/serine/threonine phosphatase activity (is_a GO:0004721 only,
  checked with OAK; not a child of GO:0004725/GO:0004722, so those rows are kept, not modified).
- Mouse sperm axoneme MIP (PMID:37295417 abstract only; PMID:37989994, PMID:41764189 full text).
  Mouse KO has normal motility and fertility (PMID:41764189), so the GO:0030317
  flagellated sperm motility rows (rat ISO/IEA from mouse IDA rows that rest on cryo-EM
  structure papers) are marked over-annotated, with a CHECK source defect for UniProt.
- Nucleus/cytoplasm/nucleolus rows trace to the human ortholog, whose nuclear/cytoplasmic
  localization came from N-terminally tagged overexpression (PMID:12408986), which
  PMID:18385140 argues blocks mitochondrial import. Nucleus and nucleolus marked
  over-annotated. Cytoplasm is true but general (mitochondrial matrix and axoneme are both
  part_of cytoplasm per OAK), so MODIFY to GO:0005759 and GO:0160111.
- MAP kinase phosphatase (GO:0017017, InterPro2GO from IPR020420): no KIM/CH2, no MAPK
  activity in cells (PMID:12408986), MAPK not in mitochondria (PMID:18385140): over-annotated.
- No NEW BP terms: KO phenotype is normal; phosphoproteomic changes are not a process
  assignment.
