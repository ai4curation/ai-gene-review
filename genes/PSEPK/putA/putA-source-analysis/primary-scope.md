# Pseudomonas PutA/PutP source and construct boundaries

Read 2026-11-06. Existing publication caches remain unchanged. Official PMC full texts were acquired separately into ignored audit cache.

- PMID10613867, https://pmc.ncbi.nlm.nih.gov/articles/PMC94244/?report=xml : the assayed strain is KT2442. The native insertion mutant and complementation establish proline-utilization genetics; the dual catalytic regions and PutP topology are assigned by sequence comparison, not purified KT2440 kinetics or direct sodium-flux measurement.
- PMID11097893, https://pmc.ncbi.nlm.nih.gov/articles/PMC92447/?report=xml : Table 1 identifies `KT2442` as `Rif r derivative of KT2440`. The Figure 3 caption states: “The strains were P. putida KT2442 (lanes 1 and 2), P. putida S14D2 (lanes 3 and 4), and P. putida KT2442-Pro21 (lanes 5 and 6).” Thus its abstract's KT2440 description must not erase the derivative backgrounds used in the repression comparison. Methods calls the spontaneous mutant KT2440-Pro21, whereas Table 1/Figure 3 call it KT2442-Pro21; this naming difference is retained, not silently repaired. Regulatory evidence is an actual promoter-expression comparison, not an inference from divergent gene orientation. The paper reports a Glu896→Lys mutant; that historical residue number is not newly mapped onto the current 1317-residue Q88D80 record.
- PMID18767154, full cached primary: the construct consists of PutA residues 1–45, expressed as a C-terminal His6 fusion in E. coli BL21(DE3)pLysS. The paper explicitly says “The 6xHis tag was retained for subsequent experiments.” It measures fragment DNA binding and dimerization, not full-length catalytic activity or membrane switching. RCSB 2JXG entity 1 declares the 45-residue protein sequence below; it exactly equals frozen Q88D80 residues 1–45. The entity representation omits the experimental His tag, and generic P. putida source metadata alone does not specify the donor strain.

```
MATTTLGVKLDDPTRERLKAAAQSIDRTPHWLIKQAIFNYLEKLE
```

The exact sequence bridge supports attribution of the N-terminal DNA-binding domain. It does not establish full-length sequence identity for historical constructs or transfer E. coli substrate-channeling kinetics to KT2440. Sodium-coupled transport by KT2440 PutP is supported as a conserved-function inference by its specific NCBIfam assignment and curated RuleBase statement; primary pathway genetics alone does not measure ion coupling or stoichiometry.
