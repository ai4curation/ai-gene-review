# AMIGO3 (Q86WK7) review notes

## 2026-10-04: PAINT/affinage review

AMIGO3 is an AMIGO-family adhesion protein and a Nogo-receptor co-receptor.
- **Co-receptor role:** [PMID:23613963 "These findings demonstrate that AMIGO3 substitutes for LINGO-1 in the NgR1-p75/TROY inhibitory signalling complex"]
- **Knockdown in vivo** promotes dorsal column axon regeneration (PMID:30013050).
- **Species:** both papers work mainly in rat. The human IEA rows for complex binding and negative regulation of neuron projection development derive from rat IPI/IMP from PMID:23613963 (QuickGO, Q80ZD5).

Decisions:
- **Accepted:** adhesion (IBA, IEA, ISS), complex binding, negative regulation of neuron projection development, and membrane.
- **Kept as non-core:** brain development (IBA) and nervous system development (IEA). No developmental phenotype is reported.
- **No NEW.** No protein-binding rows.

## Round 1 (PR #4017 review)

- **Complex binding:** GO:0044877 is MODIFYed to GO:0030159 signaling receptor complex adaptor activity, which is also the core MF. AMIGO3 does not bind the myelin ligand, so coreceptor activity (GO:0015026) does not fit. OLS has no Nogo-receptor complex CC term.
- **Adhesion core function added.** The three accepted adhesion rows now have a matching core function.
- **GO:0051965 positive regulation of synapse assembly** appears in `AMIGO3-uniprot.txt` as an IBA:GO_Central cross-reference but is absent from `AMIGO3-goa.tsv`. Live QuickGO (2026-10-04) returns 9 annotations for Q86WK7 and does not include it, so it is a stale UniProt cross-reference. It is not reviewed, and the derived files are not edited.
