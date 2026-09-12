# NCSTN notes

## Review status

- First-pass review completed on 2026-06-19.
- `just fetch-gene human NCSTN` created local UniProt, GOA, publication, and PANTHER-family evidence files; `just fetch-gene-pmids human NCSTN` confirmed all 25 PMID-backed publication caches were present.
- Falcon deep research was attempted with `timeout 180 just deep-research-falcon human NCSTN --fallback perplexity-lite`, but the process timed out and no provider deep-research artifact was written. These notes rely on cached UniProt, GOA, and publication files.
- `just validate human NCSTN` passes cleanly.

## Functional synthesis

NCSTN encodes nicastrin, an essential non-catalytic subunit of the gamma-secretase complex. The original nicastrin paper supports its presenilin association: [PMID:10993067 "Nicastrin, a transmembrane glycoprotein, forms high molecular weight complexes with presenilin 1 and presenilin 2"] and its role in intramembrane proteolysis: [PMID:10993067 "functional components of a multimeric complex necessary for the intramembranous proteolysis of proteins such as Notch/GLP-1 and betaAPP"].

Structural work supports the four-subunit complex model: [PMID:25043039 "The γ-secretase complex consists of four components: presenilin, Pen-2, Aph-1, and Nicastrin"] and the substrate-recruitment framing for nicastrin's extracellular domain: [PMID:25043039 "Nicastrin contains a large extracellular domain that is thought to be responsible for substrate recruitment"].

NCSTN should therefore be curated as an adaptor/activator/substrate-recognition component that contributes to complex-level intramembrane aspartyl endopeptidase activity, not as an independently catalytic peptidase. APH1/PEN2/nicastrin perturbation studies support the broader complex function in APP and Notch processing: [PMID:12297508 "mAPH-1 is probably a functional component of the gamma-secretase complex required for the intramembrane proteolysis of APP and Notch"].

## Annotation decisions

- Accepted gamma-secretase complex membership, protein-macromolecule adaptor activity, endopeptidase activator activity, contribution to intramembrane aspartyl endopeptidase activity, APP catabolic/metabolic process, amyloid-beta formation, Notch receptor processing, membrane-protein intracellular domain proteolysis, protein processing, and core ER/Golgi/endosomal/plasma-membrane locations.
- Modified broad `endopeptidase activity`, `peptidase activity`, `proteolysis`, and `membrane protein ectodomain proteolysis` annotations toward complex-level intramembrane proteolysis/protein-processing terms.
- Marked generic `protein binding` annotations as over-annotated.
- Kept melanosome, focal adhesion, extracellular exosome, azurophil granule membrane, sarcolemma, synaptic membrane/vesicle, cerebellum development, ATPase binding, and growth-factor receptor binding as non-core.

Final action distribution: 73 ACCEPT, 12 KEEP_AS_NON_CORE, 10 MARK_AS_OVER_ANNOTATED, 4 MODIFY.

## Knowledge gaps and experiments

- The key ontology/curation issue is how to represent NCSTN substrate recruitment separately from presenilin catalytic activity.
- Useful experiments would use endogenous NCSTN extracellular-domain mutants to separate complex assembly, substrate recruitment, APP cleavage, and Notch cleavage.
- Compartment-resolved gamma-secretase assays would clarify which NCSTN-containing pools process APP versus Notch in vivo.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for the core NCSTN/gamma-secretase papers supporting nicastrin complex membership, APP/Notch proteolysis, and structural placement. No annotation action changes were needed: NCSTN remains curated as a non-catalytic substrate-recruitment/adaptor component of the presenilin-containing gamma-secretase complex, with broad peptidase terms modified toward complex-level intramembrane proteolysis and generic interaction/localization terms kept non-core or over-annotated.
