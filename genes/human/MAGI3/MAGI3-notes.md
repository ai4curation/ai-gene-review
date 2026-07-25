# MAGI3 review notes

## 2026-07-18: setup and research provenance

- UniProt accession: Q5TCQ9; human MAGI3.
- `just fetch-gene human MAGI3` retrieved 59 GOA rows, grouped by the review seeder into 23 annotation records.
- `just fetch-gene-pmids human MAGI3` cached all nine PMID references present in the seeded GOA review.
- The required automated research attempt (`just deep-research-falcon human MAGI3 --fallback perplexity-lite`) could not run: Falcon/Edison returned HTTP 402 (payment required), and Perplexity Lite returned HTTP 401 (quota exceeded). No provider-named research file was created. The evidence synthesis below was therefore performed manually from the local UniProt record, cached primary publications, GOA, and current GO definitions. A standalone synthesis is in `MAGI3-deep-research-manual.md`.

## Functional synthesis

MAGI3 is a large, soluble MAGUK-family scaffold with an N-terminal guanylate-kinase-like region, two WW domains, and six PDZ domains. The guanylate-kinase-like region is not a nucleotide kinase: a full-text MAGI3 study explicitly calls it a "catalytically inactive region of homology to the yeast guanylate kinase" [PMID:27205883 "MAGI3 is a scaffolding protein with 2 WW and 6 PDZ domains, along with a catalytically inactive region of homology to the yeast guanylate kinase"]. This is decisive against GO:0004385 GMP kinase activity and the automatically inferred GMP/GDP metabolic-process annotations.

The founding human paper localized MAGI3 to epithelial tight junctions and showed PDZ-mediated association with PTEN. MAGI3 and PTEN cooperate to modulate AKT/PKB, consistent with MAGI3 positioning a phosphatase in a membrane-proximal signaling context [PMID:10748157 "MAGI3 and PTEN/MMAC cooperate to modulate the kinase activity of AKT/PKB"; PMID:10748157 "MAGI3 allows for the juxtaposition of PTEN/MMAC to phospholipid signaling pathways involved with cell survival"]. A second study directly localized MAGI3 at plasma-membrane, nuclear, tight-junction, adherens-junction, and focal-adhesion sites and showed that it links receptor tyrosine phosphatase beta to a substrate [PMID:12615970 "These findings suggest a possible role for MAGI-3 as a scaffolding molecule that links receptor tyrosine phosphatase with its substrates at the plasma membrane"]. Together these papers support enzyme-substrate adaptor activity, cell-junction localization, and regulation of signaling, but not intrinsic phosphatase or kinase activity.

MAGI3 also organizes receptor-specific signaling through its PDZ domains. It binds beta1- and beta2-adrenergic receptors and attenuates their ERK1/2 output in expression systems [PMID:16316992 "MAGI-3 co-expression with beta1AR profoundly impaired beta1AR-mediated ERK1/2 activation"; PMID:20353789 "beta2AR-stimulated extracellular signal-regulated kinase-1/2 (ERK1/2) activation was substantially retarded by MAGI-3 expression"]. In contrast, endogenous MAGI3 supports LPA2-driven ERK and RhoA activation in SW480 cells, illustrating receptor- and cell-context dependence [PMID:16904289 "MAGI-3 interacts directly with LPA(2) and regulates the ability of LPA(2) to activate Erk and RhoA"]. A mouse study further showed a FZD4-MAGI3-Ltap/Vangl2 complex that activates JNK through Rac [PMID:15195140 "MAGI-3 functions as a scaffold protein for frizzled-4 and Ltap and regulates the JNK signaling cascade"]. Neutral regulation terms are preferable where MAGI3 has opposite effects in different receptor contexts.

An additional direct activity was reported in colorectal-cancer cells: MAGI3 recognizes c-Myc through PDZ5, binds SKP1 through PDZ2, and assembles a c-Myc-MAGI3-SKP1-CUL1 complex that promotes c-Myc K48 polyubiquitylation and proteasomal degradation [PMID:35864508 "these results demonstrate the existence of a macromolecular complex c-Myc-MAGI3-SKP1-CUL1"; PMID:35864508 "MAGI3 modulates c-Myc protein stability by promoting c-Myc ubiquitin–proteasome degradation"]. The molecular activity is best represented as GO:1990756 ubiquitin-like ligase-substrate adaptor activity, not ubiquitin-protein transferase activity: MAGI3 supplies substrate recognition and bridging rather than the catalytic E3 center.

Full-length MAGI3 also binds and inhibits YAP in mammary epithelial cells. A cancer-associated premature-polyadenylation product lacks the C-terminal PDZ6 domain, associates with full-length MAGI3, and acts dominantly to release YAP inhibition [PMID:27205883 "the C-terminal PDZ6 domain of MAGI3 is essential for MAGI3/YAP interaction"]. This is important isoform/pathology context but is not mapped onto the four normal UniProt splice isoforms in the current record.

## Annotation-review decisions

- Accept the junction, tight-junction, plasma-membrane, nuclear, cytoplasmic, and enzyme-substrate-adaptor annotations. The direct localization papers support the otherwise electronic terms.
- Modify generic signal-transduction annotations toward GO:0009966 regulation of signal transduction or GO:0051896 regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction.
- Remove GO:0004385 GMP kinase activity plus GO:0046037 GMP metabolic process and GO:0046710 GDP metabolic process. They are name/domain-driven over-propagation contradicted by the documented catalytically inactive region.
- Mark all GO:0005515 protein-binding annotations as over-annotated. Several interactions are sound and mechanistically useful, but generic protein binding does not describe MAGI3's molecular activity. For PMID:16964398, PMID:21799911, PMID:33961781, and PMID:36115835, the accessible record does not independently expose every MAGI3 pair; the review does not dispute those interaction records.
- Add GO:1990756 ubiquitin-like ligase-substrate adaptor activity and GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process from PMID:35864508.
- Add GO:0070372 regulation of ERK1 and ERK2 cascade, using the neutral regulator term because direct studies report both attenuation and support depending on receptor/cell context.
- Add GO:0043507 positive regulation of JUN kinase activity by orthology from the mouse MAGI3 FZD4-Ltap study.

## Identifier checks

Current Gene Ontology records were checked before use:

- GO:0140767 enzyme-substrate adaptor activity: an adaptor that brings together an enzyme and substrate.
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity: a child of GO:0140767 that brings together a ubiquitin-like ligase and substrate.
- GO:0051896 regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction.
- GO:0070372 regulation of ERK1 and ERK2 cascade.
- GO:0043507 positive regulation of JUN kinase activity.
- GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process.
- GO:0031461 cullin-RING ubiquitin ligase complex.

## Remaining uncertainties

- The normal-tissue importance and tissue distribution of the c-Myc substrate-adaptor mechanism should be independently reproduced outside colorectal-cancer models.
- MAGI3 changes ERK output in opposite directions in beta-adrenergic versus LPA2 receptor contexts. The determinants of this sign switch remain unclear.
- Nuclear localization is experimentally supported, but the relative partitioning of junctional versus nuclear MAGI3 isoforms and the functions of the four normal splice isoforms are unresolved.
- The cancer-associated MAGI3 premature-polyadenylation product is not one of the four curated UniProt alternative products; it should not be treated as a normal isoform without explicit context.

