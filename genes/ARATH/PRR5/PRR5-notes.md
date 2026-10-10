# PRR5 (APRR5, At5g24470; UniProt Q6LA42) curation notes

## 2026-10-06: initial review (module plant_circadian_clock_oscillator)

- Fetched with `just fetch-gene ARATH Q6LA42 --alias PRR5`. Falcon deep research failed; review based on cached publications.

### Key findings
- Represses CCA1/LHY [PMID:20233950]; binds DNA through the CCT motif [PMID:23027938 "PRR5 associates with target DNA through binding at the CCT motif in vivo"]; ChIP-seq direct targets include flowering-time, hypocotyl and cold-stress TFs [PMID:23027938].
- Represses PIF4/PIF5 [PMID:32165445 "PRRs directly bind the promoters of PHYTOCHROME-INTERACTING FACTOR4 (PIF4) and PIF5 to repress their expression"].
- SCF-ZTL substrate [PMID:17693530 "ZTL targets PRR5 for degradation by 26S proteasomes in the circadian clock and in early photomorphogenesis"]; with TOC1 the only PRR targeted by ZTL [PMID:18562312].
- PRR5-TOC1 heteromer enhances TOC1 nuclear import [PMID:20407420 "TOC1-PRR5 oligomerization enhances TOC1 nuclear accumulation two-fold, most likely through enhanced nuclear import"].
- O-fucosylation by SPY promotes PRR5 proteolysis [PMID:31899321].

### Decisions
- TOC1 protein binding: MODIFY to protein heterodimerization activity (GO:0046982), which has a demonstrated functional consequence. SPY binding: REMOVE (PRR5 is the substrate).
- Response to water deprivation IEP (PMID:41566362, a drought GWAS): UNDECIDED, because the abstract does not mention PRR5.
- Import into nucleus (acts upstream, on TOC1): KEEP_AS_NON_CORE.
