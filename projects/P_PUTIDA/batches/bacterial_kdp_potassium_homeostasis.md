---
title: "PSEPK Kdp potassium homeostasis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [kdpA, kdpB, kdpC, kdpD, kdpE, kdpF]
autolink_gene_symbols: false
---

# PSEPK Kdp potassium homeostasis

This batch models the regulated high-affinity Kdp potassium-uptake system,
linking the KdpD/KdpE phosphorelay to the KdpFABC membrane pump.

## Boundary

1. KdpD senses inducing conditions and phosphorylates KdpE.
2. Activated KdpE promotes transcription of the Kdp pump genes.
3. KdpA and KdpB provide ion translocation and ATP coupling, with KdpC and
   KdpF as membrane accessory components.

Constitutive potassium channels, low-affinity uptake systems, respiratory
quinone metabolism, and global osmotic-stress regulation are outside the core.

## Status

- [x] Define a reusable three-role Kdp system module.
- [x] Curate the six KT2440 protein reviews.
- [ ] Complete OpenScientist gene, module, and taxon research (kdpA complete;
  remaining gene/module/taxon jobs active and non-gating).
- [x] Complete independent annotation-reviewer and module audit.
- [x] Validate and render all artifacts.
- [x] Open draft PR [#2532](https://github.com/ai4curation/ai-gene-review/pull/2532).

The independent audit removed unsupported KdpC ATP binding and KdpD cytoplasm
localization, corrected complex-level transporter annotations to
`contributes_to`, and grounded the KdpF stabilizing role with PMID:10608856.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `kdpE` | PP_4157 | Q88FE0 | DNA-binding phosphorelay response regulator |
| `kdpD` | PP_4158 | Q88FD9 | Membrane sensor histidine kinase |
| `kdpC` | PP_4159 | Q88FD8 | Pump accessory membrane subunit |
| `kdpB` | PP_4160 | A0A140FWL1 | P-type ATPase energy-coupling subunit |
| `kdpA` | PP_4161 | Q88FD7 | Potassium-selective translocation subunit |
| `kdpF` | PP_5660 | A0A140FWL2 | Small pump-stabilizing membrane subunit |
