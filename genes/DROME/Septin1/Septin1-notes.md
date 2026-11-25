# Septin1 (Sep1, P42207) notes

SEPT2-class septin; subunit of the Sep1-Sep2-Pnut complex.

- First Drosophila septin cloned by homology; localizes to cleavage furrow leading edge [PMID:8590810 "The protein is concentrated at the leading edge of the cleavage furrows of dividing cells and cellularizing embryos"]; associates with Pnut [PMID:8590810 "Both immunolocalization and biochemical experiments show that Sep1 is intimately associated with Pnut"]
- Complex purified with Pnut and Sep2 [PMID:8636235 "The purified complex is comprised of the three previously identified septin polypeptides Pnut, Sep2, and Sep1."]
- GTP-domain requirement [PMID:25355953 "We show that Drosophila septin complex functions depend on the intact GTP-binding and/or hydrolysis domains of Pnut, Sep1, and Sep2."]
- Wound repair: Sep1 knockdown phenotype [PMID:38728140 "Sep1 knockdown and Sep2 mutant embryos exhibit delayed wound closure, reduced recruitment of actin to the actomyosin ring, and premature actomyosin ring disassembly"]; binds F-actin [PMID:38728140 "Strikingly, we find that all five Drosophila Septins can bind to and bundle actin filaments"]
- CPTI YFP trap: Sep1 at closing contractile structures [PMID:25294944 "These include Category I proteins Zipper, Msn and Septin 1 and 5 other lines"]
- Border cells [PMID:37329886 "Expressing RNAi against Sep1, Sep2, or Pnut impaired migration (Figures 2B–2D)."]
- Parkin substrate [PMID:17456438 "peanut and septin1, D. melanogaster septin proteins, were also ubiquitinated by D. melanogaster Parkin"]

Decisions consistent with pnut/Septin2: GTPase ACCEPT (catalytic SEPT2 class), protein binding REMOVE, photoreceptor NAS over-annotated.

## Deep research (falcon) follow-up

The falcon report confirms that purified Sep1 itself incorporates and hydrolyses GTP and that G-motif substitutions reduce both (Akhmetova 2015), supporting GTPase activity as Sep1's core MF and the contrast with Sep2. It also cites Sep1-GFP entering the contractile ring during planar epithelial cytokinesis (Founounou et al. 2013), not in GOA or the cache; no annotations were added.

## 2026-11-15 re-review: photoreceptor cell development source defect withdrawn

The `WRONG_GENE_PRODUCT` source defect on the ComplexPortal NAS row for photoreceptor cell development (GO:0042461, PMID:8181057) was withdrawn. The ComplexPortal record for the Septin1-Septin2-pnut complex (CPX-26526, checked through the complex web service) itself carries GO:0042461, and QuickGO by reference shows the same row, dated 2025-11-21, on the complex and on every subunit of both pnut-containing septin complexes (Septin1, Septin2, Septin4, Septin5 and pnut), with ECO:0005547 (inference from background knowledge). That is ComplexPortal's standard export of a complex-level annotation to its subunits, not a row attached to the wrong gene, and pnut already carries the row, so there was nothing to repoint. The weak basis (a pnut-sina genetic interaction that the authors read as possible pleiotropy; abstract only, full text not read) is a review judgement and stays expressed by MARK_AS_OVER_ANNOTATED.
