# Pfkfb4 notes

- UniProtKB:P25114 states: FUNCTION: Synthesis and degradation of fructose 2,6-bisphosphate. [UniProtKB:P25114].
- Core interpretation: bifunctional synthesis and degradation of fructose 2,6-bisphosphate.
- Accepted direct GO terms include: 6-phosphofructo-2-kinase activity, fructose 2,6-bisphosphate metabolic process, fructose metabolic process, fructose-2,6-bisphosphate 2-phosphatase activity.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-04

**GOA changes.** Two new IBA rows (GO_REF:0000033): GO:0004331 fructose-2,6-bisphosphate 2-phosphatase activity (PTN000064403) and GO:0006003 fructose 2,6-bisphosphate metabolic process (PTN000743282). One row retired: GO:0006000 fructose metabolic process (IEA, GO_REF:0000002). Its review is kept, with a note that GOA no longer carries it.

**PENDING resolved.**
- GO:0004331 (IBA) -> ACCEPT. Rat Pfkfb4 is inside the PFKFB clade, and its phosphatase was measured directly [PMID:1651918 "The expressed enzyme was bifunctional with specific activities of 90 and 22 milliunits/mg of the kinase and the phosphatase activities, respectively."].
- GO:0006003 (IBA) -> ACCEPT, the direct process reading of both activities; consistent with the existing IEA/ISS rows for the same term.

**Row audit.** No other action changed. Supporting evidence was tightened:
- The two IDA rows from PMID:1651918 quoted only the cloning sentence; they now also quote the measured kinase and phosphatase specific activities (abstract-only cache).
- ATP binding (KEEP_AS_NON_CORE) now cites the measured ATP Km ("KM=270 uM for ATP").
- The ISO kinase row names its donor (human PFKFB4, Q16877).

**Description.** Rewritten as standalone biology (removed "The review accepts ... modifies ... keeps ..."). Added the PKC-but-not-PKA phosphorylation that distinguishes the testis isozyme [PMID:1651918 "The enzyme was phosphorylated by Fru-2,6[2-32P]P2 and also by protein kinase C, but not by cAMP-dependent protein kinase"]. `status` set to COMPLETE.

**Open questions.** None new. The glycolysis and gluconeogenesis NAS rows rest on a review (PMID:15581487) with no cached abstract and stay KEEP_AS_NON_CORE.
