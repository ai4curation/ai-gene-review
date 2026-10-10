# tda1 (biosynthetic threonine deaminase, UniProt O94634, SPBC1677.03c) - notes

## Identity / NAMING TRAP
- PomBase tda1 = SPBC1677.03c = UniProt O94634 (UniProt has no gene name). It is the ortholog of S. cerevisiae **ILV1** (P00927), not of S. cerevisiae TDA1 (an unrelated protein kinase). Conversely S. pombe **ilv1** (P36620) is the acetolactate synthase (S. cerevisiae ILV2 ortholog).

## Function
- Threonine dehydratase/deaminase EC 4.3.1.19: "Reaction=L-threonine = 2-oxobutanoate + NH4(+); Xref=Rhea:RHEA:22108," [UniProt:O94634]; PLP cofactor; isoleucine inhibits, valine activates (by similarity).
- S. pombe enzyme characterised biochemically [PMID:4698209 "Biosynthetic threonine deaminase (TD) from Schizosaccharomyces pombe has been partially purified from crude extracts"; "TD showed marked stimulation by pyridoxal phosphate"; "the natural feedback inhibitor, l-isoleucine"; "l-Valine was found to reverse isoleucine inhibition"]. This regulatory behaviour matches S. cerevisiae Ilv1. Note this 1973 work used extracts; the assignment of the activity to SPBC1677.03c is by the PomBase curator.

## Localization
- Predicted mitochondrial transit peptide (FT TRANSIT 1..?) and Mitochondrion by similarity to P00927 [UniProt:O94634].
- ORFeome HDA: cytoplasm [PMID:16823372]. Conflicts with the mitochondrial prediction; PomBase also has IC mitochondrial matrix and the GO-CAM places the activity in the matrix.

## GO-CAM
- gomodel:6690711d00002706: SPBC1677.03c enables GO:0004794, occurs_in GO:0005759 mitochondrial matrix, part_of GO:1901705 (IDA PMID:4698209 + IBA). No causal edge to AHAS (ilv1).
