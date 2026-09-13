# asr1 notes

Identity: asr1, UniProt O94400; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `asr1-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

LSP: Metal ion binding is a credible consequence of the target zinc-finger architecture. The reviewed sequence record identifies a PHD finger at residues 122-170 through PROSITE-ProRule PRU00146 and an atypical RING region; the actual PHD sequence retains its cysteine/histidine-rich ligand pattern. This is sequence/domain-based inference, not a target zinc-binding experiment or corroboration by ARBA prose. Zinc and zinc-finger annotations already provide the more specific metal identity, and the XML itself records hydration from GO:0008270. The broad metal-ion prediction therefore recovers a known, less precise property rather than a novel function.

[file:SCHPO/asr1/asr1-uniprot.txt "FT   ZN_FING         122..170 FT                   /note="PHD-type" FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00146""]

[file:SCHPO/asr1/asr1-uniprot.txt "     ETCRCVICGR SDHAEVLLLC DGCDDAYHTY CLNMDAVPIE EFYCPNCVLL"]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. In particular, the report does not recover the target localization evidence in PMID:16823372; the reviewed UniProt record explicitly cites it. The current PomBase identifier mapping and orthology annotations resolve identity or inherited functions more specifically than the report's ambiguous-symbol caveats. PHD/RING zinc binding is supported by the target sequence features. Autophagy, phosphoinositide binding and exact histone-mark recognition are not established by those features. The E3 inference is anchored to the curator-selected ortholog paper (PMID:19064926).
