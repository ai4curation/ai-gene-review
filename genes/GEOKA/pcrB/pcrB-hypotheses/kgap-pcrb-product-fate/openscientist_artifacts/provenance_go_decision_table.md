# GO decision table: Q5L3C1 / pcrB / GK0274 (*Geobacillus kaustophilus* HTA426)

Current annotation state retrieved from QuickGO in this job. All recommendations are **leads requiring
curator verification**, not applied decisions.

| GO term | Aspect | Current evidence on Q5L3C1 | Assessment | Recommended action (lead) |
|---|---|---|---|---|
| GO:0120536 heptaprenylglyceryl phosphate synthase activity | MF | IEA GO_REF:0000120; IGI PMID:21761520; **EXP PMID:24684232** | Exact and experimentally supported for this protein. PDB 4NAE (2.0 A) is Q5L3C1 with ligand 1GP, sn-glycerol-1-phosphate | **Retain as core MF.** Highest-precision term available |
| GO:0004659 prenyltransferase activity | MF | IEA GO_REF:0000104; IDA PMID:21761520 | Correct but a parent of GO:0120536 | Retain or mark redundant with the child term; non-core |
| GO:0016765 transferase activity, transferring alkyl or aryl (other than methyl) groups | MF | IEA GO_REF:0000002 (InterPro) | Grandparent; uninformative on its own | Non-core; generalised ancestor of the supported MF |
| GO:0000287 magnesium ion binding | MF | IEA GO_REF:0000104 | Mechanistically plausible for this TIM-barrel prenyltransferase; no direct Mg assay cited for the Geobacillus protein | Retain as non-core; flag that the evidence is rule-based |
| GO:0046474 glycerophospholipid biosynthetic process | BP | IEA GO_REF:0000120; IGI PMID:21761520 | Chemically defensible (the product is a glycerophosphate bearing an O-alkyl group) but describes the product class, not the pathway the product serves. Predates PMID 40626731 | **Retain, but do not treat as the core BP.** Add a note that the product is not committed to membrane phospholipid |
| GO:0006650 glycerophospholipid metabolic process | BP | IEA GO_REF:0000041 | Parent of GO:0046474 | Non-core |
| GO:0042160 lipoprotein modification | BP | **not annotated** | Supported in *B. subtilis* by PMID 40626731, where Ac-HepG made by PcrB/YvoF "is required for lipoprotein acetylation". The shuttling step is stated as a proposal | **Candidate new BP lead.** If added for GEOKA, evidence would be ISS/IBA transferred from *B. subtilis*, with the caveat that no Geobacillus lipoprotein has been shown to be N-acetylated |
| GO:0006474 N-terminal protein amino acid acetylation | BP | not annotated | PcrB does not acetylate protein; it makes the precursor of the acetyl carrier | **Do not assign to PcrB.** Appropriate for LhaT/GK2189, not for PcrB |
| CC (any) | CC | none | Cytosolic by the PMID 40626731 model ("synthesized by PcrB/YvoF in the cytosol"); no localisation experiment on the Geobacillus protein | Optional GO:0005737 cytoplasm lead, evidence transferred; low priority |

## Related proteins in this genome (leads, not part of this gene's review)

| Protein | Locus | Evidence here | Candidate GO lead |
|---|---|---|---|
| YvoF ortholog | GK3078 (Q5KVC3) | 282.8 bits, E=1.3e-77 to O34993; reciprocally distinct from the MAT ortholog GK1921 | MF GO:0016407 acetyltransferase activity by ISS; BP GO:0042160 lead |
| LhaT/YpjA ortholog | GK2189 (Q5KXW2) | 281.9 bits, E=2.6e-77 to P54392; next-best hit 27.7 bits | BP GO:0006474 / GO:0042160 lead; CC membrane |
| PpaX (HAD phosphatase), co-operonic with GK3078 | GK3079 (Q5KVC2) | 4 bp overlap with GK3078; same arrangement in *B. subtilis* | **No GO lead.** Hypothesis only: candidate for the unassigned HepGP phosphatase step |
| Heptaprenyl diphosphate synthase | GK2212, GK2210 | orthologs of HepS/HepT | Supplies the C35 donor; already annotated |
| Glycerol-1-phosphate dehydrogenase | **absent** | three independent checks | Gap: the G1P acceptor has no identified source in this genome |
