# tp53bp2b notes

## Setup and provenance

- Fetched with `just fetch-gene` on F1QWN1 (TrEMBL, "apoptosis-stimulating of p53 protein 2b
  isoform X1", 1063 aa); 14 GOA rows (IBA/IEA plus 2 IMP from PMID:24362258, 1 IMP and 1 IDA from
  PMID:25139857). ZFIN ZDB-GENE-050208-453, Ensembl ENSDARG00000054858, chromosome 22.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` was generated. Literature searched by hand via Europe PMC
  (same queries as tp53bp2a; `"tp53bp2b"` returns only one unrelated hit).
- Part of DANRE_DUPLICATION batch 4 (random sample, seed 20260928); paralog tp53bp2a. Ensembl
  Compara dates the duplication to Osteoglossocephalai.
- The shared analysis lives in `genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/`.

## Zebrafish literature

- Growth/Akt study of both copies (abstract only)
  [PMID:24362258 "Here, we show that zebrafish Aspp2a and Aspp2b negatively regulate embryonic growth without affecting developmental rate."]
  [PMID:24362258 "Zebrafish Aspp2a and Aspp2b physically bound with Irs-1, and the growth inhibitory effects of ASPP2/Aspp2 depend on the presence of their ankyrin repeats and SH3 domains."]
- Foxj1-target morpholino screen (full text cached, but tp53bp2b's own data are only in
  supplementary Table S3, not cached). The screen picked 50 Foxj1-induced genes at random, tested
  GFP-fusion localization and morpholino phenotypes; KV cilia motility was measured for ten genes
  [PMID:25139857 "We selected the ten morpholinos that exhibited the most severe left-right asymmetry abnormalities (excluding the genes that gave ciliary shortening phenotypes) for examining ciliary motility in KV."].
  GOA's IMP "cilium movement" and IDA "cytoplasm" for tp53bp2b come from this screen. I cannot
  see the gene-specific numbers, so the cilium row is UNDECIDED.

## Own analysis

See [tp53bp2a-bioinformatics/RESULTS.md](../tp53bp2a/tp53bp2a-bioinformatics/RESULTS.md).
Ankyrin repeats 90.7-97.1% identical to human; SH3 intact; relative rate equal to tp53bp2a.
tp53bp2b is the lower-expressed copy during development (maternally provided like tp53bp2a, then 2-9 TPM from
gastrula to pharyngula, 11-15 TPM in larvae), broadly expressed in adults with its highest Bgee
score in retina.

## Curation decisions (summary)

- Same decisions as tp53bp2a for the shared IBA/IEA and PMID:24362258 rows.
- cilium movement (IMP, morpholino screen): UNDECIDED (gene-specific data not visible; no
  ciliary role known for ASPP2 elsewhere).
- cytoplasm (IDA from GFP fusion): ACCEPT.
- NEW: insulin receptor substrate binding (IPI, PMID:24362258).
