# MITF (human, O75030) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human MITF is reviewed as the experimentally characterised reference for the
donkey (EQUAS) MITF ortholog A0A9L0JBN5. No ProtNLM2 output was consulted.

### Process
- `just fetch-gene human MITF` created the uniprot, goa (130 rows) and stub files;
  `just fetch-gene-pmids` cached all 20 GOA PMIDs (12 abstract-only).
- `just deep-research-falcon human MITF --fallback perplexity-lite` FAILED: falcon
  "Exception: Failed to authenticate"; perplexity-lite fallback HTTP 401
  (insufficient_quota). No deep-research file exists; the review is built from the
  cached publications, the UniProt record, Reactome cache entries and the PANTHER/PAINT
  file `interpro/panther/PTHR45776/PTHR45776-paint.tsv`.

### Evolutionary grounding
- UniProt: PANTHER PTHR45776:SF4 (MICROPHTHALMIA-ASSOCIATED TRANSCRIPTION FACTOR);
  "Belongs to the MiT/TFE family". Domains: bHLH (PF00010), MiT/TFE N-terminal
  (PF15951), MiT/TFE C-terminal (PF11851).
- PAINT IBDs at PTN005248237 (taxon:33154, Opisthokonta root of the family) seeded by,
  among others, UniProtKB:O75030 itself: GO:0000978, GO:0000981, GO:0005634, GO:0006357.
  MITF appearing among the seeds is expected (its own IDA rows ground the node).
- GO:0030318 melanocyte differentiation IBD at PTN000000820 (taxon:32523, Tetrapoda),
  seeded by mouse Mitf (MGI:104554).
- GO:0007040 lysosome organization and GO:0010508 positive regulation of autophagy are
  IBD at PTN002908969 (Euteleostomi) seeded by TFEB/Tfe3; MITF does not receive them.
  Treated as a deliberate PAINT decision: lysosome/autophagy master-regulator functions
  are not transferred to MITF here, even though MITF-A is regulated at the lysosome by
  Rag/mTORC1 (PMID:23401004, PMID:36608670). Regulation *at* the lysosome is not the same
  claim as regulating lysosome biogenesis.

### Experimentally established in human (key evidence)
- Sequence-specific DNA binding at M-box/E-box: EMSA of WT human MITF
  [PMID:27889061 "strong M-box (TCATGTG) and E-box (CACGTG) binding"]; tyrosinase family
  M box bound in vitro [PMID:8995290].
- Transcriptional activation of Pol II target promoters (TYR, TYRP1, MC1R, PRKCB, BEST1,
  c-fos): reporter assays [PMID:8995290, PMID:9647758, PMID:12204775, PMID:16411896,
  PMID:20530484], ChIP at FOS [PMID:14737107].
- Heterodimerization with TFE3/TFEB [PMID:15507434 "MITF and its related family members
  TFE3 and TFEB heterodimerize with each other"]; COMMAD mutants dimerize with MiT
  partners and act dominant-negative [PMID:27889061].
- Localization: predominantly nuclear [PMID:27889061]; cytoplasmic retention by
  phospho-dependent 14-3-3 binding [PMID:16822840]; Rag-dependent recruitment to the
  lysosomal surface [PMID:23401004, PMID:36608670].
- Repression of ZEB1 (Reactome R-HSA-9926484, CUT&RUN/ChIP-seq) — non-core.

### Isoforms
- MITF-M (melanocyte; O75030-9) vs MITF-A (widely expressed; O75030-1) and others.
  MITF-A failed to activate PKC-beta/TYR reporters in one study [PMID:16411896] while
  activating TYR/TYRP1 in another [PMID:9647758]; isoform-specific target selectivity.
  Lysosome recruitment is a property of N-terminally extended isoforms (MITF-A); MITF-M
  lacks the Rag-binding N-terminus (PMID:23401004 discusses "specific MITF isoforms").

### Transfer guidance for the donkey ortholog
- Safe to transfer (same subfamily SF4, root IBDs): GO:0000978, GO:0000981/GO:0001228,
  GO:0005634, GO:0006357, GO:0030318 (tetrapod node).
- Not to transfer: lysosome organization / autophagy regulation (TFEB/TFE3 node only).
