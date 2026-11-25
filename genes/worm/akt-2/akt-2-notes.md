# akt-2 notes

Deep research: `just deep-research-falcon worm akt-2 --fallback perplexity-lite` failed on 2026-10-08 (falcon failed, and the perplexity provider was unavailable in this environment). No deep-research file was created. The review is based on the cached publications, the UniProt record (Q9XTG7) and GOA.

## Key findings
- akt-1 and akt-2 transduce DAF-2/AGE-1 signals and act mainly to antagonize DAF-16 [PMID:9716402 "AKT-1 and AKT-2 function primarily to antagonize DAF-16"].
- AKT-2 is in a complex with AKT-1 and SGK-1, and all three phosphorylate DAF-16 directly [PMID:15068796 "All three kinases of this complex are able to directly phosphorylate DAF-16/FKHRL1"]. AKT-1 and AKT-2 matter more for dauer, and SGK-1 more for lifespan and stress.
- They also phosphorylate SKN-1 [PMID:18358814 "The IIS kinases AKT-1, -2, and SGK-1 phosphorylate SKN-1"].
- AKT-2 binds PIP3 in vitro [PMID:25383666 "both AKT-2 and SGK-1 bound strongly to PIP3"].
- AKT-2 and SGK-1 antagonize AKT-1 in maintaining gonadal basement membrane integrity [PMID:22916022].

## Decisions
- protein binding (4 IPI): REMOVE, because the interactions are captured by the kinase activity and kinase complex annotations.
- IBA "positive regulation of blood vessel endothelial cell migration": REMOVE, because C. elegans has no vasculature.
- Lifespan, NMJ, gene expression and anti-apoptosis annotations: KEEP_AS_NON_CORE.
