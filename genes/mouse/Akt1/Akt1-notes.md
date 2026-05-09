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
[file:mouse/Akt1/Akt1-deep-research-bioreason.md "A cytoplasmic AGC-type
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
