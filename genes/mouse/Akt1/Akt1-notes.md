# Akt1 review notes

Falcon deep research attempt timed out on 2026-05-04 while running
`just deep-research-falcon mouse Akt1`; no `Akt1-deep-research-falcon.md` file
was produced. Review decisions used the cached UniProt record, cached
publications, and BioReason research.

Core function judgment: AKT1 is a PH-domain AGC serine/threonine protein kinase
activated downstream of PI3K and growth factor/insulin signaling. UniProt
describes AKT1 as one of three closely related AKT serine/threonine kinases that
regulate metabolism, proliferation, survival, growth, and angiogenesis through
serine/threonine phosphorylation of downstream substrates [UniProt:P31750
"This is mediated through serine and/or threonine phosphorylation"]. The
BioReason report supports the same architecture-based conclusion:
PH-domain membrane recruitment plus an AGC kinase domain explains
ATP-dependent serine/threonine kinase activity
[file:mouse/Akt1/Akt1-bioreason-rl-predictions.md "A cytoplasmic AGC-type
serine/threonine kinase"].

Key local evidence for process calls includes insulin-stimulated GLUT4
translocation [PMID:9415393 "Physiological role of Akt in insulin-stimulated
translocation of GLUT4"], GSK3/CRMP2 signaling [PMID:22057101 "degrading AKT to
induce GSK3B-dependent CRMP2 phosphorylation"], direct regulation of mTORC2
[PMID:23684622 "Akt directly regulates mTORC2"; PMID:26235620 "positive
feedback loop between Akt and mTORC2"], and MICU1/mitochondrial calcium control
[PMID:30504268 "Akt-mediated phosphorylation of MICU1"].

Curation stance: protein serine/threonine kinase activity and protein
phosphorylation are core. PI3K/AKT, insulin, mTORC1/2, growth factor, survival,
metabolic, migration, and development terms are valid pathway contexts but are
kept as non-core unless the term directly describes AKT1 catalytic activity.
Generic `protein binding`, broad kinase/transferase labels, and very broad
cellular responses are marked as over-annotated when a more informative term is
already present.

## 2026-09-30 refresh

Refreshed the GOA snapshot and resolved 32 newly seeded source rows without
moving any of the survival-kinase pathway rows to apoptosis terms. The
refreshed rows include replicated MGI evidence for BMP2/PI3K/AKT control of
osteoblast differentiation [PMID:19208758 "an intact IGF-induced
PI3-kinase-Akt signaling cascade is essential for BMP2-activated osteoblast
differentiation"], Cntnap2/Akt-mTOR pain and inflammatory hypersensitivity
phenotypes [PMID:31874168 "the dorsal root ganglion (DRG) from Cntnap2-/-
mice also showed hyperactive Akt-mTOR signaling"], TSC/IRS genetic evidence
for PI3K/AKT pathway signaling [PMID:15249583 "TSC1-2 is required for insulin
signaling to PI3K"], and refreshed PAINT support for broad AKT-family
serine/threonine kinase and intracellular signal-transduction assertions.

Removed three newly seeded generic `GO:0005515 protein binding` rows from
PMID:16051150 and PMID:16116448. Those papers support an Akt/beta-arrestin
2/PP2A dopamine signaling complex [PMID:16051150 "D2 class-receptor-mediated
Akt regulation involves the formation of signaling complexes containing
beta-arrestin 2, PP2A, and Akt"] and a BAG1/B-Raf/Akt complex [PMID:16116448
"a tripartite complex formed by Akt, B-Raf and Bag1"], respectively, but the
generic molecular-function term does not identify AKT1's catalytic function or
a specific adapter activity.

The new UniProt EXP kinase rows from PMID:22057101, PMID:26440888, and
PMID:30504268 were accepted because they directly report phosphorylation of
GSK3B, mouse cGAS Ser291, and MICU1 by AKT. Nuclear localization from
PMID:20189988 was kept as non-core, while cytoplasmic and plasma-membrane
localization rows from PMID:19028694 and PMID:20189988 were accepted as part
of the normal PH-domain AKT1 recruitment cycle. The mouse Aatf anti-apoptosis
GO-CAM already places Akt1 upstream of `GO:2001243 negative regulation of
intrinsic apoptotic signaling pathway`, so this refresh did not invent a new
apoptosis annotation from broad pro-survival phenotypes.

## 2026-10-02 PR follow-up

Reclassified the remaining generic `GO:0005515 protein binding` IPI rows from
`MARK_AS_OVER_ANNOTATED` to `REMOVE`, matching the review stance that these
physical-interaction rows do not identify an AKT1 molecular function when a
specific kinase activity or pathway context is available. Added
`propagation_review` blocks to the non-accepted propagated AKT1 rows so broad
or redundant IEA/ISO/IBA transfers explicitly record a scoping problem rather
than implying unsupported human or rat source annotations.
