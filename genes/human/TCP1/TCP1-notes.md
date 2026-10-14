# TCP1 (CCT1) notes

Deep research: skipped because the providers are unavailable here. The review is based on UniProt P17987 and cached publications.

## Key findings
- TCP1 acts as a cytosolic chaperone for tubulin, and ATP hydrolysis is required [PMID:1630491 "Addition of Mg-ATP, but not nonhydrolysable analogues, released the tubulin subunits as assembly-competent protein"].
- Human TRiC contains all eight subunits [PMID:23011926].
- CCT1 is a higher-affinity ATP-binding subunit [PMID:23041314 "CCT5 and CCT4 have the highest affinities and thus are occupied at the lowest ATP concentrations, followed by CCT1 and CCT2."].
- TRiC folds TCAB1 [PMID:25467444 "TRiC is required for folding the telomerase cofactor TCAB1"]. The telomere and Cajal-body process rows are client-specific consequences and were kept as non-core.
- CCT works with BBS6/10/12 in BBSome assembly at the centrosome [PMID:20080638].

## Decisions
- The core MF is ATP binding, and the subunit contributes to GO:0140662 ATP-dependent protein folding chaperone. This matches the worm cct-1 review.
- Protein folding chaperone (GO:0044183) rows were modified to GO:0140662.
- Protein-binding rows were removed: CCT subunit-subunit rows as redundant with complex membership, and client rows as uninformative.
- The microtubule IDA (PMID:21525035, a PEX14 paper, abstract only) was left UNDECIDED.
