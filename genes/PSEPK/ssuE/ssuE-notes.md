# ssuE curation notes

## Identity and evidence

- Q88R97 is the reviewed PP_0236 SsuE-family NADPH-dependent FMN reductase at
  the start of the KT2440 `ssuEADCB` locus
  [file:PSEPK/ssuE/ssuE-uniprot.txt, "Belongs to the SsuE family"].
- Purified E. coli SsuE P80644 is the explicit ISS comparator and directly
  supplies reduced FMN to SsuD [PMID:10480865, "SsuE is the FMN reducing enzyme
  providing SsuD with FMNH(2)"].
- P. putida S-313 genetics provides both positive pathway evidence and an
  essentiality caveat: SsuE was needed for arylsulfonate growth but was
  dispensable for tested aliphatic sulfonates, implying an alternative
  reductase [PMID:10781557, "was needed for growth with arylsulfonates";
  "suggesting that an alternative isozyme exists"]. This is why the reusable
  module makes canonical SsuE-mediated FMNH2 supply optional while retaining
  the SsuD requirement for reduced FMN.

## Research coverage

The completed OpenScientist process for `ssuE` did not materialize a report in
this worktree. No provider output was reconstructed or invented. Curation uses
the exact reviewed UniProt record, the purified E. coli ortholog, and direct
Pseudomonas locus genetics.

## Localization

The reaction is expected in the cytoplasm, but the exact Q88R97 record has no
subcellular-location assertion and no target-specific localization experiment
was found. No GO cellular-component annotation was added.


## 2026-10-26 — independent member audit

Reassessed every existing annotation/proposal with unchanged term, evidence, reference, qualifier and donor fields. No new row was added. Family and role inference are separated from native target assays. The 2000 E. coli deletion study is available in a normal PMC URL cache; full S-313 PMID:10781557 exposes transporter redundancy and conditional SsuE dispensability. These are not KT2440 knockout results.

A fresh literature search found Garret William O'Connell's 2024 DTU thesis, chapter 1: native KT2440 ΔssuD and combined ΔssuBC growth tests, strain mapping, and Figure 4 were inspected. The chapter was a manuscript in preparation; a matching journal publication was not established. The experiments support target pathway placement but do not isolate individual B/C activities, or test individual A/E necessity. Composite growth fitness is not a direct import-rate measurement, and the source documents contamination concerns for some sulfur compounds. The full normal URL cache is in publications/. No direct target kinetic constants, expanded substrate spectrum or PFAS-degradation claim is inferred.

The apparent inverted SsuE CC growth requirement is recorded as a suspected transferred source defect; no native opposite phenotype is manufactured. Actual Falcon/fallback and fitness acquisition outcomes are recorded in the shared foundation logs; no failed provider output was fabricated. Existing genuine SsuB/SsuD reports remain discovery context. GOA files are annotation state, never biological support.

Focused schema, term, title and source-quote validation: valid with zero errors. Two panel advisories concern available but uncited genuine provider reports (SsuB/SsuD); independent primary/classification support is used rather than copying provider prose to silence them. All five helper histories and renders pass. No panel accession occurs in the cached GO-CAM index.

### PR 5593 source-audit follow-up (2026-10-26)

Recovered full-source citations now point to the unchanged local publication caches so supporting quotations are mechanically checked. The 2024 doctoral thesis is unpublished primary evidence: joint ΔssuBC results do not isolate B versus C, while ΔssuD tests D separately. No isolated A/E necessity or purified KT2440 kinetics is inferred. All original annotation payloads, actions and source-cache bytes are preserved.
