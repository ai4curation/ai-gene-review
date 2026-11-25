# erg1 (SPBC713.12, UniProt Q9C1W3) notes

Module: `ergosterol_biosynthesis` (squalene epoxidase); S. cerevisiae ortholog ERG1 (P32476). Fetch verified: Q9C1W3.

## Evidence
- Reaction squalene + O2 + reduced CPR -> (S)-2,3-epoxysqualene; FAD cofactor [UniProt:Q9C1W3 "Reaction=squalene + reduced [NADPH--hemoprotein reductase] + O2 = (S)-"].
- Inhibition of Erg1 (terbinafine) causes squalene accumulation [PMID:33223513 "Moreover, inhibition of Erg1 leads to the intracellular accumulation of squalene, a toxic metabolite that leads to rapid cell death"]; UniProt disruption phenotype: squalene accumulation.
- Takami et al. quantified fission-yeast squalene and ergosterol by LC-MS/MS after terbinafine treatment, directly tying Erg1 inhibition to squalene accumulation and ergosterol-pathway flux [PMID:23145048 "terbinafine significantly decreased lanosterol level and increased squalene level in wild-type cells"].
- Anaerobic induction is Sre1-independent [PMID:16537923 "Importantly, erg1 + , the first oxygen-requiring step in the pathway, was induced anaerobically but was Sre1p independent."] - contradicts UniProt INDUCTION text ("up-regulated via ... sre1").

## 2026-11-06 re-review

- Re-fetched `SCHPO/erg1`; GOA still has 13 rows and the existing review covers them all. The Q9C1W3 UniProt record advanced from entry version 137 to 138, changing only the OMA cross-reference among cached lines used here.
- Tried the default `just deep-research-falcon SCHPO erg1` provider, but falcon was not available in this environment, so no provider-authored deep-research file was generated.
- Searched for newer direct fission-yeast Erg1/squalene monooxygenase literature with `"erg1" "Schizosaccharomyces pombe" terbinafine fission yeast`, `"Tif302" "erg1" terbinafine fission yeast Erg1`, and `"Schizosaccharomyces pombe" "squalene epoxidase" "LC-MS/MS"`. No newer paper directly assaying S. pombe Erg1 after PMID:33223513 was found; a 2025 Schizosaccharomyces japonicus hopanoid study only used S. pombe as a terbinafine-sensitive comparator.

## Curation decisions
- vacuolar membrane (IEA SubCell, deriving from ORFeome HTP) MARK_AS_OVER_ANNOTATED.
- cytoplasm HDA marked TOO_GENERAL; membrane IEA and sterol metabolic process ARBA modified to specific terms.
- Consistent with yeast ERG1 core function.
