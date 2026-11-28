# BIRC3 manual curation notes

## 2026-11-27 PTHR10044 cIAP review

- Reviewed BIRC3/cIAP2 as the human PTHR10044:SF178 member, alongside BIRC2/cIAP1
  and the existing XIAP, BIRC7, and BIRC8 reviews. The external deep-research provider
  used for this lane was unavailable, so the review was curated from UniProt, GOA,
  cached PMIDs, Reactome records, and local family/module reviews; no provider-branded
  deep-research file was fabricated.
- BIRC3 shares the cIAP RING E3 architecture with BIRC2 and is retained for
  ubiquitin-protein ligase activity. Direct BIRC3 evidence includes ubiquitination and
  degradation of BCL10 (PMID:16395405) and participation with BIRC2 in RIPK1-4
  ubiquitination (PMID:21931591).
- TNF, TLR, NOD-like receptor, and RIG-I signaling rows are kept where they describe
  cIAP-mediated receptor signaling or cytokine output. Generic inflammatory-response
  and receptor-signaling parents are narrowed to more informative regulation or TNF
  pathway terms.
- BIRC3 inherits the cIAP-specific PAINT necroptosis row at PTN002559449. That branch is
  separate from XIAP/BIRC8 and BIRC7, and no PAINT loss is present on the BIRC3 lineage.
- The broad PTHR10044 caspase-inhibitor PAINT row at PTN000953271 is marked as
  over-propagated into cIAP2 because PMID:16339151 shows that cIAP1/cIAP2 BIR domains can
  bind caspases but do not directly inhibit them like XIAP.
- The broad PTHR10044 cell-cycle row remains supported for BIRC2 but not for BIRC3; the
  BIRC3 review therefore marks `GO:0051726` over-propagated instead of inferring a
  cIAP2 cell-cycle function by paralogy.
- Most `GO:0005515 protein binding` rows are removed under the project bare-binding
  policy. The review keeps one existing annotation per GOA line, including rows that
  differ only by `WITH/FROM`.
- The Ensembl Compara transfers from rat A0A0G2JTI9 for spermatogenesis, generic
  protein-containing complex, and protein-containing complex binding were treated as
  unsupported rat orthology side annotations outside the human cIAP2 TNF/NF-kappaB,
  apoptosis, and necroptosis functions.
