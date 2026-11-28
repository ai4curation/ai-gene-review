# DERL2 curation notes

Deep-research services were unavailable for this family when reviewed. The
manual synthesis below uses the cached UniProt, GOA, PANTHER/PAINT, Reactome and
publication records.

DERL2 was initially described as F-LANa in a hepatocellular-carcinoma cDNA study
[PMID:11500051, "F-LANa antisense oligonucleotide suppressed F-LANa expression
in human hepatocellular carcinoma BEL-7404 cells and significantly inhibited
cell growth"]. That growth effect is not the conserved core function. The main
mechanistic paper identified DERL2 and DERL3 as mammalian Derlin-family ERAD
components for misfolded glycoproteins; overexpression accelerated, and
knockdown blocked, misfolded-glycoprotein degradation, and the proteins
associated with EDEM and p97 [PMID:16449189, "Derlin-2 and -3 are associated
with EDEM and p97"].

The core DERL2 role is therefore ER membrane glycoprotein ERAD with p97/VCP and
SEL1L/SYVN1-family complexes. Reactome uses DERL2 in an OS9/SEL1 ERAD E3 ligase
event for unfolded glycoproteins [Reactome:R-HSA-8867288, "protein sel-1
homolog 1 (SEL1L), derlin-2 (DERL2) and protein OS-9 (OS9)"], consistent with
the Oda et al. study. DERL2 also shares the Derlin-family SRP/SRPR interaction
used in ER-stress pre-emptive quality control [PMID:26565908, "through
interactions with the signal recognition particle (SRP)"].

The cached GOA IBA for signal-recognition-particle binding points at the same
PTN000109990 root as the other DERL-family terms, but GO:0005047 is absent from
the current PTHR11009 PAINT slice. The human IDA evidence still supports the
term for DERL2 and DERL3. Conversely, GO:0030968 is not kept as a UPR signaling
pathway term: Oda et al. showed DERL2 and DERL3 are UPR-regulated ERAD factors,
not core UPR transducers.
