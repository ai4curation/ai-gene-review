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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 8 GOA rows, the description and core functions. ProtNLM2 files were not consulted.

Identity: O94400 is the reviewed, full-length (571 aa) canonical UniProt product of SPCC126.07c (asr1); not a fragment, isoform or alternative gene model. RING-type 1 (18-79, atypical), PHD (122-170) and the disordered C-terminal region are all present. [file:SCHPO/asr1/asr1-uniprot.txt "FT   ZN_FING         18..79"]

Evolutionary placement (new analysis, `asr1-bioinformatics/RESULTS.md`, `compare_relatives.py`):
- PANTHER 19.0 puts O94400, human PHRF1 (Q9P1Y6) and K. phaffii Atg35 (C4QVX6) in PTHR12618:SF20, but puts S. cerevisiae Asr1 (Q06834), the PomBase-curated ortholog and ISO donor, in a different family, PTHR45798:SF97 (plant ATL-type RING-H2). S. cerevisiae has no PTHR12618 member.
- Smith-Waterman alignments with shuffle z-scores: O94400 vs PHRF1 z=28.2, vs Atg35 z=22.7, vs Sc Asr1 z=14.0 (RING/PHD only, residues 56-152). Sc Asr1 aligns to PHRF1 (z=17.0) and Atg35 (z=13.6) over the same module. So Sc Asr1 is a divergent homolog of the same RING/PHD lineage. Its separate PANTHER family looks like a classification artifact, but pairwise data cannot settle orthology.
- Consequence: only the generic RING E3 activity transfers. Asr1-specific CTD Ser5P/Ser7P recognition (PMID:40513950), Rpb1/Rpb2 substrates (PMID:19064926), alcohol-stress shuttling (PMID:15117954) and the septin overexpression phenotype (PMID:25646695) do not.

Changes from the previous version:
- GO:0005737 cytoplasm (IEA SubCell): ACCEPT -> MODIFY to GO:0005829 cytosol, which the gene already carries from the same study (correct-but-general rule).
- GO:0032991 protein-containing complex (ARBA): UNDECIDED -> MARK_AS_OVER_ANNOTATED. It is the uninformative root term and no complex is known.
- GO:0000785 chromatin (ARBA): kept UNDECIDED, with the reason rewritten. It is plausible from Sc Asr1 recruitment to Pol II and subtelomeric silencing, but there is no target evidence and the orthology is uncertain.
- GO:0061630 ISO: ACCEPT kept, with the PANTHER disagreement now stated explicitly. ND BP: ACCEPT kept. PomBase transferred MF only, a deliberate choice.
- Description: dropped the unverified "Pbr1" alias; added PANTHER subfamily context.
- Added references PMID:15117954, PMID:40513950 and PMID:25646695 (budding-yeast Asr1), plus the new RESULTS.md.

Relative: human PHRF1 (Q9P1Y6), same PANTHER subfamily (SF20); no review in the repo. Sc ASR1 (Q06834) is the PomBase ortholog but sits in a different PANTHER family; it has no review in the repo either.

Family review: interpro/panther/PTHR12618/PTHR12618-review.yaml agrees with the SF20 placement and the caution about transferring the Asr1 Pol II mechanism. It does not mention that Sc Asr1 itself is outside PTHR12618. No modules reference this gene.
