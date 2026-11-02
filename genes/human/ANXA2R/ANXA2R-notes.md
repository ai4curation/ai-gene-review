# ANXA2R notes

- Cloned as an annexin II-binding receptor clone from a marrow cDNA library; anti-AXIIR antibody blocks annexin II-stimulated osteoclastogenesis [PMID:16895901].
  - That paper reports type I membrane topology, but UniProt cautions that no TM segment is predicted.
- The same group (Roodman lab) used antibody/knockdown approaches to implicate it in myeloma and prostate cancer adhesion and homing [PMID:22223826; PMID:18636554].
- Overexpressed AXIIR [PMID:23640736]:
  - It is cytoplasmic, activates pro-caspase-8, and is pro-apoptotic independently of annexin II.
  - Protein is barely detectable despite high mRNA.
  - The paper says the gene is "peculiar to human"; the PTHR38820 ortholog check (ANXA2R-bioinformatics/RESULTS.md) finds 92 members in 57 mammals, including mouse Anxa2r, so it is mammal-specific.
- Translation is repressed by two uORFs plus hnRNPA2B1/hnRNPA0/ELAVL1 [PMID:27789685].
- GOA calls:
  - Signaling receptor activity (IEA, InterPro) → UNDECIDED, with the for and against evidence laid out. Recorded as an MF_DARK knowledge gap.
  - CNOT1 IPI (ISG AP-MS screen) → REMOVE.
- No NEW rows: the apoptosis and cancer phenotypes are overexpression or knockdown in tumour lines.
- PANTHER PTHR38820 (ANNEXIN-2 RECEPTOR): no PAINT IBDs, consistent with GOA having no IBA rows.
- Review round (PR #4152):
  - PMID:42225205 is a physiological ligand-to-receptor claim (muscle ANXA2 → hepatocyte ANXA2R, SREBP1c). Its in vivo deletion is of ANXA2, not the receptor.
  - PMID:38806323 shows methylation-driven ANXA2R downregulation linked to melanocyte apoptosis. It is an expression phenotype, not loss of annexin II signalling.
  - PMID:25944712 (mitochondrial N-terminome MS) is UniProt's only MS detection of endogenous protein; abstract-only here.
