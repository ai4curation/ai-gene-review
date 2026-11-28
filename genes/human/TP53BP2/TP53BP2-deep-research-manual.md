---
title: Manual literature synthesis for human TP53BP2 / ASPP2
gene: TP53BP2
organism: human
provider: manual
---

# TP53BP2 / ASPP2 manual synthesis

TP53BP2 encodes ASPP2, a pro-apoptotic ASPP-family scaffold whose best-supported
molecular function is binding TP53-family transcription factors through its
C-terminal ankyrin-repeat/SH3 region. The original ASPP study identified ASPP1
and ASPP2 as proteins that interact with p53, selectively enhance p53-induced
apoptosis rather than cell-cycle arrest, and increase p53 DNA binding and
transactivation at pro-apoptotic promoters [PMID:11684014]. A later study
extended this activity to p63 and p73, showing that ASPP1/ASPP2 bind these p53
family members and enhance transactivation of Bax, PIG3 and PUMA rather than
MDM2 or p21 [PMID:14729977]. Biochemical and structural work also mapped
differential binding of ASPP2's C terminus to the core domains of p53, p63 and
p73 [PMID:18275817].

ASPP2 was first characterized as 53BP2/Bbp, a p53-binding protein whose
ankyrin/SH3 region contacts the p53 core domain [PMID:8875926]. The same
C-terminal platform binds other apoptosis-regulatory partners including RELA
[PMID:10498867] and Bcl-2-family peptides [PMID:18719108]. These interactions
are real but the GO row `GO:0005515 protein binding` is a bare grouping term;
the useful curated assertion for the conserved function is p53 binding.

TP53BP2 has more ASPP2-specific cytoplasmic and regulatory biology than
PPP1R13B/ASPP1. APCL binds 53BP2 and relocates it to the perinuclear region
[PMID:10646860]. APP-BP1/NAE1 binds ASPP2; ASPP2 reduces APP-BP1-mediated
NEDD8 conjugation to cullin-1 and decreases APP-BP1-driven proliferation and
neuronal apoptosis [PMID:12694406], supporting a TP53BP2-specific negative
cell-cycle annotation. DDX42 binds ASPP2 and shifts ASPP2 between the nucleus
and cytoplasm while dampening ASPP2-driven apoptosis [PMID:19377511].
Additional direct interaction rows with PP1 isoforms, YWHAZ/14-3-3 and other
partners remain best treated as interaction facts rather than new GO functions.

The Human Protein Atlas GO_REF:0000052 rows place TP53BP2 in the cytosol and at
cell junctions. Together with ASPP2 literature on beta-catenin-dependent
epithelial plasticity [PMID:25344754], the cell-junction row is plausible but
peripheral to the core p53-family coactivator function. No new module or GO-CAM
is needed for this compact review.
