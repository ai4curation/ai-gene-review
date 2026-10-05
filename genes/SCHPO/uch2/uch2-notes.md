# uch2 notes

Identity: uch2, UniProt Q9UUB6; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `uch2-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

LSP: Fission-yeast Uch2 is directly characterized as the major deubiquitinating enzyme associated with the 26S proteasome, and proteomic work recovers its association with the proteasome. Processing ubiquitin conjugates at this complex is a function in ubiquitin-dependent protein turnover even though the DUB removes ubiquitin rather than degrading the substrate polypeptide itself. The supported, more precise proteasomal protein catabolic process annotation GO:0010498 is already present. Thus the general catabolic-process prediction is correct but less precise; weak deletion phenotypes reflect redundancy and do not negate pathway participation.

[PMID:15533439 "We report that the subunit Uch2/Uch37 is the major deubiquitinating enzyme associated with the fission yeast 26S proteasome."]

[PMID:20838651 "Rpn11 and Uch2 co-purified all of the 26S proteasome subunits (19S regulatory particle and 20S core particle) in quantities similar to those of the bait (Table S1)"]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. The report gives useful UCH37 family context but does not recover all older Uch2-specific work; PMID:10872838, PMID:15533439 and the full-text census PMID:20838651 directly establish target localization, catalytic class and proteasome association.

## Ontology specificity

QuickGO GO:0019784 (deNEDDylase activity), accessed 2026-09-08: "An isopeptidase activity that cleaves NEDD8 from a target protein to which it is conjugated.". The frozen JSON is adjacent to this file.

QuickGO GO:0140492 (metal-dependent deubiquitinase activity), accessed 2026-09-08: "An metal-dependent isopeptidase activity that cleaves ubiquitin from a target protein to which it is conjugated.". The frozen JSON is adjacent to this file.

