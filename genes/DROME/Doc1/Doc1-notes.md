# Doc1 (Dorsocross1, Q9U8L5, unreviewed TrEMBL) — curation notes

Automated deep research was unavailable (falcon 402, OpenAI 401); no `-deep-research-<provider>.md`
generated. Notes from cached publications and UniProt.

## Identity and redundancy
- T-box, Tbx6-related; Doc1/2/3 clustered and redundant
  [PMID:12783790 "are expressed in identical patterns in embryos, and appear to be genetically redundant"];
  [PMID:14732398 "have a conserved T-box domain related to the vertebrate Tbx6 subfamily and act redundantly to induce dorsal structures"].
  Most loss-of-function data use deficiencies (Df(3L)DocA) removing all three genes or pan-Doc RNAi;
  annotations from such data apply to the Doc paralogs collectively.

## Molecular function
- Binds Toll dorsal vessel enhancer [PMID:15870289 "DNase I protection assays were used to demonstrate the in vitro binding of Doc1 and Doc2 to the Toll 305-bp dorsal vessel enhancer"] (full text); activator.
- Represses reaper HRE through a mapped site [PMID:19282966 "whereas Brinker (Brk), Disco, Dorsocross 1 (Doc1), En and Slp1 repressed lacZ expression"] (full text).

## Development
- Amnioserosa [PMID:12783790 "Dorsocross gene activity is crucial for the completion of differentiation, cell proliferation arrest, and survival of amnioserosa cells"].
- Heart: [PMID:16221729 "Dorsocross activity is required for the formation of all myocardial and pericardial cell types, with the exception of the Eve-positive pericardial cells"];
  activates pannier with tinman; later ostia [PMID:16221729 "the Dorsocross genes are re-expressed in a segmental subset of cardioblasts, which in the heart region develop into inflow valves (ostia)"];
  Tin restricts Doc to ostial cells [PMID:16987868].
- Wing disc primordium [PMID:14732398]; anterior Malpighian tubules [PMID:17190812]; thorax closure [PMID:35562934].

## Curation decisions
- GO:0001700 -> MODIFY to GO:0046665 amnioserosa maintenance; NEW GO:0046665 IMP PMID:12783790.
- GO:0010468 -> MODIFY to GO:0000122 (rpr repression via binding site).
- GO:0160108 ARBA -> MARK_AS_OVER_ANNOTATED (uninformative).
- GO:0007507 TAS from Hox review (abstract lacks Doc) -> ACCEPT on primary evidence.
- Module annoton GO:0000981 in heart development: consistent. Note no evidence of Doc physically binding Tin/Pnr in flies (the module's TBX5-NKX2-5 interaction is vertebrate-only).
