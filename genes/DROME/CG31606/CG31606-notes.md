# CG31606 / Q8IPG8

Q8IPG8 is the 197-residue CG31606-PB product linked to FBgn0051606 and RefSeq NP_723348.1. The completed Falcon report was inspected and found no focused functional literature; its uncontextualized expression-table lead does not establish a mechanism. Unlike the report’s supplied prompt, the full selected sequence record contains a SignalP-derived signal peptide. The cleaved N-terminus and soluble mature sequence support a reasonable extracellular-location inference.

[Donor provenance assessment](CG31606-bioinformatics/RESULTS.md) identifies P0DTS2 as northern elephant seal ApoA-V and Q55286 as Shigella IpgD. Partial structural matching is not equivalent to orthology or biochemical specificity. Three lipid claims remain UNC; extracellular region is COR from sequence topology, not from the bacterial donor. All three original ND GOA rows are preserved and reviewed. No core molecular function can be specified.

## Sequence and research provenance

The selected frozen UniProt record is retained in [CG31606-uniprot-source.json](CG31606-uniprot-source.json), with the complete original prediction metadata in [CG31606-predictions-source.json](CG31606-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not use ProtNLM2 output or prediction-donor reasoning. The evidence is the UniProt sequence record, the Falcon literature report, and a new reproducible homology analysis ([rereview/RESULTS-rereview.md](CG31606-bioinformatics/rereview/RESULTS-rereview.md), script `rereview/homology_rereview.py`, raw `rereview/homology_rereview.json`).

- **Identity:** Q8IPG8 (197 aa) is the only UniProtKB entry for FBgn0051606, and OMA marks it as the main isoform. Two cDNA fragments from the same locus (G2J5W9, 198 aa; D9PTT6, 142 aa) are identical over their aligned length. The benchmark accession is the canonical full-length product, not a fragment, isoform or alternative gene model.
- **Family:** InterPro has 0 entries and UniProt lists no PANTHER family, so there is no PAINT/IBA node. The only feature is the SignalP signal peptide (1-18).
- **Phylogeny:** The OMA HOG is restricted to the melanogaster group, with 1:1 orthologs in sec/sim/ere/yak/ana/bip/suz. blastp found no Swiss-Prot hit, and every UniProtKB Eukaryota hit is from *Drosophila*. The only paralog-level signal is marginal (E ~ 1e-4) partial similarity to CG42763 and TsetseEP-domain-labelled ana/yak proteins. CG31606 is a lineage-restricted orphan, so no function can be transferred. The "vertebrate homolog: Yes" flag in the Tran 2010 expression table (via Falcon) is not supported.
- **Annotations:** MF ND is ACCEPTED and BP ND is ACCEPTED. CC ND is MODIFIED to GO:0005576 extracellular region, based on the signal peptide, the soluble mature chain and the absence of a KDEL/HDEL motif. This is a sequence inference, not observed localisation. core_functions is left empty on purpose because no activity is known. A BIOLOGY knowledge gap (WHOLLY_DARK) was added.
- **Relative:** No characterised ortholog or PANTHER subfamily exists. The nearest detectable relative is the uncharacterised *D. melanogaster* paralog CG42763 (M9MRG9), which has no review in the repo. It is too weakly related and too poorly characterised to be a useful reference.
- **Modules / PANTHER family review:** None apply (no PANTHER family, no hits in modules/ or gocams/index.tsv).
