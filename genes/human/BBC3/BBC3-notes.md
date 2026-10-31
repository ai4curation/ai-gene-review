# BBC3 / PUMA manual notes

## 2026-09-30 apoptosis review

BBC3 encodes PUMA, a short BH3-only BCL2-family protein that is induced
transcriptionally by p53 and by several p53-independent stress programs. The two
2001 discovery papers are enough to establish the core biology: Yu et al.
identified PUMA as a p53-upregulated mitochondrial protein that binds BCL2 and
BCL-xL through its BH3 domain and rapidly induces apoptosis [PMID:11463391
PUMA induces the rapid apoptosis of colorectal cancer cells], while Nakano and
Vousden independently showed that the alpha and beta isoforms bind BCL2,
localize to mitochondria, induce cytochrome-c release, and help mediate
p53-dependent cell death through the cytochrome-c/APAF1 pathway [PMID:11463392
PUMA, a novel proapoptotic gene, is induced by p53].

PUMA-side interaction rows to canonical anti-apoptotic BCL2-family proteins
should not be re-labeled as `GO:0051434 BH3 domain binding`. That term is
groove-side: it describes the pro-survival BCL2 protein recognizing a BH3
domain. For PUMA, as for BIM, the missing activity is BH3-mediated inhibition
of a pro-survival BCL2-family protein. Chen et al. showed by BH3-peptide
binding that BIM and PUMA engage the five assayed mammalian pro-survival
proteins broadly [PMID:15694340 Differential targeting of prosurvival Bcl-2
proteins by their BH3-only ligands allows complementary apoptotic function].
Ming et al. then tied the BCL-xL interaction to BAX displacement in colon cancer
cells [PMID:16608847 PUMA Dissociates Bax and Bcl-X(L) to induce apoptosis in
colon cancer cells]. Ambroise et al. adds a useful localization nuance: PUMA can
be cytosolic and inactive in Burkitt lymphoma B cells, and apoptosis-promoting
stimuli drive PUMA to mitochondria where it binds BCL2 and MCL1 [PMID:26431330
Subcellular localization of PUMA regulates its pro-apoptotic activity in
Burkitt's lymphoma B cells].

PUMA has weaker direct-activator activity than tBID or BIM, but the activity is
not absent. Du et al. found that Puma BH3 peptides can trigger cytochrome-c
release from Bim/Bid double-knockout mitochondria and, in reconstituted assays,
can relieve BCL-xL or MCL1 inhibition while directly activating BAX and a
truncated BAK construct [PMID:21041309 BH3 domains other than Bim and Bid can
directly activate Bax/Bak]. Because PUMA is both a broad pro-survival inhibitor
and a context-dependent direct activator, the core review should carry the same
two proposed NTR molecular functions used for BIM: pro-survival BCL2 family
protein inhibitor activity and pro-apoptotic BCL2 family effector activator
activity.

The p53 axis should be interpreted as induction of the BBC3 transcript, not as a
PUMA protein role in DNA damage sensing or repair. Han et al. showed that p53
transactivates BBC3 through p53-binding sites in the promoter [PMID:11572983
Expression of bbc3, a pro-apoptotic BH3-only gene, is regulated by diverse cell
death and survival signals]. Chipuk et al. and Follis et al. provide a more
specialized p53-coupling mechanism: newly induced PUMA can disrupt
BCL-xL/cytosolic-p53 complexes, allowing p53 to activate BAX/BAK [PMID:16151013
PUMA couples the nuclear and cytoplasmic proapoptotic function of p53;
PMID:23340338 PUMA binding induces partial unfolding within BCL-xL to disrupt
p53 binding and promote apoptosis].

The ER-stress annotations are downstream-context rows, not UPR machinery rows.
Ghosh et al. showed that PUMA is transcriptionally induced downstream of
CHOP/FOXO3a and contributes to ER-stress-induced neuronal death
[PMID:22761832 CHOP potentially co-operates with FOXO3a in neuronal cells to
regulate PUMA and BIM expression in response to ER stress]. That supports
positive regulation of ER-stress intrinsic apoptotic signaling as a contextual
apoptosis row, but not positive regulation of IRE1-mediated UPR by PUMA.

Several BBC3 rows are useful examples of over-annotation from stress or
interactome readouts. The hypoxia paper argues for BAD, not PUMA, as the
pro-apoptotic correlate in syncytiotrophoblast hypoxia [PMID:20810912 Hypoxia
downregulates p53 but induces apoptosis and enhances expression of BAD in
cultures of human syncytiotrophoblasts]. The EGFR row is a real but contextual
glioblastoma sequestration interaction, while the HuRI/BioPlex/cell-map rows are
large-scale discovery outputs and should not be treated as PUMA's mitochondrial
BCL2-family mechanism without follow-up validation [PMID:20153921 EGFR and
EGFRvIII interact with PUMA to inhibit mitochondrial translocalization of PUMA
and PUMA-mediated apoptosis independent of EGFR kinase activity; PMID:28514442
Architecture of the human interactome defines protein communities and disease
networks; PMID:40205054 Multimodal cell maps as a foundation for structural and
functional genomics].
