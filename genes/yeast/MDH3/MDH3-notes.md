# MDH3 notes (P32419, YDL078C)

- Third isozyme, SKL PTS1, peroxisomal [PMID:1447211 "The MDH3 sequence was found to contain a carboxyl-terminal SKL tripeptide, characteristic of many peroxisomal enzymes, and immunochemical analysis was used to confirm organellar localization of the MDH3 isozyme."]
- Triple mutant lacks MDH activity [PMID:1447211 "Combined disruption of MDH1, MDH2, and MDH3 loci in a haploid strain resulted in the absence of detectable cellular malate dehydrogenase activity."]
- Beta-oxidation NADH reoxidation, not glyoxylate cycle [PMID:7628449 "suggesting that MDH3 is involved in the reoxidation of NADH generated during fatty acid beta-oxidation rather than functioning as part of the glyoxylate cycle"]
- Matrix import as dimer [PMID:8824293 "Because we show that dimerization of MDH3 precedes import into the organelle"]

## Decisions
- Mitochondrion IBA and TCA cycle IBA/IEA from the MDH1 clade -> REMOVE (paralog relocated to peroxisomes).
- Cytosol RCAs (glyoxylate pathway, PWY3O-94) -> REMOVE.
- Glyoxylate cycle RCA -> non-core (contested: mild acetate defect vs van Roermund data).
- Module note: YeastCyc assigns MDH3 to gluconeogenesis I/TCA via the superpathway; evidence supports only a peroxisomal redox-shuttle role.
