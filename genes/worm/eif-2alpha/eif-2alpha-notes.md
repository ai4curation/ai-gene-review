# eif-2alpha (Q9BKU3, Y37E3.10) notes

Deep research: the falcon and perplexity-lite run failed (falcon timeout; perplexity unavailable). No deep-research file.
Q9BKU3 is the only UniProt entry for this gene (TrEMBL). All 8 GOA rows are IBA/IEA.

## Key findings
- eIF2 alpha subunit [PMID:32292896 "The gene eif-2alpha (Y37E3.10) in C. elegans encodes for the alpha subunit of eukaryotic translation initiation factor 2 (eIF2)."].
- Ser49 is the stress phosphosite [PMID:32292896 "This result confirms that serine 49 is the site of phosphorylation in eif-2alpha in response to salt stress and is a novel finding for heat and oxidative stress in C. elegans."].
- ER stress needs eIF2alpha phosphorylation [PMID:38161330 "The ISR was not dispensable under ER stress conditions, as demonstrated by the requirement for PERK and eIF2α phosphorylation for decreased translation and wild type-like survival."].
- GCN-2 phosphorylates eIF2alpha under mitochondrial stress [PMID:22719267 "supporting the role of GCN-2 in eIF2α phosphorylation in response to stress"].
- Neuronal S49D enhances dauer entry [PMID:28292919]. Semaphorin signaling lowers phospho-eIF2alpha [PMID:18413715].

## Curation decisions
- All translation-initiation IBA/IEA rows are accepted; ribosome binding is kept as non-core.
- NEW: GO:0036499 PERK-mediated unfolded protein response (IMP, PMID:38161330). Comparator: human EIF2S1 (P05198) carries
  GO:0036499 by IDA in GOA (QuickGO, checked 2026-10-08). Phospho-eIF2alpha is the effector that inhibits eIF2B; it is not
  only a substrate. The ER UPR module models eIF2alpha as a PEK-1 target, not a participant; the module curator should
  note this possible tension.
