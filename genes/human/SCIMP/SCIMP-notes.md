# SCIMP (human, Q6UWF3) review notes

## Deep research

`just deep-research-falcon human SCIMP --fallback perplexity-lite` failed on 2026-10-16:
falcon (Edison API) returned "Failed to authenticate" and perplexity is not configured in
this environment. No `-deep-research-*.md` file was produced. Literature was collected by a
manual PubMed search (`SCIMP[Title/Abstract]`, 33 hits) and the primary papers below were
cached with `just fetch-gene-pmids`.

## Biology

- Discovery: palmitoylated transmembrane adaptor in B cells and other APCs; localizes to the
  immunological synapse through tetraspanin-enriched microdomains; constitutively bound to Lyn;
  after MHC-II stimulation phosphorylated tyrosines bind SLP65 (positive) and Csk (negative
  feedback) [PMID:21930792 "When phosphorylated, SCIMP binds to the SLP65 adaptor protein and also
  to the inhibitory kinase Csk."]. Cached abstract only; finer localization (uropod, leading edge)
  and interaction-domain detail are taken from the UniProt curated text that cites this paper.
- Mouse knockout: no B cell defect in primary cells; sustained late Dectin-1 signalling and
  cytokine production in BMDCs [PMID:27288407].
- Non-TIR TLR adaptor: binds TLR4-TIR after LPS, required for TLR4 tyrosine phosphorylation,
  selectively drives IL-6 and IL-12p40 but not TNF [PMID:28098138 "SCIMP is a non-TIR-containing
  adaptor, binding directly to the TLR4-TIR domain in response to lipopolysaccharide."].
- Scaffold for Erk1/2 at ruffles/macropinosomes [PMID:34496234 "SCIMP is a direct scaffold for
  Erk1/2 in TLR pathways"] and for Syk via pY96/pY120 [PMID:35337798 "Here, we show that SCIMP
  recruits Syk in response to lipopolysaccharide-mediated TLR4 activation."]; the latter includes a
  human THP-1 experiment. SCIMP/SYK mediate TLR4 Y672 (human Y674) phosphorylation [PMID:37058370].
- A downstream-start translational variant (TV1) in mouse localizes to the Golgi and enhances CpG
  (TLR9) responses [PMID:35201640]; not annotated (overexpression, isoform-specific).
- Exosome-secreted SCIMP / N-terminal peptide as an FPR1/2 neutrophil chemoattractant in acute lung
  injury [PMID:38263143]; unusual for a TRAP, raised as a question rather than annotated.

## Annotation decisions

- Core: signaling adaptor activity (MODIFY from molecular adaptor activity), TLR4 signalling,
  LPS-mediated signalling, IL-6 and IL-12 production, ERK1/2 cascade; plasma membrane,
  tetraspanin-enriched microdomain, immunological synapse.
- Non-core: TLR3/TLR7/TLR1:TLR2 (supplementary siRNA data), Dectin-1/fungal response, p38/JNK,
  ruffle, filopodium, phagocytic vesicle, uropod, leading edge, receptor complex.
- protein binding: MODIFY to SH3 domain binding (LYN) or SH2 domain binding (CSK, GRB2, BLNK);
  REMOVE for tetraspanins, CCDC81 and MEOX2 (uninformative; interaction not disputed).
- membrane: MODIFY to plasma membrane.
