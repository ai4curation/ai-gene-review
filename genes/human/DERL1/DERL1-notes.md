# DERL1 curation notes

Deep-research services were unavailable for this family when reviewed. The
manual synthesis below uses the cached UniProt, GOA, PANTHER/PAINT, Reactome and
publication records.

DERL1 is the best-characterized human Derlin. Lilley and Ploegh identified it
as the mammalian Der1 homolog recruited by cytomegalovirus US11 for MHC class I
heavy-chain dislocation and showed that Derlin-1 is essential for US11-driven,
but not US2-driven, MHC class I degradation [PMID:15215855, "Derlin-1 is
essential for the degradation of class I MHC molecules catalysed by US11"].
Ye et al. then placed DERL1 in the ER membrane with VIMP and p97/VCP, tying
luminal substrate recognition to cytosolic ATPase extraction [PMID:15215856,
"with VIMP, a novel membrane protein that recruits the p97 ATPase and its
cofactor"].

The reviewed core is therefore ER membrane retrotranslocation in ERAD. Later
work supports DERL1 binding to ERAD ubiquitin ligases [PMID:16186510, "p97
interacts directly with several ubiquitin ligases and facilitates their
recruitment to Derlin-1"], to the Kf-1/RNF103 ubiquitin ligase [PMID:18675248,
"Kf-1 interacted with components of the ER-associated degradation (ERAD)
pathway, including Derlin-1 and VCP"], to the VCP/p97 ATPase through its SHP
motif [PMID:27714797, "The interaction of the rhomboid pseudoprotease Derlin-1
and p97 is crucial for the retrotranslocation of polyubiquitinated substrates"],
and to an ERAD heterodecamer containing a DERL1 tetramer plus a p97 hexamer
[PMID:37831771, "hetero-decameric complex formed by the Derlin-1 tetramer and
the p97 hexamer"].

The cached PMID:24019521 full text is truncated before the relevant Results
section. The PMC Figure 4A caption directly reports RNF185/RNF5 co-IP against
endogenous DERL1 in HEK293T cells: "A, RNF185 interacts with Derlin-1 and
Erlin2. HEK293T cells were transfected with the control vector, FLAG-RNF185, or
FLAG RNF5".

Several rows are true but contextual. The MHC class I binding rows reflect viral
US11 exploitation of DERL1, not basal ERAD substrate specificity. The HM13/SPP,
TRC8 and XBP1u rows are kept as a non-core regulatory-protein turnover branch
because DERL1 recognizes XBP1u for SPP cleavage [PMID:25239945, "Derlin1 acts
in the complex as a substrate receptor by recognizing the luminal tail of
XBP1u"]. The CAV1/COX-2 rows are treated as substrate-specific readouts rather
than a general ubiquitination-regulatory function.

The current PTHR11009 PAINT slice has ER-membrane, ERAD and UPR IBDs at the
broad PTN000109990 root. ER membrane and ERAD fit DERL1, DERL2 and DERL3 but
need pruning before RHBDD2. The root UPR term is too broad: DERL genes can be
UPR-induced or UPR-protective ERAD factors, but the proteins do not execute the
IRE1, PERK or ATF6 signaling pathway.
