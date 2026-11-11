# Rnase1 review notes

## Evidence summary
- [UniProtKB:P00684] UniProt describes Rnase1 as an endonuclease that cleaves RNA after pyrimidine nucleotides and records RNase A activity by EC/InterPro/orthology evidence.
- [UniProtKB:P00684] No rat PMID was present in the fetched GOA references, so immune-response process terms are retained only as non-core transferred context.

## Curation decisions
- Core function: pancreatic ribonuclease A (ribonuclease A activity, GO:0004522).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-04

**GOA changes:** none relevant. The refresh added no new rows and retired none (18 rows, all previously reviewed); qualifiers and WITH/FROM were backfilled.

**Actions:** no action changed. All rows were re-audited against the current policy:
- IBA GO:0004540 RNA nuclease activity: ACCEPT. The node-placement argument and residue claims are intact.
- IBA GO:0050830 defense response to Gram-positive bacterium: MARK_AS_OVER_ANNOTATED kept. The challenge rests on node placement and seed composition at PTN008517922 (a host-defence seed set), not on donor count, so it is policy-compliant. Removed a circular UniProt DR-line quote from its support.
- Ten Reactome TAS rows (8 cytosol, 2 lysosomal lumen): KEEP_AS_NON_CORE kept, with the reasons and support rewritten. These are rat chaperone-mediated autophagy events in which Rnase1 is the Hspa8/Lamp2a substrate [Reactome:R-RNO-9615712 "Heat shock cognate 71 kDa protein (Hspa8) acts as the constitutive chaperone that binds Ribonuclease pancreatic beta-type (Rnase1) in the cytosol."]. The cytosolic and luminal pools are a degradation-substrate state; the enzyme itself is secreted [UniProtKB:P00684 "SUBCELLULAR LOCATION: Secreted."].
- ISO GO:0009617 response to bacterium (mouse Rnase1, MGI:97919): KEEP_AS_NON_CORE kept. The reason was corrected to the real donor basis, an IEP from the intestinal transcriptome of Listeria-infected gnotobiotic mice [PMID:23012479 "A whole genome intestinal transcriptomic analysis revealed that each Lactobacillus changes expression of a specific subset of genes during infection"]. Added a propagation_review.
- ISO GO:0004540 (human RNASE1 P07998) and NOT ISO GO:0051607 defense response to virus: traced both to human IDA PMID:9826755 (now cached, abstract-only) [PMID:9826755 "While RNase activity is crucial to antiviral activity, it is clearly not sufficient"]. Both stay ACCEPT.
- Replaced the remaining circular UniProt DR-line quotes on the ACCEPT/KEEP/MODIFY rows with the FUNCTION or SUBCELLULAR LOCATION text.

**Description:** removed the curation commentary ("The review accepts ...") and the "secreted/cytosolic" framing. Rewrote it as standalone biology.

**Open questions:**
- Should cytosol/lysosomal lumen localizations that come from CMA-substrate Reactome events be kept for an endogenously secreted protein, or marked as over-annotation? The original CMA work used exogenously introduced RNase A.

**Stale UniProt quotes (2026-10-10):** replaced 5 `UniProtKB:P00684` supporting_text quotes (the FUNCTION text now wraps at "double-/stranded", so the old quote no longer matched the flat file) with the verbatim first FUNCTION sentence on cleavage of RNA 3' of pyrimidine nucleotides from the current `Rnase1-uniprot.txt`.

Review follow-up 2026-10-17 (PR #4617 reviewer findings): The eight GO:0005829 cytosol and two GO:0043202 lysosomal lumen Reactome TAS rows changed from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED. They describe the exogenous RNase A model substrate of chaperone-mediated autophagy; Rnase1 has a signal peptide and is secreted, so it is never natively cytosolic. The family-level KFERQ/CMA sentence was dropped from the description, which is about this gene product. CC convention for this batch: a location row is ACCEPTed only when that location is part of a core_functions entry (Pnlip extracellular region for luminal digestion, Arsb lysosome for GAG degradation); otherwise location rows are KEEP_AS_NON_CORE. Batch policy for broad parents (applied to all eight genes in PR #4617): an uninformative broad parent of a specific activity or process the gene already carries is MODIFIED to that specific term; experimental rows stay at the curator's breadth unless the cited assay itself identifies the specific substrate.
