# FUR1 (P18562, YHR128W) notes

Module: `pyrimidine_salvage`, role = uracil phosphoribosyltransferase (uracil + PRPP -> UMP + PPi, EC 2.4.2.9). YeastCyc: YEAST-RNT-SALV.

## Evidence journal
- Activity [PMID:2189783 "The FUR1 gene of Saccharomyces cerevisiae encodes uracil phosphoribosyltransferase (UPRTase) which catalyses the conversion of uracil into uridine 5'-monophosphate (UMP) in the pyrimidine salvage pathway."]
- Only UPRTase [PMID:2189783 "indicate that the FUR1 encoded protein possesses only UPRTase activity"]
- Regulation [PMID:1913872 "uracil, as a free base, induces a significative increase in transcription and UPRTase activity"]; fur1-5 R134S alters UTP regulation.
- GTP activation and Mg-PRPP by similarity; Fur1-Urk1 interaction in 4 HTP datasets [UniProt:P18562].

## Decisions
- All MF/BP rows ACCEPT; UMP salvage is the most precise BP. Cytoplasm IC and cytosol RCA ACCEPT (plausible, not directly measured).
- protein binding (Urk1) x4 REMOVE (uninformative), but flag the reproducible Fur1-Urk1 association.
