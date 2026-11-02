# erg1 (SPBC713.12, UniProt Q9C1W3) notes

Module: `ergosterol_biosynthesis` (squalene epoxidase); S. cerevisiae ortholog ERG1 (P32476). Fetch verified: Q9C1W3.

## Evidence
- Reaction squalene + O2 + reduced CPR -> (S)-2,3-epoxysqualene; FAD cofactor [UniProt:Q9C1W3 "Reaction=squalene + reduced [NADPH--hemoprotein reductase] + O2 = (S)-"].
- Inhibition of Erg1 (terbinafine) causes squalene accumulation [PMID:33223513 "Moreover, inhibition of Erg1 leads to the intracellular accumulation of squalene, a toxic metabolite that leads to rapid cell death"]; UniProt disruption phenotype: squalene accumulation.
- Anaerobic induction is Sre1-independent [PMID:16537923 "Importantly, erg1 + , the first oxygen-requiring step in the pathway, was induced anaerobically but was Sre1p independent."] - contradicts UniProt INDUCTION text ("up-regulated via ... sre1").

## Curation decisions
- vacuolar membrane (IEA SubCell, deriving from ORFeome HTP) MARK_AS_OVER_ANNOTATED.
- cytoplasm HDA kept non-core; membrane IEA and sterol metabolic process ARBA modified to specific terms.
- Consistent with yeast ERG1 core function.
