# PA2870 (Q9HZX6) review notes

## Summary of the literature

PA2870 is a 525-aa protein with two predicted TM helices (UniProt Phobius, 20-40
and 184-207) flanking a periplasmic region, and a C-terminal GGDEF domain (391-525).
My scan of the UniProt sequence finds the GGEEF motif at 440. No EAL domain.
No name has been assigned.

Literature search (Europe PMC, 2026-11-05, mostly 503 errors; PubMed E-utilities
500 errors). The gene is mentioned only in genome-wide c-di-GMP surveys:

1. Kulasekara et al. 2006 [PMID:16477007]; full text read on PMC (PMC1413825).
   - Table 1: "PA2771 GGEEF — PA2818 EAL — PA2870 GGEEF +(96)" (pmol c-di-GMP per mg
     wet cell weight in extracts of overexpressing PA14; detection limit 12).
   - "P. aeruginosa expressing PA2870 and PA3343, two DGCs that produce high levels
     of c-di-GMP in our assay ( Table 1 ), do not cause an alteration in the biofilm
     phenotype."
2. Merritt et al. 2010 [PMID:20978535]: a single-crossover PA2870 mutant had no
   consistent biofilm defect [PMID:20978535 "Only the single-crossover mutation in
   PA1107 resulted in a consistent observable biofilm defect (not shown)."].
3. Eilers et al. 2022 [PMID:35935233]: the PAO1 deletion reduced early attachment
   [PMID:35935233 "This was clearly observed for 7 mutations, PA0169, PA1120 (yfiN;
   Malone et al., 2010), PA2870, PA3702"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002895344 | GO:0052621 diguanylate cyclase activity | 19 | 205 (28 taxa) | GO:0052621, IDA, PMID:16477007 (PseudoCAP) | SOUND | Extracts of the overexpressing strain contained 96 pmol c-di-GMP/mg (full text read); GGEEF motif intact. Crude whole-cell assay, no purified protein. | E. coli DosC, DgcC/J/M/N/P/Q/Z; B. subtilis DgcK, DgcP; Shewanella DgcS; P. aeruginosa WspR, SadC, GcbA, DgcP, PA3177, PA1107, PA3343 | Yes; see PA1107 notes. No GO_CENTRAL defect for the MF. |

PTN002895351 (GO:0043709 IBD): the node-level GO_CENTRAL defect is recorded once in
PA1107-ai-review.yaml (see PA1107 notes); not repeated here.

## Annotation decisions

- GO:0052621 (IBA, IEA, IDA): ACCEPT; core function.
- GO:0005886 (IBA, IEA): ACCEPT; two predicted TM helices.
- GO:0043709 IBA: MODIFY to GO:1900190. The deletion lowers early attachment in
  PAO1, but other assays show no biofilm phenotype.
- GO:1902201 IBA: KEEP_AS_NON_CORE; no motility data on PA2870.
