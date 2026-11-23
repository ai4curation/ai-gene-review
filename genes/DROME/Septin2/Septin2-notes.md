# Septin2 (Sep2, P54359) notes

SEPT6-class septin; subunit of Sep1-Sep2-Pnut complex; Sep5 is its retrogene paralog.

- Sep2 alone lacks GTPase activity [PMID:25355953 "Sep2 protein, on the other hand, did not possess any noticeable GTPase activity (Table 1)."], does not exchange GTP [PMID:25355953 "Earlier studies on Drosophila septin complex also suggested that Sep2 does not exchange bound GTP"], structural role [PMID:25355953 "supporting a structural rather than regulatory role for Sep2 in Drosophila septin complex assembly"]. GOA already carries a NOT|enables GTPase activity IDA from this paper.
  -> REMOVE GTPase IBA/ISS and the complex-level IDA (PMID:8636235; contradicted by direct measurement); ACCEPT the NOT row.
- Sep2/Sep5 redundancy [PMID:24433211 "Sep2 Sep5 double mutants have an early pupal lethal phenotype and lack imaginal discs, suggesting that these genes have redundant functions during imaginal cell proliferation"]; oogenesis [PMID:24433211 "Their ovaries have egg chambers containing abnormal numbers of nurse cells."]
  -> 'regulation of cell cycle' IGI marked over-annotated (proliferation defect best explained by cytokinesis).
- Wound repair [PMID:38728140 "Sep1 knockdown and Sep2 mutant embryos exhibit delayed wound closure, reduced recruitment of actin to the actomyosin ring, and premature actomyosin ring disassembly"]
- UniProt spindle location is by similarity only [file:DROME/Septin2/Septin2-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm. Cytoplasm, cytoskeleton, spindle"] -> marked over-annotated.

## Deep research (falcon) follow-up

The falcon report independently concludes that Sep2 is a structural, GTP-bound subunit without detectable intrinsic GTPase activity (Akhmetova 2015; Field 1996), supporting the REMOVE/over-annotated decisions on GTPase rows and the accepted NOT annotation. It also cites Sep2-GFP stability at spermatocyte cleavage furrows and anillin dependence (Goldbach et al. 2010), not in GOA or the cache; no annotations were added.

## 2026-11-15 re-review: photoreceptor cell development source defect withdrawn

The `WRONG_GENE_PRODUCT` source defect on the ComplexPortal NAS row for photoreceptor cell development (GO:0042461, PMID:8181057) was withdrawn. The ComplexPortal record for the Septin1-Septin2-pnut complex (CPX-26526, checked through the complex web service) itself carries GO:0042461, and QuickGO by reference shows the same row, dated 2025-11-21, on the complex and on every subunit of both pnut-containing septin complexes (Septin1, Septin2, Septin4, Septin5 and pnut), with ECO:0005547 (inference from background knowledge). That is ComplexPortal's standard export of a complex-level annotation to its subunits, not a row attached to the wrong gene, and pnut already carries the row, so there was nothing to repoint. The weak basis (a pnut-sina genetic interaction that the authors read as possible pleiotropy; abstract only, full text not read) is a review judgement and stays expressed by MARK_AS_OVER_ANNOTATED.
