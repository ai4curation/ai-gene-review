# P33154 (PR1, At2g14610) manual literature synthesis

No deep-research API was available; this synthesis was assembled by hand from cached
publications in `publications/` and PubMed searches.

## Identity

- UniProt P33154 (PR1_ARATH), Pathogenesis-related protein 1, 161 aa precursor, locus
  At2g14610 (TAIR symbol PR1). UniProt: "Belongs to the CRISP family" (CAP superfamily).
- UniProt: "SUBCELLULAR LOCATION: Secreted, extracellular space, apoplast."

## Discovery and expression

- PR1 was one of three proteins purified from the apoplast of INA-treated Arabidopsis
  leaves [PMID:1392589 "Three proteins that accumulated to high levels in the apoplast in
  response to INA treatment were purified and characterized"]; expression is induced by
  INA, pathogen infection and salicylic acid [PMID:1392589 "Expression of the genes
  corresponding to these proteins was induced by INA, pathogen infection, and salicylic
  acid"]. PR1 has since become the canonical SA/SAR marker.
- Thiamine induces PR-1 via the SA pathway [PMID:15980201 "Treatment of Arabidopsis
  ecotype Columbia-0 plants with thiamine resulted in the activation of PR-1 but not
  PDF1.2"].
- Drought lowers PR1 transcript [PMID:23144921 "only the expression level of PR1, which is
  associated with the salicylic acid pathway, decreased under drought stress"].
- PR1 is a robust marker of defense priming but not specific to it [PMID:38347062 "PR1,
  owing to its robust expression (Fig. 3A), is also a recommended marker gene for
  detecting priming in this plant"].

## Function: precursor of the phytocytokine CAPE9

- Chen et al. 2023 [PMID:37542077] showed that cleavage after the C-terminal "CNYD" motif
  of PR1 releases the 11-residue peptide AtCAPE9 (PRGNYVNEKPY), detected endogenously by
  LC-MS/MS and increased by SA. Synthetic AtCAPE9 raised SA levels and reduced Pst DC3000
  growth.
- A CRISPR pr1 mutant lost Agrobacterium-induced systemic immunity; local expression of
  native PR1 or local AtCAPE9 restored it, whereas PR1 D150A (cleavage-site) or
  PR1-deltaCAPE9 did not [PMID:37542077 "both CNYD and CAPE domains for proteolytic
  production of AtCAPE9 from PR1 are crucial for eliciting Arabidopsis systemic immunity"].
- The protease is the papain-like cysteine protease XCP1 (At4g35350), which cleaves
  immobilized PR1-eYFP in vitro and co-localizes with PR1 in the apoplast
  [PMID:37542077 "These data suggest that XCP1 directly processes PR1 into AtCAPE9."].
  The cleaving is done by XCP1; PR1 is the pro-cytokine substrate.
- The CAPE receptor is not identified.

## Family-level biochemistry

- CAP/PR-1 proteins bind sterols; tobacco/tomato PR-1 inhibit sterol-auxotrophic
  oomycetes by sequestering sterol [PMID:27747953 "we provide genetic and biochemical
  evidence for the capacity of PR-1 proteins to bind sterols"]. This was not shown for
  Arabidopsis PR1 in the cached abstract (abstract only).
- Review: [PMID:28743380 "Recent reports have emerged demonstrating that PR-1 proteins
  possess sterol-binding activity, harbour an embedded defence signalling peptide, and are
  targeted by plant pathogens during host infection."]

## Localization

- Apoplast (purification from apoplastic fluid, PMID:1392589; PR1-eYFP apoplastic in
  N. benthamiana, PMID:37542077); cell wall/apoplastic-fluid proteomics (PMID:15593128,
  abstract only).
