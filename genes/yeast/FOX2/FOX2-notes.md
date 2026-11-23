# FOX2 (YKR009C; MFE-2; UniProt Q02207) notes

- Multifunctional enzyme type 2: 2-enoyl-CoA hydratase 2 + D-(3R)-3-hydroxyacyl-CoA dehydrogenase; lacks crotonase, L-(3S)-dehydrogenase and epimerase [PMID:1551874 "demonstrated an absence of activities originally assigned to an MFP of S. cerevisiae (crotonase, L-3-hydroxyacyl-CoA dehydrogenase, and 3-hydroxyacyl-CoA epimerase)"].
- Yeast beta-oxidation goes via the (3R) intermediate [PMID:1551874 "it occurs via a D-3-hydroxyacyl-CoA intermediate"].
- Two SDR dehydrogenase domains A (medium/long chain) and B (short chain); inactivating both abolishes growth on oleate [PMID:10497229 "cells transformed with pYE352::ScMFE-2(aDeltabDelta) failed to grow"].
- C-terminal MaoC-like hydratase 2 domain; EC 4.2.1.119 and 1.1.1.n12 [UniProt:Q02207].
- Peroxisomal; PTS1 plus Pex5p-dependent PTS1-independent import, weak Pex9p import [PMID:30131444 "also exhibits weak receptor activity towards Fox2p and Cta1p"].

## Pathway-context observations (important for module curator)
- YeastPathways context gives EC 4.2.1.17 (S-hydratase) and EC 1.1.1.35 ((3S)-dehydrogenase). These are the wrong stereochemistry for S. cerevisiae: the correct activities are EC 4.2.1.119 (GO:0080023) and (3R)-3-hydroxyacyl-CoA dehydrogenase (GO:0106386).
- The IDA GO:0003857 from PMID:1551874 contradicts its own abstract; reviewed MODIFY -> GO:0106386. IBA node PTN002894972 is seeded only by FOX2 itself, so it inherits the same error.
- PWY-5177 RCA rows (dehydratase, (3S)-dehydrogenase, carboxylic acid catabolism, cytosol) come from a non-beta-oxidation YeastCyc pathway with no yeast evidence for FOX2 involvement.

## Genome-scale metabolic models (2026-11-21)
- Checked FOX2 in iMM904 and yeast-GEM 9.1.1 while reviewing GO-CAM YeastPathways_PWY-5177 [file:gocams/YeastPathways_PWY-5177/YeastPathways_PWY-5177-bioinformatics/gem_gene_audit.md; interpretation in RESULTS.md].
- iMM904 repeats the YeastPathways stereochemistry error: all 12 3-hydroxyacyl-CoA participants on FOX2 reactions are (S), with ECs 4.2.1.17 and 1.1.1.35.
- yeast-GEM is mostly right (28 R) but six participants are (S) (C14, C16, C26: r_2250/r_0057, r_2251/r_2268, r_2253/r_2270) and two are unspecified, although those reactions carry EC 4.2.1.119 / 1.1.1.n12.
- Both models keep FOX2 peroxisomal only. yeast-GEM has the C4 steps (r_2254, r_2271) with (R)-3-hydroxybutanoyl-CoA. Candidate defects to report to the model maintainers; no change to this review.
