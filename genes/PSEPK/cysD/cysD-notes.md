# cysD curation notes

## First-pass synthesis

- Q88NA9 is a reviewed UniProt entry for sulfate adenylyltransferase subunit 2.
  The record assigns EC 2.7.7.4, CysN partnership, and sulfate + ATP -> APS +
  diphosphate [UniProtKB:Q88NA9, "With CysN forms the ATP sulfurylase (ATPS) that
  catalyzes the adenylation of sulfate producing adenosine
  5'-phosphosulfate"].
- A homologous Pseudomonas CysD/CysN complex has been biochemically and
  structurally characterized; GTP turnover by CysN is coupled to APS formation
  [PMID:16387658, "coupling the energy of GTP hydrolysis to APS formation"].
- The review therefore treats GO:0004781 and sulfate assimilation as core and
  the generic catalytic-activity annotation as over-annotated.

## Boundary decision

CysD belongs to the sulfate-to-sulfide pathway module. Sulfate import is
upstream, and cysteine synthesis from sulfide is downstream.


## Comparative sulfate-assimilation audit — 2026-10-26

Re-reviewed all four rows. Primary [PMID:16387658] characterizes P. syringae CysD/CysN, not a native KT2440 preparation. Conserved CysD sulfurylase chemistry supports ATP-dependent sulfate activation. The broad catalytic parent is refined, not treated as false. No universal holoenzyme stoichiometry is inferred from the interacting CysD/CysN unit.

Research provenance: parent already attempted Falcon (403) and Perplexity-lite (401 quota) for this batch; no generated report was fabricated. Existing PSEPK OpenScientist reports were used only as discovery. Source caches were fetched normally and never hand-edited. All original annotation payloads were preserved, with a retirement marker only for the existing CysI donor-specific NEW proposal.
