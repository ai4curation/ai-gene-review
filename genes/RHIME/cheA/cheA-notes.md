# RHIME/cheA evidence review — 2026-11-06

CheA is the central soluble histidine kinase of the Sinorhizobium meliloti chemotaxis pathway. It couples chemoreceptor signaling to ATP-dependent autophosphorylation and phosphotransfer to response regulators. In the S. meliloti phosphate-sink circuit, CheA also accepts phosphate back from the motor regulator CheY2-P and transfers it to CheY1 for signal termination. CheS associates with CheA and enhances CheY1 recruitment. The 1021 protein conserves this kinase architecture; its sequence differs at five positions from the deposited RU11/001 protein used to establish the detailed coupling mechanism.

Normal fetch seeded this record before review. Original review documents, original non-review row payloads and raw SHA256 hashes are preserved in `.cache/module-audit-logs/chemotaxis-20261106/sinorhizobium-new-members-baseline.json`. All original rows are retained; only their review fields are curated. New rows are explicitly NEW.

## Identity and literature

See [reproducible identity analysis](../../RHIME/cheA/cheA-source-analysis/identity-summary.md), official sequence records and identity-proof.json. CheY1, CheY2 and CheS exactly match RU-operon translations; current CheA is the 1021 ortholog with five sequence conflicts; CheT matches the paper's 1021 alignment reference but lacks a complete independently verified RU assay-insert sequence. Species-level RHIML taxonomy is retained for the three exact RU-linked records. CheS is the historical orf2, not a protein inferred solely from an automatically named STAS-family hit.

PMID9485379 reconstructs CheY2-P → CheA → CheY1 phosphotransfer. PMID18573176 distinguishes CheY2 binding to CheA P2 from CheY1's weak association. PMID15066432 supports CheY2-dependent speed regulation rather than reversal of motor direction. PMID22194454 demonstrates CheA/CheS complex formation and enhanced CheY1 affinity, without establishing direct CheS phosphatase activity or a direct CheS–CheY1 bridge. PMID39081077 adds CheT-catalyzed CheY1-P decay; it does not demonstrate CheY2-P dephosphorylation or a resolved CheR-regulatory reaction. Exact supporting quotations are recorded per review row/core. No binding constants measured in RU are presented as 1021 measurements.

The normal caches are abstract-only. The 2012 PMC and 2024 Wiley full texts were read online for the strain and construct checks documented in the identity analysis. No cached publication was manually edited or replaced. Earlier primary abstracts explicitly support the cited transfer/structural claims; full experimental details remain limited to available text. Original experimental annotations were not rejected on that access limitation.

## Process proposal checks

Every authored chemotaxis proposal names the actual catalytic or functional-complex contribution, checks its nonredundant ontology position and records same-role comparator results in its reason. The GO-CAM index contained none of the five accessions. Comparator annotations are context for convention checks, never evidence for target biochemistry. No positive/negative taxis or growth-process term is added from perturbation alone.

## Research provider and verification

The provider-free command failed because this checkout requires an explicit provider. A subsequent normal `just deep-research RHIME cheA --provider falcon` attempted Falcon and failed with HTTP 403 authentication. Logs are preserved at `.cache/module-audit-logs/chemotaxis-20261106/falcon-explicit-RHIME-cheA.log`. No provider report was fabricated; these are manual evidence notes.


## 2026-11-06 — PR #6100 review follow-up

QuickGO checked 2026-11-06 confirms GO:0000155 is_a GO:0140299 molecular sensor activity, as well as GO:0004673. The sensor parent describes ligand binding with an activity change in response to intracellular ligand level. Receptor-controlled histidine phosphorylation is established, but the experiments do not establish that sensor activity on CheA itself: chemoreceptors detect the stimulus and control CheA through the coupling complex. The child definition alone had obscured this inherited requirement. Retain the demonstrated kinase chemistry as GO:0004673 and the receptor-controlled phosphorelay in the process/core description; ask GO to resolve the term-scope mismatch rather than asserting an experimentally disproven kinase or a wrong PAINT node.

PMID:9485379 establishes the kinase and forward/reverse phosphotransfer in the RU lineage. The current 1021 record differs at five positions from deposited RU11/001 CheA; the qualitative role is inferred from the ortholog and conserved architecture, without transferring quantitative RU measurements.

This supersedes the earlier direct-binding-only rationale. Exact QuickGO endpoints and is_a results are preserved in modules/bacterial_chemotaxis_signal_transduction-source-analysis/chea-ontology-check.yaml. Original annotation IDs, evidence codes and source entities remain unchanged.
