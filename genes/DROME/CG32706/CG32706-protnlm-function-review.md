# ProtNLM function paragraph: CG32706 / Q8IRM9

## Original prediction

> Involved in the small subunit (SSU) processome assembly and function, and in the 18S rRNA synthesis. Required for the early cleavages at sites A0, A1 and A2

The complete original comment and source metadata are preserved in [predictions source](CG32706-predictions-source.json). There are no GO-term predictions for this record. The phmmer donor is fission-yeast Esf2 O74362, score 77.1.

## Claim assessments

**SSU-processome assembly/function and 18S-rRNA synthesis: CNN.** These broad claims are supported by the specific ABT1/Esf2 family assignment and direct experimental characterization of budding-yeast Esf2 in [PMID:15964808](https://pubmed.ncbi.nlm.nih.gov/15964808/). “Esf2p-depleted cells are defective for pre-rRNA processing at the early nucleolar cleavage sites A0 through A2 and consequently are inhibited for 18S rRNA synthesis.” These conserved functions are already represented by the existing fly IBA annotations. Transfer is justified by the specific family, retained RNA-binding region and conserved ribosome-assembly mechanism.

**Requirement for the specifically named sites A0, A1 and A2: CNN.** These are the experimentally characterized yeast processing sites, and the same three cleavages are already represented for this gene by PAINT IBA annotations from the ABT1/Esf2 node PTN000267771: GO:0000480 (5′-ETS cleavage, site A0), GO:0000472 (cleavage generating the mature 18S 5′ end, site A1) and GO:0000447 (ITS1 cleavage, site A2). The curated gene review retains all three as phylogenetically sound but non-core, because Esf2 is a processome assembly factor and the cleavage defect follows from failed processome assembly. Q8IRM9 is the canonical, full-length CG32706 product with the RRM and family core intact, so no required feature is missing. The claim says the protein is required for these cleavages; it does not imply, and should not be read as, intrinsic nuclease activity. O74362 repeats a by-similarity paragraph and is not independent experimental validation; the experimental grounding is budding-yeast Esf2 in [PMID:15964808](https://pubmed.ncbi.nlm.nih.gov/15964808/). No Drosophila experiment maps these sites to CG32706 directly.
