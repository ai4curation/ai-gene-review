# RHIML/cheY1 evidence review — 2026-11-06

CheY1 is a small cytoplasmic response regulator that serves as a phosphate sink in Sinorhizobium meliloti chemotaxis. It accepts phosphoryl groups from the histidine kinase CheA and hydrolyzes its phosphorylated state, draining phosphate transferred back to CheA by the motor regulator CheY2-P. CheS enhances CheY1 interaction with CheA, and CheT accelerates CheY1-P dephosphorylation. This sink helps terminate the signal controlling flagellar rotary speed; CheY1 is distinct from the principal motor-response regulator CheY2.

Normal fetch seeded this record before review. Original review documents, original non-review row payloads and raw SHA256 hashes are preserved in `.cache/module-audit-logs/chemotaxis-20261106/sinorhizobium-new-members-baseline.json`. All original rows are retained; only their review fields are curated. New rows are explicitly NEW.

## Identity and literature

See [reproducible identity analysis](../../RHIME/cheA/cheA-source-analysis/identity-summary.md), official sequence records and identity-proof.json. CheY1, CheY2 and CheS exactly match RU-operon translations; current CheA is the 1021 ortholog with five sequence conflicts; CheT matches the paper's 1021 alignment reference but lacks a complete independently verified RU assay-insert sequence. Species-level RHIML taxonomy is retained for the three exact RU-linked records. CheS is the historical orf2, not a protein inferred solely from an automatically named STAS-family hit.

PMID9485379 reconstructs CheY2-P → CheA → CheY1 phosphotransfer. PMID18573176 distinguishes CheY2 binding to CheA P2 from CheY1's weak association. PMID15066432 supports CheY2-dependent speed regulation rather than reversal of motor direction. PMID22194454 demonstrates CheA/CheS complex formation and enhanced CheY1 affinity, without establishing direct CheS phosphatase activity or a direct CheS–CheY1 bridge. PMID39081077 adds CheT-catalyzed CheY1-P decay; it does not demonstrate CheY2-P dephosphorylation or a resolved CheR-regulatory reaction. Exact supporting quotations are recorded per review row/core. No binding constants measured in RU are presented as 1021 measurements.

The normal caches are abstract-only. The 2012 PMC and 2024 Wiley full texts were read online for the strain and construct checks documented in the identity analysis. No cached publication was manually edited or replaced. Earlier primary abstracts explicitly support the cited transfer/structural claims; full experimental details remain limited to available text. Original experimental annotations were not rejected on that access limitation.

## Process proposal checks

Every authored chemotaxis proposal names the actual catalytic or functional-complex contribution, checks its nonredundant ontology position and records same-role comparator results in its reason. The GO-CAM index contained none of the five accessions. Comparator annotations are context for convention checks, never evidence for target biochemistry. No positive/negative taxis or growth-process term is added from perturbation alone.

## Research provider and verification

The provider-free command failed because this checkout requires an explicit provider. A subsequent normal `just deep-research RHIML cheY1 --provider falcon` attempted Falcon and failed with HTTP 403 authentication. Logs are preserved at `.cache/module-audit-logs/chemotaxis-20261106/falcon-explicit-RHIML-cheY1.log`. No provider report was fabricated; these are manual evidence notes.
