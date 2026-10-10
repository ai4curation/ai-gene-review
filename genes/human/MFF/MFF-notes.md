# MFF notes

Deep research (`just deep-research-falcon human MFF`) was attempted and produced no
output in this session, so the review was built from the GOA-seeded references plus
three papers fetched with `just fetch-pmid`.

## Function
- Tail-anchored outer-membrane and peroxisomal protein [PMID:18353969 "Mff and Fis1 are both tail anchored in the mitochondrial outer"].
- Required for both mitochondrial and peroxisomal fission [PMID:18353969 "and it inhibits peroxisomal"].
- Essential DRP1 receptor; re-targeting to the plasma membrane redirects DRP1 [PMID:21149567 "a Mff mutant with the plasma membrane-targeted CAAX motif directed Drp1 to the target"].
- One of several DRP1 receptors (FIS1, MFF, MiD49, MiD51) [PMID:23283981 "multiple receptors can recruit Drp1 to mediate"]; unlike MiD49/51, MFF is on peroxisomes [PMID:23921378 "Unlike Fis1 and Mff, MiD49 and"].
- Activates DRP1 GTPase; oligomerization required [PMID:34347505 "At 100 µM, Mff-∆TM stimulates Drp1 GTPase activity 10-fold"; "Dynamic Mff oligomerization is required for Drp1 activation"].

## Disease
- Biallelic loss of function causes EMPF2, Leigh-like encephalopathy with optic and peripheral neuropathy [PMID:26783368 "Our findings establish MFF loss of function as a cause of disturbed mitochondrial and peroxisomal dynamics"].
- Peroxisome maturation is affected though peroxisomal biochemistry is largely normal [PMID:32224193].

## Curation decisions
- Core MF: GO:0043495 protein-membrane adaptor activity (DRP1 receptor) and GO:0005096 GTPase activator activity (DRP1 activation); both proposed as NEW (GOA has only binding MF terms).
- The dismech EMPF2 entry binds GO:0005096 on its MFF Loss of Function node; consistent with core function 2.
- No ai-gene-review module covers mitochondrial fission; MFF appears only in modules/peroxisome-lifecycle.yaml (MFF-dependent DRP1 division route) without an MF term.
