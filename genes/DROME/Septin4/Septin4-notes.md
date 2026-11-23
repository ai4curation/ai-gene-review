# Septin4 (Sep4, Q0KHR7) notes

SEPT2-class septin (paralog of Sep1); subunit of the Sep4-Sep5-Pnut complex. Poorly characterised beyond wound repair.

- Two complexes [PMID:38728140 "Taken together, our findings further suggest that Sep1/Sep2/Pnut and Sep4/Sep5/Pnut are functioning as distinct complexes within the context of cell wound repair."]
- Phenotype [PMID:38728140 "Sep4 knockdown and Sep5 mutant embryos exhibit delayed actomyosin ring disassembly"]; localization [PMID:38728140 "Pnut, Sep4, and Sep5 are also enriched in a ring at the wound edge, but this ring overlaps completely with the actomyosin ring"]
- F-actin binding [PMID:38728140 "Strikingly, we find that all five Drosophila Septins can bind to and bundle actin filaments"]

Decisions: GTPase IBA/ISS ACCEPT (SEPT2 class is catalytic); regulation of exocytosis and synaptic vesicle IBAs (donors only mammalian SEPTIN5) MARK_AS_OVER_ANNOTATED; mitochondrion ISS from human SEPTIN4 (ARTS isoform property) REMOVE.

## Deep research (falcon) follow-up

The falcon report treats Sep4 GTP binding/hydrolysis as family-level inference (no Sep4-specific biochemistry), agreeing with accepting the IBA/ISS GTPase rows only as inherited. It warns that human SEPT4/ARTS is a different protein, consistent with removing the mitochondrion ISS. It cites a 2026 bioRxiv wound-recruitment screen and a 2023 dissertation (Sep4 RNAi impairs border-cell migration); neither is peer-reviewed or cached, so no annotations were added.

## 2026-11-15 re-review: photoreceptor cell development source defect withdrawn

The `WRONG_GENE_PRODUCT` source defect on the ComplexPortal NAS row for photoreceptor cell development (GO:0042461, PMID:8181057) was withdrawn. The ComplexPortal record for the Septin4-Septin5-pnut complex (CPX-26529, checked through the complex web service) itself carries GO:0042461, and QuickGO by reference shows the same row, dated 2025-11-21, on the complex and on every subunit of both pnut-containing septin complexes (Septin1, Septin2, Septin4, Septin5 and pnut), with ECO:0005547 (inference from background knowledge). That is ComplexPortal's standard export of a complex-level annotation to its subunits, not a row attached to the wrong gene, and pnut already carries the row, so there was nothing to repoint. The weak basis (a pnut-sina genetic interaction that the authors read as possible pleiotropy; abstract only, full text not read) is a review judgement and stays expressed by MARK_AS_OVER_ANNOTATED.
