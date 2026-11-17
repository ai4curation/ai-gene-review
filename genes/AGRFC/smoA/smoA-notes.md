# smoA (Atu3277, Q7CS24) notes

## Deep research
- 2026-11-10: `just deep-research AGRFC smoA --provider perplexity` failed (no provider
  credentials / unsatisfiable deep-research-client dependency in the offline environment:
  "All providers failed"). The review is built from the UniProt record and cached primary
  literature instead.

## Literature
- PMID:35074914 (Sharma et al. 2022 PNAS, full text cached) defines the sulfo-SMO cluster
  Atu3277-Atu3285 (smoA-smoI) in A. tumefaciens C58.
  - Proteomics: cluster proteins strongly increased on SQ vs glucose
    [PMID:35074914 "The largest and most significant change we observed was an increase in the abundance of proteins encoded by a single cluster of genes (Atu3277-Atu3285) for cells grown on SQ."]
  - SmoA copurifies with FMN
    [PMID:35074914 "flavin mononucleotide (FMN) was the sole detectable flavin"]
  - Kinetics: NADH strongly preferred over NADPH (kcat/KM 4.1e5 vs 6.8e2 M-1 s-1)
    [PMID:35074914 "indicating that NADH is the preferred cofactor for SmoA"]
  - SmoA, FMN and NADH generate FMNH2 in situ for the SmoC sulfite-release assay
    [PMID:35074914 "SmoC was incubated with SQ in the presence of SmoA, FMN, and NADH, which generate FMNH2 in situ"]
  - No structure of A. tumefaciens SmoA; homolog RoSmoA (A0A1X7D6Q3) also FMN/NADH.

## Annotation decisions
- GO:0052874 FMN reductase (NADH) activity: EXP + EC IEA accepted (core).
- GO:0042602 riboflavin reductase (NADPH) (TreeGrafter): wrong reductant (NADPH activity
  ~600-fold weaker) and riboflavin untested -> MODIFY to GO:0052874.
- GO:0016646 (ARBA): correct parent of GO:0052874 -> MODIFY to GO:0052874.
- GO:0010181 FMN binding: true (FMN copurifies) but FMN is the substrate -> non-core.
- NEW GO:1902777: SmoA supplies the FMNH2 cosubstrate of the C-S cleavage step
  (cofactor-supply case; comparator E. coli SsuE carries GO:0046306 alkanesulfonate
  catabolic process by IDA, the same role in the Ssu system).
- PANTHER PTHR30466:SF11 (HsaB-like reductase subfamily).
