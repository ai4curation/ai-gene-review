# PhyB notes

- The GOA file is header-only, so there are no existing GOA annotations to review or convert into NEW rows.
- UniProt identifies this as a Phytochrome B fragment and describes reversible red/far-red photoconversion that controls morphogenic and transcriptional responses [file:MISSI/PhyB/PhyB-uniprot.txt "SubName: Full=Phytochrome B"] [file:MISSI/PhyB/PhyB-uniprot.txt "Regulatory photoreceptor which exists in two forms that are reversibly interconvertible by light"].
- Core curation uses photoreceptor activity, detection of visible light, and regulation of DNA-templated transcription from the UniProt GO cross-references [file:MISSI/PhyB/PhyB-uniprot.txt "GO; GO:0009881; F:photoreceptor activity"] [file:MISSI/PhyB/PhyB-uniprot.txt "GO; GO:0009584; P:detection of visible light"] [file:MISSI/PhyB/PhyB-uniprot.txt "GO; GO:0006355; P:regulation of DNA-templated transcription"].
- I did not assign nucleus or photobody localization because this fragment entry has no subcellular-location line.
- I flagged the GO:0006355 transcription-regulation call as an expert question because phytochrome signaling can affect transcription indirectly downstream of light perception.
- PANTHER PTHR47876:SF3 is named PHYTOCHROME 1 and includes PhyA, PhyB, and PhyC proteins, so the PhyB subtype call rests on the EMBL/UniProt submission name rather than a PhyB-specific PANTHER subfamily [file:interpro/panther/PTHR47876/PTHR47876-entries.csv "P14713,Phytochrome B"] [file:interpro/panther/PTHR47876/PTHR47876-entries.csv "P14714,Phytochrome C"].
