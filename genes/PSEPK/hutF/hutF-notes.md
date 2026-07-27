# hutF curation notes

- Q88CZ3 is an unreviewed, predicted formimidoylglutamate deiminase with EC 3.5.3.13 and a predicted zinc cofactor. [file:PSEPK/hutF/hutF-uniprot.txt, "RecName: Full=Formimidoylglutamate deiminase"] [file:PSEPK/hutF/hutF-uniprot.txt, "Name=Zn(2+)"]
- HutF-specific support comes from IPR010252, the HutF N-terminal domain IPR055156/PF22429, and NCBIfam TIGR02022. [file:PSEPK/hutF/hutF-uniprot.txt, "DR   InterPro; IPR010252; HutF."] [file:PSEPK/hutF/hutF-uniprot.txt, "DR   NCBIfam; TIGR02022; hutF; 1."]
- HutF is curated as converting N-formimidoyl-L-glutamate to N-formyl-L-glutamate plus ammonia; HutG then releases glutamate plus formate. This two-enzyme route must not be conflated with direct formamide release from N-formimidoyl-L-glutamate. [file:PSEPK/hutF/hutF-uniprot.txt, "L-histidine catabolic process to glutamate and formate"] [file:PSEPK/hutG/hutG-uniprot.txt, "N-formylglutamate deformylase activity"]
- PTHR11271 is broad and named guanine deaminase at family level, while Q88CZ3 is assigned only to an amidohydrolase-related subfamily in UniProt and is absent from the local family member snapshot. The PANTHER family was not used to propagate guanine deaminase activity. [file:PSEPK/hutF/hutF-uniprot.txt, "PTHR11271:SF48; AMIDOHYDROLASE-RELATED DOMAIN-CONTAINING PROTEIN"]
- The mapped P. putida hut locus directly identifies hutF as encoding
  formiminoglutamate hydrolase. [PMID:2842309 "hutF, encoding
  formiminoglutamate hydrolase"]
- Generic hydrolase and deaminase terms were marked over-annotated. The locus
  paper supports gene identity and pathway membership, but no purified KT2440
  HutF assay was identified in this pass.
