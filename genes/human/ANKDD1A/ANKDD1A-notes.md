# ANKDD1A notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKDD1A (Q495B1) has 11 ankyrin repeats and a C-terminal death domain. Its only functional study is in glioblastoma cells: it binds FIH1 (HIF1AN) and lowers HIF1-alpha activity (PMID:30082910). Its promoter is hypermethylated in glioma (PMID:21962230).
- **FIH1 protein-binding IPI (BioPlex, PMID:33961781):** removed in round 1, then MODIFY → GO:0019899 enzyme binding in round 2. The interaction is corroborated by PMID:30082910, but its meaning is unresolved: ANKDD1A could be an FIH1 regulator or an FIH1 substrate, since FIH1 hydroxylates the ankyrin-consensus Asn of many ARD proteins (PMID:17003112). No informative MF term fits yet.
- **Signal transduction IEA (death domain):** MARK_AS_OVER_ANNOTATED; there is no supporting data.
- **Not proposed as NEW:** HIF regulation, which rests on one paper of gain-of-function overexpression in glioma (see round 2).
- No core function; WHOLLY_DARK knowledge gap.

## 2026-10-04 round 2 (reviewer comments on #4067)

- **Correction:** I wrote "no in vivo study exists". PMID:30082910 includes subcutaneous and intracranial U251 xenografts with survival analysis. The real limitation is that every result is gain-of-function: ANKDD1A is overexpressed in glioma lines that silence it, in one paper from one group. The knowledge-gap boundary and description now say so.
- **FIH1 IPI:** REMOVE changed to MODIFY → GO:0019899 enzyme binding (verified in OLS). FIH1 is an asparaginyl hydroxylase, and the interaction is replicated and mapped to the FIH1 N-terminal domain. The term holds whether ANKDD1A is a regulator or a substrate.
