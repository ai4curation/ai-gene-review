# wss1 notes

Identity: wss1, UniProt Q9P7B5; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `wss1-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

UNC: The reviewed target record places Wss1 in the nucleus and identifies a soluble WLM metalloprotease domain; it does not establish membrane residence. The original XML hydrates the membrane claim from KW-0539, which is the UniProt keyword Nucleus, not a membrane-specific observation. Nuclear residence alone does not entail association with the nuclear envelope, and the family DNA-protein-crosslink repair mechanism does not require a membrane. Nevertheless, lack of a transmembrane helix would not exclude peripheral membrane association, so the broad claim cannot be conclusively refuted solely from these data. Direct membrane fractionation, colocalization or an established membrane-associated complex is missing.

[file:SCHPO/wss1/wss1-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:16823372}."]

[file:SCHPO/wss1/wss1-keyword-KW-0539.json ""name": "Nucleus",     "id": "KW-0539""]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. In particular, the report does not recover the target localization evidence in PMID:16823372; the reviewed UniProt record explicitly cites it. The current PomBase identifier mapping and orthology annotations resolve identity or inherited functions more specifically than the report's ambiguous-symbol caveats. The structural Wss1b report cannot be treated as a Q9P7B5 experiment without resolving its paralog mapping. WLM family transfer remains justified by the diagnostic domain and the curated orthology assertion.
