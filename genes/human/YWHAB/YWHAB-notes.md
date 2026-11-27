# YWHAB review notes

YWHAB encodes 14-3-3 beta/alpha, one of the ubiquitous 14-3-3 phosphoprotein-binding
adaptors. The GO-CAM activity `gomodel:65a1f4f800003542/65a1f4f800003748`
models YWHAB in the cytoplasm, enabling `GO:0140311` protein sequestering
activity and participating in `GO:0042308` negative regulation of protein import
into nucleus by binding phosphorylated YAP1 downstream of LATS2. This is
consistent with the gene-level review: Zhao et al. showed that YAP2 interacts
with 14-3-3 after LATS-dependent phosphorylation, and Reactome represents YWHAB
as a 14-3-3 beta/alpha dimer that binds phosphorylated YAP1 and sequesters it in
the cytosol [PMID:17974916, "YAP2 interacts with 14-3-3, and this interaction
is completely abolished by phosphatase treatment."; Reactome:R-HSA-2028644,
"YWHAB (14-3-3 beta/alpha) binds phosphorylated YAP1 proteins, sequestering them
in the cytosol."]. No YWHAB-specific GO-CAM correction is needed.

The same biochemical principle explains most of the credible non-Hippo rows.
Grozinger and Schreiber showed that 14-3-3 proteins bind phosphorylated HDAC4
and HDAC5 and sequester them in the cytoplasm, thereby relieving class II HDAC
repression [PMID:10869435, "The association of 14-3-3 with HDAC4 and HDAC5
results in the sequestration of these proteins in the cytoplasm."]. Other rows
come from Reactome events in which 14-3-3 dimers bind phosphorylated BAD, RAF,
KSR1, AKT1S1 and AUF1/BRF family proteins. These were retained as cytosolic,
non-core pathway contexts rather than curated as separate core functions.

Two assertions look over-extended. The Chlamydia paper shows recruitment of
host 14-3-3 beta to the pathogen inclusion membrane through the IncG effector,
which does not make a native human vacuolar membrane location. The PDE3B paper
shows that 14-3-3 binding protects a phosphorylated substrate from
phosphatase-dependent inactivation, not that YWHAB directly inhibits a protein
phosphatase.

All bare `GO:0005515` interaction rows were removed under the project
protein-binding policy. YWHAB has hundreds of reported clients, but the
informative molecular function is phosphoserine/phosphoprotein binding by a
14-3-3 dimer and sequestration or conformational control of phosphorylated
client proteins. The 315 QuickGO rows collapsed to 313 review assertions because
two bare interaction rows were exact duplicates after ignoring GOA date stamps.

Manual deep research note: Falcon and Perplexity were unavailable in the shared
runtime, and this branch was asked not to launch extra provider workers on the
2-CPU host. I therefore used the cached PMID/Reactome records, UniProt entry and
GO-CAM review as manual research inputs rather than creating a provider-named
deep-research file.
