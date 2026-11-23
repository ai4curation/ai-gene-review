# soxA (P40873) notes

## 2026-11-04 initial review

- Reviewed from scratch from the 5 GOA rows (all IEA). No provider deep research was generated in this
  session (no API keys available); evidence comes from the Swiss-Prot entry and cached abstracts
  (PMID:9563845, PMID:7887617, PMID:8779579, PMID:11035956, PMID:9185627; all abstract-only).
- Direct TE1826 evidence: sarcosine oxidase activity assayed in purified wild-type and mutant enzymes
  [PMID:8779579 "Most of them showed inhibited or remarkably decreased sarcosine oxidase activity"];
  covalent FAD at Cys318 [PMID:11035956 "The covalent flavin attachment site in the Arthrobacter sarcosine
  oxidase (cysteine at position 318)"].
- Numbering: PMID:8779579 numbers D-35 and the motif 12-17 from the mature N-terminus; UniProt features use
  Asp36 and 13-18. C265/C318 are the same in the papers and UniProt.
- Folate: monomeric enzymes do not use THF [PMID:9185627 "only the heterotetrameric sarcosine oxidases can use
  tetrahydrofolates as substrates"]; the abstract does not name which monomeric enzymes were tested, so this is
  family-level support. GO:0008115 (formaldehyde-forming reaction) is therefore the correct MF, consistent with
  the module (modules/bacterial_dimethylglycine_sarcosine_catabolism.yaml).
- Bacillus sp. B-0618 MSOX structural work (separate UniProt entry) was not transferred to this protein.
- Actions: cytoplasm ACCEPT; GO:0008115 ACCEPT (core); GO:0050660 ACCEPT; GO:0016491 and GO:0016647
  TOO_GENERAL (both strict ancestors of the accepted GO:0008115; MODIFY to GO:0008115 would duplicate that row).
- No BP added: GO sarcosine catabolic process (GO:1901053) is obsolete; GO:0006602 creatinine catabolic
  process is suggested only by the gene cluster [PMID:9563845], with no physiological data, so left as a
  suggested question.
- P40873 is the reference protein for PANTHER PTHR10961 (subfamily SF7 per UniProt DR line).


## 2026-11-06 comparative module audit

Persistent marker DMG-ARTST-soxA-20261106. Reviewed every original row, inherited proposal, core and cited source. Default Falcon was attempted normally because no provider artifact existed; HTTP403 authentication/access failure is logged. These are manual notes, not a fabricated provider report.

- Retained all five annotation decisions and the direct monomeric sarcosine oxidase core.
- Clarified enzymatic folate coupling versus possible nonenzymatic formaldehyde trapping; family-level comparative evidence is not relabeled as an exact TE1826 assay.

Original machine payloads, inherited NEW rows and raw files are protected by original-members-baseline.json. Source limitations are explicit: many original primary citations remain abstract-only, with curated UniProt evidence and direct deposited structure mappings used for corroboration. No inaccessible experimental annotation was rejected merely for missing full text.
