# atg-9 (Q9TXN6) review notes

Accession: Q9TXN6 (TrEMBL, 921 aa) is the full-length ATG-9 (T22H9.2a). The other
UniProt entry for the gene, H2L0M4, is a 138 aa product and was not used. No Swiss-Prot
entry exists. Fetched with `just fetch-gene worm Q9TXN6 --alias atg-9`.

Deep research: falcon attempt timed out on 2026-10-08, perplexity unavailable; no deep-research file.

## Key facts
- Atg9 family proteins are lipid scramblases [PMID:33106658 "yeast and human Atg9 are lipid scramblases"; PMID:33106659 "lipid scrambling by ATG9A is essential for membrane expansion"].
- C. elegans ATG-9 scramblase-attenuating mutations enhance lysosome biogenesis without an evident autophagy defect [PMID:40202485].
- ATG-9 localises to presynaptic sites, transported by UNC-104/KIF1A; needed for autophagosome biogenesis near synapses and for AIY presynaptic assembly [PMID:27396362 "ATG-9 localizes to presynaptic sites in neurons"].
- TGN-to-synapse sorting via AP-3 and activity-dependent exo-endocytosis [PMID:35349396].
- RAB-10 needed for ATG-9 punctate localisation in intestine [PMID:28872980].

## Decisions
- Scramblase activity is the core MF (IBA accepted).
- plasma membrane phospholipid scrambling (IEA, inter-ontology inference) removed.
- Presynapse assembly rows kept as non-core (consequence of general autophagy role).
- NEW: GO:0000045 autophagosome assembly (IMP, PMID:27396362).
