---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCB
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q8NB91
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCB (human)

## Current model (mechanistic narrative)

FANCB (originally identified as FAAP95) is an X-linked component of the Fanconi anemia (FA) core complex that acts upstream to promote FANCD2 monoubiquitination during the repair of DNA interstrand crosslinks (ICLs) [PMID:15611632, PMID:21458466]. Loss of FANCB abolishes MMC- and crosslink-induced FANCD2 foci formation and reduces RAD51 foci, sister chromatid exchange, and gene targeting, producing crosslinker hypersensitivity and chromosomal instability, while a parallel MUS81-dependent route handles replication-fork repair independently of FANCB [PMID:17903171, PMID:21458466]. Biochemical reconstitution establishes that FANCB protein is indispensable for FANCD2 monoubiquitination, and the degree of residual monoubiquitination conferred by FANCB missense variants correlates with clinical severity [PMID:32106311]. Beyond canonical ICL repair, FANCB has dedicated germline and stem-cell roles: during male meiosis it localizes to the sex chromosomes in an MDC1/γH2AX-dependent manner, is required for meiotic FANCD2 localization, and shapes sex-chromosome H3K9 methylation (decreasing H3K9me2 and increasing H3K9me3 upon loss), with FANCB-mutant mice showing primordial germ cell defects and spermatogonial failure [PMID:26123487]; it also maintains hematopoietic stem cell quiescence and repopulating capacity [PMID:26658157]. Truncating loss-of-function FANCB mutations cause X-linked VACTERL-hydrocephalus syndrome in hemizygous males, with carrier females showing skewed X-inactivation [PMID:21910217].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-4839726 Chromatin organization
- **partners:** FANCD2, MDC1
- **complexes:** FA core complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | Medium | FANCB (previously misidentified as BRCA2/FANCB) was identified as FAAP95, a previously uncharacterized component of the FA core complex that functions upstream of FANCD2 monoubiquitination, placing FANCB in the FA core complex rather than downstream or in a parallel pathway. | PMID:15611632 | Cell cycle (Georgetown, Tex.) |
| 2007 | High | FANCB (as a component of the FA core complex) and Mus81 act independently in repairing camptothecin-induced DNA damage during replication; FANCB is required for FANCD2 foci formation after DNA crosslink damage but not for sister chromatid exchanges, gene targeting, or hydroxyurea-induced replication fork repair, while Mus81 handles the latter functions. | PMID:17903171 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2011 | High | FancB-mutant mouse embryonic stem cells show hypersensitivity to the crosslinking agent mitomycin C, increased chromosomal abnormalities, reduced sister chromatid exchanges, reduced gene targeting, reduced MMC-induced Rad51 foci, and absent MMC-induced FancD2 foci, confirming FANCB is required for FancD2 monoubiquitination/foci formation and HR repair of ICLs. | PMID:21458466 | Mutation research |
| 2015 | High | FANCB is essential for male germline function: Fancb mutant mice are infertile with primordial germ cell defects and spermatogonial maintenance failure. During meiosis, FANCB localizes to sex chromosomes in an MDC1-dependent manner (MDC1 binds γH2AX to initiate chromosome-wide silencing), is required for FANCD2 localization during meiosis, and regulates H3K9 methylation on sex chromosomes—loss of FANCB decreases H3K9me2 and increases H3K9me3 on sex chromosomes. | PMID:26123487 | Human molecular genetics |
| 2015 | High | Fancb-deficient mice have decreased HSC quiescence, reduced progenitor activity in vitro, and reduced repopulating capacity in vivo; Fancb-deficient bone marrow is hypersensitive to MMC and shows impaired recovery from myelotoxic stress; RNA-seq reveals altered expression of genes involved in HSC function and cell cycle regulation in Fancb-deficient HSCs. | PMID:26658157 | Scientific reports |
| 2020 | High | FANCB protein is indispensable for FANCD2 monoubiquitination (an essential step in ICL repair); FANCB missense variants show variable residual FANCD2 monoubiquitination activity that correlates with clinical severity. Aberrant splicing and transcript destabilization were associated with 2 missense variants. Biochemical reconstitution confirmed that reduced FANCD2 monoubiquitination correlates with earlier disease onset and shorter survival. | PMID:32106311 | Blood |
| 2017 | Medium | A somatic mosaic intragenic duplication of FANCB covering exon 3 introduces a premature stop codon (p.A319*) in the FANCB protein; lentiviral transduction of FANCB-null cells with the mutant construct confirmed loss of FANCD2 ubiquitination and foci formation activity, while WT FANCB restored these functions. | PMID:29193904 | Molecular genetics & genomic medicine |
| 2011 | Medium | Loss-of-function FANCB mutations (truncating) cause X-linked VACTERL-hydrocephalus syndrome in hemizygous males, and carrier females show highly skewed X-inactivation; increased chromosomal breakage on exposure to DNA cross-linking agents was confirmed in affected cells, consistent with FANCB's role in the FA pathway. | PMID:21910217 | American journal of medical genetics. Part A |

## Citations

- PMID:15611632
- PMID:17903171
- PMID:21458466
- PMID:21910217
- PMID:26123487
- PMID:26658157
- PMID:29193904
- PMID:32106311
