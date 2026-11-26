# btuE (P06610, E. coli K-12) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: btuE is the experimentally characterised reference for the Xanthomonas
BtuE-like ortholog Q8P365 (PANTHER PTHR11592:SF40; shared PAINT node PTN000173904,
Gammaproteobacteria, where PAINT placed an IBD of GO:0008379 thioredoxin peroxidase
activity seeded by P06610). ProtNLM2 outputs were not consulted.

Deep research: `just deep-research-falcon ECOLI btuE --fallback perplexity-lite` failed
(Edison API "Failed to authenticate"/403; perplexity fallback also failed). Review was
done from the cached primary literature, UniProt, and the PTHR11592 PAINT table.
FEBA fitness fetch also failed (no data source reachable).

### What is experimentally established in E. coli
- MF: thioredoxin-dependent hydroperoxide reduction (H2O2, cumene-OOH, t-BuOOH,
  linoleic acid-OOH); TrxA/TrxC preferred; GSH supports H2O2 reduction less well
  [PMID:20621065 "Figure 2 shows that BtuE uses preferentially thioredoxins A or C as reducing agents irrespective of the peroxide substrate."]
- Induction by tellurite, menadione, H2O2 and in stationary phase [PMID:20621065].
  Also upregulated in a sodAB mutant [PMID:41883781 "upregulated the catalase KatE and the organic peroxidases Tpx and BtuE"].
- In vivo antioxidant role: deletion raises ROS/carbonyls/lipid peroxides, Hpx- ΔbtuE
  impaired aerobically, complementation restores [PMID:21264338 "Genetic complementation of E. coli ΔbtuE restored toxicant resistance to levels exhibited by the wild type strain."]
- NOT B12 transport: nonpolar in-frame deletions [PMID:2671656 "Thus, despite its genetic location in the transport operon, the btuE product plays no essential role in vitamin B12 transport."]

### Inferred only (do not over-transfer)
- Peroxidatic Cys37 (HAMAP ACT_SITE, GPX signature); no mutagenesis, no kinetic constants.
  Resolving cysteine unknown (Cys65, Cys84 candidates).
- Lipid hydroperoxides as physiological substrate: suggested, not proven.
- Location: periplasm claimed from 1986 maxicell osmotic shock (partial release) but no
  signal peptide [PMID:3528129 "lacks an obvious signal sequence"]; left UNDECIDED.

### Decisions
- GO:0140824 ACCEPT (core). GO:0008379 (obsolete per QuickGO; redundant with GO:0140824)
  MODIFY -> GO:0140824. GO:0004601, GO:0051920 MODIFY -> GO:0140824.
- GO:0004602 GSH peroxidase KEEP_AS_NON_CORE (real but minor reductant).
- GO:0034599 IBA ACCEPT; GO:0098869 ACCEPT; GO:0000302 IMP ACCEPT; GO:0006979 MODIFY.
- GO:0033194 IEP KEEP_AS_NON_CORE. Periplasmic space (IDA, IEA) UNDECIDED.
- NOT GO:0015889 cobalamin transport ACCEPT (support from PMID:2671656).
