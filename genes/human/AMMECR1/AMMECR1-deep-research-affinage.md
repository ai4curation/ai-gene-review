---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMMECR1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9Y4X0
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 8
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AMMECR1 (human)

## Current model (mechanistic narrative)

AMMECR1 is an X-linked nuclear protein implicated in cell cycle progression, cell survival, and vertebrate development [PMID:29193635, PMID:31519561]. Its paralog interaction defines its core biochemistry: AMMECR1 dimerizes with AMMECR1L and the complex localizes to the nucleus, and the patient-derived missense substitution p.G177D disrupts correct nuclear targeting, identifying G177 as a residue required for proper localization [PMID:27811305, PMID:29193635]. Loss-of-function studies establish a cellular role: RNAi silencing in A549 lung cancer cells suppresses proliferation and colony formation, promotes apoptosis, and arrests cells in S and G2/M phases [PMID:31519561]. In zebrafish, knockdown of the AMMECR1 ortholog produces growth, bone, and cardiac phenotypes that mirror patient features, linking the gene to developmental processes [PMID:29193635]. The direct molecular activity of AMMECR1 has not been demonstrated biochemically in the available corpus; an enzymatic or nucleic-acid/nucleotide-interaction role has only been predicted computationally [PMID:17715145, PMID:24646681].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** *(none)*
- **partners:** AMMECR1L
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | Low | AMMECR1 encodes a 35.5 kDa protein with a six-amino-acid domain (encoded by exon 2) that is identically conserved across species from yeast and C. elegans to humans, suggesting a critical conserved function; computational analysis of the predicted protein raised the possibility it codes for a regulatory factor. | PMID:10049589 | Genomics |
| 2007 | Low | AMMECR1 contains a RAGNYA fold — a shared alpha+beta fold involved in nucleic acid, nucleotide, or peptide interactions — and structure similarity searches predicted a catalytic/enzymatic role for AMMECR1 in nucleic acid or nucleotide interaction via the exposed face of its beta-sheet. | PMID:17715145 | Nucleic acids research |
| 2014 | Low | Computational analysis predicted that the AMMECR1 family of proteins may participate in a pathway involving RNA base modifications, potentially as part of a hitherto unknown modification mechanism that could target rRNAs, at least in archaea and possibly eukaryotes, in association with a DNA glycosylase-related enzymatic domain. | PMID:24646681 | RNA biology |
| 2016 | Medium | A missense mutation in AMMECR1 (p.G177D) causes aberrant nuclear localization of the AMMECR1 protein compared to wild-type, demonstrating that the G177 residue is required for correct nuclear targeting/localization of the protein. | PMID:27811305 | Journal of medical genetics |
| 2017 | Medium | AMMECR1 and its paralog AMMECR1L proteins dimerize and localize to the nucleus, consistent with their nucleic acid-binding RAGNYA folds; knockdown of the zebrafish ortholog produced phenotypes reminiscent of patient features (growth, bone, and cardiac alterations), establishing a role in development. | PMID:29193635 | Human mutation |
| 2017 | Low | AMMECR1 is co-expressed with genes implicated in cell cycle regulation, five of which were previously associated with growth and bone alterations, suggesting AMMECR1 is potentially involved in cell cycle control. | PMID:29193635 | Human mutation |
| 2019 | Medium | Lentiviral RNAi-mediated silencing of AMMECR1 in A549 human lung cancer cells significantly suppressed cell proliferation, reduced colony formation, promoted apoptosis, and arrested cells in the S and G2/M phases, establishing a role for AMMECR1 in cell cycle progression and anti-apoptotic function. | PMID:31519561 | Anticancer research |
| 2019 | Low | The AMMECR1 domain shows conserved genomic context associations with the Memo domain and a radical S-adenosylmethionine family domain, extending predicted functional links to nucleotide base and aliphatic isoprenoid modification pathways. | PMID:31092555 | The Journal of biological chemistry |

## Citations

- PMID:10049589
- PMID:17715145
- PMID:24646681
- PMID:27811305
- PMID:29193635
- PMID:31092555
- PMID:31519561
