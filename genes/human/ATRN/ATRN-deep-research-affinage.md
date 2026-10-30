---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATRN
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O75882
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 10
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATRN (human)

## Current model (mechanistic narrative)

ATRN (Attractin) is a multidomain glycoprotein produced as functionally distinct secreted and membrane-bound isoforms whose roles span immune cell interaction, CNS myelination, and receptor regulation [PMID:10811918, PMID:11444801]. The two isoforms arise by alternative splicing: a soluble form terminating at a LINE-1 retrotransposon-derived exon, and a membrane form that splices over this exon to add transmembrane and cytoplasmic domains [PMID:10811918]; activated leukocytes first display the membrane isoform on the surface and then release the soluble form [PMID:10811918]. The secreted protein, a 175 kDa serum glycoprotein with DPPIV enzymatic activity, is released by activated T lymphocytes and drives monocyte spreading, T cell clustering, and co-stimulation of T-cell antigen responses [PMID:9736737, PMID:8596018]. The membrane isoform acts as a transmembrane adapter, recruiting the E3 ubiquitin ligase MGRN1 through MGRN1's RING domain to the melanocortin receptors MC1R and MC4R, enabling their ubiquitination and degradation [PMID:bio_10.1101_2025.03.25.645338]. Loss-of-function mutations establish ATRN as essential for CNS integrity: mouse mutants develop spongiform vacuolization across the brain and spinal cord [PMID:11444801], and a homozygous human splice-site mutation causes hypomyelinating leukodystrophy [PMID:28493104]. In zebrafish embryos, Atrn binds the demethylase Alkbh4 and is required for actomyosin contractile ring formation during epiboly [PMID:28924386], and transmembrane ATRN additionally serves as a shared cell-surface entry receptor for a modular family of bacterial exotoxins [PMID:bio_10.1101_2025.10.08.681221].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0001618 virus receptor activity, GO:0016787 hydrolase activity
- **localization:** GO:0005886 plasma membrane, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-392499 Metabolism of proteins
- **partners:** MGRN1, MC1R, MC4R, ALKBH4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | Medium | Attractin (DPPT-L/ATRN) is a 175 kDa serum glycoprotein secreted by activated T lymphocytes that mediates monocyte spreading and the clustering of non-proliferating T lymphocytes around those monocytes, establishing its role in modulating immune cell interactions. | PMID:9736737 | Proceedings of the National Academy of Sciences of the United States of America |
| 1998 | Medium | Attractin protein contains a putative serine protease catalytic serine, four EGF-like motifs, a CUB domain, a C-type lectin domain, and a domain homologous to the ligand-binding region of the common gamma cytokine chain, defining its domain architecture. | PMID:9736737 | Proceedings of the National Academy of Sciences of the United States of America |
| 1996 | Medium | The 175-kDa serum form of DPPT-L (ATRN) is antigenically and biochemically distinct from the 105-kDa CD26/DPPIV, yet possesses DPPIV enzymatic activity and functions as a co-stimulatory molecule for T-cell responses to recall antigen (tetanus toxoid). | PMID:8596018 | Journal of immunology (Baltimore, Md. : 1950) |
| 2000 | High | Soluble and membrane-bound isoforms of human ATRN arise from alternative splicing: the soluble form uses 25 sequential exons with a terminal LINE-1 retrotransposon-derived exon providing a stop codon and polyadenylation signal, while the membrane form splices over this LINE-1 exon to include five additional exons encoding transmembrane and cytoplasmic domains. | PMID:10811918 | Proceedings of the National Academy of Sciences of the United States of America |
| 2000 | Medium | Activation of peripheral blood leukocytes with PHA induces strong surface expression of membrane ATRN followed by its release as soluble ATRN into the medium, establishing the sequential relationship between membrane and secreted isoforms during an inflammatory response. | PMID:10811918 | Proceedings of the National Academy of Sciences of the United States of America |
| 2001 | High | Loss-of-function mutations in the mouse Atrn (mahogany) gene cause severe spongiform vacuolization of the cerebrum, brainstem, granular layer of cerebellum, and spinal cord, establishing ATRN as required for CNS integrity independent of its coat-color and energy-metabolism roles. | PMID:11444801 | Journal of neuropathology and experimental neurology |
| 2017 | Medium | A homozygous splice-site mutation (c.3068+5G>A) in ATRN causing intronic sequence insertion and premature termination results in hypomyelinating leukodystrophy in humans, confirming that ATRN plays a critical role in central nervous system myelination. | PMID:28493104 | Neurogenetics |
| 2017 | Medium | Zebrafish maternal Atrn depletion causes severe epiboly defects by impairing actomyosin contractile ring formation; Atrn was identified as a binding partner of the demethylase Alkbh4 by yeast two-hybrid assay, and Atrn preferentially interacts with the active form of Alkbh4 to cooperatively regulate actin demethylation and actomyosin formation. | PMID:28924386 | International journal of biological sciences |
| 2025 | Medium | Transmembrane ATRN (Attractin) functions as the cell-surface receptor for the bacterial exotoxin Nigritoxin (Ntx) from Vibrio, mediating toxin entry into cells; this ATRN-targeting entry domain is shared by at least two other toxins with unrelated effector domains (Rho-GTPase AMPylation and actin-targeting/proteolysis), establishing ATRN as a common entry receptor for a modular toxin family. | PMID:bio_10.1101_2025.10.08.681221 | bioRxiv |
| 2025 | Medium | Transmembrane ATRN acts as an adapter that recruits the E3 ubiquitin ligase MGRN1 (via interaction with MGRN1's RING domain) to melanocortin receptors MC1R and MC4R, enabling MGRN1-dependent ubiquitination and degradation of these receptors at the cell surface; loss of MGRN1 increases surface/ciliary MC4R in fibroblasts and elevates MC1R levels in melanocytes, enhancing eumelanin production. | PMID:bio_10.1101_2025.03.25.645338 | bioRxiv |

## Citations

- PMID:10811918
- PMID:11444801
- PMID:28493104
- PMID:28924386
- PMID:8596018
- PMID:9736737
- PMID:bio_10.1101_2025.03.25.645338
- PMID:bio_10.1101_2025.10.08.681221
