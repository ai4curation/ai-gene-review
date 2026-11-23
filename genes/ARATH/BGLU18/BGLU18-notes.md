# BGLU18 review notes

## Session 1 (2026-10-28)

- fetch-gene resolved Q9SE50 (TAIR AT1G52400, GeneID 841670); GOA has 31 rows all keyed to Q9SE50.
- No deep-research API keys; manual synthesis in BGLU18-deep-research-manual.md.
- Key papers: PMID:16990135 (Lee 2006, abstract only), PMID:19147648 (abstract only),
  PMID:31761937 (full text), PMID:30696747 (full text), PMID:23144921 (full text; BGL1 only in
  aphid expression panel).

### Decisions

- Core MF: abscisic acid glucose ester beta-glucosidase activity (GO:0051993), which is_a
  beta-glucosidase activity (GO:0008422) is_a hydrolase activity, hydrolyzing O-glycosyl
  compounds (GO:0004553) (checked with OLS ancestors). The broader MF rows are MODIFIED to GO:0051993.
- Locations: ER lumen / ER body [PMID:19147648 "BGLU18 protein was exclusively localized in ER bodies formed directly at the wounding site on cotyledons"].
  High-throughput nucleus/chloroplast/plasmodesma/vacuole/peroxisome rows marked over-annotated
  (ER-retention motif; ER body cargo). Extracellular region (AtSubP ISM) removed: signal peptide is
  real but the C-terminal ER-retention motif retains the protein.
- identical protein binding IPI (PMID:16990135) has With/From AT1G54200, which looks like a digit
  transposition of AT1G52400 (BGLU18 itself); recorded as a source defect (WRONG_WITH_FROM).
- defense response to fungus IEP (PMID:19656045): the pathogen is the oomycete
  Hyaloperonospora arabidopsidis, and induction is in compatible (susceptible) interactions, so
  "defense response" and "fungus" are both off. MODIFY to response to oomycetes (GO:0002239), with
  a WRONG_TERM source defect.
- Glucosinolate catabolic process (IBA): BGLU18/PYK10 double mutant fails to hydrolyse 4MI3G
  [PMID:30696747 "These results suggest that 4MI3G is hydrolyzed by BGLU18 and/or PYK10, but not by TGG1 and TGG2"]; kept as non-core.
- No NEW terms proposed.
