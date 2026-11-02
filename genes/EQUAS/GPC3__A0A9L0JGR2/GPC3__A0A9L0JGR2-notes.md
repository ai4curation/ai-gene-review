# GPC3 (donkey, Equus asinus; UniProt A0A9L0JGR2) - review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. This is the first review of this accession. It is the
canonical, colinear product of the donkey GPC3 gene (Ensembl ENSEASG00005018489). The same gene's
alternative-first-exon model A0A9L0J2B1 is reviewed separately in `genes/EQUAS/GPC3/`.

### Setup
- `just fetch-gene EQUAS A0A9L0JGR2 --alias GPC3__A0A9L0JGR2`. Stub id confirmed as A0A9L0JGR2. GOA has 8 IEA rows (5 TreeGrafter GO_REF:0000118 from PTN001327382, 2 InterPro2GO from IPR001863, plasma membrane via GO_REF:0000120). No PMIDs in GOA.
- Deep research: `just deep-research-falcon EQUAS GPC3__A0A9L0JGR2 --fallback perplexity-lite` failed. Falcon returned "Edison API request failed: Failed to authenticate" and the perplexity-lite fallback also failed. No deep-research file exists. The review relies on cached literature and UniProt records.

### Evolutionary grounding
- Donkey A0A9L0JGR2, human P51654 and mouse Q8CFZ4 all carry PANTHER PTHR10822:SF4 (GLYPICAN-3) in their UniProt records.
- PAINT (`interpro/panther/PTHR10822/PTHR10822-paint.tsv`): positive regulation of canonical Wnt at PTN000850517 (seeds dally, human GPC3); cell surface, extracellular region, cell migration, regulation of protein localization to membrane at PTN002247069; plasma membrane at PTN002585559 (seeds mouse Gpc3, rat Gpc3, human GPC3). These match the donkey TreeGrafter rows and human GPC3 IBA rows (QuickGO, 2026-10-21).
- Not inherited by the GPC3 lineage: extracellular matrix/synapse (PTN000088172), FGF binding (PTN002585522, seed Gpc1). Human GPC3 has no IBA for them, so I treat this as a deliberate omission. That supports MARK_AS_OVER_ANNOTATED for the InterPro2GO extracellular matrix row.
- No PAINT node carries a hedgehog term. The hedgehog function rests on mouse Gpc3 experiments [PMID:18477453 "GPC3 competes with Patched for Hedgehog binding"], and human GPC3 has it only by ISS from mouse. I transferred it only within the GPC3 subfamily (ISS) and not as a family-wide glypican function.

### Sequence (new analysis)
- `GPC3__A0A9L0JGR2-bioinformatics/compare_orthologs.py` (PEP 723) produced `compare_orthologs_output.txt`, which is summarised in `RESULTS.md`. Donkey vs human: 558/580 identical (96.21%), no indels, signal peptide 22/24 identical. R358/S359 convertase site, S495/S509 heparan sulfate serines and N554 GPI anchor are all conserved. Donkey vs mouse: 551/579 (95.16%).

### Experimental status in this species
- None. No donkey GPC3 study was found. Every function in the review is inferred from human (Wnt/Frizzled, membrane location, processing) or mouse (hedgehog) GPC3 in the same subfamily, and the NEW rows are ISS.

### Decisions
- ACCEPT: plasma membrane, cell surface, positive regulation of canonical Wnt signaling pathway.
- KEEP_AS_NON_CORE: extracellular region (shed form), cell migration (zebrafish morphant phenotype not used as participation evidence), regulation of protein localization to membrane.
- TOO_GENERAL: regulation of signal transduction.
- MARK_AS_OVER_ANNOTATED: extracellular matrix.
- NEW (ISS): frizzled binding (PMID:24496449, human), hedgehog family protein binding and negative regulation of smoothened signaling pathway (PMID:18477453, mouse). Hh participation: GPC3 itself binds and sequesters the ligand.
- Not added: peptidyl-dipeptidase inhibitor activity (human IDA, PMID:17549790, DPP4). It comes from a single cancer-cell study and is not part of the core signaling roles. Organ-development ISS terms on human GPC3 (kidney, heart, BMP response) are downstream phenotypes of mouse knockouts and were not added.
