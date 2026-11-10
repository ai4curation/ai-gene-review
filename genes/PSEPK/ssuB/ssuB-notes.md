# ssuB curation notes

## Identity and ISS provenance

- Q88R93 is reviewed as the PP_0240 ATP-binding subunit of the KT2440 SsuABC
  importer [file:PSEPK/ssuB/ssuB-uniprot.txt, "Part of the ABC transporter
  complex SsuABC involved in"]. The record specifies an SsuB2-SsuC2-SsuA
  assembly [file:PSEPK/ssuB/ssuB-uniprot.txt, "The complex is composed of two
  ATP-binding proteins (SsuB)"].
- E. coli SsuB P0AAI1 is the explicit `supporting_entities` comparator on every
  ISS annotation. The conserved ABC transporter domain and ATP-binding feature
  support ATP binding/hydrolysis, while the syntenic `ssuEADCB` context supports
  alkanesulfonate specificity.
- GO:0005524 ATP binding is retained as a low-information `NEW` annotation but
  is not the core function. The informative biology is ATP hydrolysis coupled
  to contribution to GO:0042959, whose official QuickGO label includes the
  doubled word `transporter`.

## Research coverage

The completed OpenScientist report materialized at
`ssuB-deep-research-openscientist.md`. It correctly notes that direct
biochemical characterization of KT2440 SsuB itself has not been reported
[file:PSEPK/ssuB/ssuB-deep-research-openscientist.md, "Direct biochemical
characterization of the KT2440 SsuB protein itself has not been reported"].
Identifiers, motifs, complex composition, and central pathway claims were
independently checked against UniProt and cached primary literature.

## Residual uncertainty

Target-protein ATPase kinetics, stimulation by cognate SsuA/SsuC, and the exact
transported substrate range remain unmeasured.


## 2026-10-26 — independent member audit

Reassessed every existing annotation/proposal with unchanged term, evidence, reference, qualifier and donor fields. No new row was added. Family and role inference are separated from native target assays. The 2000 E. coli deletion study is available in a normal PMC URL cache; full S-313 PMID:10781557 exposes transporter redundancy and conditional SsuE dispensability. These are not KT2440 knockout results.

A fresh literature search found Garret William O'Connell's 2024 DTU thesis, chapter 1: native KT2440 ΔssuD and combined ΔssuBC growth tests, strain mapping, and Figure 4 were inspected. The chapter was a manuscript in preparation; a matching journal publication was not established. The experiments support target pathway placement but do not isolate individual B/C activities, or test individual A/E necessity. Composite growth fitness is not a direct import-rate measurement, and the source documents contamination concerns for some sulfur compounds. The full normal URL cache is in publications/. No direct target kinetic constants, expanded substrate spectrum or PFAS-degradation claim is inferred.

ATP binding is integral to SsuB energy coupling; earlier non-core wording was incorrect. Actual Falcon/fallback and fitness acquisition outcomes are recorded in the shared foundation logs; no failed provider output was fabricated. Existing genuine SsuB/SsuD reports remain discovery context. GOA files are annotation state, never biological support.

Focused schema, term, title and source-quote validation: valid with zero errors. Two panel advisories concern available but uncited genuine provider reports (SsuB/SsuD); independent primary/classification support is used rather than copying provider prose to silence them. All five helper histories and renders pass. No panel accession occurs in the cached GO-CAM index.

### PR 5593 source-audit follow-up (2026-10-26)

Recovered full-source citations now point to the unchanged local publication caches so supporting quotations are mechanically checked. The 2024 doctoral thesis is unpublished primary evidence: joint ΔssuBC results do not isolate B versus C, while ΔssuD tests D separately. No isolated A/E necessity or purified KT2440 kinetics is inferred. All original annotation payloads, actions and source-cache bytes are preserved.
