# YPC1 (YBR183W, P38298) notes

## Identity and activity
- ACER-family alkaline ceramidase; hydrolyses phyto- and dihydroceramide, not unsaturated ceramide [PMID:10702247 "We demonstrate that the yeast gene YPC1 encodes an alkaline ceramidase activity responsible for the breakdown of dihydroceramide and phytoceramide but not unsaturated ceramide."].
- Reverse, CoA-independent ceramide synthase [PMID:10702247 "This ceramide synthase activity is CoA-independent and is resistant to fumonisin B1"]; in vivo prefers C24/C26 [PMID:24866405 "when working backwards as a ceramide synthase in vivo, Ypc1p prefers C24 and C26 fatty acids as substrates"].
- Cortical ER [UniProt:P38298 "Localizes to the cortical ER."].

## Curation decisions
- GO:0050291 sphingosine N-acyltransferase activity (acyl-CoA dependent, EC 2.3.1.24; IMP + 2 IGI) -> MODIFY to GO:0017040: Ypc1 ceramide synthesis is the CoA-independent reverse of its amidohydrolase reaction.
- Rhea IEA RHEA:38891 (unsaturated C16 ceramide hydrolysis) conflicts with the cloning paper abstract; GO term itself fine, Rhea assignment in UniProt questionable.
- Note: GO obsoleted phytoceramidase (GO:0070774) and dihydroceramidase (GO:0071633); GO:0017040 is now the general ceramidase term.
- RCA cytosol -> MODIFY to ER membrane.
