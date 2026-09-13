# PTHR43503 (MCG48959-RELATED) family review

## Scope

This review covers the current PANTHER/PAINT annotation propagated to *S. pombe*
Ral2 (UniProt P15258), which is classified in the official subfamily
**PTHR43503:SF2, NEGATIVE REGULATOR OF SPORULATION MDS3-RELATED**. The broad
family also contains peroxiredoxin-6 subfamilies, so ancestral gains and
subfamily losses must be read from the PAINT tree rather than inferred from the
family's InterPro prose description.

## Ral2 propagation

| GO ID | Label | Aspect | PANTHER node | Our action | Flags | Verdict |
|-------|-------|--------|--------------|------------|-------|---------|
| GO:0031137 | regulation of conjugation with cellular fusion | BP | PTN005166285 | ACCEPT | NO_UNIPROT_SEEDS;SINGLE_NODE_SEED | **Appropriate** |

**GO:0031137.** PAINT places this gain on the Ral2/Mds3-related node
PTN005166285. The leaf GOA source set includes `PomBase:SPBC21.05c`, Ral2's own
experimentally annotated gene product. That self-appearance is expected evidence
that the ancestral placement is grounded on the target; it is not circularity.
Classic ral2 disruption and activated-ras1 rescue experiments establish the
mating/conjugation phenotype independently (PMID:2586528; PMID:3071741).
The extractor's seed flags arise because no canonical UniProt seed maps through
its restricted seed subset, not because the PAINT node lacks experimental
support. **Appropriate — core biological process.**

## Function-loss boundary

The same node carries explicit IRD/NOT annotations for peroxidase activity
(GO:0004601), cytosol (GO:0005829), and cell redox homeostasis (GO:0045454).
These losses prevent functions acquired on the broad peroxiredoxin-containing
ancestor PTN000073790 from propagating into PTHR43503:SF2. Ral2's current GOA
accordingly contains none of the obsolete redox-related annotations present in
the older review. This is a positive example of PAINT loss annotation protecting
a deeply heterogeneous family boundary.

## Verdict

The current conjugation IBA is supported by the node placement and direct Ral2
genetics. The peroxiredoxin-like functions are explicitly lost before the
Ral2/Mds3 subfamily and should not be restored. No current Ral2 IBA
over-propagation is detected.

## Review status

- **Date:** 2026-09-01
- **Reviewer:** AI-assisted review
- **Status:** DRAFT
- **Based on:** PANTHER member table and PAINT slice, Ral2 GOA, and the refreshed
  `ral2-ai-review.yaml`
