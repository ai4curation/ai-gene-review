# crt10 notes

Identity: crt10, UniProt O42996; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `crt10-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

UNC: Crt10 has a diagnostic CRT10 domain and a documented orthologous role in Rtt101-Mms1-dependent nonfunctional rRNA decay. This supports a relationship to cullin-mediated ubiquitination, but does not establish residence in the specific Cul4-RING E3 complex in fission yeast. The XML claim is a low-scoring phmmer transfer from Arabidopsis WDR5B Q9SY00 (model_score 0.11; phmmer_score 66.0); shared WD-repeat architecture does not demonstrate the relevant cullin partner or conserved subfamily function. Direct target-complex evidence or defensible orthology connecting this complex membership is missing. The claim is neither validated nor conclusively refuted.

[PMID:25534857 "We herein demonstrated that another accessory component, Crt10 was required for 25S NRD, but not for DNA repair, suggesting that this accessory component specifies the function of the E3 complex differently."]

[file:SCHPO/crt10/crt10-uniprot.txt "DR   InterPro; IPR014839; Crt10."]

UNC: The exact UV-B response prediction is not supported by the reviewed target annotations. Its source is a TMalign comparison to Arabidopsis DHU1 Q8GYY7 (model_score 0.11; chain-normalized scores 0.56569 and 0.36277), rather than a demonstrated conserved UV-B response mechanism. The experimentally characterized budding-yeast Crt10 directs nonfunctional 25S rRNA decay and is dispensable for the DNA-repair assay examined in that study, which does not exclude every possible UV-B response. Shared WD-repeat structure alone cannot validate this wavelength-specific phenotype in fission yeast. Target UV-B experiments or a conserved mechanistic link are missing, so UNC is appropriate.

[PMID:25534857 "We herein demonstrated that another accessory component, Crt10 was required for 25S NRD, but not for DNA repair, suggesting that this accessory component specifies the function of the E3 complex differently."]

[file:SCHPO/crt10/crt10-uniprot.txt "DR   Pfam; PF08728; CRT10; 1. DR   Pfam; PF00400; WD40; 1."]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. In particular, the report does not recover the target localization evidence in PMID:16823372; the reviewed UniProt record explicitly cites it. The current PomBase identifier mapping and orthology annotations resolve identity or inherited functions more specifically than the report's ambiguous-symbol caveats. The report's coatomer speculation is not a demonstrated pathway. The CRT10 domain and PomBase nonfunctional-rRNA-decay ISO assertion are weighed against the primary Crt10 study (PMID:25534857).
