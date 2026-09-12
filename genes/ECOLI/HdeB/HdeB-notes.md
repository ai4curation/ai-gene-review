# HdeB annotation re-review — 2026-08-29

## Scope and physical-row reconciliation

- Reviewed all 8 current GOA signatures exactly once, qualifier-aware: 2 `enables`, 2 `located_in`, 2 `involved_in`, and 2 `acts_upstream_of_or_within`.
- Evidence distribution is 4 IEA, 3 IDA, and 1 IMP. There are no IBA annotations and no PTN/WITH-FROM provenance to audit for this gene.
- The two GO:0051082 rows are physical current GOA records (InterPro IEA and EcoCyc IDA); their machine-sourced term IDs are preserved even though live GO now marks the term obsolete.

## Holdase versus carrier semantics

HdeB is an acid-activated, ATP-independent in-situ holdase. The direct study reports that “HdeB is more efficient than HdeA in preventing periplasmic-protein aggregation” at pH 3 and concludes that HdeA and HdeB “prevent periplasmic-protein aggregation at acidic pH.” [PMID:17085547]

Later work refined the activation range and mechanism: “the chaperone function of HdeB is optimal at pH 4, at which HdeB is still fully dimeric and largely folded,” and “Once activated, HdeB binds various unfolding client proteins, prevents their aggregation, and supports their refolding upon subsequent neutralization.” [PMID:25391835]

No cached experiment identifies a defined acceptor molecule, delivery destination, or escort step. Consequently, GO:0140309 does not satisfy its carrier semantics for HdeB. Both GO:0051082 rows are `MODIFY`, with GO:0051082 retained explicitly as an interim descriptor until the project-defined general “holdase chaperone activity” NTR is created. [file:projects/UNFOLDED_PROTEIN_BINDING.md]

GO:0044183 was not substituted: the evidence shows aggregation prevention followed by client refolding upon neutralization, not autonomous catalysis of folding by HdeB. The direct core biology is therefore represented by the interim GO:0051082 slot plus the proposed holdase NTR, in periplasmic acid-stress context.

## Evidence limitations and mechanistic refinement

- PMID:17085547 and PMID:25391835 are abstract-only in the repository cache. Their abstracts directly support the experimental GO rows and core holdase conclusion, so no experimental annotation was overruled from incomplete evidence.
- PMID:26593705 is cached in full text and supports a folded, dynamic-dimer mechanism at mildly acidic pH: “HdeB activation is coupled to its intrinsic dynamics instead of structural changes, and therefore its functional mechanism is apparently different from HdeA.”
- UniProt independently records that HdeB is required for optimal acid-stress protection, prevents aggregation of multiple periplasmic proteins, contains a signal peptide, and localizes to the periplasm. [file:ECOLI/HdeB/HdeB-uniprot.txt]

## PR #2736 review follow-up

- Corrected both GO:0051082 `MODIFY` rows so `proposed_replacement_terms` now uses the machine-readable CRYAA/project convention `id: NTR`, `label: holdase chaperone activity (NTR needed; GO:0140309 does not fit -- carrier-specific)`. The existing physical GO:0051082 rows remain present as interim annotations; they no longer self-replace with their own obsolete ID.
- Reordered the core-function description to lead with HdeB biology and close with the interim ontology caveat.
- Restored the UniProt-supported regulation context to the standalone description: induction by EvgS/EvgA and negative regulation by H-NS and TorS/TorR. [file:ECOLI/HdeB/HdeB-uniprot.txt]
- Added a literature-supported `NEW` GO:0050821 protein stabilization BP. Direct suppression of periplasmic-protein aggregation fits stabilization and does not imply that HdeB actively catalyzes client refolding. [PMID:17085547 "Thus, we can conclude that Escherichia coli possesses two acid stress chaperones that prevent periplasmic-protein aggregation at acidic pH."]
- Clarified the BP specificity chain (GO:0009268 response to pH → GO:0010447 response to acidic pH → GO:1990451 cellular stress response to acidic pH) and recorded that the two experimental GO:0010447 rows retain GOA's broader `acts_upstream_of_or_within` qualifier while GO:1990451 uses `involved_in`.
