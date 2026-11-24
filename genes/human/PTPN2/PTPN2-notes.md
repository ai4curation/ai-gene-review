# PTPN2 review notes

Deep-research providers were unavailable in this checkout: the configured client
reported only `claude_code` as available, while the requested `falcon` and
`perplexity` providers were absent. This file records the manual synthesis used
for the PTPN2 review.

## Core function

- PTPN2/TC-PTP is the PTPN1 paralog that is split into two major isoforms:
  TC48/P17706-1 is C-terminally targeted to the ER and ER-Golgi intermediate
  compartment, while TC45/P17706-2 lacks that hydrophobic tail and shuttles
  between nucleus, cytoplasm and the cell periphery.
- UniProt summarizes PTPN2 as a non-receptor tyrosine phosphatase that
  dephosphorylates INSR, EGFR, CSF1R, PDGFR, JAK1, JAK2, JAK3, Src-family
  kinases and STAT1/STAT3/STAT6; the review retains the receptor, JAK/STAT,
  T-cell, CSF1R and insulin signaling annotations as direct regulatory roles.
- Simoncic et al. 2002 identified JAK1 and JAK3 as physiological substrates of
  TCPTP and showed negative regulation of cytokine signaling, with increased
  phospho-STAT5 after IL-2 and increased phospho-STAT1 after IFN-alpha or
  IFN-gamma in TCPTP-deficient lymphocytes or thymocytes.
- ten Hoeve et al. 2002 showed that nuclear TC45 dephosphorylates Stat1 in
  vitro and in vivo, that IFN-induced phospho-Stat1 dephosphorylation is
  defective in TC-PTP-null cells, and that TC45 but not ER-targeted TC48 rescues
  the defect.
- Galic et al. 2003 showed that both TC48 and TC45 substrate-trapping mutants
  form complexes with the insulin receptor after insulin stimulation and that
  physiological TC48 or TC45 expression suppresses enhanced insulin signaling in
  TCPTP-null cells.
- Mattila et al. 2005 showed that the ITGA1 cytoplasmic tail selectively
  interacts with TCPTP and that collagen-bound alpha1 beta1 integrin activates
  TCPTP to reduce EGFR phosphorylation after EGF stimulation.
- Persson et al. 2004 identified TC-PTP as a negative regulator of PDGFRB
  phosphorylation and found that TC-PTP and PTP-1B have distinct site
  selectivity on the PDGF beta receptor.
- Arasaki et al. 2013 found a direct interaction between ER-localized TC48 and
  syntaxin 17 and showed that purified TC48 directly dephosphorylates syntaxin
  17.

## Propagation and non-core rows

- The PTHR46047 root PAINT IBDs for non-membrane-spanning protein tyrosine
  phosphatase activity, protein kinase binding, nucleus, cytoplasm, negative
  JAK-STAT regulation and negative ERK1/ERK2 regulation are appropriate for
  human PTPN2. PTPN2 lacks the PTPN1 branch losses for nucleus and JAK-STAT.
- PTPN2 has direct substrate evidence for multiple cell-surface receptor
  pathways, but broader process rows such as glucose homeostasis, lipid storage,
  T-cell differentiation, B-cell differentiation, erythrocyte differentiation,
  macrophage differentiation, inflammatory response and thymic selection are
  downstream physiological consequences of those substrate dephosphorylation
  events. This review keeps the immune and metabolic terms as non-core when
  UniProt or a substrate pathway supports the direction, but keeps them out of
  the core function summary.
- The Reactome gene-expression event R-HSA-9008894 lists the PTPN family as
  transcription and translation products; it does not itself show that PTPN2
  actively dephosphorylates a substrate in the nucleoplasm. PTPN2 nevertheless
  has independent nuclear TC45 evidence from UniProt and the STAT1 literature.
- The bare `GO:0005515 protein binding` annotations on PTPN2 should be removed:
  interaction evidence supports more specific receptor, protein kinase, syntaxin
  or integrin binding rows where it identifies a substrate or regulator, but
  `protein binding` alone does not describe TC-PTP function.

