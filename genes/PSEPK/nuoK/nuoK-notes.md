# nuoK notes

- NuoK is a small integral-membrane subunit that helps connect quinone-site
  chemistry to the distal membrane arm [file:PSEPK/nuoK/nuoK-uniprot.txt
  "RecName: Full=NADH-quinone oxidoreductase subunit K"].

- GO:0050136 is removed because a non-electrogenic activity is incompatible
  with proton-translocating complex I.

## 2026-11-01 rework

Earlier draft quoted only the RecName. It was reworked to quote HAMAP MF_01456 text
(function, reaction, subunit, location), with the E. coli orthologue's literature
(PMID:15996109, PMID:21822288, PMID:36920092) used by orthology. Deep-research providers
are unavailable here (no API keys). GO:0016651 MODIFY to GO:0008137; GO:0030964 (TreeGrafter)
MODIFY to GO:0045271; GO:0042773 ACCEPT as core (P. putida is a strict aerobe); GO:0050136 REMOVE
(non-electrogenic term wrong for NDH-1; same HAMAP rule gives RHEA:57888).
