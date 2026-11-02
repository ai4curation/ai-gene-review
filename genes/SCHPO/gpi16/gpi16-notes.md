# gpi16 (O94380) — evidence and prediction assessment

Gpi16 is the PIG-T-family accessory subunit of the endoplasmic-reticulum GPI-anchor transamidase complex. Its large lumenal domain and C-terminal membrane anchor support assembly and function of the machinery that attaches preformed GPI anchors to proteins. The catalytic cleavage/transamidation chemistry belongs to the Gpi8/PIG-K subunit, rather than to Gpi16 alone.

## Evidence and family boundary

PIG-T/Gpi16 is distinct from the Gpi8/PIG-K catalytic protease. The full 545-aa target has a predicted signal peptide1–22, lumenal domain23–493, membrane helix494–514 and cytosolic tail515–545 in the [curated sequence record](gpi16-uniprot.txt). GPI transamidase membership supports the protein-attachment process; it does not justify an autonomous peptidase or transamidase MF.

[PMID:15003443](https://pubmed.ncbi.nlm.nih.gov/15003443/) is a computational GPI-site predictor paper used by ComplexPortal as a NAS source, not a direct target-complex purification. The annotation is retained as curated orthology/context. Falcon provides useful yeast/mammalian mechanistic synthesis but misses the target HDA ER localization already attributed to PMID:16823372. Its assertion of no target localization should not override that observation. A conserved PIG-T/PIG-K disulfide is not claimed as experimentally measured in pombe.

## External ProtNLM statements

[Exact retained output](gpi16-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | GPI transamidase component PIG-T | CNN | PIG-T/Gpi16 identity agrees with the curated orthology, PIG-T domain and type-I ER membrane architecture. The name asserts complex membership rather than autonomous transamidase catalysis (O94380; IPR007245; CPX-10141). |

## Source quotations

## Research provenance

The genuine [Falcon report](gpi16-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.

## Direct ortholog evidence for the subunit boundary

Budding-yeast Gpi16 co-purifies with Gaa1 and Gpi8; depletion accumulates complete GPI lipid and unprocessed precursor proteins. Mammalian PIGT knockout and complex experiments establish an essential stabilizing role, while human structural analysis identifies PIGK as the catalytic component. These observations ground the conserved accessory-subunit inference for pombe Gpi16. The three cached articles are abstract-only, and their abstracts explicitly describe these experiments.

- [PMID:11598210](https://pubmed.ncbi.nlm.nih.gov/11598210/): Budding-yeast affinity purification establishes Gpi16 as a GPI-transamidase component, providing direct ortholog evidence.

> These complexes can be affinity purified
> and are shown to consist of Gaa1p, Gpi8p, and Gpi16p (YHR188c).

- [PMID:11483512](https://pubmed.ncbi.nlm.nih.gov/11483512/): Mammalian knockout and complex experiments establish a stabilizing accessory role for PIG-T.

> PIG-T maintains the complex by stabilizing the expression of GAA1 and GPI8.

- [PMID:35165458](https://pubmed.ncbi.nlm.nih.gov/35165458/): The human structure and mutational study identifies PIGK, not PIGT, as the catalytic component.

> The PIGK subunit 
> functions as the catalytic component


## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: every existing annotation, the description and core functions were re-examined against the cached primary literature, the UniProt record, the PANTHER/PAINT data and the Falcon report. No ProtNLM2 file or prediction output was consulted.

**Identity.** O94380 is the reviewed Swiss-Prot canonical entry for gpi16/SPBC1604.15, 545 aa, full length. It has a signal peptide (1-22), a lumenal PIG-T domain (23-493), one TM helix (494-514) and a cytosolic tail (515-545). It is not an isoform, fragment or alternative gene model.

**Evolutionary grounding.** PANTHER PTHR12959:SF11 (GPI TRANSAMIDASE COMPONENT PIG-T), the same subfamily as S. cerevisiae GPI16 (P38875), mouse Pigt and human PIGT (Q969N2) (`interpro/panther/PTHR12959/PTHR12959-entries.csv`). The PAINT IBD node PTN000311103 sits at taxon Eukaryota and carries only GO:0042765 (complex) and GO:0016255 (attachment of GPI anchor to protein), with SGD, FB, MGI and human donors (`PTHR12959-paint.tsv`). It carries no MF, and human PIGT has no contributes_to transamidase-activity row, so the ND MF is kept and no MF is proposed. The family review `interpro/panther/PTHR12959/PTHR12959-review.yaml` puts O94380 in SF11, which agrees with UniProt. No disagreement over subfamily placement.

**Changes from the previous review.**
- GO:0031505 fungal-type cell wall organization (ComplexPortal NAS): KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. The cell wall depends on GPI-anchored proteins downstream of the transamidase, but Gpi16 does none of the work of organising it. That is necessity, not participation. No fission-yeast gpi16 cell-wall phenotype has been reported (Falcon report).
- GO:0006506 MODIFY to GO:0016255 kept, now with the GO structure stated: GO:0016255 sits under GO:0180046 GPI anchored protein biosynthesis, not under GO:0006506 (checked with OLS hierarchicalAncestors). Budding-yeast Gpi16 depletion accumulates the complete GPI lipid CP2 [PMID:11598210 "Depletion of Gpi16p results in the accumulation of the complete GPI lipid CP2 and of unprocessed GPI precursor proteins."].
- Added ortholog topology support [PMID:11598210 "Its bulk resides on the lumenal side of the ER, and it has a single C-terminal transmembrane domain"] for the ER membrane and lumenal-side rows, and pan-eukaryotic conservation [PMID:11598210 "Homologues of Gpi16p are found in all eucaryotes."].
- Added PMID:12582175 (mammalian GPI8-PIG-T disulfide) as background only. It is not transferred, because budding-yeast Gpi16 reportedly lacks the disulfide (Falcon report).
- Description rewritten to name the full complex and the type-I topology; reference_review added for PMID:15003443 and PMID:16823372; suggested questions and experiments added.
- All other actions are unchanged (ACCEPT on complex, process, ER membrane, lumenal side, ND MF; MODIFY of HDA ER to ER membrane).

**Relative for next review.** S. cerevisiae GPI16 (P38875, SGD:S000001231): the same PANTHER subfamily SF11, a PAINT donor at PTN000311103, and the experimentally characterised fungal ortholog (affinity purification, depletion). There is no `genes/yeast/GPI16` folder in the repo. Human PIGT (`genes/human/PIGT`) exists but has status INITIALIZED.

**Modules.** `modules/gpi_anchor_transamidase.yaml` (models the human PIGK/PIGS/PIGT/PIGU/GPAA1 complex; no fission-yeast member listed). The upstream GPI-assembly modules (`gpi_anchor_glcnac_transferase.yaml`, `gpi_anchor_core_glycan_assembly.yaml`, `gpi_anchor_ethanolamine_phosphate.yaml`) and the downstream `gpi_anchor_remodeling.yaml` give pathway context.
