# PUT2 (P07275, YHR037W) notes

- P5C dehydrogenase, second step of proline utilization [PMID:3025596 "the second enzyme in the proline utilization (Put) pathway of Saccharomyces cerevisiae and the product of the PUT2 gene"]
- Reaction EC 1.2.1.88 [UniProt:P07275 "Reaction=L-glutamate 5-semialdehyde + NAD(+) + H2O = L-glutamate + NADH"]
- Matrix by fractionation/latency [PMID:3025596 "was localized to the matrix compartment by a mitochondrial fractionation procedure"]; UniProt says inner membrane (PMID:11502169, not cached) -> inner membrane kept non-core.
- put2 mutants lack P5C DH, cannot use proline as N source [PMID:387737 "Mutants in put1 are deficient in proline oxidase, and those in put2 lack P5C dehydrogenase"]
- Arginine degradation converges at P5C [PMID:387737 "The arginine-degradative pathway intersects the proline-degradative pathway at P5C"]

## YeastPathways / GO-CAM
- BioPAX summary: RXN-14116 has no gene in PROUT-PWY or ARGDEG-YEAST-PWY, but the YeastPathways GO-CAMs (gocams/index.tsv) DO attach PUT2 to RXN-14116 and GOA has RCA rows; both put PUT2 in cytosol (wrong, removed).
- Protein binding with Ssa2 (HT) removed.
