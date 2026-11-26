# SYP121 (PEN1/SYR1; At3g11820; Q9ZSD4) curation notes

## 2026-10-02 session

Sources: UniProt Q9ZSD4, GOA (58 rows), SYP121-deep-research-falcon.md, cached publications (many abstract-only; checked `full_text_available`). Added PMIDs 18678865, 20884800, 19794113, 17241452 (verified via PubMed MCP).

### Identity / core activity
- Plasma-membrane Qa-SNARE. Forms ternary SNARE complexes with SNAP33 and VAMP721/722 [PMID:18273019 "plasma-membrane-resident PEN1 promiscuously forms SDS-resistant soluble N-ethylmaleimide sensitive factor attachment protein receptor (SNARE) complexes together with the SNAP33 adaptor and a subset of vesicle-associated membrane proteins (VAMPs)"].
- SNARE-domain variants that fail ternary assembly lose defense activity [PMID:18678865 "Our findings are consistent with the hypothesis that PEN1 acts in plant defense through the formation of ternary SNARE complexes"].
- Constitutive secretion: SYP121ΔC blocks secretion at PM [PMID:32699172 "the dominant-negative truncated protein SYP121ΔC, which blocks secretion at the plasma membrane"]; secGFP traffic suppressed by SYP121 Sp2 [PMID:17662029].
- Cargo: PIP2;7 with SYP61 [PMID:25082856 "Our results show that the post-Golgi traffic of PIP2;7 is mediated by both SYP61 and SYP121, which, together, form a previously unknown SNARE complex."].

### Immunity (project curation question 3: necessity vs participation)
- PEN1 recruited to papillae; 2-h delay in papilla formation in pen1-1 [PMID:15342780 "being required for the polarized secretion events that give rise to papilla formation"].
- Judgement: PEN1 *participates* (executes the fusion step of focal secretion), so `defense response to fungus` (IGI) is ACCEPTED alongside `exocytosis` as the mechanistic core. `response to fungus` (IMP) and `defense response` (TAS) kept as non-core.
- Negative regulation of defense: SYP121+SYP122 suppress SA/JA/ET/PCD [PMID:17241452 "through a molecular function distinct from that of SYP121 in penetration resistance"] -> kept non-core (likely indirect).

### K+ channels
- SYP121 binds KC1, promotes AKT1 gating [PMID:19794113 "SYP121 promoted gating of the inward-rectifying K + channel AKT1 but only when heterologously coexpressed with KC1."]; FxRF motif required [PMID:20884800]. Added NEW `potassium channel regulator activity` (GO:0015459).
- `protein-membrane adaptor activity` (IDA, PMID:16531497, full text available) REMOVED: authors state "These observations do not necessarily confirm an immediate role for the SNAREs in K + channel anchoring, nor do they imply direct protein–protein interaction".
- Stomatal phenotypes (delayed reopening, KAT1 recycling) [PMID:21914010] kept non-core.

### Other
- Protein binding IPIs -> SNARE binding (SNAP33, SYP61, VAMP721) or transmembrane transporter binding (KAT1, PIP2;7); SEC11 and EXO70A1 rows removed (no informative MF term).
- Cytosol HDA marked over-annotated (tail-anchored membrane protein).
- Validation ontology still labels GO:0005484 "SNAP receptor activity" (QuickGO: "helical-bundle zippering fusogenic activity"); core_functions use the validator label.
