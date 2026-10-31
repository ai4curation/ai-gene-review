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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: benchmark accession Q9P7B5 is the canonical, reviewed full-length product of wss1/SPAC521.02 (262 aa, sequence version 2). It is not an isoform, fragment or alternative gene model. It carries the complete WLM domain (8-195), the HExxH...H zinc site (H96/E97/H100/H106) and the C-terminal SIM (235-242) [file:SCHPO/wss1/wss1-uniprot.txt "FT   ACT_SITE        97"].

Evolutionary grounding: Q9P7B5 and budding-yeast WSS1 (P38838) are both in PANTHER PTHR46622:SF1, and they have identical zinc-ligand spacing. S. pombe has exactly one other WLM protein, O94580 (wss2/wss1b, SPCC1442.07c), and it is in a different PANTHER family, PTHR47795 [file:SCHPO/wss1/wss1-bioinformatics/RESULTS-rereview.md]. This resolves the Falcon report's open question. The S. pombe "Wss1b" crystal-structure and biochemistry data concern the paralog Wss2, not Q9P7B5, and they were not used as subfamily evidence for wss1. Falcon's quoted Wss1b residue numbers (H111/E112/H115/H130) do not map onto the current sequence of either S. pombe protein, so I did not use them.

Target-organism evidence found this round, absent from the previous review: wss1 loss sensitizes cells to formaldehyde and leads to replication defects [PMID:32034465 "loss of Wss1 or Wss2, proteases involved in the removal of DNA-protein crosslinks, sensitizes cells to formaldehyde and leads to replication defects"]. Wss1 and Wss2 also contribute to acetaldehyde tolerance [PMID:27687866 "We also show the involvement of Wss1-related metalloproteases, Wss1 and Wss2, in acetaldehyde tolerance."]. These corroborate the ISO DPC-repair transfer. They are phenotypes, so no new process terms were added from them.

Donor annotations on P38838 (QuickGO, 2026-10-21) include SUMO-related terms (GO:0016925, GO:0032183, GO:0061665), nuclear envelope, vacuole and GO:1990414. PomBase and PAINT did not transfer any of these to S. pombe, and I treat that omission as deliberate. No NEW terms are proposed.

Action changes vs previous review:
- GO:0006281 DNA repair (IBA): ACCEPT -> MODIFY to GO:0106300, which the gene already carries.
- GO:0008237 metallopeptidase activity (IBA): ACCEPT -> MODIFY to GO:0004222, which the gene already carries.
- GO:0019985 translesion synthesis (ISO): ACCEPT -> KEEP_AS_NON_CORE. The donor has IDA/IMP evidence (PMID:24998930, full text not cached), so the annotation is not removed. Wss1 proteolyses the adduct upstream of bypass; it does not do the synthesis.
- The other rows (metalloendopeptidase ISO, three nucleus rows, DPC repair ISO) stay ACCEPT. Their reasons were rewritten with the subfamily-level grounding.

Description was rewritten to separate inferred biochemistry from S. pombe genetics and to note the Wss2 paralog.

Relative to review next: S. cerevisiae WSS1 (P38838; SGD:S000001176), the experimentally characterized member of the same PANTHER subfamily (PTHR46622:SF1) and the PAINT/ISO donor. No repo review exists (no genes/yeast/WSS1). The PANTHER family review interpro/panther/PTHR46622/PTHR46622-review.yaml lists only Q9P7B5 as an SF1 representative, and it agrees with the subfamily placement. No modules/ file covers DPC repair.
