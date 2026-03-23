# pcaH notes

- UniProt `Q88E12` maps `pcaH` to locus tag `PP_4656` and describes the product as `Protocatechuate 3,4-dioxygenase beta chain`; the entry also assigns EC `1.13.11.3` and places the protein in the intradiol ring-cleavage dioxygenase family. [file:PSEPK/pcaH/pcaH-uniprot.txt, "Name=pcaH"; "OrderedLocusNames=PP_4656"; "Protocatechuate 3,4-dioxygenase beta chain"; "Belongs to the intradiol ring-cleavage dioxygenase family"]

- Classic Pseudomonas biochemical genetics identifies `pcaH` and `pcaG` as the genes for the beta and alpha subunits of protocatechuate 3,4-dioxygenase. [PMID:8407791, "two successive open reading frames, designated pcaH and pcaG, corresponding to the beta and alpha subunits, respectively, of 3,4-PCD"]

- The purified P. putida enzyme is a ferric-iron-containing multimer with `4 beta subunits` and `4 ferric irons`, supporting ferric iron binding as a real catalytic property of the complex rather than only a family prediction. [PMID:6273403, "Protocatechuate dioxygenase from P. putida has a molecular weight of 200,000 and contains 4 alpha subunits of 23,000 daltons, 4 beta subunits of 26,500 daltons, and 4 ferric irons"; "the minimal catalytic unit of all non-heme iron intradiol dioxygenases is an (alpha beta Fe+3) structure"]

- Mechanistic work on the same P. putida enzyme states that protocatechuate chelates the active-site `Fe(III)`, reinforcing that the enzyme is ferric-iron-dependent. [PMID:16101286, "The active site Fe(III) of protocatechuate 3,4-dioxygenase (3,4-PCD) from Pseudomonas putida"; "protocatechuate (3,4-dihydroxybenzoate, PCA) chelates the iron"]

- KT2440 engineering papers use `pcaHG` knockout to block protocatechuate consumption and reroute PCA into product pathways, which is strong strain-specific evidence that the locus performs the protocatechuate ring-cleavage step in this background. [PMID:29188181, "The lignin monomers p-coumarate and ferulate are metabolized via protocatechuate, which is redirected to catechol by deletion of pcaHG and integration of aroY"]; [PMID:38611834, "all six phenolic compounds in hydrolysates could be converted into PCA and then split by pcaGH"; "it has been found that knocking out of the gene pcaGH is necessary for the accumulation of PCA"; "As for the construction of a pcaGH (PP_4655-4656) disruption mutant"]

- Curation direction:
  - `GO:0018578 protocatechuate 3,4-dioxygenase activity` should be core.
  - `GO:0019619 3,4-dihydroxybenzoate catabolic process` should be core.
  - `GO:0008199 ferric iron binding` is supported by primary enzymology and should be retained.
  - `GO:0005506 iron ion binding` is correct but redundant with ferric iron binding.
  - `GO:0016702` is a reasonable higher-level parent but non-core because the specific dioxygenase term is present.
  - `GO:0003824 catalytic activity` is too generic to keep as informative biology.
