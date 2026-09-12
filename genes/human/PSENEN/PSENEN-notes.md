# PSENEN curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human PSENEN --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, and publication evidence.
- PSENEN encodes PEN-2, a small multipass membrane subunit of the gamma-secretase complex. UniProt and primary papers support PEN-2 as an essential non-catalytic subunit that modulates presenilin endoproteolysis, complex stability, trafficking, and gamma-secretase activity.
- PEN-2 is a bona fide gamma-secretase complex component: Steiner et al. identify it as "a critical component of PS1/gamma-secretase and PS2/gamma-secretase complexes" and conclude that it is an integral gamma-secretase component [PMID:12198112 "a critical component of PS1/gamma-secretase and PS2/gamma-secretase complexes"; PMID:12198112 "PEN-2 is an integral gamma-secretase complex component"].
- PEN-2 has a direct role in presenilin maturation/endoproteolysis: PEN-2 knockdown abolishes PS1 endoproteolysis and overexpression promotes PS1 fragment formation [PMID:12522139 "Down-regulation of PEN-2 expression by small interfering RNA (siRNA) abolishes the endoproteolysis of PS1"; PMID:12522139 "overexpression of PEN-2 promotes the production of PS1 fragments"].
- Gamma-secretase activity and APP/Notch processing are core outputs. Drosophila/mammalian evidence states that PEN-2 is required for presenilin endoproteolytic processing and confers gamma-secretase activity [PMID:12660785 "PEN-2 is required for endoproteolytic processing of presenilin and conferring gamma-secretase activity to the complex"], while human structural work describes the four-component complex and APP substrate cleavage [PMID:25043039 "The gamma-secretase complex consists of four components: presenilin, Pen-2, Aph-1, and Nicastrin"].
- PEN-2 also contributes to gamma-secretase complex stability and trafficking, not only presenilin endoproteolysis [PMID:24941111 "Pen-2 may also stabilize the complex prior to PS1 endoproteolysis, allowing time for full assembly and proper trafficking"].
- The glucose-starvation/AMPK/TORC1 annotations are retained as non-core. They are not the main human PSENEN gamma-secretase function and appear in GOA via similarity/automatic transfer rather than direct cached human evidence in this review.
- Generic `protein binding` and broad `enzyme binding` annotations are less informative than complex membership and endopeptidase-activator/contribution terms. I marked generic protein binding as over-annotated and kept enzyme binding as non-core.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for PEN-2/PSENEN papers supporting integral gamma-secretase complex membership, presenilin endoproteolysis, complex stability, and purified/structural complex composition. No annotation action changes were needed: PSENEN remains curated as a small non-catalytic gamma-secretase subunit required for presenilin maturation and complex activity, while broad stress-response transfers remain non-core.
