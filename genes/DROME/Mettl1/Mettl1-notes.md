# Mettl1 (O77263; CG4045) review notes

## Identity
- TrmB-family class I SAM methyltransferase, ortholog of human METTL1 / yeast Trm8.
  UniProt: [file:DROME/Mettl1/Mettl1-uniprot.txt "Catalytic component of Mettl1-wuho methyltransferase complex"].

## Literature
- Kaneko et al. 2024 (Nat Commun) is the key fly study:
  - [PMID:39317727 "Knockout of Mettl1 (Mettl1-KO) causes no major effect on the development of non-gonadal tissues, but abolishes the production of elongated spermatids and mature sperm, which is fully rescued by expression of a Mettl1-transgene, but not a catalytic-dead Mettl1 transgene."]
  - [PMID:39317727 "Mettl1-KO results in a loss of m7G modification on a subset of tRNAs and decreased tRNA abundance."]
  - [PMID:39317727 "Mettl1 associates with Wh in vivo and in vitro and catalyzes m7G-modification on a subset of tRNAs in a Wh-dependent mechanism"]
  - [PMID:39317727 "Drosophila Mettl1 required Wh for tRNA methylation"]
  - [PMID:39317727 "MBP-Mettl1 but not MBP alone associated with GST-Wh"]
  - Ribosome profiling showed stalling at codons decoded by the affected tRNAs, and reduced
    translation of spermatid-elongation genes.
- DPIM2 AP-MS (PMID:38944040) also recovered the Mettl1-Wuho interaction (abstract only cached).

## Decisions
- Accept tRNA (guanine(46)-N7)-methyltransferase activity (IMP + IBA + ISS + IEA), tRNA
  (m7G46) methyltransferase complex (IPI), tRNA methylation, RNA/tRNA guanine-N7 methylation.
- Protein binding (IPI to Wuho): kept as non-core; captured better by the complex term.
- Nucleus: kept as non-core (orthology-only; no fly localization data).
- Spermatogenesis phenotype not proposed as NEW: the defect is a downstream consequence of
  reduced tRNA abundance and translation in testis.

## Deep research (falcon)
- Summarizes Kaneko et al. 2024; catalytic-site mutant: [file:DROME/Mettl1/Mettl1-deep-research-falcon.md "Substituting L157 and D160 in Mettl1 abolished the assayed activity."]
