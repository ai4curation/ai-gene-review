# APH1A curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human APH1A --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, and publication evidence.
- APH1A encodes a multipass non-catalytic gamma-secretase subunit. UniProt summarizes APH1A as a component of the endoprotease complex that cleaves integral membrane substrates including Notch receptors and APP, and says APH1A is required for normal complex assembly.
- Direct APH1A evidence supports complex membership and substrate processing: the Lee et al. abstract states that mammalian APH-1 "physically associates with nicastrin and the heterodimers of the presenilin" and that APH-1 knockdown reduces amyloid-beta peptides plus APP and Notch intracellular domains [PMID:12297508 "physically associates with nicastrin and the heterodimers of the presenilin"; PMID:12297508 "reduction of gamma-secretase products (amyloid-beta peptides and the intracellular domains of APP and Notch)"].
- APH1A should be curated as a non-catalytic adaptor/assembly/activator subunit, not as an independent peptidase. The complex contains presenilin, Pen-2, Aph-1, and nicastrin [PMID:25043039 "The gamma-secretase complex consists of four components: presenilin, Pen-2, Aph-1, and Nicastrin"], while presenilin is the catalytic aspartyl protease subunit in the complex.
- APP and Notch processing are core outputs. The APH1A-containing complex cleaves APP-C100 in vitro [PMID:25043039 "Cleavage of the substrate APP-C100 was blocked by the specific inhibitor III-31C"] and older RNAi/overexpression work describes APH1/PEN2/nicastrin as essential or limiting for gamma-secretase activity [PMID:12763021 "these components are essential for gamma-secretase activity"].
- The steady-state localization emphasis for APH1A is ER and cis-Golgi, with membrane and endomembrane annotations biologically consistent. Plasma-membrane Reactome annotations probably reflect substrate event locations rather than the strongest APH1A-specific localization evidence, so I treated them as retained but non-core.
- Generic `protein binding` annotations capture real interactions but are not informative GO molecular-function statements for APH1A. I marked those as over-annotated rather than removing them, because several are experimental interaction datasets and complex membership is real.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for the main APH1A/gamma-secretase papers documenting APH-1 association with presenilin/nicastrin, APP and Notch proteolysis, purified human gamma-secretase composition, and APH1 isoform effects on substrate cleavage. No annotation action changes were needed: APH1A remains curated as a non-catalytic scaffold/adaptor subunit required for gamma-secretase assembly and complex-level intramembrane protease activity, not as an independent protease.
