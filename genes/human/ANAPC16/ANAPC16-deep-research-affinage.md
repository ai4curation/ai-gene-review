---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANAPC16
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q96DE5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANAPC16 (human)

## Current model (mechanistic narrative)

ANAPC16 (APC16) is a metazoan-specific subunit of the APC/C E3 ubiquitin ligase that contributes to the ubiquitination of cell-cycle substrates required for mitotic and meiotic progression [PMID:20392738, PMID:21775471]. It is a bona fide component of the human APC/C present throughout the cell cycle, and its depletion reduces APC/C ubiquitin ligase activity toward mitotic substrates, phenocopying loss of other APC/C subunits [PMID:20392738]. Structurally, APC16 resides in the Arc Lamp subcomplex together with CDC26, APC13, and the TPR proteins APC7, APC3, APC6, and APC8, where a single APC16 molecule binds asymmetrically to the symmetric APC3 homodimer and bridges APC3 to APC7, recruiting APC7 into the assembly [PMID:25490258]. APC16 is conserved across metazoans but absent in fungi, with functional equivalents identified in C. elegans (emb-1/K10D2.4) and zebrafish [PMID:20392738]; in C. elegans, loss of emb-1 arrests one-cell embryos in metaphase of meiosis I and is genetically suppressed and enhanced by known APC/C regulators, and it is additionally required for mitotic germline proliferation, placing APC16 firmly within the APC/C pathway for both meiotic and mitotic cell division [PMID:21775471].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-392499 Metabolism of proteins
- **partners:** APC3, APC7
- **complexes:** APC/C, Arc Lamp subcomplex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | High | Crystal structures of APC3Δloop alone and in complex with the C-terminal domain of APC16 revealed that one APC16 molecule binds asymmetrically to the symmetric APC3 homodimer, establishing the structural basis for APC3-APC16 interaction and showing how APC16 recruits APC7 to APC3 within the APC/C Arc Lamp subcomplex. | PMID:25490258 | Journal of molecular biology |
| 2014 | High | APC16 is located in the Arc Lamp subcomplex of the APC/C together with CDC26, APC13, and TPR proteins (APC7, APC3, APC6, APC8), where it mediates assembly by bridging APC3 and APC7. | PMID:25490258 | Journal of molecular biology |
| 2010 | High | APC16 is a bona fide subunit of the human APC/C, present in APC/C complexes throughout the cell cycle; depletion of APC16 reduces APC/C ubiquitin ligase activity toward mitotic substrates and phenocopies depletion of other APC/C subunits. | PMID:20392738 | Journal of cell science |
| 2010 | Medium | APC16 is conserved in metazoans but not fungi; C. elegans K10D2.4 and zebrafish zgc:110659 are functional equivalents of human APC16, establishing its role as a metazoan-specific APC/C subunit. | PMID:20392738 | Journal of cell science |
| 2011 | High | C. elegans emb-1 encodes the APC16 homolog K10D2.4; emb-1 loss-of-function arrests one-cell embryos in metaphase of meiosis I, and the phenotype is enhanced in double mutants with other APC/C subunits and suppressed by known APC/C suppressors, placing APC16/EMB-1 within the APC/C pathway for meiotic progression. | PMID:21775471 | Genetics |
| 2011 | Medium | In addition to its meiotic role, C. elegans APC16 (EMB-1) is required for mitotic proliferation of the germline, indicating a mitotic function consistent with its role as an APC/C subunit. | PMID:21775471 | Genetics |

## Citations

- PMID:20392738
- PMID:21775471
- PMID:25490258
