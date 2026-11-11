# DUSP5 (donkey, A0A8C4MED2) - review notes

DONKEY40 cohort. All 11 GOA rows are IEA (TreeGrafter, EC mapping, InterPro2GO, UniRule, Ensembl Compara, combined). No PMIDs were cited by GOA; evidence comes from the human ortholog record, a cached paper, and a sequence comparison.

## Sequence
- Donkey 384 aa vs human Q16690 384 aa: [file:EQUAS/DUSP5/DUSP5-bioinformatics/RESULTS.md "94.79% identity over 384 paired residues"]. Catalytic Cys conserved: ["ACT_SITE Phosphocysteine intermediate: human [263] C -> donkey [263] C"]. NLS fully conserved: ["22 of 22 human residues in this span are identical"].
- Script: `DUSP5-bioinformatics/compare.py` (Biopython global alignment); human GOA download in `human-Q16690-quickgo-annotations.tsv`.

## Function
- Human UniProt: [file:EQUAS/DUSP5/DUSP5-bioinformatics/human-Q16690-uniprot.txt "Dual specificity protein phosphatase; active with phosphotyrosine, phosphoserine and phosphothreonine residues. The highest relative activity is toward ERK1."]
- [PMID:15713638 "We conclude that DUSP5 is an inducible nuclear ERK-specific MAP kinase phosphatase that functions as both an inactivator of and a nuclear anchor for ERK2 in mammalian cells."]
- Specificity: [PMID:15713638 "it inactivates ERK2 but not Jun N-terminal protein kinase or p38 MAP kinase"].

## Decisions
- Core: GO:0017017 MAPK Tyr/Ser/Thr phosphatase activity; GO:0043409 negative regulation of MAPK cascade; nucleus.
- TreeGrafter rows: endoderm formation (over-annotated; zebrafish developmental phenotype), cytoplasm (over-annotated; DUSP5 is nuclear), phosphoprotein phosphatase activity (too general), negative regulation of MAPK cascade (accept).
- ProtNLM2 GO:0017018 myosin phosphatase activity: wrong (myosin phosphatase is the PP1c/MYPT1 holoenzyme, a different phosphatase family).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this pass.

### Identity
- A0A8C4MED2 is the full-length donkey DUSP5 product, not a fragment, isoform or alternative model: 384 aa, the same length as human Q16690, aligned over 100% of both sequences [file:EQUAS/DUSP5/DUSP5-bioinformatics/RESULTS.md "94.79% identity over 384 paired residues"]. Rhodanese/KIM domain 122/123 identical, DSP domain 136/142, NLS 22/22, catalytic Cys263 conserved.
- Evolutionary placement: UniProt cross-references PANTHER PTHR10159:SF40 "DUAL SPECIFICITY PROTEIN PHOSPHATASE 5" (the task header said "none listed", but the UniProt record does list it). Human Q16690 and rat O54838 are also SF40 in interpro/panther/PTHR10159/PTHR10159-entries.csv, so function transfer from human DUSP5 is ortholog-level, not best-hit.
- No PANTHER family review (only entries/metadata files) exists under interpro/panther/PTHR10159/; no placement disagreement to report.

### Deep research
- `just deep-research EQUAS DUSP5 --provider falcon` failed ("Exception: Failed to authenticate", Edison JWT). Proceeded with cached literature: PMID:15713638 (full text), PMID:7961985 (abstract; newly cached), PMID:24531476 (abstract; newly cached, not used as support).

### PAINT context (from human QuickGO download in DUSP5-bioinformatics/)
- Human IBA endoderm formation comes from PTN000017039 with a single zebrafish donor; cytoplasm and negative regulation of MAPK cascade from the deep MKP node PTN001605855; nucleus from PTN000806857. The donkey TreeGrafter rows cite PTN001300107.

### Changes vs previous pass
- GO:0043409 ACCEPT -> MODIFY to GO:0070373 negative regulation of ERK1 and ERK2 cascade: DUSP5 is ERK-selective [PMID:15713638 "it inactivates ERK2 but not Jun N-terminal protein kinase or p38 MAP kinase"].
- Generic phosphatase rows (GO:0004721, GO:0008138, GO:0016791) -> MODIFY to GO:0017017 (descendant already carried); EC-derived GO:0004722 and GO:0004725 -> MODIFY (lateral) to GO:0017017, since in current GO GO:0017017 is not under either single-specificity term and DUSP5 is a PTP-family dual-specificity enzyme. Hydrolase activity kept TOO_GENERAL. Consistent with the human DUSP6 review.
- Endoderm formation and cytoplasm remain MARK_AS_OVER_ANNOTATED; reasons rewritten to argue biology (developmental outcome / lineage-specific nuclear MKP) rather than donor count.
- NEW GO:0051019 mitogen-activated protein kinase binding: KIM-mediated ERK2 binding with catalysis-independent nuclear anchoring [PMID:15713638 "the use of a catalytically inactive mutant to anchor ERK2 in the nucleus"]. Comparator: DUSP6 review uses the same term.
- Added second core function (MAPK binding / nuclear anchoring); first core function now uses GO:0070373.

### Relative
- Human DUSP5 (Q16690), ortholog (same PANTHER SF40). No review in repo (no genes/human/DUSP5) -> needs review.
- Modules: modules/erk_cascade.yaml (DUSP/MKP feedback step, represented by DUSP6); also see modules/kinase_phosphatase_toggle.yaml.
