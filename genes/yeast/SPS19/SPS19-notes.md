# SPS19 (YNL202W, UniProt P32573) notes

Module: `peroxisomal_beta_oxidation` (decr_activity). Missing from YeastCyc YEAST-FAO-PWY.

## Evidence journal
- Purified homodimer reduces 2,4-hexadienoyl-CoA to 3-hexenoyl-CoA with NADPH; peroxisomal matrix [PMID:9268358 "converted 2,4-hexadienoyl-CoA into 3-hexenoyl-CoA in an NADPH-dependent manner and therefore contained 2,4-dienoyl-CoA reductase activity."; "Antibodies raised against Sps19p decorated the peroxisomal matrix of oleate-induced cells."].
- sps19 cannot use petroselinate, grows on oleate [PMID:9268358 "an SPS19 deleted strain was unable to utilize petroselineate (cis-C18:1(6)) as the sole carbon source, but remained viable on oleate (cis-C18:1(9))."]; dispensable for sporulation on acetate [PMID:9268358 "SPS19 is dispensable for growth and sporulation on solid acetate and oleate media"].
- Sporulation IMP (PMID:7969036) used a deletion of the shared SPS18/SPS19 promoter [PMID:7969036 "A null mutation deleting the intergenic promoter prevented expression of both genes"] -> cannot be attributed to SPS19; MARK_AS_OVER_ANNOTATED.
- UniProt: EC 1.3.1.124, (3E)-enoyl-CoA producing; PTS1 SKL [UniProt:P32573].

## Curation decisions
- Core MF GO:0008670, BP GO:0009062, CC GO:0005782.
- GO has no unsaturated-fatty-acid beta-oxidation term; suggested question raised.
