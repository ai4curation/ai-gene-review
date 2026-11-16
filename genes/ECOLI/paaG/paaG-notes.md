# paaG (P77467) notes — E. coli K-12 1,2-epoxyphenylacetyl-CoA isomerase

## Deep research
- 2026-10-23: `just deep-research-falcon ECOLI paaG` failed ("Exception: Failed to authenticate"). No deep-research file.

## Function
- Purified His-tagged PaaG reversibly isomerizes ring 1,2-epoxyphenylacetyl-CoA to oxepin-CoA (EC 5.3.3.18).
  [PMID:20660314 "We purified his-tagged PaaG and found that it catalyzed a reversible conversion of the epoxide to a new product"]
  [PMID:20660314 "PaaG therefore acted as a ring 1,2-epoxyphenylacetyl-CoA isomerase (oxepin-CoA–forming)."]
- Crotonase superfamily; resembles delta3,delta2-enoyl-CoA isomerases with a single catalytic Asp.
  [PMID:20660314 "It shares greatest similarity with Δ 3 ,Δ 2 -enoyl-CoA isomerases, containing a single conserved aspartic acid in the active center acting as a proton relay"]
- Probable second role: 3,4- to 2,3-dehydroadipyl-CoA isomerization after the first PaaJ thiolysis — stated as
  "probably" by Teufel 2010 and modelled structurally by Grishin 2012; not directly assayed. Not annotated (kept as a question).
- paaG deletion mutant cannot grow on phenylacetate and accumulates ring-1,2-dihydroxy-1,2-dihydrophenylacetyl lactone
  [PMID:12846838].
- PaaG forms homotrimeric discs and a stable PaaF-PaaG hetero-complex (four-layer sandwich; PDB 4FZW); active site
  adapted to Paa intermediates, steric hindrance prevents octanoyl conformations [PMID:22961985]. This argues against
  the IBA to fatty acid beta-oxidation (propagated from mammalian ECH/ECI homologs).

## GOA review summary
- GO:0016853 isomerase activity IDA -> MODIFY to GO:0016863 (intramolecular oxidoreductase activity, transposing C=C bonds; the EC 5.3.3 class containing EC 5.3.3.18). No GO term exists for EC 5.3.3.18 itself; proposed new term.
- GO:0010124 x3 ACCEPT; GO:0006635 IBA REMOVE; GO:0005515 REMOVE (policy); GO:0042802 and GO:1902494 KEEP_AS_NON_CORE.
