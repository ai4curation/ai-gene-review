# RGA4 (ORYSJ, F7J0M4) curation notes

## 2026-10-02 — initial review (claude-code)

Sources: UniProt F7J0M4, GOA (14 rows), falcon deep research, cached publications
PMID:25024433 (full text), PMID:23548743, PMID:21251109, PMID:27289079 (abstract only).
Full text of PMID:23548743 was not retrievable via PMC (PubMed MCP returned abstract only).

### Identity
- CC-NB-ARC-LRR (CNL) protein, 996 aa; Pia / Pi-CO39 locus on chr 11, paired head-to-head with RGA5.
- Both genes required for Pia: [PMID:21251109 "the two NBS-LRR-type R genes, SasRGA4 and SasRGA5"]; [PMID:21251109 "suggesting that SasRGA4 is necessary for Pia function"].
- Pair recognises two unrelated M. oryzae effectors, but binding is to RGA5 only: [PMID:23548743 "revealed direct binding of AVR-Pia and AVR1-CO39 to RGA5-A"].

### Executor function (key paper PMID:25024433, full text)
- Autoactive cell death: [PMID:25024433 "These results suggest that RGA4 acts as a constitutively active cell death inducer."]
- Repressed by RGA5, de-repressed by AVR-Pia binding to RGA5: [PMID:25024433 "RGA4 triggers an AVR-independent cell death that is repressed in the presence of RGA5"].
- Physiological, not overexpression artefact: RGA5 RNAi in Sasanishiki protoplasts triggers death that requires RGA4 [PMID:25024433 "the cell death induced by RGA5 depletion relies entirely on RGA4"].
- P-loop K209R abolishes RGA4 activity; RGA5 P-loop dispensable: [PMID:25024433 "an intact RGA4 nucleotide-binding pocket is required for cell death induction by RGA4"].
- Degenerate MHD (TYG500-502) underlies autoactivity; G502D (TYD) kills it.
- Model: [PMID:25024433 "RGA4 mediates cell death activation, while RGA5 acts as a repressor of RGA4 and as an AVR receptor."]
- Homo- and hetero-complexes via CC domains (Y2H on CC fragments + co-IP in rice protoplasts and N. benthamiana); AVR-Pia does not disrupt hetero-complex.
- Localisation: [PMID:25024433 "Localization studies in rice protoplast suggest that RGA4 and RGA5 localize to the cytosol."] — no nuclear relocalisation on AVR-Pia.

### Bacterial resistance
- Only via engineering: [PMID:27289079 "the transactivation of an auto-active NLR by Xoo-delivered designer TAL effectors"] and TAL-induced AVR1-CO39 in Pi-CO39 lines. Not a natural recognition specificity, so non-core.

### Mechanism unknowns (deep research)
- No resistosome / Ca2+ channel data for RGA4; downstream partners unknown.

### Decisions
- protein binding (IPI, RGA5) -> MODIFY to protein heterodimerization activity (+ homodimerization).
- regulation of PRR signaling pathway (EXP, PHI-base) -> MODIFY: RGA4 is an intracellular NLR, not a PRR-pathway regulator; the paper contains no PRR work. Replace with innate immune response-activating signaling pathway.
- defense response to bacterium IDA from PMID:23548743: abstract is purely about the fungal effectors; bacterial evidence lives in PMID:27289079. Kept as non-core rather than removed (cannot see 2013 full text).
- NEW: defense response to fungus (GO:0050832) — RGA4 is the executor of resistance to M. oryzae; absent from GOA. Participation: RGA4 itself generates the immune/cell-death signal.
- Notably no receptor MF for RGA4 (RGA5 carries innate immune receptor activity EXP). RGA4 must NOT get effector binding / receptor terms.

### Project Q5 (sensor vs executor)
GOA rows for RGA4 and RGA5 are nearly identical (same IDA/IMP/EXP set from the same two papers, same ARBA/InterPro IEAs). Only difference: RGA5 has innate immune receptor activity (EXP) and metal ion binding (IEA, HMA). After review, RGA4 distinctive terms: HR execution (core), heterodimerization with RGA5, nucleotide-binding-dependent signalling; RGA5's PRR-regulation row would map to negative regulation of RGA4 signalling instead.
