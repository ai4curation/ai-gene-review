# sar1 review notes

## Setup

- `just fetch-gene SCHPO sar1` created the review stub, GOA seed, and UniProt cache.
- `just fetch-gene-pmids SCHPO sar1` found all cited PMIDs already present or cached the missing records.
- `just mod-description-deep-research SCHPO sar1` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO sar1 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `sar1` lineage.

## Literature and database evidence

- The original S. pombe cloning paper isolated the fission-yeast Sar1 homolog by functional complementation of a budding-yeast `sec12ts` mutant [PMID:1396601, "we screened cDNA expression libraries derived from the fission yeast Schizosaccharomyces pombe and from the plant Arabidopsis thaliana for complementation of the sec12ts mutation"].
- The same paper also established `stl1+`/`spo14+` as the S. pombe Sec12-like exchange factor, which places Sar1 upstream of COPII assembly at the ER [PMID:1396601, "That Stl1p and Stl2p are functional homologues of Sec12p was confirmed by showing that expression of either cloned gene complements a sec12 null mutation"].
- Matynia et al. directly linked S. pombe `sar1` to early secretion: the `sns-A10` mutant carries a lesion in the fission-yeast Sar1 homolog and accumulated secretory cargo in the ER [PMID:11839792, "sns-A10, sns-B2 and sns-B9 have mutations in the fission yeast homologues of S. cerevisiae Sar1p, Sec31p and Sec53p, respectively, which are required for the early steps of the protein secretory pathway"].
- Nakamura-Kubo et al. showed that Spo14/Sec12 is a Sar1 GEF in the forespore-membrane setting: Sar1 overproduction suppressed both spo14 sporulation and vegetative growth defects [PMID:12631727, "Overproduction of psr1(+) coding for an S. pombe Sar1 homologue suppressed both the sporulation defect of spo14-B221 and cold-sensitive growth of newly isolated spo14-6 and spo14-7 mutants"].
- Conserved budding-yeast work summarized by Kurokawa et al. supports the GO-CAM placement of Sar1 as the GTPase that recruits inner coat, is stimulated by Sec23/Sec31 for GTP hydrolysis, and must come off the coat before vesicle tethering [PMID:27432890, "Sar1-GTP on the ER membrane recruits Sec23 and Sec24 forming an inner layer on COPII-coated vesicles through the interaction with Sec23, and the transmembrane cargo is captured by the contact with Sec24 to form a pre-budding complex"].

## GO-CAM context

Model `693b3c0900004859` uses Sar1 in a COPII vesicle uncoating activity on the ER-to-Golgi transport vesicle membrane. The activity is consistent with Sar1 acting as the COPII GTPase; the previously reviewed model issue is on the incoming Sec23 edge, where Sec23 GAP activity should positively regulate Sar1 GTPase activity rather than directly negatively regulate it.
