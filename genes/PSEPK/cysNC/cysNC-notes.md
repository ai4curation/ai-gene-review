# cysNC curation notes

## First-pass synthesis

- Q88NA8 is the CysN-family GTPase subunit that partners with CysD for APS
  formation [UniProtKB:Q88NA8, "With CysD forms the ATP sulfurylase (ATPS) that
  catalyzes the adenylation of sulfate"].
- The conserved mechanism couples CysN GTP turnover to sulfate adenylation
  [PMID:16387658, "conserved switch motifs in the G domain of CysN allosterically
  mediate interactions between the nucleotide binding sites"].
- The imported `enables GO:0004781` relation is too strong for the regulatory
  GTPase subunit. CysNC contributes to the CysD-catalyzed ATP sulfurylase
  activity; its own catalytic activity is GTP hydrolysis.
- Q88NA8 contains an APS-kinase-like C-terminal domain, but the exact record
  does not assign an APS kinase reaction. The first pass therefore does not add
  a PAPS-producing pathway step.

## Open issue

Test whether the C-terminal domain is active or is a catalytically eroded fusion
remnant. This distinction determines whether KT2440 can generate PAPS through
CysNC even though its CysH is assigned as an APS reductase.


## Comparative sulfate-assimilation audit — 2026-10-26

Re-reviewed all six rows. Intrinsic GTPase activity is separated from contribution to the CysD/CysNC sulfurylase reaction. The imported qualifier is not changed or rejected merely for being enables; the core explicitly records contributes_to_molecular_function. GTP binding is integral to the core regulatory cycle. Broad sulfur metabolism is refined to sulfate assimilation. A fused APS-kinase-like domain remains insufficient evidence for actual kinase catalysis or use of a PAPS-reduction route.

Research provenance: parent already attempted Falcon (403) and Perplexity-lite (401 quota) for this batch; no generated report was fabricated. Existing PSEPK OpenScientist reports were used only as discovery. Source caches were fetched normally and never hand-edited. All original annotation payloads were preserved, with a retirement marker only for the existing CysI donor-specific NEW proposal.
