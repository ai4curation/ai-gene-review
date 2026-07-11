# PANTHER Family Review: PTHR24096

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24096 |
| **Family Name** | ATP-dependent AMP-binding enzyme |
| **InterPro Entry** | none (not integrated) |
| **Total Proteins** | 38,465 |
| **Taxonomic Breadth** | 14,325 taxa |
| **Subfamilies** | 71 |
| **Representative Structure** | 3ni2 (4-coumarate:CoA ligase from *Populus tomentosa*) |
| **Module role** | Provides **4CL (4-coumarate:CoA ligase)**, which activates hydroxycinnamates to their CoA thioesters for monolignol biosynthesis. Exemplar: `UniProtKB:Q42524 (4CL1_ARATH, At4CL1)`, PANTHER `PTHR24096:SF352`; function `GO:0016207 4-coumarate-CoA ligase activity`. |

## Executive Summary

PTHR24096 is the **ANL superfamily of adenylate-forming (AMP-binding / acyl-activating) enzymes** — the acyl-CoA synthetase / firefly-luciferase / non-ribosomal-peptide-synthetase adenylation-domain clan. Members use a conserved two-step mechanism: adenylation of a carboxylate substrate by ATP (releasing PPi) followed by thioester transfer to CoA (or another thiol acceptor). Substrate specificity is highly variable across the superfamily, which includes long-chain and medium-chain fatty acyl-CoA synthetases, acetyl-CoA synthetases, and many secondary-metabolite activating enzymes.

Within this large superfamily, the plant **4-coumarate:CoA ligase (4CL, EC 6.2.1.12)** converts *p*-coumarate (and related hydroxycinnamates: caffeate, ferulate, 5-hydroxyferulate, sinapate) into the corresponding CoA thioesters. 4CL is the third core step of the general phenylpropanoid pathway (after PAL and C4H) and supplies the hydroxycinnamoyl-CoA substrates that feed the monolignol-specific branch (CCR, HCT/C3'H, CCoAOMT, etc.). 4CL is thus one specialized acyl-activating subfamily among ~71 in a functionally sprawling superfamily.

## Subfamily Analysis

The exemplar At4CL1 (Q42524) is in `PTHR24096:SF352` (4-COUMARATE--COA LIGASE 1); other reviewed 4CL orthologs map to `:SF402` and related 4CL-labelled subfamilies. The reviewed entries span 24 distinct subfamilies out of the family's 71, and the parent name — **ATP-dependent AMP-binding enzyme** — reflects the ancestral adenylation/acyl-CoA-synthetase activity, *not* 4CL specifically. The bulk of members are fatty-acyl-CoA synthetases and other acyl-activating enzymes; 4CL is a plant hydroxycinnamate-specific offshoot.

## IBA / PAINT Assessment

Local PAINT (`PTHR24096-paint.tsv`) shows the expected superfamily heterogeneity:

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN000644304 | `GO:0006633 fatty acid biosynthetic process` | P | Fatty-acid-metabolism clade. |
| PTN000645769 | `GO:0005777 peroxisome` | C | Peroxisomal acyl-activating clade. |
| PTN001186584 | `GO:0016405 CoA-ligase activity` | F | Broad acyl-CoA ligase node (large mixed-taxon seed set). |
| PTN001186783 | `GO:0004467 long-chain fatty acid-CoA ligase activity`; `GO:0046949 fatty-acyl-CoA biosynthetic process` | F/P | LACS clade. |
| PTN001534794 | `GO:0005777 peroxisome`; `GO:0006744 ubiquinone biosynthetic process` | C/P | 4-coumarate-CoA-ligase-like / ubiquinone clade. |
| PTN001534798 | `GO:0016207 4-coumarate-CoA ligase activity` | F | **Plant 4CL clade** (taxon:3398; seeds AT1G65060, Q42982). |
| PTN004669572 | `GO:0016207 4-coumarate-CoA ligase activity` | F | Additional 4CL-like node (Arabidopsis AT3G21230/40, AT1G51680). |

The specific 4CL activity (`GO:0016207`) is propagated only at the dedicated plant 4CL nodes (PTN001534798, PTN004669572), while the rest of the superfamily carries fatty-acyl-CoA-synthetase and generic CoA-ligase terms. This is correct, conservative propagation.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0016207 4-coumarate-CoA ligase activity` at the **parent level is clearly unsafe**. PTHR24096 is the ANL/AMP-binding acyl-CoA-synthetase superfamily (71 subfamilies, ~14k taxa, bacteria to plants to animals); most members are fatty-acyl-CoA synthetases, and a parent-level 4CL mapping would massively over-annotate them. At most the superfamily supports the generic `GO:0016405 CoA-ligase activity`. The specific 4CL function must be restricted to the **4CL subfamilies / PAINT nodes (PTHR24096:SF352 and the PTN001534798 / PTN004669572 clades)**, as the current PAINT structure does.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
