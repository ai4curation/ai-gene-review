# ssuD curation notes

## Molecular function and PAINT provenance

- The exact substrate-specific term is GO:0008726 alkanesulfonate
  monooxygenase activity. The broad GO:0016705 oxygenase parent is therefore
  `MODIFY` to GO:0008726, which already exists as a separate accepted GOA row;
  downstream curation should not create a duplicate annotation.
- The GOA row carries PANTHER:PTN002450490 as TreeGrafter provenance. The local
  canonical PTHR42847 PAINT table instead identifies ancestral node
  PTN000768559, seeded by E. coli SsuD P80645, for GO:0008726 and GO:0046306.
  These identifiers describe different provenance objects and are not
  interchangeable.

## Localization restraint

The Falcon report calls a cytosolic site "most consistent" with the reaction
context [file:PSEPK/ssuD/ssuD-deep-research-falcon.md, "most consistent with a
**cytosolic** site of reaction"], but the exact Q88R95 UniProt record has no
subcellular-location assertion and no target-specific localization experiment
was identified. No cellular-component annotation is proposed from this indirect
context alone.


## 2026-10-26 — independent member audit

Reassessed every existing annotation/proposal with unchanged term, evidence, reference, qualifier and donor fields. No new row was added. Family and role inference are separated from native target assays. The 2000 E. coli deletion study is available in a normal PMC URL cache; full S-313 PMID:10781557 exposes transporter redundancy and conditional SsuE dispensability. These are not KT2440 knockout results.

A fresh literature search found Garret William O'Connell's 2024 DTU thesis, chapter 1: native KT2440 ΔssuD and combined ΔssuBC growth tests, strain mapping, and Figure 4 were inspected. The chapter was a manuscript in preparation; a matching journal publication was not established. The experiments support target pathway placement but do not isolate individual B/C activities, or test individual A/E necessity. Composite growth fitness is not a direct import-rate measurement, and the source documents contamination concerns for some sulfur compounds. The full normal URL cache is in publications/. No direct target kinetic constants, expanded substrate spectrum or PFAS-degradation claim is inferred.

Actual Falcon/fallback and fitness acquisition outcomes are recorded in the shared foundation logs; no failed provider output was fabricated. Existing genuine SsuB/SsuD reports remain discovery context. GOA files are annotation state, never biological support.

Focused schema, term, title and source-quote validation: valid with zero errors. Two panel advisories concern available but uncited genuine provider reports (SsuB/SsuD); independent primary/classification support is used rather than copying provider prose to silence them. All five helper histories and renders pass. No panel accession occurs in the cached GO-CAM index.
