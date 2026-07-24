# BRCA2 (FANCD1) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 27 discoveries · self-eval pairwise = win, faith 100% · gates passed.

The Affinage record for BRCA2 is a strong, PMID-dense (27 citations) mechanistic narrative of the
RAD51-mediator life cycle: C-terminal DBD (three OB folds + HTH) binding ssDNA, full-length BRCA2
selectively loading RAD51 onto ssDNA over dsDNA and displacing RPA, single-molecule acceleration of
RAD51 nucleation on RPA-coated ssDNA, BRC-repeat non-equivalence, TR2 filament brace, PALB2/BRCA1
recruitment, FA-pathway/FANCD2 chromatin loading, reversed-fork protection, R-loop control,
phosphoregulation (ATM/ATR-PP2A-B56, PLK1-T207), meiotic DMC1 mediation, and metabolite-triggered
(formaldehyde/methylglyoxal) proteolysis. The AIGR review is curated, GOA-grounded, validated, and
was already the product of a careful A→Z manual pass plus a 2026-07-22 QA re-review.

## Agreement (brief)

The two sources agree on the core biology. Both center BRCA2 on homologous recombination as the
defining RAD51 mediator: ssDNA binding via the OB-fold DBD, loading/stabilizing RAD51 onto
RPA-coated resected ssDNA to build the presynaptic filament, D-loop/strand invasion, and reversed-
/stalled-fork protection from nucleolytic degradation (AIGR: GO:0003697 ACCEPT, GO:0000724 ACCEPT
across IBA/IEA/IDA/IMP, GO:0031297 ACCEPT, NEW GO:0000730 / GO:0042148, two core_functions; Affinage
narrative + PMID:12228710/20729832/36976771/29038466). Both treat nuclear/nucleoplasm/chromosome
localization, the BRCA1-PALB2-BRCA2 axis (GO:1990391 DNA repair complex), telomere and centrosome
pools, and meiotic HR (spermatogenesis, male meiosis I) as established, with the germline/meiotic and
centrosome roles demoted to non-core. Both also treat the intrinsic-HAT claim skeptically.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | `molecular_activity` = `GO:0003677 DNA binding`, `GO:0140096 catalytic activity acting on a protein`, `GO:0060090 molecular adaptor activity`, `GO:0098772 molecular function regulator activity` | Core MF is the specific `GO:0003697 ssDNA binding`; BRCA2 is not a protein-acting enzyme, adaptor, or generic regulator | **AIGR right.** Affinage's own header flags this layer as coarse/collapsed-to-parents and self-contradictory. `catalytic activity, acting on a protein` is wrong-branch (BRCA2 has no such catalytic activity); `DNA binding` is the less-specific parent of the annotated ssDNA binding. Not imported. |
| `protein binding` (GO:0005515) | Narrative leans on dozens of PPIs (RAD51, PALB2, DSS1, FANCD2, DMC1, p53, USP11, HSF2BP, MEILB2…) | ~40 IPI `protein binding` rows REMOVE'd as uninformative; interactors retained in summaries / specific-MF / complex terms | **AIGR right** per repo-wide curation policy; Affinage does not assert the generic term, so no true conflict. |
| Meiotic DMC1 mediation | Distinct, well-cited function (PMID:26976601, 31242413, 32345962) | Captured only as non-core BP terms (spermatogenesis, male meiosis I, oocyte maturation, gonad development) | **Both defensible; AIGR conservative-correct.** DMC1-mediator activity is real but germline-restricted; demoting to non-core meiotic processes is appropriate. No specific mitotic-vs-meiotic MF gap forces a new term. Left unchanged. |
| R-loop suppression / RNase H2 recruitment | Real function (PMID:30560944, 28575672, 35715464) | Not annotated | **Affinage right that it is real, but coarse/indirect for BRCA2.** Left unannotated conservatively: BRCA2's R-loop effect is via recruiting RNase H2 and via fork stability, not a demonstrated intrinsic BRCA2 MF; adding a NEW term here would over-reach on this high-quality existing review. |
| Metabolite-triggered proteolysis, PLK1/PP2A phosphoregulation | Emphasized (PMID:28575672, 38608703, 32286328, 34593815) | Regulation of BRCA2, not BRCA2's own function; not annotated as BRCA2 GO | **AIGR right to exclude.** These describe upstream regulation/degradation of BRCA2, not molecular functions/processes executed by BRCA2. Correctly out of scope. |
| HAT activity | Not asserted (Affinage does not carry the disputed intrinsic-HAT claim) | GO:0010484/0010485 UNDECIDED; negated GO:0004402 (NOT HAT) ACCEPT | **AIGR right / no conflict.** Affinage's silence corroborates skepticism toward the contested 1998 intrinsic-HAT claim. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:12228710 | ssDNA binding (GO:0003697) | Yang et al. 2002 Science crystal structure of the BRCA2 DBD-DSS1-ssDNA complex. Added verbatim `supported_by` ("demonstrate that this BRCA2 domain binds single-stranded DNA") to the GO:0003697 IBA annotation, which previously had only the falcon deep-research file + an indirect RAD51-recombination quote; reference + `reference_review` (HIGH/VERIFIED). |
| PMID:29038466 | Replication fork processing (GO:0031297) + core function 2 | Mijic et al. 2017 Nat Commun (reversed-fork protection from MRE11/PTIP/RAD52). Added verbatim `supported_by` ("protects stalled replication forks from nucleolytic degradation") to the GO:0031297 annotation and ("RAD51 nucleofilaments on regressed arms, to protect them from degradation") to the fork-protection `core_functions` entry — both previously falcon-only; reference_review HIGH/VERIFIED. |
| PMID:36976771 | RAD51 loading (GO:0000730 / GO:0000724) + core function 1 | Bell et al. 2023 PNAS single-molecule study. Added verbatim `supported_by` ("BRCA2 regulates recombination by initiating RAD51 filament formation") to the NEW GO:0000730 DNA recombinase assembly annotation and to the RAD51-loading `core_functions` entry; reference_review HIGH/VERIFIED. |

All three PMIDs fetched/cached via `fetch-pmid`; every `supporting_text` is a verbatim substring of
the cached abstract/full text (confirmed against the reference validator — the only errors reported
are the pre-existing benign offline-fetch failures for `file:`/`GO_REF`/`Reactome` references). No
new GO terms were minted: each addition strengthens an already-present, correctly-branched annotation
or core function. Zero NEW annotations were added — the review already carried NEW GO:0000730 and
GO:0042148, and the only functions Affinage surfaced beyond those (R-loop, phosphoregulation,
degradation) are either indirect/regulatory or out of scope for a BRCA2 MF/BP under a conservative bar.

## Net assessment

The AIGR review and Affinage agree on BRCA2's core RAD51-mediator/HR and fork-protection biology.
Affinage's own GO/Reactome `mechanism_profile` is coarse and in places wrong-branch (a
`catalytic activity, acting on a protein` MF BRCA2 does not possess; `DNA binding` where the review
correctly uses `ssDNA binding`) and was correctly not imported. Affinage's genuine value here was its
dense, well-anchored narrative supplying three canonical primary papers — Yang 2002 (ssDNA-binding
structure), Mijic 2017 (reversed-fork protection), and Bell 2023 (single-molecule RAD51 loading on
RPA-coated ssDNA) — that the GOA-grounded review supported only through the falcon deep-research file
or an indirect quote. These were incorporated conservatively as added references + verbatim
`supported_by` on existing annotations and core functions, with no change to any existing curation
decision and no weakening from Affinage's coarse GO layer. File remains ✓ Valid.
