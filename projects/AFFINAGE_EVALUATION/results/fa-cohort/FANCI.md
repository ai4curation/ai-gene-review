# FANCI (FANCI) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 43 discoveries · self-eval `win` (faith 100%) · gates passed.

## Agreement (brief)

Both sources converge on FANCI's core biology and the AIGR review already captures it:
- FANCI is the obligate ID2-clamp partner of FANCD2, monoubiquitinated on Lys523 by
  FANCL/UBE2T, mutually interdependent with FANCD2 monoubiquitination (AIGR
  `GO:0031398`, `GO:1990391`; core_functions).
- DNA binding with preference for branched structures; the monoubiquitinated ID2
  complex becomes a closed sliding clamp encircling dsDNA (AIGR NEW `GO:0003677`;
  PMID:32269332).
- ATR S/TQ-cluster phosphorylation acts as the activating molecular switch (AIGR
  description + `GO:0031398`; PMID:18931676).
- Interstrand cross-link repair as the defining process; nucleoplasm/chromatin
  localization (AIGR `GO:0036297`, `GO:0000785`, `GO:0005654`).
- Downstream partners FAN1 and POLN captured as non-core interactions.

Affinage's PMID-dense narrative (43 citations) is a strong, accurate literature scan and
matches the curated picture on all central mechanistic points.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| GO grounding layer | `mechanism_profile` lists coarse parents: `GO:0140096` catalytic activity acting on a protein, `GO:0098772` molecular function regulator, `GO:0060090` molecular adaptor, `GO:0003723` RNA binding | Specific curated terms: `GO:0003677` DNA binding (MF), `GO:0031398`, `GO:0036297`, `GO:1990391` | AIGR right. Affinage's own note flags this layer as coarse/contradictory. FANCI is not a catalytic protein-modifying enzyme (it is the substrate/co-factor for FANCL/UBE2T); "catalytic activity acting on a protein" is wrong-branch. AIGR's DNA-binding MF is the correct defining activity. |
| Cytoplasm / membrane localization | Not asserted by Affinage (narrative is nuclear) | AIGR carries and down-scores them: cytoplasm `MARK_AS_OVER_ANNOTATED` (PMID:18445686 EML3 spindle proteomics), membrane `REMOVE` (PMID:19946888 NK membrane fraction) | AIGR right and more rigorous — it adjudicates GOA-inherited noise Affinage never surfaced. |
| RNA binding / R-loop, nucleolar rRNA | Included as discoveries (PMID:30650351, PMID:30692263) with `GO:0003723` RNA binding | Not annotated | AIGR defensibly conservative. These are real but largely FANCD2-independent, secondary functions; importing `GO:0003723` at FANCI's core level would over-annotate. Documented, not adopted. |
| RAD51 filament stabilization / fork protection | Discovery (PMID:27694619): ID complex binds RAD51, stabilizes RAD51-DNA filament, protects 5' end from FAN1 | Was absent | Partially incorporated. Well-evidenced, and FANCI's (not FANCD2's) DNA binding is explicitly required — so PMID:27694619 was added as supporting evidence for the DNA-binding MF. No clean GO BP term exists ("replication fork protection" resolves only to CC complex `GO:0031298` or the ill-fitting `GO:0031297` processing), so no new BP annotation was created. |
| PIDD1/caspase-2 apoptotic switch; dormant-origin firing; meiosis/spermatogenesis; Akt/PHLPP1; PARP1; IMPDH2 | Included as discoveries (PMID:34256011, 25843623, 34373449/31219578, 27097374, 39037758, 32021289) | Not annotated | AIGR right to exclude from core. These are context-specific or single-study over-reaches (several are cancer-cell or mouse-specific); appropriate as narrative, not as curated core GO. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:19589784 | FANCI intrinsic DNA binding (branched-structure preference); K523 monoub by UBE2T-FANCL | Added verbatim `supported_by` to the DNA-binding NEW `GO:0003677` annotation (independent primary biochemistry alongside structural PMID:32269332); reference + `reference_review` (HIGH/VERIFIED) |
| PMID:22287633 | DNA-binding-dependent stimulation of FANCD2 monoubiquitination by FANCI | Added verbatim `supported_by` to `GO:0031398` positive regulation of protein ubiquitination (IDA); reference + `reference_review` (HIGH/VERIFIED) |
| PMID:27694619 | FANCI's DNA binding explicitly required for ID2-mediated RAD51-DNA filament stabilization / fork-end protection | Added verbatim `supported_by` to the DNA-binding NEW `GO:0003677` annotation; reference + `reference_review` (MEDIUM/VERIFIED, notes no clean BP term) |

No new GO annotations (terms/qualifiers) were created; the three papers strengthen existing
core annotations. Validation remains `✓ Valid` (single expected deep-research-file warning).

## Net assessment

The AIGR review was already accurate and complete on FANCI's core biology, and is more
rigorous than Affinage on GOA-inherited localization noise (cytoplasm/membrane) and on GO
branch precision (Affinage's coarse `mechanism_profile` mislabels FANCI as a protein-acting
catalytic enzyme). Affinage's value here was surfacing well-cited primary biochemistry that
the curated review carried on a single structural reference; three of those papers were
incorporated as independent verbatim support for the DNA-binding molecular function and the
positive-regulation-of-ubiquitination process. Affinage's remaining "discoveries" (RNA/R-loop,
nucleolar rRNA, meiosis, PIDD1 apoptosis, dormant origins, cancer-cell partnerships) are
genuine literature but are secondary/context-specific and were correctly left out of core GO —
several would be over-annotations if imported at FANCI's core level.
