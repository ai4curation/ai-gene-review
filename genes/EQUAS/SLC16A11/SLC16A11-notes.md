# SLC16A11 (donkey, A0A9L0JV53) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry, 439 aa; names and comments come from ARBA.

## Identity and sequence
- PANTHER PTHR11360:SF80 (MONOCARBOXYLATE TRANSPORTER 11); InterPro MFS (IPR011701) and proton-linked MCT (IPR050327) [file:EQUAS/SLC16A11/SLC16A11-uniprot.txt "DR   PANTHER; PTHR11360:SF80; MONOCARBOXYLATE TRANSPORTER 11; 1."].
- Gene-model defect: donkey residues 1-100 are not homologous to human Q8NCK7, while donkey 101-439 align to human 113-447 at high identity; human TM1-TM3 have no counterpart [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/RESULTS.md "The human N-terminal region containing predicted transmembrane helices 1-3 (human 12-32, 54-74, 82-102) therefore has no homologous counterpart in the donkey model"].
- The donkey sequence does not begin with Met, consistent with an incomplete/misassembled 5' end. The donkey gene is still expected to encode a full-length MCT11; the defect is in this UniProt/Ensembl model.

## Function (human ortholog)
- Proton-linked monocarboxylate transporter that moves pyruvate across the plasma membrane; implicated in hepatic lipid metabolism and type 2 diabetes risk [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/SLC16A11-human-Q8NCK7-uniprot.txt "Proton-linked monocarboxylate transporter. It catalyzes the"].
- Location: ER membrane (PMID:24390345) and cell membrane, where it pairs with BSG (PMID:28666119) [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/SLC16A11-human-Q8NCK7-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]. Neither paper is cached locally; evidence taken from the Swiss-Prot record.

## Annotation decisions
- ER membrane, plasma membrane: ACCEPT.
- monocarboxylic acid transmembrane transporter activity and monocarboxylic acid transport (TreeGrafter): ACCEPT.
- transmembrane transporter activity, transmembrane transport (InterPro2GO): TOO_GENERAL.
- NEW pyruvate transmembrane transporter activity (ISS from human IDA).

## ProtNLM2
- GO:0022857 transmembrane transporter activity: correct, in donkey GOA, but less specific than donkey GOA's monocarboxylic acid transmembrane transporter activity -> LSP.
- No non-GO ProtNLM2 rows for this accession.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research EQUAS SLC16A11 --provider falcon` failed ("Exception: Failed to authenticate"; all providers failed), so no deep-research file exists. Literature was read directly: PMID:24390345 and PMID:28666119 (both full text), PMID:39516648 (full text), PMID:30673611, PMID:31618643, PMID:31618644 and PMID:31185508 (abstracts only). These are cached in publications/.

### Identity of the benchmark accession
- New analysis: `SLC16A11-bioinformatics/compare_gene_models_rereview.py` -> `RESULTS-rereview.md` (the original RESULTS.md and align_to_human.py are unchanged).
- UniProt has five unreviewed donkey SLC16A11 entries (A0A8C4PS96 520 aa, A0A9L0J0E5 472, A0A9L0JV53 439, A0A9L0JFG5 434, A0A9L0JZU6 416). All are transcripts of one Ensembl gene, ENSEASG00005017919.2, and all are in PANTHER PTHR11360:SF80 [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/RESULTS-rereview.md "UniProt holds five unreviewed donkey entries named SLC16A11, all cross-referenced to one Ensembl gene, ENSEASG00005017919.2"].
- A0A9L0JV53 is an alternative transcript model, not the canonical product: residues 108-439 are identical to the full-length model A0A8C4PS96 (189-520 = human 116-447). Residues 1-107 are an alternative N-terminal sequence that does not match human TM1-TM3, so TM1-TM3 are missing [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/RESULTS-rereview.md "Its residues 108-439 are identical to A0A8C4PS96 residues 189-520, which correspond to human residues 116-447."]. Part of that N-terminal segment also occurs in A0A9L0JFG5, so it looks like an alternative 5' exon rather than a one-off misassembly. This refines the earlier "misassembled" wording.
- A0A8C4PS96 is the only donkey model that contains the whole human MCT11 sequence (human Met1 = donkey 74, 90.6% identity). It is the best candidate for the canonical donkey MCT11 and has no review in the repo.

### Evolutionary grounding
- PAINT (interpro/panther/PTHR11360/PTHR11360-paint.tsv): GO:0008028 IBD at PTN000888455 (taxon 6072), with Q8NCK7 (human MCT11) among the seeds; GO:0005886 and GO:0022857 IBD at the root PTN002260587. Human MCT11's IDA terms GO:0050833 (pyruvate transmembrane transporter activity) and GO:0006629 (lipid metabolic process) were NOT propagated. Following campaign rules, that omission is treated as deliberate.
- No PANTHER family review file exists for PTHR11360 (only entries/metadata/paint), so there is no family-level subfamily disagreement to report. The donkey and human proteins are both in SF80.

### Changes from the previous review
- Removed the NEW row GO:0050833 pyruvate transmembrane transporter activity. Reasons: PAINT curators did not propagate it from the human IDA; mouse MCT11 mediates lactate uptake [PMID:39516648 "Conditional deletion of MCT11 in T cells reduced lactic acid uptake by Tex cells"], so pyruvate is not the only substrate; and one of its supporting quotes was the human record's own DR GO line, which restates an annotation and is not evidence. The core MF is now GO:0008028 (family level), with pyruvate and lactate named in the description.
- Support moved from the human UniProt record to the primary papers: ER [PMID:24390345 "SLC16A11-V5 co-localizes with the endoplasmic reticulum membrane protein Calnexin"], plasma membrane and BSG [PMID:28666119 "We found that BSG knockout significantly reduces localization of SLC16A11REF to the plasma membrane"], H+ coupling [PMID:28666119 "These results support a H+-coupled mechanism underlying SLC16A11 transport"].
- Actions on the GOA rows are unchanged: ER membrane, plasma membrane, GO:0008028 and GO:0015718 are ACCEPT; GO:0022857 and GO:0055085 are TOO_GENERAL (both are entailed by GO:0008028; GO:0015718 is not itself under GO:0055085, which was checked in OLS).
- Not added: lipid metabolic process (human overexpression and knockdown metabolic effects are indirect; PAINT did not propagate it); T2D and glucose tolerance phenotypes (organismal; the knockout and gain-of-function evidence is disputed, PMID:30673611 vs PMID:31618643).
- The description was rewritten to be project-independent and to describe the transcript-model status.

### Relative to review next
- Same gene, canonical product: A0A8C4PS96 (donkey SLC16A11, 520 aa, full-length). No review exists; its folder would be genes/EQUAS/SLC16A11__A0A8C4PS96 because genes/EQUAS/SLC16A11 is keyed to the A0A9L0JV53 transcript model.
- The best-characterised ortholog is human SLC16A11 (Q8NCK7, same subfamily SF80). It has no review in the repo either; only donkey and horse (genes/HORSE/SLC16A11, a separate agent's partner review) folders exist.
- Modules: no module in modules/ mentions SLC16A11, Q8NCK7 or PTHR11360.
