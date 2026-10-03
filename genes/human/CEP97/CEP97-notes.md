# CEP97 curation notes

## Deep research status
- `just deep-research-falcon human CEP97` was attempted (first with `--fallback perplexity-lite`, unavailable here; then `--timeout 2400`, which was killed with exit code 137). See the end of this file for the final outcome. The review was written from the cached primary literature.

## Key findings (with provenance)
- Identified in CP110 complexes; recruits CP110 to centrosomes [PMID:17719545 "identified a previously uncharacterized protein, Cep97, that recruits CP110 to centrosomes"]
- Loss causes CP110 loss, spindle defects, polyploidy [PMID:17719545 "Depletion of Cep97 or expression of dominant-negative mutants results in CP110 disappearance from centrosomes, spindle defects, and polyploidy."]
- Suppresses ciliogenesis with CP110 [PMID:17719545 "loss of Cep97 or CP110 promotes primary cilia formation in growing cells"]
- MPHOSPH9 binds CEP97 directly to anchor the cap [PMID:30375385 "recruits CP110-CEP97 by directly binding CEP97"]
- CEP97 does not bind microtubules (unlike CP110) [PMID:39847124 "We found that whereas CEP97 does not bind to microtubules directly, CP110 autonomously binds microtubule plus ends, blocks their growth, and inhibits depolymerization."]
- Also required for early stages of cilia formation in some contexts [PMID:39847124 "CP110 and CEP97 are also required for early stages of cilia formation"]

## Curation decisions (summary)
- 16 protein binding IPIs: REMOVE (uninformative). The CP110-recruiting function is captured by protein-macromolecule adaptor activity (IDA, ACCEPT).
- Centrosome/centriole (incl. HPA GO_REF:0000052 centrosome) and negative regulation of cilium assembly: ACCEPT.
- Regulation of mitotic spindle assembly: KEEP_AS_NON_CORE (likely indirect via CP110 loss).
- No NEW terms (centriole-length effects of CEP97 are probably mediated by CP110; raised as a question).

## HPA cilium atlas vs module role
- Module: stage 1 CP110-CEP97 cap component ("distal centriole cap partner"), process negative regulation of cilium assembly.
- HPA v25: Basal body (A), Centrosome (S), Centriolar satellite (A); main locations centriolar satellite, centrosome, cytosol. GOA carries the HPA centrosome row (GO_REF:0000052), accepted.
- Assessment: consistent with the module role. The basal body call (Approved) is compatible with residual or daughter-centriole/basal-body signal in ciliated cells; the satellite pool is not explained by the module and is raised as a question. core_functions are consistent with the module (adaptor activity in negative regulation of cilium assembly at the centriole).
