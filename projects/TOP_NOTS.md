---
species: [human, mouse, yeast, SCHPO, DROME, ANOGA, ACET2, BACSU, DESVH, ECOLI, METEA, METTP, PSEAE, PSEPK, SALTY, CANGA, CLOCL, ARATH, worm]
---
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

Candidates were identified by scanning all `*-ai-review.yaml` files for `action: REMOVE` or `action: MARK_AS_OVER_ANNOTATED` annotations whose review summaries contain multiple strong negative-evidence keywords (e.g., "does not have", "lacks catalytic", "pseudoenzyme", "no detectable activity", "domain lacks", "misannotation", "does not catalyze", "no intrinsic").

A keyword-based scoring system ranks candidates by confidence of negative evidence. Score >= 6 indicates very high confidence; score 4-5 indicates strong candidates; score 3 indicates moderate candidates worth manual review.

## Statistics

- Total REMOVE/MARK_AS_OVER_ANNOTATED annotations across all reviews: ~6,319
- NOT candidates (score >= 3): 250 across 19 species
- Strong NOT candidates (score >= 4): 115
- Very strong NOT candidates (score >= 6): 22
- Already marked as `negated: true`: ~15 across all reviews

## Tier 1: Highest Confidence NOT Candidates (score >= 6)

These are the strongest cases where a domain predicts an activity that is demonstrably absent.

| Species | Gene | UniProt | Incorrect Term | Evidence | Score | Pattern |
|---------|------|---------|----------------|----------|-------|---------|
| DROME | CG6051 | Q9VB70 | `GO:0004438` phosphatidylinositol-3-phosphate phosphatase activity | IEA | 10 | FYVE domain binds PI3P but has no phosphatase activity |
| DROME | CG6051 | Q9VB70 | `GO:0052629` phosphatidylinositol-3,5-bisphosphate 3-phosphatase activity | IEA | 9 | Same gene, second phosphatase term |
| human | MEX3B | Q6ZN04 | `GO:0006468` protein phosphorylation | ISS | 9 | RNA-binding/E3 ligase, NOT a kinase |
| ANOGA | PGRPS1 | Q7QFK2 | `GO:0008745` N-acetylmuramoyl-L-alanine amidase activity | IBA | 7 | Non-catalytic PGRP, lacks zinc-binding residues |
| BACSU | spoVAD | P40869 | `GO:0016746` acyltransferase activity | IEA | 7 | Thiolase-like fold but no enzymatic activity |
| SCHPO | Epe1 | O94603 | `GO:0016491` oxidoreductase activity | IEA | 7 | JmjC pseudo-enzyme, degenerate active site |
| human | AKTIP | Q9H8T0 | `GO:0061631` ubiquitin conjugating enzyme activity | IBA | 7 | UEV domain lacks catalytic cysteine |
| human | CHRAC1 | Q9NRG0 | `GO:0003887` DNA-directed DNA polymerase activity | IEA | 7 | Histone-fold structural protein, no catalytic activity |
| human | PLD5 | Q8N7P1 | `GO:0003824` catalytic activity | IEA | 7 | Pseudoenzyme, lacks conserved HKD motifs |
| yeast | YDJ1 | P25491 | `GO:0005524` ATP binding | IEA | 7 | DnaJ/HSP40 stimulates Hsp70 ATPase but does not bind ATP itself |
| ACET2 | cipB | Q01866 | `GO:0004553` hydrolase activity, hydrolyzing O-glycosyl compounds | IEA | 6 | Dockerin domain =/= hydrolase |
| SCHPO | Epe1 | O94603 | `GO:0051213` dioxygenase activity | IEA | 6 | JmjC pseudo-enzyme |
| human | CREB1 | P16220 | `GO:0006468` protein phosphorylation | IDA | 6 | Is phosphorylated BY kinases, not itself a kinase |
| human | DNAJA4 | Q8WW22 | `GO:0005524` ATP binding | IEA | 6 | DnaJ/HSP40, same pattern as YDJ1 |
| human | GMFB | P60983 | `GO:0006468` protein phosphorylation | TAS | 6 | Glia maturation factor, not a kinase |
| human | ILF3 | Q12906 | `GO:0006468` protein phosphorylation | IDA | 6 | dsRNA-binding protein, not a kinase |
| human | MEX3B | Q6ZN04 | `GO:0046777` protein autophosphorylation | ISS | 6 | Same gene, second phosphorylation term |
| human | PRRT1 | Q99946 | `GO:0006468` protein phosphorylation | ISS | 6 | SynDIG4, regulates phosphorylation of GRIA1 but is not a kinase |
| human | RASA1 | P20936 | `GO:0003924` GTPase activity | TAS | 6 | Stimulates Ras GTPase, has no intrinsic GTPase activity |
| human | SURF1 | Q15526 | `GO:1902600` proton transmembrane transport | IEA | 6 | Assembly factor, not itself a proton transporter |
| human | SURF1 | Q15526 | `GO:0004129` cytochrome-c oxidase activity | IEA | 6 | Assembly factor for CIV, does not have CcO activity itself |
| yeast | ATP10 | P18496 | `GO:0051082` unfolded protein binding | IPI | 6 | Assembly factor for ATP synthase, not a chaperone |

## Tier 2: Strong NOT Candidates (score 4-5)

### Pseudo-enzymes and Wrong Catalytic Activity

| Species | Gene | UniProt | Incorrect Term | Evidence | Score |
|---------|------|---------|----------------|----------|-------|
| ACET2 | cipA | Q06851 | `GO:0004553` hydrolase activity, hydrolyzing O-glycosyl compounds | IEA | 5 |
| ANOGA | PGRPLD | A7UTR2 | `GO:0008745` N-acetylmuramoyl-L-alanine amidase activity | IEA | 5 |
| BACSU | fliY | P24073 | `GO:0003774` cytoskeletal motor activity | IEA | 5 |
| DESVH | DVU_3336 | Q725T9 | `GO:0004673` protein histidine kinase activity | IEA | 5 |
| DESVH | DVU_3336 | Q725T9 | `GO:0016301` kinase activity | IEA | 5 |
| DESVH | rpoN | Q72BK7 | `GO:0016779` nucleotidyltransferase activity | IEA | 5 |
| DESVH | rpoN | Q72BK7 | `GO:0016740` transferase activity | IEA | 5 |
| DROME | CG6051 | Q9VB70 | `GO:0004721` phosphoprotein phosphatase activity | IEA | 5 |
| DROME | CG6051 | Q9VB70 | `GO:0046856` phosphatidylinositol dephosphorylation | IEA | 5 |
| DROME | Ccs | A1Z850 | `GO:0016491` oxidoreductase activity | IEA | 5 |
| SALTY | slrP | Q8ZQQ2 | `GO:0051082` unfolded protein binding | IPI | 5 |
| human | ADM2 | Q7Z4H4 | `GO:0006468` protein phosphorylation | IDA | 5 |
| human | AIP | O00170 | `GO:0003755` peptidyl-prolyl cis-trans isomerase activity | IEA | 5 |
| human | BIRC6 | Q9NR09 | `GO:0006468` protein phosphorylation | TAS | 5 |
| human | CHRAC1 | Q9NRG0 | `GO:0016740` transferase activity | IEA | 5 |
| human | CHRAC1 | Q9NRG0 | `GO:0003887` DNA-directed DNA polymerase activity | NAS | 5 |
| human | CTBP1 | Q13363 | `GO:0006468` protein phosphorylation | TAS | 5 |
| human | DNAJA2 | O60884 | `GO:0005524` ATP binding | IEA | 5 |
| human | EGFR | P00533 | `GO:0004709` MAP kinase kinase kinase activity | NAS | 5 |
| human | IDH3B | O43837 | `GO:0016616` oxidoreductase activity, acting on CH-OH donors | IEA | 5 |
| human | LIPE | Q05469 | `GO:0006468` protein phosphorylation | TAS | 5 |
| human | MORC3 | Q14149 | `GO:0018105` peptidyl-serine phosphorylation | IDA | 5 |
| human | PICK1 | Q9NRD5 | `GO:0006468` protein phosphorylation | ISS | 5 |
| human | PIWIL1 | Q96J94 | `GO:0003729` mRNA binding | IEA | 5 |
| human | RARA | P10276 | `GO:0006468` protein phosphorylation | IMP | 5 |
| human | RUNX3 | Q13761 | `GO:0006468` protein phosphorylation | IDA | 5 |
| human | SLC3A2 | P08195 | `GO:0005975` carbohydrate metabolic process | IEA | 5 |
| mouse | Dnaja3 | Q99M87 | `GO:0005524` ATP binding | IEA | 5 |
| yeast | HST1 | P50111 | `GO:0004864` protein phosphatase inhibitor activity | IMP | 5 |

### Wrong Binding, Localization, and Process (score 4-5)

| Species | Gene | UniProt | Incorrect Term | Evidence | Score |
|---------|------|---------|----------------|----------|-------|
| ANOGA | PGRPS1 | Q7QFK2 | `GO:0008270` zinc ion binding | IEA | 4 |
| ANOGA | PGRPS1 | Q7QFK2 | `GO:0009253` peptidoglycan catabolic process | IEA | 4 |
| CLOCL | cbpA | P38058 | `GO:0030245` cellulose catabolic process | IEA | 4 |
| CLOCL | hbpA | Q9RGE7 | `GO:0000272` polysaccharide catabolic process | IEA | 4 |
| DESVH | DVU_3335 | Q725U0 | `GO:0006355` regulation of DNA-templated transcription | IEA | 4 |
| DESVH | DVU_3336 | Q725T9 | `GO:0000155` phosphorelay sensor kinase activity | IEA | 4 |
| DESVH | DVU_3336 | Q725T9 | `GO:0016740` transferase activity | IEA | 4 |
| DESVH | DVU_3336 | Q725T9 | `GO:0034220` monoatomic ion transmembrane transport | IEA | 4 |
| DESVH | kdpC | Q725T8 | `GO:0005524` ATP binding | IEA | 4 |
| DESVH | kdpC | Q725T8 | `GO:0016787` hydrolase activity | IEA | 4 |
| DROME | Ccs | A1Z850 | `GO:0019430` removal of superoxide radicals | IEA | 4 |
| DROME | Ccs | A1Z850 | `GO:0016209` antioxidant activity | IEA | 4 |
| ECOLI | DnaJ | P08622 | `GO:0005524` ATP binding | IEA | 4 |
| SCHPO | Epe1 | O94603 | `GO:0046872` metal ion binding | IEA | 4 |
| SCHPO | pmp20 | O14313 | `GO:0008379` thioredoxin peroxidase activity | IEA | 4 |
| human | AIP | O00170 | `GO:0003755` peptidyl-prolyl cis-trans isomerase activity | IDA | 4 |
| human | APBB1 | O00213 | `GO:0006915` apoptotic process | IEA | 4 |
| human | BCL2 | P10415 | `GO:0000209` protein polyubiquitination | IDA | 4 |
| human | BECN1 | Q14457 | `GO:0006915` apoptotic process | IEA | 4 |
| human | C1QBP | Q07021 | `GO:0006915` apoptotic process | IEA | 4 |
| human | CDC25B | P30305 | `GO:0006468` protein phosphorylation | IDA | 4 |
| human | CDK1 | P06493 | `GO:0006915` apoptotic process | IEA | 4 |
| human | CDK1 | P06493 | `GO:0016579` protein deubiquitination | TAS | 4 |
| human | CFTR | P13569 | `GO:0016853` isomerase activity | IEA | 4 |
| human | CHMP3 | Q9Y3E7 | `GO:0140678` molecular function inhibitor activity | EXP | 4 |
| human | CHRAC1 | Q9NRG0 | `GO:0071897` DNA biosynthetic process | IEA | 4 |
| human | CPT1C | Q8TCG5 | `GO:0016740` transferase activity | IEA | 4 |
| human | GMFG | O60234 | `GO:0006468` protein phosphorylation | TAS | 4 |
| human | GRPEL1 | Q9HAV7 | `GO:0051082` unfolded protein binding | IBA | 4 |
| human | HCST | Q9UBK5 | `GO:0006468` protein phosphorylation | IGI | 4 |
| human | HSPB6 | O14558 | `GO:0005212` structural constituent of eye lens | IEA | 4 |
| human | HSPG2 | P98160 | `GO:0005509` calcium ion binding | IEA | 4 |
| human | IL7R | P16871 | `GO:0003823` antigen binding | TAS | 4 |
| human | KCTD11 | Q693B1 | `GO:0016740` transferase activity | IEA | 4 |
| human | MORC3 | Q14149 | `GO:0006468` protein phosphorylation | IDA | 4 |
| human | PDGFA | P04085 | `GO:0038083` peptidyl-tyrosine autophosphorylation | NAS | 4 |
| human | PEX14 | O75381 | `GO:0034614` cellular response to reactive oxygen species | IDA | 4 |
| human | PIWIL1 | Q96J94 | `GO:0003729` mRNA binding | ISS | 4 |
| human | PPP3CB | P16298 | `GO:0006468` protein phosphorylation | ISS | 4 |
| human | SCG5 | P05408 | `GO:0005634` nucleus | IEA | 4 |
| human | SIRT1 | Q96EB6 | `GO:0004857` enzyme inhibitor activity | IEA | 4 |
| human | SLC14A1 | Q13336 | `GO:0005372` water transmembrane transporter activity | IEA | 4 |
| human | SPR | P35270 | `GO:0008106` alcohol dehydrogenase (NADP+) activity | TAS | 4 |
| human | TMEM67 | Q5HYA8 | `GO:0051082` unfolded protein binding | IPI | 4 |
| mouse | Pld4 | Q497R3 | `GO:0004630` phospholipase D activity | IEA | 4 |

## Tier 3: Moderate Candidates (score 3, selected highlights)

These need manual review but include notable patterns. Many of these are better treated as **simple removals** rather than formal NOT annotations — a NOT annotation requires positive evidence that the function is absent, not merely insufficient evidence that it is present.

| Species | Gene | UniProt | Incorrect Term | Evidence | Pattern |
|---------|------|---------|----------------|----------|---------|
| ACET2 | celC | A3DJ77 | `GO:0008422` beta-glucosidase activity | IEA | Xylanase, not a glucosidase |
| ACET2 | xynZ | P10478 | `GO:0033905` xylan endo-1,3-beta-xylosidase activity | IDA | Wrong xylanase specificity |
| DROME | Ccs | A1Z850 | `GO:0004784` superoxide dismutase activity | IEA | Copper chaperone for SOD1, not SOD itself |
| DESVH | fliA | Q726C4 | `GO:0003899` DNA-directed RNA polymerase activity | IEA | Sigma factor, not the catalytic subunit |
| METEA | mxaI | P14775 | `GO:0004022` alcohol dehydrogenase (NAD+) activity | IEA | Beta subunit, catalysis is in alpha |
| SCHPO | Epe1 | O94603 | `GO:0032452` histone demethylase activity | IBA | Core pseudo-enzyme case |
| SCHPO | Epe1 | O94603 | `GO:0032454` histone H3K9 demethylase activity | IDA | Even IDA is contested |
| SCHPO | pmp20 | O14313 | `GO:0004601` peroxidase activity | IEA | Distinct from thioredoxin peroxidase |
| SCHPO | sou1 | Q9Y6Z9 | `GO:0050085` mannitol 2-dehydrogenase (NADP+) activity | IEA | Different substrate specificity |
| human | AGRN | O00468 | `GO:0005200` structural constituent of cytoskeleton | TAS | Extracellular proteoglycan, not cytoskeletal |
| human | APEX1 | P27695 | `GO:0033892` deoxyribonuclease (pyrimidine dimer) activity | IDA | AP endonuclease, not pyrimidine dimer nuclease |
| human | APEX1 | P27695 | `GO:0004844` uracil DNA N-glycosylase activity | TAS | Misattributed activity |
| human | ATF2 | P15336 | `GO:0018107` peptidyl-threonine phosphorylation | IDA | Is phosphorylated, not a kinase |
| human | ATP6V0C | P27449 | `GO:0046933` proton-transporting ATP synthase activity, rotational | TAS | V-ATPase, not F-ATP synthase |
| human | CAPG | P40121 | `GO:0051014` actin filament severing | IBA | Caps filaments, does not sever |
| human | CFTR | P13569 | `GO:0006695` cholesterol biosynthetic process | IEA | Chloride channel, not cholesterol synthesis |
| human | CTLA4 | P16410 | `GO:0050853` B cell receptor signaling pathway | IBA | T cell inhibitory receptor |
| human | DCN | P07585 | `GO:0003723` RNA binding | HDA | HTP artifact; decorin is extracellular |
| human | IL7R | P16871 | `GO:0003823` antigen binding | TAS | Cytokine receptor, not antigen-binding |
| human | PSMD1 | Q99461 | `GO:0016887` ATPase activity | IBA | Structural lid subunit, not the ATPase ring |
| mouse | Ang2 | P21258 | `GO:0006412` translation | IEA | Angiogenin, ribonuclease activity, not a ribosome |
| worm | pgl-1 | Q9XTR1 | `GO:0003677` DNA binding | IEA | P granule component, RNA-binding |

## Emerging Patterns

### 1. Pseudo-enzyme Pattern (Highest value for NOT annotations)

Proteins with enzyme-family domains that have lost catalytic activity. These are the strongest NOT candidates because:
- Automated pipelines will repeatedly re-annotate them
- The negative evidence is biochemically definitive
- NOT annotations prevent IBA propagation

**Examples**: Epe1 (JmjC pseudo-demethylase), PLD5 (pseudo-phospholipase D), AKTIP (pseudo-E2), AIP (pseudo-PPIase), CG6051 (pseudo-phosphatase), CPT1C (pseudo-transferase), Pld4 (pseudo-PLD)

### 2. Domain =/= Function Pattern

Domains that serve structural/binding roles but are annotated with the catalytic activity of the domain family.
- Dockerin domains annotated as hydrolases (cipB, cipA, celX)
- Sensor domains annotated as kinases (DVU_3336)
- DnaJ domains annotated as ATP-binding (YDJ1, DNAJA2, DNAJA4, Dnaja3, DnaJ)
- PGRP domains annotated as amidases (PGRPS1, PGRPLD)

### 3. "Is Phosphorylated" =/= "Does Phosphorylation" Pattern (Over-annotation — removals, not NOTs)

A systematic class of over-annotation where proteins annotated to `GO:0006468` (protein phosphorylation) are actually kinase SUBSTRATES, and the cited paper only demonstrates their phosphorylation BY kinases, not that they are kinases. This is especially common with TAS and IDA evidence codes.

**Important caveat**: Being a phosphorylation substrate does NOT definitively mean the protein lacks kinase activity — autophosphorylation exists, and some proteins are both substrates and kinases. These are therefore primarily **over-annotation candidates** (the evidence cited doesn't support the annotation), not necessarily true NOT candidates (where there is positive evidence the activity is absent).

However, none of these 19 genes have a kinase domain in InterPro, which strengthens the case. The nuance is:
- `GO:0006468` (protein phosphorylation) is a **process term** — a gene product can be "involved in" phosphorylation via regulation without being a kinase. So a NOT for process involvement is a higher bar than a NOT for kinase MF.
- For a formal NOT on the **MF** (e.g. `NOT GO:0004672 protein kinase activity`), the absence of a kinase domain IS strong structural evidence and could justify NOTs for some of these.
- For the **BP** annotation `GO:0006468`, these are better treated as evidence-insufficient removals unless the gene has no plausible regulatory role in phosphorylation either.

**Examples**: CREB1, MEX3B, ATF2, RARA, RUNX3, ILF3, GMFB, ADM2, BIRC6, PICK1, PRRT1, CTBP1, LIPE, HCST, CDC25B, PPP3CB, GMFG, MORC3, PDGFA

This is the single largest category by count. **Most should be simple removals, not formal NOTs.** The exception: proteins with no kinase domain AND no plausible regulatory role in phosphorylation could warrant NOT annotations specifically on the MF term `GO:0004672` (protein kinase activity), where structural absence of the kinase domain is positive evidence.

### 4. Assembly Factor =/= Complex Activity Pattern

Proteins required for assembly of multi-subunit complexes but annotated with the activity of the complex itself.
- SURF1: Assembly factor for Complex IV, annotated with cytochrome-c oxidase activity and proton transport
- ATP10: Assembly factor for ATP synthase, annotated with unfolded protein binding
- IDH3B: Regulatory subunit annotated with catalytic activity of the alpha subunit
- Ccs: Copper chaperone for SOD1, annotated with SOD activity

### 5. Upstream Regulator =/= Direct Activity

Genes annotated with the activity of their downstream targets.
- EGFR annotated as MAP3K (activates RAF, the actual MAP3K)
- RASA1 annotated with GTPase activity (stimulates Ras GTPase)

### 6. Non-catalytic Family Members

Family members that have lost the signature catalytic activity.
- PGRPS1, PGRPLD: PGRP family, lost amidase activity, retain binding
- Epe1: JmjC family, lost demethylase activity
- CG6051: Myotubularin family, lost phosphatase activity

## Relationship to Other Projects

- **CONTESTED_FUNCTION.md**: Overlaps with pseudo-enzyme cases (Epe1)
- **OVER_ANNOTATION_PATTERNS.md**: Overlaps with domain-based prediction errors
- **PAINT.md**: NOT annotations would prevent IBA propagation of these errors
- **PHOSPHORYLATION_REFACTOR.md**: The "is phosphorylated" pattern overlaps with phosphorylation curation

## Next Steps

- [ ] Prioritize Tier 1 candidates for formal NOT annotation submission
- [ ] For each Tier 1 candidate, verify literature reference supporting the negative claim
- [ ] Add `negated: true` to confirmed candidates in review YAML files
- [ ] Identify which NOT annotations would have the highest impact on preventing IBA propagation
- [ ] Develop systematic screen for additional pseudo-enzymes across all reviewed genes
- [ ] Consider building automated detection of pseudo-enzyme motifs (degenerate active sites)
- [ ] File GO tracker issues for the "protein phosphorylation" misannotation class
- [ ] Investigate whether DnaJ ATP-binding can be fixed at the InterPro2GO mapping level

---

# STATUS

## Completed
- [x] Initial scan of all reviews for NOT annotation candidates
- [x] Keyword-based scoring and ranking
- [x] Pattern categorization
- [x] Expanded keyword set and rescoring (250 candidates at score >= 3)

## In Progress
- [ ] Literature verification of Tier 1 candidates
- [ ] Formal NOT annotation proposals

Last updated: 2026-03-06

# NOTES

## 2026-03-06

**Project Creation**

Scanned 6,319 REMOVE/MARK_AS_OVER_ANNOTATED annotations across all gene reviews. Identified 22 very high-confidence (score >= 6) and 115 strong (score >= 4) candidates for formal NOT annotations across 19 species.

The most impactful pattern is **pseudo-enzymes**: proteins with enzyme-family domains that have demonstrably lost catalytic activity. These are particularly valuable NOT annotations because automated pipelines (InterPro2GO, IBA) will repeatedly re-annotate them without explicit NOT annotations to prevent propagation.

Key insight: The DnaJ/HSP40 ATP binding pattern (YDJ1, DNAJA2, DNAJA4, Dnaja3, DnaJ) represents a systematic class error worth addressing at the pipeline level - DnaJ proteins stimulate HSP70 ATPase but do not themselves bind ATP.

**Expanded Search**

Added keywords for "misannotation", "does not catalyze", "no intrinsic", "erroneous", "does not bind", "not itself", "false positive". This expanded the candidate pool from 53 to 250 at score >= 3.

Major new finding: the **"is phosphorylated" =/= "does phosphorylation"** pattern is the single largest category by count, with ~19 human genes incorrectly annotated to `GO:0006468` protein phosphorylation because a paper described their phosphorylation by kinases. This is a systematic issue with TAS/IDA evidence codes.

Also identified the **assembly factor pattern** (SURF1, ATP10, IDH3B, Ccs) where proteins required for complex assembly get annotated with the complex's activity.
