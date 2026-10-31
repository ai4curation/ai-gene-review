---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMH3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T2E6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMH3 (human)

## Current model (mechanistic narrative)

ARMH3 (C10orf76/DGARM) is an armadillo-repeat protein that organizes phosphatidylinositol 4-phosphate (PI4P) production at the trans-Golgi network to drive downstream membrane trafficking, lipid transport, and innate immune signaling [PMID:39580461, PMID:36921576]. It is recruited to the TGN as an effector of the active GTPase ARL5, binding GTP-bound but not inactive ARL5 in a SYS1-ARFRP1-ARL5-dependent manner [PMID:39580461]. At the Golgi, ARMH3 forms a heterodimeric complex with PI4KB by binding the PI4KB kinase linker region, an interaction modulated by PKA-dependent phosphorylation of PI4KB; this complex is required both for ARMH3 membrane recruitment and for Golgi PI4P levels [PMID:31829496]. Through this PI4KB-dependent PI4P pool, ARMH3 promotes recruitment of the oncoprotein GOLPH3 and TGN glycan modifications [PMID:39580461], and supplies a distal-Golgi PI4P pool preferentially used by the ceramide transport protein CERT for ER-to-Golgi ceramide trafficking [PMID:37195633]. In innate immunity, ARMH3 interacts with STING at the Golgi upon cGAMP stimulation and recruits PI4KB to generate PI4P that directs STING Golgi-to-endosome trafficking via AP-1 and GGA2; disruption of the ARMH3-PI4KB-PI4P axis impairs STING activation, and Armh3-deficient mice are susceptible to DNA virus challenge [PMID:36921576]. ARMH3 also interacts with the ARF GEF GBF1 and contributes to Arf1 activation, with its depletion causing Golgi fragmentation and impaired secretion [PMID:31829496, PMID:31519766], while its function is distinct from GARP-mediated endosome-to-TGN retrograde transport [PMID:39580461].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-168256 Immune System, R-HSA-1430728 Metabolism
- **partners:** PI4KB, ARL5, STING1, GBF1
- **complexes:** C10orf76-PI4KB heterodimer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | High | ARMH3 (C10orf76) binds to active (GTP-bound) but not inactive ARL5, and is recruited to the trans-Golgi network (TGN) in a SYS1-ARFRP1-ARL5-dependent manner, functioning as an ARL5 effector. | PMID:39580461 | Nature Communications |
| 2024 | High | ARMH3, recruited to the TGN via the SYS1-ARFRP1-ARL5 axis, activates PI4KB (phosphatidylinositol 4-kinase IIIβ) to generate the main pool of PI4P at the TGN, which in turn contributes to recruitment of the oncoprotein GOLPH3 and glycan modifications at the TGN. | PMID:39580461 | Nature Communications |
| 2024 | Medium | ARMH3 (DGARM/C10orf76) is not required for retrograde transport of various cargo proteins from endosomes to the TGN, distinguishing its function from that of GARP. | PMID:39580461 | Nature Communications |
| 2023 | High | Upon cGAMP stimulation, ARMH3 interacts with STING at the Golgi and recruits PI4KB to synthesize PI4P, which directs STING Golgi-to-endosome trafficking via the PI4P-binding proteins AP-1 and GGA2. | PMID:36921576 | Immunity |
| 2023 | High | Disruption of the ARMH3-PI4KB-PI4P axis impairs STING activation, while aberrantly elevated cellular PI4P leads to cGAS-independent STING activation, and Armh3fl/fl;LyzCre/Cre mice are susceptible to DNA virus challenge in vivo. | PMID:36921576 | Immunity |
| 2019 | High | C10orf76 (ARMH3) directly binds PI4KB via the kinase linker region of PI4KB, forming a heterodimeric complex whose assembly is modulated by PKA-dependent phosphorylation of PI4KB. | PMID:31829496 | EMBO Reports |
| 2019 | High | PI4KB is required for membrane recruitment of C10orf76 (ARMH3) to the Golgi, and an intact C10orf76-PI4KB complex is required for Golgi PI4P levels and replication of c10orf76-dependent enteroviruses (e.g., coxsackievirus A10). | PMID:31829496 | EMBO Reports |
| 2019 | Medium | C10orf76 (ARMH3) contributes to proper Arf1 activation at the Golgi, providing a putative mechanism for the C10orf76-dependent increase in PI4P levels. | PMID:31829496 | EMBO Reports |
| 2019 | High | C10orf76 (ARMH3) interacts with GBF1 (a Golgi-localized ARF guanine nucleotide exchange factor) and rapidly cycles on and off GBF1-positive Golgi structures; its depletion causes Golgi fragmentation, alters GBF1 recruitment, and impairs secretion. | PMID:31519766 | Molecular & Cellular Proteomics |
| 2023 | High | C10orf76 (ARMH3) localizes predominantly at distal Golgi regions and, together with PI4KB, generates a PI4P pool that is preferentially utilized by the ceramide transport protein CERT for ER-to-distal-Golgi ceramide trafficking (as opposed to the PI4KB pool recruited by ACBD3). | PMID:37195633 | Journal of Cell Biology |

## Citations

- PMID:31519766
- PMID:31829496
- PMID:36921576
- PMID:37195633
- PMID:39580461
