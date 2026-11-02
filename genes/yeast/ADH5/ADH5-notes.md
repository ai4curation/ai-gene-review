# ADH5 notes

## Shared ADH family evidence
- Any of ADH1-5 or SFA1 suffices for the final Ehrlich step [PMID:12499363 "the final step of amino acid catabolism (conversion of an aldehyde to a long chain or complex alcohol) can be accomplished by any one of the ethanol dehydrogenases (Adh1p, Adh2p, Adh3p, Adh4p, Adh5p) or by Sfa1p (formaldehyde dehydrogenase.)"]
- Quadruple-deletion (single-ADH) strains [PMID:22094012 "Adh1 was the only alcohol dehydrogenase capable of efficiently catalysing the reduction of acetaldehyde to ethanol"]; [PMID:22094012 "Strains Q2 and Q3, expressing only ADH2 or ADH3, respectively, produced ethanol from glucose, albeit less than strain Q1, and were also able to oxidise added ethanol."]; [PMID:22094012 "Strains Q4 and Q5 grew poorly on glucose and produced ethanol, but were neither able to utilise the produced ethanol nor grow on added ethanol."]
- Compartments [PMID:2937632 "two in the cytoplasm (ADHI and ADHII) and one in the mitochondrion (ADHIII)"]

## Systematic YeastPathways (RCA) issues seen across ADH1-5
- GLUCFERMEN-PWY maps to GO:0019658 "bifid shunt" (Bifidobacterium pathway) - REMOVE for all ADHs.
- Pathway-default cytosol: wrong for ADH3 (matrix; REMOVE), unsupported for ADH4 (mitochondrial in HTP; over-annotated).
- Ethanol degradation (PWY3O-4300) attached to all five ADHs; ADH4/ADH5 cannot support growth on ethanol (REMOVE).

## ADH5-specific
- WGD paralog of ADH1 [PMID:10974568 "the alcohol dehydrogenase genes ADH1 and ADH5 are part of a duplicated block of genome"]
- Unlikely fermentative contributor [PMID:22094012 "Transcription profiles of the ADH4 and ADH5 genes suggested that participation of these gene products in ethanol production from glucose was unlikely."]
- No purified-enzyme data for ADH5; MF rests on ISS + IGI (Ehrlich).
