# PP_4677 review notes

## Identity and pathway role

- Target: `PP_4677`, UniProt Q88DZ1, *Pseudomonas putida* KT2440.
- Q88DZ1 is a 283-residue, eight-pass member of the integral-membrane
  CDP-alcohol phosphatidyltransferase family.
- The specific IPR004533 and PTHR14269:SF61 assignments distinguish a
  phosphatidylserine synthase candidate from broader members of this
  phosphatidyltransferase superfamily.

## Exact provenance

Source: `file:PSEPK/PP_4677/PP_4677-uniprot.txt`.

- `"DE   RecName: Full=CDP-diacylglycerol--serine O-phosphatidyltransferase"`
- `"CC       Reaction=a CDP-1,2-diacyl-sn-glycerol + L-serine = a 1,2-diacyl-sn-"`
- `"CC       {ECO:0000256|ARBA:ARBA00004127}; Multi-pass membrane protein"`
- `"DR   InterPro; IPR004533; CDP-diaglyc--ser_O-PTrfase."`
- `"DR   PANTHER; PTHR14269:SF61; CDP-DIACYLGLYCEROL--SERINE O-PHOSPHATIDYLTRANSFERASE; 1."`
- `"DR   GO; GO:0003882; F:CDP-diacylglycerol-serine O-phosphatidyltransferase activity; IEA:UniProtKB-EC."`

The organism-specific lipidomics paper reconstructs the KT2440
glycerophospholipid pathway with both `pssA` and `pssA-2` upstream of `psd`
[PMID:21895997, "Biosynthesis routes of glycerophospholipids and fatty acids in P. putida."].

Normalized curation statements used as exact YAML support:

- `"Q88DZ1 carries the specific IPR004533 and PTHR14269:SF61 phosphatidylserine synthase assignments."`
- `"PP_4677 is an eight-pass membrane protein predicted to form phosphatidylserine from CDP-diacylglycerol and L-serine."`
- `"The phosphatidylserine product supplies the consecutive Psd reaction in phosphatidylethanolamine biosynthesis."`

## Curation conclusions

- Accept GO:0003882 as the specific predicted molecular function.
- Accept membrane localization; the eight predicted transmembrane helices
  establish an integral-membrane architecture.
- Keep the broad phospholipid-biosynthesis process as non-core and add the
  more specific phosphatidylethanolamine-biosynthesis process.
- Mark GO:0016780 over-annotated because GO:0003882 captures the same activity
  with the correct donor and acceptor specificity.
- Treat Q88DZ1 as a strong type-II PssA candidate, not as experimentally
  proven to carry most pathway flux. Its contribution relative to the
  PLD-superfamily type-I candidate Q88GQ4 remains unresolved.
- The type-I/type-II labels here follow the bacterial PssA nomenclature of
  PMID:39693441. UniProt's statement that Q88DZ1 belongs to the CDP-alcohol
  phosphatidyltransferase "class-I family" uses a separate family-classification
  axis and therefore does not make Q88DZ1 a type-I PssA.
