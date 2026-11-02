# dpm1 (S. pombe, SPAC31G5.16c, UniProt O14466) notes

## Identity
- UniProt O14466 (DPM1_SCHPO), 236 aa, PomBase SPAC31G5.16c; fetched accession verified against the request.
- Glycosyltransferase family 2; PANTHER PTHR43398:SF1 [UniProt:O14466].

## Function
- Catalytic subunit of dolichol-phosphate-mannose (Dol-P-Man) synthase, EC 2.4.1.83 (by similarity to human O60762) [UniProt:O14466 "Transfers mannose from GDP-mannose to dolichol monophosphate"].
- Cloned by Colussi et al.; the gene is essential: [PMID:9223280 "Disruption of the gene for the S. pombe Dol-P-Man synthase homolog, dpm1(+), is lethal."]
- Belongs to the human-type class lacking a C-terminal TM anchor: [PMID:9223280 "the other contains the human, S. pombe, and Caenorhabditis synthases, which lack a hydrophobic COOH-terminal domain"].
- Functional equivalence with S. cerevisiae DPM1 and human DPM1, which both rescue the null [PMID:9223280 "S. cerevisiae DPM1 and its human counterpart both complement the lethal null mutation in S. pombe dpm1(+)"]; membranes of rescued haploids had Dol-P-Man synthase activity [PMID:9223280 "Membranes prepared from the uracil plus histidine-prototrophic haploids all had in vitro Dol- P -Man synthase activity (not shown)."]. No GOA row uses this paper; the MF is supported only by ISS/IBA/IEA in GOA, but the paper supports it for the S. pombe protein (complementation by heterologous enzymes plus the 65% identity to human DPM1).
- S. pombe has all three subunits [PMID:10835346 "Schizosaccharomyces pombe has proteins that resemble three human subunits"].

## Location
- ER (and cytoplasm) in the ORFeome YFP screen [PMID:16823372]. As a TM-less catalytic subunit it sits on the cytoplasmic face of the ER membrane, tethered by dpm3 (human data, PMID:16280320).

## Comparison with S. cerevisiae DPM1 (genes/yeast/DPM1)
- Same MF (GO:0004582) and BP (GO:0180047). Difference: S. cerevisiae Dpm1 is a single-subunit anchored enzyme; S. pombe dpm1 is the catalytic subunit of the three-subunit complex (GO:0033185).

## GO-CAM
- PomBase gomodel:671ae02600003596 activity 671ae02600003597: dpm1 enables GO:0004582, occurs_in ER membrane, part_of GO:0180047 (IBA). Agrees.

## Annotation notes
- GO:0046474 glycerophospholipid biosynthetic process (ARBA): Dol-P-Man is a polyprenyl-phosphate sugar, not a glycerophospholipid; the term can only be reached through the downstream GPI-anchor use. Over-annotation.
- GO:0051604 protein maturation (ARBA): too indirect.
