# APLP1 (human) review notes

UniProt P51693 (APLP1_HUMAN). Taxon NCBITaxon:9606.

These notes were added as a 2026 update to an already-complete review. They cover one
topic only: APLP1's proposed role as a neuronal receptor for pathological alpha-synuclein
fibrils, which the existing review did not mention (the file contained zero occurrences of
"synuclein" or "fibril" before this update). Nothing else in the review was changed.

## Why this was added

APLP1 is now routinely named as one of three candidate neuronal mediators of alpha-synuclein
preformed-fibril (PFF) uptake and spread, alongside FAM171A2 and LAG3:
[PMID:41270468 "have been identified as critical mediators of α-syn preformed fibril (PFF)
uptake, propagation, and neurotoxicity"].

## What is actually established for APLP1

**Direct biophysics (strongest evidence).** The isolated APLP1 E1 domain binds the acidic
C-terminus of alpha-synuclein by an electrostatic mechanism shared with LAG3 D1, with strong
preference for the fibrillar over the monomeric state:
[PMID:34172566 "LAG3 D1 and APLP1 E1 domains commonly use an alkaline surface to bind the
acidic C terminus"] and [PMID:34172566 "can preferentially bind α-syn in the amyloid over
monomeric state to initiate cell-to-cell transmission"]. Cached abstract-only.

**Cellular/in vivo (partner-dependent).** APLP1 is presented as acting through a complex
with LAG3: [PMID:38821932 "amyloid β precursor-like protein 1 (Aplp1) interacts with Lag3
that facilitates the binding, internalization, transmission, and toxicity of pathologic
α-syn"]. The genetic rescue is from a **double** knockout, not an Aplp1 single knockout:
[PMID:38821932 "Deletion of both Aplp1 and Lag3 eliminates the loss of dopaminergic
neurons"]. So the APLP1-only contribution has not been isolated in vivo.

That paper carries an Author Correction, which is a statistics/figure-legend fix to Fig. 4
and not a retraction: [PMID:39080298 "The original version of this Article contained an
error in Fig. 4"].

## Why the field is unsettled

- **LAG3, the partner the APLP1 mechanism depends on, is disputed.**
  [PMID:34309222 "we found no evidence for LAG3 expression by neurons"] and
  [PMID:34309222 "These data suggest that the proposed role of LAG3 in the spreading of
  α-synucleinopathies is not universally valid."]. Important caveat: **this paper does not
  mention APLP1 anywhere** (checked: zero occurrences in the cached full text). It is
  evidence against LAG3, and touches APLP1 only indirectly.
- **A third candidate receptor was reported in 2025.**
  [PMID:39977508 "Our findings identified FAM171A2 as a potential receptor for the neuronal
  uptake of α-syn fibrils"]. This paper likewise does not mention APLP1 (zero occurrences).
- **Provenance is concentrated.** PMID:27708076 (LAG3, Science 2016), PMID:34172566 (PNAS
  2021) and PMID:38821932 (Nat Commun 2024) share senior authorship (Dawson/Mao, with Liu
  for the biophysics). The 2021 and 2024 papers are therefore not independent replications
  of the 2016 proposal.
- **The one paper that puts all three side by side is computational.** AlphaFold3 modelling,
  not experiment: [PMID:41270468 "The APLP1 was predicted to interact with both monomeric
  and hexameric α-syn proteins."], and it could not reproduce the LAG3 interaction at all:
  [PMID:41270468 "Neither full-length nor domain-restricted constructs resulted in accurate
  prediction of the experimentally identified interaction between LAG3 and α-syn protein."].

## Curation position taken

**No annotation was added or changed.** Checked the whole of `APLP1-goa.tsv`: no existing
GO annotation on APLP1 concerns alpha-synuclein, fibril binding, or endocytic uptake of
aggregates, so nothing in `existing_annotations` is affected and no action changed.

A receptor molecular function was deliberately *not* proposed, for three reasons:
1. The in vivo evidence is double-knockout only, so APLP1 cannot be separated from LAG3.
2. The LAG3 half of the mechanism is actively contested.
3. The only source that frames APLP1 as one of three receptors is a review with AlphaFold3
   predictions; structure predictions cannot support a GO molecular function.

What was recorded instead: the six references above (with `findings` and `reference_review`),
a `knowledge_gaps` entry stating precisely what is unknown and what would resolve it, four
`suggested_questions`, and two `suggested_experiments`.

## Ontology note

GO has `GO:0001540 amyloid-beta binding` but **no** alpha-synuclein binding term (checked
via QuickGO term search). The nearest available parent is `GO:0051787 misfolded protein
binding`, which loses the ligand identity. A proposed term is recorded under the knowledge
gap's `proposed_terms`; it is an ontology-coverage request and is not an assertion that
APLP1 should carry it.

## Open question for experts

Does APLP1 bind and internalize alpha-synuclein fibrils in LAG3-null neurons? An Aplp1
single-knockout uptake/spreading experiment, replicated outside the originating
laboratories, would settle whether APLP1 is a receptor in its own right or only a
co-factor of a partner that may not be expressed in neurons at all.
