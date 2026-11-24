# PA2200 (Q9I1R7) review notes

## Summary of the literature

PA2200 is a 531-aa protein with two predicted TM segments (20-39, 248-273 in
UniProt), a periplasmic region between them, and a C-terminal cytoplasmic EAL
domain (275-528). It has an intact EAL motif.

Literature search (Europe PMC, query "PA2200 AND aeruginosa", 2026-11-05; 18 hits,
mostly unrelated): the only primary data on PA2200 itself are in Kulesekara et al.
2006 (PMID:16477007). I read the full text on PMC (PMC1413825); the cached copy is
abstract-only. Verbatim excerpts:

- Assay: "The ability of the PDE-containing proteins to hydrolyze c-di-GMP was
  tested by adding synthetic c-di-GMP to lysates of strains overexpressing these
  proteins and measuring the disappearance of the dinucleotide from the reaction
  mixture".
- Table 1: "PA2133 ETL — +(71) PA2200 EAL +(61)" (PDE activity as percent of
  added c-di-GMP degraded).
- Phylogeny: "Three of these putative PDE modules, in PA2200, PA2818, and PA3285,
  appear to be more closely related and are not linked to DGCs."
- Overexpression phenotype: "PA14, overexpressing PA2133, PA2200, PA3947, PA4367,
  PA4396, PA5017, and PA5442, were significantly impaired in their ability to kill
  CHO cells."
- Loss of function: "insertion in genes encoding only PDE domains, with the
  exception of pvrR , did not cause a biofilm-related phenotype in our assay."

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002105365 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 18 | 162 (24 taxa) | GO:0071111, IDA, PMID:16477007 (PseudoCAP) | SOUND | Lysates of the overexpressing strain degraded 61% of added c-di-GMP compared with the vector control (full text read). The assay is crude, but the EAL motif is intact. | E. coli PdeA/B/C/F/H/I/K/L/N, DosP; Mtb P9WM13; P. aeruginosa bifA, rocR, PA2133, nbdA, PA2567, PA3825 | Yes. Node-level defects are recorded once in rocR-ai-review.yaml. |

PA2200 is not a seed of PTN009140332, but it inherits its GO:1900190 IBA. The IBD
stands on bifA (see bifA and PA2133 notes). PA2200's own insertion mutant had no
biofilm phenotype.

## Annotation decisions

- GO:0071111 (IBA, IEA, IDA): ACCEPT.
- GO:0005886 (IBA, IEA SubCell): ACCEPT. Two predicted TM helices; no direct
  localisation data.
- GO:1900190 IBA: KEEP_AS_NON_CORE. Plausible for a c-di-GMP PDE, but there is no
  gene-specific biofilm evidence.
