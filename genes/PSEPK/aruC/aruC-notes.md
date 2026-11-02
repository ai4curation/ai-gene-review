# aruC / PP_0372 curation notes

PP_0372 is named `aruC` in the submitted genome annotation, but the standard
Pseudomonas AruC/AstC role is the catabolic succinylornithine transaminase in the
arginine succinyltransferase operon. In KT2440 that operon contains PP_4481,
whereas PP_0372 belongs to the separate K00821/SF79 anabolic branch and is the
strongest candidate for the acetylornithine aminotransferase step. The
assignment is still indirect: no PP_0372 enzyme assay or knockout phenotype was
retrieved [file:PSEPK/aruC/aruC-deep-research-openscientist.md, "no direct
enzymology has been performed on PP_0372 or its close ortholog PA0530
themselves"].

A direct KT2440 study identifies its tested PP_4481 insertion as `argD (= astC
[PP_4481])` and reports that this mutant remains arginine prototrophic because
another transaminase can compensate; it does not identify PP_0372 as that
enzyme [PMID:31451546, full text checked online; local cache is abstract-only].


## 2026-10-25 systematic arginine-panel review

PP_0372/Q88QW2 must be distinguished from PP_4481/astC. Full PMID31451546 Table1 explicitly maps its argD insertion to PP_4481; retained prototrophy does not demonstrate absent activity and does not prove PP_0372 compensation. PMID35254100 identifies astC as the AST-pathway succinylornithine transaminase. PP_0372 acetylornithine activity and the pre-existing NEW biosynthetic annotation remain explicit SF79/classIII inferences, supported by comparative E. coli ArgD enzymology (PMID10074354). No new BP is proposed. PLP binding is supported by a curated RuleBase family statement and InterPro classification rather than the ARBA cofactor line. Comparative ArgD/AstC dimer structures support homomerization as an inference, not direct KT2440 measurement. Free-ornithine activity remains unresolved; family preference for acylated substrate is not proof of its absence. Provider claims of exclusive anabolic/catabolic separation or exact measured target kinetics are not adopted.

All 6 annotation rows were inspected. Imported term, evidence, original reference and qualifier payloads were preserved. No new annotation rows were added. Broad catalytic terms were refined rather than rejected solely for generality; core substrate/cofactor binding and metabolic compartment annotations were judged on biology.

Existing OpenScientist research was reused for discovery, with source-specific caveats above; no provider text was rewritten. `just fetch-fitness PSEPK aruC` failed because no local or remote FEBA data source was reachable (log `.cache/module-audit-logs/arginine-fitness-aruC.log`); this is an access failure, not absence of fitness phenotypes. PMID35285712 supplies independently inspected native BarSeq context but no uninspected per-target score is asserted.

Primary PMID31451546 was normally re-fetched with full text; its table-preserving source is https://pmc.ncbi.nlm.nih.gov/articles/PMC6805116/. Negative auxotrophy results do not establish absence of enzyme function. No pyoverdine, biofilm or oxidative-stress BP was manufactured from indirect arginine-pool phenotypes. Independent annotation-reviewer consultation agreed with the ArgJ uncertainty, NADP refinement and pathway-scoping distinction.
