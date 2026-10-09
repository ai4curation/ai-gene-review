# Septin2 (Sep2, P54359) notes

SEPT6-class septin; subunit of Sep1-Sep2-Pnut complex; Sep5 is its retrogene paralog.

- Sep2 alone lacks GTPase activity [PMID:25355953 "Sep2 protein, on the other hand, did not possess any noticeable GTPase activity (Table 1)."], does not exchange GTP [PMID:25355953 "Earlier studies on Drosophila septin complex also suggested that Sep2 does not exchange bound GTP"], structural role [PMID:25355953 "supporting a structural rather than regulatory role for Sep2 in Drosophila septin complex assembly"]. GOA already carries a NOT|enables GTPase activity IDA from this paper.
  -> REMOVE GTPase IBA/ISS; MARK_AS_OVER_ANNOTATED the complex-level IDA (PMID:8636235); ACCEPT the NOT row.
- Sep2/Sep5 redundancy [PMID:24433211 "Sep2 Sep5 double mutants have an early pupal lethal phenotype and lack imaginal discs, suggesting that these genes have redundant functions during imaginal cell proliferation"]; oogenesis [PMID:24433211 "Their ovaries have egg chambers containing abnormal numbers of nurse cells."]
  -> 'regulation of cell cycle' IGI marked over-annotated (proliferation defect best explained by cytokinesis).
- Wound repair [PMID:38728140 "Sep1 knockdown and Sep2 mutant embryos exhibit delayed wound closure, reduced recruitment of actin to the actomyosin ring, and premature actomyosin ring disassembly"]
- UniProt spindle location is by similarity only [file:DROME/Septin2/Septin2-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm. Cytoplasm, cytoskeleton, spindle"] -> marked over-annotated.

## Deep research (falcon) follow-up

The falcon report independently concludes that Sep2 is a structural, GTP-bound subunit without detectable intrinsic GTPase activity (Akhmetova 2015; Field 1996), supporting the REMOVE/over-annotated decisions on GTPase rows and the accepted NOT annotation. It also cites Sep2-GFP stability at spermatocyte cleavage furrows and anillin dependence (Goldbach et al. 2010), not in GOA or the cache; no annotations were added.
