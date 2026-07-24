# ITIH3 review notes

## Review scope and provenance

- Target: human **ITIH3**, UniProtKB **Q06033** (inter-alpha-trypsin inhibitor heavy chain H3/HC3).
- Review date: 2026-07-18.
- The GOA stub contained nine source annotations, and every annotation was reviewed manually.
- `just deep-research-falcon human ITIH3 --fallback perplexity-lite` was attempted. Falcon/Edison returned HTTP 402 and Perplexity-lite returned HTTP 401, so no provider-named deep-research file was created. The synthesis below instead uses the reviewed UniProt record, cached primary literature, and the current Reactome participant record.

## Protein identity, processing, and complex assembly

ITIH3 is a secreted precursor processed to a mature HC3 chain. UniProt maps a signal peptide (residues 1-20), an N-terminal propeptide (21-34), the mature heavy chain (35-651), and a C-terminal propeptide (652-890), together with VIT and VWFA domains. The mature C-terminal Asp651 is ester-linked to the chondroitin-4-sulfate chain of bikunin after processing [UniProtKB:Q06033, "Heavy chains are linked to bikunin via chondroitin 4-sulfate"].

Human pre-alpha-inhibitor is composed of HC3 and bikunin. Direct structural analysis showed that the heavy and light chains are joined by a chondroitin-sulfate protein-glycosaminoglycan-protein cross-link [PMID:1898736, "The human blood protein pre-alpha-inhibitor is composed of one heavy and one light protein chain"]. Critically, bikunin is the inhibitory component: purified human pre-alpha-inhibitor "comprises bikunin (BK) responsible for antiprotease activity, covalently linked to a heavy chain H3" [PMID:9188816]. The older chain-stoichiometry study likewise found a single 30-kDa trypsin-inhibitory chain and a distinct 90-kDa heavy chain in pre-alpha-inhibitor [PMID:2476436, "pre-alpha-trypsin inhibitor contains a heavy chain of 90,000 Da"]. ITIH3/HC3 must therefore not inherit the protease-inhibitor activity of bikunin or of the named complex.

## Direct hyaluronan and extracellular-matrix evidence

- Purified human plasma HC3 contains an N-terminal BX7B hyaluronan-binding site, but the activity was conditional: a thermolysin-generated N-terminal fragment strongly bound HA, whereas intact mature HC3 did not [PMID:11168393, "a thermolysin-generated, N-terminal fragment of this H3 chain strongly bound HA whereas the intact H3 chain did not"]. This supports hyaluronic acid binding for a processed HC3 species, not constitutive noncovalent binding by every intact plasma molecule.
- Purified human plasma experiments directly established transfer of HC3 from pre-alpha-inhibitor through a covalent HC3-TSG-6 intermediate to an HC3-hyaluronan product. HC2 is an essential cofactor: "Proteins containing HC2 including IalphaI, HC2.bikunin, and free HC2 promoted the formation of HC3.TSG-6 and subsequently HC3.hyaluronan complexes" [PMID:18448433]. ITIH3 is the transferred substrate/structural heavy chain; TSG-6 and HC2 provide the transfer machinery.
- Mouse biochemical studies found HC3 in physiological and pathological SHAP-hyaluronan complexes as well as in complexes formed in vitro [PMID:18293178, "All three HC isoforms are found in the SHAP-hyaluronan complexes of physiological or pathological origins as well as that formed in vitro"]. Together with the direct human transfer experiment, this supports an extracellular-matrix location for human HC3 by orthology.
- In human airway studies, TSG-6 mediates transfer of heavy chains from inter-alpha-inhibitor/pre-alpha-inhibitor onto HA, while TSG-6-driven release of bikunin increases antiprotease activity [PMID:16873769, "TSG-6 mediates the transfer of the heavy chains from IαI/PαI onto HA"; "bikunin in its free state, but not when associated with HCs, is a relevant protease inhibitor"]. The paper also directly detected HC3 expression in human airway epithelial cells, but this inflammatory context does not justify a broad human airway-disease process annotation for ITIH3.

## Annotation decisions

| Source term | Decision | Rationale |
|---|---|---|
| serine-type endopeptidase inhibitor activity | REMOVE | InterPro transfers the activity of bikunin/the named complex to HC3; direct chain analysis assigns inhibition to bikunin. |
| extracellular region (IEA, TAS, NAS) | MODIFY to extracellular space | Correct but overly broad for a soluble secreted plasma protein. All three duplicate terms receive the same action. |
| hyaluronan metabolic process | ACCEPT | Human HC3 is directly transferred covalently to HA and therefore participates in HA remodeling. |
| protein binding | MARK_AS_OVER_ANNOTATED | The HC3-bikunin/TSG-6 relationships are real but covalent glycosaminoglycan assembly and transfer are not usefully represented by generic protein binding. |
| platelet dense granule lumen | KEEP_AS_NON_CORE | Reactome's current participant set explicitly contains Q06033/ITIH3 in the platelet dense-granule-content set, but the underlying 1992 source is not gene-specific in the accessible record and the location is not a defining HC3 function. |
| extracellular exosome | KEEP_AS_NON_CORE | Retain the HDA detection; a secreted plasma protein can co-purify with vesicle preparations, so this is not a core location. |
| endopeptidase inhibitor activity | REMOVE | The cited cDNA paper does not establish intrinsic HC3 inhibition; independent direct biochemistry assigns inhibition to bikunin. |
| hyaluronic acid binding | NEW | Direct human HC3-fragment binding plus covalent human HC3-HA formation supports the term, with the processing caveat recorded. |
| extracellular matrix | NEW | Direct human HC3-HA formation and mouse HC3 recovery in physiological SHAP-HA matrices support this location conservatively by ISS. |

## Curation boundaries

- HC3 is a transferred substrate/structural matrix component, not the TSG-6 heavy-chain transferase and not the HC2 cofactor that makes HC3 transfer possible.
- The direct noncovalent HA-binding assay is conditional: intact mature human HC3 did not bind in that experiment, whereas a proteolytically generated N-terminal fragment did. The core description must retain this limitation.
- The mouse SHAP-HA work supports a conserved matrix role, but mouse reproductive or inflammatory phenotypes are not sufficient for new human disease, fertility, or inflammatory-process annotations specific to ITIH3.
- The Reactome record is target-specific at the curated participant level: the current `R-HSA-481009` participant set explicitly lists UniProt Q06033/ITIH3. The only linked publication is PMID:1435334, whose cached record has no abstract and no independently checkable ITIH3 text; the localization is therefore retained as non-core rather than promoted into the core function.
- Exosome proteomics establishes recovery from a preparation, not vesicle incorporation or an exosomal activity.

## Open questions

- Which endogenous proteases expose the N-terminal HC3 hyaluronan-binding site, and in which tissues or inflammatory states does that processing occur?
- How does HC2 enable TSG-6-mediated transfer of HC3 from pre-alpha-inhibitor, and does HC2 remain associated with the transfer machinery in vivo?
- Does HC3 confer matrix properties distinct from HC1- or HC2-containing HC-HA complexes?
- Is ITIH3 genuinely stored within platelet dense granules, or does the Reactome participant assignment reflect adsorption or co-isolation of an abundant plasma protein?
