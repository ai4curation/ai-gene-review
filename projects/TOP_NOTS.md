---
title: "Top-Nots: Candidate NOT Annotations from Existing Reviews"
maturity: IN_PROGRESS
last_reviewed: 2026-10-05
autolink_gene_symbols: false
tags: [PIPELINE, EVALUATION]
species: [human, mouse, yeast, SCHPO, DROME, ANOGA, ACET2, BACSU, DESVH, ECOLI, METEA, METTP, PSEAE, PSEPK, SACEN, SALTY, STRCO, CANGA, CLOCL, ARATH, worm]
manifest:
  slides:
    - href: TOP_NOTS/slides/TOP_NOTS-slides.html
---
# Top-Nots: Candidate NOT Annotations from Existing Reviews

**Bottom line:** a NOT annotation states that a gene product lacks a function, and it is
the only thing that stops automated pipelines from re-asserting a wrong activity by IEA
or IBA. Many of the repo's ~6,319 REMOVE and MARK_AS_OVER_ANNOTATED decisions are really
negative findings, so we mined them for the strongest NOT candidates with a keyword score
over the review summaries ("lacks catalytic", "pseudoenzyme", "no detectable activity"
and similar). We did this because a REMOVE only cleans one review, while a NOT, filed
upstream, prevents the same error from propagating again. The scan (2026-03-06) found
250 candidates across 19 species, 115 strong (score 4 or more) and 22 very strong,
dominated by pseudo-enzymes, "is phosphorylated" misread as "does phosphorylation", and
assembly factors given the activity of their complex; 21 of the 22 Tier 1 rows are
REMOVE in their reviews and one is MARK_AS_OVER_ANNOTATED. A later BGC addendum adds
five more high-score candidates from a heme-less P450 homologue and active-site-less
condensing-enzyme folds. No candidate has yet been
literature-verified or proposed as a formal NOT, so the list is a worklist, not a
submission.

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
- Already marked as `negated: true`: 295 rows in 187 reviews (2026-10-08 recount; the earlier ~15 was an undercount). See [NOT_NOTs](#not_nots-existing-not-annotations-that-do-not-hold-up)

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

### BGC project: catalytic/cofactor terms on non-catalytic subunits & pseudoenzymes

NOT candidates from the biosynthetic-gene-cluster reviews (`BGC.md`). EryCII is a heme-less
cytochrome-P450 homologue; PqsB and the act chain-length factor are condensing-enzyme folds
with no active site (the catalytic residues are in their partner subunit).

| Species | Gene | UniProt | Incorrect Term | Evidence | Score | Pattern |
|---------|------|---------|----------------|----------|-------|---------|
| SACEN | eryCII | A4F7P2 | `GO:0020037` heme binding | IEA | 9 | P450 homologue lacks the conserved heme-ligating Cys; apo structure (PDB 2YJN); UniProt "lacks the heme-binding sites" |
| SACEN | eryCII | A4F7P2 | `GO:0004497` monooxygenase activity | IEA | 9 | No heme → no P450 monooxygenase chemistry; functions as a GT activator |
| SACEN | eryCII | A4F7P2 | `GO:0005506` iron ion binding | IEA | 8 | No heme iron; depends on the absent heme cofactor |
| PSEAE | pqsB | Q9I4X2 | `GO:0016746` acyltransferase activity | IEA | 7 | FabH/KAS-III fold but no active site (Cys-129/His-269 are in PqsC); contributes_to only |
| STRCO | actI-ORF2 | Q02062 | `GO:0016746` acyltransferase activity | IEA | 7 | Type II PKS chain-length factor; "does not have an active site" |

## Tier 2: Strong NOT Candidates (score 4-5)

The March 2026 scan returned 93 score-4 and score-5 rows. The selected highlights
below have been pruned against the current reviews; rows since accepted, moved to
`UNDECIDED`, or already represented by a curated NOT row are no longer listed.

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
| human | CHRAC1 | Q9NRG0 | `GO:0016740` transferase activity | IEA | 5 |
| human | CHRAC1 | Q9NRG0 | `GO:0003887` DNA-directed DNA polymerase activity | NAS | 5 |
| human | CTBP1 | Q13363 | `GO:0006468` protein phosphorylation | TAS | 5 |
| human | DNAJA2 | O60884 | `GO:0005524` ATP binding | IEA | 5 |
| human | EGFR | P00533 | `GO:0004709` MAP kinase kinase kinase activity | NAS | 5 |
| human | IDH3B | O43837 | `GO:0016616` oxidoreductase activity, acting on CH-OH donors | IEA | 5 |
| human | LIPE | Q05469 | `GO:0006468` protein phosphorylation | TAS | 5 |
| human | MORC3 | Q14149 | `GO:0018105` peptidyl-serine phosphorylation | IDA | 5 |
| human | PICK1 | Q9NRD5 | `GO:0006468` protein phosphorylation | ISS | 5 |
| human | RARA | P10276 | `GO:0006468` protein phosphorylation | IMP | 5 |
| human | RUNX3 | Q13761 | `GO:0006468` protein phosphorylation | IDA | 5 |
| human | SLC3A2 | P08195 | `GO:0005975` carbohydrate metabolic process | IEA | 5 |
| mouse | Dnaja3 | Q99M87 | `GO:0005524` ATP binding | IEA | 5 |

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
| SCHPO | pmp20 | O14313 | `GO:0008379` thioredoxin peroxidase activity | IBA | 4 |
| human | AIP | O00170 | `GO:0003755` peptidyl-prolyl cis-trans isomerase activity | IDA | 4 |
| human | APBB1 | O00213 | `GO:0006915` apoptotic process | IEA | 4 |
| human | BCL2 | P10415 | `GO:0000209` protein polyubiquitination | IDA | 4 |
| human | BECN1 | Q14457 | `GO:0006915` apoptotic process | IEA | 4 |
| human | CDC25B | P30305 | `GO:0006468` protein phosphorylation | IDA | 4 |
| human | CDK1 | P06493 | `GO:0006915` apoptotic process | IEA | 4 |
| human | CDK1 | P06493 | `GO:0016579` protein deubiquitination | TAS | 4 |
| human | CFTR | P13569 | `GO:0016853` isomerase activity | IEA | 4 |
| human | CHMP3 | Q9Y3E7 | `GO:0140678` molecular function inhibitor activity | EXP | 4 |
| human | CHRAC1 | Q9NRG0 | `GO:0071897` DNA biosynthetic process | IEA | 4 |
| human | CPT1C | Q8TCG5 | `GO:0016740` transferase activity | IEA | 4 |
| human | GMFG | O60234 | `GO:0006468` protein phosphorylation | TAS | 4 |
| human | GRPEL1 | Q9HAV7 | `GO:0051082` unfolded protein binding | IBA | 4 |
| human | HSPB6 | O14558 | `GO:0005212` structural constituent of eye lens | IEA | 4 |
| human | HSPG2 | P98160 | `GO:0005509` calcium ion binding | IEA | 4 |
| human | IL7R | P16871 | `GO:0003823` antigen binding | TAS | 4 |
| human | KCTD11 | Q693B1 | `GO:0016740` transferase activity | IEA | 4 |
| human | MORC3 | Q14149 | `GO:0006468` protein phosphorylation | IDA | 4 |
| human | PDGFA | P04085 | `GO:0038083` peptidyl-tyrosine autophosphorylation | NAS | 4 |
| human | PEX14 | O75381 | `GO:0034614` cellular response to reactive oxygen species | IDA | 4 |
| human | PPP3CB | P16298 | `GO:0006468` protein phosphorylation | ISS | 4 |
| human | SCG5 | P05408 | `GO:0005634` nucleus | IEA | 4 |
| human | SIRT1 | Q96EB6 | `GO:0004857` enzyme inhibitor activity | IEA | 4 |
| human | SLC14A1 | Q13336 | `GO:0005372` water transmembrane transporter activity | IEA | 4 |
| human | SPR | P35270 | `GO:0008106` alcohol dehydrogenase (NADP+) activity | TAS | 4 |
| human | TMEM67 | Q5HYA8 | `GO:0051082` unfolded protein binding | IPI | 4 |
| mouse | Pld4 | Q8BG07 | `GO:0004630` phospholipase D activity | TAS | 4 |

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
| SCHPO | sou1 | Q9Y6Z9 | `GO:0050085` mannitol 2-dehydrogenase (NADP+) activity | IEA | Different substrate specificity |
| human | APEX1 | P27695 | `GO:0033892` deoxyribonuclease (pyrimidine dimer) activity | IDA | AP endonuclease, not pyrimidine dimer nuclease |
| human | APEX1 | P27695 | `GO:0004844` uracil DNA N-glycosylase activity | TAS | Misattributed activity |
| human | ATF2 | P15336 | `GO:0018107` peptidyl-threonine phosphorylation | IDA | Is phosphorylated, not a kinase |
| human | ATP6V0C | P27449 | `GO:0046933` proton-transporting ATP synthase activity, rotational | TAS | V-ATPase, not F-ATP synthase |
| human | CAPG | P40121 | `GO:0051014` actin filament severing | IBA | Caps filaments, does not sever |
| human | CFTR | P13569 | `GO:0006695` cholesterol biosynthetic process | IEA | Chloride channel, not cholesterol synthesis |
| human | CTLA4 | P16410 | `GO:0050853` B cell receptor signaling pathway | IBA | T cell inhibitory receptor |
| human | DCN | P07585 | `GO:0003723` RNA binding | HDA | HTP artifact; decorin is extracellular |
| human | IL7R | P16871 | `GO:0003823` antigen binding | TAS | Cytokine receptor, not antigen-binding |

## Emerging Patterns

### 1. Pseudo-enzyme Pattern (Highest value for NOT annotations)

Proteins with enzyme-family domains that have lost catalytic activity. These are the strongest NOT candidates because:

- Automated pipelines will repeatedly re-annotate them
- The negative evidence is biochemically definitive
- NOT annotations prevent IBA propagation

**Examples**: Epe1 (JmjC pseudo-demethylase), PLD5 (pseudo-phospholipase D), AKTIP (pseudo-E2), AIP (pseudo-PPIase), CG6051 (pseudo-phosphatase), CPT1C (pseudo-transferase), EryCII (heme-less P450)

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

**Examples**: CREB1, MEX3B, ATF2, RARA, RUNX3, ILF3, GMFB, ADM2, PICK1, PRRT1, CTBP1, LIPE, CDC25B, PPP3CB, GMFG, MORC3, PDGFA

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

## NOT_NOTs: existing NOT annotations that do not hold up

The rest of this project mines REMOVE decisions for NOT annotations that
*should* exist. This section goes the other way: existing NOT annotations
that reviewers overturned. One test settles both directions. A NOT is worth
having only when the negative result rules out the function: the activity is
absent, or the process or location is excluded. A failure to detect something
is not enough.

**Scan (2026-10-08).** [scripts/not_nots.py](TOP_NOTS/scripts/not_nots.py)
writes [not_nots.tsv](TOP_NOTS/not_nots.tsv), one row per negated annotation
in any review.

| Review action on the NOT | Rows |
|---|---|
| ACCEPT | 234 |
| KEEP_AS_NON_CORE | 25 |
| UNDECIDED | 25 |
| REMOVE | 8 |
| MARK_AS_OVER_ANNOTATED | 3 |
| **Total** | **295** (187 reviews) |

Most NOTs hold up. The 11 overturned ones are below, grouped by why the
negative result failed to support a NOT. Each was checked against the
reviewer's reason.

### Worked example: ARL3 NOT located in cilium

ARL3 carried `NOT|located_in cilium` (IDA, PMID:17646400). The full text
shows the basis was a screen of EGFP-tagged Rab and Arl GTPases
overexpressed in serum-starved RPE1 cells. Arl family members other than
ARL13B "were also absent from primary cilia (Fig. S2 A)". That shows only
that tagged ARL3 is not selectively enriched in cilia under one condition.
It says nothing about where ARL3 acts, and ARL3 acts inside the cilium:
ARL13B, its GEF, is confined to the ciliary membrane, so ARL3-GTP is made
there and releases lipidated cargo from PDE6D and UNC119 (PMID:26551564).
Endogenous ARL3 also stains cilia. The NOT was removed; see
`genes/human/ARL3/ARL3-ai-review.yaml`.

### Failure types among the 11 overturned NOTs

| Type | Gene: NOT term (evidence, reference) | Why the NOT fails |
|---|---|---|
| **Non-detection of an overexpressed tagged protein** | human ARL3: cilium (IDA, PMID:17646400) | GFP-ARL3 was not enriched in cilia. Native ARL3 is in cilia and functions there. |
| **Absence from a fractionation proteome** | ARATH OST1: cytosol (RCA, PMID:21166475); ARATH AT5G02500 (HSC70-1): cytosol (RCA, PMID:21166475) | Not recovered in one cytosolic-proteome dataset. Direct IDA shows both are cytosolic. Missing from a proteome is not exclusion from a compartment. |
| **One allele or condition generalized to the gene** | human DCTN1: axonal transport (IMP, PMID:18364389); human AGR2: response to ER stress (IMP, PMID:25666625) | G59S p150Glued mice showed no bulk transport defect, but dynactin is required for dynein-driven axonal transport. AGR2 was not induced in one context, but later work shows it alleviates ER stress. |
| **Early negative assay superseded** | human AGO3: miRNA-mediated silencing by mRNA destabilization (IDA, PMID:15260970) | The 2004 assay detected no AGO3 slicing. PMID:29040713 later showed guide- and target-dependent AGO3 slicer activity. |
| **NOT on a parent of an asserted child** | ARATH RGA: regulation of developmental vegetative growth (IMP, PMID:11606552) | RGA also carries the positive annotation *negative regulation of* vegetative growth. NOT on the unsigned parent logically contradicts the child. This is a signed/unsigned curation slip, and could be caught automatically. |
| **Probable identity confusion** | human TOMM40: mitochondrion (IMP, PMID:11745481) | The paper studies TOMM40 under the name p38.5/Haymaker. TOMM40 is the core outer-membrane translocase pore. |
| **Negative is real but uninformative** (marked over-annotated, not removed) | human GBA1: mitochondrion organization, neuron projection development (IMP, PMID:25456120); human CDK5: microtubule binding (TAS, PMID:17491008) | GBA1 iPSC neurons had normal mitochondrial morphology. True, but these are not processes GBA1 would be expected to act in, so the NOT prevents no plausible error. For CDK5, microtubule binding belongs to its activator p35. |

### Lessons for making and trusting NOTs

- **Localization NOTs need positive evidence of exclusion.** Examples are a
  validated antibody against the native protein, or a compartment marker plus
  a functional test. A tagged construct or a proteome list that misses the
  protein is not enough.
- **Process NOTs from loss-of-function need the whole gene tested.** One
  missense allele, one cell line or one condition can show the allele is
  dispensable. It cannot show the gene is uninvolved.
- **Check NOTs against the ontology.** A NOT on a term whose descendant is
  asserted positively for the same gene is a contradiction, and a query
  could find these systematically (the RGA case).
- **Old negative assays age badly.** AGO3's 2004 negative was overturned by
  later work. The same 2004 paper (PMID:15260970) supplies NOTs for AGO1
  and AGO4 that are still UNDECIDED (below), so they should be reviewed
  together with AGO3.

### Undecided NOTs (follow-up list)

25 negated rows are UNDECIDED, usually because the reviewer could not see
the full text. They cluster:

- **AGO1, AGO4** (×4): NOT siRNA/miRNA silencing by mRNA destabilization,
  PMID:15260970. These come from the same paper as the overturned AGO3 NOT.
  AGO1 and AGO4 are generally considered slicer-deficient, so these NOTs may
  be right where AGO3's was not.
- **SIRT1, SIRT5** (×5): NOT ADP-ribosyltransferase activities (TAS,
  PMID:17456799) and SIRT5 NOT protein deacetylation (IDA, PMID:22076378).
  These reflect the debated sirtuin activities.
- **BMPR2, BMPR1A** (×5): NOT cardiac and neural-crest developmental
  processes, ISS (GO_REF:0000024). These are inferred negatives, which are
  unusual.
- **ANO5, ANO10**: NOT calcium-gated chloride channel activity (IDA).
- **Singletons:** Epe1 heterochromatin formation; A3GALT2
  alpha-1,3-galactosyltransferase; ABCB4 ceramide floppase and ceramide
  translocation; RAB1B; TMEM65; VAPA; YTHDF3; rat Slc5a1 (ISO).

## Relationship to Other Projects

- **CONTESTED_FUNCTION.md**: Overlaps with pseudo-enzyme cases (Epe1)
- **OVER_ANNOTATION_PATTERNS.md**: Overlaps with domain-based prediction errors
- **PAINT.md**: NOT annotations would prevent IBA propagation of these errors
- **PHOSPHORYLATION_REFACTOR.md**: The "is phosphorylated" pattern overlaps with phosphorylation curation

## Next Steps

Tracked in [ai-gene-review#4019](https://github.com/ai4curation/ai-gene-review/issues/4019).

- Todo: prioritize Tier 1 candidates for formal NOT annotation submission
- Todo: for each Tier 1 candidate, verify literature reference supporting the negative claim
- Todo: add `negated: true` to confirmed candidates in review YAML files
- Todo: identify which NOT annotations would have the highest impact on preventing IBA propagation
- Todo: develop a systematic screen for additional pseudo-enzymes across all reviewed genes
- Todo: consider building automated detection of pseudo-enzyme motifs (degenerate active sites)
- Todo: file GO tracker issues for the "protein phosphorylation" misannotation class
- Todo: investigate whether DnaJ ATP-binding can be fixed at the InterPro2GO mapping level
- Todo: NOT_NOTs: review the AGO1/AGO4 NOTs (PMID:15260970) together with the overturned AGO3 NOT
- Todo: NOT_NOTs: query for NOTs on a parent term where a descendant is asserted positively for the same gene (RGA pattern)
- Todo: NOT_NOTs: work through the 25 UNDECIDED negated rows

---

# STATUS

## Completed
- Done: initial scan of all reviews for NOT annotation candidates
- Done: keyword-based scoring and ranking
- Done: pattern categorization
- Done: expanded keyword set and rescoring (250 candidates at score >= 3)
- Done: NOT_NOTs scan of existing negated annotations and typing of the 11 overturned ones (2026-10-08)

## In Progress
- Todo: literature verification of Tier 1 candidates
- Todo: formal NOT annotation proposals

Last updated: 2026-10-08

# NOTES

## 2026-10-08

**NOT_NOTs section added.** This started from the ARL3 review in the
HUMAN_PROTEIN_ATLAS cilium project, where `NOT|located_in cilium` turned out
to rest on a tagged-construct screen (see the worked example). Recounted all
negated annotations: there are 295, not ~15. Of these, 11 were overturned and
25 are undecided. Recorded the overturned ones by failure type, plus the
lessons and follow-ups, as a section here rather than a separate project.
The numbers are small, and the test for a good NOT is the same in both
directions.

## 2026-03-06

**Project Creation**

Scanned 6,319 REMOVE/MARK_AS_OVER_ANNOTATED annotations across all gene reviews. Identified 22 very high-confidence (score >= 6) and 115 strong (score >= 4) candidates for formal NOT annotations across 19 species.

The most impactful pattern is **pseudo-enzymes**: proteins with enzyme-family domains that have demonstrably lost catalytic activity. These are particularly valuable NOT annotations because automated pipelines (InterPro2GO, IBA) will repeatedly re-annotate them without explicit NOT annotations to prevent propagation.

Key insight: The DnaJ/HSP40 ATP binding pattern (YDJ1, DNAJA2, DNAJA4, Dnaja3, DnaJ) represents a systematic class error worth addressing at the pipeline level - DnaJ proteins stimulate HSP70 ATPase but do not themselves bind ATP.

**Expanded Search**

Added keywords for "misannotation", "does not catalyze", "no intrinsic", "erroneous", "does not bind", "not itself", "false positive". This expanded the candidate pool from 53 to 250 at score >= 3.

Major new finding: the **"is phosphorylated" =/= "does phosphorylation"** pattern is the single largest category by count, with ~19 human genes incorrectly annotated to `GO:0006468` protein phosphorylation because a paper described their phosphorylation by kinases. This is a systematic issue with TAS/IDA evidence codes.

Also identified the **assembly factor pattern** (SURF1, ATP10, IDH3B, Ccs) where proteins required for complex assembly get annotated with the complex's activity.
