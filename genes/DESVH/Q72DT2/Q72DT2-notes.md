

## 2026-09-20 TreeGrafter re-review

The current GO:0009055 definition includes redox transformations during enzymatic reactions; AprA performs the FAD-dependent reduction of APS. [QuickGO GO:0009055](https://www.ebi.ac.uk/QuickGO/term/GO:0009055), checked 2026-09-20, therefore supports ACCEPT rather than restricting electron transfer to AprB/Fe-S carriers.

All seven rows were re-reviewed. Retain the succinate-dehydrogenase rejection because APS-specific reaction and domain evidence contradict that activity, not because every SDH/FRD must use covalent FAD. Existing OpenScientist and Falcon adjudications were read and incorporated; no duplicate run requested. Falcon proposes GO:0033748, which is hydrogenase (acceptor) activity, not APS reductase. This identifier is not adopted. Preserve the existing GO:0009973. The plasma-membrane refinement and sulfate-respiration refinement remain reasonable, but direct AprAB interaction with membrane QmoABC means soluble does not itself prove complete absence of peripheral membrane association; a second opinion on GO:0005886 would benefit from direct membrane-fractionation evidence.

Coordinator cross-check: GO:0005886 is now UNDECIDED pending the focused localization report. The evidence does not justify a confident wrong-location claim from soluble topology alone.


## Focused localization adjudication incorporated (2026-09-20)

OpenScientist job 81dccdeb-fe21-441f-ac3c-3c52ef5efa6e recovered direct membrane-preparation and reciprocal Qmo/Apr purification evidence in the exact Hildenborough strain from [PMID:23842468](https://pubmed.ncbi.nlm.nih.gov/23842468/). The fetched cache and publisher abstract explicitly describe these experiments; the cache remains abstract-only. This is evidence for a membrane-associated pool, beyond merely being a soluble electron-transfer partner.

GO:0005886 includes associated proteins; GO:0031234 reaches it through part_of/is_a relations. Live QuickGO definitions and ancestry are preserved in `projects/TREEGRAFTER/rereview-2026-09-20/apra-membrane-term-check.json`. The report accepts a peripheral pool while rejecting the broad plasma-membrane term; that distinction is unsupported by GO. Restore the original row to ACCEPT and add the membrane pool to the biological description/core locations. Do not convert its original IEA into experimental evidence and do not assert exclusive localization. The report claims a sequence-analysis CSV but delivers only PDF/HTML; its numerical results are not independently adopted. The succinate-dehydrogenase rejection remains supported by catalytic chemistry, without claiming the exact grafting error has been reconstructed.
