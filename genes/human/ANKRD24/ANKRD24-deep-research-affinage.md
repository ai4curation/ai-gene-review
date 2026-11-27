---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD24
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8TF21
self_evaluation_pairwise: tie
faith_pct: 100.0
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

# Affinage mechanistic annotation for ANKRD24 (human)

## Current model (mechanistic narrative)

ANKRD24 is an ankyrin-repeat protein that organizes the stereocilia rootlet architecture of inner ear hair cells, where it is required for normal mechanosensory function and hearing [PMID:35175278]. It concentrates at the stereocilia insertion point, forming a ring at the junction between the lower and upper rootlets, and surrounds and binds TRIOBP-5 within the lower rootlet where TRIOBP-5 bundles rootlet F-actin; the two proteins are mutually dependent for correct localization, as TRIOBP-5 is mislocalized in Ankrd24-null hair cells, ANKRD24 fails to localize to rootlets without TRIOBP-5, and exogenous TRIOBP-5 restores endogenous ANKRD24 to rootlets [PMID:35175278]. By bridging the apical plasma membrane to the lower rootlet, ANKRD24 maintains TRIOBP-5 distribution, and its loss produces progressive hearing loss, impaired recovery after noise damage, and increased mechanical vulnerability of the hair bundle [PMID:35175278]; positioning of ANKRD24 and TRIOBP-5 at this rootlet pivot point depends on the upstream factor TPRN/taperin [PMID:40471101]. A homozygous frameshift variant in ANKRD24 segregates with autosomal recessive nonsyndromic sensorineural hearing loss in a consanguineous family, implicating the gene in human deafness [PMID:39434538]. Independently of its rootlet role, ANKRD24 is a transcriptional target of HMGCS2 and acts in a ketone body-linked autophagic pathway, where its silencing reduces LAMP1 and LC3-II and diminishes HMGCS2-induced autophagic clearance of Tau/pTau [PMID:36442191].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-9612973 Autophagy, R-HSA-9709957 Sensory Perception
- **partners:** TRIOBP, TPRN
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | High | ANKRD24 concentrates at the stereocilia insertion point in hair cells, forming a ring at the junction between the lower and upper rootlets, and surrounds and binds TRIOBP-5 within the lower rootlet, where TRIOBP-5 bundles rootlet F-actin. TRIOBP-5 is mislocalized in Ankrd24KO/KO hair cells, and ANKRD24 no longer localizes with rootlets in mice lacking TRIOBP-5; exogenous DsRed-TRIOBP-5 restores endogenous ANKRD24 to rootlets, establishing mutual dependence for correct localization. | PMID:35175278 | The Journal of cell biology |
| 2022 | High | ANKRD24 bridges the apical plasma membrane with the lower stereocilia rootlet to maintain a normal distribution of TRIOBP-5. Loss of ANKRD24 (Ankrd24KO/KO mice) results in progressive hearing loss, diminished recovery of auditory function after noise damage, and increased susceptibility to overstimulation of the hair bundle. | PMID:35175278 | The Journal of cell biology |
| 2023 | Medium | ANKRD24 is identified as a transcriptional target of HMGCS2 via RNA sequencing, and silencing of ANKRD24 reduces autophagy markers LAMP1 and LC3-II, alters autophagic vacuole formation, and diminishes HMGCS2-induced autophagic clearance of Tau/pTau, placing ANKRD24 downstream of HMGCS2 in a ketone body-linked autophagic pathway. | PMID:36442191 | Journal of Alzheimer's disease : JAD |
| 2025 | Medium | In TPRN (taperin)-deficient mice, TRIOBP-5 and ANKRD24 are progressively lost from mechanosensory stereocilia rows starting postnatally, indicating that TPRN is upstream of ANKRD24 (and TRIOBP-5) localization at the stereocilia rootlet pivot point. | PMID:40471101 | The Journal of cell biology |
| 2024 | Medium | A homozygous frameshift variant in ANKRD24 (c.1934_1937del; p.Thr645Lysfs*52) segregates with autosomal recessive nonsyndromic sensorineural hearing loss in a consanguineous human family, implicating ANKRD24 for the first time in human hearing loss. | PMID:39434538 | Clinical genetics |

## Citations

- PMID:35175278
- PMID:36442191
- PMID:39434538
- PMID:40471101
