# ADH3 notes

## Shared ADH family evidence
- Any of ADH1-5 or SFA1 suffices for the final Ehrlich step [PMID:12499363 "the final step of amino acid catabolism (conversion of an aldehyde to a long chain or complex alcohol) can be accomplished by any one of the ethanol dehydrogenases (Adh1p, Adh2p, Adh3p, Adh4p, Adh5p) or by Sfa1p (formaldehyde dehydrogenase.)"]
- Quadruple-deletion (single-ADH) strains [PMID:22094012 "Adh1 was the only alcohol dehydrogenase capable of efficiently catalysing the reduction of acetaldehyde to ethanol"]; [PMID:22094012 "Strains Q2 and Q3, expressing only ADH2 or ADH3, respectively, produced ethanol from glucose, albeit less than strain Q1, and were also able to oxidise added ethanol."]; [PMID:22094012 "Strains Q4 and Q5 grew poorly on glucose and produced ethanol, but were neither able to utilise the produced ethanol nor grow on added ethanol."]
- Compartments [PMID:2937632 "two in the cytoplasm (ADHI and ADHII) and one in the mitochondrion (ADHIII)"]

## Systematic YeastPathways (RCA) issues seen across ADH1-5
- GLUCFERMEN-PWY maps to GO:0019658 "bifid shunt" (Bifidobacterium pathway) - REMOVE for all ADHs.
- Pathway-default cytosol: wrong for ADH3 (matrix; REMOVE), unsupported for ADH4 (mitochondrial in HTP; over-annotated).
- Ethanol degradation (PWY3O-4300) attached to all five ADHs; ADH4/ADH5 cannot support growth on ethanol (REMOVE).

## ADH3-specific
- Matrix [PMID:3550419 "Alcohol dehydrogenase isoenzyme III (ADH III) in Saccharomyces cerevisiae, the product of the ADH3 gene, is located in the mitochondrial matrix."]
- "inside the mitochondrial inner membrane" [PMID:2937632 "Here we demonstrate that ADHIII is located inside the mitochondrial inner membrane."] was read as inner membrane by EXP/IEA rows -> MODIFY to matrix.
- Redox shuttle [PMID:10940011 "Here we demonstrate that this is due to in vivo activity of an ethanol-acetaldehyde redox shuttle, which transfers the redox equivalents from the mitochondria to the cytosol."]
- No GO term for the mitochondrial NADH/ethanol-acetaldehyde shuttle; used ethanol metabolic process in core_functions.
