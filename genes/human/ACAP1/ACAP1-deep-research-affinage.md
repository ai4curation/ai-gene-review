---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACAP1
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q15027
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACAP1 (human)

## Current model (mechanistic narrative)

ACAP1 is an ARF6 GTPase-activating protein that operates as a coat component of the endocytic recycling pathway, sorting cargo from endosomes back to the plasma membrane to control processes such as cell migration and glucose homeostasis [PMID:17664335]. It assembles into a novel ARF6-regulated clathrin coat complex that drives stimulation-dependent recycling of integrin beta1 and insulin-stimulated recycling of Glut4 [PMID:17664335], and it localizes to a tubular recycling endosome distinct from the ARAP2/APPL1-positive compartment, with the two ARF6 GAPs exerting opposing effects on integrin internalization and focal adhesions [PMID:25225293]. Cargo engagement is switch-regulated: Akt phosphorylation of ACAP1 relieves a localized autoinhibition to enhance binding of a defined recycling sorting signal in the integrin beta1 cytoplasmic tail, coupling recycling to upstream signaling [PMID:16256741, PMID:22645133]. Its membrane-deforming activity arises from an unconventional division of labor between adjacent domains, in which the PH domain mediates membrane binding and curvature generation while the BAR domain mediates clustering of ACAP1 molecules into a lattice that deforms the membrane [PMID:25284369]. Beyond integrin and Glut4 trafficking, ACAP1 acts in a Rab10-ACAP1-Arf6 cascade that inactivates Arf6 to arrest the M4 muscarinic acetylcholine receptor in early endosomes [PMID:36917255], and it scaffolds a PTPN9-FGFR2 complex to facilitate FGFR2 dephosphorylation, a function requiring its PH and Arf-GAP domains [PMID:37505213].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008289 lipid binding, GO:0060090 molecular adaptor activity, GO:0005198 structural molecule activity
- **localization:** GO:0005768 endosome, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization, R-HSA-162582 Signal Transduction
- **partners:** ARF6, ITGB1, GULP1, RAB10, PTPN9, FGFR2
- **complexes:** ARF6-regulated clathrin coat complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | High | ACAP1 participates in stimulation-dependent recycling of integrin beta1 to control cell migration, and this role requires phosphorylation of ACAP1 by Akt, which is regulated by a canonical signaling pathway. Disrupting ACAP1 or Akt activities, or their assembly with endosomal beta1, inhibits beta1 recycling and cell migration. | PMID:16256741 | Developmental Cell |
| 2007 | High | ACAP1, an ARF6 GAP, is a component of a novel clathrin coat complex regulated by ARF6 that mediates endocytic recycling of integrin (stimulation-dependent, for cell migration) and Glut4 (insulin-stimulated, for glucose homeostasis). | PMID:17664335 | The Journal of Cell Biology |
| 2007 | Medium | GULP/CED-6 regulates ACAP1 and Arf6 signaling: GULP binds directly to GDP-bound Arf6 via its PTB domain, associates with ACAP1 at endogenous levels, reverses Arf6-GTP decrease induced by ACAP1, counters ACAP1-mediated inhibition of cell migration, and forms a tripartite complex with ACAP1 and GDP-bound Arf6, suggesting sequestration of ACAP1 as one mechanism. | PMID:17398097 | Current Biology |
| 2012 | High | Akt phosphorylation of ACAP1 relieves a localized autoinhibitory mechanism to enhance cargo binding. A critical sequence in the cytoplasmic domain of integrin beta1 recognized by ACAP1 was defined and shown to act as a recycling sorting signal. Structural and modeling studies support phosphorylation-relieved autoinhibition as the regulatory mechanism. | PMID:22645133 | The Journal of Biological Chemistry |
| 2014 | High | ACAP1's BAR domain cannot bind membrane or impart curvature on its own but requires its neighboring PH domain; specific residues within the PH domain mediate both membrane binding and curvature generation, while the BAR domain enables clustering of ACAP1 proteins at the membrane by interacting with BAR domains of neighboring ACAP1 molecules. | PMID:25284369 | Developmental Cell |
| 2014 | Medium | ACAP1 and ARAP2 are distinct Arf6 GAPs that define separate endosomal compartments with opposing effects: ACAP1 knockdown accelerated integrin beta1 internalization and ACAP1 overexpression reduced focal adhesions, while ARAP2 had the opposite effects. ACAP1 localizes to a tubular recycling endosome distinct from the ARAP2/APPL1-positive compartment. | PMID:25225293 | The Journal of Biological Chemistry |
| 2017 | Low | Molecular dynamics simulations revealed that the PH domain of ACAP1 has two binding pockets with preference for PIP2 lipids, and defined the orientation of PH domain relative to the BAR domain during membrane binding, providing molecular basis for protein-lipid interactions during membrane remodeling. | PMID:28092439 | The Journal of Physical Chemistry B |
| 2019 | Medium | ACAP1 dimerizes into a symmetrical structure in solution but is recruited asymmetrically to the membrane through dynamic behavior. Computational refinement and EM studies identified critical protein contacts within the ACAP1 lattice and revealed multiple stages of lattice assembly enabling membrane deformation. | PMID:31291238 | PLoS Computational Biology |
| 2023 | Medium | Rab10-GTP recruits the Arf6 GAP ACAP1 to inactivate Arf6, acting as part of a Rab10-ACAP1-Arf6 cascade that arrests M4 muscarinic acetylcholine receptor in Rab5-positive early endosomes and hinders receptor resensitization. M4 binds Rab10-GTP via the motif 386RKKRQMAA393 in the third intracellular loop; deletion of this motif causes M4 to bypass Rab10 control and switch to Rab4-facilitated fast recycling. | PMID:36917255 | Cellular and Molecular Life Sciences |
| 2023 | Medium | ACAP1 mediates the interaction between the sec14p domain of PTPN9 and FGFR2, facilitating PTPN9 dephosphorylation of FGFR2 at pY656/657. The PH and Arf-GAP domains of ACAP1 are required for this interaction. The 'YRETRRKE' motif of the sec14p domain and Y471 of PTPN9 are key residues for the sec14p-ACAP1-FGFR2 complex. | PMID:37505213 | Hepatology |

## Citations

- PMID:16256741
- PMID:17398097
- PMID:17664335
- PMID:22645133
- PMID:25225293
- PMID:25284369
- PMID:28092439
- PMID:31291238
- PMID:36917255
- PMID:37505213
