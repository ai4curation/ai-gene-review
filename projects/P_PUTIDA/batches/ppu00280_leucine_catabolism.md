---
title: "PSEPK distal L-leucine catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ivd, mccA, mccB, liuC, mvaB, PP_3394]
autolink_gene_symbols: false
---

# PSEPK distal L-leucine catabolism

This batch tests the distal, leucine-specific route from
3-methylbutanoyl-CoA to acetoacetate and acetyl-CoA. The adjacent TSV retains
all 35 genes on KEGG `ppu00280`; the curated module excludes upstream
branched-chain aminotransferase and 2-oxoacid-dehydrogenase reactions shared
with valine and isoleucine.

## Required Workflow

- [x] Fetch the selected PSEPK records from UniProt and GOA.
- [x] Attempt OpenScientist deep research for the selected genes; LiuC and
  MvaB reports completed, Ivd and MccA exhausted corrected 7,200-second
  requests, and MccB plus PP_3394 exhausted their earlier 3,600-second
  provider requests without reports.
- [x] Curate the six selected gene reviews.
- [x] Revise and semantically validate the species-neutral module.
- [x] Attempt generic module-level OpenScientist research; the corrected
  request exhausted the 7,200-second provider timeout without a report.
- [x] Attempt module + pathway + PSEPK OpenScientist research; the corrected
  request exhausted the 7,200-second provider timeout without a report.
- [x] Validate and render all changed reviews, the module, and project pages.
- [x] Open one non-draft PR for this module:
  [#2237](https://github.com/ai4curation/ai-gene-review/pull/2237).
- [x] Resolve review and CI feedback.

## Selected Genes

| Position | Gene | Locus | UniProt | Role | Module disposition |
|---|---|---|---|---|---|
| 1 | `ivd` | PP_4064 | Q88FM5 | 3-methylbutanoyl-CoA dehydrogenase | exemplar |
| 2a | `mccA` | PP_4067 | Q88FM2 | MCC biotin-carboxylase/carrier subunit | exemplar |
| 2b | `mccB` | PP_4065 | Q88FM4 | MCC carboxyltransferase subunit | exemplar |
| 3 | `liuC` | PP_4066 | Q88FM3 | bacterial methylglutaconyl-CoA hydratase | exemplar |
| 4 | `mvaB` | PP_3540 | Q88H25 | HMG-CoA lyase | exemplar |
| candidate | `PP_3394` | PP_3394 | Q88HG4 | electronically predicted HMG-CoA lyase | not asserted |

## Boundary And Curation Notes

- The reusable module has no global mitochondrial context. Human exemplars act
  in the mitochondrial matrix, whereas the PSEPK instance is bacterial.
- Ivd-bound FAD is a cofactor; oxidized and reduced electron-transfer
  flavoprotein are the electron-transfer participants.
- The MCC position is a two-subunit complex with distinct alpha
  biotin-carboxylase/carrier and beta carboxyltransferase roles.
- Human AUH and bacterial LiuC occupy the same reaction position but use
  distinct lineage-associated implementations. AUH uses its exact PANTHER
  subfamily; LiuC is selected by a crotonase-family record plus the required
  methylglutaconyl-CoA hydratase function because its available PANTHER
  assignment is not LiuC-specific.
- The Ivd and MCC selectors use exact PANTHER subfamilies rather than broad
  acyl-CoA dehydrogenase or biotin-dependent carboxylase parent families.
- The electronic isoprenoid-catabolism annotation on `liuC` was removed:
  PMID:16820476 reports that P. putida utilizes leucine and isovalerate but
  not acyclic terpenes.
- `PP_3394` has both HMGL-like and
  alpha-isopropylmalate/homocitrate-synthase signatures and lacks the HMG-CoA
  lyase PROSITE signature found in MvaB. Its exact function and pathway
  annotations remain undecided rather than being used to fill the terminal
  step.
- The MvaB OpenScientist report gives 78.6% identity for MvaB versus
  characterized P. aeruginosa LiuE and 41.8% for MvaB versus PP_3394. These
  provider calculations were not independently reproduced, and the report does
  not provide a direct PP_3394-versus-LiuE identity; they support MvaB as the
  stronger terminal-step exemplar without resolving PP_3394.
- MvaB/PP_3540 is separated from the upstream ivd-mccB-liuC-mccA cluster. The
  pathway assignment therefore rests on reaction continuity, the close
  characterized LiuE ortholog, and the P. putida leucine/isovalerate phenotype,
  not on local operon membership.
- The generic and species-aware OpenScientist requests were each allowed the
  full configured 7,200 seconds with three iterations. Neither returned a
  report, so the module retains only the direct Reactome, exact-record, gene
  review, and primary-literature evidence that can be inspected locally.
- The completed LiuC and MvaB reports corroborated their bacterial hydratase
  and HMG-CoA-lyase roles. They supplied no evidence that overrides the
  sequence conflict for `PP_3394`; it remains an unresolved candidate outside
  the module.
