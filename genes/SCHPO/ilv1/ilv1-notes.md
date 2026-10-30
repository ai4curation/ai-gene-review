# ilv1 (acetolactate synthase catalytic subunit, UniProt P36620, SPBP35G2.07) - notes

## Identity / NAMING TRAP
- PomBase ilv1 = SPBP35G2.07 = UniProt P36620 = acetohydroxyacid synthase (AHAS) catalytic subunit; ortholog of S. cerevisiae **ILV2** (P07342), NOT of S. cerevisiae ILV1 (threonine deaminase, whose S. pombe ortholog is tda1).

## Function
- Acetolactate synthase EC 2.2.1.6: "Reaction=2 pyruvate + H(+) = (2S)-2-acetolactate + CO2;" [UniProt:P36620]; ThDP, Mg2+ cofactors; FAD (flavoprotein keyword). First step of valine (and leucine) synthesis, second step of isoleucine synthesis [UniProt:P36620 PATHWAY lines].
- Gene cloned; complements S. cerevisiae ilv2 deletion [PMID:8299177 "The putative ilv1 isolated from S. pombe was shown to encode a functional subunit of acetolactate synthase by complementation of an S. cerevisiae strain deleted for the ILV2 locus."].
- S. pombe AHAS enzymology [PMID:4698210 "The regulatory properties of acetohydroxy acid synthetase (AHAS), the first enzyme in the biosynthetic pathway to valine and the second in the isoleucine pathway, were investigated in the fission yeast Schizosaccharomyces pombe."; valine feedback "K(i) = 0.1 mM"]. Extract-based; gene assignment by curator.
- PMID:4821071 is abstract-less in cache (regulation of BCAA enzymes); IDA rows deferred to curator.

## Localization
- Transit peptide 1..140 (Mitochondrion) [UniProt:P36620]; mitochondrion HDA [PMID:16823372]; PomBase IC mitochondrial matrix.

## Complex
- IBA part_of acetolactate synthase complex; S. cerevisiae Ilv2 forms complex with Ilv6. A S. pombe regulatory subunit was not checked here.

## GO-CAM
- gomodel:6690711d00002706: two ilv1 activities, both GO:0003984 in mitochondrial matrix; one part_of L-leucine biosynthetic process (GO:0009098), one part_of L-isoleucine biosynthetic process (GO:1901705). No activity part_of L-valine biosynthesis even though valine is the immediate product branch of acetolactate.
