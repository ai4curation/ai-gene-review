# cemA notes

- The GOA file is header-only, so there are no existing GOA annotations to review or convert into NEW rows.
- UniProt identifies cemA as a plastid-encoded envelope membrane protein and supports membrane localization plus proton transmembrane transport [file:MISSI/cemA/cemA-uniprot.txt "SubName: Full=Envelope membrane protein"] [file:MISSI/cemA/cemA-uniprot.txt "GO; GO:1902600; P:proton transmembrane transport"].
- I used chloroplast envelope as the location based on the plastid-encoded gene context and the PANTHER subfamily assignment [file:MISSI/cemA/cemA-uniprot.txt "PANTHER; PTHR33650:SF2; CHLOROPLAST ENVELOPE MEMBRANE PROTEIN"].
- The core-function support now cites both the UniProt PANTHER cross-reference and a PTHR33650 entries CSV row with the same chloroplast envelope membrane protein subfamily assignment [file:interpro/panther/PTHR33650/PTHR33650-entries.csv "P46641,Potassium/proton antiporter CemA"].
- I did not assign potassium:proton antiporter activity as a core molecular function because the Miscanthus UniProt entry lacks the detailed K(+)/H(+) reaction present in some reviewed CemA homologs.
