# AHP1 (YLR109W, P38013) notes

Module context: `glutathione_thioredoxin_redox_systems`, thiol_peroxidase_step, variant atypical_2cys_prx ("Atypical 2-Cys peroxiredoxin (AHP1)"), MF GO:0140824, BP GO:0042744, cytosol. Not in the YeastPathways summary; no RCA rows; no S. cerevisiae GO-CAM.

## Evidence
- Prx5 subfamily, 176 aa, PANTHER PTHR10430:SF16 [UniProt:P38013].
- Thioredoxin-dependent peroxidase [PMID:10391912 "We demonstrate that both recombinant proteins present a thioredoxin-dependent peroxidase activity in vitro."].
- Substrate preference and electron donor [PMID:9888818 "type I preferentially reduces H2O2 rather than alkyl hydroperoxides, whereas type II shows the reverse specificity"]; [PMID:9888818 "The formed disulfide can then be reduced by thioredoxin, but not by glutathione."].
- Abundance: [PMID:10681558 "Their transcriptional activities suggest that cTPx I and cTPx III are the most predominant isoforms among the five type isoforms."]; cTPx III = "TSA II/AHPC1".
- Metal/GSH-depletion sensitivity [PMID:12270680 "We report that Ahp1p protects yeast against toxicity induced by copper, cobalt, chromium, arsenite, arsenate, mercury, zinc and diethyl maleate"].
- Cad1 signalling, urmylation, Mn homeostasis [UniProt:P38013].

## Nomenclature caution
- "TSA II" in PMID:10681558 means AHP1, while "cTPx II" means TSA2. "Type II TPx" (PMID:9888818) is AHP1. This naming collision probably explains why TSA2 also carries SGD rows from PMID:9888818 (see TSA2 notes).
- The module labels AHP1 "atypical 2-Cys"; UniProt describes its catalytic cycle as intersubunit (typical-like) disulfide, Cys62 with Cys31 of the partner subunit per crystal structures. The "atypical" label in the module variant is questionable; "Prx5-type" would be safer.

## Localisation
- Experimental: cytoplasm (PMID:10681558), cytosol (SWAT HDA). C-terminus AHL matches PTS1 consensus and Candida PMP20 is peroxisomal [PMID:10391912 "an abundant yeast protein related to PMP20, a peroxisomal protein of Candida"], so IBA peroxisome kept non-core. IBA mitochondrion marked over-annotated (no presequence; PRX1 is the yeast mitochondrial Prx). Plasma membrane HDA marked over-annotated (abundant soluble protein in membrane proteome).

## Decisions
- Obsolete GO:0008379 rows -> MODIFY GO:0140824. Bare protein binding (PXA2, MYTH) -> REMOVE. NOT protein stabilization accepted.
