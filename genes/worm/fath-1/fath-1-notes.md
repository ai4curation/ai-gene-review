# fath-1 review notes

Session: initial review of fath-1 (C25A1.5, Q9XVS0, unreviewed TrEMBL).

## Sources consulted
- fath-1-uniprot.txt (PIRNR/PIRSR family rules, Phobius TM helices).
- PMID:30184537 (Li 2018, full text): product rescue by (R)-2-OH fatty acid, expression pattern, organelle phenotypes.
- PMID:23705068 (Zhu 2013, full text): fath-1 RNAi L1 arrest epistatic with cgt-1/cgt-3 and nprl-3.
- PMID:21926990 (Zhang 2011, full text): C25A1.5 RNAi polarity phenotype; GlcCer invariably hydroxylated.
- PMID:14992718 (Tewari 2004, abstract only): Y2H source of FATH-1-DAF-3 IPI.
- Human FA2H review in this repo (genes/human/FA2H) used for consistency.
- See fath-1-deep-research-manual.md for the literature summary with provenance.

## Decisions
- GO:0080132 fatty acid 2-hydroxylase activity (IBA, IEA): ACCEPT. Family (PIRSF005149/IPR014430),
  conserved His di-metal centre and cyt b5 domain; worm in vivo complementation by (R)- but not (S)-2-OH
  fatty acid [PMID:30184537 "The results showed that (R)-2-OH FA supplement nicely rescued the growth defect caused by fath-1 RNAi, while (S)-2-OH FA did not"].
  Not refined to GO:0120520 free fatty acid 2-hydroxylase activity: substrate form not tested in worm (raised as a question).
- GO:0046513 ceramide biosynthetic process (IBA): ACCEPT. FATH-1 performs the 2-hydroxylation step that generates
  the 2-hydroxy acyl chain of ceramides; worm GlcCer is invariably hydroxylated [PMID:21926990].
- GO:0006629 lipid metabolic process (IEA): MODIFY to fatty acid metabolic process and ceramide biosynthetic process.
- GO:0005783 ER (IBA): ACCEPT under root-organelle policy (PAINT seeds Arabidopsis FAH1/FAH2 and mouse Fa2h are ER
  enzymes; worm protein has 4 TM helices). The GFP reporter in PMID:30184537 looked cytoplasmic/nuclear at low resolution;
  this does not resolve the ER and is recorded as a caveat.
- GO:0005789 ER membrane (IEA): ACCEPT (sub-compartment; Phobius TMs + family).
- GO:0016020 membrane (IEA): MODIFY to ER membrane.
- GO:0005515 protein binding (IPI, DAF-3 Y2H): REMOVE per protein-binding policy; removal does not deny the interaction.

## NEW terms considered and rejected
- Developmental / growth / lifespan / dauer / epithelial polarity / lipid droplet process terms: only RNAi phenotype
  evidence; FATH-1 makes a lipid precursor and does not perform those processes. Not proposed.
- glucosylceramide biosynthetic process: plausible (human FA2H review uses it) but not shown in worm
  (no lipidomics of fath-1 RNAi animals for GlcCer-OH). Not proposed; kept as a question.
- heme binding / zinc ion binding: domain-based only; not asserted.
