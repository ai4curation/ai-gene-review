---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTA1
affinage_run_date: 2026-06-09T22:02:39
uniprot_accession: P68133
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 11
citation_count: 11
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTA1 (human)

## Current model (mechanistic narrative)

ACTA1 encodes skeletal muscle alpha-actin, the predominant thin-filament protein of adult skeletal muscle sarcomeres, where it polymerizes into filaments that interact with myosin to generate contractile force and with Z-line proteins such as alpha-actinin to organize the sarcomere [PMID:16945537, PMID:23029319]. Its expression is developmentally regulated: alpha-cardiac actin predominates in fetal skeletal muscle and the heart, while ACTA1 becomes the exclusive skeletal isoform from infancy onward, accounting for the muscle-restricted phenotype of ACTA1 disease [PMID:16288873]. Dominant disease-causing mutations act through a poison-protein mechanism rather than loss of function: mutant actin misfolds, polymerizes abnormally, and aggregates into insoluble filaments and nemaline/intranuclear rods [PMID:15198992], modifies the actin-actin interface to block strong myosin cross-bridge binding [PMID:23029319, PMID:27112274], and in some cases stabilizes tropomyosin in the switched-off state without disrupting sarcomere ultrastructure [PMID:17387733]. Disease severity tracks directly with mutant protein load, and raising the wild-type-to-mutant ratio—including by substituting cardiac alpha-actin—is therapeutic in mouse models [PMID:21303860, PMID:23736297]. Beyond contraction, ACTA1 deficiency is associated with mislocalization of nuclear envelope and LINC-complex proteins and abnormal nuclear shape in patient muscle [PMID:35810298].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-397014 Muscle contraction
- **partners:** MYH, ACTN2, TPM, LMNA, SYNE1, SYNE2
- **complexes:** sarcomere thin filament

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | Mutant ACTA1 proteins (e.g., V163L, V163M, R183G) show abnormal folding, altered polymerization capacity, and aggregation when expressed in C2C12 myoblasts; mutant actin isoforms were detected in insoluble actin filaments from patient muscle, providing direct evidence for a dominant-negative mechanism where mutant actin disrupts normal filament assembly. | PMID:15198992 | Human molecular genetics |
| 2005 | Medium | Alpha-cardiac actin is the predominant sarcomeric isoform in human donor hearts and early fetal skeletal muscle, while alpha-skeletal actin (ACTA1) becomes the exclusive isoform in skeletal muscle from infancy through adulthood; this differential expression was established by direct protein quantification and explains the absence of cardiac involvement in ACTA1 nemaline myopathy. | PMID:16288873 | Neuromuscular disorders : NMD |
| 2006 | Medium | The ACTA1 K336E mutation reduces the sliding speed of actin in an in vitro motility assay by ~13% and reduces the affinity of actin for the Z-line protein alpha-actinin by 10-fold, establishing a specific functional defect in sarcomere protein interactions. | PMID:16945537 | Neuromuscular disorders : NMD |
| 2007 | High | ACTA1 CFTD mutations D292V and P332S cause muscle weakness through disruption of sarcomere function rather than structure: D292V abnormally stabilizes tropomyosin in the 'switched-off' position (as shown by in vitro motility), while both mutations are associated with normal sarcomeric ultrastructure, distinguishing them mechanistically from nemaline myopathy mutations. | PMID:17387733 | Annals of neurology |
| 2011 | High | In transgenic mice expressing ACTA1 D286G, skeletal muscles contain ~25% mutant protein and are significantly weaker; when mutant protein load is increased to ~50% (by crossing with Acta1+/- knockouts), mice develop severe nemaline bodies, actin accumulations, and widespread sarcomeric disarray with early lethality, establishing that mutant ACTA1 protein load directly determines disease severity. | PMID:21303860 | Brain : a journal of neurology |
| 2012 | Medium | The ACTA1 D286G mutation acts as a 'poison-protein' by modifying the actin-actin interface (as computed by molecular energy state calculations), preventing proper myosin cross-bridge binding in the strong-binding state, thereby reducing force-generating capacity in single permeabilized muscle fibers. | PMID:23029319 | PloS one |
| 2013 | High | Transgenic over-expression of cardiac alpha-actin in postnatal skeletal muscle of ACTA1(D286G).Acta1+/- mice reduced lethality before 30 days from ~59% to ~12%, demonstrating that cardiac alpha-actin can functionally substitute for mutant skeletal alpha-actin and that increasing the ratio of wild-type to mutant actin is therapeutic for dominant ACTA1 disease. | PMID:23736297 | Human molecular genetics |
| 2016 | Medium | The ACTA1 H40Y mutation severely disrupts the DNase I-binding-loop structure and actin filament organization, causes mutant actin monomers to form distinctive homopolymers with abnormally high stiffness, and prevents proper myosin binding, establishing the molecular basis of contractile dysfunction. | PMID:27112274 | Biochimica et biophysica acta |
| 2022 | Medium | Severe ACTA1-related nemaline myopathy patients show abnormal localization of nuclear envelope proteins lamin A/C, Nesprin-1, and Nesprin-2, with enlarged perinuclear space on electron microscopy, indicating that skeletal muscle alpha-actin contributes to maintaining nuclear shape and LINC complex integrity. | PMID:35810298 | Acta neuropathologica communications |
| 2006 | Low | The Val163Met ACTA1 mutation (causing intranuclear rod myopathy) introduces substitution at a residue adjacent to the nuclear export signal of actin, providing a structural basis for intranuclear rod formation; this was supported by the finding in [15198992] that V163L and V163M mutant actin accumulates in the nucleus in C2C12 transfection models. | PMID:16427282 | Neuromuscular disorders : NMD |
| 2013 | Medium | In the ACTA1 H40Y mouse model, skeletal muscle shows reduced maximal force (-40% absolute, -25% specific), improved fatigue resistance (+40%), and increased energy cost of contraction as measured by 31P-MRS, indicating impaired cross-bridge cycling and potentially altered mitochondrial function or actomyosin interaction kinetics. | PMID:23613869 | PloS one |

## Citations

- PMID:15198992
- PMID:16288873
- PMID:16427282
- PMID:16945537
- PMID:17387733
- PMID:21303860
- PMID:23029319
- PMID:23613869
- PMID:23736297
- PMID:27112274
- PMID:35810298
