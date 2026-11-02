# Csn1s2a (mouse gamma-casein / alpha-S2-casein-like A, Q02862) - review notes

- Mouse gamma-casein, ortholog-group of ruminant alpha-s2-casein (PTHR16656). Purified from milk and sequenced [PMID:7763793 "A partial amino acid sequence of mouse gamma-casein was determined on a gas-phase amino acid sequencer."] Phosphoserines at 23-25, 37 (UniProt, ECO:0000269 PMID:7763793).
- UniProt FUNCTION: "Important role in the capacity of milk to transport calcium phosphate."
- Gamma-casein is a prominent mouse milk protein, quantified in Kolb et al.: [PMID:21789179 "In addition, the amounts of β- and γ-casein are also significantly reduced"]; carries phosphate centres [PMID:21789179 "The sequences of α- (αS1 in ruminants) β-, and γ-casein (αS2-casein in ruminants) contain one or more clusters of phosphorylated residues known as phosphate centres."]
- zymogen binding IBA: propagated from bovine alpha-s2-casein ligand blotting with t-PA [PMID:8186264 "multimeric forms of kappa-casein and dimeric alpha s2-casein were identified as t-PA binding components"]. In-vitro, micelle-associated; mouse not tested -> over-annotation.
- A gamma-casein knockout is mentioned in Kolb et al. (ref 27) but I could not identify/verify that paper; not cited.

## Deep research
- OpenScientist deep research not available at time of review.

## Deep research integration (OpenScientist, 2026-10-24)

The report arrived after the review; all its PMIDs were fetched into publications/ and the
points used were checked against the abstracts.

- No contradiction with the review's core call (GO:0140314, extracellular, milk).
- One over-reach in the report, not adopted: it uses the alpha-casein (Csn1s1) knockout
  growth delay (PMID:23321409) as confirmation "by extension" for Csn1s2a. That knockout
  targets a different gene; it shows gamma-casein falls in alpha-casein-null milk, not
  that gamma-casein is itself required.
- Added to GO:0140314 (NEW): PMID:18420601 (phosphoserine domains of alpha-s1, alpha-s2
  and beta-casein stabilize calcium phosphate nanoclusters), PMID:12427545 (mouse
  gamma-casein corresponds to ruminant alpha-s2-casein) and a quote from the report.
- Not used: prolactin/STAT5 and glucocorticoid promoter regulation (PMID:12427545;
  expression control), FAM20C and Ergic2/3 (kinase pathway; PMID:23754375, 24706917,
  42439892), condensate proposal (PMID:35815989).

## Reviewer feedback (PR #5352, 2026-10-24)

- GO:0045735 nutrient reservoir activity (NEW) and its core function: replaced the
  truncated figure-legend quote and the abundance-only "amounts ... reduced" quote. Support
  is now abundance (PMID:21789179 "most prominent proteins ... α-, β- and γ-casein";
  PMID:12427545 "mRNA levels of gamma- and beta-casein are similar") plus the
  amino-acid-supply role of the casein micelle (PMID:22436214 "transport of amino acids,
  calcium and phosphorus"). No cached paper states the amino-acid supply for gamma-casein
  alone, so the summary and core-function description now say the role is inferred from
  abundance and micelle membership, not from a knockout.
- Core vs mouse Csn3: kept core here, as for mouse Csn1s1 and Csn2, because gamma-casein
  is a major casein whose bulk is the store; Csn3 keeps the term non-core because
  kappa-casein is the least abundant casein and its essential role is micelle
  stabilization. This is stated in the row's reason.
- Status COMPLETE.
- Also added PMID:16698927 (mouse kappa-casein knockout abstract: "Milk casein micelles
  are a primary source of amino acids and calcium phosphate to neonates") as the
  mouse-specific statement of the micelle's amino-acid supply role.
