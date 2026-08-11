# LOXL2 literature and provenance notes

## Provenance and evidence boundary

No provider-generated deep-research file was present during the initial evidence audit. Falcon subsequently completed `LOXL2-deep-research-falcon.md`; it was inspected as a secondary lead source after the primary-paper findings had been assembled. Its central extracellular-enzyme framing agrees with the cached primary literature, but none of its claims is used here without checking a primary cache or the local UniProt record. These notes remain a manual evidence synthesis and are not presented as provider output. [file:human/LOXL2/LOXL2-deep-research-falcon.md, "The most defensible functional annotation of human LOXL2 is **a secreted copper/LTQ-dependent protein-lysine oxidase that initiates collagen and elastin cross-linking in the extracellular matrix**."]

All biochemical statements below distinguish recombinant human LOXL2 from ortholog loss-of-function evidence and distinguish full-length protein from engineered truncations. The local GOA contains no isoform field, and the reviewed UniProt record contains no `ALTERNATIVE PRODUCTS` block. Consequently, no finding is treated as isoform-specific. Experimental truncations and catalytically inactive mutants are constructs, not curated human isoforms.

## Core catalytic activity and substrates

The strongest direct substrate evidence supports a copper/LTQ-dependent protein-lysine oxidase acting on extracellular collagen and elastin substrates.

- Recombinant human LOXL2 constructs oxidized several collagen types and elastin in vitro: [PMID:20306300, "All of the purified recombinant LOXL2 proteins, with or without the SRCR domains in the N-terminus, showed significant amine oxidase activity toward several different types of collagen and elastin in in vitro amine oxidase assays"]
- Enzymology included fibrillar type-I collagen as well as small diamines: [PMID:20439985, "In this report, we assessed the steady-state enzymatic activity of lysyl oxidase-like 2 (LOXL2) against the substrates 1,5-diaminopentane (DAP), spermine, and fibrillar type I collagen."] Small-diamine activity is an assay capability and should not displace protein substrates as the biologically informative function.
- Recombinant human LOXL2 directly bound and deaminated tropoelastin and generated allysines and cross-linked peptides: [PMID:30676771, "We detected direct interaction between LOXL2 and tropoelastin (TE) and also LOXL2-mediated deamination of TE. Using proteomics, we identified several allysines together with cross-linked TE peptides."] This chemistry was demonstrated in vitro; vascular codistribution only suggests an in-vivo elastogenesis role.
- Endothelial studies support collagen-IV assembly and vascular basement-membrane organization: [PMID:21835952, "Further investigation in vitro by loss and gain of function experiments confirmed that LOXL2 was required for tubulogenesis in 3D fibrin gels and demonstrated that this enzyme was required for collagen IV assembly in the ECM."]
- Later work separates collagen-IV scaffolding from catalysis: [PMID:31759052, "Neither enzyme activity nor catalytic domain were necessary for collagen IV deposition and angiogenesis, whereas the SRCR domains were effective for these processes."] Thus collagen-IV deposition is not itself proof that LOXL2 oxidizes collagen IV under those conditions.

## Cofactors, precursor state, processing, and domain boundary

- Copper loading supports LTQ biogenesis and enzymatic activation: [PMID:29581294, "Biochemical analysis confirms that copper loading robustly activates hLOXL2 and supports LTQ formation."]
- The crystal structure captured a zinc-bound inactive precursor-like state, not the mature active conformation: [PMID:29581294, "Unexpectedly, the copper-binding site of hLOXL2 is occupied by zinc, which blocks LTQ generation and the enzymatic activity of hLOXL2 in our in vitro assay."] The crystallized protein was an engineered residues-318–774 N455Q fragment.
- Glycosylation and secretion were assessed using recombinant human protein expressed in Drosophila S2 cells: [PMID:23319596, "Disruption of N-glycosylation by site-directed mutagenesis or tunicamycin treatment completely inhibited secretion so that only small quantities of inclusion bodies were detected."] This expression-system dependence should be retained.
- LOXL2 must not be described using the classic LOX precursor/propeptide model. LOX and LOXL1 have removable activation propeptides, whereas LOXL2 has four N-terminal SRCR domains. Full-length LOXL2 can be active, and its SRCR1/2 processing is not catalytic activation: [PMID:30676771, "Our data suggest that SRCR domains 1 and 2 are located away from the catalytic domain, supporting the notion that LOXL2 processing is not associated with enzyme activation, as recently proposed in López-Jiménez et al. (4)."]

## Localization audit

The reliable core localization is the secretory pathway and extracellular matrix/basement membrane. Intracellular observations are real experimental contexts but require narrower interpretation.

- Secreted recombinant human LOXL2 and ECM activity are supported by PMID:23319596 and PMID:21835952.
- Nuclear/cytoplasmic LOXL2 was detected by tumor immunohistochemistry, but this does not demonstrate nuclear catalysis: [PMID:22204712, "The protein manifested decreased nuclear expression and increased cytoplasmic expression."]
- Endoplasmic-reticulum accumulation was induced by LOXL2 overexpression in carcinoma cells: [PMID:28332555, "We demonstrate that overexpression of LOXL2 promotes its accumulation in the Endoplasmic Reticulum (ER), inducing ER stress and activating the IRE1-XBP1 signalling pathway of the ER-stress response."] It is a maturation/overexpression context rather than the mature extracellular enzyme's terminal site of action.
- The UniProt chromosome/chromatin localization currently cites PMID:27735137, which belongs to the disputed H3K4me3 evidence chain described below. It should not be treated as secure catalytic localization.

## Retraction and disputed H3K4me3 oxidation

PMID:22483618 is explicitly a retracted publication: [PMID:22483618, "1. RETRACTED ARTICLE"] The linked notice states: [PMID:27392148, "Retraction of Mol Cell. 2012 May 11;46(3):369-76. doi: 10.1016/j.molcel.2012.03.002."] Its LOXL2/H3K4me3 oxidation claim is invalid evidence and must not support chromosome localization or a nuclear histone-oxidase core function.

PMID:27735137 later reasserted that recombinant LOXL2 deaminates H3K4me3: [PMID:27735137, "Infrared spectroscopy and mass spectrometry analyses demonstrated that recombinant LOXL2 specifically deaminates trimethylated H3K4."] Because it is an abstract-only report from substantially the same author group after the earlier paper's retraction, it is classified here as `DISPUTED`, not as independent restoration of the claim. PMID:24239292 likewise depends mechanistically on an H3K4-deaminase premise and is not secure evidence for chromosome-associated catalysis.

The methylated-TAF10 claim is distinct from histone H3K4: [PMID:25959397, "Using an unbiased proteomic approach, we have identified methylated TAF10, a member of the TFIID complex, as a LOXL2 substrate."] It remains context-specific, abstract-only evidence and does not make LOXL2 a stable TFIID subunit.

## Interaction and complex boundaries

The structural fragment studied in PMID:29581294 was monomeric in solution: [PMID:29581294, "Despite the observation of two molecules in a single ASU, hLOXL2 is revealed as being in a monomeric state in solution."] Therefore crystal packing must not be converted into a physiological LOXL2 homodimer annotation.

Reported partners include SNAI1, MARCKSL1, vimentin, collagen IV, fibronectin, and tropoelastin in different assays and disease/cell contexts. These establish pairwise association or context-dependent scaffolding, not one stable complex containing all partners. In particular, the PMID:27339457 cached abstract names binding of fibulin-4 to LOX and LOXL1, not LOXL2; because the cache is abstract-only, the curator's LOXL2 IPI is retained as unverified rather than declared a miscitation.

## Human versus ortholog evidence

Human recombinant protein establishes catalytic activity, structural chemistry, and several interactions. Physiological angiogenesis evidence in PMID:21835952 combines endothelial-cell assays with zebrafish knockdown, while inhibitor phenotypes in PMID:20818376 use xenograft and fibrosis models. These ortholog/model results support conserved biology but do not by themselves demonstrate the identical tissue-specific mechanism in healthy humans.
