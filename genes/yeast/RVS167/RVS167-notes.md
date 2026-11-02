# RVS167 (P39743, YDR388W) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RVS167 is the experimentally characterised member of PANTHER
PTHR47174:SF1 (Rvs167 subfamily), which also holds Neurospora NCU04637
(Q7S3B9), C. albicans RVS167 (Q59LF3) and S. pombe hob1 (O74352). This review
is of S. cerevisiae Rvs167 in its own right; no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon yeast RVS167 --fallback perplexity-lite` failed:
falcon raised `Exception: Failed to authenticate` (Edison auth), and the
perplexity-lite fallback returned HTTP 401 `insufficient_quota`. No
deep-research file was written. The review is built from the cached
publications (29 PMIDs via `just fetch-gene-pmids`) and the UniProt record.

### Evolutionary grounding

- UniProt: `PANTHER; PTHR47174:SF1; REDUCED VIABILITY UPON STARVATION PROTEIN 167`;
  BAR (17-254) + GPA region + SH3 (421-482). InterPro IPR046982 (BIN3/RVS161-like).
- IBA rows come from two PAINT nodes plus two deeper ones:
  - PTN002932529 (donors SGD RVS161 S000000602, SGD RVS167 S000002796, CGD
    members): endocytosis, lipid binding (contributes_to), plasma membrane
    tubulation. Donors are budding-yeast/Candida only. S. pombe hob1 is
    reported dispensable for endocytosis (InterPro IPR046982 text quoted in
    interpro/panther/PTHR47174/PTHR47174-review.yaml), so the endocytic
    function should not be assumed for every SF1 member outside
    Saccharomycotina without species evidence.
  - PTN002932538: Rvs161p-Rvs167p complex, mating projection tip (SGD donor)
    and medial cortex (PomBase donors only, SPBC21D10.12 hob1 and
    SPBC725.09c).
  - PTN005335241 (actin cytoskeleton), PTN002240831 (actin cortical patch).
- Rvs167 is a donor to these nodes, so its own experimental rows are the
  grounding for the IBAs (not circular).

### Experimentally established in S. cerevisiae (the reference set for transfer)

1. Obligate N-BAR heterodimer with Rvs161 [PMID:20610658 "Because Rvs161 and
   Rvs167 form an obligate heterodimer"; PMID:9434108 two-hybrid + co-IP].
2. Rvs161-Rvs167 complex binds liposomes and tubulates them in vitro
   [PMID:20610658 "the purified Rvs161-Rvs167 complex binds to liposomes in a
   curvature-independent manner and promotes tubule formation in vitro"].
3. Rvs167 N-BAR binds calmodulin; calmodulin enhances tubulation and
   constriction; CaM-binding mutants are defective in endocytic vesicle
   release [PMID:27093085].
4. Required for endocytic internalization [PMID:8590801]; arrives late at
   endocytic sites, and rvs deletion causes invagination retraction rather
   than scission (Kaksonen 2005, PMID:16239147, discussed in PMID:27093085
   full text). Supports NEW GO:0099051 vesicle scission involved in
   endocytosis. Comparator check: GO:0099051 is used sparsely (one yeast
   annotation, VPS1 IMP), so absence on RVS167 reflects low uptake of a
   specific term, not a deliberate curator exclusion; Rvs167 does work in
   the step (membrane constriction, PMID:27093085), passing the participation
   test.
5. SH3 domain binds proline-rich ligands (class I and II; Las17, Abp1, Vrp1,
   Myo5 etc.) [PMID:11743162, PMID:14737190, PMID:19841731, PMID:10388809,
   PMID:9190214]. GO:0070064 proline-rich region binding is the informative
   MF used to MODIFY those GO:0005515 rows.
6. Localization: cortical actin patches [PMID:10393809, PMID:16239147,
   PMID:16824951, PMID:20610658], shmoo tip [PMID:10393809], small-bud tip with
   Gyp5/Gyl1 [PMID:32015451].
7. Redundant with Hof1 for actomyosin ring assembly; SH3-dependent; Iqg1
   recruitment defective in double mutant [PMID:23469085]. Mechanism
   undefined (authors say direct interaction not established) — kept non-core.

### Not established / inferred only

- Direct actin binding: only two-hybrid (PMID:7719850; large-scale
  PMID:10688190). Latrunculin A does not displace Rvs167 from patches
  (PMID:10393809). Not asserted as an MF.
- Exocytosis / ER-Golgi trafficking: suggested from Gyp5/Gyl1 interaction
  (PMID:15802519, PMID:32015451); general vesicle-mediated transport kept as
  non-core, no exocytosis term added.
- Medial cortex: the IBA comes from S. pombe donors only; no budding-yeast
  data beyond a personal communication of bud-neck colocalisation cited in
  PMID:23469085. Marked over-annotated.

### Actions summary

- 69 GO:0005515 rows: Rvs161 partner rows -> MODIFY to GO:0046982 protein
  heterodimerization activity; SH3-domain specificity/ligand rows -> MODIFY to
  GO:0070064 proline-rich region binding; remaining (actin, Vrp1/Myo5 from
  non-domain screens, large-scale screens of other partners) -> REMOVE as
  uninformative (interactions not disputed).
- Core: N-BAR heterodimer membrane binding/tubulation in endocytic vesicle
  scission at cortical actin patches; SH3 proline-rich ligand binding.
