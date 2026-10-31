---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARRDC5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: A6NEK1
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARRDC5 (human)

## Current model (mechanistic narrative)

ARRDC5 is a testis-enriched α-arrestin/arrestin-domain protein that functions as an essential regulator of spermiogenesis, the morphological transformation of round spermatids into mature spermatozoa [PMID:37069147]. Genetic ablation in mice produces specifically sterile males that generate low numbers of immotile, malformed sperm unable to capacitate or fertilize oocytes [PMID:37069147]. Mechanistically, ARRDC5 acts as a scaffold that organizes protein trafficking and complex assembly at multiple steps of sperm maturation: it associates with and controls the levels and localization of the head-tail coupling apparatus components NDC1 and SUN5, modulating SEC22A-dependent vesicle trafficking that anchors the sperm head to the flagellum [PMID:37997706]; it physically partners with TEX38 to drive cytoplasmic droplet biogenesis, cargo loading, and migration along the flagellum during epididymal maturation, including deposition of proteins such as TOMM40 to the mitochondrial sheath [PMID:41420860]; and it forms a complex with TEX38, CLGN, and PDILT that governs ADAM3 maturation and the ability of sperm to migrate to the oviduct [PMID:40783453]. ARRDC5 is itself a substrate of the testis-enriched palmitoyltransferase ZDHHC19, which S-palmitoylates ARRDC5 during spermatid differentiation [PMID:40030029]. Loss of ARRDC5 has downstream consequences for offspring, transmitting DNA damage to paternal pronuclei and compromising embryogenesis [PMID:41147775].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-5653656 Vesicle-mediated transport
- **partners:** TEX38, CLGN, PDILT, NDC1, SUN5, SEC22A, ZDHHC19
- **complexes:** TEX38-ARRDC5-CLGN-PDILT complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2023 | High | ARRDC5 (an α-arrestin/arrestin-domain containing protein) is essential for spermiogenesis in mice; Arrdc5 knockout males are specifically sterile, producing low numbers of immotile, malformed sperm, with defective spermiogenesis (round spermatid-to-spermatozoa transformation) and inability of epididymal sperm to capacitate and fertilize oocytes. | PMID:37069147 | Nature Communications |
| 2023 | Medium | ARRDC5 affects spermatogenesis by interacting with and influencing the levels/localization of NDC1 and SUN5 (head-tail coupling apparatus components), and may modulate SEC22A-mediated vesicle trafficking responsible for transport and localization of NDC1, SUN5, and other HTCA-related proteins that anchor the sperm head to the tail. | PMID:37997706 | Development (Cambridge, England) |
| 2024 | Low | The interactome of ARRDC5 (by affinity purification and mass spectrometry) includes multiple components of V-type ATPase, suggesting a role for ARRDC5 in V-ATPase-related processes. | PMID:38270169 | eLife |
| 2025 | High | ZDHHC19 (a testis-enriched palmitoyltransferase) palmitoylates ARRDC5, establishing S-palmitoylation as a post-translational modification of ARRDC5 during spermatid differentiation. | PMID:40030029 | Proceedings of the National Academy of Sciences of the United States of America |
| 2025 | High | ARRDC5 physically interacts with TEX38, and together they are required for cytoplasmic droplet (CD) biogenesis and migration along the sperm flagellum during epididymal maturation; in Arrdc5-/- or Tex38-/- mice, saccular element biogenesis in CDs is deficient, the CD proteome is abnormal, and migration from the neck to the flagellum does not occur. ARRDC5 and TEX38 facilitate cargo loading during CD biogenesis and deposition of proteins such as TOMM40 from the CD to the mitochondrial sheath. | PMID:41420860 | Cell Reports |
| 2025 | Medium | ARRDC5 interacts with TEX38, CLGN (calmegin), and PDILT, and this complex affects ADAM3 maturation; loss of ARRDC5 (or TEX38) results in failure of sperm to migrate to the oviduct due to impaired ADAM3 maturation. | PMID:40783453 | Communications Biology |
| 2026 | Medium | ARRDC5 is expressed specifically in the male germline and is required for normal embryogenesis; ICSI with Arrdc5-/- sperm results in significantly compromised 2-cell and blastocyst stage embryo generation, evidence of DNA damage transmission to paternal pronuclei, and abnormal organ weights in resulting offspring. | PMID:41147775 | Biology of Reproduction |

## Citations

- PMID:37069147
- PMID:37997706
- PMID:38270169
- PMID:40030029
- PMID:40783453
- PMID:41147775
- PMID:41420860
