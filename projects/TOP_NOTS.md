# Top-Nots: Candidate NOT Annotations from Existing Reviews

## Overview

NOT annotations (negated annotations) in GO explicitly state that a gene product does NOT have a particular function, localization, or involvement in a process. They are valuable because they:

1. Prevent propagation of incorrect IBA/IEA annotations to other species
2. Document experimentally-tested negative results
3. Correct systematic errors from domain-based prediction pipelines
4. Provide essential context for computational analyses

This project mines existing AI gene reviews to find the strongest candidates for formal NOT annotations - cases where the reviewer found strong evidence that the gene definitively does NOT have the annotated function, not merely that evidence is insufficient.

**Key distinction**: A REMOVE action means "this annotation should be removed" - but only a subset of these warrant a NOT annotation. The best NOT candidates are cases where:
- There is positive experimental evidence the gene lacks the function
- The gene has a domain that predicts an activity it demonstrably lacks (pseudo-enzyme pattern)
- The misannotation is likely to recur via automated pipelines without an explicit NOT

## Methodology

Candidates were identified by scanning all `*-ai-review.yaml` files for `action: REMOVE` or `action: MARK_AS_OVER_ANNOTATED` annotations whose review summaries contain multiple strong negative-evidence keywords (e.g., "does not have", "lacks catalytic", "pseudoenzyme", "no detectable activity", "domain lacks").

A keyword-based scoring system ranks candidates by confidence of negative evidence. Score >= 6 indicates very high confidence; score 4-5 indicates strong candidates.

## Statistics

- Total REMOVE/MARK_AS_OVER_ANNOTATED annotations across all reviews: ~6,319
- Strong NOT candidates (score >= 4): ~53
- Very strong NOT candidates (score >= 6): 11
- Already marked as `negated: true`: ~15 across all reviews
- Unique genes with strong candidates: 42

## Tier 1: Highest Confidence NOT Candidates (score >= 6)

These are the strongest cases where a domain predicts an activity that is demonstrably absent.

| Species | Gene | UniProt | Incorrect Term | Evidence | Score | Pattern |
|---------|------|---------|----------------|----------|-------|---------|
| DROME | CG6051 | Q9VB70 | `GO:0004438` phosphatidylinositol-3-phosphate phosphatase activity | IEA | 7 | FYVE domain binds PI3P but has no phosphatase activity |
| SCHPO | Epe1 | O94603 | `GO:0016491` oxidoreductase activity | IEA | 7 | JmjC pseudo-enzyme, degenerate active site |
| human | AKTIP | Q9H8T0 | `GO:0061631` ubiquitin conjugating enzyme activity | IBA | 7 | UEV domain lacks catalytic cysteine |
| human | PLD5 | Q8N7P1 | `GO:0003824` catalytic activity | IEA | 7 | Pseudoenzyme, lacks conserved HKD motifs |
| ACET2 | cipB | Q01866 | `GO:0004553` hydrolase activity, hydrolyzing O-glycosyl compounds | IEA | 6 | Dockerin domain =/= hydrolase |
| ANOGA | PGRPS1 | Q7QFK2 | `GO:0008745` N-acetylmuramoyl-L-alanine amidase activity | IBA | 6 | Non-catalytic PGRP, lacks zinc-binding residues |
| BACSU | spoVAD | P40869 | `GO:0016746` acyltransferase activity | IEA | 6 | Thiolase-like fold but no enzymatic activity |
| DROME | CG6051 | Q9VB70 | `GO:0052629` phosphatidylinositol-3,5-bisphosphate 3-phosphatase activity | IEA | 6 | Same as above, second phosphatase term |
| SCHPO | Epe1 | O94603 | `GO:0051213` dioxygenase activity | IEA | 6 | JmjC pseudo-enzyme |
| human | CHRAC1 | Q9NRG0 | `GO:0003887` DNA-directed DNA polymerase activity | IEA | 6 | Histone-fold structural protein, no catalytic activity |
| yeast | YDJ1 | P25491 | `GO:0005524` ATP binding | IEA | 6 | DnaJ/HSP40 stimulates Hsp70 ATPase but does not bind ATP itself |

## Tier 2: Strong NOT Candidates (score 4-5)

| Species | Gene | UniProt | Incorrect Term | Evidence | Score |
|---------|------|---------|----------------|----------|-------|
| ANOGA | PGRPLD | A7UTR2 | `GO:0008745` N-acetylmuramoyl-L-alanine amidase activity | IEA | 5 |
| ANOGA | PGRPS1 | Q7QFK2 | `GO:0009253` peptidoglycan catabolic process | IEA | 4 |
| ANOGA | PGRPS1 | Q7QFK2 | `GO:0008270` zinc ion binding | IEA | 4 |
| DESVH | DVU_3336 | Q725T9 | `GO:0004673` protein histidine kinase activity | IEA | 5 |
| DESVH | DVU_3336 | Q725T9 | `GO:0016301` kinase activity | IEA | 5 |
| DESVH | DVU_3336 | Q725T9 | `GO:0000155` phosphorelay sensor kinase activity | IEA | 4 |
| DESVH | DVU_3336 | Q725T9 | `GO:0016740` transferase activity | IEA | 4 |
| DESVH | rpoN | Q72BK7 | `GO:0016779` nucleotidyltransferase activity | IEA | 4 |
| DESVH | rpoN | Q72BK7 | `GO:0016740` transferase activity | IEA | 4 |
| DROME | Ccs | A1Z850 | `GO:0016491` oxidoreductase activity | IEA | 4 |
| SCHPO | Epe1 | O94603 | `GO:0046872` metal ion binding | IEA | 4 |
| SCHPO | pmp20 | O14313 | `GO:0008379` thioredoxin peroxidase activity | IEA | 4 |
| human | AIP | O00170 | `GO:0003755` peptidyl-prolyl cis-trans isomerase activity | IEA | 5 |
| human | AIP | O00170 | `GO:0003755` peptidyl-prolyl cis-trans isomerase activity | IDA | 4 |
| human | CPT1C | Q8TCG5 | `GO:0016740` transferase activity | IEA | 4 |
| human | CREB1 | P16220 | `GO:0006468` protein phosphorylation | IDA | 5 |
| human | DNAJA2 | O60884 | `GO:0005524` ATP binding | IEA | 5 |
| human | EGFR | P00533 | `GO:0004709` MAP kinase kinase kinase activity | NAS | 4 |
| human | HSPB6 | O14558 | `GO:0005212` structural constituent of eye lens | IEA | 4 |
| human | IDH3B | O43837 | `GO:0016616` oxidoreductase activity, acting on CH-OH donors | IEA | 4 |
| human | MEX3B | Q6ZN04 | `GO:0006468` protein phosphorylation | ISS | 5 |
| human | MORC3 | Q14149 | `GO:0018105` peptidyl-serine phosphorylation | IDA | 4 |
| human | PRRT1 | Q99946 | `GO:0006468` protein phosphorylation | ISS | 4 |
| human | RASA1 | P20936 | `GO:0003924` GTPase activity | TAS | 4 |
| human | SLC14A1 | Q13336 | `GO:0005372` water transmembrane transporter activity | IEA | 4 |
| human | SPR | P35270 | `GO:0008106` alcohol dehydrogenase (NADP+) activity | TAS | 4 |
| mouse | Dnaja3 | Q99M87 | `GO:0005524` ATP binding | IEA | 5 |
| mouse | Pld4 | Q497R3 | `GO:0004630` phospholipase D activity | IEA | 4 |

## Emerging Patterns

### 1. Pseudo-enzyme Pattern (Highest value for NOT annotations)

Proteins with enzyme-family domains that have lost catalytic activity. These are the strongest NOT candidates because:
- Automated pipelines will repeatedly re-annotate them
- The negative evidence is biochemically definitive
- NOT annotations prevent IBA propagation

**Examples**: Epe1 (JmjC pseudo-demethylase), PLD5 (pseudo-phospholipase D), AKTIP (pseudo-E2), AIP (pseudo-PPIase), CG6051 (pseudo-phosphatase), CPT1C (pseudo-transferase)

### 2. Domain =/= Function Pattern

Domains that serve structural/binding roles but are annotated with the catalytic activity of the domain family.
- Dockerin domains annotated as hydrolases (cipB, celX)
- Sensor domains annotated as kinases (DVU_3336)
- DnaJ domains annotated as ATP-binding (YDJ1, DNAJA2, Dnaja3)

### 3. Upstream Regulator =/= Direct Activity

Genes annotated with the activity of their downstream targets.
- EGFR annotated as MAP3K (activates RAF, the actual MAP3K)
- RASA1 annotated with GTPase activity (stimulates Ras GTPase)
- CREB1 annotated with protein phosphorylation (is phosphorylated, not a kinase)

### 4. Non-catalytic PGRP Pattern

PGRP family members that have lost amidase activity but retain peptidoglycan binding/recognition.
- PGRPS1, PGRPLD: lack conserved zinc-binding residues for amidase activity

## Relationship to Other Projects

- **CONTESTED_FUNCTION.md**: Overlaps with pseudo-enzyme cases (Epe1)
- **OVER_ANNOTATION_PATTERNS.md**: Overlaps with domain-based prediction errors
- **PAINT.md**: NOT annotations would prevent IBA propagation of these errors

## Next Steps

- [ ] Prioritize Tier 1 candidates for formal NOT annotation submission
- [ ] For each Tier 1 candidate, verify literature reference supporting the negative claim
- [ ] Add `negated: true` to confirmed candidates in review YAML files
- [ ] Identify which NOT annotations would have the highest impact on preventing IBA propagation
- [ ] Develop systematic screen for additional pseudo-enzymes across all reviewed genes
- [ ] Consider building automated detection of pseudo-enzyme motifs (degenerate active sites)

---

# STATUS

## Completed
- [x] Initial scan of all reviews for NOT annotation candidates
- [x] Keyword-based scoring and ranking
- [x] Pattern categorization

## In Progress
- [ ] Literature verification of Tier 1 candidates
- [ ] Formal NOT annotation proposals

Last updated: 2026-03-06

# NOTES

## 2026-03-06

**Project Creation**

Scanned 6,319 REMOVE/MARK_AS_OVER_ANNOTATED annotations across all gene reviews. Identified 11 very high-confidence (score >= 6) and ~42 strong (score >= 4) candidates for formal NOT annotations.

The most impactful pattern is **pseudo-enzymes**: proteins with enzyme-family domains that have demonstrably lost catalytic activity. These are particularly valuable NOT annotations because automated pipelines (InterPro2GO, IBA) will repeatedly re-annotate them without explicit NOT annotations to prevent propagation.

Key insight: The DnaJ/HSP40 ATP binding pattern (YDJ1, DNAJA2, Dnaja3, DNAJA4) represents a systematic class error worth addressing at the pipeline level - DnaJ proteins stimulate HSP70 ATPase but do not themselves bind ATP.
