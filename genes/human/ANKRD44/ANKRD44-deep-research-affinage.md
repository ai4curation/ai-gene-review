---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD44
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8N8A2
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 5
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD44 (human)

## Current model (mechanistic narrative)

ANKRD44 is an ankyrin-repeat scaffold subunit of the protein phosphatase 6 (PP6) holoenzyme, one of three interchangeable ankyrin subunits (with ANKRD28 and ANKRD52) that assemble with the PP6 catalytic subunit and a SAPS-domain regulatory subunit (PP6R1–R3) into a >440 kDa heterotrimer specific to PP6 rather than PP2A or PP4 [PMID:18186651, PMID:39014521]. Within this complex, PP6R1 serves as the bridging scaffold, using a C-terminal region to recruit the ankyrin subunit through a site distinct from its PP6 catalytic-binding region [PMID:18186651]. Functionally, the PP6–PP6R1–ankyrin complex restrains TNFα-induced degradation of IκBε, positioning ANKRD44 as a negative regulator of NF-κB signaling [PMID:18186651]. Consistent with this role, ANKRD44 loss in HER2+ breast cancer cells drives constitutive NF-κB activation through the TAK1/AKT axis, increased glycolysis, and partial trastuzumab resistance [PMID:31297336]. ANKRD44 is itself a direct target of miR-133a-3p, and its expression promotes osteogenic differentiation of bone marrow mesenchymal stem cells [PMID:34350837].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** PPP6C, PPP6R1, PPP6R3
- **complexes:** PP6 holoenzyme (PP6c–PP6R1/R3–ANKRD44 heterotrimer)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | High | ANKRD44 (along with Ankrd28 and Ankrd52) was identified as an ankyrin repeat subunit of the PP6 holoenzyme complex. Tagged Ankrd28 (the closest characterized paralog used as proxy) coprecipitated with PP6 catalytic subunit but not PP2A or PP4, and with SAPS domain subunits PP6R1 and PP6R3. The C-terminal region of PP6R1 was sufficient to coprecipitate the ankyrin subunit but not PP6 itself, establishing PP6R1 as a scaffold with separate binding regions for PP6 and the ankyrin repeat subunit. Endogenous PP6 holoenzymes containing PP6R1, PP6R3, and Ankrd28 eluted at >440 kDa from Superose 12, consistent with a heterotrimer. | PMID:18186651 | Biochemistry |
| 2008 | Medium | Knockdown of PP6R1 or Ankrd28 (but not PP6R3) produced equivalent enhancement of IκBε degradation in response to TNFα, placing the PP6–PP6R1–Ankrd28/ANKRD44 complex upstream of IκBε stability in the NF-κB pathway. | PMID:18186651 | Biochemistry |
| 2024 | Medium | PP6 functions as a heterotrimer composed of PP6c catalytic subunit, a regulatory subunit (PP6R1–3), and a scaffold subunit (ANKRD28, ANKRD44, or ANKRD52). The PP6c–PP6R3 complex specifically regulates cancer stem cell (CSC) marker expression in colorectal cancer cells, and PP6c knockdown decreased colony-forming ability and in vivo proliferation. | PMID:39014521 | Cancer science |
| 2019 | Medium | Silencing of ANKRD44 in the HER2+ breast cancer cell line BT474 produced partial resistance to trastuzumab, constitutive activation of NF-κB via the TAK1/AKT pathway, increased glycolysis (evidenced by LDHB upregulation), and increased TROP2 expression. | PMID:31297336 | Frontiers in oncology |
| 2021 | Medium | miR-133a-3p directly targets the ANKRD44 3′UTR (validated by dual luciferase assay) and negatively regulates ANKRD44 expression. Overexpression of ANKRD44 rescued the anti-osteogenic effects of miR-133a-3p in bone marrow mesenchymal stem cells, placing ANKRD44 downstream of miR-133a-3p in the osteogenic differentiation pathway. | PMID:34350837 | General physiology and biophysics |

## Citations

- PMID:18186651
- PMID:31297336
- PMID:34350837
- PMID:39014521
