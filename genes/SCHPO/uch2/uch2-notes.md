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


## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used for this section.

### Identity
- Q9UUB6 is the reviewed, canonical, full-length uch2/SPBC409.06 product (300 aa, sequence version 1). It is not an isoform, fragment or alternative gene model.
- UCH catalytic domain 2-220 and ULD 261-290 (PROSITE); catalytic residues checked on the sequence: Q77, C83 (nucleophile), H159 (proton donor), D174, all intact.
- PANTHER PTHR10589:SF16 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE ISOZYME L5), the same subfamily as human UCHL5 (Q9Y5K5), mouse Uchl5 (Q9WUP7), worm ubh-4, Arabidopsis UCH1/UCH2 (interpro/panther/PTHR10589/PTHR10589-entries.csv). The family review interpro/panther/PTHR10589/PTHR10589-review.yaml also puts uch2 in the UCHL5 branch, so there is no placement disagreement. S. cerevisiae has no ortholog in this subfamily (Yuh1 is a small UCH).

### Evolutionary grounding of the IBAs
- Both IBAs (GO:0004843, GO:0005737) come from PTN000063280, the PTHR10589 family root. The seeds include UCHL1/UCHL3/BAP1/Yuh1 as well as UCHL5 and Uch2 itself.
- The cysteine-type DUB activity is ancestral and was kept (ACCEPT).
- For cytoplasm, no S. pombe donor is among the seeds, and target imaging says exclusively nuclear [PMID:20838651 "Ubp6, Ubp8, Ubp14, Ubp16, Rpn11, and Uch2 are exclusively nuclear (Figure 2A and 2B)"], with nuclear-periphery enrichment [PMID:10872838 "The GFP-tagged Uch2p is localized predominantly to the nuclear periphery, which is similar to the 26S proteasome localization."]. Changed UNDECIDED to MARK_AS_OVER_ANNOTATED and added propagation_review.

### Literature re-checks
- PMID:23496905 (full text in cache): GST-Uch2 cleaves NEDD8-AMC, but "the deletion of both homologues of YUH1 in S. pombe does not result in any loss of Cul1 neddylation". Decisions: deNEDDylase activity (IDA) goes from MARK_AS_OVER_ANNOTATED to KEEP_AS_NON_CORE, since it is a real in vitro activity measured with the conventional assay; protein deneddylation (IDA, BP) stays MARK_AS_OVER_ANNOTATED, since no in vivo deconjugation is shown.
- PMID:28765280: the cache is abstract-only and a forced re-fetch got no full text. I read the full text at PMC5602385 online. It states: "For both uch2Δ (the UCH37/UCHL5 orthologue in fission yeast) and ubp3Δ, we observed a suppression of the sec3-913 temperature-sensitive growth defect" and "This phenotype suppression was more pronounced for ubp3 than for uch2". GO:0071629 goes from UNDECIDED to KEEP_AS_NON_CORE (it is a substrate context of the core proteasomal role). No quote is asserted in the YAML, because the cache cannot verify it.
- GO:0140492 metal-dependent DUB (HDA): MODIFY to GO:0004843 is kept. Uch2 is a C12 cysteine protease, and the pulldown contains Rpn11 (JAMM).
- GO:0006511 (IEA): changed from ACCEPT to MODIFY, with GO:0043161 as the replacement. GO:0043161 is an is_a child of both GO:0006511 and GO:0010498 (checked against the OLS parents). Core function now uses GO:0043161 together with GO:0016579.

### Relative
- The closest experimentally characterised relative in the same subfamily is human UCHL5 (Q9Y5K5). The repo has no UCHL5 review (no genes/*/UCHL5 folder), so it needs a review.
- Modules: none in modules/ cover the S. pombe proteasome or the UCH37/Rpn13 module. modules/dmel_proteasome.yaml is the only proteasome module, and it is Drosophila-specific.
