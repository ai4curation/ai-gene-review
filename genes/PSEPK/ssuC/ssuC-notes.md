# ssuC curation notes

## Identity and pathway placement

- Q88R94 is PP_0239 in the contiguous KT2440 `ssuEADCB` locus. Its six
  predicted transmembrane helices and exact PANTHER subfamily identify the
  membrane unit of the binding-protein-dependent importer
  [file:PSEPK/ssuC/ssuC-uniprot.txt, "PTHR30151:SF38; ALIPHATIC SULFONATES
  TRANSPORT PERMEASE PROTEIN SSUC-RELATED"].
- The syntenic SsuA binding protein, SsuD oxygenase, SsuE reductase, and SsuB
  ATPase distinguish Q88R94 from related MetI-like permeases. Pseudomonas
  genetics identifies this locus as containing SsuABC [PMID:10781557, "an
  ATP-binding cassette-type transporter (ssuABC)"].
- E. coli SsuC P75851 is the explicit ISS comparator. E. coli deletion and
  complementation show that SsuABC and TauABC components are not functionally
  interchangeable [PMID:10781534, "the individual components of the two
  transport systems were not functionally exchangeable"].

## Research coverage

The completed OpenScientist process for `ssuC` did not materialize a report in
this worktree. No provider output was reconstructed or invented. Curation uses
the exact UniProt topology/family record, operon synteny, and cached ortholog-
system genetics.

## Residual uncertainty

No direct uptake assay was found for Q88R94. Its precise transported
alkanesulfonate spectrum remains an inference from the cognate cluster and
orthologous SsuABC systems.


## 2026-10-26 — independent member audit

Reassessed every existing annotation/proposal with unchanged term, evidence, reference, qualifier and donor fields. No new row was added. Family and role inference are separated from native target assays. The 2000 E. coli deletion study is available in a normal PMC URL cache; full S-313 PMID:10781557 exposes transporter redundancy and conditional SsuE dispensability. These are not KT2440 knockout results.

A fresh literature search found Garret William O'Connell's 2024 DTU thesis, chapter 1: native KT2440 ΔssuD and combined ΔssuBC growth tests, strain mapping, and Figure 4 were inspected. The chapter was a manuscript in preparation; a matching journal publication was not established. The experiments support target pathway placement but do not isolate individual B/C activities, or test individual A/E necessity. Composite growth fitness is not a direct import-rate measurement, and the source documents contamination concerns for some sulfur compounds. The full normal URL cache is in publications/. No direct target kinetic constants, expanded substrate spectrum or PFAS-degradation claim is inferred.

Actual Falcon/fallback and fitness acquisition outcomes are recorded in the shared foundation logs; no failed provider output was fabricated. Existing genuine SsuB/SsuD reports remain discovery context. GOA files are annotation state, never biological support.

Focused schema, term, title and source-quote validation: valid with zero errors. Two panel advisories concern available but uncited genuine provider reports (SsuB/SsuD); independent primary/classification support is used rather than copying provider prose to silence them. All five helper histories and renders pass. No panel accession occurs in the cached GO-CAM index.
