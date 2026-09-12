---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTL7B
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q9Y614
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACTL7B (human)

## Current model (mechanistic narrative)

ACTL7B is a testis-enriched actin-related protein required for spermiogenesis and male fertility [PMID:36617158]. The intronless human gene on chromosome 9q31 arose by retroposition of a spliced actin-progenitor mRNA and encodes a 415-amino-acid actin-like protein expressed predominantly in testis [PMID:10373328]. Its germ-cell-restricted expression is controlled at two levels: repressive CpG methylation within the ORF CpG island silences the promoter in somatic cells, while demethylation accompanies expression in spermatogenic cells [PMID:12907721], and a bidirectional intergenic regulatory region together with CREMτ acting on CRE-like promoter motifs drives haploid germ-cell-specific transcription [PMID:12704725]. During spermiogenesis ACTL7B localizes to the developing acrosome, the early spermatid nucleus, and the flagellum connecting region, and its loss in mice produces severe oligoteratozoospermia with multiple morphological abnormalities of the flagellum and sperm head [PMID:36617158]. Beyond this established role, ACTL7B's intranuclear function and its candidate involvement in chromatin regulation through HDAC1/HDAC3 and nucleosome remodeler complexes have not been biochemically characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005634 nucleus, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-1474165 Reproduction
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | Medium | Methylation of the CpG island within the open reading frame (ORF) of Tact1/Actl7b, but not methylation of the 5' upstream region, represses promoter activity in somatic cells; demethylation of the ORF CpG island is required for expression in spermatogenic cells. | PMID:12907721 | Nucleic acids research |
| 2003 | Medium | A ~2 kb intergenic sequence between Tact1 and Tact2 bidirectionally controls haploid germ-cell-specific expression; the Tact1 promoter contains CRE-like motifs and CREMτ can activate Tact1 expression in germ cells. | PMID:12704725 | Molecular reproduction and development |
| 1999 | Medium | ACTL7B is an intronless gene on human chromosome 9q31 encoding a 415-amino-acid actin-like protein expressed predominantly in the testis and, to a lesser extent, in the prostate; the gene arose by retroposition of a spliced mRNA from an actin progenitor gene. | PMID:10373328 | Genomics |
| 2023 | High | ACTL7B localises specifically to the developing acrosome, within the nucleus of early spermatids, and to the flagellum connecting region during spermiogenesis; knockout of Actl7b in mice causes male infertility with severe oligoteratozoospermia (OAT) and multiple morphological abnormalities of the flagellum (MMAF) and sperm head, identifying ACTL7B as a key regulator of spermiogenesis. | PMID:36617158 | Biology of reproduction |
| 2024 | Low | ACTL7B is present intranuclearly in spermatocytes and round spermatids; ablation of ACTL7B leads to loss of intranuclear localisation of HDAC1 and HDAC3 in KO mouse testis; in silico modelling predicts ACTL7B can bind HSA domains of INO80 and SWI/SNF nucleosome remodeler family members in a manner analogous to nuclear actin and ACTL6A, suggesting ARP subunit swapping in chromatin regulatory complexes. | PMID:38464253 | bioRxiv |

## Citations

- PMID:10373328
- PMID:12704725
- PMID:12907721
- PMID:36617158
- PMID:38464253
