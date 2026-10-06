# VAL1 (Q8W4L5, At2g30470; HSI2) curation notes

## 2026-10-06 initial review

- Deep research: `just deep-research-falcon ARATH VAL1` failed (HTTP 402 from provider); review built from cached publications and UniProt.
- Added references (cached via `just fetch-gene-pmids`): PMID:29660015 (VAL1 B3-DNA crystal structure, full text), PMID:27819666 (cold memory element / VAL1-VAL2 readers, abstract), PMID:36130923 (VAL1 assembly platform, full text).
- Architecture: B3 domain, PHD-like, CW-type zinc finger, EAR motif. Active repressor [PMID:15894743 "These results indicate that HSI2 and related proteins are B3 domain-EAR motif active transcription repressors."].
- Sequence-specific DNA binding: B3 recognises Sph/RY [PMID:29660015 "crystal structure of VAL1 B3 domain (VAL1-B3) bound to a 12 bp oligoduplex containing the canonical Sph/RY DNA sequence"]. Added NEW GO:0043565 (IDA).
- Vernalization: VAL1 binds the FLC nucleation region and triggers PHD-PRC2 nucleation [PMID:27471304 "VAL1 localizes to the nucleation region in vivo, promoting histone deacetylation and FLC transcriptional silencing"]; [PMID:27819666 "The sequence-specific readers recognize both the cis element (termed the cold memory element) and a repressive mark"]. Added NEW GO:0010048 involved_in: VAL1 performs a step (targeting/recruitment), not merely necessity.
- PRC2 recruitment genome-wide [PMID:33270882 "We further show that VAL1 and VAL2 physically interact with SWN and CLF in vivo."]. Bare protein-binding rows to CLF, SWN, PYL9 removed per policy (no PRC2-binding MF term exists); SNL1 row -> transcription corepressor binding.
- Mitochondrion HDA (large proteome) -> MARK_AS_OVER_ANNOTATED (nuclear TF, likely co-purification).
- Core MF GO:0043565 matches the module `vernalization_flc_silencing` annoton for VAL1.
