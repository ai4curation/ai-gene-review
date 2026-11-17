# PP_3206 curation notes

- UniProt Q88HZ6 supplies only an epimerase/dehydratase-fold name
  [file:PSEPK/PP_3206/PP_3206-uniprot.txt "RecName: Full=NAD-dependent
  epimerase/dehydratase domain-containing protein"]. This does not establish an
  epimerase substrate or reaction.
- OpenScientist identifies the KEGG K26183/FdeJ and R13076 assignment but also
  states that the reaction is inferred rather than experimentally demonstrated
  [file:PSEPK/PP_3206/PP_3206-deep-research-openscientist.md "FdeJ's specific
  reaction (oxaloacetate-releasing hydrolysis, KEGG R13076) is therefore a
  pathway/orthology inference"].
- A committed global alignment gives 51.1% identity to Hsero_1012/D8J0X4
  [file:PSEPK/PP_3206/PP_3206-bioinformatics/RESULTS.md "Pairwise identity over
  aligned residue pairs: 51.1%"], not the report's unreproduced 52.4%. Neither
  sequence has direct R13076 evidence.
- Organism-level evidence establishes flavonoid A-ring fission in P. putida
  [PMID:8071218 "Pseudomonas putida degraded quercetin via an initial fission in
  its A-ring"], while the Herbaspirillum pathway produces oxaloacetate after
  meta-cleavage [PMID:27059806 "After meta-cleavage of the A-ring, the subsequent
  metabolic steps generate oxaloacetic acid that is metabolized via the
  tricarboxylic acid cycle."]. Neither paper identifies PP_3206 as the catalyst.
- GO:0009812 is retained as an ISS pathway annotation. GO:0016822 is not
  asserted because the donor is also uncharacterized for R13076 and the
  epimerase/dehydratase fold does not establish carbon-carbon hydrolase
  chemistry. The exact R13076 activity remains a proposed term and knowledge gap.

## 2026-11-06 — late-component participation reassessment

The inherited GO:0046275 proposal is withdrawn and explicitly `retired: true`: the epimerase/dehydratase fold and similarity to unassayed Hsero_1012 do not establish the proposed oxaloacetate-releasing R13076 reaction. Locus induction, whole-operon phenotypes and similarity to another unassayed candidate do not establish this product's individual step. Original source fields and row position are preserved; retirement records curator withdrawal, not an upstream GOA disappearance. The former process-only core block is removed, and the unresolved role remains a knowledge gap. The same-role BRADU comparator bll6421 likewise asserts no process annotation. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md`.


## 2026-11-07 PR #6140 round-2 review follow-up

The inherited GO:0046275 proposal now uses REMOVE with its existing retired:true flag. This explicitly withdraws a curator-authored proposal, following the documented cysI precedent, rather than making a biological absence claim or reporting disappearance from upstream GOA. Original payload, position and evidence remain present. The uncharacterized reaction-specific proposed term has been removed from the active GO-request slot and preserved as a suggested question plus exact archived proposal in round2-relocated-proposals.yaml. No reaction-level activity is newly asserted.

See `analysis/module_audits/bacterial_flavonoid_degradation/round2-review-response.md` for source provenance, limits and disposition of all seven review points. Earlier journal entries record superseded judgments and remain unchanged.
