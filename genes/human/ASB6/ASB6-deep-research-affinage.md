---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB6
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NWX5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB6 (human)

## Current model (mechanistic narrative)

ASB6 is a substrate-recognition adaptor for CUL5/Elongin BC ubiquitin E3 ligase complexes that couples target proteins to K48-linked ubiquitination and proteasomal degradation across insulin signaling, autophagy, and lipid metabolism [PMID:15231829, PMID:34164402, PMID:37087475]. It was first defined as a constitutive partner of the APS adapter that recruits Elongins B and C to the insulin receptor signaling complex in an insulin-dependent manner and promotes APS degradation [PMID:15231829]. The CUL5-ASB6 complex ubiquitinates and degrades p62/SQSTM1, with ASB6 loss causing p62 accumulation and impaired autophagy [PMID:34164402], and mediates K48-linked ubiquitination of INSIG1 at lysines 156 and 158 to promote INSIG1 turnover and cholesterol biosynthesis, an activity recruited by the circINSIG1-encoded peptide circINSIG1-121 [PMID:37087475]. In cancer contexts ASB6 sustains stem-like properties and metastatic capacity, attenuating ER stress in oral squamous cell carcinoma [PMID:31182927], and is itself a substrate of the E3 ligase RNF41, which targets ASB6 for ubiquitination [PMID:36446779].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-9612973 Autophagy, R-HSA-1430728 Metabolism
- **partners:** CUL5, APS, ELOB, ELOC, SQSTM1, INSIG1, RNF41
- **complexes:** CUL5-ASB6 E3 ubiquitin ligase complex, Elongin BC complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | ASB6 (Asb6) interacts constitutively with the APS adapter protein (independent of insulin stimulation), recruits Elongins B and C to the insulin receptor signaling complex in an insulin-dependent manner, and promotes degradation of APS when co-expressed with Asb6; this places ASB6 as an E3 ligase adaptor coupling APS to the Elongin BC ubiquitin ligase complex downstream of the insulin receptor. | PMID:15231829 | The Journal of biological chemistry |
| 2021 | Medium | The CUL5-ASB6 complex functions as a ubiquitin E3 ligase that mediates ubiquitination and proteasomal degradation of p62/SQSTM1; depletion of CUL5 or ASB6 causes p62 accumulation, while ASB6 overexpression promotes p62 ubiquitination and degradation, inhibits cell proliferation, and impairs autophagy. | PMID:34164402 | Frontiers in cell and developmental biology |
| 2023 | Medium | The CUL5-ASB6 complex mediates K48-linked ubiquitination of INSIG1 at lysine residues 156 and 158, promoting INSIG1 degradation and cholesterol biosynthesis; this activity is recruited by the circINSIG1-encoded peptide circINSIG1-121. | PMID:37087475 | Molecular cancer |
| 2022 | Medium | ASB6 is ubiquitinated and degraded by RNF41 (an E3 ubiquitin ligase); ASB6 overexpression reverses the suppression of CRC stemness and metastasis mediated by circFNDC3B or RNF41, placing ASB6 downstream of the RNF41 ubiquitination pathway. | PMID:36446779 | Cell death & disease |
| 2019 | Medium | ASB6 knockdown increases ER stress levels and reduces stemness markers (Oct-4, Nanog), sphere formation, colony formation, vimentin expression, and filopodia formation, while ASB6 overexpression increases these stemness properties; ASB6 thus attenuates ER stress to sustain cancer stem-like cell properties and metastatic capacity in oral squamous cell carcinoma. | PMID:31182927 | International journal of biological sciences |
| 2008 | Low | Porcine ASB6 gene has six exons and produces an alternative transcript via intron retention; the secondary transcript, if translated, would encode a protein lacking the SOCS box domain, establishing that the SOCS box is encoded by specific exons and can be lost by alternative splicing. | PMID:18607786 | Animal biotechnology |

## Citations

- PMID:15231829
- PMID:18607786
- PMID:31182927
- PMID:34164402
- PMID:36446779
- PMID:37087475
