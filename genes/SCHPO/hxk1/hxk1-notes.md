# hxk1 (S. pombe, SPAC24H6.04, UniProt Q09756) notes

## Identity
- UniProt Q09756 (HXK1_SCHPO), 484 aa; PANTHER PTHR19443:SF16 [UniProt:Q09756].
- Naming trap: S. pombe hxk1/hxk2 numbering was assigned independently of S. cerevisiae HXK1/HXK2 (PMID:8549830); the names do not imply 1:1 orthology.

## Function
- Unusual hexokinase with poor glucose phosphorylation: [PMID:8549830 "hexokinase 1, with a low phosphorylation coefficient on glucose (Km 8.5 mM)"].
- Kinetics [UniProt:Q09756 "KM=1.5 mM for D-fructose"; "KM=9.4 mM for D-glucose"; "KM=0.2 mM for D-mannose"]; Vmax fructose/glucose = 5 [PMID:9790975 "This mutation decreased Km for glucose from 9.4 mM to 1.6 mM and the ratio Vmax (Fructose)/Vmax (Glucose) from 5 to 2.5."].
- A conserved Asn in the glucose-binding region is Ser213 in hxk1 [PMID:9790975].
- hxk1 alone cannot support glucose fermentation [PMID:9790975 "Fermentation of glucose is not detectable in a S. pombe mutant with only hexokinase 1 activity"].
- Induced on fructose/glycerol [PMID:8549830 "Expression of hxk1+ increased strongly during growth in fructose or glycerol."]; hxk1 hxk2 double disruptant does not grow on glucose or fructose [PMID:8549830].
- No glucokinase (glucose-specific enzyme) in S. pombe [PMID:8549830 "A NADP-dependent glucose dehydrogenase was detected, but not a glucokinase."]. The GO term "glucokinase activity" (GO:0004340) is just the glucose-phosphorylating reaction, so it still applies to hexokinases.

## Location
- Cytosol (ORFeome screen PMID:16823372; PomBase GO-CAM).
- GO:0032473 (cytoplasmic side of mitochondrial outer membrane) IBA and IC rows: mammalian HK1/HK2 binding to VDAC via an N-terminal helix; no S. pombe evidence; the IC row contradicts PomBase's own GO-CAM (cytosol).

## Comparison with S. cerevisiae HXK1/HXK2 reviews
- Same core MF (GO:0004396), cytosol. S. pombe-specific: hxk1 is a low-glucose-affinity enzyme whose physiological substrates are fructose and mannose; it cannot sustain glucose fermentation on its own.

## GO-CAM
- gomodel:663d668500002302 activity 663d668500002664: hxk1 enables GO:0004396 (IDA PMID:8549830), cytosol, part_of GO:0061621 canonical glycolysis (term obsolete in GOA; the replacement is GO:0006096 glycolysis).
