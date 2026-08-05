# FANCF (FANCF) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 9 discoveries · self-eval pairwise = win, faith 100% · gates passed.

## Agreement (brief)

Affinage and the AIGR review agree on the core biology: FANCF is a **nuclear** subunit of
the **Fanconi anemia (FA) core complex** that drives **FANCD2 monoubiquitination** to enable
**DNA interstrand cross-link (ICL) repair**, and its molecular role is a **flexible molecular
adaptor** that bridges the FANCA:FANCG and FANCC:FANCE subcomplexes. Both cite the same
primary structural/interaction papers (PMID:11063725 nuclear core-complex membership;
PMID:15262960 flexible adaptor; PMID:17082180 Cand1-like C-terminal fold + adaptor surface).
Affinage's narrative `molecular_activity` (GO:0060090 molecular adaptor activity) and
`localization` (GO:0005634 nucleus) match the AIGR `core_functions` and localization calls.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| GO grounding depth | Coarse `mechanism_profile`: adaptor activity / nucleus / "DNA Repair" + "Reproduction" (Reactome) | Granular: GO:0060090 adaptor activity, GO:0043240 FA nuclear complex, GO:0036297 ICL repair, GO:0000785 chromatin, GO:0005654 nucleoplasm | **AIGR.** Affinage's own note concedes the profile collapses to general parents; AIGR re-grounds to specific, correctly-branched terms. Nucleus is retained but the more granular nucleoplasm/chromatin are added. |
| "Reproduction" as a FANCF function | Lists Reactome R-HSA-1474165 Reproduction as a pathway; cites Fancf-KO gonadal/ovarian-tumour phenotype (PMID:21915857) | Not annotated as a FANCF process | **AIGR.** Impaired gametogenesis/ovarian tumours in KO mice are downstream organismal consequences of genome instability, not a distinct molecular/cellular function of FANCF. The paper is incorporated as in-vivo support for the DNA-damage/ICL role, not as a reproduction annotation. |
| Transcriptional regulation of FANCF (IRF8/ICSBP up; p53→miR-30c down) | Presents PMID:19801548 and PMID:31511498 as FANCF findings | Not annotated | **AIGR.** These describe regulation *of* the FANCF gene (and chemoresistance consequences), not functions *of* the FANCF protein; annotating them to FANCF would be a category error. Correctly excluded. |
| Cancer chemoresistance / p38-JNK MAPK | PMID:22952942, PMID:23440494: FANCF silencing sensitizes tumour cells via p38/JNK | Not annotated | **AIGR.** Silencing-phenotype/pathway-crosstalk observations, not evidence FANCF enables MAPK signaling. Excluding these avoids over-annotation. |
| Plant / meiotic anti-crossover role | PMID:36652992: conserved FANCC-FANCE-FANCF subcomplex is an anti-crossover factor in Arabidopsis meiosis | Not annotated for human FANCF | **AIGR.** The meiotic anti-crossover activity is demonstrated in *Arabidopsis*; extrapolating a meiotic-recombination process term to human FANCF from a plant assay is not warranted. Conservatively excluded (subcomplex conservation is noted, but no human annotation). |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:15262960 | Flexible-adaptor role bridging FANCA:FANCG and FANCC:FANCE subcomplexes (core molecular function) | Added to `references` (relevance HIGH, VERIFIED) with verbatim `supporting_text`; attached as `supported_by` to `core_functions` (adaptor activity) and to the first GO:0005515→GO:0060090 MODIFY annotation. This is the primary experimental source for the adaptor model the review already asserted. |
| PMID:21915857 | In-vivo requirement of FANCF for FANCD2 monoubiquitination and the DNA cross-link damage response | Added to `references` (relevance MEDIUM — mouse, VERIFIED); attached as additional `supported_by` on the GO:0006974 DNA damage response annotation. Corroborates existing ICL-repair/DDR decisions; does not change any action. |

No new GO annotations were added. Affinage's remaining five citations (PMID:19801548,
22952942, 23440494, 31511498, 36652992) concern regulation of FANCF, chemoresistance
consequences, or non-human meiotic context, and are appropriately left out of the human
FANCF annotation set.

## Net assessment

Affinage's PMID-dense narrative is factually strong and fully aligned with AIGR on FANCF's
core adaptor/FA-core-complex/ICL-repair biology; its value here was surfacing the primary
flexible-adaptor paper (PMID:15262960) and the in-vivo KO paper (PMID:21915857), both now
folded in as supporting evidence for existing decisions. Its weaknesses are the coarse
GO `mechanism_profile` (which AIGR replaces with granular, correctly-branched terms) and a
tendency to blur regulation-of-FANCF, cancer-phenotype, and cross-species findings into the
gene's own function — over-reaches the conservative AIGR review correctly excludes. Net:
AIGR review is more precise and better scoped; Affinage contributed two well-evidenced
corroborating references but no defensible new function.
