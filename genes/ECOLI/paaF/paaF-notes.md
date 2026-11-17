# paaF (P76082) notes, E. coli K-12

## Deep research

`just deep-research ECOLI paaF --provider falcon` was attempted on 2026-10-23 and failed
("Exception: Failed to authenticate"; all providers failed). No deep-research file exists;
this review is built directly from the cached literature and the UniProt record.

## Function

- PaaF is the 2,3-dehydroadipyl-CoA hydratase of the aerobic phenylacetate (box) pathway.
  [PMID:20660314 "PaaF is an enoyl-CoA hydratase. Purified PaaF, when added to the assay ( Fig. 2 E ), catalyzed the reversible conversion of enzymatically produced 2,3-dehydroadipyl-CoA into 3-hydroxyadipyl-CoA"]
- Caveat: in Teufel et al. 2010 the PaaF protein actually assayed was the Pseudomonas sp. strain Y2 ortholog, not E. coli PaaF.
  [PMID:20660314 "Recombinant enzymes from Escherichia coli (PaaZ, PaaH) or Pseudomonas sp. strain Y2 (PaaABC(D)E, PaaG, PaaJ, PaaF) were tagged"]
  The supplementary methods were not available to check. The GOA IDA row (assigned by UniProt) for
  GO:0004300 cites this paper; recorded as a probable evidence-code issue (ortholog, so ISS-like),
  but the activity itself is well supported for E. coli PaaF by orthology, the in vivo mutant
  phenotype and the E. coli PaaF crystal structure (conserved catalytic Glu-109/Glu-129).
- Stereochemistry of the enoyl substrate is not established
  [PMID:20660314 "Note also that the cis configuration of 2,3-dehydroadipyl-CoA ( Fig. 1 B , compound VI) is hypothetical, because its stereochemistry has not yet been determined."]
- In vivo: E. coli paaF deletion mutant cannot grow on phenylacetate and accumulates delta3-dehydroadipate
  [PMID:12846838 "Incubation of the paaF and paaH mutants with phenylacetate yielded delta3-dehydroadipate and 3-hydroxyadipate, respectively."]

## Structure / complex

- E. coli PaaF forms a stable complex with PaaG (enoyl-CoA isomerase), the only stable complex in the lower pathway
  [PMID:22961985 "The only stable complex identified was between PaaF and PaaG"]
- PaaF homotrimers stack into a hexamer sandwiched by PaaG trimers
  [PMID:22961985 "PaaF and PaaG associate into homotrimeric rings; two PaaF homotrimers pack face-to-face into a homohexamer"]
- No FadBA-like complex with PaaH/PaaJ
  [PMID:22961985 "No complex between PaaF, PaaH, and PaaJ, equivalent to the fatty acid β-oxidation complex, was detected."]
- Catalytic residues
  [PMID:22961985 "The structurally equivalent residues in PaaF are Glu-109 and Glu-129, which suggests that the catalytic mechanism of PaaF is similar to ECH."]

## Regulation

paaABCDEFGHIJK operon repressed by PaaX, de-repressed by phenylacetyl-CoA, activated by CRP and IHF
[PMID:10766858 "PA-coenzyme A (PA-CoA), but not PA, specifically inhibited binding of PaaX to the target sequences"].

## Curation decisions

- GO:0006635 fatty acid beta-oxidation (IBA): marked over-annotated; no evidence E. coli PaaF acts on fatty acyl-CoAs in vivo; its substrate is a C6 dicarboxylic intermediate of phenylacetate catabolism.
- GO:0005515 (IPI with PaaG): REMOVE per protein-binding policy; the interaction is captured by GO:1902494 catalytic complex.
