# CSN1S1 (human alpha-S1-casein, P47710) - review notes

## Identity

- 185 aa precursor, 15 aa signal peptide, mature chain 16-185; alpha-casein family
  (Pfam PF00363), part of the SCPP gene cluster.
- Minor casein in human milk
  [PMID:38339021 "A reason for this could be the low content of breast-milk αS1-casein with less than 1% (3 mg/L to 537 mg/L) of total milk protein content"];
  human casein ratio [PMID:36903269 "Human milk lacks αS2-casein, and the relative ratio of αS1-, β-, and κ-caseins in human milk is 3:70:27."].

## Core function

- Calcium-sensitive casein in the micelle interior
  [PMID:36903269 "The calcium-sensitive caseins (αS1-, αS2-, and β-) bind calcium, mainly by electrostatic interactions with colloidal calcium phosphate (CCP)"].
- Core MF: GO:0140314 calcium ion sequestering activity, as for all calcium-sensitive
  caseins in this batch. This is an approximation (the real cargo is amorphous calcium
  phosphate nanoclusters), recorded as a suggested question.
- Lactation (GO:0007595) as process; extracellular region as location. Casein micelle
  proposed as a new CC term (same proposal as human CSN2/CSN3).

## Immunomodulatory activity of the recombinant / non-phosphorylated protein (non-core)

- Monocyte skewing [PMID:24083466 "CSN1S1 skews in vitro differentiation of monocytes towards a macrophage-like phenotype."];
  DC inhibition [PMID:24083466 "Early GM-CSF, but not GM-CSF/IL-4 induced differentiation of monocytes towards dendritic cells (DC) was inhibited by addition of CSN1S1."].
- TLR4 dependence and phosphorylation switch
  [PMID:26909866 "Phosphorylation of CSN1S1 by casein-kinase 2 completely abolished proinflammatory cytokine induction and binding to TLR4."];
  [PMID:30553868 "In this study, αS1-casein was identified as binder of theTLR4 ecto domain."];
  [PMID:38339021 "Our results indicate that αS1-casein appears in two distinct conformations, an α-helical TLR4-agonistic and a less α-helical TLR4 non-agonistic conformation induced by phosphorylation."].
- All in vitro with recombinant protein; milk alpha-S1-casein is phosphorylated, so the
  physiological relevance is unclear. Not proposed as GO annotations; noted in description
  with the references above, and raised as a suggested question.

## Annotation decisions

- Steroid-response IBA rows: MARK_AS_OVER_ANNOTATED (family convention; casein is the
  expression readout, PANTHER PTN000028262 seeded by bovine PMID:3585228).
- GO:0005515 (HuRI, WITH UniProtKB:Q9UHD9 UBQLN2): REMOVE; UBQLN2 is a cytosolic ubiquilin
  two-hybrid partner with no relevance to a secreted casein (as in human CSN2/CSN3).

## Batch-standard revision (2026-10-24)

- Rewrote the description: removed unsupported claims, backed the TLR4, monocyte and
  dendritic-cell statements with PMID:24083466, PMID:26909866, PMID:30553868 and
  PMID:38339021 (all fetched and read; abstracts or full text).
- Rewrote the UBQLN2 protein-binding row (summary, reason, supporting_entities) and
  dropped the citation-fragment supporting_text.
- Split the core function so it covers calcium sequestering only (immune effects and
  bioactive peptides removed from it).
- Added proposed_new_terms (casein micelle), suggested questions (including that
  GO:0140314 is an approximation) and a suggested experiment.
- No OpenScientist deep-research report exists for human CSN1S1.
